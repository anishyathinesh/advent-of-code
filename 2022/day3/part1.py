"""
author: Anishya T
advent of code day 3!
"""

# split into two compartments. map first comp to a dict. find repeating
# letter. calculate ascii.


def main():
    sum = 0
    with open("input") as fd:
        for line in fd:
            c1_dict = {}
            line = line.strip()
            c1 = line[:int((len(line)/2))]
            c2 = line[int(len(line)/2):]

            for char in c1:
                c1_dict[char] = 1
            for char in c2:
                if char in c1_dict:
                    repeat = char

            if repeat.islower():
                sum += ord(repeat) - 96
            else:
                sum += ord(repeat) - 38

    return sum


print(main())
