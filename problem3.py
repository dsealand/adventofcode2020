list1 = []

with open("input3.txt", "r") as file:
    for line in file:
        row = []
        for char in line.strip():
            row.append(char)
        list1.append(row)

def part1(input):
    count = 0
    x = 0
    y = 0
    while y < len(input):
        if input[y][x % len(input[0])] == '#':
            count += 1
        y += 1
        x += 3
    return count
    
def part2(input, xSlope, ySlope):
    count = 0
    x = 0
    y = 0
    while y < len(input):
        if input[y][x % len(input[0])] == '#':
            count += 1
        y += ySlope
        x += xSlope
    return count

print(part1(list1))

total = part1(list1)
slopes = [[1,1],[5,1],[7,1],[1,2]]
for slope in slopes:
    total = total * part2(list1, slope[0], slope[1])

print(total)