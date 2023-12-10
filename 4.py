import io
import math

ex = io.StringIO("""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""")

def part_1():
    with open('inputs/4') as f:
        lines = f.read().splitlines()
    
    worthSum = 0
    for line in lines:
        winningNumbers, hand = list(map(lambda x: x.split(), line.split(': ')[1].split(' | ')))
        worthSum += int(math.pow(2, len([num for num in hand if num in winningNumbers])-1) // 1)
    print(worthSum)

def part_2():
    with open('inputs/4') as f:
        lines = f.read().splitlines()
    
    scratchcards = [1] * len(lines)
    for idx, line in enumerate(lines):
        matchingNumbers, numbers = list(map(lambda x: x.split(), line.split(': ')[1].split(' | ')))
        for copy in range(len([num for num in numbers if num in matchingNumbers])):
            scratchcards[idx+copy+1] += scratchcards[idx]
    print(sum(scratchcards))

#part_1()
part_2()