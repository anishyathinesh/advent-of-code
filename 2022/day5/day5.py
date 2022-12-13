"""
author: Anishya T
advent of code day 5!
"""


def make_stacks():
    stacks = {}
    for i in range (1, 10):
        stacks['stack'+str(i)] = []
    return stacks


def part1():
    stacks = make_stacks()
    with open("input") as fd:
        for i in range(8):
            stack_num = 1
            line = fd.readline()
            for j in range(9):
                snip = line[:4].strip()
                if snip == '':
                    pass
                else:
                    stacks['stack'+str(stack_num)].insert(0, line[1])
                line = line[4:]
                stack_num += 1
        for i in range(2):
            line = fd.readline().strip()

        print(stacks)

        for line in fd:
            line = line.strip().split()
            num = int(line[1])
            start = line[3]
            end = line[5]
            for i in range(num):
                crate = stacks['stack'+start].pop()
                stacks['stack'+end].append(crate)
    final_str = ""
    for stack in stacks.values():
        final_str += stack[len(stack) - 1]

    return final_str


def part2():
    stacks = make_stacks()
    with open("input") as fd:
        for i in range(8):
            stack_num = 1
            line = fd.readline()
            for j in range(9):
                snip = line[:4].strip()
                if snip == '':
                    pass
                else:
                    stacks['stack'+str(stack_num)].insert(0, line[1])
                line = line[4:]
                stack_num += 1
        for i in range(2):
            line = fd.readline().strip()

        print(stacks)

        for line in fd:
            line = line.strip().split()
            num = int(line[1])
            start = line[3]
            end = line[5]
            moving = []
            for i in range(num):
                moving.insert(0, stacks['stack'+start].pop())
            stacks['stack'+end].extend(moving)
    final_str = ""
    for stack in stacks.values():
        final_str += stack[len(stack) - 1]

    return final_str


print(part2())