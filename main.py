import pygame
from game import Game
import math

pygame.init()

# génération fenetre jeu
pygame.display.set_caption("Comet Fall Game")
screen = pygame.display.set_mode((1080, 720))
background = pygame.image.load("assets/bg.jpg")

# importer banniere
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# charger bouton lance partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# charger notre jeu
game = Game()

running = True

while running:

    # appliquer arrière plan
    screen.blit(background, (0, -200))

    # vérifier si jeu a commencé ou non
    if game.is_playing:
        # déclencher les instruction de la partie
        game.update(screen)
    # vérfier si jeu a pas commencé
    else:
        # ajouter écran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    print(game.player.rect.x)

    # MAJ écran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # Détecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # détecter si la touche espace est enclenchée pour lancer projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Vérif si souris en collision avec bouton jouer
            if play_button_rect.collidepoint(event.pos):
                # mettre jeu en mode lancé
                game.start()

















