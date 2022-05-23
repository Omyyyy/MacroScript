import compiler
import sys
import os
import pycode
import time
import errors

def main():

    INFO = False

    JUSTPRINTCOMPILED = False

    if len(sys.argv) < 2:
        print("usage: macroscript.py <flags> <script>")
        sys.exit(1)
    args = sys.argv[1:][::-1]
    script = sys.argv[-1]
    if "-i" in args:
        INFO = True

    if "-p" in args:
        JUSTPRINTCOMPILED = True

    if not os.path.isfile(script):
        print(errors.Error("filenotfound", f"'{script}' not found", "<argv>").returnerror())
        sys.exit(1)

    with open(script, "r") as f:
        code = f.readlines()
        code = [x.rstrip() for x in code]
        linepos = 0
        for line in code:
            linepos += 1
            compiler.Compiler(line, linepos, script) if not line.isspace() and line != "\n" else None

    runstart = time.time()

    try:
        exec(pycode.pycode) if not JUSTPRINTCOMPILED else print(pycode.pycode)

    except Exception as e:
        print(f"error: {e}")
        exit()

    runend = time.time()

    print(f"info: execution took {round(runend - runstart, 2)}s") if INFO else None

if __name__ == "__main__":
    main()
