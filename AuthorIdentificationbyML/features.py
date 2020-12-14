import math, os, re, sys
from collections import defaultdict
from heapq import nlargest

# return only alphabets in the word
def alphas(w):
    return ''.join([c for c in w if c.lower() >= 'a' and c.lower() <= 'z'])

# List of paragraphs.
pars = list()
# set of features
features = set()
# novel should be an iterable text object.  Returns the
# list of paragraph containing dictionary of each paragraph
# Each paragraph(word:0 or 1) contains paragraph number, title,
# class(austen:0, shelly:1), and features(word:1)
def create_pars(novel):
    par = defaultdict(int)
    # "*" stands for class
    if "austen" in novel.name:
        par["*"] = 0
    elif "shelley" in novel.name:
        par["*"] = 1
    else:
        par["*"] = 2
    par_cnt = 1
    # "&":paragraph and "#":title
    par["&"] = par_cnt
    par["#"] = novel.name.replace(".txt","")
    novel_class = par["*"]
    novel_title = par["#"]

    for line in novel:
        words = line.split()
        if not words:
            if par and len(par) > 1:
                pars.append(par)
                par = defaultdict(int)
                par_cnt += 1
                par["&"] = par_cnt
                par["*"] = novel_class
                par["#"] = novel_title
        for w in words:
            aw = alphas(w)
            features.add(aw)
            par[aw] = 1

def count_labels(insts):
    ninsts = len(insts)

    np = 0
    for i in insts:
        np += i["*"]

    return np, ninsts - np

def entropy(insts):
    np, nn = count_labels(insts)
    ninsts = np + nn

    if np == 0 or nn == 0:
        return 0

    pr_p = np / ninsts
    pr_n = nn / ninsts

    return -pr_p * math.log2(pr_p) - pr_n * math.log2(pr_n)

# Create list of paragraph with all available novels.
# Create bag of words(features) as a set.
for fn in sys.argv[1:]:
    with open(fn, "r", encoding='UTF-8') as f_in:
        create_pars(f_in)

# Gain-Based feature selection
# Create dictionary for gains(feature:gain)
gains = defaultdict()
# class entropy
c_entropy = entropy(pars)
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

# Get only 300 largest gains from the gains
top_feat = nlargest(300, gains, key=gains.get)

# Emit comma-separated line with paragraph identifier
# instances means a list of paragraph
instances = list()
for par in pars:
    inst = list()
    inst.append(par["#"] + "." + str(par["&"]))
    inst.append(par["*"])
    for f in top_feat:
        inst.append(par[f])
    instances.append(inst)

# write to features.csv
with open("features.csv", "w", encoding="utf-8") as f_out:
    f_out.write("\n".join([','.join([str(f) for f in i]) for i in instances]))