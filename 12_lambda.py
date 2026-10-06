# Lambda -> Anonymous Function -> Nameless Function
# Lambdas are single line expressions.
# Easy to write and deploy for collection operations.
#---------------------------------------------------

# perform addition of two numbers:

addition = lambda num1, num2: num1+num2

# print(addition(3, 4))

# Reverse a string
reverse_string = lambda txt: txt[::-1]
# print(reverse_string("PUNE"))

# ----------- map with lambda:
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

square = list(map(lambda num:num**2, nums))
# print(square)

str1 = "HELLO"
ascii_codes = list(map(lambda char: ord(char), str1))
# print(ascii_codes)

#-----------filter with lambda
numbers = [23, 45, 66, 90, 89, 12, 34, 77]
evens = list(filter(lambda num: num if num%2 == 0 else None, numbers))
# print(evens)

str2 = "A*e10P/-f"
sp_chars = list(filter(lambda char: char if not(char.isalnum()) else None, str2))
# print(sp_chars)

#------------------reduce with lambda
nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
from functools import reduce

total = reduce(lambda num1, num2: num1+num2, nums1)
# print(total)

chars = ["A", "P", "P", "L", "E"]

str11 = reduce(lambda char1, char2: char1+char2, chars)
# print(str11)

#-------------sorted with lambda
fruits = ["Banana", "Tea", "Apple", "Grapes", "Dragon Fruit"]
# fruits.sort()
# print(fruits)

# sorted_fruits = sorted(fruits, key=lambda word: len(word))
# print(sorted_fruits)

