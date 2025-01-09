# 8.1.2025

# AoC 2024 Day 7: Bridge Repair



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
        numbers = data[i][1]

        d = math.ceil(len(numbers))-1
        ceiling = 2**d

        for count in range(ceiling):
            binary = binarystr(count,d)
            if calc_using_string(numbers,binary) == result:
                #print(result)
                results.add(result)
    return results


def calc_using_string(list,slab):
    d = len(list)-1
    if d != len(slab):
        print("boom ONE")
        return

    running = list[0]

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
