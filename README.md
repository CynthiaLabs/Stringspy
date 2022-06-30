# Stringspy
File Fingerprinting made easy written by ClaraCrazy

Stringspy is a super-small custom module that can be used to generate fingerprints of files, for example when generating payloads etc.
The payload-builder can contain the following code to generate an ID:

```py
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
```
which will generate a string like this: `IxZ6VQx1YwRkBP43Av4lZwLtsPODLacwnTqlMFOOoaclBvODrJ5yoyOyoz1fVUjtHTW6L2uapzHtIHcJHGbtHwtkZIVlZSVgH1R1ZP1FAmRkYGyCHGVgBGtlBH42ZmSBBQADVUjtD25frJWhpGbtEzqyqzS0MzAfVUSlrzVtsPOHpzSlMJ5apaRtozp6VQZjYmN2YmVjZwVtZQp6AQV6AGp=`


This string can then be attached to the file and later decrypted to return a healthy amount of info about the built payload: `IP: 95.118.76.XXX | Computer Name: ClaraCrazy | Computer HWID: E811E20E-FD50-E711-9BD2-9829A631A83C | Payload: Stringspy demo | Generated at: 30/06/2022 07:42:57`

the function for that looks like this:
```py
def unstringspy(stringspy):
    decoder = str(decode(str(b64decode(decode(stringspy, 'rot13'))), "rot13")).replace("o'", "").replace("'", "")
    return decoder
```
