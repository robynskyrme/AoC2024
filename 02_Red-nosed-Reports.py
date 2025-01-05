
# AoC 2024
# Day 2: Red-nosed Reports

# 2.1.2025

import time
def safety_check(report):                   # Check a single report (line) for safety, returns True/False
    report = report[:-1]
    data = list(report)

    report = [""]                           # 8 lines: turn text string into list of integers
    index = 0
    for char in range(len(data)):
        if data[char] == " ":
            report.append("")
            index += 1
        else:
            report[index] += data[char]

    for entry in range(len(report)):
        report[entry] = int(report[entry])

    max,min = 3,1

    index = 1
    gradient = []
    if report[0] < report[1]:
        climb = True
    else:
        climb = False

    safe = False

    while index < len(report):
        slope = report[index] - report[index-1]
        if abs(slope) > max or abs(slope) < min:
            safe = False
        elif slope < 0 and climb == True:
            safe = False
        elif  slope > 0 and climb == False:
            safe = False
        else:
            safe = True
        gradient.append(slope)
        index += 1

    return safe

                                            # function added for PART TWO
def single_peak(report):         # checks if there is a single peak which, if removed, keeps the report in a gradient
    print(report)


if __name__ == "__main__":
    stopwatch = time.time()

    file = open("02_1.aoc","r")

    input = file.readlines()
    file.close()

    safe = 0

    for i in range(len(input)):
        if safety_check(input[i]) == True:
            safe += 1

    print("\n[Part One] Total safe reports:")
    print(safe)

    print("\n/// done in " + str(time.time()-stopwatch) +" seconds ///")
