from sys import argv
from collections import namedtuple
import math

Point = namedtuple("Point", "x, y")

with open("closest_pair.txt", "r") as file:
    cases = [x.strip() for x in file.read().split("\n") if x]

def find_distance(point1, point2):
    x = math.fabs(point1.x - point2.x)
    y = math.fabs(point1.y - point2.y)
    return math.sqrt(x**2 + y**2)

cases.pop(0)
cases.pop(len(cases) - 1)
cases = [Point(int(x), int(y)) for x,y in (case.split(" ") for case in cases if " " in case)]
solution = 10000

for index, point in enumerate(cases):
    if index == len(cases) - 1:
        break
    temp_solution = find_distance(point, cases[index + 1])
    if temp_solution < solution:
        solution = temp_solution
if solution == 10000:
    print("INFINITY")
else:
    print(round(solution, 4))