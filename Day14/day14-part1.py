## INPUT START

# We keep track of each reindeer's speed, time it can travel and rest time before flying again
reindeers = [[22, 8, 165],
             [8, 17, 114],
             [18, 6, 103],
             [25, 6, 145],
             [11, 12, 125],
             [21, 6, 121],
             [18, 3, 50],
             [20, 4, 75],
             [7, 20, 119]]

total_time = 2503

## INPUT END

def main():
    # Entry point; Setup a state for each reindeer
    state = [[0, 1, 0] for ctr in range(len(reindeers))]
    # We keep state as: total distance covered, flying (1) or sleeping (2) and time spent doing any activity
    for time in range(total_time):
        # For each second, go through each reindeer
        ctr = 0 # Counter to keep track of which reindeer we are one
        for ctr in range(len(reindeers)):
            # Loop over and start doing stuff
            # STEP 1: Check state
            if state[ctr][1] == 1:
                # Given reindeer is flying. See for how many seconds it has been flying and do necessary actions
                if state[ctr][2] == reindeers[ctr][1]:
                    # We've maxed out travel time, now goto sleep mode
                    state[ctr][1] = 2 # Now sleeping
                    state[ctr][2] = 1 # Reset timer
                else:
                    state[ctr][0] += reindeers[ctr][0] # It has flown by that much distance this second
                    state[ctr][2] += 1 # It has spent one second flying
            elif state[ctr][1] == 2:
                # Given reindeer is sleeping. See for how many seconds it has been sleeping and do necessary actions
                if state[ctr][2] == reindeers[ctr][2]:
                    # We've maxed out sleep time, now goto flying mode
                    state[ctr][0] += reindeers[ctr][0] # We've flown this distance
                    state[ctr][1] = 1 # Now flying
                    state[ctr][2] = 1 # Reset timer
                else:
                    # Keep sleeping
                    state[ctr][2] += 1 # It has spent one more second sleeping
    # Print out the final stats
    print max([x[0] for x in state])

if __name__ == "__main__":
    main() # Call the main