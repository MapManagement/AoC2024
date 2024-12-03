def read_input():
    with open("input", "r") as input:
        return input.read()

def mul_parser(text):
    splitter = ","
    pieces = text.split(splitter)

    if pieces[0].isdecimal() and pieces[1].isdecimal():
        return int(pieces[0]) * int(pieces[1])

    return -1

def first_puzzle():
    input = read_input()
    start_pattern = "mul("
    end_pattern = ")"

    start = 0
    sum = 0

    while input.find(start_pattern, start) != -1:
        start = input.find(start_pattern, start)
        end = input.find(end_pattern, start)
        numbers = input[start+4:end]

        product = mul_parser(numbers)

        if product >= 0:
            sum += product

        start += 4

    return sum

def do_finder(input):
    do_pattern = "do()"
    dont_pattern = "don't()"
    do_ranges = []

    start = 0

    while input.find(dont_pattern, start) != -1:
        start_dont = input.find(dont_pattern, start)
        do_ranges.append((start, start_dont))

        start_do = input.find(do_pattern, start_dont)

        start = start_do

    do_ranges.append((start, len(input)-1))

    return do_ranges

def second_puzzle():
    input = read_input()
    do_ranges = do_finder(input)
    print(do_ranges)

    start_pattern = "mul("
    end_pattern = ")"

    sum = 0

    for r in do_ranges:
        start = 0
        temp_input = input[r[0]:r[1]]

        while temp_input.find(start_pattern, start) != -1:
            start = temp_input.find(start_pattern, start)

            end = temp_input.find(end_pattern, start)
            numbers = temp_input[start+4:end]

            product = mul_parser(numbers)

            if product >= 0:
                sum += product

            start += 4

    return sum

def main():
    print(f"First puzzle: {first_puzzle()}")
    print(f"Second puzzle: {second_puzzle()}")

if __name__ == "__main__":
    main()
