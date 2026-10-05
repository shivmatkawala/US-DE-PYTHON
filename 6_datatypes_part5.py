# Set Operations:

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

# # Union
# print(s1.union(s2))
# print(s1 | s2)

# # Difference
# print(s1 - s2)
# print(s2 - s1)
# print(s1.difference(s2))
# print(s2.difference(s1))

# # Intersection:
# print(s1 & s2)
# print(s1.intersection(s2))

#----------------------------------
# s1.update(s2)
# s1.difference_update(s2)
# s2.difference_update(s1)
# s2.intersection_update(s1)

# print(s2)

#---------------------------------------------------
# Subset and Superset:

set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}   # set1 is superset of set2
set2 = {4, 0}   # set2 is subset of set1

# print(set1.issuperset(set2))
# print(set2.issubset(set1))