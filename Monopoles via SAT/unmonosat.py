#!/usr/bin/python3
# Mi Yon Kim

# Read DIMACS format SAT solver output
# http://www.satcompetition.org/2009/format-benchmarks2009.html
# to solve a monopole instance.

import sys
from sys import stdin, stderr

num_of_monopoles, num_of_rooms = int(sys.argv[1]), int(sys.argv[2])

monopole_table = [[None]*num_of_rooms for _ in range(num_of_monopoles)]


def unlit(b):
    b -= 1
    m = b % num_of_monopoles + 1
    n = b // num_of_monopoles
    return (m, n)

header = next(stdin).strip()
if header == "s SATISFIABLE":
    # picosat
    lines = [l[1:] for l in stdin.readlines() if l and l[0] == 'v']
    solution = [int(b) for l in lines for b in l.split() if int(b) > 0]
elif header == "SAT":
    # minisat
    solution = [int(b) for b in next(stdin).split() if int(b) > 0]
else:
    print("unknown solution format", file=stderr)
    exit(-1)

for n in solution:
    (r, c) = unlit(n)
    assert monopole_table[r-1][c] == None
    monopole_table[r-1][c] = r-1

for c in range(num_of_rooms):
    print("Room ", c, end=": ")
    for r in range(num_of_monopoles):
        if monopole_table[r][c] is not None:
            print(monopole_table[r][c], end=", ")
    print()

