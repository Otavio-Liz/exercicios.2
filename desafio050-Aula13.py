'''
Desenvolva um programa que LEIA NÚMERO INTEIROS e mostre a soma APENAS daqueles que forem PARES. Se o valor digitado for IMPAR, desconsidere-o.
'''
soma = 0
cont = 0
for n in range(1, 6):
    num = int(input("Digite o {}° número: ".format(n)))
    cont += 1
    if num % 2 == 0:
        soma += num
print("Você digitou {} números. A soma dos pares é igual a {}.".format(cont, soma))
