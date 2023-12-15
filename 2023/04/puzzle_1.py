import re

total = 0

with open("input.txt") as file:
    for line in file.readlines():
        winning_numbers = re.search(r"( {1,}\d{1,2}){1,} \|", line.strip()).group(0)[:-2][1:].split()
        drawn_numbers = list(set(re.search(r"\|( {1,}\d{1,2}){1,}", line.strip()).group(0)[1:].split()))

        result = 0
        for number in drawn_numbers:
            if winning_numbers.count(number) > 0:
                result *= 2
                if result == 0:
                    result = 1

        total += result
print(total)
