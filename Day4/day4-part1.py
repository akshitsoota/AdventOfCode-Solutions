import hashlib

# Base input
base_input = "yzbqklnj"
# Start looping over and check
number = 1
while True:
    find_hash_of = base_input + str(number)
    # Solve for the MD5 hash now
    md5_hash = hashlib.md5(find_hash_of).hexdigest()
    # Now check if we can find the 5 zeros or not
    if md5_hash[:5] == "00000":
        break
    # Increment the number
    number += 1
# Print the input string that works now
print number