import pycode
import errors
import sys

class Compiler:
    def __init__(self, line: str, linepos: int, filename: str):

        self.line = line
        self.linepos = linepos
        self.filename = filename

        if line.startswith("#"):
            return
        
        if ":" in line:
            self.cmd = line.split(":", 1)[0].strip()
            self.args = line.split(":", 1)[1].strip()

        else:
            self.cmd = line.strip()
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

            case "open":
                pycode.pycode += ind + f"webbrowser.open({self.args})\n"

            case "setdelay":
                pycode.pycode += ind + f"pydirectinput.PAUSE = float({self.args})\n"

            case "var" | "variable":
                varname = self.args.split("=")[0].strip()
                varvalue = self.args.split("=")[1].strip()
                if varvalue == "clipboard":
                    varvalue = "pyperclip.paste()"

                elif varvalue == "xposition":
                    varvalue = "pydirectinput.position()[0]"

                elif varvalue == "yposition":
                    varvalue = "pydirectinput.position()[1]"

                pycode.pycode += ind + f"{varname} = {varvalue}\n"

            case "copy":
                pycode.pycode += ind + f"pyperclip.hotkey('ctrl', 'c')\n"

            case "click":
                if self.args == "":
                    pycode.pycode += ind + f"pydirectinput.click()\n"
                else:
                    lenargs = len(self.args.split(","))
                    if lenargs == 1:
                        pycode.pycode += ind + f"pydirectinput.click(clicks={self.args})\n"

                    elif lenargs == 2:
                        pycode.pycode += ind + f"pydirectinput.click(x={self.args.split(',')[0].strip()}, y={self.args.split(',')[1].strip()})\n"

                    elif lenargs == 3:
                        pycode.pycode += ind + f"pydirectinput.click(x={self.args.split(',')[0].strip()}, y={self.args.split(',')[1].strip()}, clicks={self.args.split(',')[2].strip()})\n"

                    else:
                        print(errors.Error("argumenterror", "'click' only takes a max of three values after the command'", self.filename, self.linepos).returnerror())
                        sys.exit(1)


            case "rightclick":
                if self.args == "":
                    pycode.pycode += ind + f"pydirectinput.click(button='right')\n"
                else:
                    lenargs = len(self.args.split(","))
                    if lenargs == 1:
                        pycode.pycode += ind + f"pydirectinput.click(clicks={self.args}, button='right')\n"

                    elif lenargs == 2:
                        pycode.pycode += ind + f"pydirectinput.click(x={self.args.split(',')[0].strip()}, y={self.args.split(',')[1].strip()}, button='right')\n"

                    elif lenargs == 3:
                        pycode.pycode += ind + f"pydirectinput.click(x={self.args.split(',')[0].strip()}, y={self.args.split(',')[1].strip()}, clicks={self.args.split(',')[2].strip()}, button='right')\n"

                    else:
                        print(errors.Error("argumenterror", "'rightclick' only takes a max of three values after the command'", self.filename, self.linepos).returnerror())
                        sys.exit(1)
                        
            case "type":
                pycode.pycode += ind + f"pydirectinput.typewrite(str({self.args}))\n"

            case "move":
                pycode.pycode += ind + f"pydirectinput.moveTo({self.args})\n"

            case "press":
                pycode.pycode += ind + f"pydirectinput.press({self.args})\n"

            case "hold":
                pycode.pycode += ind + f"pydirectinput.keyDown({self.args})\n"

            case "release":
                pycode.pycode += ind + f"pydirectinput.keyUp({self.args})\n"

            case "if":
                pycode.pycode += ind + f"if {self.args}:\n"

            case "unless":
                pycode.pycode += ind + f"if not {self.args}:\n"

            case "elif":
                pycode.pycode += ind + f"elif {self.args}:\n"

            case "else":
                if self.args == "":
                    pycode.pycode += ind + f"else:\n"

                else:
                    print(errors.Error("argumenterror", "'else' does not need any values after the command;", self.filename, self.linepos).returnerror())
                    sys.exit(1)

            case "while":
                pycode.pycode += ind + f"while {self.args}:\n"

            case "for":
                pycode.pycode += ind + f"for {self.args}:\n"

            case "until":
                pycode.pycode += ind + f"while not {self.args}:\n"

            case "exit":
                if self.args == "":
                    pycode.pycode += ind + f"exit()"
                
                else:
                    print(errors.Error("argumenterror", "'exit' does not need any values after the command;", self.filename, self.linepos).returnerror())