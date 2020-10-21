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
        self.rooms_sum = [None] * int(num_rooms)
        for i in range(int(num_rooms)):
            self.rooms_sum[i] = set()
        self.cur_room_num = int(0)
        self.num_rooms = int(num_rooms)
        self.num_fail = 0

    def show(self):
        print(self.monopoles)
        print(self.rooms)
        print(self.rooms_sum)

    def solve(self):
        # base case
        if len(self.monopoles) == 0:
            return True

        # base case
        if self.num_fail == self.num_rooms:
            return None

        self.num_fail = 0
        # Recursive case: try to put monopole into the room
        peek = self.monopoles[0]
        # Iterate room from 0 through n-1
        for i in range(self.num_rooms):
            # if the monopole can append to current room
            if peek not in self.rooms_sum[i]:
                m = peek
                n_monopoles = len(self.rooms[i])
                undo = False
                temp_set = set()
                # Append the sum of monopoles to rooms_sum
                if n_monopoles >= 1:
                    rooms_sum_wo_cur = list(self.rooms_sum)
                    rooms_sum_wo_cur.remove(self.rooms_sum[i])
                    for j in self.rooms[i]:
                        temp_set.add(j+m)
                    # iterate temp_set check if all of the rooms_sum has element of temp_set
                    # if one of the element meets the condition, undo
                    for k in temp_set:
                        cnt = 0
                        for r_sum in rooms_sum_wo_cur:
                            if k in r_sum and m not in r_sum:
                                cnt += 1
                        if len(rooms_sum_wo_cur) == cnt:
                            undo = True

                            break
                if not undo:
                    self.monopoles.pop(0)
                    self.rooms_sum[i] = self.rooms_sum[i].union(temp_set)
                    self.rooms[i].append(m)
                    break
            else:
                self.num_fail += 1

        sol = self.solve()
        if sol:
            return sol

    def solve2(self):
        # base case
        if len(self.monopoles) == 0:
            return True

        # Recursive case:
        peek = self.monopoles[0]
        if peek not in self.rooms_sum[self.cur_room_num]:
            m = self.monopoles.pop(0)
            n_monopoles = len(self.rooms[self.cur_room_num])
            if n_monopoles >= 1:
                for i in self.rooms[self.cur_room_num]:
                    self.rooms_sum[self.cur_room_num].add(i + m)
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

        sol = self.solve2()
        if sol:
            return sol


monopole = Monopole(sys.argv[1], sys.argv[2])
monopole.show()
vals = monopole.solve()
if vals is None:
    print("unsat")
else:
    monopole.show()

