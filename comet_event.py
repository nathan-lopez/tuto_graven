import pygame
from comet import Comet

# creer une classe pour géner cet eventment
class CometFallEvent:

    # lors du chargment ==> creer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 5
        self.game = game
        self.fall_mode = False
        # groupe de sprite pour stocker nos cometes
        self.all_comets = pygame.sprite.Group()


    def add_percent(self):
        self.percent += self.percent_speed/100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        # booucle pour les valeurs entre 1 et 10
        for i in range(1, 11):
            # apparaitre une boule de feu
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        # si la barre d'evenemennt est completement charger
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            print("pluie de comets")
            self.meteor_fall()
            self.fall_mode = True

    def update_ber(self, screen):
        # ajouter du pourcentage à la barre
        self.add_percent()


        # barre noir en bg
        pygame.draw.rect(screen, (0, 0, 0), [
            0, screen.get_height() - 20, screen.get_width(), 10
        ])
        # barre rouge (jauge d'evenement)
        pygame.draw.rect(screen, (187, 11, 11), [
            0, screen.get_height() - 20, (screen.get_width() / 100) * self.percent, 10
        ])