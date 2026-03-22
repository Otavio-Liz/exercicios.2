'''
Crie um programa que leia o NOME e o PREÇO de vários produtos.
O programa deverá perguntar se o USUÁRIO vai continuar. No final mostre:
→ Qual é o TOTAL GASTO na compra
→ Quantos produtos custam MAIS de R$1000
→ Qual é o NOME do produto MAIS BARATO
'''
total = 0.0
acima_1000 = 0
mais_barato = 0
produto_mais_barato = ""
print("---" * 10)
print("""         LOJAS LISBOA
 O melhor dos produtos Lisboa""")
print("---" * 10)
while True:
    produto = str(input("Produto: "))
    preco = float(input("Preço: "))
    total += preco
    if preco > 1000:
        acima_1000 += 1
    if mais_barato == 0 or preco < mais_barato:
        mais_barato = preco
        produto_mais_barato = produto
    continua_ou_não = str(input("Inserir mais itens no carrinho: [S/N]? ")).strip().upper()[0]
    if continua_ou_não == "N":
        break
print("---" * 5, end="")
print("Suas Compras", end="")
print("---" * 5)
print()
print(f"""O valor total de suas compras é R${total} reais.
Os produtos acima de R$1.000 reais da sua lista de compra, somam um total de {acima_1000} produtos.
O produto mais barato da lista é o/a {produto_mais_barato}, custando apenas R${mais_barato} reais.""")

