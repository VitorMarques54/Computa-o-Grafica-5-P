import pygame

pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

done = False
white = pygame.Color(255,255,255)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        pygame.draw.rect(screen, white, (250, 400, 10, 10))# Hamal
        pygame.draw.rect(screen, white, (450, 360, 10, 10))# Sheratan
        pygame.draw.rect(screen, white, (600, 420, 10, 10))# Mesarthim
        pygame.draw.rect(screen, white, (700, 500, 10, 10))# 41 Arietis
    pygame.display.update()


pygame.quit()