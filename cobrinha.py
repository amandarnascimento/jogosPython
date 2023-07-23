import pygame
import pygame.locals
from random import randint

"""Funções para funcionamento do jogo"""
def posicao_aleatoria():
    x = randint(0,590)
    y = randint(0,590)

    return (x//10*10, y//10*10)

"""
    200,200 - cobrinha
    200,200 - comida
"""
def colisao(a, b):
    return (a[0] == b[0]) and (a[1] == b[1])

# Lógica de funcionamento de um jogo
# 1. eventos;
# 2. os eventos são atualizados (FPS);
# 3. eventos são repetidos

## Iniciando as variáveis de controle
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Iniciamos o nosso módulo pygame
pygame.init()

# Fizemos as definições de tela
tela = pygame.display.set_mode((600,600))
pygame.display.set_caption("Jogo da Cobrinha")

# Desenhando a cobrinha (entidade)
cobrinha = [(200,200), (210,200), (220,200)] #defini a cobrinha
cobrinha_roupa = pygame.Surface((10,10)) #defini o corpo/roupa da cobrinha
cobrinha_roupa.fill((3, 94, 7)) #adicinei cor ao corpo da cobrinha

# Desenhando a maçã que
posicao_comida = posicao_aleatoria()
comida = pygame.Surface((10,10))
comida.fill((240, 65, 7))

direcao_eventos = LEFT

controle = pygame.time.Clock()

while True:

    controle.tick(10)

    # Manipulando os nosso eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            direcao_eventos = UP
        if event.key == pygame.K_DOWN:
            direcao_eventos = DOWN
        if event.key == pygame.K_LEFT:
            direcao_eventos = LEFT
        if event.key == pygame.K_RIGHT:
            direcao_eventos = RIGHT
    
    if colisao(cobrinha[0], posicao_comida):
        posicao_comida = posicao_aleatoria()
        cobrinha.append((0,0))
    
    # Estamos aumentando o tamanho da cobrinha
    for indice in range(len(cobrinha)-1, 0, -1):
        cobrinha[indice] = (cobrinha[indice-1][0], cobrinha[indice-1][1])
        

    # Movimentação da entidade cobrinha
    if direcao_eventos == UP:
        cobrinha[0] = (cobrinha[0][0], cobrinha[0][1]-10)
    if direcao_eventos == DOWN:
        cobrinha[0] = (cobrinha[0][0], cobrinha[0][1]+10)
    if direcao_eventos == RIGHT:
        cobrinha[0] = (cobrinha[0][0]+10, cobrinha[0][1])
    if direcao_eventos == LEFT:
        cobrinha[0] = (cobrinha[0][0]-10, cobrinha[0][1])

    tela.fill((0,0,0))
    tela.blit(comida, posicao_comida)

    for posicao in cobrinha:
            tela.blit(cobrinha_roupa, posicao)

    # atualiza os eventos do jogo e executa
    pygame.display.update()