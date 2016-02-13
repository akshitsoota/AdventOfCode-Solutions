nice_lines_count = 0
# Iterate over each line in the input file
with open("input_day5.txt", "r") as input_file:
    for line in input_file:
        # Get rid of \n
        line = line.replace("\n", "")
        # Vowel count
        vowel_count = 0
        if 'a' in line: vowel_count = line.count('a')
        if 'e' in line: vowel_count += line.count('e')
        if 'i' in line: vowel_count += line.count('i')
        if 'o' in line: vowel_count += line.count('o')
        if 'u' in line: vowel_count += line.count('u')
        # Check vowel count with required number
        if vowel_count < 3:
            continue;
        # Twice in a row check
        twice_in_a_row = False
        for char_index in range(len(line)):
            if char_index != (len(line) - 1):
                if line[char_index] == line[char_index + 1]:
                    twice_in_a_row = True
                    break
        # Check if twice a row was satisfied or not
        if not twice_in_a_row:
            continue
        # Finally check that the strings don't exist
        if "ab" in line: continue
        if "cd" in line: continue
        if "pq" in line: continue
        if "xy" in line: continue
        # Nothing failed => NICE string
        nice_lines_count += 1
# Output the required count
print nice_lines_count