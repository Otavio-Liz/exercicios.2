'''
Escreva um programa qu leia um NÚMERO n INTEIRO qualquer e mostre na tela, os n primeiros elementos de uma SEQUÊNCIA DE FIBONACCI
Ex: 0 > 1 > 1 > 2 > 3 > 5 > 8
'''
print("-" * 23)
print("SEQUÊNCIA DE FIBONACCI")
print("-" * 23)
num = int(input("Quantos termos você quer mostrar? "))
Term1 = 0
Term2 = 1
print("{} → {}".format(Term1, Term2), end="")
cont = 3
while cont <= num:
    Term3 = Term1 + Term2
    print(" → {}".format(Term3), end="")
    Term1 = Term2
    Term2 = Term3
    cont += 1
print(" → FIM!")
