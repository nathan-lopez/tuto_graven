import pygame
from player import Player
from monster import Monster


# creer une nouvelle classe qui va representer notre jeu
class Game:

    def __init__(self):
        # definir si le jeu a commencer ou non
        self.is_playing = False
        self.all_players = pygame.sprite.Group()
        # generer notre joueur
        self.player = Player(self)
        self.all_players.add(self.player)
        # definir un groupe de monsters
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()

    def start(self):
        self.is_playing = True
        self.spawn_monster()
    def game_over(self):
        # remettre le jeu à neuf
        # retirer le monstre
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, surface):
        # appliquer l'image de mon joeur
        surface.blit(self.player.image, self.player.rect)
        # actualiser la barre de vie du joueur
        self.player.update_health_bar(surface)
        # recuperer les projectiles que le joueur lance
        for projectile in self.player.all_projectille:
            projectile.move()
        # recuperer les monstres de notre jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(surface)
        # appliquer l'ensemble des image du projectile
        self.player.all_projectille.draw(surface)

        # appliquer l'ensemble des images du groupe monster
        self.all_monsters.draw(surface)

        # pour verifier si le joueur souhaite aller à gauche ou à droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < surface.get_width() - 200:
            self.player.move_rigth()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()


    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)

    def check_collision(self, sprite, groupe):
        return pygame.sprite.spritecollide(sprite, groupe, False, pygame.sprite.collide_mask)
