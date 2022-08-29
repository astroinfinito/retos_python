#### Este es un reto de programación que pinta divertido####
####  Enunciado: Crea una función que reciba un texto y muestre cada palabra en una línea, formando
# * un marco rectangular de asteriscos.
# * - ¿Qué te parece el reto? Se vería así:
# *   **********
# *   * ¿Qué   *
# *   * te     *
# *   * parece *
# *   * el     *
# *   * reto?  *
# *   **********
# *

def funcion():

    frase = "Hola"
    frase2 = "a "
    frase3 = "todos"
    for i in range(3):
        if i < 3:
            print("**********")
            print("*",frase,"  * ",end="\n")
            print("*",frase2,"    * ",end="\n")
            print("*",frase3," * ",end="\n")
            print("**********")   
        else:
            print(i)

funcion()