from sys import argv

with open("rightmost_char.txt", "r") as file:
    for line in (x.strip() for x in file.read().split("\n") if x):
        try:
            text,char_to_be_found = [x.strip() for x in line.split(",") if x]
        except ValueError:
            continue
        reverse = text[::-1]
        for index, char in enumerate(reverse):
            if char == char_to_be_found:
                print(len(text) - 1 - index)
                break