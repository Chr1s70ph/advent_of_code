import re

f = open("input.txt", "r")

sum = 0

for line in f.readlines():
    max_numbers = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    game = line.split()[1].replace(':', '')

    rounds = line.rsplit(':', 1)[1].rsplit(';')

    game_sum = 0

    for index, round in enumerate(rounds):
        current_max_numbers = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        stripped_words = []
        for temp_word in round.split():
            stripped_words.append(re.sub('[^A-Za-z0-9]+', '', temp_word))

        for index, word in enumerate(stripped_words):
            for color in current_max_numbers:
                if color == word:
                    count = stripped_words[index - 1]
                    if int(count) > current_max_numbers[color]:
                        current_max_numbers[color] = int(count)

        for color in max_numbers:
            if int(current_max_numbers[color]) > int(max_numbers[color]):
                max_numbers[color] = int(current_max_numbers[color])

    for color in max_numbers:
        if max_numbers[color] != 0:
            if game_sum == 0:
                game_sum += max_numbers[color]
            else:
                game_sum *= max_numbers[color]

    sum += game_sum

print(sum)
