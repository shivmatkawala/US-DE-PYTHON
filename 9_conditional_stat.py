# Conditional Statements:

    # if, elif, else

    # Define first condition of program with "if"
    # define rest of the conditions with "elif"
    # define default condition with "else"

# Write a program to ask user to enter his/her favourate 
# primary color.
# as per color theory display the meaning of that color.

# Red, Blue, Green

# fav_prim_color = input("Enter your favourate primary color: ")

# if fav_prim_color.rstrip().title() == "Red":
#     print("Sacrifice")
# elif fav_prim_color.rstrip().title() == "Blue":
#     print("Peace")
# elif fav_prim_color.rstrip().title() == "Green":
#     print("Nature")
# else:
#     print("Invalid Color")


# if fav_prim_color.rstrip().title() == "Red":
#     print("Sacrifice")
# if fav_prim_color.rstrip().title() == "Blue":
#     print("Peace")
# if fav_prim_color.rstrip().title() == "Green":
#     print("Nature")
# if fav_prim_color.rstrip().title() not in ("Red", "Blue", "Green"):
#     print("Invalid Color")


#-----------------------------------

# Nested Conditions:

# Write a program where you ask user to enter any nuumber
# in between -10 to 10

# 7:
    # +ve
        # even
        # odd
    # -ve
        # even
        # odd
    # neither +ve nor -ve
    # zero is even

num = int(input("Enter a num {-10 to 10}: "))

if num > 0:
    print(f"{num} is +ve")
    if num%2 == 0:
        print("Even")
    else:
        print("odd")

elif num < 0:
    print(f"{num} is -ve")
    if num%2 == 0:
        print("even")
    else:
        print("odd")

else:
    print("It is zero, neither +ve nor -ve.")
    print("even")