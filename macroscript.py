import compiler
import sys
import os
import pycode
import time

def main():

    INFO = False

    JUSTPRINTCOMPILED = False

    if len(sys.argv) < 2:
        print("Usage: macroscript.py <script>")
        sys.exit(1)
    args = sys.argv[1:][::-1]
    script = sys.argv[-1]
    if "-i" in args:
        INFO = True

    if "-p" in args:
        JUSTPRINTCOMPILED = True

    if not os.path.isfile(script):
        print("error: file not found:", script)
        sys.exit(1)

    with open(script, "r") as f:
        code = f.readlines()
        code = [x.rstrip() for x in code]
        for line in code:
            compiler.Compiler(line) if not line.isspace() and line != "\n" else None

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