#! /usr/bin/env python3

import re, subprocess
from collections import Counter
from argparse import ArgumentParser
import q4



def main():

    parser = ArgumentParser()
    parser.add_argument('-f', '--frequency', action='store_true', help='print tags by frequency')
    parser.add_argument("url", help="url to fetch")
    args = parser.parse_args()

    process = subprocess.run(["wget", "-q", "-O-", args.url],
                             capture_output=True, text=True)
    
    output = process.stdout
    # print(output)

    tags = re.findall(r'<\s*(\w+)', output)
    # print(tags)

    tag_counter = Counter(tags)
    # print(tag_counter)

    if (args.frequency == False):
        # print in alphabetic order
        for tag,count in sorted(tag_counter.items()):
            print(f"{tag} {count}")
    else:
        # print in sorted order
        for tag,count in tag_counter.most_common():
            print(f"{tag} {count}")



if __name__ == "__main__":
    main()
    q4.hello()
