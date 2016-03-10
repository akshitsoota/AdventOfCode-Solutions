def main():
    # Process the top part of the file by opening the file
    map = {}
    # Process the file
    with open("input_day19.txt", "r") as open_file:
        for line in open_file:
            # Check if line is blank
            if len(line.strip()) == 0:
                break # Exit this processing loop
            # For each of the top lines; Process the line
            line_from = line.split(" => ")[0]
            line_to = line.strip().split(" => ")[1]
            # Check if line_from exists in the map or not
            if line_from in map:
                # Add to existing map at that spot
                map[line_from].add(line_to)
            else:
                # Doesn't exist in the map. Add value by adding a list
                map[line_from] = {line_to}
        # We've reached here
        unique_molecules = []
        for line in open_file:
            if len(line) == 0:
                continue
            # Now we've got our line; Go character by character and replace each character with our map representation
            position_in_line = 0
            for char in line:
                # If we find this character in our map
                if char in map:
                    # Iterate over the set
                    for to_replace_to in map[char]:
                        new_string = line[0:position_in_line] + to_replace_to + line[position_in_line+1:]
                        # Once we've resolved our new string, see if it is in our list or not
                        if not new_string in unique_molecules:
                            unique_molecules.append(new_string)
                # Increment position in the line
                position_in_line += 1
            # Now go two characters at a time and replace the pair with our map representation
            for pos in range(len(line) - 1):
                pair = line[pos:pos+2]
                # If we find a pair in our map
                if pair in map:
                    # Iterate over the set
                    for to_replace_to in map[pair]:
                        new_string = line[0:pos] + to_replace_to + line[pos+2:]
                        # Once we've resolved our new string, see if it is in our list or not
                        if not new_string in unique_molecules:
                            unique_molecules.append(new_string)
        # Finally, return our desired count
        print len(unique_molecules)


# Invoke the main
if __name__ == "__main__":
    main()
