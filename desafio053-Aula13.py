'''
Crie um programa que leia uma FRASE qualquer e diga se ela é um PALÍNDROMO,
desconsiderando os espaços.
'''


nome = str(input("Digite uma frase qualquer: ")).upper()
n1 = nome.replace(" ", "")
n2 = nome[::-1].replace(" ", "")
print("O inverso de {} é {}.".format(n1, n2))
if n1 == n2:
    print("PALÍNDROMO")

frase = str(input("Digite uma frase:")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print("O inverso de {} é {}".format(junto, inverso))
if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("As palavras não formam palíndromo!")

