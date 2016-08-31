from itertools import product as prod
from sys import argv

with open("string_list.txt", "r") as file:
    test_cases = [x.strip() for x in file.read().split("\n") if x]

for case in test_cases:
    case = case.split(",")
    if len(case) != 2:
        continue
    N, S = case
    options = prod(S, repeat = int(N))
    options = set(options)
    options = sorted(["".join(x) for x in options])
    print(",".join(options))