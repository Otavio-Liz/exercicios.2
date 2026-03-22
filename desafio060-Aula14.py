'''
Faça um programa que leia um número e MOSTRE O SEU FATORIAL.
EX: 5! = 5*4*3*2*1 = 120
'''
num = int(input("Digite um número para saber seu fatorial: "))
cont = num
fatorial = 1
while cont > 0:
    print ("{}".format(cont), end=" ")
    print(" x " if cont > 1 else " = ", end=" ")
    fatorial *= cont
    cont -= 1 
print(fatorial)



