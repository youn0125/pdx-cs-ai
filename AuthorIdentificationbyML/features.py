import os
from os import path
def alphas(w):
    return ''.join([c for c in w if c.lower() >= 'a' and c.lower() <= 'z'])

allwords = set()
prefix = ""
for fname in os.listdir(prefix):
    with open(path.join(prefix, fname), "r", encoding="utf-8") as f_in:
        text = f_in.read()
        words = text.split()
        for w in words:
            aw = alphas(w)
            if len(aw) <= 1:
                allwords.add(aw)


print(len(allwords))
print(list(allwords)[:10])