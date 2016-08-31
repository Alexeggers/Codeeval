from sys import argv


file_name = "trailing_string.txt"

with open(file_name, "r") as file:
    for line in (x.strip() for x in file.read().split("\n") if x):
        text, string = [x.strip() for x in line.split(",")]
        if text[len(text)-len(string):len(text)] == string:
            print("1")
        else:
            print("0")