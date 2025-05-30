enemies = ["Skeleton", "Zombie", "Alien"]
game_level = 3

if game_level<5:
    new_enemy = enemies[0]

print(new_enemy)

def create_enemy():
    new_enemy = ""
    if game_level<4:
        new_enemy = enemies[1]
        print(new_enemy)

create_enemy()
print(new_enemy)