'''
Crie um programa que LEIA DOIS VALORES e mostre um MENU na tela:
[1]Somar
[2]Multiplicar
[3]Maior
[4]Novos Números
[5]Sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
from time import sleep
print("\033[33m""-=-" * 24, "\033[m")
print(" SEJA MUITO BEM VINDO AO NOSSO SISTEMA DE OPERAÇÕES COM DOIS ALGORISMOS")
print("\033[33m""-=-" * 24, "\033[m")
while True:
    n1 = int(input("Digite um número: ")) 
    n2 = int(input("Digite outro número: "))
    nums = n1, n2
    print('''[1]Somar
[2]Multiplicar
[3]Maior
[4]Novos Números
[5]Sair do programa''')
    print("\033[33m""-=-" * 24, "\033[m")
    opcao = int(input("Qual operação deseja realizar com os números {} e {}?\n".format(n1,n2)))
    if opcao == 1:
        print("Você selecionou a opção {}(SOMAR)".format(opcao))
        print(f"{n1} + {n2} = {n1+n2}")
        print("\033[33m""-=-" * 15, "\033[m")
    elif opcao == 2:
        print("Você selecionou a opção {}(MULTIPLICAR)".format(opcao))
        print(f"{n1} * {n2} = {n1*n2}")
        print("\033[33m""-=-" * 15, "\033[m")
    elif opcao == 3:
        print("Você selecionou a opção {}(MAIOR)".format(opcao))
        print(f"O maior número entre os dois digitados é {max(nums)}")
        print("\033[33m""-=-" * 15, "\033[m")
    elif opcao == 4:
        print("Você selecionou a opção {}(NOVOS NÚMEROS)".format(opcao))
        print("Por favor, informe novos números: ")
        print("\033[33m""-=-" * 15, "\033[m")
    elif opcao == 5:
        print("Finalizando o Sistema...")
        sleep(2)
        print("Sistema Finalizado! ")
        break
    else:
        print("Opção inválida, tente novamente!")
