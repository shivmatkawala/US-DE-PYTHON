# Operators:
    # Arithmetic Operators:
        # +, -, *, /, //, **, % [Only on Numeric and Boolen Datatypes]
x = 5
y = 3
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x//y)
# print(x%y)
# print(x**y)

    # Assignement Operators:
        # =, +=, -=, *=, /=, //=, **=, %= [Only on Numeric and Boolean]
# z = 10
# z = z+10
# z+=10
# z-=3
# z*=2
# z/=4
# z//=0.5
# z**=2
# z%=3

# print(z)
    # Comaprision Operators:
        # >, <, ==, !=, >=, <=, 
# print(x > y)
# print(x < y)
# print(x == y)
# print(x != y)
# print(x >= y)
# print(x <= y)

    # Identity Operatort:
        # is, is not 
        # x = y
        # x  = y.copy()
        # x = deepcopy(y)   
alpha = [1, 2, 3, 4, [12, 23, 34]]
# beta = alpha
# print(id(alpha))
# print(id(beta))
# print(alpha is beta)

# beta = alpha.copy()
# print(id(alpha), alpha)
# print(id(beta), beta)
# print(alpha is beta)

# from copy import deepcopy
# beta = deepcopy(alpha)
# print(id(alpha), alpha)
# print(id(beta), beta)

# print(alpha is beta)

    # Membership Operators:
        # in, not in
# set11 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# print(6 in set11)
# print(100 not in set11)

    # Logiacal Operators:
        # and, or, not
# print(True and True)
# print(False and False)
# print(True and False)

# print(True or True)
# print(False or False)
# print(True or False)

# print(not(True))
# print(not(False))

    # Ternary Operators:
        # if, else
# Red, Blue, Green
# fav_prim_color = input("Enter Favourate Primary Color: ")

# result = "Sacrifice" if fav_prim_color == "Red" else "Peace" if fav_prim_color == "Blue" else "Nature" if fav_prim_color == "Green" else "Invalid Color"
# print(result)

    # Bitwise operators:
        # &, |, ^

print(10 & 34)
print(10 | 34)
print(10 ^ 34)

# print(bin(10))
# print(bin(34))

# print(int("101010", 2))
