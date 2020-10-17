#!/usr/bin/python3
# Monoples solver using DFS
# Mi Yon Kim

import sys

class Monopole:

    def __init__(self, nMonopoles, nRooms):
        self.monopoleSet = set()
        for i in range(int(nMonopoles)):
            self.monopoleSet.add(i+1)
        self.rooms = [None] * int(nRooms)
        for i in range(int(nRooms)):
            self.rooms[i] = list()

    def show(self):
        print(self.monopoleSet)
        print(self.rooms)



monopole = Monopole(sys.argv[1], sys.argv[2])
monopole.show()



