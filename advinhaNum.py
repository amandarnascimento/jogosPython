from random import randint #importar a biblioteca "random" e a função gerar um numero aleatorio


numero_certo = randint(0, 10)

# Estrutura de repetiçao WHILE

ganhou = False

while ganhou == False:
    numero_usuario = int(input('Chute um número: '))

    if numero_usuario == numero_certo:
        ganhou = True
    else:
        if numero_usuario < numero_certo:
            print('O número é maior...')
        else:
            print('O número certo é menor...')

print('Você ganhou! ')

