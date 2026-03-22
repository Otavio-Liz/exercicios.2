'''
Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é CONDIÇÃ DE PARADA. No final, mostre QUANTOS NÚMEROS foram digitados e qual foi a SOMA entre eles (desconsiderandoo flag)
'''

nums = soma = cont = 0
while nums != 999:
    nums = int(input("Digite um número: "))
    if nums == 999:
        print("Programa encerrado!")
        if soma == 0:
            print("Nenhum valor informado!")
    elif nums != 999: 
        cont += 1
        soma += nums
print("Você digitou {} números e a soma entre eles é igual a {}".format(cont, soma))
    

