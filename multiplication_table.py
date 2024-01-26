# Print multiplication table from 1 to 10

# Pseudocode

# Create a for loop for multiplicand 
for multiplicand in range (1, 11):
# Print "Multiplication Table for " with space
    print("Multiplcation Table for  ",  multiplicand) 
    
# Start a nested loop for each number from 1 to 10 as the multiplier
    for multiplier in range(1, 11):
        # PRINT multiplicand, "*", multiplier, "=", result
        print(multiplicand * multiplier, end = " ")
    print("\t\t")

