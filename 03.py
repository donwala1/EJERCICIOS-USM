from os import system
system("cls")

num=int(input("Ingrese un numero: "))

for i in range(11):
    res= num*i
    print(f"{i}x{num}={res}")
