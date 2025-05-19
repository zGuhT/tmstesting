import csv
import glob
import os
import sys
import xml.etree.ElementTree as ET
import xml.dom.minidom

testfiles_dir = "testfiles"
file_pattern = os.path.join(testfiles_dir, "tms_test_*.csv")
start_index = 100000

if len(sys.argv) != 2:
    print("Usage: python convert_csv.py <test_file_number>")
    sys.exit(1)

# Argument for which test file to process
try:
    test_file_num = int(sys.argv[1])
except ValueError:
    print("Argument must be an integer (e.g., 14)")
    sys.exit(1)

target_filename = os.path.join(testfiles_dir, f"tms_test_{test_file_num}.csv")
if not os.path.exists(target_filename):
    print(f"File {target_filename} not found.")
    sys.exit(1)

# List all previous files in order, only those numbered less than the chosen file
csv_files = sorted(
    glob.glob(file_pattern),
    key=lambda x: int(os.path.splitext(os.path.basename(x))[0].split('_')[-1])
)
previous_files = [f for f in csv_files if int(os.path.splitext(os.path.basename(f))[0].split('_')[-1]) < test_file_num]

# Count total rows in all previous files (excluding headers)
total_prior_rows = 0
for csv_file in previous_files:
    with open(csv_file, newline='', encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        total_prior_rows += sum(1 for _ in reader)

# Process the target file
with open(target_filename, newline='', encoding="utf-8") as f:
    reader = csv.reader(f)
    headers = next(reader)
    current_index = start_index + total_prior_rows
    row_num = 0
    for row in reader:
        file_id = current_index
        xml_file = f"WMS_TMS_{file_id}.xml"

        root = ET.Element("GenericDoc")
        ET.SubElement(root, "SenderID").text = "Komatsu"
        ET.SubElement(root, "ReceiverID").text = "TMS"
        ET.SubElement(root, "DocumentID").text = f"WMS_TMS_{file_id}"
        ET.SubElement(root, "ContentType").text = "text/plain"
        ET.SubElement(root, "Content")  # Placeholder

        row_data = "|".join(row)
        cdata_content = f"<![CDATA[{ '|'.join(headers) }\n{ row_data }\n]]>"

        xml_str = ET.tostring(root, encoding="unicode")
        if "<Content />" in xml_str:
            xml_str = xml_str.replace("<Content />", f"<Content>{cdata_content}</Content>")
        else:
            xml_str = xml_str.replace("<Content></Content>", f"<Content>{cdata_content}</Content>")

        xml_str = xml.dom.minidom.parseString(xml_str).toprettyxml(indent="  ")
        xml_path = os.path.join(testfiles_dir, xml_file)
        with open(xml_path, "w", encoding="utf-8") as out_f:
            out_f.write(xml_str)
        print(f"Generated XML file: {xml_path}")
        current_index += 1
        row_num += 1

if row_num == 0:
    print(f"Warning: {target_filename} has no data rows.")