"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
1 - para binário
2 - para octal
3 - para exadecimal

"""

num = int(input("Digite um número inteiro qualquer: "))
print("Para qual base deseja converter o numero {}?.".format(num))
opcao = int(input("[1]Binário\n[2]Octal\n[3]Hexadecimal\n"))
if opcao == 1:
    print("O número {} na base binária é {}".format(num, bin(num)[2:]))
elif opcao == 2:
    print("O número {} na base octal é {}".format(num, oct(num)[2:]))
elif opcao == 3:
    print("O número {} na base hexadecimal é {}".format(num, hex(num)[2:]))