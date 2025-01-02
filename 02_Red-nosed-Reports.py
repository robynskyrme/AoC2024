
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

    while index < len(report):
        slope = report[index] - report[index-1]
        if slope < 0 and climb == True:
            return "DIRECTION CHANGES"
        if slope > 0 and climb == False:
            return "DIRECTION CHANGES"
        if abs(slope) > max or abs(slope) < min:
            return "CHANGE TOO STEEP (OR NO CHANGE)"
        gradient.append(slope)
        index += 1

    return True



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
