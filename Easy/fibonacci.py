from sys import argv

# name = argv[1]
name = "fibonacci.txt"

with open(name, "r") as file:
    cases = [int(x.strip()) for x in file.read().strip().splitlines() if x]

max_value = max(cases)

fib = [0, 1, 1]

while len(fib) <= max_value:
    fib.append(fib[(len(fib)-1)] + fib[(len(fib) - 2)])

for case in cases:
    print(fib[case])