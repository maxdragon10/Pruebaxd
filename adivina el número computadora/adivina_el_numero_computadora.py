import random


def adivina_el_número_computadora(x):

    print("=======================")
    print(" Bienvenido(a) al juego")
    print("=======================")
    print(f"selecciona un  número entre 1 y {x} para que la computadora intente adivinarlo")

    límite_inferior = 1 
    límite_superior = x

    respuesta = ""
    while respuesta  != "c":
        # Generar una predicción
        if límite_inferior != límite_superior: 
            predicción = random.randint(límite_inferior, límite_superior)
        else:
            predricción = límite_inferior # También  podria  ser el límite superior.

            # Obtener una respuesta del usuario 
            respuesta= input(f"Mi predicción es {predicción}.  Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcto, ingresa (C): ").lower()

            if respuesta == "a":
                límite_superior = predicción - 1
            elif respuesta == "b":
                límite_inferior = predicción + 1    

                # "A"
                # Intervalo inicial: [1, 10]
                # Predicción: 6
                # Respuesta: "a"
                # Intervalo: [1, 5]

                # "B"
                # Intervalo inicial: [1, 10]
                # Predicción: 6
                # Respuesta: "b"
                # Intervalo: [7, 10]
            
    print(f" ¡Siiii! la computadora adivino tu número correctamente: {predicción} ")   


adivina_el_número_computadora()
