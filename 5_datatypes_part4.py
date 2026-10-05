# # Set:

#     # It is collection datatype
#     # It is mutable
#     # It is partially heterogeous (allows only Immutable data)
#     # It is unordered
#     # It doesnt support indexing
#     # IT diesnt allow duplicates
#     # It can be created using {}

# s1 = {0}
# print(s1)
# print(type(s1))

# s2 = set()
# print(s2)
# print(type(s2))

# # IN-Built Methods:

s3 = {1, 2, 3}

#         # Insertion methods
#             # .add() => adds single element
s3.add(4)
print(s3)
              # .update() => to add muliple elements

s3.update([100, 200, 4, 3])
print(s3)

    # Deletion methods

            # .remove() => Removes specific element
s3.remove(100)

            # .pop() removes any random element
s3.pop()
            # .clear() removes all elements
s3.clear()

print(s3)