import functools
from io import StringIO
import itertools

ex = StringIO("""seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""")

def part_1():
    with open('inputs/5') as f:
        lines = f.read().split('\n\n')
    seeds = list(map(int, lines[0].split()[1:]))
    for mapping in lines[1:]:
        # num - src + dst if num >= src and num < src + length
        mappings = []
        for mapping in mapping.splitlines()[1:]:
            dst, src, l = list(map(int, mapping.split()))
            mappings.append((range(src, src + l), dst))
        for i in range(len(seeds)):
            for r in mappings:
                if seeds[i] in r[0]:
                    seeds[i] = seeds[i] - r[0][0] + r[1]
                    break
    print(min(seeds))

def part_2():
    with open('inputs/5') as f:
        lines = f.read().split('\n\n')
    seeds = list(map(int, lines[0].split(": ")[1].split()))
    seedRanges = [(range(seeds[2*x], seeds[2*x]+seeds[2*x+1])) for x in range(len(seeds) // 2)]
    for mapping in lines[1:]:
        # num - src + dst if num >= src and num < src + length
        mappings = []
        for mapping in mapping.splitlines()[1:]:
            dst, src, l = list(map(int, mapping.split()))
            mappings.append((range(src, src + l), dst))

        nextSeedRanges = []
        while seedRanges:
            cur = seedRanges.pop(0)
            for dstRange in mappings:
                overlap = range(max(cur[0], dstRange[0][0]), min(cur[-1], dstRange[0][-1])+1)
                if overlap:
                    if overlap != cur:
                        # overlap is always smaller
                        if cur[0] < overlap[0]:
                            # _
                            # cur   cur
                            # 012   12
                            #  ov   overlap
                            #  ^^
                            seedRanges.append(range(cur[0], overlap[0]))
                        else:
                            # __
                            # ov    overlap
                            # 012   01
                            # cur   cur
                            #   ^
                            seedRanges.append(range(overlap[-1] + 1, cur[-1] + 1))
                        cur = overlap
                    # transform
                    cur = range(cur[0] - dstRange[0][0] + dstRange[1], cur[-1] - dstRange[0][0] + dstRange[1] + 1)
                    break
            nextSeedRanges.append(cur)
        seedRanges = nextSeedRanges
    print(functools.reduce(lambda x, y: min(x, y[0]), nextSeedRanges, float('inf')))

#part_1()
part_2()