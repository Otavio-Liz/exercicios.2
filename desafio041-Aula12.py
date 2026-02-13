"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER

"""
from datetime import date
ano_atual = date.today().year
ano_nascimento = int(input("Digite o ano de seu nascimento: "))
idade = ano_atual - ano_nascimento 
print("O atleta tem {} anos.".format(idade))
if (ano_atual - ano_nascimento) < 10:
    print("CATEGORIA MIRIM")
elif (ano_atual - ano_nascimento) < 15:
    print("CATEGORIA INFANTIL")
elif (ano_atual - ano_nascimento) < 20:
    print("CATEGORIA JUNIOR")
elif (ano_atual - ano_nascimento) < 21:
    print("CATEGORIA SÊNIOR")
elif (ano_atual - ano_nascimento) > 20:
    print("CATEGORIA MASTER")
else:
    print("Valor inválido")