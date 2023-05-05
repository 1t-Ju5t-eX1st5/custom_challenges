"""
Name inspired by JusCodin's (impossible-to-solve) Flag Server
"""
e = "MTAyLTEwOC05Ny0xMDMtOTUtMTE1LTEwMS0xMTQtMTE4LTEwMS0xMTQtNDYtMTE2LTEyMC0xMTY="

try:
    with open((lambda x: ''.join(chr(int(i)) for i in x.split('-')))(__import__(chr(98)+chr(97)+chr(115)+chr(101)+chr(54)+chr(52)).b64decode(e).decode())) as f:
        g = f.read()
    exec(__import__(chr(98)+chr(97)+chr(115)+chr(101)+chr(54)+chr(52)).b64decode(g.replace("/", "__").replace(".", "\n").replace("\n", "__").replace("__", "")).decode())
except Exception as e:
    print(e)
    print("File not found")