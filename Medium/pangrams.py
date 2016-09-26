import string
from sys import argv

file_name = "pangrams.txt"

with open(file_name, "r") as file:
    cases = [set(x.lower()) for x in file.read().splitlines() if x]

alphabet = set(string.ascii_lowercase)

for case in cases:
    missing = alphabet - case
    print("".join(missing or "NULL")
