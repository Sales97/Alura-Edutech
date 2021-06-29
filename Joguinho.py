print("Bem-vindo ao jogo da adivinhação!")
numero_secreto = 5
tentativas = 3

while(tentativas > 0):
    chute_str = input("Digite o seu número: ")
    print("você digitou " + chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Acertou!!!")
        break
    else:
        if (maior):
            print("Seu chute foi muito alto!")
        elif (menor):
            print("Seu chute foi muito baixo!")

    tentativas = tentativas - 1
    tentativas_str = str(tentativas)
    print("Tentativas restantes:" + tentativas_str)

escolha_replay = input("Quer jogar de novo? Se sim, digite 1. Se não, digite 0.")

print("Fim do jogo :)")