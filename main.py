import pygame
from game import Game

pygame.init()

# génération fenetre jeu
pygame.display.set_caption("Comet Fall Game")
screen = pygame.display.set_mode((1080, 720))
background = pygame.image.load("assets/bg.jpg")

# charger notre jeu
game = Game()

running = True

while running:

    # appliquer arrière plan

    screen.blit(background, (0, -200))

    # image joueur
    screen.blit(game.player.image, game.player.rect)

    # MAJ écran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            # quelle touche a été utilisée
            if event.key == pygame.K_RIGHT:
                game.player.move_right()
            elif event.key == pygame.K_LEFT:
                game.player.move_left()









