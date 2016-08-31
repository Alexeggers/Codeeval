import sys
import re

file_name = sys.argv[1]
regex = "[a-zA-Z]+"


def eval_line(line):
    print(" ".join(x.lower() for x in re.findall(regex,line)))


with open(file_name, "r") as file:
    for line in file.read().split("\n"):
        eval_line(line)
