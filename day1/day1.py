def read_input_one():
    left_list = []
    right_list = []
    splitter = "   "

    with open("input", "r") as input:
        for line in input:
            lists = line.split(splitter)

            left_list.append(int(lists[0].strip()))
            right_list.append(int(lists[1].strip()))

    return (left_list, right_list)

def puzzle_one():
    left_list, right_list = read_input_one()

    left_list.sort()
    right_list.sort()

    sum = 0

    for i in range(len(left_list)):
        distance = abs(left_list[i] - right_list[i])
        sum += distance

    return sum

def read_input_two():
    left_list = []
    right_dict = {}
    splitter = "   "

    with open("input", "r") as input:
        for line in input:
            lists = line.split(splitter)

            left_list.append(int(lists[0].strip()))

            right_number = int(lists[1].strip())

            if right_number in right_dict.keys():
                right_dict[right_number] += 1
            else:
                right_dict[right_number] = 1

    return (left_list, right_dict)


def puzzle_two():
    left_list, right_dict = read_input_two()

    sum = 0

    for i in range(len(left_list)):
        if left_list[i] in right_dict.keys():
            sum += left_list[i] * right_dict[left_list[i]]

    return sum

def main():
    print(f"Puzzle 1: {puzzle_one()}")
    print(f"Puzzle 2: {puzzle_two()}")

if __name__ == '__main__':
    main()
