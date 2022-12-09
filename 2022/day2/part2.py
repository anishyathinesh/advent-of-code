"""
author: Anishya T
advent of code day 2!
"""
# the input is the predictor of what will happen. the goal is to calculate
# the points earned by me for each line, and then sum them up.
# this time we are trying to determine what move to pick in order to follow
# the outcome of the strat guide.
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
            outcome = line[1]

            if outcome == "Y":  # we need the same move as the elf's
                my_choice = elf_choice
            elif outcome == "X":  # we need to lose
                if elf_choice == "A":
                    my_choice = "C"
                elif elf_choice == "B":
                    my_choice = "A"
                else:
                    my_choice = "B"
            else:  # we need to win
                if elf_choice == "A":
                    my_choice = "B"
                elif elf_choice == "B":
                    my_choice = "C"
                else:
                    my_choice = "A"

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
            print("my choice:", my_choice, "elf choice:", elf_choice, " ", )
            print("points for this round:", round_points)
            total_points += round_points
            print("total points:", total_points)
            print()

    return total_points




print(main())
