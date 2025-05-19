# pretty_print_xml.py
import xml.dom.minidom
import sys
import glob

def pretty_print(xml_file):
    with open(xml_file, encoding="utf-8") as f:
        xml_content = f.read()
    dom = xml.dom.minidom.parseString(xml_content)
    print(dom.toprettyxml())

if len(sys.argv) == 2:
    pretty_print(sys.argv[1])
else:
    for xml_file in glob.glob("testfiles/WMS_TMS_*.xml"):
        print(f"\n--- {xml_file} ---")
        pretty_print(xml_file)