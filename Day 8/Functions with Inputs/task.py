def greet(name):
    # print("Hello",name+",")
    print(f"Hello {name}")
    print("This is Pycharm Bot!")
    print("Tell me if you need any assitance...")

greet(input("Enter Name:"))


def life_in_weeks(age):
    remaining_years = 90 - age
    weeks_in_year = 52
    print(f"You have {remaining_years * weeks_in_year} weeks left.")


user_age = int(input("Enter your current age:"))
life_in_weeks(user_age)