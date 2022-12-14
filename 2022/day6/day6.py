"""
author: Anishya T
advent of code day 6!
"""
# Base case: repeating char(snip) == False
# 	return num
# Else:
# 	cut off 3 from beginning of str
# 	snip is first 4 chars
# 	num += 3
# 	fcn(str

import sys
sys.setrecursionlimit(5000)


def repeating_chars(str):
    """
    checks if there are repeating characters in a string
    :return: (bool) True if there are repeating chars, False if there are not.
    """
    for i in range(0, len(str)):
        for j in range(len(str)):
            if j == i:
                pass
            else:
                if str[j] == str[i]:
                    return True
    return False


def part1_rec(input, snip, num=0):
    if repeating_chars(snip) is False:
        return num + 4
    else:
        input = input[3:]
        snip = input[:4]
        num += 3
        return part1_rec(input, snip, num)


def part1():
    with open("input") as fd:
        input = fd.readline()

    num = part1_rec(input, input[:4], 0)

    return num



def part2_rec(input, snip, num=0):
    if repeating_chars(snip) is False:
        return num + 14
    else:
        input = input[1:]
        snip = input[:14]
        num += 1
        return part2_rec(input, snip, num)


def part2():
    with open("input") as fd:
        input = fd.readline()

    num = part2_rec(input, input[:14], 0)

    return num


print(part1())
print(part2())
