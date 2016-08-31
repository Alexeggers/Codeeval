import sys, operator

##file_name = sys.argv[1]
file_name = "lines.txt"
with open(file_name, "r") as file:
    lines = file.read().split("\n")
num_of_outputs = int(lines.pop(0))
lines_dict = dict(enumerate(lines))
for index in lines_dict.keys():
    lines_dict[index] = len(lines_dict[index])
lines_dict = sorted(lines_dict.items(), key = operator.itemgetter(1))[::-1]
for num in range(num_of_outputs):
    print(lines[lines_dict[num][0]])
