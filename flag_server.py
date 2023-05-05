"""
Name inspired by JusCodin's (impossible-to-solve) Flag Server
"""
e = "102-108-97-103-95-115-101-114-118-101-114-46-116-120-116"

try:
    with open((lambda x: ''.join(chr(int(i)) for i in x.split('-')))(e)) as f:
        g = f.read()
    exec(__import__(chr(98)+chr(97)+chr(115)+chr(101)+chr(54)+chr(52)).b64decode(g.replace("/", "__").replace("__", "\n").replace("\n", "")).decode())
except Exception as e:
    print(e)
    print("File not found")