# Interrompendo estrutura de Repetição
s = 0
nome = "Sírius"
idade = 45
salario = 833.56
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n
# print("A soma vale {}.".format(s))
print(f"A soma vale {s}")
print(f"O {nome} tem {idade} anos e recebe {salario:.2f} galeões.")