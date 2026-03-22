'''
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 TERMOS
'''
from time import sleep
print("==" * 20)
print("\033[33m""     OS 10 TERMOS DA PROGRESSÃO""\033[m")
print("==" * 20)
primeirotermo = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
total = 0
maistermos = 10
cont = 1
while maistermos != 0:
    total = total + maistermos
    while cont <= total:
        print("{} → ".format(primeirotermo), end="")
        primeirotermo += razao
        cont += 1
    print("PAUSA")
    maistermos = int(input("Deseja adicionar mais termos? "))
print("O número total de termos foi {}.".format(total))
print("Finalizando o Sistema...")
sleep(2)
print("Sistema Finalizado!")