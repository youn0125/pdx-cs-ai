import math, os, re, sys
from collections import defaultdict
from heapq import nlargest

def alphas(w):
    return ''.join([c for c in w if c.lower() >= 'a' and c.lower() <= 'z'])

# List of paragraphs.
pars = list()
features = set()
# novel should be an iterable text object.  Returns the
# processed text of novel as a string.
def process(novel):
    # Accumulate paragraphs, filtering out extraneous lines.
    par = defaultdict(int)
    # "c" stands for class
    if "austen" in novel.name:
        par["c"] = 0
    elif "shelley" in novel.name:
        par["c"] = 1
    else:
        par["c"] = 2
    par_cnt = 1
    # "p" stands for paragraph
    par["p"] = par_cnt
    par["t"] = novel.name.replace(".txt","")
    novel_class = par["c"]
    novel_title = par["t"]

    for line in novel:
        words = line.split()
        if not words:
            if par and len(par) > 1:
                pars.append(par)
                par = defaultdict(int)
                par_cnt += 1
                par["p"] = par_cnt
                par["c"] = novel_class
                par["t"] = novel_title
        for w in words:
            aw = alphas(w)
            features.add(aw)
            par[aw] = 1

def count_labels(insts):
    ninsts = len(insts)

    np = 0
    for i in insts:
        np += i["c"]

    return np, ninsts - np

def entropy(insts):
    np, nn = count_labels(insts)
    ninsts = np + nn

    if np == 0 or nn == 0:
        return 0

    pr_p = np / ninsts
    pr_n = nn / ninsts

    return -pr_p * math.log2(pr_p) - pr_n * math.log2(pr_n)

# Process all available novels.
for fn in sys.argv[1:]:
    with open(fn, "r", encoding='UTF-8') as f_in:
        process(f_in)
print(len(features))
print(list(features)[:10])
# Gain-Based feature selection
gains = defaultdict()
c_entropy = entropy(pars)
print(c_entropy)
# Get gain for each feature
for f in features:
    inst0 = list()
    inst1 = list()
    for p in pars:
        if p[f] == 0:
            inst0.append(p)
        elif p[f] == 1:
            inst1.append(p)
    u0 = entropy(inst0)
    u1 = entropy(inst1)
    pr0 = len(inst0) / len(pars)
    pr1 = len(inst1) / len(pars)
    uprime = pr0*u0 + pr1*u1
    g = c_entropy - uprime
    gains[f] = g

top_feat = nlargest(300, gains, key=gains.get)
print(top_feat)

instances = list()
for par in pars:
    inst = list()
    inst.append(par["t"] + "." + str(par["p"]))
    for f in top_feat:
        inst.append(par[f])
    instances.append(inst)

with open("features.csv", "w", encoding="utf-8") as f_out:
    f_out.write("\n".join([','.join([str(f) for f in i]) for i in instances]))



