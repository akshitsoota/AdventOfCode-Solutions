def count_chars(str):
    ret = 0
    # Accept the string and loop over like we do
    while len(str) > 0:
        ret += 1
        str = str[1:]
    # Return the desired value
    return ret

def main():
    chars_in_new = chars_in_old = 0
    # Open the file and go through line by line
    with open("input_day8.txt", "r") as file:
        for line in file:
            # Read the line; First strip off the \n
            oldline = newline = line.replace("\n", "")
            # Encode the string
            newline = newline.replace("\\", "\\\\").replace("\"", "\\\"")
            newline = "\"" + newline + "\""
            # Go character by character
            chars_in_new += count_chars(newline)
            chars_in_old += count_chars(oldline)
    # Output the desired answer
    print (chars_in_new - chars_in_old)

if __name__ == "__main__":
    main()