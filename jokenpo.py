from random import randint
itens = ['Pedra','Papel','Tesoura'] #criei uma lista com as jogadas
computador = randint (0,2) #computador vai sortear um dos itens 0 a 2

print (''' Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
'''
)
jogador = int(input('Qual a sua jogada? '))
print('=='*11)
print ('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('=='*11)

if computador == 0: #computador PEDRA
    if jogador == 0: #jogador PEDRA
        print ('EMPATE!! O computador jogou {} e o jogador jogou {}'.format(computador,jogador))
    elif jogador == 1: #jogador PAPEL
         print ('GANHOU!! O computador jogou {} e o jogador jogou {}'.format(computador,jogador))
    elif jogador == 2: #jogador TESOURA 
         print ('PERDEU!! O computador jogou {} e o jogador jogou {}'.format(computador,jogador))
    else:
         print('JOGADA INVALIDA. DIGITE 0, 1 ou 2')

elif computador == 1: #computador PAPEL
    if jogador == 0: #jogador PEDRA
        print ('PERDEU!! O computador jogou {} e o jogador jogou {}'.format(computador,jogador))
    elif jogador == 1: #jogador PAPEL
         print ('EMPATE!! O computador jogou {} e o jogador jogou {}'.format(computador,jogador))
    elif jogador == 2: #jogador TESOURA 
         print ('GANHOU!! O computador jogou {} e o jogador jogou {}'.format(computador,jogador))
    else:
         print('JOGADA INVALIDA. DIGITE 0, 1 ou 2')
        
elif computador == 1: #computador TESOURA
    if jogador == 0: #jogador PEDRA
        print ('GANHOU!! O computador jogou {} e o jogador jogou {}'.format(computador,jogador))
    elif jogador == 1: #jogador PAPEL
         print ('PERDEU!! O computador jogou {} e o jogador jogou {}'.format(computador,jogador))
    elif jogador == 2: #jogador TESOURA 
         print ('EMPATE!! O computador jogou {} e o jogador jogou {}'.format(computador,jogador))
    else:
         print('JOGADA INVALIDA. DIGITE 0, 1 ou 2')
