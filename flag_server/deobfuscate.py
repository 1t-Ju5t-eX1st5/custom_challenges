with open("flag_server.txt") as _:
    with open("flag_server.py", "w") as __:
        __.write(__import__("base64").b64decode(_.read().encode()).decode())
        __import__("os").remove("flag_server.txt")
