# 7.1.2025

# Advent of Code 2024
# Day 4: Ceres Search

import time

class wordsearch():
    grid = []
    width = 0
    height = 1
    def __init__(self,path):
        self.path = path

        file = open(path, "r")
        input = file.read()
        file.close()

        self.process(input)

    def process(self,raw):
        self.width = 0
        width_gathered = False

        data = []

        while raw:
            if raw[:1] == "\n":
                self.height += 1
                width_gathered = True
                raw == raw[1:]
            else:
                data.append(raw[0])
                if width_gathered == False:
                    self.width += 1
            raw = raw[1:]

        self.grid = data

    def extract(self,index,length,direction):          # DIRECTION key: 1 horizontal 2 vertical 3 fwdslash 4 backslash
        word = ""                                      # if the extract asked for is out of grid bounds, returns None
        width = self.width
        height = self.height

        margin_left = length - 1
        margin_right = width - length
        margin_top = width * (length - 1)
        margin_bottom = (height - length + 1) * width

        cells = []

        pos = index % width

        for cell in range(length):
            cells.append(index)

        if direction == 1:                            # FORWARD
            if pos > margin_right:
                return None
            for inc in range(length):
                cells[inc] += inc

        if direction == 2:                            # UP
            if index < margin_top:
                return None
            for inc in range(length):
                cells[inc] -= inc * width

        if direction == 3:                            # FORWARD SLASH
            if index >= margin_bottom or pos < margin_left:
                return None
            for inc in range(length):
                cells[inc] += inc * width - inc

        if direction == 4:                            # BACK SLASH
            if index >= margin_bottom or pos > margin_right:
                return None
            for inc in range(length):
                cells[inc] += inc * width + inc

        for cell in range(length):                      # turn the cells gathered into a string
            word += self.grid[cells[cell]]

        return word

    def xmas(self):                                     # PART TWO of the problem

        hits = 0

        w = self.width
        h = self.height
        for cell in range(w * h):
            letter = self.grid[cell]
            if letter == "A":
                fwd = self.extract(cell+1-w,3,3)
                back = self.extract(cell-1-w,3,4)
                if fwd == "SAM" or fwd == "MAS":
                    if back == "SAM" or back == "MAS":
                        hits += 1

        return hits



    def search(self,word):
        hits = 0

        backword = ""
        for i in range(len(word)):
            backword += word[len(word)-1-i]

        for direction in range(1,7):
            for cell in range(self.width * self.height):
                get = self.extract(cell,len(word),direction)
                if get == word or get == backword:
                    hits += 1
        return hits








if __name__ == "__main__":
    stopwatch = time.time()

    ceres = wordsearch("04_1.aoc")

    part_one = ceres.search("XMAS")

    part_two = ceres.xmas()

    print("XMAS occurences: " + str(part_one))
    print("X-MAS occurences: " + str(part_two))

    print("\n/// done in " + str(time.time()-stopwatch) +" seconds ///")
