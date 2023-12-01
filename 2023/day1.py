# Advent of Code 2023!
# day 1
def day1():
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    total = 0
    file = open("2023/day1_input.txt")

    for line in file:
        tmp = ""
        for character in range(len(line)):
            if line[character].isnumeric():
                tmp += line[character]
            else:
                for c in range(len(line[character:]) + 1):
                    if line[character:character+c] in nums:
                        tmp += str(int(nums.index(line[character:character+c]) + 1))
        if len(tmp) == 1:
            tmp = tmp + tmp
            tmp = str(tmp)
        else:
            tmp = tmp[0] + tmp[-1]
            tmp = str(tmp)
        total += int(tmp)
    return total

print(day1())
