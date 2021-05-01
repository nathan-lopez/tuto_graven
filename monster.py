import pygame
import random
import animation

# classe qui gere la notion du monter
class Monster(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.health_max = 100
        self.attack = 2
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540 - offset
        self.loot_amount = 10
        self.start_animation()

    def set_speed(self, speed):
        self.default_speed = 3
        self.velocity = random.randint(1, self.default_speed)

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def damage(self, amount):
        # infliger le degat au monstre
        self.health -= amount
        # verifier si ses points de vie est inferieure à zero
        if self.health <= 0:
            # supprimer le gars et le faire reaparaitre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 4)
            self.health = self.health_max
            # ajouter le nombre de points
            self.game.add_score(self.loot_amount)

            # si la barre d'evenemet est charger au max
            if self.game.comet_event.is_full_loaded():
                # le retirer du jeu
                self.game.all_monsters.remove(self)

                # pour essayer de declancher la pluie de commet
                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)

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

# definir une classe pour la momie
class Mummy(Monster):
    def __init__(self, game):

        super().__init__(game, "mummy", (130, 130))
        self.set_speed(3)
        self.set_loot_amount(20)

# definir une classe pour l'alliene
class Alien(Monster):

    def __init__(self, game):

        super().__init__(game, 'alien', (300, 300), 127)
        self.health = 250
        self.health_max = 250
        self.set_speed(2)
        self.set_loot_amount(40)

