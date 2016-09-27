from sys import argv

with open(argv[1], "r") as file:
    test_cases = ([y.strip() for y in x.split(":")] for x in file.read().splitlines() if x)

for case in test_cases:
    arr = [int(x) for x in case[0].split(" ")]
    swaps = [[int(y.strip()) for y in x.split("-")] for x in case[1].split(",")]
    for swap in swaps:
        arr[swap[0]],arr[swap[1]] = arr[swap[1]],arr[swap[0]]
    print(" ".join((str(x) for x in arr)))
