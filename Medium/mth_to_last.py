import sys

##file_name = sys.argv[1]
file_name = "mth_to_last.txt"

with open(file_name, "r") as file:
    for line in file.read().strip().split("\n"):
        temp = line.split(" ")[::-1]
        if int(temp[0]) >= len(temp):
            continue
        print(temp[int(temp[0])])
