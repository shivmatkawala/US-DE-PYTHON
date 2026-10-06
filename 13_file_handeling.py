# Create File:
# file = open("./storage/file1.txt", "w")

# file = open("./storage/file1.py", "w")

# file = open("./storage/file1.java", "w")

# file = open("./storage/file1.js", "w")

# file = open("./storage/file1.csv", "w")

# file = open("./storage/file1.xlsx", "w")

#-------------------------------------------
# Write into Existing File:

file = open("./storage/file1.txt", "w")
file.write("This is Python sission and we are learning file handelling.")
file.close()

file = open("./storage/file1.txt", "w")
file.write("We learned how to wrte in file using open function.")
file.close()

file = open("./storage/file1.txt", "a")
file.write("\nThis is october month..")
file.close()

#-------------------------------------------------

file = open("./storage/file1.txt", "r")
content = file.read()
print(content)
file.close()

#-----------------------------
import os
print(os.getcwd())
# os.remove("./storage/file1.py")
os.remove("./storage/file1.js")
os.remove("./storage/file1.java")
os.remove("./storage/file1.xlsx")
os.remove("./storage/file1.csv")