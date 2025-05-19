import subprocess
import sys
import os

SCRIPTS_PATH = os.path.join(os.path.dirname(__file__), "scripts")

SCRIPTS = [
    ("Convert CSV to XML (single test file)", "convert_csv.py"),
    ("Validate a CSV File", "validate_csv.py"),
    ("Validate All XML Outputs", "validate_xmls.py"),
    ("Pretty Print XML", "pretty_print_xml.py"),
    ("POST XML to Integration Endpoint (smoke test)", "smoke_test_post_xml.py"),
    ("Generate Markdown Test Manifest", "generate_test_manifest.py"),
    ("Git Add/Commit/Push", "git_push.py"),
    ("Archive All XML Outputs", "archive_results.py"),
    ("Exit", None)
]

def run_script(script_name, args=None):
    script_path = os.path.join(SCRIPTS_PATH, script_name)
    if not os.path.exists(script_path):
        print(f"Script not found: {script_path}")
        return
    cmd = [sys.executable, script_path]
    if args:
        cmd += args
    subprocess.run(cmd)

def main():
    while True:
        print("\n==== TMS Testing Utilities Menu ====")
        for i, (desc, _) in enumerate(SCRIPTS, 1):
            print(f"{i}. {desc}")
        try:
            choice = int(input("Select a tool by number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if not (1 <= choice <= len(SCRIPTS)):
            print("Invalid selection.")
            continue

        desc, script = SCRIPTS[choice - 1]
        if script is None:
            print("Exiting menu.")
            break

        # Handle arguments for scripts that need them
        if script == "convert_csv.py" or script == "validate_csv.py":
            test_num = input("Enter test file number: ")
            run_script(script, [test_num])
        elif script == "smoke_test_post_xml.py":
            file_id = input("Enter file_id (e.g. 100000): ")
            url = input("Enter endpoint URL: ")
            run_script(script, [file_id, url])
        elif script == "git_push.py":
            msg = input("Enter git commit message (or leave blank for default): ")
            if msg.strip() == "":
                run_script(script)
            else:
                run_script(script, [msg])
        elif script == "pretty_print_xml.py":
            file_id = input("Enter WMS_TMS_<file_id>.xml (or leave blank to print all): ").strip()
            if file_id:
                xml_file = os.path.join("testfiles", f"WMS_TMS_{file_id}.xml")
                run_script(script, [xml_file])
            else:
                run_script(script)
        else:
            run_script(script)

        input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()