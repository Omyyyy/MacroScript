import pycode

class Compiler:
    def __init__(self, line: str):

        self.line = line

        if line.startswith("#"):
            return
        
        if ":" in line:
            self.cmd = line.split(":")[0].lstrip()
            self.args = line.split(":")[1].strip()

        else:
            self.cmd = line.rstrip()
            self.args = ""

        self.compile()

    def compile(self):
        ind = " " * (len(self.line) - len(self.cmd.rstrip()))

        match self.cmd:
            case "log":
                pycode.pycode += ind + f"print({self.args})\n"
            
            case "error":
                pycode.pycode += ind + f"print(red({self.args}))\nexit()\n"