#!/usr/bin/env python3

import sys, re

def line_matches(address, line, line_num):
    "line_matches('3', 'hello', 3) -> True"
    "line_matches('/h[ae]llo/', 'hello', 42) -> True"

    if (re.fullmatch(r"\d+", address)):
        return int(address) == line_num
    elif (re.fullmatch(r"/.*/", address)):
        # get the regex part
        regex = address[1:-1]

        return bool(re.search(regex, line))
        # return re.search(...) != None
        # return False

    return False

def main():
    address = sys.argv[1]

    for line_num, line in enumerate(sys.stdin, start=1):
        if line[-1] == "\n":
            line = line[0:-1]
            # line.rstrip('\n')

        print(line)
        if line_matches(address, line, line_num):
            sys.exit(0)
        #     quit


if __name__ == "__main__":
    main()