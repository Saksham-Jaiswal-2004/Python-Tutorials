import random

heads=0
tails=0

for i in range(1, 10000, 1):
    choice = random.randint(0, 1)

    if choice == 0:
        heads += 1
    else:
        tails += 1

headsPercent = (heads/10000)*100
tailsPercent = (tails/10000)*100

print(f"Heads percentage {tailsPercent}")
print(f"Tails percentage {tailsPercent}")