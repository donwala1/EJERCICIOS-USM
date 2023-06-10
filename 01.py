from os import system
system("cls")

while True:
    a=int(input("Ingrese un numero: "))
    if a%2==0:
        print("El numero es par")
    else:
        print("El numero es impar")