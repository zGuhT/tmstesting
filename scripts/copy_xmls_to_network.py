import shutil
import glob
import os

# Source and destination paths
source_dir = os.path.join(os.path.dirname(__file__), "..", "testfiles")
destination_dir = r"\\komatsu.aus\ESBINT-MFT\Active Transfer\KWMS\TMS\in"

# Ensure destination exists
if not os.path.exists(destination_dir):
    print(f"Destination folder does not exist:\n{destination_dir}\n\nMake sure you have network access.")
    exit(1)

# Find all XML files in testfiles folder
xml_files = glob.glob(os.path.join(source_dir, "WMS_TMS_*.xml"))

if not xml_files:
    print("No XML files found to copy.")
else:
    for file in xml_files:
        try:
            shutil.copy(file, destination_dir)
            print(f"Copied: {os.path.basename(file)}")
        except Exception as e:
            print(f"Failed to copy {os.path.basename(file)}: {e}")

    print(f"\nDone. {len(xml_files)} file(s) copied to:\n{destination_dir}")