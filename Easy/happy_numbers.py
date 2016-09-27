from sys import argv

with open(argv[1], "r") as file:
    test_cases = (int(x) for x in file.read().splitlines() if x)

def square_up(x):
    numbers = [int(i)**2 for i in list(str(x))]
    x = sum(numbers)
    return x

for case in test_cases:
    already_found = []

    while case != 1:
        case = square_up(case)
        if case in already_found:
            break
        already_found.append(case)

    if case == 1:
        print("1")
    else:
        print("0")
