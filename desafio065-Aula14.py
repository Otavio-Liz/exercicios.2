'''
Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo teclado. No final da execução, mostre a MÉDIA ENTRE TODOS os valores e qual foi o MAIOR e MENOR valores lidos. O programa deve perguntar ao usuário se ele quer ou não CONTINUAR a digitar valores.
'''
media = 0
condicao = ""
soma = 0
cont = 0
maior = 0
menor = 0
while condicao != "N":
    num = int(input("Digite um número: "))
    cont += 1
    if menor == 0:
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    soma = soma + num
    condicao = str(input("Deseja informar mais valores? [S/N]")).strip().upper()
media = soma/cont
print(f'''A média dos {cont} números informados é igual a {media:.1f}.
O Maior valor digitado foi {maior} e o Menor {menor}.''')