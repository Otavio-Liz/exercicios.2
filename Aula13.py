for i in range(0,6): 
    print("Hi")
print("FIM")

#---------------------------------------------------------------------------------------------
for i in range(6, 0, -1):
    print(i) # Ordeno que faça uma contagem regressiva de 6 a 1 diminuindo(-1) de 1 em 1.
    # Primeiro parâmetro é o início da contagem;
    # Segundo é o Ponto final;
    # Terceiro é a contagem de passos, se de 1 em 1, ou 2 em 2 etc...

#---------------------------------------------------------------------------------------------
i = float(input("Início: "))
f = float(input("fim: "))
p = float(input("Passo: "))
                            
for i in range(i, f, p):
    print(i)
print("FIM")
# Podemos fazer as variáveis(APENAS DO TIPO INTEIRO) interagir com o laço de repetição com range(intervalo).
# A função RANGE só itera sobre números inteiros.

#---------------------------------------------------------------------------------------------