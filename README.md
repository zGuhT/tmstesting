# TMS Testing Utilities

## Overview

This repository is designed to streamline the creation, conversion, and management of test files for Komatsu Australia's TMS v2 workflow rules. It enables quick generation of valid XML documents from CSV templates, supporting automated and manual testing of our TMS and Freight Exchange system integrations.

---

## Repository Structure

```go
tmstesting/
├─ convert_csv_to_multiple_xml.py # Main Python script for conversion
├─ testfiles/
│ ├─ tms_template.csv # CSV template for creating test files
│ ├─ tms_test_1.csv # Example test input file (add more as needed)
│ ├─ ... # Additional test files
│ └─ WMS_TMS_*.xml # Generated XML files will appear here
├─ .gitignore
├─ README.md
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/zGuhT/tmstesting.git
cd tmstesting
```

### 2. Prepare Your Test Files

* Use testfiles/tms_template.csv as a base.
* For each test, create a new file named tms_test_#.csv in the testfiles folder (replace # with the next available number).
* Manually enter your test data, save the file.

### 3. Run the Conversion Script

* Make sure you have Python 3 installed.
* From the project root, run the script with the number of the test file you want to convert. For example, to process tms_test_2.csv:

```bash
python convert_csv_to_multiple_xml.py 2
```

* This will generate XML files for each row in the specified test CSV. The files will be named WMS_TMS_<file_id>.xml and saved in the testfiles folder.
* The <file_id> is automatically incremented to avoid duplicates across all your test cases.

### 4. Review the Output

* Open the generated XML files in the testfiles folder.
* Use these files to test workflow rules and integrations in TMS v2 and Freight Exchange.

---

## Why This Exists

This repository helps automate repetitive test creation, making it faster and safer to validate changes or new rules in the TMS v2 workflow and Freight Exchange system. It also reduces the risk of duplicate file IDs when multiple team members are testing.

---

## License

This repository is for internal testing and development at Komatsu Australia.

```yaml
**You can copy-paste this directly into your `README.md`!**  
Let me know if you want a more technical/less technical version, or if you want to mention specific rules or test cases in the description.
```