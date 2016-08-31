from sys import argv

with open("sum_ints_from_file.txt", "r") as file:
    total = 0
    for line in file.read().split("\n"):
        total += int(line.strip())
        
print(total)
