from sys import argv

file_name = "reverse_groups.txt"
#file_name = argv[1]

with open(file_name, "r") as file:
    cases = [x for x in file.read().splitlines() if x]

def reverse_in_steps(list, steps):
    new_list = []
    for i in range(0,len(list),steps):
        sublist = list[i:i+steps]
        sublist = sublist[::-1]
        new_list += sublist
    return new_list


for case in cases:
    line, steps = case.split(";")
    line = line.split(",")
    steps = int(steps)

    if not len(line) % steps:
        line = reverse_in_steps(line,steps)
    else:
        rem_index = len(line)-(len(line)%steps)
        remainder = line[rem_index:len(line)]
        line = line[0:rem_index]
        line = reverse_in_steps(line,steps)
        line += remainder
    print(",".join(line))