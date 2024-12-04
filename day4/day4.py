def read_input_one():
    with open("input", "r") as input:
        return [list(line.strip()) for line in input]

def find_horizontally(input):
    input += [x[::-1] for x in input]
    sum = 0

    for i in range(len(input)):
        for j in range(len(input[i])-3):
            if input[i][j] == "X" and input[i][j+1] == "M" and input[i][j+2] == "A" and input[i][j+3] == "S":
                sum += 1

    return sum

def find_vertically(input):
    flipped_input = input.copy()[::-1]
    input.append(['-' for x in range(len(input[0]))])
    input += flipped_input
    sum = 0

    for i in range(len(input)-3):
        for j in range(len(input[i])):
            if input[i][j] == "X" and input[i+1][j] == "M" and input[i+2][j] == "A" and input[i+3][j] == "S":
                sum += 1

    return sum

def find_diagonally(input):
    vertically_flipped_input = [x[::-1] for x in input.copy()]
    horizontally_flipped_input = input.copy()[::-1]
    doubly_flipped_input = [x[::-1] for x in input.copy()[::-1]]

    input.append(['-' for x in range(len(input[0]))])
    input += vertically_flipped_input
    input.append(['-' for x in range(len(input[0]))])
    input += horizontally_flipped_input
    input.append(['-' for x in range(len(input[0]))])
    input += doubly_flipped_input
    sum = 0

    for i in range(len(input)-3):
        for j in range(len(input[i])-3):
            if input[i][j] == "X" and input[i+1][j+1] == "M" and input[i+2][j+2] == "A" and input[i+3][j+3] == "S":
                sum += 1

    return sum

def first_puzzle():
    input = read_input_one()

    sum = 0
    sum += find_horizontally(input.copy())
    sum += find_vertically(input.copy())
    sum += find_diagonally(input.copy())
    return sum

def main():
    print(f"First puzzle: {first_puzzle()}")
    #print(f"Second puzzle: {puzzle_two()}")

if __name__ == '__main__':
    main()
