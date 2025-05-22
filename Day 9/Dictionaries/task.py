# Dictionary in Python
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    1234: "New data with number key"
}

# Fetching data using key in the Dictionary
print(programming_dictionary["Function"])
print(programming_dictionary[1234])

# Adding new data in dictionary
programming_dictionary["Book"] = "Best way to feel expressed."
print(programming_dictionary)

# Creating an empty dictionary
new_dictionary = {}

new_dictionary["A"] = "1st Data"
new_dictionary["B"] = "2nd Data"
new_dictionary["C"] = "3rd Data"
print(new_dictionary)

# To delete all the elements in a Dictionary
new_dictionary = {}
print(new_dictionary)

# Editting an element in a Dictionary
programming_dictionary[1234] = "Changed Data"
print(programming_dictionary)

# Looping through the Dictionary
for things in programming_dictionary:
    print(things) # Prints all the keys
    print(programming_dictionary[things]) # Prints all the values