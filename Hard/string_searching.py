from sys import argv
import re

normal_pattern = re.compile(r"(?<!\\)\*")
file_name = "string_searching.txt"

with open(file_name, "r") as file:
    for line in (x.strip() for x in file.read().split("\n") if x):
        text, regex = [x.strip() for x in line.split(",")]
        regex = re.sub(normal_pattern, ".*", regex)
        if re.match(regex, text) or regex in text:
            print("true")
        else:
            print("false")