import os, re, sys
from collections import defaultdict
from os import path

# Regexes for processing.
name = re.compile("[a-z] +([A-Z][a-zA-Z]+)")
justname = re.compile("[A-Z][a-zA-Z]+")
punct = re.compile("[^-' a-zA-Z]+")
dash = re.compile("--")
possess = re.compile("'s")


class Bow:
    def __init__(self, fname):
        if "austen" in fname:
            self.auClass = 0
        elif "shelley" in fname:
            self.auClass = 1
        else:
            self.auClass = None
        self.paragraph_cnt = 1
        self.wordsDic = defaultdict(set)

def alphas(w):
    return ''.join([c for c in w if (c.lower() >= 'a' and c.lower() <= 'z') or c == '\n'])

bowList = list()

# novel should be an iterable text object.  Returns the
# processed text of novel as a string.
def process(novel):

    bowObj = Bow(novel.name)

    # List of paragraphs. Each paragraph is a list of string
    # lines, not newline-terminated.


    # Accumulate paragraphs, filtering out extraneous lines.
    par = list()
    for line in novel:
        words = line.split()
        if not words:
            if bowObj.wordsDic[bowObj.paragraph_cnt] and len(bowObj.wordsDic[bowObj.paragraph_cnt]) > 1:
                bowObj.paragraph_cnt += 1
            continue
        for w in words:
            bowObj.wordsDic[bowObj.paragraph_cnt].add(w)

    bowList.append(bowObj)

# Process all available novels.
for fn in sys.argv[1:]:
    with open(fn, "r", encoding='UTF-8') as f_in:
        process(f_in)

