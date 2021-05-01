import pygame
import random

# creer une classe pour gere cette comete
class Comet(pygame.sprite.Sprite):
    def __init__(self, comet_event):
        super().__init__()
        # definir l'immage du comet
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event
        self.damag = 20

    def remove(self):
        self.comet_event.all_comets.remove(self)
        # joueur le son
        self.comet_event.game.sound_manager.play('meteorite')
        # verifier si le nombre de comet est de zero
        if len(self.comet_event.all_comets) == 0:
            # evenement fini
            self.comet_event.reset_percent()
            # apparaitre les monster
            self.comet_event.game.start()

    def fall(self):
        self.rect.y += self.velocity

         # ne tombe pas sur le sol
        if self.rect.y >= 500:
            # retirer la boule de feu
            self.remove()

            # verifier si il lya plus de joueur
            if len(self.comet_event.all_comets) == 0:
                # remettre la jauge au depart
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        # verifier si la boule de feu touche le joueur
        if self.comet_event.game.check_collision(
            self, self.comet_event.game.all_players
        ):
            self.remove()
            # subir le dega
            self.comet_event.game.player.damage(self.damag)