from decimal import MIN_EMIN
import random
import time


def búqueda_ingenua(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i 
    return -1        

    # range(len(lista)) -> 0, 1, 2, 3, ....., len(lista)-1

def búsqueda_binaria(lista, objetivo, límite_inferior=None, límite_superior=None):
    if límite_inferior is None:
        límite_inferior = 0 # Inicio de la lista.
    if límite_superior is None:
        límite_superior = len(lista)-1 # Final de la lista.
    if límite_superior < límite_inferior:
        return -1

    punto_medio = (límite_inferior + límite_superior) // 2

     # [1, 3, 5, 10, 12]
     #  0  1  2  3  4 
     # punto_medio = (0 + 4) // 2 = 4 // 2 = 2

    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return búsqueda_binaria(lista, objetivo, límite_inferior, punto_medio-1) 
    else:
        return búsqueda_binaria(lista, objetivo, punto_medio+1, límite_superior)


if __name__=='__main__':
    
    # Crear una lista ordenada con 10000 números aleatorios.
    tamaño = 10000
    conjunto_inicial = set()

while len(conjunto_inicial) < tamaño:
    conjunto_inicial.add(random.randint(-3*tamaño, 3*tamaño))

lista_ordenada =  sorted(list(conjunto_inicial))

# Medir el tiempo de búsqueda ingenua.
inicio = time.time()
for objetivo in lista_ordenada:
    búqueda_ingenua(lista_ordenada, objetivo)
fin = time.time()
print(f"Tiempo de búsqueda ingenua: {fin - inicio} segundos.")

# Medir el tiempo de búqueda binaria.
inicio = time.time()
for objetivo in lista_ordenada:
    búsqueda_binaria(lista_ordenada,  objetivo)
fin = time.time()
print(f"Tiempo de búsqueda binaria: {fin - inicio} segubdos.")    
