import re
from typing import Dict, Tuple

list1 = []
seenCache = Dict[Tuple[str, str], bool]

with open("input7.txt", "r") as file:
    for line in file:
        list1.append(line.strip())

def readRules(input):
    bagDict = dict()
    for rule in input:
        rule = re.split(" contain ", rule)
        bag = rule[0][:-5]
        bagDict[bag] = dict()
        contains = re.split(",", rule[1])
        for rule in contains:
            rule = rule.strip()
            rule = re.split(" ", rule)
            if rule[0] != 'no':
                bagNum = int(rule[0])
                bagColor = rule[1] + " " + rule[2]
                (bagDict[bag])[bagColor] = bagNum
    return bagDict

def part1(input):
    bagDict = readRules(input)
    return sum(bagFinder(bagDict, 'shiny gold', bag) for bag in bagDict)

def part2(input):
    bagDict = readRules(input)
    return bagCounter(bagDict, 'shiny gold')

def bagFinder(bagDict, targetBag, outerBag, cache: seenCache = {}) -> bool:
    if (targetBag, outerBag) in cache:
        return cache[(targetBag, outerBag)]
    else:
        for innerBag in bagDict[outerBag]:
            if innerBag == targetBag:
                cache[(targetBag, outerBag)] = True
                return True
            elif bagFinder(bagDict, targetBag, innerBag):
                cache[(targetBag, innerBag)] = True
                return True
    return False

def bagCounter(bagDict, targetBag):
    innerBags = bagDict[targetBag]
    return sum(innerBags.values()) + sum((bagCounter(bagDict, innerBag) * innerBags[innerBag]) for innerBag in innerBags)


print(part1(list1))
print(part2(list1))

