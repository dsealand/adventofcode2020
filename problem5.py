import re

list1 = []

with open("input5.txt", "r") as file:
    for line in file:
        list1.append(line.strip())

def part1(input):
    maxID = 0
    for seat in input:
        row = 0
        col = 0
        for i in range(0,7):
            zone = seat[i:i+1]
            if zone == 'B':
                row += 64/(2**i)

        for i in range(0, 3):
            zone2 = seat[i+7:i+8]
            if zone2 == 'R':
                col += 4/(2**i)
        
        seatID = row * 8 + col
        if seatID > maxID:
            maxID = seatID    

    return maxID

def part2(input):
    IDs = []
    for seat in input:
        row = 0
        col = 0
        for i in range(0,7):
            zone = seat[i:i+1]
            if zone == 'B':
                row += 64/(2**i)

        for i in range(0, 3):
            zone2 = seat[i+7:i+8]
            if zone2 == 'R':
                col += 4/(2**i)
        
        seatID = row * 8 + col
        IDs.append(seatID)

    sortedIDs = sorted(IDs)
    seatID = 0
    for i in range(len(sortedIDs)-1):
        if sortedIDs[i+1] - sortedIDs[i] == 2:
            seatID = sortedIDs[i] + 1
    return seatID

print(part1(list1))
print(part2(list1))
