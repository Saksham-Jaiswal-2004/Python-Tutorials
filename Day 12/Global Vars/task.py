# Modifying Global Scope

enemies = 1


def increase_enemies():
    # Targeting global variable instead of creating new ones
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")