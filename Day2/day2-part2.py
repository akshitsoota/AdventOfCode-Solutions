# Basic storage variables
total_required_ribbon = 0
# Start by reading the file line by line
with open("input_day2_part2.txt", "r") as open_file:
    for file_line in open_file:
        # Get rid of the trailing \n character
        file_line = file_line.replace("\n", "")
        # Move onto extract the sides
        lwh = file_line.split("x")
        l = int(lwh[0])
        w = int(lwh[1])
        h = int(lwh[2])
        # Solve for the perimeters now
        lw_perimeter = 2 * (l + w)
        wh_perimeter = 2 * (w + h)
        lh_perimeter = 2 * (l + h)
        # Find the smallest one now
        if (lw_perimeter < wh_perimeter) and (lw_perimeter < lh_perimeter):
            min_perimeter = lw_perimeter
        elif wh_perimeter < lh_perimeter:
            min_perimeter = wh_perimeter
        else:
            min_perimeter = lh_perimeter
        # Now solve for the ribbon size on this line
        ribbon_size_required = min_perimeter + (l * w * h)
        # Add to the total
        total_required_ribbon += ribbon_size_required

# Print the total required now
print total_required_ribbon