"""
author: Anishya T
day1 advent of code!
"""
# calculate first elf's calories. set this as the greatest. readline to get
# rid of blank. start a for loop and start accumulating runner. if line in
# blank. stop and check if u need to reassign.


def main():
    acc = 0
    greatest = 0
    with open("puzzleinput") as fd:
        for line in fd:
            line = line.strip()
            if line == "":
                if acc > greatest:
                    greatest = acc
                acc = 0
            else:
                acc += int(line)
    return greatest


if __name__ == "__main__":
    print(main())
