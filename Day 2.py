from aocd import get_data, submit

# Constants
YEAR = 2024
DAY = 2

def main():
    # Fetch the input data for the specified day
    input_data = get_data(day=DAY, year=YEAR)

    print(input_data)

    # Example processing function
    result_part1 = solve_part1(input_data)
    print(f"Part 1: {result_part1}")

    result_part2 = solve_part2(input_data)
    print(f"Part 2: {result_part2}")

    # Submit answers
    submit(result_part1, part='a', day=DAY, year=YEAR)
    submit(result_part2, part='b', day=DAY, year=YEAR)

def solve_part1(data):
    # Implement your solution for part 1 here
    reports = data.split('\n')
    sum = 0

    for report in reports:
        report = [int(item) for item in report.split()]
        increasing = report[0]<report[-1]
        failures=0
        index = 0

        while index<len(report)-1:
            if not succeed(increasing, report[index], report[index + 1]):
                failures = 1
                break
            index += 1

        if failures<1:
            sum+=1
        # diffs = [report[i]-report[i+1] for i in range(len(report)-1)]
        # if any(x==0 for x in diffs):
        #     continue
        # elif all(x > 0 for x in diffs):
        #     if any(x>3 for x in diffs):
        #         continue
        #     else:
        #         sum+=1
        # elif all(x < 0 for x in diffs):
        #     if any(x<-3 for x in diffs):
        #         continue
        #     else:
        #         sum+=1

    return sum

def succeed(increasing, num1, num2):
    diff = num2-num1
    if increasing:
        return diff>0 and diff<=3
    if not increasing:
        return diff<0 and diff>=-3

def solve_part2(data):
    # Implement your solution for part 2 here
    reports = data.split('\n')
    sum = 0

    #so essentially we're going to implement part 1, but just lazily check every possible iteration of removal if it's not safe.

    for report in reports:
        report = [int(item) for item in report.split()]
        increasing = report[0] < report[-1]
        failures = 0
        index = 0

        while index < len(report) - 1:
            if not succeed(increasing, report[index], report[index + 1]):
                failures = 1
                break
            index += 1

        if failures < 1:
            sum += 1
        else:
            for i in range(len(report)):
                candidate = report[:i] + report[i+1:]
                failures = 0
                index = 0

                while index < len(candidate) - 1:
                    if not succeed(increasing, candidate[index], candidate[index + 1]):
                        failures = 1
                        break
                    index += 1

                if failures < 1:
                    sum += 1
                    break


    return sum


if __name__ == "__main__":
    main()