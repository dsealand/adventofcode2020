import re

list1 = ""
list2 = []

with open("input4.txt", "r") as file:
    for line in file:
        list1 += line
list1 = re.split("\n\n", list1)
for passport in list1:
    list2.append(re.split("\n| ", passport))

def part1(input):
    count = 0
    for entry in input:
        fieldCount = 0
        for field in entry:
            key = re.split(":", field)
            print(key[0])
            if key[0] != 'cid' and key[0] != '':
                fieldCount += 1
        print("fieldCount ", fieldCount)
        if fieldCount == 7:
            count += 1
    return count

def part2(input, validEyes):
    count = 0
    
    for entry in input:
        print("\n")
        print(entry)
        validPassport = 0
        for field in entry:
            print(field)
            # validPassport = 0
            key = re.split(":", field)

            if key[0] == 'hcl':
                validHCL = True
                print(key[1])
                if key[1][0] == '#':
                    
                    print(key[1][1:])
                    if len(key[1][1:]) == 6:
                        for char in key[1][1:]:
                            if (ord(char) >= 0 and ord(char) <= 47) or (ord(char) >= 58 and ord(char) <= 96) or (ord(char) >= 103):
                                print(char)
                                print(ord(char))
                                validHCL = False
                else: 
                    validHCL = False
                if validHCL:
                    validPassport += 1
                print(validPassport)
            
            # print(validPassport)
                
            elif key[0] == 'ecl':
                print(key[1])
                if key[1] in validEyes:
                    validPassport += 1
                print(validPassport)
            
            # print(validPassport)

            elif key[0] == 'pid':
                number = re.sub("[^0-9]", "", key[1])
                if len(number) == 9:
                    validPassport += 1
                print(validPassport)

            # print(validPassport)
            
            elif key[0] == 'hgt':
                validHGT = False
                height = int(re.sub("[^0-9]", "", key[1]))
                print(height)
                print(key[1][len(key[1]) - 2:])
                if key[1][len(key[1]) - 2:] == 'cm':
                    if height >= 150 and height <= 193:
                        validHGT = True
                if key[1][len(key[1]) - 2:] == 'in':
                    if height >= 59 and height <= 76:
                        validHGT = True
                if validHGT:
                    validPassport += 1
                print(validPassport)

            # print(validPassport)
            
            elif key[0] == 'byr':
                year = int(key[1])
                if year >= 1920 and year <= 2002:
                    validPassport += 1
                print(validPassport)

            # print(validPassport)

            elif key[0] == 'iyr':
                year = int(key[1])
                if year >= 2010 and year <= 2020:
                    validPassport += 1
                print(validPassport)
            
            elif key[0] == 'eyr':
                year = int(key[1])
                if year >= 2020 and year <= 2030:
                    validPassport += 1
                print(validPassport)

        print(validPassport)
        if validPassport == 7:
            count += 1

    return count


validECL = set()
validECL.add('amb')
validECL.add('blu')
validECL.add('brn')
validECL.add('gry')
validECL.add('grn')
validECL.add('hzl')
validECL.add('oth')

# print(list2)
print(part1(list2))
print(part2(list2, validECL))