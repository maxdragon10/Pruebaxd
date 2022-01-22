
import random


def juego_2(x):

 print("==========================")
print(" ¡Bienvenido(a) al Juego! ")
print("==========================================================")
print("Tu meta es adivinar el número generado por la computadora.")
print("==========================================================")
número_aleatorio = random.randint(1, 10) #número aleatorio entre 1 y x.
 
predicción = 0

while predicción != número_aleatorio: 
    # El usuario ingresa un número
    predicción = int(input(f"Adivina un número entre 1 y {10}: ")) # f-string

    if predicción < número_aleatorio:
     print("Intenta otra vez. Este número es muy pequeño.")
    elif predicción > número_aleatorio:
     print("Intenta otra vez. Este número es muy grande.")

    print(f"¡Felicitaciones! Adivinaste el número {número_aleatorio} correctamente.")


juego_2(10)