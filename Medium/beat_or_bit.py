from sys import argv
import fileinput

#file_name = argv[1]
file_name = "beat_or_bit.txt"

def g2d(a):
    a ^= a >> 4
    a ^= a >> 2
    a ^= a >> 1
    return a

with open(file_name, "r") as file:
    for line in ((y.strip() for y in x.split("|")) for x in file.read().split("\n")):
        print(" | ".join(str(g2d(int(x, 2))) for x in line))


#for line in fileinput.input():
#    print(" | ".join([str(g2d(int(i, 2))) for i in line.split(" | ")]))