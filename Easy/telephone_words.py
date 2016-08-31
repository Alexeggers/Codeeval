from sys import argv

file_name = "telephone_words.txt"

buttons = {
    "0": "0",
    "1": "1",
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

with open(file_name, "r") as file:
    for line in (x.strip() for x in file.read().split("\n") if x):

        pass