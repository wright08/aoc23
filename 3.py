import io
import string
from math import prod

ex = io.StringIO("""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""")

def part_1():
    with open("inputs/3") as f:
        lines = f.read().splitlines()
        lines = ['.' * len(lines[0])+'..'] + list(map(lambda x: '.'+x+'.', lines)) + ['.' * len(lines[0]) + '..']
    
    partNumberSum = 0
    for row in range(1, len(lines) - 1):
        line = lines[row]
        i = 1
        while i < len(line) - 1:
            num = None
            while line[i].isdigit():
                if not num:
                    num = i
                i += 1
            if num:
                for sym in lines[row-1][num-1:i+1] + line[num-1] + line[i] + lines[row+1][num-1:i+1]:
                    if sym not in '.' + string.digits:
                        partNumberSum += int(line[num:i])
                        break
            else:
                i += 1
    print(partNumberSum)

def part_2():
    with open("inputs/3") as f:
        lines = f.read().splitlines()
        lines = ['.' * len(lines[0])+'..'] + list(map(lambda x: '.'+x+'.', lines)) + ['.' * len(lines[0]) + '..']
    
    gears = {}
    for row in range(1, len(lines) - 1):
        line = lines[row]
        i = 1
        while i < len(line) - 1:
            num = None
            while line[i].isdigit():
                if not num:
                    num = i
                i += 1
            if num:
                for srow in [row-1, row, row+1]:
                    for col in range(num - 1, i+1):
                        if lines[srow][col] == '*':
                            gears.setdefault((srow, col), []).append(int(line[num:i]))
            else:
                i += 1
    print(sum([prod(v) for v in gears.values() if len(v) == 2]))

part_2()