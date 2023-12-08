import io
import math

ex = io.StringIO("""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""")

def p1():
    with open("inputs/2") as f:
        #lines = ex.read().splitlines()
        lines = f.read().splitlines()

    colors = {'r': 12, 'g': 13, 'b': 14}
    idSum = 0
    for id, line in enumerate(lines, start=1):
        possible = True
        game = line.split(": ")[1]
        for set in game.split("; "):
            for colorNumber in set.split(", "):
                number, color = colorNumber.split(" ")
                if int(number) > colors[color[0]]:
                    possible = False
                    break
            if not possible:
                break
        if not possible:
            continue
        idSum += id
    return idSum

def p2():
    with open("inputs/2") as f:
        #lines = ex.read().splitlines()
        lines = f.read().splitlines()

    minColorPowerSum = 0
    for line in lines:
        game = line.split(": ")[1]
        colors = dict.fromkeys("rgb", 0)
        for set in game.split("; "):
            for colorNumber in set.split(", "):
                number, color = colorNumber.split(" ")
                if int(number) > colors[color[0]]:
                    colors[color[0]] = int(number)
        minColorPowerSum += math.prod(colors.values())
    return minColorPowerSum

print(p1())
print(p2())
