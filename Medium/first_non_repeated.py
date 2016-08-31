from sys import argv

##file_name = argv[1]
file_name = "first_non_repeated.txt"

with open(file_name, "r") as file:
    for line in file.read().split("\n"):
        for _char in line:
            if line.count(_char) > 1:
                line = line.replace(_char, "")
        if len(line):
            print(line[0])
