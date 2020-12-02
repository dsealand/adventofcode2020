list1 = []

with open("input1.txt", "r") as file:
    for line in file:
        list1.append(int(line.strip()))

print(list1)

def part1(input):
    set1 = set()

    for i in input:
        if (2020 - i) in set1:
            return (2020 - i) * i
        else:
            set1.add(i)

def part2(input):
    set2 = set()

    for i in input:
        for j in input:
            if (2020 - i - j) in set2:
                return (2020 - i - j) * i * j
            else:
                set2.add(j)


print(part1(list1))
print(part2(list1))