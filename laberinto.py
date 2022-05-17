import random
from random import randrange


class Laberinto:

    def __init__(self, x, y, numObstaculos=0.3):
        self.x = x
        self.y = y
        self.laberinto = [[' '] * y for _ in range(x)]

    def colocarSalida():
        return (posx, posy)

    def colocarEntrada():
        return (posx, posy)

    def getEntrada(self):
        return "entrada"

    def getSalida(self):
        return "Salida"

    def colocarObstaculosSimple():


    def print(self):
        print("Laberinto")

    def getPosActual(self):
        return self.posActual


def buscaCandidatos():
    candidatos = []

    return candidatos


def esSalida():
    return True


def resolverLaberinto(laberinto, posActual):

    if esSalida():
        return True
    else:
        return False


def main():
    laberinto = Laberinto(10, 10)
    laberinto.print()
    entrada = laberinto.getEntrada()
    resolverLaberinto(laberinto, entrada)


if __name__ == '__main__':
    main()
