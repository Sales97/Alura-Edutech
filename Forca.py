import random

def jogar():
    mensagem_inicial()

    escolha_replay = 1
    while (escolha_replay == 1):
        palavra_secreta = escolha_ps()

        qtdd_letras = len(palavra_secreta)

        x = ["_"]
        letras_acertadas = x*qtdd_letras

        lista_erros = []

        enfoucou = False
        acertou = False
        erros = 0

        print(letras_acertadas)

        while(not enfoucou and not acertou):

            chute = input("Qual letra?").upper()
            if(chute in palavra_secreta):
                posicao = 0
                for letra in palavra_secreta:
                    if(chute == letra):
                        letras_acertadas[posicao] = letra
                    posicao = posicao + 1

            elif(chute in lista_erros):
                print("\n")
                print("Você já chutou essa letra!")

            else:
                erros = erros + 1
                print("Ops, você errou! Faltam {} tentativas.".format(7 - erros))
                desenha_forca(erros)
                lista_erros.append(chute)
                print(f"Chutes errados: {lista_erros}")

            enfoucou = erros == 7
            acertou = "_" not in letras_acertadas
            print("\n")
            print(letras_acertadas)

        if(acertou):
            print("Você ganhou!")
            print("       ___________      ")
            print("      '._==_==_=_.'     ")
            print("      .-\:      /-.    ")
            print("     | (|:.     |) |    ")
            print("      '-|:.     |-'     ")
            print("        \::.    /      ")
            print("         '::. .'        ")
            print("           ) (          ")
            print("         _.' '._        ")
            print("        '-------'       ")
        else:
            print(f"Acabaram suas chances! A palavra secreta era {palavra_secreta}!")
            print("    _______________         ")
            print("   /               \       ")
            print("  /                 \      ")
            print("//                   \/\  ")
            print("\|   XXXX     XXXX   | /   ")
            print(" |   XXXX     XXXX   |/     ")
            print(" |   XXX       XXX   |      ")
            print(" |                   |      ")
            print(" \__      XXX      __/     ")
            print("   |\     XXX     /|       ")
            print("   | |           | |        ")
            print("   | I I I I I I I |        ")
            print("   |  I I I I I I  |        ")
            print("   \_             _/       ")
            print("     \_         _/         ")
            print("       \_______/           ")

        escolha_replay = int(input("Deseja jogar de novo? Digite 1 se sim. Se não, digite 0."))
        if (escolha_replay == 1):
            print("\n" * 2)

    print("Fim do jogo")

def mensagem_inicial():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def escolha_ps():
    repertorio = ["Amarelo", "Amiga", "Amor", "Ave", "Avião", "Avó", "Balão", "Bebê", "Bolo", "Branco", "Cama",
                  "Caneca", "Celular", "Clube", "Copo", "Doce", "Elefante", "Escola", "Estojo", "Faca", "Foto",
                  "Garfo",
                  "Geleia", "Girafa", "Janela", "Limonada", "Mãe", "Meia", "Noite", "Óculos", "Ônibus", "Ovo",
                  "Pai",
                  "Pão", "Parque", "Passarinho", "Peixe", "Pijama", "Rato", "Umbigo"]
    palavra_secreta = random.choice(repertorio).upper()
    return palavra_secreta

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()