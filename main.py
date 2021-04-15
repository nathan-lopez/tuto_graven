import pygame
from game import Game
from math import ceil
pygame.init()
# generer la fenêtre de nptre jeu
# etape1 : definir le titre de notre jeu.
# titre de  notre jeu#
pygame.display.set_caption("Nathan_Game")
screen = pygame.display.set_mode((1080, 720))        # Surface de notre jeu ; redimension de notre fentre

# importation de l'image de bg de notre jeu et le stocker dans la variable si bat
background = pygame.image.load("assets/bg.jpg")

# importation de notre banniere
banner = pygame.image.load("assets/banner.png")
banner = pygame.transform.scale(banner, (500, 500)) # zoumer ou dezoumer l'ecran
banner_rect = banner.get_rect()
banner_rect.x = ceil(screen.get_width() / 4)
# importer le bouton
play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x  = ceil(screen.get_width()/3.3)
play_button_rect.y = ceil(screen.get_height()/2)
# charher la classe Game qui est notre jeu
game = Game()

# variable de debut de jeu
running = True

# boucle principale du jeu
while running:

    # application de l'arriere plan de notre jeu grace a blit
    screen.blit(background, (0, -200))

    # verifier si notre jeu a commencé ou non
    if game.is_playing:
        # declancher les instruction de la partie
        game.update(screen)
    else:
        # ecran d'accueil

        screen.blit(play_button, (play_button_rect.x, play_button_rect.y))
        screen.blit(banner, (banner_rect.x, 0))
    # mettre à jour l'ecran
    pygame.display.flip()

    # condition de sorti , si le joueur ferme la fenetre
    for event in pygame.event.get():
        # verifie si event = quitter
        if event.type == pygame.QUIT:
            running = False
        # pour detecter si l(user utilise une touche
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # si la touche espace est appuyer
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # si la souris est en colision avec le bouton joueur
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu on mode lancer
                game.start()
