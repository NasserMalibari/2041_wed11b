#!/usr/bin/env python3

import sys

def main():

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    file1_words = set()
    file2_words = set()
    # add file1 words
    file1_words = word_set(file1)
    file2_words = word_set(file2)

    # print(file1_words)
    # print(file2_words)
    difference = file1_words - file2_words
    # add file2 words

    # set difference
    for word in sorted(difference):
        print(word)

def word_set(file1):
    file1_words = set()
    with open(file1) as f1:
        for line in f1:
            line = line.strip()
            file1_words.add(line)      

    return file1_words


if __name__ == "__main__":
    main()