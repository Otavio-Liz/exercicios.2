'''
Faça um programa que LEIA O  SEXO de uma pessoa, MAS SÓ ACEITE OS VALORES 'M' ou 'F'. Caso esteja errado, PEÇA A DIGITAÇÃO NOVAMENTE até um valor correto. 
'''
genero = str(input("Informe seu sexo: [M/F] ")).strip().upper()[0]
while genero not in "MmFf":
    genero = str(input("Valor informado é inválido.\nInforme seu sexo: [M/F] ")).strip().upper()[0]
if genero == "M":
    print("Sexo 'M'(Masculino) registrado com sucesso")
elif genero == "F":
    print("Sexo 'F'(Feminino) registrado com sucesso")