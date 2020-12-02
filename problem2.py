import re

list1 = []

with open("input2.txt", "r") as file:
    for line in file:
        list1.append(line.strip())

def problem1(input):
    validCount = 0
    for line in input:
        splitString = re.split("-| |:", line)
        lowerBound = int(splitString[0])
        upperBound = int(splitString[1])
        char = splitString[2]
        password = splitString[4]
        charCount = 0
        for i in password:
            if i == char:
                charCount += 1
        if charCount >= lowerBound and charCount <= upperBound:
            validCount += 1
    return validCount

def problem2(input):
    validCount = 0
    for line in input:
        splitString = re.split("-| |:", line)
        lowerIndex = int(splitString[0])
        upperIndex = int(splitString[1])
        char = splitString[2]
        password = splitString[4]
        charCount = 0
        if (password[lowerIndex - 1] == char) != (password[upperIndex - 1] == char):
            validCount += 1
    return validCount

print(problem1(list1))
print(problem2(list1))