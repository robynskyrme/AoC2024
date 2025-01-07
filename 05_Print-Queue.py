# 7.1.2025

# Advent of Code 2024 Day 5: Print Queue

import time

def process(raw):
    buffer = raw.index("\n")

    rules = {}
    updates = []

    left = []                                       # Turn the rules into two columns, left and right
    right = []

    for i in range(buffer):
        left.append(raw[i][:2])
        right.append(raw[i][3:5])

    raw = raw[buffer+1:]

    for i in range(len(raw)):
        raw[i] = raw[i][:-1]
        raw[i] = raw[i].split(",")


    for i in range(buffer):                         # Make them into a set of pairs: for each page, another set
        if left[i] not in rules:                    # of pages which can only be inserted AFTER it
            rules.update({left[i]:set()})
            rules[left[i]].add(right[i])
        if left[i] in rules:
            rules[left[i]].add(right[i])

    init_banned = set(right)                             # This list constitues all pages with a required precedent:
                                                    # they are therefore, before any pages have been added, forbidden
    return rules, raw, init_banned                  # all that's left of 'raw' has now become the list of updates



def check(update,rules,banned):

    valid = True

    allow = set()

    print(banned)

    for page in banned:
        for preceding in rules:
            if page in rules[preceding]:
                if preceding not in update:
                    allow.add(page)
                    print("allowing" + page)

    for each in allow:
        banned.remove(each)

    print(update)
    print(banned)

    while update:
        page = update[0]
        #print(page)
        if page in banned:
            print(page)
            print("boom")           # if the page can't
            return False
        if page in rules:
            following = rules[page]
            #print(following)
            for each in following:
                if each in banned:
                    banned.remove(each)


        update = update[1:]

    return True



if __name__ == "__main__":
    stopwatch = time.time()

    file = open("05_1.aoc","r")
    data = file.readlines()
    file.close

    print(data)
    print("")

    rules,updates,init_banned = process(data)

    print(rules)

    for i in range(len(updates)):
        print(check(updates[i],rules,init_banned))


    print("\n/// done in " + str(time.time()-stopwatch) +" seconds ///")
