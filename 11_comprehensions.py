# Comprehension:

    # Comprehensions are single line expressions written inside 
    # collections.

    # Types:
        # List comprehension
# Create a list of all numbers which are divisible by 3 and 7
# in between 1 and 100.

nums_divisible_by_3_and_7 = [num for num in range(1, 100) if num % 3 == 0 and num % 7 == 0]
# print(nums_divisible_by_3_and_7)

        # Tuple comprehension
# Create a tuple containing all special charecters from bellow string.
str1 = "A67Gk %bUf*$ __"

sp_chars_from_str1 = (char for char in str1 if not(char.isalpha()) and not(char.isdigit()))
print(sp_chars_from_str1)

# for num in sp_chars_from_str1:
#     print(num, end="")

        # set comprehension

# Write a program to get all those charecters from str2 
# whicha are capital alphabets, but make sure the collection
# not containing duplicates.

str1 = "NAyaNTAeA RavANa"
caps = {char for char in str1 if (char.isalpha() and char.isupper())}
print(caps)

        # dict comprehension

# create a dictioonary of number and its cube 
# from 1 to 10

# dict = {num:num**3 for num in range(1, 11)}
# print(dict)