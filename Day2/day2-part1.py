# Basic storage variables
total_required_paper = 0
# Start by reading the file line by line
with open("input_day2_part1.txt", "r") as open_file:
    for file_line in open_file:
        # Get rid of the trailing \n character
        file_line = file_line.replace("\n", "")
        # Move onto extract the sides
        lwh = file_line.split("x")
        l = int(lwh[0])
        w = int(lwh[1])
        h = int(lwh[2])
        # Now solve for each of the areas
        lw = l * w
        wh = w * h
        lh = l * h
        # Find minimum area
        if (lw < wh) and (lw < lh):
            min_area = lw
        elif wh < lh:
            min_area = wh
        else:
            min_area = lh
        # Once we've done that calculate the required wrapping paper for this line
        wrapping_paper_required = 2*lw + 2*wh + 2*lh + min_area
        # Add to the total and continue
        total_required_paper += wrapping_paper_required

# Print the total required now
print total_required_paper