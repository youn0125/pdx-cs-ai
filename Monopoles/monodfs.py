#!/usr/bin/python3
# Monopoles solver using DFS
# Mi Yon Kim
import sys


class Monopole:

    def __init__(self, num_monopoles, num_rooms):
        self.pvars = list()
        for i in reversed(range(int(num_monopoles))):
            self.pvars.append(i+1)

        self.rooms_sum = [None] * int(num_rooms)
        for i in range(int(num_rooms)):
            self.rooms_sum[i] = list()

        self.num_rooms = int(num_rooms)

    def show(self, vals=dict()):
        print(vals)

    def solve(self, pvars=None, vals=None, val=None):
        # New solution attempt. Can't put these values
        # inline because bad things happen with Python's
        # evaluator.
        if pvars is None:
            pvars = list(self.pvars)
        if vals is None:
            vals = dict()
        if val is None:
            val = -1

        # Return True iff no constraint violations
        def ok():

            if len(vals.values()) < 3:
                return True
            room = [monopole for monopole, r_n in vals.items() if r_n == val]

            if len(room) <= 2:
                return True
            for m1 in range(0, len(room)-1):
                for m2 in range(m1+1, len(room)):
                    sum = room[m1] + room[m2]
                    if sum in room:
                        return False
            return True

        # Base case: check for failure.
        if not ok():
            return None

        # Base case: check for solution.
        if not pvars:
            return vals

        # Recursive case:
        v = pvars.pop()
        assert v not in vals
        for val in range(self.num_rooms):
            vals[v] = val
            soln = self.solve(pvars=pvars, vals=vals, val=val)
            if soln:
                return soln

        # No solution found. Undo the current assignment and
        # return failure.
        del vals[v]
        pvars.append(v)
        return None


monopole = Monopole(sys.argv[1], sys.argv[2])
monopole.show()
vals = monopole.solve()
if vals is None:
    print("unsat")
else:
    monopole.show(vals)

