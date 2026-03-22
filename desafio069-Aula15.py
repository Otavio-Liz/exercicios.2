'''
Leia a IDADE e o SEXO de VÁRIAS PESSOAS.
A cada pessoa cadrastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final mostre:
→ Quantas pessoas tem mais de 18 anos.
→ Quantos HOMENS foram cadrastrados.
→ Quantas MULHERES tem menos de 20 anos.
'''
maiores18 = homens = mulher_menor_20 = 0
while True:
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite seu gênero: [M/F]")).strip().upper()[0]
    if idade >= 18:
        maiores18 += 1
    if sexo == "M":
        homens += 1
    if idade < 20:
        if sexo == "F":
            mulher_menor_20 += 1
    opcao = str(input("Deseja cadastrar mais alguém? [S/N]")).strip().upper()[0]
    if opcao == "N":
        break
print(f"""Foram cadastrados um total de {maiores18} pessoas maiores de 18 anos.
Temos um total de {homens} homens cadastrados.
Entre as mulheres, {mulher_menor_20} delas tem menos de 20 anos de idade!""")