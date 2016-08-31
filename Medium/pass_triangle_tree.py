import sys

with open("mad_tree.txt", 'r') as file:
    test_cases = file.read().strip().splitlines()

triangle = [[int(n) for n in l.split()] for l in test_cases if l]

triangle = triangle[::-1]
