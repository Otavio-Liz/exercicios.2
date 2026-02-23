'''
Faça um programa que leia o pode de 5 pesoas. No final, 
mostre qual foi o maior e menor peso
'''
# Maior e Menor Peso
maior_peso = 0
menor_peso = 0
lista_peso = []
for i in range (1, 6):
    peso = float(input("Qual o peso da {}° pessoa?".format(i)))
    lista_peso.append(peso)
maior_peso = max(lista_peso)
menor_peso = min(lista_peso)
print("O maior peso da lista é {}.".format(maior_peso))
print("O menor peso é {}.".format(menor_peso))

maior = 0
menor = 0
for p in range(1, 6):
    kg = float(input("Qual o peso da {}º pessoa?".format(p)))
    if p == 1:
        maior = kg
        menor = kg
    elif kg > maior:
        maior = kg
    elif kg < menor:
        menor = kg
print("O maior peso lido foi {}.".format(maior))
print("O menor peso da lista foi {}.".format(menor))