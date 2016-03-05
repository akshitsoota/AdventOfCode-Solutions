def main():
    # Loop over and compare with each Aunt Sue
    with open("input_day16.txt", "r") as open_file:
        for line in open_file:
            # Start processing the line; Separate based on first colon
            splitted = line.split(":")
            splitted = splitted[1:] # Remove the first element
            former_line = ':'.join([str(x) for x in splitted]).strip()
            # Split based on colons
            splitted = former_line.split(",")
            # Keep track of all of this Aunt's attributes
            children = cats = samoyeds = pomeranians = akitas = vizslas = goldfish = trees = cars = perfumes = -1
            # -1 implies value isn't know; Loop over now
            for split_entity in splitted:
                # Split based on colon and extract number
                name = split_entity.split(":")[0].strip()
                count = int(split_entity.split(":")[1].strip())
                # Add to necessary count
                if name == "children": children = count
                if name == "cats": cats = count
                if name == "samoyeds": samoyeds = count
                if name == "pomeranians": pomeranians = count
                if name == "akitas": akitas = count
                if name == "vizslas": vizslas = count
                if name == "goldfish": goldfish = count
                if name == "trees": trees = count
                if name == "cars": cars = count
                if name == "perfumes": perfumes = count
            # Check if find a matching aunt
            if ((children == 3 or children == -1) and
                (cats == 7 or cats == -1) and
                (samoyeds == 2 or samoyeds == -1) and
                (pomeranians == 3 or pomeranians == -1) and
                (akitas == 0 or akitas == -1) and
                (vizslas == 0 or vizslas == -1) and
                (goldfish == 5 or goldfish == -1) and
                (trees == 3 or trees == -1) and
                (cars == 2 or cars == -1) and
                (perfumes == 1 or perfumes == -1)):

                print line.split(":")[0]
                return

if __name__ == "__main__":
    main()