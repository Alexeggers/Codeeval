from sys import argv
import re

regex = '^"[a-z|A-Z|0-9|_|-|+|.|@]+"|[a-z|A-Z|0-9|_|-|+|.?]*@{1}[a-z|0-9]+\.{1}[a-z|0-9|-]+\.?[a-z|0-9|-]{2,}'

with open(argv[1], "r") as file:
    for line in (x.strip() for x in file.read().split("\n")):
        if re.match(re.compile(regex), line):
            print("true")
        else:
            print("false")
