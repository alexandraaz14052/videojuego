import os
from random import randint
from types import TracebackType


def run():
    os.system("clear")
    print("""BIENVENIDO  A  TU  VIDEOJUEGO  FAVORITO""")
    print("\nPara jugar primero dinos el rango de numeros desde el cual "
    "el sistema debe crear el numero aleatorio")

    ##Inicializando todas las variables
    try_numer = int(input("\n**Ingresa el numero de intentos que quieres "))
    first_intervalo = int(input("\n**Ingresa el numero menor para ingresar "))
    second_intervalo = int(input("\n**Ingresa el numero mayor para ingresar "))
    goal_number = randint(first_intervalo,second_intervalo)
    chance = int(input("Intenta adivinar el numero aleatorio: "))
    try_numer = try_numer - 1

    while goal_number != chance:
        if try_numer <= 0:
            os.system("clear")
            print("Lo sentimos ya no te quedan oportunidades, mejor suerte a la proxima. 😞")
            exit()
        if goal_number < chance:
            chance = int(input("\nTe quedan "+str(try_numer)+" intentos \nEl numero es menor, Intenta de nuevo 🤑.\n"))
        elif goal_number > chance:
            chance = int(input("\nTe quedan "+str(try_numer)+" intentos \nEl numero es mayor, Intenta de nuevo 🤑.\n"))
        try_numer = try_numer - 1
     
    os.system("clear")   
    print("\n\n😎😎 Felcidades Ganaste el Juego. 😎😎")



if __name__ == "__main__":
    run()