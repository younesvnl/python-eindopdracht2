
monster_health = 150
player_damage = 25
aantal_aanvallen = 0
 
while monster_health > 0:
    monster_health = monster_health - player_damage
    aantal_aanvallen = aantal_aanvallen + 1
 
    if monster_health < 0:
        monster_health = 0
 
    print("Zombie heeft nog", monster_health, "health")
 
print("Zombie verslagen!")
print("Aantal aanvallen:", aantal_aanvallen)
