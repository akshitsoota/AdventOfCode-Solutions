# Initialize the 2D Array
lights_on_brightness = [[0 for x in range(0, 1000)] for x in range(0, 1000)]
# Start reading the file
with open("input_day6.txt", "r") as input_file:
    for line in input_file:
        # Remove line \n
        line = line.replace("\n", "")
        # Start processing the lines of the file
        method = -1;
        if line.startswith("turn off"):
            startindex = 9
            method = 0 # Turn off
        elif line.startswith("toggle"):
            startindex = 7
            method = 1 # Toggle
        elif line.startswith("turn on"):
            startindex = 8
            method = 2 # Turn on
        # Extract the remainder of the string
        firsthalf = line[startindex:]
        # Extract the first and second pair of coordinates
        first_coords = firsthalf[:firsthalf.index(" through ")]
        second_coords = firsthalf[firsthalf.index(" through ") + len(" through "):]
        # Extract the coords
        x_start = int(first_coords[:first_coords.index(",")])
        y_start = int(first_coords[first_coords.index(",") + 1:])
        x_end = int(second_coords[:second_coords.index(",")]) + 1
        y_end = int(second_coords[second_coords.index(",") + 1:]) + 1
        # Now run the loop
        for i in range(x_start, x_end):
            for j in range(y_start, y_end):
                if method == 0:
                    lights_on_brightness[i][j] -= 1 # Turing off decreases brightness by 1
                    if lights_on_brightness[i][j] < 0:
                        lights_on_brightness[i][j] = 0
                elif method == 1:
                    lights_on_brightness[i][j] += 2 # Toggle increases brightness by 2
                elif method == 2:
                    lights_on_brightness[i][j] += 1 # Turning on increases brightness by 1
# Now count the number of lights on
total_lights_on_brightness = 0
for i in range(0, 1000):
    for j in range(0, 1000):
        total_lights_on_brightness += lights_on_brightness[i][j]
# Print out the results
print total_lights_on_brightness