from io import StringIO

ex = StringIO("""0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""")

def part_1():
    with open('inputs/9') as f:
        lines = ex.read().splitlines()

    extrapolatedSum = 0
    for valueHistory in lines:
        difs = [tuple(map(int, valueHistory.split()))]
        for i in range(len(difs[-1]) - 1): # An array of length 2 can at most produce 1 list of differences
            difs.append(tuple(b - a for a, b in zip(difs[i][:-1], difs[i][1:]))) # append an array of differences
            if difs[-1].count(difs[-1][0]) == len(difs[-1]): # diffs all the same
                extrapolatedSum += sum([dif[-1] for dif in difs])
                break
    print(extrapolatedSum)

def part_2():
    with open('inputs/9') as f:
        lines = f.read().splitlines()

    extrapolatedSum = 0
    for valueHistory in lines:
        difs = [tuple(map(int, reversed(valueHistory.split())))]
        for i in range(len(difs[-1]) - 1): # An array of length 2 can at most produce 1 list of differences
            difs.append(tuple(b - a for a, b in zip(difs[i][:-1], difs[i][1:]))) # append an array of differences
            if difs[-1].count(difs[-1][0]) == len(difs[-1]): # diffs all the same
                extrapolatedSum += sum([dif[-1] for dif in difs])
                break
    print(extrapolatedSum)
#part_1()
part_2()