print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

amount = (bill + ((tip/100)*bill))/people
amount = round(amount, 2)

print(f"Each person should pay: ${amount}")