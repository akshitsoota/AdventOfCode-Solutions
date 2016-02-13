import sys

# Open and read all of the input file
with open("input_day1_part2.txt", "r") as loaded_file:
    filecontents = loaded_file.read()
# Initialize basic variables
floorups = 0
floordowns = 0
counter = 1
# Now count the number of open and close parens
for character in filecontents:
    if character == '(':
        floorups += 1
    elif character == ')':
        floordowns += 1
    # Calculate the floor Santa is on now
    if (floorups - floordowns) < 0:
        # Santa is in the basement
        print counter
        sys.exit()
    # Increment the counter
    counter += 1