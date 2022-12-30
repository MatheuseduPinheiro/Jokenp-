from random import randint
from time import sleep
def jokenpo_single_player(player,pc):
    if player == 0: # jogador escolheu pedra
        if pc == 0:
            print('EMPATE')
        elif pc == 1:
            print("Jogador GANHOU")
        elif pc == 2:
            print("Jogador PERDEU")
    elif(player == 1): # jogador escolheu papel
        if pc == 0:
            print('Jogador GANHOU')
        elif pc == 1:
            print('EMPATE')
        elif pc == 2:
            print('jogador PERDEU')
    elif(player == 2): # se jogador escolher tesoura
        if pc == 0:
            print('Jogador PERDEU')
        elif pc == 1:
            print('jogador GANHOU')
        elif pc == 2:
            print('EMPATE')




def tratamento_escolha(player):
    while True:
        if player < 0 or player > 2:
            player=int(input('->Faça uma jogada válida: '))
        else:
            break




def play():
    print('\n0 - Pedra')
    print('1 - Papel')
    print('2 - Tesoura')

    itens=('Pedra ',' Papel ', 'Tesoura')
    jogador=int(input('\nQual é a sua jogada? '))
    tratamento_escolha(jogador)
    computador=randint(0,2)
    sleep(1)
    print('-='*15)

    print(f"Computador escolheu {itens[computador]}")
    print(f"Jogador escolheu {itens[jogador]}")
    print('-='*15)
    sleep(1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('POOOO!!!')
    sleep(1)
    print('')
    jokenpo_single_player(jogador,computador)


print('>>'*10+'BEM VINDOS AO JOKENPÔ'+'<<'*10)
play()
while True:
    continuar = str(input('Deseja continuar?[S/N]')).strip().upper()[0]
    if continuar in 'SN':
        if continuar in 'S':
            play()
        elif continuar in 'N':
            break
    else:
        continue