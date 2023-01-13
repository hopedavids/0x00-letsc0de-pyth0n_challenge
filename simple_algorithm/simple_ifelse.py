# Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 6 to ,20 print Weird
# If  is even and greater than 24 , print Not Weird

# solutions
#1. Get an integer from the user input
import random
#getInput = int(input("Enter a number: "))
getInput = random.randint(0,1000)
print(getInput)
#2. Convert user input as integer
#3. use modulo to determine the number is odd or even
if (getInput % 2 != 0):
    print("Weird")

elif ((getInput % 2 == 0) and (2 <= getInput <= 5)):
    print("Not Weird")

elif ((getInput % 2 == 0) and (6 <= getInput <= 20)):
    print("Weird")

else:
    if ((getInput % 2 == 0) and (getInput > 24)):
        print("Not Weird")
