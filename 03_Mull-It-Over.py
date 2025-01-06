
# AoC 2024
# Day 3: Mull It Over

# 5.1.2025

# yo *Roger* please remember to comment stuff



import time


def is_string(slab,index,string):
    for i in range(len(string)):
        if slab[index] != string[i]:
            return i
        index += 1
    return True

def valid_mult(slab):
    opencheck = is_string(slab,0,"mul(")

    if opencheck is not True:
        return False,0,0

    x = number_digout(slab,4)

    if not x[0]:
        return False,0,0

    if not is_string(slab,4+len(str(x[1])),","):
        #print("boom ONE")
        return False,0,0

    y = number_digout(slab,5+len(str(x[1])))

    if not y[0]:
        #print("boom TWO")
        return False,0,0

    if not is_string(slab,5+len(str(x[1]))+len(str(y[1])),")"):
        #print("boom THREE")
        return False,0,0

    return True,x[1],y[1]

def number_digout(slab,index):
    if not slab[index].isdigit():
        return False,0

    numst = slab[index]
    index += 1

    while index < len(slab):
        if slab[index].isdigit() == True:
            numst += slab[index]
        else:
            return True,int(numst)
        index += 1

    return True,int(numst)


def process(slab):
    valid_data = []

    do = True

    index = 0

    while slab:
        if is_string(slab,0,"don't()") is True:     # added these checks for Part Two
#            print("boom FOUR")
#            print(slab[:7])
            do = False
        if is_string(slab,0,"do()") is True:
#            print("boom FIVE")
#            print(slab[:7])
            do = True

        valid,x,y = valid_mult(slab)

        if valid == True and do == True:
            valid_data.append(x)
            valid_data.append(y)

        slab = slab[1:]

    return(valid_data)

def add_multiplications(data):
    sum = 0
    for i in range(0,len(data),2):
        m = data[i] * data[i+1]
        sum += m

    return sum


if __name__ == "__main__":
    stopwatch = time.time()

    file = open("03_1.aoc","r")

    input = file.read()
    file.close()

    data = process(input)
#    print(data)

    sum = add_multiplications(data)

    print("Total: " + str(sum))

    print("\n/// done in " + str(time.time()-stopwatch) +" seconds ///")
