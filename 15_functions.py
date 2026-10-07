#Functions:

    # It is a programming paradigm.

    # Functions are nothing but set of programs written under
    # behaviour name.

    # "def" keyword is used to create a function.
    # functions do have "Head" and "Body"

    # Functions will not execute untill they are called.
        # Reusibility, Seperation of concerns, unnecessary execution of programs stopped
#-----------------------------------------------
# Create a function to print a table of 2
def table_of_2():
    for i in range(1, 11):
        print(f"2*{i} = {2*i}")

# table_of_2()
# table_of_2()

#----------------- Types of Functions:
    # No Argument Function:
# def greet_students():
#     print("Hello Students")

# greet_students()
    # Single Argument Function:
# def greet_student(name:str):
#     print("Hello {}".format(name))
# greet_student("Amisha")

    # Default Argument Function:
# def greet_student(name="My Dear Student"):
#     print(f"Hello {name}")

# greet_student()
# greet_student("Ajay")

    # Variable Length Argument Function:
# def greet_student(*names):
#     for name in names:
#         print(f"Hello dear {name}")

# greet_student("Raj", "Vijay", "Alan", "David", "Sara")

    # Keyword Argument Function:
# Roll_1 => Amisha
# Roll_2 => Urvi
# Roll_3 => Naga
# Roll_4 => Vijay
# Roll_5 => Harsh

# def greet_student(roll_1, roll_2, roll_3, roll_4, roll_5):
#     print(f"Hello Roll No. 1 {roll_1}")
#     print(f"Hello Roll No. 2 {roll_2}")
#     print(f"Hello Roll No. 3 {roll_3}")
#     print(f"Hello Roll No. 4 {roll_4}")
#     print(f"Hello Roll No. 5 {roll_5}")

# greet_student("Naga", "Harsh", "Urvi", "Amisha", "Vijay")
# greet_student(roll_3="Naga", roll_4="Vijay", roll_5="Harsh", roll_2="Urvi", roll_1="Amisha")


    # Variable Length Keyword Argument Function:

# def greet_student(**kwargs):
#     for roll_no, student in kwargs.items():
#         print(f"Hello {roll_no}: {student}")

# dict1 = {
#     "Roll_1": "Amisha",
#     "Roll_2": "Urvi",
#     "Roll_3":"Naga",
#     "Roll_4": "Vijay",
#     "Roll_5": "Harsh"
# }
# greet_student(**dict1)
# greet_student(Roll_1="Urvi", Roll_2="Naga", Roll_3="Amisha")


#-------------------------------------

# def greet_student(name, age=20, *hobbies, **fav_game_ranking):
#     print(f"Hello {name}")
#     print(f"Your age is {age}")    
#     print("------- Hobbies --------")
#     sr = 1
#     for hobby in hobbies:
#         print(f"{sr}. {hobby}")
#         sr+=1
#     print("***********************")
#     print("------ Favourate Games With Rank ------")
#     for game, rank in fav_game_ranking.items():
#         print(f"{rank}:=> {game}")

# greet_student("Siva Kumaran", 32, "Painting", "Reading", "Watching Movies", Rank_1="Cricket", Rank_2="Hockey", Rank_3="Kabaddi")
