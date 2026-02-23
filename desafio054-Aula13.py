'''
Crie um programa que leia o ANO DE NASCIMENTO de SETE PESSOAS.
No final, mostre quantas pessoas ainda não atingiram a maioridade e 
quantas já são maiores.
'''
from datetime import date
ano_atual = date.today().year
menor = 0
ano_nascimento = 0
idade = 0
maior = 0
for i in range (7):
    ano_nascimento = int(input("Digite seu ano de nascimento:"))
    idade = ano_atual - ano_nascimento
    if idade < 18:
        menor += 1
    else:
        maior += 1
print("{} pessoas ainda não atingiram a maioridade.\n{} pessoas já são maiores de idade.".format( menor,maior))

    