# 9.1.2025
# AoC Day 9: Disk Fragmenter


import time

table = []
disk = []

def process(raw):

    ID = 0
    last_empty = 1

    for index in range(len(raw)):
        char = raw[index]
        odd = index % 2

        blocksize = int(char)
        table.append(blocksize)

        disk.append([])

        if not odd:
            for b in range(blocksize):
                disk[index].append(ID)
            ID += 1
        if odd:
            last_empty = index

    table.append(last_empty)

def compact(caret_block,caret_data):
    c = disk
    last_empty = table[len(table)-1]

    if caret_block > last_empty:
        return 0,0

    if last_empty == 0:
        return False

    endblock = len(disk)-1

    if len(disk[endblock]) == 0 and last_empty == 0:
        disk.pop(endblock)
        return 0,0

    while len(disk[endblock]) == 0:

        disk.pop(endblock)
        endblock -= 1
        if endblock % 2 == 1:
            table[len(table)-1] -= 2


    endID = disk[endblock][len(disk[endblock])-1]

    if caret_block > last_empty:
        return 0,0

    disk[caret_block].append(endID)
    caret_data += 1

    if len(disk[caret_block]) == table[caret_block] and caret_block == last_empty:
        table[len(table)-1] = 0
        return 0,0

    if len(disk[caret_block]) == table[caret_block]:
        caret_block += 2
        caret_data = 0


    disk[endblock] = disk[endblock][:-1]

    return caret_block,caret_data



if __name__ == "__main__":
    stopwatch = time.time()

    file = open("09_puzzle.aoc","r")
    data = file.read()

    data = "12345"

    process(data)
    file.close()

    print("TABLE",table)
    print(" DISK",disk)

    caret_block = 1
    caret_data = 0

    uinp = ""
    while uinp != "quit":
        caret_block,caret_data = compact(caret_block,caret_data)
        if caret_block + caret_data == 0:
            uinp = "quit"
    print(disk)

    print("\n/// done in " + str(time.time()-stopwatch) +" seconds ///")
