import string

file_name = "pangrams.txt"

with open(file_name, "r") as file:
    cases = [x for x in file.read().splitlines() if x]

alphabet = list(string.ascii_lowercase)

for case in cases:
    present = []
    for letter in alphabet:
        if letter in case:
            present.append(letter)
    if present:
        print("".join(present))
    else:
        print("NULL")