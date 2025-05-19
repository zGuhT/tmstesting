# TMS Testing Utilities

## Overview

This repository streamlines the creation, conversion, validation, and management of test files for Komatsu Australia's TMS v2 workflow rules. It enables rapid generation and automated handling of valid XML documents from CSV templates, supporting robust testing of our TMS and Freight Exchange system integrations. A toolkit launcher and modular utility scripts make testing, regression, and workflow validation efficient and repeatable.

---

## Repository Structure

```go
tmstesting/
├─ scripts/
│ ├─ archive_results.py # Moves XML test results to an archive folder
│ ├─ convert_csv.py # Converts a specified test CSV to XML(s)
│ ├─ generate_test_manifest.py # Generates a markdown manifest of test cases
│ ├─ git_push.py # Automates git add/commit/push with a message
│ ├─ pretty_print_xml.py # Formats XML for human-readable review
│ ├─ smoke_test_post_xml.py # Sends XMLs to an API endpoint for integration tests
│ ├─ validate_csv.py # Checks CSVs for formatting and data issues
│ ├─ validate_xmls.py # Checks that all generated XMLs are well-formed
├─ testfiles/
│ ├─ tms_template.csv # CSV template for creating test files
│ ├─ tms_test_1.csv # Example test input file (add more as needed)
│ ├─ ... # Additional test files
│ └─ WMS_TMS_*.xml # Generated XML files will appear here
├─ .gitignore
├─ README.md
├─ tms_toolkit_launcher.py # Interactive menu for running utility scripts
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

### 3. Run the Toolkit Launcher

* Make sure you have Python 3 installed.
* From the project root, launch the toolkit:

```bash
python tms_toolkit_launcher.py
```

* Select a tool from the interactive menu.
* The toolkit will prompt for required arguments (such as test file number, file ID, or endpoint URL) as needed.

### 4. Review and Use Outputs

* Generated XML files will appear in testfiles/ with the format WMS_TMS_<file_id>.xml.
* Use these files to test workflow rules and integrations in TMS v2 and Freight Exchange.
* Use other scripts to validate, pretty-print, archive, or manage test files.

---

## Utility Scripts Included

* archive_results.py – Move all generated XMLs into an archive folder (for result management).
* convert_csv.py – Convert a single specified test CSV to one or more XMLs (per row).
* generate_test_manifest.py – Summarize test cases in a markdown table.
* git_push.py – Quickly stage, commit, and push changes with a custom message.
* pretty_print_xml.py – Print formatted XML to the console for easy review.
* smoke_test_post_xml.py – POST a selected XML file to an endpoint for integration/smoke testing.
* validate_csv.py – Check CSVs for missing headers, empty fields, or malformed rows.
* validate_xmls.py – Check all XMLs in testfiles/ for well-formedness.

---

## Why This Exists

This repository helps automate repetitive test creation, validation, and system integration checks, making it faster and safer to validate changes or new rules in the TMS v2 workflow and Freight Exchange system. It reduces the risk of duplicate file IDs, increases repeatability, and accelerates debugging and regression testing for all team members.

---

## Version History / Change Log

### v1.1 (2024-05-19)

* Added interactive toolkit launcher (tms_toolkit_launcher.py) for menu-driven access to all test scripts.
* Moved utility scripts into a /scripts subfolder for better organization.
* Added CSV and XML validation scripts (validate_csv.py, validate_xmls.py).
* Added pretty print and manifest generation tools for easier review.
* Introduced result archiving, git automation, and smoke test posting utilities.
* README.md and .gitignore updated to reflect new structure and workflows.

### v1.0 (2024-05-17)

* Initial project setup for conversion of test CSVs to XML using convert_csv_to_multiple_xml.py.
* Added template and example test files.
* Provided documentation for manual test creation and XML usage.

---

## License

This repository is for internal testing and development at Komatsu Australia.

```yaml
**You can copy-paste this directly into your `README.md`!**  
Let me know if you want a more technical/less technical version, or if you want to mention specific rules or test cases in the description.
```