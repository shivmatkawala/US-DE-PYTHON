# Always thry to handle errors gracefully.

# ask user to provide height, weight
# write program to find BMI

# try:
#     weight = eval(input("Enter your weight[KG]: "))
#     height = eval(input("Enter your height[M]: "))
# except NameError:
#     print("You entered invalid value.\nPlease enter correct values")
# except SyntaxError:
#     print("You did not enter anything.\nPlease enter value")
# else:
#     BMI = weight/ (height**2)
#     print(f"Your BMI: {BMI:.2f}")
# finally:
#     print("Program ended successfully.")

#-----------------------------------------------

class AgeError(Exception):
    pass

age = int(input("Enter your age: "))
if age > 22:
    print("Eligible")
elif age <= 0:
    raise AgeError("Age cant be zero or negative")
else:
    print("Not Eligible")
