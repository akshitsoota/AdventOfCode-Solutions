def find_neighbors(grid, r, c):
    return [grid[r - 1][c - 1], grid[r - 1][c], grid[r - 1][c + 1],
                grid[r][c - 1],                     grid[r][c + 1],
            grid[r + 1][c - 1], grid[r + 1][c], grid[r + 1][c + 1]]

def count_on_neighbors(neighbors):
    return reduce(lambda x, y: x + y, neighbors)
    # Sum up all the 1s (Thanks to http://www.python-course.eu/lambda.php)

def main():
    # Create the 100x100 grid; 0 indicating off and 1 indicating on
    grid = [[[0 for ___ in range(102)] for __ in range(102)] for _ in range(101)]
    # 102x102 grids to mark off the boundary table
    # 101 of 102x102 to mark grid after each iteration

    # Read in the file and get the initial config
    with open("input_day18.txt", "r") as file:
        lines = file.readlines()
    lines = [line.replace("\n", "") for line in lines]
    for r in range(1, 101):
        for c in range(1, 101):
            if lines[r - 1][c - 1] == '#':
                grid[0][r][c] = 1
    # Edges are forced on
    grid[0][1][1] = grid[0][1][100] = grid[0][100][1] = grid[0][100][100] = 1 # Forced on
    # Run 100 iterations
    for count in range(1, 101):
        # Before starting an iteration, force all switches to on
        grid[count][1][1] = grid[count][1][100] = grid[count][100][1] = grid[count][100][100] = 1 # Forced on
        # Iterate over each cell and see what happens
        for r in range(1, 101):
            for c in range(1, 101):
                # Check if we're on edge
                if (r == 1 and c == 1) or (r == 1 and c == 100) or (r == 100 and c == 1) or (r == 100 and c == 100):
                    continue # Make no changes to these lights
                # Check grid status
                if grid[count - 1][r][c] == 1:
                    # It was previously on
                    on_neighbors = count_on_neighbors(find_neighbors(grid[count - 1], r, c))
                    if on_neighbors == 2 or on_neighbors == 3:
                        grid[count][r][c] = 1 # It stays on
                    else:
                        grid[count][r][c] = 0 # It turned off
                elif grid[count - 1][r][c] == 0:
                    # It was previously off
                    on_neighbors = count_on_neighbors(find_neighbors(grid[count - 1], r, c))
                    if on_neighbors == 3:
                        grid[count][r][c] = 1 # It stays on
                    else:
                        grid[count][r][c] = 0 # It turned off
    # Count lights on in the 100th iteration
    sum_a_list = lambda x, y: x + y
    sum = 0 # Sum to be returned
    for r in range(1, 101):
        sum += reduce(sum_a_list, grid[100][r])
    # Print it out
    print sum

# Invoke the main
if __name__ == "__main__":
    main()