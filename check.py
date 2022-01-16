#!/usr/bin/env python3
import re

#TODO: work on regex , make write status , read from Client
class CheckStatus():
    def __init__(self):
        self.check_status()
    def check_status(self):
        with open("index.html","r") as f:
            origin = f.read()
            regex = re.sub(r"<.*?>",'', origin)
            print(regex)


if __name__ == "__main__":
    app = CheckStatus()
