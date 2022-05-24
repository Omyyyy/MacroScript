# MacroScript
A simple scripting language for writing macros 

# Installation
Clone the repo: 

> git clone https://github.com/Omyyyy/MacroScript.git

# CLI

> Usage: python3 macroscript.py (flags) \[script\]

All flags:
+ -i: Print out additional info about compilation and runtime, such as time taken. Defaults to off.
+ -p: Instead of running the macro, print all the compiled Python code for whatever reason. Defaults to off.

# Commands

Info: '[]' denotes any mandatory arguments, while '()' denotes optional ones

### Writing stuff to the terminal:
>1. log: \[expression\] - Prints the specified expression to the screen.
>2. warning: \[expression\] - Prints the specified expression in yellow in order to 'warn' the user.
>3. error: \[expression\] - Prints the specified expression in red and exits the program.

### Time related
>1. wait: \[seconds\] - Halts execution for specified number of seconds. Accepts decimals.
>2. setdelay: \[seconds\] - Sets delay between each macro action to specified value. Accepts decimals.

### Mouse macro commands:
>1. click: (x position), (y position, (number of clicks) - Emulates a mouse click. x position and y position defaults to current mouse position, and number of clicks defaults to 1. Simply use 'click' to use all of the defaults.
>2. rightclick: (x position), (y position, (number of clicks) - Emulates a right mouse click. x position and y position defaults to current mouse position, and number of clicks defaults to 1. Simply use 'rightclick' to use all of the defaults.
>3. move: \[x position\], \[y position\] - Moves the cursor to specified coordinates.

### Keyboard macro commands:
>1. type: \[expression\] - Emulates typing the specified expression.
>2. press: \[key\] - Emulates a key press of the specified key.
>3. hold: \[key\] - Holds down the specified key.
>4. release: \[key\] - Releases the key that is held. Does nothing if no key is held.
>5. copy - Emulates the CTRL+C shortcut. Just type the word, no arguments are needed.

### Logic / Conditionals
>1. if: \[condition\] \[codeblock\] - Regular if statement, like in all programming languages. Indent the block on the next line (like Python).
>2. elif: \[condition\] \[codeblock\] - Regular elif/else if statement, like in all programming languages. Indent the block on the next line (like Python).
>3. else - Regular else statement, like in all programming languages. Indent the block on the next line (like Python) and do not specify any arguments
>4. unless: \[condition\] \[codeblock\] - Regular if statement, except the code block is only executed if the specified condition is false. Indent the block on the next line (like Python).

### Loops
>1. while: \[condition\] \[codeblock\] - Regular while loop, like in all programming languages. Indent the block on the next line (like Python).
>2. for: \[varname\] in \[iterable object\] - For loop just like in Python. Indent the block on the next line (like Python).
>3. until: \[condition\] \[codeblock\] - Regular while loop, except the loop is executed until the specified condition is true. Indent the block on the next line (like Python).

### Other
>1. exit - Exits the program. Does not require arguments.