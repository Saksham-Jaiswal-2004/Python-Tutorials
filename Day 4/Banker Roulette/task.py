import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

print(random.choice(friends)) #Selects a random element from a list or a string
print(friends[random.randrange(0,4,1)]) #Generates a random number from the given range with as step of given value
print(friends[random.randrange(0,4)])