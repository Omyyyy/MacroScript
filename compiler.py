import pycode

class Compiler:
    def __init__(self, line: str):

        self.line = line

        if line.startswith("#"):
            return
        
        if ":" in line:
            self.cmd = line.split(":")[0].rstrip()
            self.args = line.split(":")[1].strip()

        else:
            self.cmd = line.rstrip()
            self.args = ""

        self.compile()

    def compile(self):
        ind = " " * (len(self.line) - len(self.line.lstrip()))

        match self.cmd:
            case "log":
                pycode.pycode += ind + f"print({self.args})\n"
            
            case "error":
                pycode.pycode += ind + f"print(Fore.RED + {self.args} + Fore.RESET)\nexit()\n"

            case "warning":
                pycode.pycode += ind + f"print(Fore.YELLOW + {self.args} + Fore.RESET)\n"

            case "wait":
                pycode.pycode += ind + f"time.sleep(float({self.args}))\n"

            case "click":
                if self.args == "":
                    pycode.pycode += ind + f"pyautogui.click()\n"
                else:
                    lenargs = len(self.args.split(","))
                    if lenargs == 1:
                        pycode.pycode += ind + f"pyautogui.click(clicks={self.args})\n"

                    elif lenargs == 2:
                        pycode.pycode += ind + f"pyautogui.click(x={self.args.split(',')[0].strip()}, y={self.args.split(',')[1].strip()})\n"

                    elif lenargs == 3:
                        pycode.pycode += ind + f"pyautogui.click(x={self.args.split(',')[0].strip()}, y={self.args.split(',')[1].strip()}, clicks={self.args.split(',')[2].strip()})\n"