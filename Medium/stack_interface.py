import sys

class stack():

    values = []
    
    def __init__(self, _list = None):
        if _list:
            self.values = list(_list)

    def push(self, item):
        self.values.append(item)

    def pop(self):
        if self.values:
            return self.values.pop(len(self.values) - 1)
        else:
            return None

    def __str__(self):
        return str(self.values)

##file_name = sys.argv[1]
file_name = "stack_nums.txt"

with open(file_name, "r") as file:
    lines = [stack(x.split(" ")) for x in file.read().split("\n")]

for line in lines:
    values = []
    while line.values:
        values.append(line.pop())
        line.pop()
    print(" ".join(values))

        
