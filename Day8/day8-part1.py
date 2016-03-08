def main():
    chars_of_code = 0
    chars_in_memo = 0
    # Open the file and go through line by line
    with open("input_day8.txt", "r") as file:
        for line in file:
            # Read the line; First strip off the \n
            line = line.replace("\n", "")
            # Add for the quotes and strip them off
            chars_of_code += 2
            line = line[1:-1]
            # Go character by character
            while len(line) > 0:
                if line[0] == '\\' and line[1] == '\\':
                    # Double backslash
                    line = line[2:]
                    chars_of_code += 2 # Two characters of code
                    chars_in_memo += 1 # One character in memory
                elif line[0] == '\\' and line[1] == '\"':
                    # Double quotes
                    line = line[2:]
                    chars_of_code += 2 # Two characters in code
                    chars_in_memo += 1 # One character in memory
                elif line[0] == '\\' and line[1] == 'x':
                    # ASCII code
                    line = line[4:]
                    chars_of_code += 4 # Four characters in code
                    chars_in_memo += 1 # Rendered as one ASCII code in the memory
                else:
                    chars_in_memo += 1 # One character in code
                    chars_of_code += 1 # One character in memory as well
                    line = line[1:]
    # Output the desired answer
    print (chars_of_code - chars_in_memo)

if __name__ == "__main__":
    main()