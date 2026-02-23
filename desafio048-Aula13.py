'''
Faça um programa que calcule a soma entre todos os números ímpares e que são múltiplos de três e qua se encontram no intervalo de 1 - 500.
'''
soma = 0
cont = 0
for i in range(1, 501,2):
    if i % 3 == 0:
        soma += i
        cont += 1
print("A soma de todos os {} valores, resultou no valor {}.".format(cont, soma))
        
    
    
    
