import re

instructions = []

with open("input8.txt", "r") as file:
    for line in file:
        instructions.append(line.strip())

def part1(instructions):
    seen = set()
    acc = 0
    i = 0
    while i < len(instructions):
        if (instructions[i], i) in seen:
            return acc
        else:
            seen.add((instructions[i], i))
            code = instructions[i][0:3]
            sign = instructions[i][4:5]
            if sign == '+':
                value = int(instructions[i][5:])
            else:
                value = int(instructions[i][5:]) * -1
            
            if code == 'jmp':
                i += value
            elif code == 'acc':
                acc += value
                i += 1
            else:
                i += 1
    return acc

def part2Helper(instructions):
    seen = set()
    acc = 0
    index = 0
    while True:
        if index in seen:
            return False, acc
        code = instructions[index][0:3]
        sign = instructions[index][4:5]
        if sign == '+':
            value = int(instructions[index][5:])
        else:
            value = int(instructions[index][5:]) * -1
        seen.add(index)
        if code == 'acc':
            acc += value
        if code == 'jmp':
            index += value
        else:
            index += 1
        if index >= len(instructions):
            return True, acc

def part2(instructions):
    for index, line in enumerate(instructions):
        if 'acc' in line:
            continue
        elif 'nop' in line:
            instructions[index] = line.replace('nop', 'jmp')
        else:
            instructions[index] = line.replace('jmp', 'nop')
        flag, acc = part2Helper(instructions)
        if flag:
            return acc
        else:
            instructions[index] = line

# def part2Helper(instructions, flag, acc):

print(part1(instructions))
print(part2(instructions))