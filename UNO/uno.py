# Simulador joc UNO
import random

colors = ["verd", "blau", "groc", "roig"]
cartes_inici = 7


def crear_carta():
    num = random.randint(0,9)
    col = random.randint(0,3)
    return (num, colors[col])

def generar_ma(n):
    ma = []
    for i in range(0,n):
        ma.append(crear_carta())
    return ma


n = int(input("Entra nombre de jugadors: "))
jugador = {'nom': 'jugador', 'cartes': generar_ma(cartes_inici)}
l_bots = []
for i in range(1,n):
    bot = {'nom': "bot" + str(i), 'cartes': generar_ma(cartes_inici)}
    l_bots.append(bot)
    print(bot)

print(jugador)
