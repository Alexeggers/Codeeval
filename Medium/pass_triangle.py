##import sys
##
##
####file_name = sys.argv[1]
##file_name = "mad_tree.txt"
##tree = []
##result = 0
##
##
##def add_together(tree_index, level_index, total):
##    total += tree[tree_index][level_index]
####    print("Current total: " + str(total))
####    print("Current tree index: " + str(tree_index))
####    print("Current level index: " + str(level_index))
##    if tree_index == len(tree) - 1:
##        return total
##    else:
##        if level_index > 0 and level_index < len(tree[tree_index + 1]) - 1:
##            return add_together(tree_index + 1, level_index - 1, total) if tree[tree_index + 1][level_index - 1] > tree[tree_index + 1][level_index] else add_together(tree_index + 1, level_index, total)
##        elif level_index > 0:
##            return add_together(tree_index + 1, level_index - 1, total)
##        else:
##            return add_together(tree_index + 1, level_index, total)
##
##
##with open(file_name, "r") as file:
##    for line in file.read().split("\n"):
##        tree.append([int(x) for x in line.strip().split(" ")])
##tree = tree[::-1]
##for index in range(len(tree)):
##    temp_result = add_together(0,index,0)
####    print(temp_result)
##    if result < temp_result:
##        result = temp_result
##print(result)

import sys

with open("mad_tree.txt", 'r') as input:
    test_cases = input.read().strip().splitlines()

triangle = [[int(n) for n in l.split()] for l in test_cases if l]

for row in range(len(triangle) - 1, -1, -1):
    for number in range(len(triangle[row]) - 1):
        chosen = max(triangle[row][number] + triangle[row - 1][number], triangle[row][number + 1] + triangle[row - 1][number])
        triangle[row - 1][number] = chosen

print(triangle[0][0])
