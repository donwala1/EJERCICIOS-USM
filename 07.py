from os import system
system("cls")

num=int(input("Ingrese un numero: "))
for i in range(1,num+1):
    if num%i==0:
        print(i, end=" ")