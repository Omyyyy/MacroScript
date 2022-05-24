from colorama import Fore

class Error:
    def __init__(self, errorname, errorinfo, line):
        self.errorname = errorname
        self.errorinfo = errorinfo
        self.line = line

    def returnerror(self):
        return Fore.RED + f"error: {self.errorname} on line {self.line}: {self.errorinfo}" + Fore.RESET
