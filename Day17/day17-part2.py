## INPUT START
list_of_numbers = [50, 44, 11, 49, 42, 46, 18, 32, 26, 40, 21, 7, 18, 43, 10, 47, 36, 24, 22, 40]
total_to_form = 150
## INPUT END

def recursive(choice_of_numbers, number_to_form):
    # BASE CASE: number_to_form == 0
    if number_to_form == 0:
        return [[]] # Return a list with just an empty list as no other numbers are needed to form the combination
    # Find the minimum from the list and see if the number to form is less than that or what OR
    # if the number we're trying to form is negative
    if number_to_form < 0 or min(choice_of_numbers) > number_to_form:
        return False # We cannot form the desired number
    # Holds the list of possible combinations
    possible_combinations = []
    # Pick each item in the list and start forming a new combination
    number_index = 0
    for number in choice_of_numbers:
        if number == 0:
            number_index += 1 # New code: we'll now be processing the next number in the list
            continue # New code skips over if we find a zero as that cannot possibly form the combination
        # Remove this number and recursively call
        new_choice_of_numbers = choice_of_numbers[:] # Make a copy / clone it
        ## new_choice_of_numbers.remove(number) # Old code to remove the number
        new_choice_of_numbers[number_index] = 0 # New code replaces the number at that index to zero
        # Recursively call now
        return_value = recursive(new_choice_of_numbers, number_to_form - number)
        # See what the return value was
        if return_value != False:
            # We got a valid response from the recursive call; Recursively add the number to each list in return_value
            for list_obj in return_value:
                # Form a new list
                ## to_add = [number] # Old code to add the number to the list itself
                to_add = [number_index] # We are adding the number index here instead of the number itself
                to_add.extend(list_obj)
                # Finally, append to the list
                possible_combinations.append(to_add)
        # Old code didn't contain the following lines
        # Increment the number index
        number_index += 1
    # Return the possible combinations
    return possible_combinations

def main():
    # We will call the recursive function on the input
    output = recursive(list_of_numbers, total_to_form)
    # Sort all the elements of each element
    for ctr in range(len(output)):
        output[ctr].sort()
    # Start to remove the duplicates
    new_output = []
    for list_obj in output:
        if not list_obj in new_output:
            new_output.append(list_obj)
    # Replace old output
    output = new_output
    # Mapping is unnecessary for our output at this point
    # Count it out
    sizes = {}
    for list_obj in output:
        size = len(list_obj)
        # See if exists
        if not size in sizes:
            sizes[size] = 1
        else:
            sizes[size] += 1
    # Print it out
    print len(output), ";", sizes

if __name__ == "__main__":
    main() # Invoke main