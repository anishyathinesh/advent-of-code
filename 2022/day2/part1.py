"""
author: Anishya T
advent of code day 2!
"""
# the input is the predictor of what will happen. the goal is to calculate
# the points earned by me for each line, and then sum them up.
# points earned by me: move selected + outcome of the round

# A,X = Rock (1pt). B,Y = Paper(2pt). C,Z = Scissors(3pt)
# loss = 0pt. draw = 3pt. win = 6pt.


def main():
    round_num = 0
    total_points = 0
    with open("input") as fd:
        for line in fd:
            round_num += 1
            round_points = 0
            line = line.strip().split()
            elf_choice = line[0]
            my_choice = line[1]
            # reassign my values
            if my_choice == "X":
                my_choice = "A"
            elif my_choice == "Y":
                my_choice = "B"
            else:
                my_choice = "C"

            # points from selection
            if my_choice == "A":
                round_points += 1
            elif my_choice == "B":
                round_points += 2
            else:
                round_points += 3

            # calculate outcome. tie and winning cases
            if my_choice == elf_choice:
                round_points += 3

            if my_choice == "A":
                if elf_choice == "C":
                    round_points += 6

            if my_choice == "B":
                if elf_choice == "A":
                    round_points += 6

            if my_choice == "C":
                if elf_choice == "B":
                    round_points += 6

            # round summary test case
            print("round #", round_num, sep="")
            print("my choice:", my_choice, "elf choice:", elf_choice, " ",)
            print("points for this round:", round_points)
            total_points += round_points
            print("total points:", total_points)
            print()

    return total_points


print(main())
