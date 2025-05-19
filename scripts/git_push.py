# git_push.py
import subprocess
import sys

msg = "Update test cases"
if len(sys.argv) > 1:
    msg = " ".join(sys.argv[1:])

subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", msg])
subprocess.run(["git", "push"])