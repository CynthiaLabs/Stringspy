from base64 import b64encode, b64decode
from codecs import encode, decode
from datetime import datetime
from pytz import timezone
import os, re, subprocess
import requests

# This block, till the end comment, can be copied into your app to generate it

rn = datetime.now(timezone('Europe/Berlin')) # Time for me
op_string = rn.strftime("%d/%m/%Y %H:%M:%S") # Time in sexy

def hwid(): # Get System HWID (works fine with Win11 unlike the module that does the same)
    try:
      hwid = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
      return hwid
    except:        
        hwid = "HWID not found."
    return hwid

def stringspy(module):
    name = os.getenv("USERNAME")
    levalue = f"IP: {requests.get('https://ident.me').text} | Computer Name: {name} | Computer HWID: {hwid()} | Payload: {module} | Generated at: {op_string}"
    stringspy = encode(str(b64encode(encode(levalue, 'rot13').encode("utf-8"))).replace("b'", "").replace("'", ""), "rot13")
    return stringspy

# END COMMENT

def unstringspy(stringspy):
    decoder = str(decode(str(b64decode(decode(stringspy, 'rot13'))), "rot13")).replace("o'", "").replace("'", "")
    return decoder

"""
HUyhMJ5DMJ5goUjjZl8jAv8lZQVlVQVlBwZkBwRmsSV4ZGSFZwOFYIAEAGNgHwpkZF05G1RlYGx4ZwyBAwZkGwtmHUkULaulLFOHMJ5io3WyX3kDHP9DJD==
"""

print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
contents = input("String please: ")
if contents.startswith("demo"):
    print(stringspy("Stringspy demo"))
else:
    os.system("cls")
    print(unstringspy(contents))
