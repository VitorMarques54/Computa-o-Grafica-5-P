import pygame


pygame.init()
screen_width = 800
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

branco = pygame.Color(255, 255, 255)
pygame.display.set_caption("tela")

done = False
fundo = pygame.image.load("Imagem/images.jpg")
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(fundo, (0, 0))
    pygame.display.update()





pygame.quit()