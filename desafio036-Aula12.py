"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprésimo será negado.

"""
cores = {"limpar": "\033[m",
         "yellow": "\033[4;33;40m"}

print("-=-" * 7)
print(cores["yellow"],"LISBOA EMPRÉSTIMOS",cores["limpar"])
print("-=-" * 7)

valor_casa = float(input("Qual o valor da casa? "))
salario = float(input("Quanto você recebe mensalmente? "))
anos_pagamento = int(input("Em quantos anos o empréstimo será pago? "))
# Calculo de parcelas mensais = (valor do imóvel / (prazo do financiamento em anos * 12)) * (1 + (taxa anual / 12))
mensal = (valor_casa / (anos_pagamento * 12)) * (1 + (0.10 / 12))
# Total do pagamento = pagamento mensal * prazo do financiamento em anos * 12
total = mensal * (anos_pagamento * 12)
minimo_salario = salario * (30/100)
if minimo_salario < mensal:
    print("EMPRÉSTIMO NEGADO!")
else:
    print("EMPRÉSTIMO APROVADO!")
    print ("A casa no valor de R${:.2f} reais, foi aprovada com parcelas mensais de R${:.2f} reais.".format(valor_casa, mensal))
    print("A casa ficou com valor total de pagamento em R${:.2f} reais.".format(total))
    print("PARABÉNS!")