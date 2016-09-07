from sys import argv

file_name = "flavius.txt"
#file_name = argv[1]

with open(file_name, "r") as file:
    cases = [x for x in file.read().splitlines() if x]

for case in cases:
    count, steps = [int(x) for x in case.split(",")]
    count = [x for x in range(0,count)]
    dead = []
    while count:
        if len(count) > 1:
            subcount = count[steps-1::steps]
            dead += subcount
            for item in subcount:
                count.remove(item)
        else:
            dead += count
    print(dead)