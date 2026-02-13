"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

- À vista cheque/dinheiro: 10% de desconto
- À vista cartão: 5% de desconto
- Até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros

"""
while True:
    print("\033[4;32m" "{:=^40}" "\033[m".format ("\033[4;33m" " ELETROS LISBOA " "\033[4;32m"))

    produto = str(input("Qual produto você irá comprar?: "))
    valor_produto = float(input("Digite o valor do produto: "))
    print(f"O {produto} custa {valor_produto}!")
    pagamento = int(input("Qual a forma de pagamento?\n[1]À vista\n[2]À vista no cartão\n[3]2x no cartão\n[4]3x ou mais no cartão\n"))
    
    if pagamento == 1:
        print("À vista, você pagará R${} reais, com desconto de 10%.".format(valor_produto - (10 / 100 * 100)))
        confirmar_negar = int(input("Deseja continuar com o pagamento?\n1[SIM]\n2[NÃO]\n"))
        if confirmar_negar == 1:
             print('\033[4;34m' "Pagamento Concluído! \033[m \n \033[4;33m Você realizou a compra à vista, com desconto de 10%." '\033[m')
        else:
            print("Pagamento Cancelado!")
        break
    if pagamento == 2:
        print("À vista no cartão, você pagará R${} reais, com desconto de 5%.".format(valor_produto - (5 / 100 * 100)))
        confirmar_negar = int(input("Deseja continuar com o pagamento?\n1[SIM]\n2[NÃO]\n"))
        if confirmar_negar == 1:
            print('\033[4;34m' "Pagamento Concluído! \033[m\n \033[4;33m Você realizou a compra à vista no cartão, com desconto de 5%."'\033[m')
        else:
            print("Pagamento Cancelado!")
        break
    if pagamento == 3:
        vezes_cartão = int(input("Você pagará em quantas vezes?"))
        print("Em até 2x no cartão, você pagará o preço normal, R${} reais.".format(valor_produto))
        confirmar_negar = int(input("Deseja continuar com o pagamento?\n1[SIM]\n2[NÃO]\n"))
        if confirmar_negar == 1:
            print('\033[4;34m' "Pagamento Concluído! \033[m\n \033[33m Você realizou a compra em {} vezes no cartão sem juros de R${} reais." '\033[m'.format(vezes_cartão, valor_produto / vezes_cartão))
        else:
            print("Pagamento Cancelado!")
        break
    if pagamento == 4:
        vezes_cartão = int(input("Você pagará em quantas vezes?"))
        print("Em {}x, você pagará júros de 20%, totalizando R${} reais.".format(vezes_cartão, valor_produto + ( 20 /100 * 100) / vezes_cartão))
        confirmar_negar = int(input("Deseja continuar com o pagamento?\n1[SIM]\n2[NÃO]\n"))
        if confirmar_negar == 1:
            print('\033[4;34m'"Pagamento Concluído! \033[m\n \033[33m Você realizou a compra em {} vezes no cartão sem juros." '\033[m'.format(vezes_cartão))
        else:
            print("Pagamento Cancelado!")
        break