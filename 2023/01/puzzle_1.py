from typing import Any


f = open("input.txt", "r")

returnValue = 0


def getfirstnumber(line):
    for letter in line:
        if letter.isdecimal():
            return letter
        else:
            continue


def getlasnumber(line):
    for letter in line[::-1]:
        if letter.isdecimal():
            return letter
        else:
            continue


for line in f:
    current_value = f"{getfirstnumber(line)}{getlasnumber(line)}"
    returnValue += int(current_value)

print(returnValue)
