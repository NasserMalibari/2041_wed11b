#!/usr/bin/env python3

import sys, re, subprocess

def main():


    # get the webpage
    process = subprocess.run(f"wget -O- -q  {sys.argv[1]}",
                              shell=True, capture_output=True, text=True)
    

    output = process.stdout
    # print(process.stdout)
    # subprocess.run(["wget", "-O-", ..])

    # find all phone numbers
    numbers = re.findall(r"[0-9 -]+", output)
    for number in numbers:
        # remove non-numbers
        number = re.sub(r"[- ]","",number)
        number = number.strip()
        if len(number) <= 15 and len(number) >= 8:
            print(number)

if __name__ == "__main__":
    main()