'''
Faça um programa que jogue PAR OU IMPAR com o computador. 
O jogo só será encerrado QUANDO O JOGADOR PERDER.
Mostre o total de vitórias consecutivas no final do jogo 
'''
from random import randint
cont = 0
win = ""
print("\033[32m" "-=-" * 10 ,"\033[m")
print("\033[33m""   VAMOS JOGAR PAR OU IMPAR" "\033[m")
print("\033[32m" "-=-" * 10 ,"\033[m")
while True:
    comp = randint(1, 10)
    jogador = int(input("Chuta um valor: "))
    soma = comp + jogador
    par_impar = str(input("Par ou Impar → [P/I]?" )).strip().upper()
    if soma % 2 == 0:
        if par_impar == "P":
            print("\033[33m" "---" * 12 , "\033[m")
            print("\033[32m""CONGRATULATIONS! You won 🎆🎆🎆🎆🎆")
            print("\033[33m" "---" * 12 , "\033[m")
            print(f"Você jogou {jogador} e o computador {comp}. O TOTAL de {soma} é PAR")
            print("Vamos jogar novamente...")
            cont += 1 
            win += "🏆"
        else: 
            print("\033[31m" "---" * 10 , "\033[m")
            print("\033[31m"" GAME OVER! 😩😩😩😩😩")
            print("\033[31m" "---" * 10 , "\033[m")
            print(f"Você jogou {jogador} e o computador {comp}. O TOTAL de {soma} é PAR")
            print(f"Você venceu {cont} vezes. {win}")
            break
    elif soma % 2 != 0:
        if par_impar == "I":
            print("\033[33m" "---" * 12 , "\033[m")
            print("\033[32m""CONGRATULATIONS! You won 🎆🎆🎆🎆🎆")
            print("\033[33m" "---" * 12 , "\033[m")
            print(f"Você jogou {jogador} e o computador {comp}. O TOTAL de {soma} é IMPAR")
            print("Vamos jogar novamente...")
            cont += 1 
            win += "🏆"
        else:
            print("\033[31m" "---" * 10 , "\033[m")
            print("\033[31m"" GAME OVER! 😩😩😩😩😩")
            print("\033[31m" "---" * 10 , "\033[m")
            print(f"Você jogou {jogador} e o computador {comp}. O TOTAL de {soma} é IMPAR")
            print(f"Você venceu {cont} vezes. {win}")
            break
