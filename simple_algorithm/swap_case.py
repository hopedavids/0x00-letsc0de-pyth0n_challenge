# You are given a string and your task is to swap cases.
# In other words, convert all lowercase letters to uppercase letters and vice versa.

# Wonder Genya ==> wONDER gENYA
# Anabi Asah
# Emmanuel Davids

# 1. Get the user input in string format
getValue = input("Enter your a word: ")
print(getValue.swapcase())

# 2. cycle through the user input
# for i in getValue:
# # 3. check if it's upercase
#     if i.isupper():
#     # 4. convert to lowercase
#         print(i.lower(), end='')
# #5. check if it's lowercase
#     if i.islower():
#     # 6. convert to upercase
#         print(i.upper(), end='')
# print()