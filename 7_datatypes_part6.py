# Dictionary:

    # It is a collection datatype
    # It is unordered
    # It is indexed by keys
    # Cant have duplicate keys
    # Can have duplicat values
    # It is a collection of key value pair

dict1 = {1:1, 2:4, 3:9, 4:16, 5:25}
# print(dict1)
# print(type(dict1))  #<class 'dict'>

dict2 = {"one": 1, "Two": 4, "Three": 9, "Four":16, "Five": 25}
# print(dict2)
# print(type(dict2))

dict3 = {
    "Apple": "Fruit", 
    "Table": "Furniture",
    "Coca-Cola": "Cold-Drink"
}

# print(dict3)
# print(type(dict3))

#----------------------------------------------
students = {"A", "B", "C", "D", "E"}
Marks = {89, 78, 90, 45, 76}

student_marks = dict(zip(students, Marks))
print(student_marks)

student_result = dict.fromkeys(students, "Pass")
print(student_result)

#------------------ IN-BUILT METHODS:

# Insertions:

dict4 = {
    "David": "England",
    "Riya": "India",
    "Chang": "China",
    "Kushigo": "Japan",
    "Wlen Yi": "Australia",
}
dict4.update({"Akbar Shah": "Pakistan"})
# print(dict4)

dict4["Sara Spilberg"] = "USA"  
dict4["Riya"] = "Nepal"
# print(dict4)
print(dict4.get("Kushigo"))

dict5 = dict4.copy()
# print(dict5)

names = dict4.keys()
countries = dict4.values()

# print(names)
# print(countries)
# print(dict4.items())

# dict4.pop("Sara Spilberg")
# dict4.popitem()
# dict4.clear()
# print(dict4)