alien = {
    "color":"azul",
    "puntos": 20,
    "posicion_x": 50,
    "posicion_y": 100
}
print (alien)

import random
listaAliens = []
alienAleatorio = {}
limite = 10
num = 0

while num < limite :
    alienAleatorio["color"] = "azul"
    alienAleatorio["puntos"] = random.randint(1,10)
    alienAleatorio["posicion_x"] = random.randint(0,100)
    alienAleatorio["posicion_y"] = random.randint(0,100)
    print(f"Alien aleatorio num {num} es {alienAleatorio}")
    #listaAliens.insert(num, alienAleatorio)
    listaAliens.append(alienAleatorio.copy())
    num = num + 1

print (listaAliens)
