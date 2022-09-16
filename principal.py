from ninja import Ninja
from pirate import Pirate

ninja = Ninja('ninja')
pirate = Pirate('pirate')


def plays():
    while ninja.health > 0 and pirate.health > 0:
        personaje = input('escribe ninja o pirate!')
        personajes = [ninja, pirate]
        if personaje == 'ninja':
            input('ninja elije una carta, presiona enter')
            carta_ninja = ninja.play()
            input('pirate elije una carta')
            carta_pirate = pirate.play()
        elif personaje == 'pirate':
            input('pirate elije una carta, presiona enter')
            carta_pirate = pirate.play()
            input('ninja elije una carta')
            carta_ninja = ninja.play()
        else:
            continue
        print(f"ninja eligio: {carta_ninja['carta']}, pirate eligio: {carta_pirate['carta']}")
        if carta_ninja['valor'] > carta_pirate['valor']:
            ninja.attack(pirate)
        elif carta_pirate['valor'] > carta_ninja['valor']:
            pirate.attack(ninja)
        ninja.show_stats()
        pirate.show_stats()
    if ninja.health > pirate.health:
        print('ninja win')
    else:
        print('pirate win')

plays()
