## INPUT START
row_count = 2980
col_count = 3085
## INPUT END

def main():
    max_rc = row_count + col_count # Max bound on both rows and columns to populate values till where it is desired
    # Define the array
    map = [[-1 for __ in range(max_rc)] for _ in range(max_rc)]
    # Keep track of the previous number
    prev = 20151125 # This is the given first code
    on_row = on_col = 1 # We start with row 1 and col 1
    # Iterate over now
    while True:
        # See if we need to break
        if on_row == max_rc or on_col == max_rc: break
        # Now we start calculating
        if on_row == 1 and on_col == 1:
            map[on_row][on_col] = prev # Base case
        else:
            prev = (prev * 252533) % 33554393 # Perform the operation
            map[on_row][on_col] = prev
        # Increment based on position of row and col; Shifting algorithm to get a matrix like:
        # [[1, 3, 6, 10], [2, 5, 9, -1], [4, 8, -1, -1], [7, -1, -1, -1]]
        if on_row > 1:
            on_col += 1
            on_row -= 1
        else:
            on_row = on_col + 1
            on_col = 1
    # Print the desired number
    print map[2978][3083]

# Invoke the main
if __name__ == "__main__":
    main()