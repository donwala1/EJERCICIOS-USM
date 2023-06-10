from os import system
system("cls")
for i in range(1,11):
    for j in range(1,11):
        res=i*j
        print(f'{res:3}', end=' ')
    print()
    