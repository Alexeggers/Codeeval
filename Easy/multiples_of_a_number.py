from sys import argv

with open(argv[1], "r") as file:
    test_cases = ([int(y) for y in x.split(",")] for x in file.read().splitlines() if x)

for case in test_cases:
    x,n = case
    _n = n
    while n < x:
        n += _n
    print(n)
