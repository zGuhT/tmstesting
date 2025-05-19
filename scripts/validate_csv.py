# validate_csv.py
import csv
import sys
import os

if len(sys.argv) != 2:
    print("Usage: python validate_csv.py <test_number>")
    sys.exit(1)

file_num = sys.argv[1]
csv_path = os.path.join("testfiles", f"tms_test_{file_num}.csv")

if not os.path.exists(csv_path):
    print(f"{csv_path} not found.")
    sys.exit(1)

required_headers = ["Col1", "Col2", "Col3"]  # Replace with your real headers

with open(csv_path, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    headers = next(reader)
    missing_headers = [h for h in required_headers if h not in headers]
    if missing_headers:
        print(f"Missing required headers: {missing_headers}")
    for i, row in enumerate(reader, start=2):
        if len(row) != len(headers):
            print(f"Row {i}: Length mismatch ({len(row)} vs {len(headers)})")
        for j, cell in enumerate(row):
            if cell.strip() == "":
                print(f"Row {i}, Column '{headers[j]}': Empty cell")
print("CSV validation complete.")