import random
from random import randrange

class Laberinto:

    def __init__(self, x, y, numObstaculos=0.3):
        self.x = x
        self.y = y
        self.laberinto = [[' '] * y for _ in range(x)]

        self.colocarObstaculosSimple(self.laberinto,numObstaculos)
        self.salida = self.colocarSalida(self.laberinto)
        self.entrada = self.colocarEntrada(self.laberinto)
        self.posActual = self.entrada

    def colocarSalida(self, laberinto):
        posx = randrange(self.x)
        posy = randrange(self.y)
        laberinto[posx][posy] = 'S'
        return (posx, posy)

    def colocarEntrada(self, laberinto):
        while True:
            posx = randrange(self.x)
            posy = randrange(self.y)
            if laberinto[posx][posy] == ' ':
                laberinto[posx][posy] = 'E'
                break
        return (posx, posy)

    def getEntrada(self):
        return self.entrada

    def getSalida(self):
        return self.salida

    def colocarObstaculosSimple(self, laberinto,numObstaculos):
        numeroObs = self.x * self.y * numObstaculos
        cont = 0

        while cont < numeroObs:
            posx = randrange(self.x)
            posy = randrange(self.y)
            if laberinto[posx][posy] == ' ':
                laberinto[posx][posy] = 'X'
                cont = cont + 1

    def print(self):
        i = 0
        k = 0

        while k < self.x * 2 + 1:
            print("-", end=" ")
            k = k + 1
        print("")

        while i < self.x:
            j = 0
            while j < self.y:
                print("| " + self.laberinto[i][j], end=" ")
                j = j + 1
            print("|")
            k = 0
            while k < self.x * 2 + 1:
                print("-", end=" ")
                k = k + 1
            print("")
            i = i + 1

    def getPosActual(self):
        return self.posActual


def buscaCandidatos(laberinto, posActual):
    x = posActual[0]
    y = posActual[1]
    xmax = laberinto.x
    ymax = laberinto.y
    candidatos = []
    laberinto = laberinto.laberinto
    noValidas = ['X', 'V', '=', 'E']

    if y + 1 < ymax:
        if not laberinto[x][y + 1] in noValidas:
            if laberinto[x][y + 1] == 'S':
                candidatos.append((x, y + 1))
                return candidatos
            else:
                candidatos.append((x, y + 1))

    if y - 1 >= 0:
        if not laberinto[x][y - 1] in noValidas:
            if laberinto[x][y - 1] == 'S':
                candidatos = []
                candidatos.append((x, y - 1))
            else:
                candidatos.append((x, y - 1))

    if x + 1 < xmax:
        if not laberinto[x + 1][y] in noValidas:
            if laberinto[x + 1][y] == 'S':
                candidatos = []
                candidatos.append((x + 1, y))
            else:
                candidatos.append((x + 1, y))

    if x - 1 >= 0:
        if not laberinto[x - 1][y] in noValidas:
            if laberinto[x - 1][y] == 'S':
                candidatos = []
                candidatos.append((x - 1, y))
            else:
                candidatos.append((x - 1, y))

    return candidatos


def esSalida(posActual, laberinto):
    return laberinto.laberinto[posActual[0]][posActual[1]] == 'S'


def resolverLaberinto(laberinto, posActual):
    especiales = ["E", "S"]

    if esSalida(posActual, laberinto):
        print("He encontrado la salida!!!")
        return True
    else:
        candidatos = buscaCandidatos(laberinto, posActual)
        if not laberinto.laberinto[posActual[0]][posActual[1]] in especiales:
            laberinto.laberinto[posActual[0]][posActual[1]] = '='

        random.shuffle(candidatos)

        for candidato in candidatos:
            if resolverLaberinto(laberinto, candidato):
                return True

    laberinto.laberinto[posActual[0]][posActual[1]] = 'V'
    return False

def main():
   laberinto = Laberinto(10, 10)
   laberinto.print()
   entrada = laberinto.getEntrada()
   resolverLaberinto(laberinto, entrada)
if __name__ == '__main__':
   main()
