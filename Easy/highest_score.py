from sys import argv

with open(argv[1], "r") as file:
    test_cases = (x.strip() for x in file.read().splitlines() if x)

for test in test_cases:
    test = [[int(i.strip()) for i in x.strip().split(" ")] for x in test.split("|")]
    max_nums = []
    for i in range(len(test[0])):
        current_contest = []
        for artist in test:
            current_contest.append(artist[i])
        max_nums.append(max(current_contest))
    print(max_nums)
