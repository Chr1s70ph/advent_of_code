import re

total = 0

cards = []

with open("input.txt") as file:
    for card_index, line in enumerate(file.readlines()):
        current_card = {
            "winning_numbers": re.search(r"( {1,}\d{1,2}){1,} \|", line.strip()).group(0)[:-2][1:].split(),
            "drawn_numbers": list(set(re.search(r"\|( {1,}\d{1,2}){1,}", line.strip()).group(0)[1:].split())),
            "count": 1
        }
        cards.append(current_card)

for index, card in enumerate(cards):
    result = 0
    for number in card["drawn_numbers"]:
        if card["winning_numbers"].count(number) > 0:
            result += 1

    for correct_numbers in range(result):
        cards[index + 1 + correct_numbers]["count"] += 1 * cards[index]["count"]

total_cards = 0

for card in cards:
    total_cards += card["count"]


print(total_cards)
