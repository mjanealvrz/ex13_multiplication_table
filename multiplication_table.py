# Print multiplication table from 1 to 10

# Pseudocode

# Print starting point 
print("Multiplcation Table for 1 to 10 ") 

# Create a for loop for multiplicand 
for multiplicand in range (1, 11):

# Start a nested loop for each number from 1 to 10 as the multiplier
    for multiplier in range(1, 11):

        # PRINT multiplicand, "*", multiplier, "=", result
        print(multiplicand * multiplier, end = " ")
    print("\t\t")

