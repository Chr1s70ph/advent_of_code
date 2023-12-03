import re

f = open("input.txt", "r")

numbers = {
   "red": 0,
   "green": 0,
   "blue": 0
}

max_numbers = {
    "red": 12,
    "green": 13,
    "blue": 14
}

valid_games = 0

for line in f.readlines():
    split_line = line.split()
    game = split_line[1].replace(':', '')

    game_valid = True
    for index, word in enumerate(split_line):
        string = re.sub('[^A-Za-z0-9]+', '', split_line[index])
        for color in numbers:
            if color == string:
                if int(split_line[index - 1]) > max_numbers[color]:
                    game_valid = False
                    break
                numbers[color] += int(split_line[index - 1])
        else:
            continue
        break

    if game_valid:
        valid_games += int(game)
        game_valid = False

    for color in numbers:
        numbers[color] = 0

print(valid_games)
