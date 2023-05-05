#############################################################################################
# A little CTF challenge that I made to try out some obfuscation methods that I saw from    #
# Youtube...                                                                                #
#                                                                                           #
# Name inspired by JusCodin's (impossible to decipher) Flag Server challenge                #
#############################################################################################

"""
TODO:
- Prevent code from executing bytecode - JusCodin (wtf do you mean by that...)
- Turn it into an actual "server" of sorts using Flask (?)
- MOAR OBFUSCATION!!!!!
"""

e = "MTAyLTEwOC05Ny0xMDMtOTUtMTE1LTEwMS0xMTQtMTE4LTEwMS0xMTQtNDYtMTE2LTEyMC0xMTY="

def a1():
    try:
        with open((lambda x: ''.join(chr(int(i)) for i in x.split('-')))(__import__(chr(98)+chr(97)+chr(115)+chr(101)+chr(54)+chr(52)).b64decode(e).decode())) as f:
            g = f.read()
        exec(__import__(chr(98)+chr(97)+chr(115)+chr(101)+chr(54)+chr(52)).b64decode(g.replace("/", "__").replace(".", "\n").replace("\n", "__").replace("__", "")).decode())
    except Exception as e:
        print(e)
        print("File not found")

def a2():
    """
    Experimenting with self-encoding... it destroys itself but it's a small price to pay for salvation
    """
    self_code = open(__file__).read().encode("ascii")
    encoded_selfcode = __import__("base64").b64encode(self_code)
    with open("src/rebuild.txt", "w") as __:
        __.write(encoded_selfcode.decode()) 
    with open(__file__.replace("py", "txt"), "w") as f:
        f.write(encoded_selfcode.decode())
        __import__("os").remove(__file__)

def rebuild_self():
    """
    KILLER QUEEN DAISA-NO BAKUDAN, BITES ZA DUSTO
    """
    with open("src/rebuild.txt") as __:
        rebuild = __.read().encode()
        with open(__file__, "w") as _:
            _.write(__import__("base64").b64decode(rebuild).decode())

a2()