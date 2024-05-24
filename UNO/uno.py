# Simulador joc UNO
import random
import time

colors = ["verd", "blau", "groc", "roig"]
cartes_inici = 7


def crear_carta():
    num = random.randint(0,9)
    col = random.randint(0,3)
    return (num, colors[col])

def tirada_valida(carta, pila):
    return carta[0] == pila[0] or carta[1] == pila[1]

def llegir_carta():
    carta = input("Carta: ")
    aux = carta.split(' ')
    aux[0] = int(aux[0])
    c = (aux[0], aux[1])
    return c

def cartes_eligibles(m,p):
    l = []
    for i in m:
        if tirada_valida(i,p):
            l.append(i)
    return l

def tirar_carta(m, c, p):
    p = c
    print(p)
    m.remove(c)
    return p

def roba_carta(j):
    generar_cartes(j['cartes'], 1)
    print("El", j['nom'], "ha robat una carta")
    return


def generar_cartes(ma, n):
    for i in range(0,n):
        ma.append(crear_carta())
    return

def torn_bot(bot, pila):
    print("Torn de", bot['nom'])
    print(bot['cartes'])
    cartes_valides = cartes_eligibles(bot['cartes'], pila)
    if not cartes_valides:
        roba_carta(bot)
        print("El", bot['nom'], "ha robat una carta")
    else:
        pila = tirar_carta(bot['cartes'], cartes_valides[0], pila)
    return pila

def torn_jugador(jugador, pila):
    print("\n")
    print(jugador['cartes'])
    print(pila)
    while True:
        print("Opcions:")
        op = int(input("1. Tirar carta \n2. Robar carta \n3. Contar cartes \n"))
        if op == 1:
            cartes_valides = cartes_eligibles(jugador['cartes'], pila)
            if not cartes_valides:
                print("No tens cartes que pugis tirar aquest torn")
            else:
                print("Pots tirar aquestes cartes:", cartes_valides)
                c = llegir_carta()
                if c in cartes_valides:
                    pila = tirar_carta(jugador['cartes'], c, pila)
                    break
                else:
                    print("No tens aquesta carta")
        elif op == 2:
            roba_carta(jugador)
            break
        elif op == 3:
            for i in l_bots:
                print(i['nom'], ":", len(i['cartes']))
        else:
            print("Opció no vàlida, Torna a intentar")
    return pila
        

n = int(input("Entra nombre de jugadors: "))
ma = []
generar_cartes(ma,cartes_inici)
jugador = {'nom': 'jugador', 'cartes': ma}
l_bots = []
for i in range(1,n):
    ma = []
    generar_cartes(ma, cartes_inici)
    bot = {'nom': "bot" + str(i), 'cartes': ma}
    l_bots.append(bot)

pila = crear_carta()
print(pila)
pila = torn_jugador(jugador, pila)
for b in l_bots:
    time.sleep(2)
    print("\n")
    pila = torn_bot(b, pila)
