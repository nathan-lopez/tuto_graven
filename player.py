import pygame
from projectil import Projectile
import animation

# creer une premiere classe qui va representer notre joueur
# faudra transformet cela en sprite, classe de base de tout les element graphique du jeu
class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__('player')
        self.health = 100
        self.game = game
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
        self.all_projectille = pygame.sprite.Group()

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else :
            # si le joeur n'a plus de point de vie
            self.game.game_over()

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 10,  self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 10, self.health, 7])

    def launch_projectile(self):
        self.all_projectille.add(Projectile(self))
        # demarrer l'animation du joueur
        self.start_animation()
        # jouer le son lors du tire
        self.game.sound_manager.play('tir')


    def move_rigth(self):
        # creer une nouvelle instance de projectile
        if not self.game.check_collision(self, self.game.all_monsters):
            # le deplacement ne se fait que si on ne croise pas de monstre
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
