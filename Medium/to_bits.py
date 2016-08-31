from sys import argv

with open(argv[1], "r") as file:
    for line in ((y.strip() for y in x.split("|")) for x in file.read().split("\n")):
        print(" | ".join(str(int(x, 2)) for x in line))
