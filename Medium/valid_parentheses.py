from sys import argv
import re

bad_brackets = re.compile("[\(\[\{].*[([{].*[\)\]\}]")
never_closed = re.compile("([\(\[\{])[^\1]")



with open(argv[1], "r") as file:
    test_cases = [x.strip() for x in file.read().splitlines() if x]

for case in test_cases:
    print("True") if not re.search(bad_brackets, case) else print("False")
