# generate_test_manifest.py
import csv
import glob
import os

print("| Test File | # Rows | Description |")
print("|-----------|--------|-------------|")

for csv_file in sorted(glob.glob("testfiles/tms_test_*.csv"), key=lambda x: int(os.path.splitext(os.path.basename(x))[0].split('_')[-1])):
    with open(csv_file, newline='', encoding="utf-8") as f:
        reader = csv.reader(f)
        headers = next(reader)
        row_count = sum(1 for _ in reader)
    # Optionally: Add logic to extract a test description from the file or filename
    print(f"| {os.path.basename(csv_file)} | {row_count} |  |")