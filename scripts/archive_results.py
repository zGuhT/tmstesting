# archive_results.py
import os
import glob
import shutil
import datetime

archive_dir = f"testfiles/archive_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
os.makedirs(archive_dir)

for f in glob.glob("testfiles/WMS_TMS_*.xml"):
    shutil.move(f, archive_dir)
print(f"All XMLs moved to {archive_dir}/")