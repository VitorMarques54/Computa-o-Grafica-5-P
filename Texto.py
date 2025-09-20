import pygame


pygame.init()
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

branco = pygame.Color(255, 255, 255)
fonte = pygame.font.SysFont('Arial', 20, bold=False, italic=True)
texto = fonte.render('Vitor da Silveira Marques', False, branco)
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(texto, (10, 10))

    pygame.display.update()





pygame.quit()