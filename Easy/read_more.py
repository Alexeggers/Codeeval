from sys import argv

with open(argv[1], "r") as file:
    test_cases = (x.strip() for x in file.read().splitlines() if x)

for case in test_cases:
    print(case) if len(case) <= 55 else print(case[0:39].strip() + "... <Read More>")
