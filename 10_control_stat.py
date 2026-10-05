# Control stat:
    
    # while:
        # More Manual
        # Gives more control to developer
         
    # for:
        # More Automatic
        # Gives les control to developer

# iteration => cycle => only performed on iterables(collections and string)

# Write progrm to print 1 to 10 numbers.
# using while loop.

# start_num = 1
# end_num = 10
# while start_num <= end_num:
#     print(start_num)
#     start_num+=1

# for num in range(1, 11):
#     print(num)

#---------------------------------------
# Write a program to get Armstrong number:
    # 153 => 1**3 + 5**3 + 3**3
    #     => 1 + 125 + 27
    # 153 = 153

# Find armstromg number in between 100 to 10000
# while loop:

# num = 100
# while num <= 10000:
#     str_num = str(num)
#     power = len(str_num)

#     total = 0

#     count = 0
#     while count < power:
#         total +=(int(str_num[count]) ** power)
#         count +=1

#     if total == num:
#         print(num)
#     num+=1

#-----------------------------

# for num in range(100, 10000):
#     str_num = str(num)
#     power = len(str_num)
#     total = 0
#     for digit in str_num:
#         total += (int(digit) ** power)
#     if total == num:
#         print(total)
    