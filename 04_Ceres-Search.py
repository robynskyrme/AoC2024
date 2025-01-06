# 6.1.2025

# Advent of Code 2024
# Day 6: Ceres Search

import time

def is_string(raw,index,string):
    for i in range(len(string)):
        if raw[index] != string[i]:
            return False
        index += 1
    return True


def search(grid,word):
    fwd = word                                                        # OK horizontal forward/backward are easy
    back = ""
    for i in range(len(word)-1,-1,-1):
        back += (word[i])

    horizontal = 0
    vertical = 0
    diagonal = 0

    for j in range(len(grid)-1):
        if j % grid[0] <= grid[0] - len(word) + 1:
            if is_string(grid,j,fwd):                               # these 'mod' bits are just to stop it from
                                                                    # reading words over linebreaks
                horizontal += 1
            if is_string(grid,j,back):
                horizontal += 1

            if j <= len(grid) - grid[0] * (len(word) - 1):
                if is_string_diagfwd(grid, j, fwd):
                    diagonal += 1
                if is_string_diagfwd(grid, j, back):
                    diagonal += 1

            if j <= len(grid) - grid[0] * (len(word) - 1):
                if is_string_diagback(grid, j, fwd):
                    diagonal += 1
                if is_string_diagback(grid, j, back):
                    diagonal += 1


        if j <= len(grid) - grid[0] * (len(word)-1):                # search for horizontal, vertical, and BOTH diagonals!
                                                                    # (i somehow forgot vertical AND one diagonal at first)
            if is_string_vert(grid,j,fwd):
                vertical += 1
            if is_string_vert(grid,j,back):
                vertical += 1


    output_individual = True

    if output_individual:
        print(horizontal)
        print(vertical)
        print(diagonal)

    return horizontal + vertical + diagonal



def is_string_vert(raw,index,string):

    for i in range(len(string)):
        if raw[index] != string[i]:
            return False
        index += raw[0]
    return True


def is_string_diagfwd(raw,index,string):

    for i in range(len(string)):
        if raw[index] != string[i]:
            return False
        index += raw[0]+1
    return True

def is_string_diagback(raw,index,string):

    for i in range(len(string)):
        if raw[index] != string[i]:
            return False
        index += raw[0]-1
    return True

def process(input):                            # make the crossword grid into one long list of letters, with index 0
                                               # storing the width of the grid
    linelength = 0

    data = [0]

    while input:
        if input[:1] == "\n":
            data[0] = linelength
            linelength = 0
            input == input[1:]
        else:
            data.append(input[0])
            linelength += 1
        input = input[1:]

    return(data)



if __name__ == "__main__":
    stopwatch = time.time()

    file = open("04_1.aoc","r")
    input = file.read()
    file.close()

    grid = process(input)

    # test puzzle as provided on AoC
    #grid = process("MMMSXXMASM\nMSAMXMSMSA\nAMXSXMAAMM\nMSAMASMSMX\nXMASAMXAMM\nXXAMMXXAMA\nSMSMSASXSS\nSAXAMASAAA\nMAMMMXMMMM\nMXMXAXMASX")

    total = search(grid,"XMAS")

    print("Total: " + str(total))

    print("\n/// done in " + str(time.time()-stopwatch) +" seconds ///")
