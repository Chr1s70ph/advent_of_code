def getindicesofnumber(list, starting_index):
    indices = []

    for index, char in enumerate(list[starting_index:]):
        if char.isalnum():
            indices += [index + starting_index]
        else:
            break

    return indices


def getindicesofline(line):
    indices = []
    for number, char in enumerate(line):
        if char.isnumeric() and number not in indices:
            indices += getindicesofnumber(line, number)

    return indices


def setlines(previous_line, current_line, reading_line):
    last_line = []
    for char in reading_line:
        last_line.append(char)
    return (previous_line, current_line, last_line)


input = open("input.txt", "r")
line_length = len(input.readline().strip())


def getadjacenedindices(list_of_indices):
    return_indices = []
    for index in list_of_indices:
        if index > 0:
            return_indices.insert(index, index - 1)
        if index != line_length:
            return_indices.append(index + 1)
        else:
            return_indices.append(index)

    return_indices = list(set(return_indices))
    return_indices.sort()

    return return_indices


previous_line = []
previous_line += ['.'] * len(open("input.txt", "r").readlines()[0].strip())
current_line = previous_line
next_line = previous_line
last_line = previous_line

lines = input.readlines()


print("previous_line                                    ", "current_line                                    ", "next_line")

for index, line in enumerate(lines):
    line = line.strip()
    (previous_line, current_line, next_line) = setlines(current_line, next_line, lines[index].strip())

    indices = getindicesofline(current_line)
    adjacened_indices = getadjacenedindices(indices)

    print(indices)
    print(adjacened_indices)
    print(previous_line, current_line, next_line)

# Extra block, so the last line is respected also
(previous_line, current_line, next_line) = setlines(current_line, next_line, last_line)

indices = getindicesofline(current_line)
adjacened_indices = getadjacenedindices(indices)

print(indices)
print(adjacened_indices)
print(previous_line, current_line, next_line)
