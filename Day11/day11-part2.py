## INPUT START
startPassword = "hxbxwxba"
## INPUT END

# Criteria: Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
def match_criteria1(string):
    # Iterate from 0 to string length minus 3
    for ctr in range(0, len(string) - 3):
        # Take this current character and check the next few
        if (ord(string[ctr]) + 1 == ord(string[ctr + 1])) and (ord(string[ctr]) + 2 == ord(string[ctr + 2])):
          return True
    # No match
    return False

# Criteria: Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
def match_criteria2(string):
    # Go over each character
    for c in string:
        # Check for non-match
        if c == 'i' or c == 'o' or c == 'l':
            return False
    # No matches, means good
    return True

# Criteria: Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz
def match_criteria3(string):
    number_of_occurrences = 0
    ctr = 0 # Loop counter
    # Iterate over the entire string
    while ((ctr < (len(string) - 1)) and (number_of_occurrences != 2)):
        if string[ctr] == string[ctr + 1]:
            ctr += 1 # Increment one over
            number_of_occurrences += 1 # Found a new overlapping occurrence
        # Even though we don't find anything
        ctr += 1 # Iterate
    # See if we found two matches or not
    return (number_of_occurrences == 2)

# Increment string function
def increment_string(string):
    # Make a copy of the string
    string = string
    # Fetch the last character
    last_char = string[-1]
    # Check and/or increment in ASCII
    if last_char == 'z':
        string = increment_string(string[:-1]) + 'a'
    else:
        string = string[:-1] + chr(ord(last_char) + 1)
    # Return the new string
    return string

def main():
    # Entry point; Fetch the input value
    global startPassword
    outputPassword = ""
    # Keep track of count
    count = 0
    # Iterate till we find a new match
    while True:
        outputPassword = increment_string(startPassword)
        if match_criteria1(outputPassword) and match_criteria2(outputPassword) and match_criteria3(outputPassword):
            count += 1 # We found a new match. But we've to find the second match
            if count == 2:
                break
        # Save the output as the new password to iterate over
        startPassword = outputPassword
    # Return the desired string
    print outputPassword

# Call the main
if __name__ == "__main__":
    main()