def getJSON(str):
    str = str.strip()  # Remove unnecessary spaces
    # See if we can cast the string to an integer or not
    try:
        int(str)  # Attempt the cast
        return int(str)  # Successful cast; Return the required value
    except ValueError:
        # See what kind is it: JSON Array or JSON Object
        if str[0] == '[' and str[-1] == ']': return getJSONSplitBy(str, '[]')
        if str[0] == '{' and str[-1] == '}': return getJSONSplitBy(str, '{}')
        # Else, return 0
        return 0

def getJSONSplitBy(str, splitby):
    # See how to split and remove it
    if (splitby == '[]' or splitby == '{}') and len(str) > 2:
        splitted = str[1:-1].split(",")
    else:
        # Maybe bad SPLITBY argument or we were given an empty list
        return 0
    # Loop over and fix bad splits
    if splitby == '{}':
        # We loop over by keeping track of the key
        new_key = True  # Defines if we're iterating over a new key or not
        key_in = None  # Defines which key in the JSON Object we are in
        string_working_on = None  # To keep track of the string being built upon
        fixed_split_list = []  # To keep track of the fixed split list
        # Iterate over now
        for val in splitted:
            # Check if its a new key or not
            if new_key:
                # Pull out unnecessary stuff and make necessary variable changes
                key_in = val.split(":")[0][1:-1]  # Solve for the new key
                # See if we should add to the fixed_split_list
                if not '[' in val.split(":")[1] and not '{' in val.split(":")[1]:
                    # Pure number
                    fixed_split_list.append(val.split(":")[1])
                else:
                    # We've a complete string or not a complete string
                    if (val.split(":")[1][0] == '[' and ':'.join(val.split(":")[1:]).count('[') == ':'.join(val.split(":")[1:]).count(']')) or \
                       (val.split(":")[1][0] == '{' and ':'.join(val.split(":")[1:]).count('{') == ':'.join(val.split(":")[1:]).count('}')):
                        # We've got a complete string
                        fixed_split_list.append(':'.join(val.split(":")[1:]))  # Make the list into a string
                    else:
                        # Incomplete string :(
                        new_key = False  # We are no longer looping to find a new key
                        string_working_on = ':'.join(val.split(":")[1:])
            else:
                # Continue adding and see how things go
                string_working_on += "," + val
                # Run a balance check
                if string_working_on.count('[') == string_working_on.count(']') and \
                   string_working_on.count('{') == string_working_on.count('}'):
                    # We're all set, add to the list, reset and go
                    new_key = True  # We will now be looking for a new key
                    fixed_split_list.append(string_working_on)
                    string_working_on = ""  # Reset the string
        # Now add up and return each item in the list's JSON evaluated value by recursively calling getJSON
        mapped_numbers = [getJSON(x) for x in fixed_split_list]
        # Reduce the mapped_numbers to a single number
        return reduce(lambda x, y: x + y, mapped_numbers)
    elif splitby == '[]':
        # We loop over and keep track of unbalanced commas
        string_working_on = None  # To keep track of the string being built upon
        fixed_split_list = []  # To keep track of the fixed split list
        # Iterate now
        for split in splitted:
            # Check if it is entirely a number
            if split.isdigit():
                fixed_split_list.append(split)
            else:
                # Add the string to the building string
                if string_working_on == "" or string_working_on == None:
                    string_working_on = split
                else:
                    string_working_on += "," + split
                # Now check for balance and reset if we've found balance
                if string_working_on.count('[') == string_working_on.count(']') and \
                   string_working_on.count('{') == string_working_on.count('}'):
                    # We're all set, add to the list, reset and go
                    fixed_split_list.append(string_working_on)
                    string_working_on = ""
        # Now add up and return each item in the list's JSON evaluated value by recursively calling getJSON
        mapped_numbers = [getJSON(x) for x in fixed_split_list]
        # Reduce the mapped_numbers to a single number
        return reduce(lambda x, y: x + y, mapped_numbers)

def main():
    # Open and read the file
    with open("input_day12.txt", "r") as open_file:
        for line in open_file:
            print getJSON(line)

# Invoke the main
if __name__ == "__main__":
    main()