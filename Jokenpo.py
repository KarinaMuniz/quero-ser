#Jokenpo - DojoPuzzles
user1 = int(input("Escolha pedra[1], papel[2] ou tesoura[3] ou [0] para terminar o jogo: "))
user2 = int(input("Escolha pedra[1], papel[2] ou tesoura[3] ou [0] para terminar o jogo: "))

while ((user1>0 and user1<4) or (user2>0 and user2<4)):
    #Exibe escolhas na tela
    if user1==1:
        print("Usuário 1 escolheu pedra")
    elif user1==2:
        print("Usuário 1 escolheu papel")
    else:
        print("Usuário 1 escolheu tesoura")

    if user2==1:
        print("Usuário 2 escolheu pedra")
    elif user2==2:
        print("Usuário 2 escolheu papel")
    else:
        print("Usuário 2 escolheu tesoura")
    #Exibe resultados do jogo
    if user1==user2:
        print("Empate.")
    elif user1 == 1:
        if user2 == 2:
            print("Pedra perde para papel")
            print("Usuário 2 ganhou!")
        else:
            print("Pedra ganha da tesoura")
            print("Usuário 1 ganhou!")
    elif user1 == 2:
        if user2 == 1:
            print("Papel ganha da pedra")
            print("Usuário 1 ganhou!")
        else:
            print("Papel perde da tesoura")
            print("Usuário 2 ganhou!")
    else:
        if user2 == 1:
            print("Tesoura perde para pedra")
            print("Usuário 2 ganhou!")
        else:
            print("Tesoura ganha do papel")
            print("Usuário 1 ganhou!")
    #Reinicia/Termina jogo
    user1 = int(input("Escolha pedra[1], papel[2] ou tesoura[3] ou [0] para terminar o jogo: "))
    user2 = int(input("Escolha pedra[1], papel[2] ou tesoura[3] ou [0] para terminar o jogo: "))

print("Fim de jogo.")
