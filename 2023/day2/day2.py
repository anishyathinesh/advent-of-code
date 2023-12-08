# author: Anishya M Thinesh
# advent of code 2023 day 2

def part_1():
    with open('day2_input') as file:
        ans = 0
        id = 0
        powers = []
        for line in file:
            id += 1
            eligible = True
            min_red = 0
            min_blue = 0
            min_green = 0
            u_input = line.strip().split(';')
            u_input[0] = u_input[0][8:]

            for grab in u_input:
                grab = grab.strip().split(',')
                for chunk in grab:
                    chunk = chunk.strip().split(' ')
                    if chunk[1] == 'blue' and int(chunk[0]) > 14:
                        eligible = False
                    elif chunk[1] == 'red' and int(chunk[0]) > 12:
                        eligible = False
                    elif chunk[1] == 'green' and int(chunk[0]) > 13:
                        eligible = False

                    if chunk[1] == 'blue' and int(chunk[0]) > min_blue:
                        min_blue = int(chunk[0])
                    if chunk[1] == 'red' and int(chunk[0]) > min_red:
                        min_red = int(chunk[0])
                    if chunk[1] == 'green' and int(chunk[0]) > min_green:
                        min_green = int(chunk[0])

            powers.append(min_blue*min_red*min_green)
            if eligible:
                ans += id
    print(sum(powers))
    print(ans)






if __name__ == "__main__":
    part_1()
