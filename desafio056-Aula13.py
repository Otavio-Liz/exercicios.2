'''
Desenvolva um programa que leia o NOME, IDADE e SEXO de 4 PESSOAS.
No final, mostre:
> A MÉDIA DE IDADE do grupo;
> Qual é o nome do homem MAIS VELHO;
> Quantas mulheres tem MENOS DE 20 ANOS.
'''
# MOSTRAR MÉDIA DE IDADE DO GRUPO
# QUAL É O NOME DO HOMEM MAIS VELHO
# QUANTAS MULHERES TEM MENOS DE 20 ANOS
maioridadehomem = 0
mulher_menor_20 = 0
media = 0
soma = 0
idade = 0
nomedomaisvelho = ''
for p in range(1, 5):
    sexo = int(input("Qual seu gênero?\n[0]MASCULINO\n[1]FEMININO\n"))
    nome = str(input("Digite seu nome:"))
    idade = int(input("Quantos anos você tem?"))

    if sexo == 0:
        if p == 1:
            maioridadehomem = idade
            nomedomaisvelho = nome
        elif idade > maioridadehomem:
            maioridadehomem = idade
            nomedomaisvelho = nome
    if sexo == 1:
        if idade < 20:
            mulher_menor_20 += 1
        
soma += idade # Média de idades funcionando
media = soma/4
print("A média de idade do grupo de 4 pessoas é {}.".format(media))
print("{} é o homem mais velho da lista, com {} anos.".format(nomedomaisvelho, maioridadehomem))
if mulher_menor_20 == 0:
    print("Todas as mulheres da lista são maiores de 20 anos")
else:
    print("{} é a quantidade de mulheres menor de 20 anos.".format(mulher_menor_20))

# SAÍDA STRING DO MAIS VELHO
# QUANTIDADE DE MULERES COM < DE 20