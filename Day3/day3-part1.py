# Create a 2D Array: 600x600 size, assuming [0][0] on the board is 300x300 on the array
house_map = [[0 for x in range(600)] for x in range(600)]
# Now start reading the file character by character
with open("input_day3.txt", "r") as loaded_file:
    file_contents = loaded_file.read()
# Initialize Santa's location (Assuming 300x300 is the center of the grid and actually 0x0)
x = 300
y = 300
house_map[x][y] = 1 # Setting to one as that is the starting house AND that MUST be counted
# Once we've read all the contents, read character by character
for character in file_contents:
    if character == '^':
        y += 1
        house_map[x][y] = 1
    elif character == 'v':
        y -= 1
        house_map[x][y] = 1
    elif character == '<':
        x -= 1
        house_map[x][y] = 1
    elif character == '>':
        x += 1
        house_map[x][y] = 1
# Now go through the entire array and count the unique houses Santa has been through
unique_house_count = 0
for i in range(600):
    for j in range(600):
        if house_map[i][j] == 1:
            unique_house_count += 1
# Output the required result
print unique_house_count