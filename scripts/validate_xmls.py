# validate_xmls.py
import glob
import xml.etree.ElementTree as ET

failures = 0
for xml_file in glob.glob("testfiles/WMS_TMS_*.xml"):
    try:
        ET.parse(xml_file)
    except Exception as e:
        print(f"Invalid XML: {xml_file} - {e}")
        failures += 1
if failures == 0:
    print("All XML files are well-formed!")
else:
    print(f"{failures} file(s) had XML errors.")