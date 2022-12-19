import random


def adivina_el_numero_computadora(x):

    print("========================")
    print("¡Bienvenido/a al juego! ")
    print("========================")
    print(f"Selecciona un numero entre un numero entre 1 y {x} para que la computadora intente adivinarlo")
    
    limite_inferior = 1
    limite_superior = x

    respuesta = ""
    while respuesta != "c":

        if limite_superior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior


        respuesta = input(f"Mi prediccion es {prediccion}. Si es muy alta ingresa (A), si es muy baja ingresa (B). Si es correcta ingresa (C)").lower()

        if respuesta == "a":
            limite_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1

    print(f"SIII!, La computadora adivino tu numero correctamente: {prediccion} ")


adivina_el_numero_computadora(10)