import re

list1 = []

with open("input6.txt", "r") as file:
    for line in file:
        list1.append(line)

def part1(input):
    totalCount = 0
    questions = set()
    for entry in input:
        if entry == '\n':
            totalCount += len(questions)
            questions.clear()

        else:
            entry = entry.strip()
            for char in entry:
                if char not in questions:
                    questions.add(char)
    totalCount += len(questions)        
    return totalCount

def part2(input):
    totalCount = 0
    groupSize = 0
    questions = dict()
    for entry in input:
        if entry == '\n':
            for item in questions:
                if questions[item] == groupSize:
                    totalCount += 1
            questions.clear()
            groupSize = 0

        else:
            groupSize += 1
            entry = entry.strip()
            for char in entry:
                if char in questions:
                    questions[char] += 1
                else:
                    questions[char] = 1
    for item in questions:
        if questions[item] == groupSize:
            totalCount += 1
    return totalCount

# print(list1[0:10])
print(part1(list1))
print(part2(list1))