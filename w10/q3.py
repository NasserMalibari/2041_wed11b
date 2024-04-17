#!/usr/bin/env python3

import sys

def main():

    for line in sys.stdin:
        if line[-1] == "\n":
            line = line[0:-1]
        
        chars = line
        newLine = ""
        for char in line:
            if (char in "aeiou"):
                char = char.upper()
            elif (char in "AEIOU"):
                char = char.lower()
            newLine += char
        print(newLine)
        # print(line)

        # 2 line solution
        # trans = str.maketrans("aeiouAEIOU", "AEIOUaeiou")
        # line = line.translate(trans)

if __name__ == "__main__":
    main()