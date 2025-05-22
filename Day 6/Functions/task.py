def my_function(word):
    print("Hello " + word)

def my_function2():
    print("Function 2")

name = input("Enter your name:")

for i in range(0,3):
    my_function(name)

my_function2()