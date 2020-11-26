import os, re, sys

class Bow:
    def __init__(self, fname):
        if "austen" in fname:
            self.auClass = 0
        elif "shelley" in fname:
            self.auClass = 1
        else:
            self.auClass = None
        self.paragraph_cnt = 0
        self.words = dict()

def alphas(w):
    return ''.join([c for c in w if (c.lower() >= 'a' and c.lower() <= 'z') or c == '\n'])

allwords = list()
for fname in sys.argv[1:]:
    with open(fname, "r", encoding='UTF-8') as f_in:
        text = f_in.read()
        words = re.findall(r'\S+|\n', text)
        for w in words:
            aw = alphas(w)
            if len(aw) > 1:
                allwords.append(aw)


print(len(allwords))
print(list(allwords)[:10])