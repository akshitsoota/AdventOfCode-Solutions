# Create a 2D Array: 600x600 size, assuming [0][0] on the board is 300x300 on the array
house_map_santa = [[0 for x in range(600)] for x in range(600)]
house_map_robo_santa = [[0 for x in range(600)] for x in range(600)]
# Now start reading the file character by character
with open("input_day3.txt", "r") as loaded_file:
    file_contents = loaded_file.read()
# Initialize Santa's location (Assuming 300x300 is the center of the grid and actually 0x0)
x_s = x_rs = 300
y_s = y_rs = 300
house_map_santa[x_s][y_s] = 1 # Setting to one as that is the starting house AND that MUST be counted
# Once we've read all the contents, read character by character
turn = 0 # 0 => Santa and 1 => Robo-Santa
for character in file_contents:
    if turn == 0:
        if character == '^':
            y_s += 1
            house_map_santa[x_s][y_s] = 1
        elif character == 'v':
            y_s -= 1
            house_map_santa[x_s][y_s] = 1
        elif character == '<':
            x_s -= 1
            house_map_santa[x_s][y_s] = 1
        elif character == '>':
            x_s += 1
            house_map_santa[x_s][y_s] = 1
    elif turn == 1:
        if character == '^':
            y_rs += 1
            house_map_robo_santa[x_rs][y_rs] = 1
        elif character == 'v':
            y_rs -= 1
            house_map_robo_santa[x_rs][y_rs] = 1
        elif character == '<':
            x_rs -= 1
            house_map_robo_santa[x_rs][y_rs] = 1
        elif character == '>':
            x_rs += 1
            house_map_robo_santa[x_rs][y_rs] = 1
    turn = (1 if (turn == 0) else 0)
# Now go through the entire array and count the unique houses Santa has been through
unique_house_count = 0
for i in range(600):
    for j in range(600):
        if (house_map_santa[i][j] == 1) or (house_map_robo_santa[i][j] == 1):
            unique_house_count += 1
# Output the required result
print unique_house_count