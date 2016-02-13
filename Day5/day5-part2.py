nice_lines_count = 0
# Iterate over each line in the input file
with open("input_day5.txt", "r") as input_file:
    for line in input_file:
        # Get rid of \n
        line = line.replace("\n", "")

        # Twice in a row check
        letter_between_duplicated = False
        for char_index in range(len(line)):
            if char_index <= (len(line) - 3):
                if line[char_index] == line[char_index + 2] and line[char_index] != line[char_index + 1]:
                    letter_between_duplicated = True
                    break
        # Check if twice a row was satisfied or not
        if not letter_between_duplicated:
            continue

        # Find pair repetitions
        pair_repetitions = False
        for char_index in range(len(line)):
            if char_index <= (len(line) - 3):
                # Calculate the pair
                pair_to_search = str(line[char_index]) + str(line[char_index + 1])
                # Search for this pair over the rest of the string
                if pair_to_search in line[char_index + 2:]:
                    pair_repetitions = True
                    break
        # Check if pair repetitions were found
        if not pair_repetitions:
            continue

        # Else, increment the required count
        nice_lines_count += 1
# Output the required count
print nice_lines_count