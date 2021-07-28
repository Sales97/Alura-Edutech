print("Bem-vindo ao jogo da adivinhação!")
import random

escolha_replay = 1
while(escolha_replay == 1):
        print("Adivinhe o número secreto de 1 até 10!")
        numero_secreto = random.randint(1, 10)
        tentativas = 3
        while(tentativas > 0):
            chute_str = input("Digite o seu número: ")
            print("Você digitou " + chute_str + "!")
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
                print("Tentativas restantes: " + tentativas_str)

        print("O número correto era o: " + str(numero_secreto))
        escolha_replay = int(input("Deseja jogar de novo? Digite 1 se sim. Se não, digite 0."))
        if(escolha_replay == 1):
            tentativas = 3
            print("\n" * 2)


print("Fim de Jogo! :)")