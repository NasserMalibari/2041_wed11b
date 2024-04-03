#!/usr/bin/env python3

import sys

def main():

   # TODO: arg checking

    rows = int(sys.argv[1])
    cols = int(sys.argv[2])
    padding = int(sys.argv[3])

    for x in range(1, rows + 1):
        for y in range(1, cols + 1):
            print(f"{x * y:>{padding}}", end="")
        print()





if __name__ == "__main__":
    main()

