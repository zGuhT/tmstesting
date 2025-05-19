# smoke_test_post_xml.py
import requests
import sys
import os

if len(sys.argv) != 3:
    print("Usage: python smoke_test_post_xml.py <file_id> <url>")
    sys.exit(1)

xml_file = f"testfiles/WMS_TMS_{sys.argv[1]}.xml"
url = sys.argv[2]

with open(xml_file, "rb") as f:
    xml_data = f.read()

response = requests.post(url, data=xml_data, headers={"Content-Type": "application/xml"})
print(f"Response ({response.status_code}):\n{response.text}")