"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento

O programa também deverá mostrar o tempo que falta ou que passou do prazo.

"""
from datetime import date
ano_atual = date.today().year
while True:
    print("\033[4;31;40m"" ==== ALISTAMENTO MILITAR ==== ""\033[m")
    genero = int(input("""Qual o seu sexo?\n"""
                   "[1]Homem\n[2]Mulher\n""[0] Sair do Menu\n"))
    print("\033[4;31;40m" "---" * 10 ,"\033[m")
    ano_nascimento = int()
    
    if genero == 1:
        ano_nascimento = int(input("Digite seu ano de nascimento: "))
        idade = ano_atual - ano_nascimento
        print("Quem nasceu em {} tem {} anos em {}.".format(ano_nascimento, idade, ano_atual))
        if idade < 18:
            saldo = 18 - idade
            print("Ainda faltam {} para o seu alistamento.".format(saldo))
            ano_alistamento = saldo + ano_atual
            print("Seu alistamento será em {}.".format(ano_alistamento))

        elif idade == 18:
            print("Está na hora de alistar-se no exército.")

        elif idade > 18:
            saldo = idade - 18
            ano = ano_atual - saldo
            print("Já passou do tempo de alistar-se")
            print("Já se passaram {} anos do alistamento.".format(saldo))
            print("Seu alistamento foi em {}.".format(ano))
            print("\033[4;31;40m" "---" * 10 ,"\033[m")
    
    elif genero == 0:
        print("\033[4;32;40m" "NAVEGAÇÃO ENCERRADA" "\033[m")
        break
    elif genero == 2:
        print("Você não é obrigada a alistar-se!")
    else:
        print("Opção inválida! Digite novamente.")
