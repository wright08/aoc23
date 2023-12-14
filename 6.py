from io import StringIO
from math import prod, sqrt, ceil

ex = StringIO("""Time:      7  15   30
Distance:  9  40  200""")

def part_1():
    with open('inputs/6') as f:
        lines = f.read().splitlines()
    
    times = list(map(int, lines[0].split(": ")[1].split()))
    distances = list(map(int, lines[1].split(": ")[1].split()))

    beat = [0] * len(times)
    for rate in range(1, times[-1]):
        for recordIdx, race in enumerate(times):
            timeRemaining = race - rate
            distance = timeRemaining * rate
            if rate < race and distance > distances[recordIdx]:
                beat[recordIdx] += 1
    print(prod(beat))

def part_2():
    with open('inputs/6') as f:
        lines = f.read().splitlines()
    
    time = int("".join(lines[0].split(": ")[1].split()))
    distance = int("".join(lines[1].split(": ")[1].split()))

    beat = 0
    for rate in range(1, time):
        timeRemaining = time - rate
        curDistance = timeRemaining * rate
        if curDistance > distance:
            beat += 1
    print(beat)

def part_2_equation():
    with open('inputs/6') as f:
        lines = f.read().splitlines()
    
    time = int("".join(lines[0].split(": ")[1].split()))
    distance = int("".join(lines[1].split(": ")[1].split()))

    # issa quadratic equation
    # time > rate > 0
    # (time - rate) * rate > distance = rate^2 - time*rate - distance > 0
    mini = ceil((time - sqrt(time**2 - 4*distance)) / 2)
    maxi = ceil((time + sqrt(time**2 - 4*distance)) / 2)
    print(maxi - mini)

part_2_equation()
