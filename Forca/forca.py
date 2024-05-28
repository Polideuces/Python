import random
import os

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def game():

    limpa_tela()
    print("\n Bem vindo ao jogo da forca!")
    print("\n Adivinhe as palavras abaixo: \n")

    palavras = ['banana', 'abacate', 'morango', 'laranja']

    # Escolha randômica de palavras
    palavra = random.choice(palavras)

    # Lista de palavras com espaços em branco
    letras_descobertas = [" "] * len(["_" for i in range(len(palavra))])

    # Número de chances
    chances = 6

    # Lista de letras erradas
    letras_erradas = []

    while chances > 0:

        print(" ".join(letras_descobertas))
        print("\nChances restantes: ", chances)
        print("Letras erradas:", " ".join(letras_erradas))

        tentativa = input("\nDigite uma letra: ").lower()

        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra.lower():
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        if all(letra != "_" for letra in letras_descobertas):
            print("\n Você venceu, a palavra era: ", palavra)
            print("\n Obrigado por jogar!!")

        if (chances == 0) & any(letra != "_" for letra in letras_descobertas):
            print("\n Você perdeu, a palavra era: ", palavra)
            print("\n Obrigado por jogar!!")


game()

    


