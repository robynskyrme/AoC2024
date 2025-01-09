# 8.1.2025

# AoC 2024 Day 7: Bridge Repair PART TWO

# Tried to add concatention, but this code evaluates it *first*, rather than left to right. Will start from scratch, I think


import time
import math

def binarystr(n,length):
    slab = str(bin(n))[2:]
    slab = slab.rjust(length,"0")
    return slab


def brute_signs(data):                                          # Use binary counting to test every possible
                                                                # combination of + and * between the numbers
    results = set()

    for i in range(len(data)):
        result = data[i][0]
        if result == 7290:
            rs=19
        numbers = data[i][1]

        table = concat_perms(numbers)
        for perms in range(len(table)):
            concatnums = table[perms]

            d = math.ceil(len(concatnums))-1
            ceiling = 2**d

            for count in range(ceiling):
                binary = binarystr(count,d)
                if calc_using_string(concatnums,binary) == result:
                    print(result)
                    results.add(result)
    return results


def calc_using_string(list,slab):
    running = list[0]

    if len(list) == 1:
        return running

    d = len(list)-1
    if d != len(slab):
        print("boom ONE")
        return



    for i in range(d):
        operator = slab[i]
        if operator == "0":
            running = running + list[i+1]
        if operator == "1":
            running = running * list[i+1]

    return running


def process(raw):
    new = []
    for i in range(len(raw)):
        raw[i] = raw[i][:-1]
        equation = raw[i].split(": ")
        equation[0] = int(equation[0])
        equation[1] = equation[1].split(" ")
        for j in range(len(equation[1])):
            equation[1][j] = int(equation[1][j])
        new.append(equation)
    return new

def concat_perms(list):
    d = len(list)-1
    ceiling = 2**d

    table = []

    for i in range(ceiling):
        newlist = []
        newlist.append(str(list[0]))
        binary = binarystr(i,d)

        for j in range(d):
            concat = binary[j]
            if concat == '0':
                newlist.append(str(list[j+1]))
            if concat == '1':
                newlist[len(newlist)-1] += str(list[j+1])

        for k in range(len(newlist)):
            newlist[k] = int(newlist[k])

        table.append(newlist)

    return table




if __name__ == "__main__":
    stopwatch = time.time()

    n = 128
    d = math.ceil(math.log(n,2))

    #file = open("07_example.aoc","r")

    file = open("07_puzzle.aoc","r")
    data = file.readlines()
    file.close

    data = process(data)

    results = brute_signs(data)
    print("Sum of correct answers: " + str(sum(results)))

    print("\n/// done in " + str(time.time()-stopwatch) +" seconds ///")
