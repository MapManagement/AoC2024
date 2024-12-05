def read_input():
    ordering_rule_list = {}
    update_list = []

    section_splitter = "\n\n"
    ordering_rules_splitter = "|"
    update_splitter = ","

    with open("input", "r") as input:
        splitted_input = input.read().split(section_splitter)
        ordering_rules = splitted_input[0].splitlines()
        updates = splitted_input[1].splitlines()

        for line in ordering_rules:
            ordering_rule = line.split(ordering_rules_splitter)
            if int(ordering_rule[0]) in ordering_rule_list:
                ordering_rule_list[int(ordering_rule[0])].append(int(ordering_rule[1]))
            else:
                ordering_rule_list[int(ordering_rule[0])] = [int(ordering_rule[1])]

        for line in updates:
            update = [int(x) for x in line.split(update_splitter)]
            update_list.append(update)

    return (ordering_rule_list, update_list)

def check_updates(input):
    correct_updates = []
    wrong_updates = []
    
    for update in input[1]:
        correct = True
        for i in range(1, len(update)):
            if update[i-1] not in input[0].keys() or update[i] not in input[0][update[i-1]]:
                correct = False
                wrong_updates.append(update)
                break

        if correct:
            correct_updates.append(update)

    return (correct_updates, wrong_updates)

def first_puzzle():
    input = read_input()
    (correct_updates, wrong_updates) = check_updates(input)

    sum = 0
    for correct_update in correct_updates:
        sum += correct_update[len(correct_update)//2]

    return sum


def second_puzzle():
    input = read_input()
    (correct_updates, wrong_updates) = check_updates(input)
    
    for update in wrong_updates:
        for i in range(1, len(update)):
            if update[i-1] not in input[0].keys() or update[i] not in input[0][update[i-1]]:
                update[i-1], update[1] = update[1], update[i-1]

    print(wrong_updates)

    sum = 0
    for update in wrong_updates:
        sum += update[len(update)//2]

    return sum

def main():
    print(f"First puzzle: {first_puzzle()}")
    print(f"Second puzzle: {second_puzzle()}")

if __name__ == '__main__':
    main()
