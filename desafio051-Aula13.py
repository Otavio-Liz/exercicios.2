'''
Desenvolva um programa que leia o PRIMEIRO TERMO e a RAZÃO de uma PROGRESSÃO ARITIMÉTICA. No final, mostre os 10 primeiros termos dessa 
progressão.
'''
print("==" * 20)
print("\033[33m""     OS 10 TERMOS DA PROGRESSÃO""\033[m")
print("==" * 20)
primeirotermo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
decimo = primeirotermo + (11 -1) * razao
for i in range(primeirotermo, decimo, razao):
    print("{}".format(i), end= " > ")
    
    