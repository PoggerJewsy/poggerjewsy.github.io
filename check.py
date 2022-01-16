#!/usr/bin/env python3
import re
import sys

# read from Client


class CheckStatus():
    def __init__(self):
        self.parser()
    def check_status(self):
        with open("index.html","r") as f:
            origin = f.read()
            regex = re.sub(r"<.*?>",'', origin)
            return regex
    def parser(self):
        usage = """
        true - pass true if ready to execute
        false - pass false if ready to execute
        """
        if len(sys.argv) < 2:
            print (usage)
        elif sys.argv[1] == "True" or sys.argv[1] == "False":
            status = sys.argv[1].lower()
        status = sys.argv[1]
        return status
    def get_status(self, status):
        status = self.parser()
        with open("index.html", "w+") as f:
            f.write(f"<title>{status}</title>")
            f.close()
            return f"Status is {status}"

if __name__ == "__main__":
    app = CheckStatus()
    status = app.check_status()
    print(app.get_status(status))
