#! python3
# Fizzbuzz.py

import sys
import re

regex = "^\d+\s\d+\s\d+$"

file_name = sys.argv[1]

def eval_line(line):
    if not re.match(regex, line):
        return
    X, Y, N = [int(s) for s in line.split(" ")]
    numbers = [x for x in range(1, N+1)]
    for index, num in enumerate(numbers):
        if not (num % X) and not (num % Y):
            numbers[index] = "FB"
        elif not (num % X):
            numbers[index] = "F"
        elif not (num % Y):
            numbers[index] = "B"
    
    print(" ".join(str(x) for x in numbers))


with open(file_name, "r") as file:
    for line in file.read().split("\n"):
        eval_line(line)
