#!/usr/bin/python3
# Monopoles solver using DFS
# Mi Yon Kim

import sys


class Monopole:

    def __init__(self, num_monopoles, num_rooms):
        self.monopoles = []
        for i in range(int(num_monopoles)):
            self.monopoles.append(i+1)
        self.rooms = [None] * int(num_rooms)
        for i in range(int(num_rooms)):
            self.rooms[i] = list()
        self.rooms_exclude = [None] * int(num_rooms)
        for i in range(int(num_rooms)):
            self.rooms_exclude[i] = set()
        self.cur_room_num = int(0)
        self.num_rooms = int(num_rooms)
        self.num_fail = 0

    def show(self):
        print(self.monopoles)
        print(self.rooms)
        print(self.rooms_exclude)

    def solve(self):
        # base case
        if len(self.monopoles) == 0:
            return True

        # Recursive case:
        peek = self.monopoles[0]
        if peek not in self.rooms_exclude[self.cur_room_num]:
            m = self.monopoles.pop(0)
            n_monopoles = len(self.rooms[self.cur_room_num])
            if n_monopoles >= 1:
                for i in self.rooms[self.cur_room_num]:
                    self.rooms_exclude[self.cur_room_num].add(i+m)
            self.rooms[self.cur_room_num].append(m)
            # reset the number of fail to append
            self.num_fail = 0
        else:
            if self.cur_room_num != self.num_rooms - 1:
                self.cur_room_num += 1
            else:
                self.cur_room_num = 0
            self.num_fail += 1
            if self.num_fail == self.num_rooms:
                return None

        sol = self.solve()
        if sol:
            return sol


monopole = Monopole(sys.argv[1], sys.argv[2])
monopole.show()
sol = monopole.solve()
if sol is None:
    print("unsat")
else:
    monopole.show()

