'''
Faça um programa que leia um NÚMERO INTEIRO e diga se ele é ou não um NÚMERO PRIMO.
'''
num = int(input("Digite um número inteiro: "))
total = 0
for i in range(1, num+1):
    if num % i == 0:
        print("\033[33m", i, "\033[m", end= " ")
        total += 1
    else:
        print("\033[32m", i, "\033[m", end= " ")
print("\nO número {} foi dividido {} vezes.".format(num, total))     
if total == 2:
    print("E por isso ele é primo")  
else:
    print("Por isso ele é par")