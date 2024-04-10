#! /usr/bin/env python3

from collections import Counter
from argparse import ArgumentParser

import requests
from bs4 import BeautifulSoup

def hello():
    """ prints hello
        no args
       """
    print('hello')

def main():

    parser = ArgumentParser()
    parser.add_argument('-f', '--frequency', action='store_true', help='print tags by frequency')
    parser.add_argument("url", help="url to fetch")
    args = parser.parse_args()

    response = requests.get(args.url)
    webpage = response.text.lower()

    soup = BeautifulSoup(webpage, 'html.parser')
    # html5lib

    tags = soup.find_all()
    tag_names = [tag.name for tag in tags]

    tag_counter = Counter(tag_names)

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