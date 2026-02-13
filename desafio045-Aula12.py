# Crie um programa que faça o computador jogar jokenpô(pedra-papel-tesoura) com você.
from random import randint
from time import sleep
jokenpô = ['Pedra', 'Papel', 'Tesoura']
com = randint(0, 2)
print("\033[33m""{:=^40}".format("JOKENPÔ"),"\033[m")
print("Qual a sua jogada?")
jogador = int(input("[0]Pedra\n[1]Papel\n[2]Tesoura\n"))

while True:
     print("\033[33m""-=-" * 10, "\033[m")
     print("Computador jogou {}.".format(jokenpô[com]))
     print("Jogador jogou {}.".format(jokenpô[jogador]))
     print("\033[33m""-=-" * 10, "\033[m")
     print("JO")
     sleep(1)
     print("KEN")
     sleep(1)
     print("PÔ!!!")

     if com == 0:
          if jogador == 0:
               print("\033[34m""EMPATE!""\033[m")
          elif jogador == 1:
               print("\033[32m""VITÓRIA!""\033[m")
          elif jogador == 2:
               print("\033[31m""DERROTA!""\033[m")
          break
     if com == 1:
          if jogador == 0:
               print("\033[31m""DERROTA!""\033[m")
          elif jogador == 1:
               print("\033[34m""EMPATE!""\033[m")
          elif jogador == 2:
               print("\033[32m""VITÓRIA!""\033[m")
          break
     if com == 2:
          if jogador == 0:
               print("\033[32m""VITÓRIA!""\033[m")
          elif jogador == 1:
               print("\033[m""DERROTA!""\033[m")
          elif jogador == 2:
               ("\033[34m""EMPATE!""\033[m")
          break