'''
Melhore o jogo do DESAFIO 028, onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
''' 
import random 
print("Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.\nSerá que você consegue advinhar qual foi?\nDê seu palpite:")
com = random.randint(0, 10)
jogador = int(input("Pense em um número de 0 a 10: "))
cont = 0
while com != jogador:
    jogador = int(input("Tente novamente! Pense em um número de 0 a 10: "))  
    cont += 1
print("""Parabéns!\n
      Você tentou {} vezes até escolher exatamente o número que eu escolhi.
      """.format(cont))

