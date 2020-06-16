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

    # actualiser barre vie joueur

    game.player.update_health_bar(screen)


# résupérer les projectiles du joueur

    for projectile in game.player.all_projectiles:
        projectile.move()

    # résupérer les monstres
    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)


    # appliquer l'ensemble des images de mon groupe de projectiles
    game.player.all_projectiles.draw(screen)

    # appliquer l'ensemble des images de mon groupe de monstres
    game.all_monsters.draw(screen)


# Vérifier si le joueur souhaite aller à gauche ou à droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

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











