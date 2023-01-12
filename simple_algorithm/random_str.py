# Write a script that convert the string to an acronyms. 
# Example: Random Acess Memmory = RAM
# united states America = USA

# PSEUDO CODE
# 1. Get input from the user: random access memory 
get_str = input("Kindly enter your words to be abbreviated: ")
# 2. Converts user input capital letters 
to_caps = get_str.upper()
to_sep = to_caps.split()
# 3. iterate through the list
for z in to_sep: 
    # 4. print out the first character of the list and include a dot
    print(z[0], end='')

# 5. include a new line
print()
# iteration, deal with spaces, newline, maybe include dot, convert to caps   