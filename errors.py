from colorama import Fore

class Error:
    def __init__(self, errorname, errorinfo, errorfile, line):
        self.errorname = errorname
        self.errorinfo = errorinfo
        self.errorfile = errorfile
        self.line = line

    def returnerror(self):
        return Fore.RED + f"in {self.errorfile}:\n\terror: {self.errorname} on line {self.line}: {self.errorinfo}" + Fore.RESET
