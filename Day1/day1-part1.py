# Open and read all of the input file
with open("input_day1_part1.txt", "r") as loaded_file:
    filecontents = loaded_file.read()
# Initialize basic variables
floorups = 0
floordowns = 0
# Now count the number of open and close parens
for character in filecontents:
    if character == '(':
        floorups += 1
    elif character == ')':
        floordowns += 1
# Print out the final result
print (floorups - floordowns)
