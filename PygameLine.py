import pygame
from pygame.locals import MOUSEBUTTONDOWN

pygame.init()
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

branco = pygame.Color(255, 255, 255)
cm = 0
ponto1 = None
ponto2 = None

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            if cm == 0:
                ponto1 = pygame.mouse.get_pos()
                cm = 1
            elif cm == 1:
                ponto2 = pygame.mouse.get_pos()
                cm = 2  # agora temos 2 pontos

    # se já temos 2 pontos, desenha a linha
    if cm == 2:
        pygame.draw.line(screen, branco, ponto1, ponto2, 2)
        cm = 0  # reseta para poder desenhar outra linha

    pygame.display.update()

pygame.quit()