from os import system
system("cls")

n1=int(input("Ingrese el primer numero: "))
n2=int(input("Ingrese el segundo numero: "))
res=0
for i in range(n1+1,n2):
    res=res+i
print(f"La suma es: {res}")