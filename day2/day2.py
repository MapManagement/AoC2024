def read_input_one():
    report_list = []
    splitter = " "

    with open("input", "r") as input:
        for line in input:
            levels = line.split(splitter)
            levels = [int(x) for x in levels]

            report_list.append(levels)

    return report_list

def unsafe_checker(first_level, second_level):
    abs_diff = abs(first_level - second_level)

    return first_level >= second_level or abs_diff > 3 or abs_diff == 0

def puzzle_one():
    reports = read_input_one()
    unsafe_reports = []
    number_safe_reports = 0

    for r in reports:
        if r[0] > r[len(r)-1]:
            r = r[::-1]

        safe = True

        for l in range(1,len(r)):
            if unsafe_checker(r[l-1], r[l]):
                unsafe_reports.append(r)
                safe = False
                break

        if safe:
            number_safe_reports += 1

    return (number_safe_reports, unsafe_reports)

def puzzle_two():
    number_safe_reports, unsafe_reports = puzzle_one()

    for r in unsafe_reports:
        if r[0] > r[len(r)-1]:
            r = r[::-1]

        any_safe = False

        for i in range(len(r)):
            modded_r = r.copy()
            modded_r.pop(i)
            safe = True

            for l in range(1,len(modded_r)):
                if unsafe_checker(modded_r[l-1], modded_r[l]):
                    safe = False
                    break

            if safe:
                any_safe = True

        if any_safe:
            number_safe_reports += 1

    return number_safe_reports

def main():
    print(f"First puzzle: {puzzle_one()[0]}")
    print(f"Second puzzle: {puzzle_two()}")

if __name__ == '__main__':
    main()
