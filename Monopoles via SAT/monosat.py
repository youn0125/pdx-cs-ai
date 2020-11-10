#!/usr/bin/python3
# Mi Yon Kim
import sys
# Create SAT problem in DIMACS format
# http://www.satcompetition.org/2009/format-benchmarks2009.html
# to solve a Sudoku instance.

# Given M monopoles and N rooms, return the atom
# corresponding to atom[m][n]
def atom(m, n):
    return num_of_monopoles * n + m + 1

num_of_monopoles, num_of_rooms = int(sys.argv[1]), int(sys.argv[2])

# Keep a list of all the clauses.
clauses = []
def clause(c):
    clauses.append(c)

# Every cell must have a value.
for r in range(num_of_monopoles):
    clause([atom(r, c) for c in range(num_of_rooms)])

# The same value may not occur twice in the same column.
for r in range(num_of_monopoles):
    for c1 in range(num_of_rooms):
        for c2 in range(num_of_rooms):
            if c1 == c2:
                continue
            clause([-atom(r, c1), -atom(r, c2)])

# The same value may not occur twice in the same column.
for c in range(num_of_rooms):
    for r1 in range(num_of_monopoles):
        for r2 in range(num_of_monopoles):
            if r1 == r2:
                continue
            clause([-atom(r1, c), -atom(r2, c), -atom(r1+r2, c)])

for c in clauses:
    print(c, "", end="")
    print("0")


