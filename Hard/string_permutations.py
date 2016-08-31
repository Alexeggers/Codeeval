from sys import argv, exit
from math import factorial
from random import shuffle

#file_name = argv[1]
file_name = "string_permutations.txt"

with open(file_name, "r") as file:
    for line in (x.strip() for x in file.read().split("\n") if x):
        line_length = len(line)
        outputs = []
        while len(outputs) < factorial(line_length):
            temp = list(line)
            while temp in outputs:
                shuffle(temp)
            outputs.append(temp)


        print(",".join(sorted(("".join(x) for x in outputs))))