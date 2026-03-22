'''
Crie um programa que simule o:
    FUNCIONAMENTO DE UM CAIXA ELETRÔNICO: 
    O programa vai informar quantas CÉDULAS de cada valor serão entregues.
        OBS: Considere que o caixa possui:
        CÉDULAS DE: R$50 
        CÉDULAS DE: R$20
        CÉDULAS DE: R$10
        CÉDULAS DE: R$1
'''

print("   BANCO LIS ")
print("---" * 5)
saque = float(input("Quanto deseja sacar?"))
total = saque
ced = 50
cont_ced = 0
while True:
    if total >= ced:
        total -= ced
        cont_ced += 1
    else:
        if cont_ced > 0:
            print(f"Total de {cont_ced} cédulas de R${ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        cont_ced = 0
        if total == 0:
            break
                