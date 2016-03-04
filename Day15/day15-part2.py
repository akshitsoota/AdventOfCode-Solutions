## INPUT START
ingredients = [[3, 0, 0, -3, 2],
               [-3, 3, 0, 0, 9],
               [-1, 0, 4, 0, 1],
               [0, 0, -2, 2, 8]]
## INPUT END

def main():
    # Process the input
    highest_score = 0
    # Start looping for each of the ingredients
    for i1 in range(0, 100 + 1):
        for i2 in range(0, 100 - i1 + 1):
            for i3 in range(0, 100 - i1 - i2 + 1):
                i4 = 100 - (i1 + i2 + i3)
                # Calculate calorie count
                calories = ingredients[0][4] * i1 + ingredients[1][4] * i2 + ingredients[2][4] * i3 + ingredients[3][4] * i4;
                if calories != 500:
                    continue # We didn't meet calorie count, continue
                # Now sum all up and see
                capacity = ingredients[0][0] * i1 + ingredients[1][0] * i2 + ingredients[2][0] * i3 + ingredients[3][0] * i4;
                durability = ingredients[0][1] * i1 + ingredients[1][1] * i2 + ingredients[2][1] * i3 + ingredients[3][1] * i4;
                flavor = ingredients[0][2] * i1 + ingredients[1][2] * i2 + ingredients[2][2] * i3 + ingredients[3][2] * i4;
                texture = ingredients[0][3] * i1 + ingredients[1][3] * i2 + ingredients[2][3] * i3 + ingredients[3][3] * i4;
                # Make all negatives to zero
                if capacity < 0 or durability < 0 or flavor < 0 or texture < 0:
                    continue # If we make it zero, essentially it can never be the maximum. Continue and iterate over
                # Now, multiply all together and compare
                multiplication = capacity * durability * flavor * texture
                if multiplication > highest_score:
                    highest_score = multiplication
    # Print the highest score
    print highest_score

if __name__ == "__main__":
    main()