# author: Anishya M Thinesh
# advent of code 2023 day 2

def part_1():
    with open('day2_input') as file:
        ans = 0
        id = 0
        for line in file:
            id += 1
            eligible = True
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
            if eligible:
                ans += id
    print(ans)






if __name__ == "__main__":
    part_1()
