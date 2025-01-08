# 7.1.2025

# AoC 2024 Day 6: Guard Gallivant

import time

map = []

class guard():
    def __init__(self,col,row,o):               # o for orientation. I will use a clock: 12, 3, 6, 9
        self.col = col
        self.row = row
        self.o = o

        self.odometer = 1
        self.visited = []

        self.facing = [0, 0]

        self.beyondmap = False

        self.lookinfront()

    def turn(self):
        self.o += 3
        if self.o == 15:
            self.o = 3

        self.lookinfront()

    def lookinfront(self):
        o = self.o
        col = self.col
        row = self.row

        if o == 12:
            self.facing = [col,row-1]
        if o == 3:
            self.facing = [col+1,row]
        if o == 6:
            self.facing = [col, row+1]
        if o == 9:
            self.facing = [col-1, row]

        if self.facing[1] < 0 or self.facing[1] >= len(map[0]) or self.facing[0] < 0 or self.facing[0] >= len(map):
            self.beyondmap = True

        infront = ""

        if self.beyondmap == False:
            infront = map[self.facing[1]][self.facing[0]]

        if infront == "#":
            self.turn()

    def walk(self,steps):

        while steps != "stop":                          # User-input (enter for one step, otherwise,a number of steps)

            if steps == "":
                steps = input()
                if steps == "":
                    steps = 1

            for march in range(int(steps)):
                self.lookinfront()
                if self.beyondmap == True:                                   # If the guard's stepping off the map...
                    self.markasvisited(self.row,self.col)
                    showmap()
                    print("Total positions visited: " + str(guard.odometer)) # The program can end
                    return
                self.stepfwd()                                               # Otherwiswe, keep going

            showmap()
            print("Positions visited: " + str(guard.odometer))


    def stepfwd(self):                                                      # Take a single step forward
        self.markasvisited(self.row,self.col)                               # marking the square as visited
        map[self.facing[1]][self.facing[0]] = ochar(self.o)
        self.col = self.facing[0]
        self.row = self.facing[1]

        if [self.row,self.col] not in self.visited:                         # add the new square to our record
            self.odometer += 1                                              # (so long as it hasn't already been visited)

    def markasvisited(self,row,col):
        self.visited.append([self.row,self.col])
        map[self.row][self.col] = "X"

def ochar(o):
    if o == 12:
        return "^"
    if o == 3:
        return ">"
    if o == 6:
        return "v"
    if o == 9:
        return "<"

def showmap():
    chunk = ""
    for i in range(len(map)):
        for j in range(len(map[i])):
            chunk += map[i][j] #+ " "
        chunk += "\n"
    print(chunk)



def process(raw):

    for y in range(len(raw)):
        raw[y] = raw[y][:-1]
        if "^" in raw[y]:
            guardy = y
            guardx = raw[y].index("^")
        raw[y] = list(raw[y])
    return raw,guardx,guardy


if __name__ == "__main__":
    stopwatch = time.time()

    file = open("06_puzzle.aoc")
    data = file.readlines()
    file.close()

    map,guardx,guardy = process(data)

    guard = guard(guardx,guardy,12)

    # showmap()
    # print("Positions visited: " + str(guard.odometer))

    guard.walk(10000)



    print("\n/// done in " + str(time.time()-stopwatch) +" seconds ///")

