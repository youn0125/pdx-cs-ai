#!/usr/bin/python3
# Get solution monopoles in each room using DFS
# Mi Yon Kim
import sys

# Architecture referred from cry.py
# https://github.com/pdx-cs-ai/crys/blob/main/crys.py
class Monopole:

    def __init__(self, num_monopoles, num_rooms):
        # Monopoles list to variables
        self.pvars = list()
        for i in reversed(range(int(num_monopoles))):
            self.pvars.append(i+1)

        self.num_rooms = int(num_rooms)

    # Print out the solution monopoles in each room on a single line in increasing order.
    def show(self, vals=dict()):
        for r in range(self.num_rooms):
            room = [monopole for monopole, r_n in vals.items() if r_n == r]
            for m in room:
                print(m, end=" ")
            print()

    # Get solution monopoles in each room using DFS.
    # pvars: The list of monopoles, vals: monopole(key):room number(value), val:room number
    def solve(self, pvars=None, vals=None, val=None):
        if pvars is None:
            pvars = list(self.pvars)
        if vals is None:
            vals = dict()
        if val is None:
            val = -1

        # Return True iff no constraint violations.
        def ok():
            # If there are below 3 elements in the vals, it is always true.
            if len(vals.values()) < 3:
                return True
            # Get monopole list in a val room.
            room = [monopole for monopole, r_n in vals.items() if r_n == val]
            # If there are below 3 monopoles in the room, it is always true.
            if len(room) <= 2:
                return True
            # Check the room if it contains the sum of any two of monopole values
            # If it contains, return false
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

        # Recursive case: try to extend partial assignment.
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
vals = monopole.solve()
if vals is None:
    print("unsat")
else:
    monopole.show(vals)