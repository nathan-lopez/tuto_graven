import pygame
import random


# classe qui gere la notion du monter
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.health_max = 100
        self.velocity = random.randint(1, 3)
        self.attack = 5
        self.image = pygame.image.load("assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540

    def damage(self, amount):
        # infliger le degat au monstre
        self.health -= amount
        # verifier si ses points de vie est inferieure à zero
        if self.health <= 0:
            # supprimer le gars et le faire reaparaitre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 4)
            self.health = self.health_max

    def update_health_bar(self, surface):
        # barre de vie
        # definir une couleur pour la jauge de vie
        ## rendons leger le code :
        ##  bar_color = (111, 210, 46)
        ## bg_color = (60, 63, 60) # couleur d'arriere plan

        ##  # je definie ici la position ainsi que la largeur et longueur de la jauge de vie
        ##  bar_position = [self.rect.x + 10, self.rect.y - 20, self.health, 5]
        ##   # definir la position de l'arriere plan de notre jeu
        ##   bg_position = [self.rect.x + 10, self.rect.y - 20, self.health_max, 5]
        ##   # dessiner notre barre de vie
        ##  pygame.draw.rect(surface, bg_color, bg_position)
        ##  pygame.draw.rect(surface, bar_color, bar_position)
        ## code aleger ;

        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.health_max, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def forward(self):
        # ne se deplace que si il y a pas de colision avec un joueur ou un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est en colision avec le joueur , on va l'infliger de dega
        else:
            self.game.player.damage(self.attack)