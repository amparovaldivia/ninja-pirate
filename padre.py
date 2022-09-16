from random import randint


class Padre:

    def play(self):
        baraja_trebol = ['as', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'j', 'q', 'k']
        posicion = randint(0, len(baraja_trebol)-1)
        return {'carta': baraja_trebol[posicion], 'valor': posicion}
