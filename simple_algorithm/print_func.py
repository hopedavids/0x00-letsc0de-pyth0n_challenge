# You are given the firstname and lastname of a person on two different lines. 
# Your task is to read them and print the following:

# Hello firstname lastname! You just delved into python.
# Sample Input 0
# Ross
# Taylor

# Sample Output 0
# Hello Ross Taylor! You just delved into python.

firstName = "Ross"
lastName = "Taylor"

# concatenate
fullName = firstName + " " + lastName

print(f"Hello {fullName}!")
print(f"Hello {firstName} {lastName}!")


print("Hello {}!".format(fullName))