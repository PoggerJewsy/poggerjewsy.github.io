#!/usr/bin/env python3
import re

class CheckStatus():
    def __init__(self):
        self.check_status()
    def check_status(self):
        with open("index.html","r") as f:
            origin = f.read()
            #TODO: work on regex , make write status , read from Client
            regex = re.findall(r"^(?\<code>)\w*", origin)
            print(regex)


if __name__ == "__main__":
    app = CheckStatus()
