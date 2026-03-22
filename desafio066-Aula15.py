'''
Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999 (CONDIÇÃO DE PARADA).
No final, mostre QUANTOS NÚMEROS foram digitados e qual foi a SOMA entre eles DESCONSIDERANDO A FLAG

'''
soma = cont = 0

while True:
    num = int(input("Digite um número: "))
    if num == 999:
        break
    else:
        cont += 1
        soma += num
print(f"Você digitou {cont} números e a soma entre eles foi {soma} ")