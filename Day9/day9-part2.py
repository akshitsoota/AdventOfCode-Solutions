def recursive_helper(calculated_distance, list_of_added_places, list_of_all_places, info_dict):
    # BASE CASE: We've added all the places possible. In that case just return what is expected
    if len(list_of_added_places) == len(list_of_all_places):
        return [calculated_distance, list_of_added_places]
    # Else, find the minimum distance place from the last one added and then recursively call myself
    last_place_added = list_of_added_places[-1]
    max_distance_from_last_place_added_name = None
    max_distance_from_last_place_added_dist = -1
    for place in list_of_all_places:
        if place in list_of_added_places: continue  # We already have this place, skip over it
        # Calculate the distance
        dist = info_dict[last_place_added][place] if last_place_added in info_dict and place in info_dict[last_place_added] else info_dict[place][last_place_added]
        # See if we're on base case
        if max_distance_from_last_place_added_dist == -1:
            # We've found a place that is NOT in our list already AND we don't have a minimum distance as our basis
            # We set this as our maximum distance to compare others with
            max_distance_from_last_place_added_dist = dist  # Checking both ways as distance from A to B = distance from B to A
            max_distance_from_last_place_added_name = place
            continue  # Force another iteration
        # Else, compare
        if max_distance_from_last_place_added_dist < dist:
            # We've found a new minimum
            max_distance_from_last_place_added_dist = dist
            max_distance_from_last_place_added_name = place
    # Now add and call recursively
    list_of_added_places.append(max_distance_from_last_place_added_name)
    return recursive_helper(calculated_distance + max_distance_from_last_place_added_dist, list_of_added_places, list_of_all_places, info_dict)

def recursive(list_of_places, info_dict):
    distances_to_return = []
    # Call our recursive helper for each place in the list of places as the start
    for place in list_of_places:
        distances_to_return.append(recursive_helper(0, [place], list_of_places, info_dict))
    # Return the desired list
    return distances_to_return

def main():
    list_of_places = []
    info_dict = {}
    # Read the information from the file
    with open("input_day9.txt") as open_file:
        for line in open_file:
            # Split up the line
            splitted = line.split("\n")[0].split(" ")
            # Check if the source and dest are in the list_of_places
            if not splitted[0] in list_of_places: list_of_places.append(splitted[0])  # Checks the source
            if not splitted[2] in list_of_places: list_of_places.append(splitted[2])  # Checks for the destination
            # Now add to the dictionary
            if not splitted[0] in info_dict:
                info_dict[splitted[0]] = {} # Make the new dict
            info_dict[splitted[0]][splitted[2]] = int(splitted[4])
    # Now simply process the information
    distances = recursive(list_of_places, info_dict)
    # Find the maximum and print it
    max_distance = max([x[0] for x in distances])
    # Print it
    print max_distance

# Invoke the main
if __name__ == "__main__":
    main()