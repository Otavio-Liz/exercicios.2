'''
Refaça o DESAFIO 009, mostrando a tabuada de um número
que o usuário escolher, só que agora utilizando um laço for.
'''
num = int(input("Digite um número de 1 a 10: "))
for n in range(1, 11):
    print("{} x {} = {}.".format(num, n, n * num))
