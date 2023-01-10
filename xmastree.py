# Write a program to print out the christmas tree given the height of the tree.

    #   
   ###         
  #####       height_tree = 5
 #######
    #

# PSEUDO-CODE
# ================
# 1 hash =  4 spaces
# 3 hashes = 3 spaces
# 5 hashes = 2 spaces
# 7 hashes = 1 space
# 1 hash = 4 spaces

#1. Get your input for the height of the tree
height_tree = input("Enter the height of the tree: ")

#2. Ensure that input is integer
height_tree = int(height_tree) 

#3. Declare my variables for the hashes and for the spaces
spaces = ((height_tree) - 1)
stem_spaces = ((height_tree) - 1)
hashes = 1

#4. write a a while loop to validate height of the tree is not zero
while height_tree != 0:

#5. use a for loop to for the spaces and hashes
    for i in range(spaces):
        print(" ", end="")
    for j in range(hashes):
        print("#", end="")
    print()
    spaces -= 1
    hashes += 2
    height_tree -= 1 

for k in range(stem_spaces):
    print(" ", end="")
print("#")