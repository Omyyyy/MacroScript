import compiler
import sys
import os
import pycode
import time
import errors

def main():

    INFO = False

    if len(sys.argv) < 2:
        print("usage: macroscript.py <flags> <script>")
        sys.exit(1)
    args = sys.argv[1:][::-1]
    script = sys.argv[-1]
    if "-i" in args:
        INFO = True

    if not os.path.isfile(script):
        print(errors.Error("filenotfound", f"'{script}' not found", "<argv>").returnerror())
        sys.exit(1)

    with open(script, "r") as f:
        code = f.readlines()
        code = [x.rstrip() for x in code]
        linepos = 0
        for line in code:
            linepos += 1
            compiler.Compiler(line, linepos) if not line.isspace() and line != "\n" else None

    runstart = time.time()

    try:
        exec(pycode.pycode)

    except Exception:
        print(pycode.pycode)

    runend = time.time()

    print("execution took ", round(runend - runstart, 2), "s") if INFO else None

if __name__ == "__main__":
    main()
