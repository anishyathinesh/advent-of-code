"""
author: Anishya T
day3 part 2
"""

# add 3 lines to a list at a time, name each rucksack.
# map each to a dict letter:# of occurrences. on the third map, check each
# time if the value becomes 3. if it's 3, find priority and add it to the accum.


def main():
    total_sum = 0
    d = {}
    nar_d = {}
    group = []
    with open("input") as fd:
        for line in fd:
            line = line.strip()
            group.append(line)

            if len(group) == 3:
                bag1, bag2, bag3 = group[0], group[1], group[2]
                for char in bag1:
                    if char not in d:
                        d[char] = True
                    else:
                        pass
                for char in bag2:
                    if char in d:
                        if char not in nar_d:
                            nar_d[char] = True
                        else:
                            pass
                for char in bag3:
                    if char in nar_d:
                        badge = char

                if badge.islower():
                    total_sum += ord(badge) - 96
                else:
                    total_sum += ord(badge) - 38

                group = []
                d = {}
                nar_d = {}

    return total_sum


print(main())
