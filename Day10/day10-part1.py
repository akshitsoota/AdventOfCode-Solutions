## INPUT START
startString = "1321131112"
## INPUT END

def main():
    # Entry point; Fetch the input value
    global startString
    outputString = ""
    for x in range(0, 40):
        # Iterate over 40 times
        while len(startString) > 0:
            # Count the occurrence of the first character in the string
            first_char = startString[0:1]
            # Find the count
            count = 0
            while startString[count:count+1] == first_char:
                count += 1
            # Add to the output string
            outputString += str(count)      # Output the count
            outputString += str(first_char) # Output the actual number itself
            # Update the startString to finish going over the string
            startString = startString[count:]
        # Update the startString with the outputString
        startString = outputString
        # Clear out the outputString
        outputString = ""
    # Print the desired output
    print len(startString)

if __name__ == "__main__":
    main()