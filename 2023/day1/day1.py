# author: Anishya M Thinesh
# advent of code day 1

def extract_num(line):
    digs = []
    i = 0
    flag = False
    while not flag:
        if line[i].isnumeric():
            digs.append(line[i])
            flag = True
        i += 1

    flag = False
    i = len(line) - 1
    while not flag:
        if line[i].isnumeric():
            digs.append(line[i])
            flag = True
        i -= 1

    return int("".join(digs))




def part_1():
    ans = 0
    with open('day1_input') as file:
        for line in file:
            to_add = extract_num(line)
            ans += to_add

    print(ans)




def extract_num_v(line):
    digs = []

    line_right = line
    flag = False
    while not flag:
        tok = line_right[:1]
        if tok.isnumeric():
            digs.append(tok)
            flag = True

        tok = line_right[:3]
        if tok == "one":
            digs.append("1")
            flag = True
        elif tok == "two":
            digs.append("2")
            flag = True
        elif tok == "six":
            digs.append("6")
            flag = True

        tok = line_right[:5]
        if tok == "three":
            digs.append("3")
            flag = True
        elif tok == "seven":
            digs.append("7")
            flag = True
        elif tok == "eight":
            digs.append("8")
            flag = True

        tok = line_right[:4]
        if tok == "four":
            digs.append("4")
            flag = True
        elif tok == "five":
            digs.append("5")
            flag = True
        elif tok == "nine":
            digs.append("9")
            flag = True
        line_right = line_right[1:]

    line_left = line
    flag = False
    while not flag:
        length = len(line_left)

        tok = line_left[length - 1:]
        if tok.isnumeric():
            digs.append(tok)
            flag = True

        tok = line_left[length - 3:]
        if tok == "one":
            digs.append("1")
            flag = True
        elif tok == "two":
            digs.append("2")
            flag = True
        elif tok == "six":
            digs.append("6")
            flag = True

        tok = line_left[length - 5:]
        if tok == "three":
            digs.append("3")
            flag = True
        elif tok == "seven":
            digs.append("7")
            flag = True
        elif tok == "eight":
            digs.append("8")
            flag = True

        tok = line_left[length - 4:]
        if tok == "four":
            digs.append("4")
            flag = True
        elif tok == "five":
            digs.append("5")
            flag = True
        elif tok == "nine":
            digs.append("9")
            flag = True
        line_left = line_left[:length - 1]

    return int("".join(digs))




def part_2():
    ans = 0
    with open('day1_input') as file:
        for line in file:
            to_add = extract_num_v(line.strip())
            ans += to_add

    print(ans)




# main fcn
if __name__ == "__main__":
    part_1()
    part_2()
