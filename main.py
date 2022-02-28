import sys
import os

stack = [0]*3000
pointer = 0

KEYWORDS = ("MIPS", "BONK", "Kap", "pa", "!")

class SynkapError(Exception):
    def __init__(self, line, word):
        self.line = line
        self.word = word

    def __str__(self):
        return f"Error is on line {self.line}, {self.word}"

def parse(path):
    """Parse file at path."""
    global stack, pointer
    with open(path, 'r') as file:
        lines = file.readlines()

    for index, line in enumerate(lines):
        words = line.split(" ")

        if words[0].strip("\n") == '//':
            # count double fowardslash as comment
            continue

        elif len(words) == 1 and words[0] == '\n':
            # removes empty lines
            continue

        for word in words:
            word = word.strip("\n")
            if word == '':
                continue

            if word == KEYWORDS[0]:
                # mips - increment current cell
                stack[pointer] = stack[pointer] + 1
            elif word == KEYWORDS[1]:
                # bonk - decrement current cell
                stack[pointer] = stack[pointer] - 1
            elif word == KEYWORDS[2]:
                # kap - move pointer left one
                pointer = pointer - 1
                if pointer == -1:
                    pointer = 0
            elif word == KEYWORDS[3]:
                # pa - move pointer right one
                pointer = pointer + 1
                if pointer == 3000:
                    pointer = 2999
            elif word == KEYWORDS[4]:
                # ! - output current cell as ascii to stdout
                cell = stack[pointer]
                try:
                    out = chr(cell)
                except ValueError:
                    continue
                sys.stdout.write(out)
            else:
                # raise syntaxerror
                raise SynkapError(index+1, word)

def main():
    """Open file from command line."""
    args = sys.argv
    try:
        file = args[1]

        if not file.endswith(".mbkappa"):
            raise IndexError

        file_path = f"./{file}"
        if not os.path.exists(file_path):
            raise IndexError

    except IndexError:
        print("run .mbkappa file")
        return
    
    parse(file_path)

    

if __name__ == "__main__":
    main()