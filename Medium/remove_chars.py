from sys import argv
from collections import namedtuple

tuple_line = namedtuple("line", "text, chars")
tuples = []

with open(argv[1], "r") as file:
    for line in file.read().split("\n"):
        try:
            tuples.append(tuple_line(*[x.strip() for x in line.split(",")]))
        except:
            continue

def clean(text, chars):
    for char in chars:
        text = text.replace(char, "")
    return text

for item in tuples:
    print(clean(*item).strip())
