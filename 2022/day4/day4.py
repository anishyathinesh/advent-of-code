"""
author: Anishya T
advent of code day 4!
"""



def part1():
    fully_contained = 0
    with open("input") as fd:
        for line in fd:
            line = line.strip().split(",")  # line contains both elves sections

            elf1 = line[0].split("-")  # elf 1 start and end
            elf1_start = int(elf1[0])
            elf1_end = int(elf1[1])

            elf2 = line[1].split("-")
            elf2_start = int(elf2[0])
            elf2_end = int(elf2[1])

            elf1_sec = {i for i in range(elf1_start, elf1_end+1)}
            elf2_sec = {i for i in range(elf2_start, elf2_end+1)}

            # case when elf1 is contained by elf2
            if elf1_sec.issubset(elf2_sec) or elf2_sec.issubset(elf1_sec):
                fully_contained += 1

    return fully_contained


def part2():
    overlaps = 0
    with open("input") as fd:
        for line in fd:
            line = line.strip().split(",")  # line contains both elves sections

            elf1 = line[0].split("-")  # elf 1 start and end
            elf1_start = int(elf1[0])
            elf1_end = int(elf1[1])

            elf2 = line[1].split("-")
            elf2_start = int(elf2[0])
            elf2_end = int(elf2[1])

            elf1_sec = {i for i in range(elf1_start, elf1_end+1)}
            elf2_sec = {i for i in range(elf2_start, elf2_end+1)}

            # case when elf1 is contained by elf2
            if len(elf1_sec.intersection(elf2_sec)) != 0:
                overlaps += 1

    return overlaps



print(part1())
print(part2())
