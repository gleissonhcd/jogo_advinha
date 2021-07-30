print("*******************************")
print("Bem vindo ao jogo de Advinhação")
print("*******************************")

numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1,total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = int(input("Digite o seu número: "))
    print("Você digitou ==> ", chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Parabéns você acertou o número!!!")
        break
    else:
        if(maior):
            print("Você errou seu chute foi maior que o número secreto")
        elif(menor):
            print("Você errou o seu número foi menor que o número secreto")


print("Fim de Jogo!!!")