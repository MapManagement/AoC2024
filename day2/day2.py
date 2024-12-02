def read_input_one():
    report_list = []
    splitter = " "

    with open("input", "r") as input:
        for line in input:
            levels = line.split(splitter)
            levels = [int(x) for x in levels]

            report_list.append(levels)

    return report_list

def puzzle_one():
    reports = read_input_one()
    safe_reports = 0

    for r in reports:
        for level in r:
            pass    

def main():
    puzzle_one()

if __name__ == '__main__':
    main()
