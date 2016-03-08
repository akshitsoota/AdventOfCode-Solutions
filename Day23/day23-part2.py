def main():
    lines = []
    # Read all the lines
    with open("input_day23.txt", "r") as open_file:
        for line in open_file:
            lines.append(line.strip().replace("\n", "")) # Add the line to the array of lines
    # Setup the registers and now process
    a = 1
    b = line_number = 0
    while True: # Infinitely iterate till we run out of lines to execute
        if line_number >= len(lines) or line_number < 0:
            break # Exit the loop as we're trying to execute lines that are out of range
        # Understand the instruction; Extract the first three characters and the rest of the string
        first_three = lines[line_number][:3]
        rest_string = lines[line_number][4:]
        # Process the instructions now
        continue_to_next = False
        if first_three == "hlf":
            if rest_string == "a": a = a / 2
            if rest_string == "b": b = b / 2
            # Continues to the next instruction
            continue_to_next = True
        elif first_three == "tpl":
            if rest_string == "a": a = a * 3
            if rest_string == "b": b = b * 3
            # Continues to the next instruction
            continue_to_next = True
        elif first_three == "inc":
            if rest_string == "a": a += 1
            if rest_string == "b": b += 1
            # Continues to the next instruction
            continue_to_next = True
        elif first_three == "jmp":
            if rest_string[0] == "+": line_number += int(rest_string[1:])
            if rest_string[0] == "-": line_number -= int(rest_string[1:])
        elif first_three == "jie" or first_three == "jio":
            # Extract register
            register = rest_string[0]
            jump_offset = int(rest_string[3:])
            # Check and proceed
            if first_three == "jie" and ((a % 2 == 0) if register == "a" else (b % 2 == 0)):
                line_number += jump_offset
            elif first_three == "jio" and ((a == 1) if register == "a" else (b == 1)):
                line_number += jump_offset
            else:
                continue_to_next = True
        # See if we've to increment instruction count or not
        if continue_to_next:
            line_number += 1
    # Print the final value as desired
    print b

# Invoke the main
if __name__ == "__main__":
    main()