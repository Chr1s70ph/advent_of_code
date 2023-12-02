numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}

f = open("input.txt", "r")


def getfirstnumber(line) -> tuple[int, int]:
    for index, letter in enumerate(line):
        if letter.isdecimal():
            return int(letter), int(index)
        else:
            continue
    return -1, -1


def getlastnumber(line) -> tuple[int, int]:
    for index, letter in enumerate(line[::-1]):
        if letter.isdecimal():
            return int(letter), int(index)
        else:
            continue
    return -1, -1


def replace_first_number_in_string(string):
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    candidates = [string]
    for number in numbers:
        temp_number = string.replace(number, str(numbers.index(number)))
        if temp_number != string:
            if getfirstnumber(string)[1] == -1 and getfirstnumber(temp_number)[1] != -1:
                candidates.append(temp_number)
                continue
            if getfirstnumber(temp_number)[1] <= getfirstnumber(string)[1]:
                candidates.append(temp_number)

    current_canidate = ""
    for candidate in candidates:
        if getfirstnumber(current_canidate)[1] == -1 and getfirstnumber(candidate)[1] != -1:
            current_canidate = candidate
            continue
        if getfirstnumber(candidate)[1] <= getfirstnumber(current_canidate)[1]:
            current_canidate = candidate
    return current_canidate


def replace_last_number_in_string(string):
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    candidates = [string]
    for number in numbers:
        temp_number = string.replace(number, str(numbers.index(number)))
        if temp_number != string:
            if getlastnumber(string)[1] == -1 and getlastnumber(temp_number)[1] != -1:
                candidates.append(temp_number)
                continue
            if getlastnumber(temp_number)[1] <= getlastnumber(string)[1]:
                candidates.append(temp_number)

    current_canidate = ""
    for candidate in candidates:
        if getlastnumber(current_canidate)[1] == -1 and getlastnumber(candidate)[1] != -1:
            current_canidate = candidate
            continue
        if getlastnumber(candidate)[1] <= getlastnumber(current_canidate)[1]:
            current_canidate = candidate
    return current_canidate


def w2n(number):
    firststring = replace_first_number_in_string(number)
    secondstring = replace_last_number_in_string(firststring)
    return secondstring


double_words = {
    "oneight": "18",
    "threeight": "3e8",
    "twone": "21",
    "fiveight": "58",
    "sevenine": "79",
    "eightwo": "82",
    "eighthree": "83",
    "nineight": "98"
}


returnValue = 0

for line in f:
    for word in double_words:
        line = line.replace(word,  double_words[word])
    replaced_line = w2n(line)
    current_value = f"{getfirstnumber(replaced_line)[0]}{getlastnumber(replaced_line)[0]}"
    returnValue += int(current_value)

print(returnValue)
