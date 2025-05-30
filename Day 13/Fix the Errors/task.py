try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have entered an invalid number, Please try again with a numerical value.")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")