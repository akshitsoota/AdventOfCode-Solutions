def calculate_happiness(list_of_people_seated, info):
    # Let us calculate the total happiness
    happiness_index = 0
    # SPECIAL CASE: The first person in the list because his happiness is calculated by wrapping around to the last
    #  person as well as this is a circular table
    happiness_index += info[list_of_people_seated[0]][list_of_people_seated[-1]] + \
                       info[list_of_people_seated[-1]][list_of_people_seated[0]]
    # Loop over all the people
    person_index = 0
    for person in list_of_people_seated:
        if person_index == 0:
            happiness_index += info[person][list_of_people_seated[person_index + 1]]  # Just look forward
        elif person_index == len(list_of_people_seated) - 1:
            happiness_index += info[person][list_of_people_seated[person_index - 1]]  # Just look backwards
        else:
            happiness_index += info[person][list_of_people_seated[person_index + 1]] + \
                               info[person][list_of_people_seated[person_index - 1]]
            # Look both forward and backwards
        # Increment the person_index
        person_index += 1
    # Return the desired value
    return happiness_index

def recursive_helper(list_of_people_seated, info):
    # BASE CASE: We've got all the people seated, return
    if len(list_of_people_seated) == len(info):
        # We've got the number of people in the list as the number of keys in the info
        #  dictionary, then return the list itself
        return [calculate_happiness(list_of_people_seated, info), list_of_people_seated]
    # Start processing based on the last person seated
    last_person_seated = list_of_people_seated[-1]
    # Now make a dictionary of people if seated next to the net happiness
    happiness_dict = {}
    for key in info:
        # If he/she is not seated already, calculate the net happiness and add to the happiness
        #  dictionary
        if not key in list_of_people_seated:
            happiness_dict[key] = info[last_person_seated][key] + info[key][last_person_seated]
    # Now find the most happiness achieved by going through the dict
    highest_happiness_achieved = -1
    highest_happiness_achieved_at = None
    for key in happiness_dict:
        # See if we already have one or not
        if highest_happiness_achieved == -1:
            # Save this one
            highest_happiness_achieved = happiness_dict[key]
            highest_happiness_achieved_at = key
        # Else, compare and see if worth it or not
        if highest_happiness_achieved < happiness_dict[key]:
            # Save this better one
            highest_happiness_achieved = happiness_dict[key]
            highest_happiness_achieved_at = key
    # Add and proceed with the recursive call
    list_of_people_seated_copy = list_of_people_seated[:]  # Make a copy
    list_of_people_seated_copy.append(highest_happiness_achieved_at)  # Add the new person
    return recursive_helper(list_of_people_seated_copy, info)  # Recursively call till we fill the table


def recursive(info):
    list_of_happiness = []
    # Start processing the information
    for key in info:
        # Try adding a different person as the first guy added and proceed to build the table
        list_of_happiness.append(recursive_helper([key], info))
    # Return the required value
    return list_of_happiness


def main():
    information = {}
    # Read the file and form a dictionary
    with open("input_day13.txt") as open_file:
        for line in open_file:
            # Start processing the line
            splitted = line.split("\n")[0].split(" ")  # Split based on spaces
            # Check if the first name is in the dict
            if not splitted[0] in information:
                information[splitted[0]] = {}
            # Now process and add the rest
            if splitted[2] == "gain":
                information[splitted[0]][splitted[10][:-1]] = int(splitted[3])
            elif splitted[2] == "lose":
                information[splitted[0]][splitted[10][:-1]] = -1 * int(splitted[3])
    # Send the call to the recursive function
    list_of_happiness = recursive(information)
    # Find and print the minimum to solve for the optimum happiness
    print max([x[0] for x in list_of_happiness])

# Invoke the main
if __name__ == "__main__":
    main()