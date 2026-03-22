'''
Refaça o DESAFIO 051, lendo o PRIMEIRO TERMO e a RAZÃO de uma PA, mostrando os 10 PRIMEIROS TERMOS da progressão usando a estrutura while
'''

'''
Desenvolva um programa que leia o PRIMEIRO TERMO e a RAZÃO de uma PROGRESSÃO ARITIMÉTICA. No final, mostre os 10 primeiros termos dessa 
progressão.
'''
print("==" * 20)
print("\033[33m""     OS 10 TERMOS DA PROGRESSÃO""\033[m")
print("==" * 20)
primeirotermo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
termo = primeirotermo
cont = 1
while cont <= 10:
    print("{} ".format(termo), end=" ")
    print(" → " if cont < 10 else "  ", end=" ")
    termo += razao
    cont += 1
    
    