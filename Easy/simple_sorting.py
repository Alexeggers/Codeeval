from sys import argv

with open("simple_sorting.txt", "r") as file:
    for line in (x.strip() for x in file.read().split("\n") if x):
        sorted_floats = sorted([float(f.strip()) for f in line.split(" ") if f])
        print(" ".join(['{:.3f}'.format(sf) for sf in sorted_floats]))