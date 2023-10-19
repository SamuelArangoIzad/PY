import time


def animacion_completar_vertical(palabra):
    for letra in palabra:
        animacion = 'a'
        while animacion <= letra:
            print(animacion, end="\r")
            time.sleep(0.1) 
            animacion = chr(ord(animacion) + 1)
        print(letra)
        time.sleep(0.5)  


def animacion_busqueda_letra(letra):
    animacion = 'a'
    while animacion <= letra:
        print(animacion, end="\r")
        time.sleep(0.1) 
        animacion = chr(ord(animacion) + 1) 

while True:
    print("Panel de Interacción:")
    print("1. Complete Word Vertically")
    print("2. Complete Word Horizontally")
    print("3. Exit")

    opcion = input("Chose A Option: ")

    if opcion == "1":
        
        palabra = input("Write A Word: ")
        animacion_completar_vertical(palabra)
    elif opcion == "2":
        
        palabra = input("Write A Word: ")
        palabra_completa = ""

        for letra in palabra:
            animacion_busqueda_letra(letra)
            palabra_completa += letra
            print(palabra_completa, end="\r") 
            time.sleep(0.5) 

        print()  
    elif opcion == "3":
        print("Exit.")
        break
    else:
        print("Negative Option")