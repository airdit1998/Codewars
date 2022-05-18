def zombie_shootout(zombies, distance, ammo):
    if ammo == 0 and distance != 0:
        return f'You shot 0 zombies before being eaten: ran out of ammo.'
    zombie = zombies
    while distance != 0:
        distance -= 0.5
        ammo -= 1
        zombie -= 1
        if zombie != 0 and ammo == 0 and distance != 0:
            return f'You shot {zombies - zombie} zombies before being eaten: ran out of ammo.'
        elif zombie == 0:
            return f'You shot all {zombies} zombies.'
    print(zombie, distance, ammo)
    return f'You shot {zombies - zombie} zombies before being eaten: overwhelmed.'

print(zombie_shootout(50, 8, 10))