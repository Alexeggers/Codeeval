import sys

file_name = sys.argv[1]

def bubble_sort(int_list):
    _sorted = []
    int_iter = iter(int_list)
    
    x = next(int_iter)
    try:
        y = next(int_iter)
    except StopIteration:
        return int_list
    
    def compare(x, y):
        bigger, smaller = (x,y) if x > y else (y,x)
        _sorted.append(smaller)
        return bigger
    
    while True:
        try:
            y = compare(x,y)
            x = next(int_iter)
        except StopIteration:
            _sorted.append(y)
            break
        
    return _sorted

with open(file_name, "r") as file:
    for line in file.read().split("\n"):
        to_sort, repeats = [x.strip() for x in line.split("|")]
        to_sort = [int(x) for x in to_sort.split(" ")]
        _sorted = sorted(to_sort)
        for i in range(int(repeats)):
            to_sort = bubble_sort(to_sort)
            if to_sort != _sorted:
                break
        print(" ".join(str(x) for x in to_sort))
