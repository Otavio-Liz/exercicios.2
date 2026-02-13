cores = {"limpar": "\033[m",
         "amarelo": "\033[4;33;40m",
         "vermelho": "\033[4;31;30"}
nome = str(input("Digite seu nome: "))

if nome == "Otávio":
    print("Que nome bonito!")
elif nome == "Pedro" or nome == "Maria" or nome == "Ambrósio":
    print("Que nome esquisito!")
elif nome in "Ana Clarisse Juliana":
    print("Seu nome feminino é bonito!")
else:
    print("Seu nome é bem normal!")
print("Tenha um bom dia, {}{}{}!".format(cores["amarelo"], nome, cores["limpar"]))