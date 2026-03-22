'''
Faça um programa que mostre a TABUADA de vários números UM DE CADA VEZ para o valor digitado.
O programa será IMTERROMPIDO quando o número solicitado for NEGATIVO
'''
while True:
    num = int(input("Digite um número: "))
    if num < 0:
        break
    else:
        for n in range(1, 11):
            print("{} x {} = {}".format(num, n, num * n))