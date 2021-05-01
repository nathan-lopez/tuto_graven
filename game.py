import pygame
from player import Player
from monster import Mummy, Alien
from comet_event import CometFallEvent
from sound import SoundManager

# creer une nouvelle classe qui va representer notre jeu

class Game:

    def __init__(self):
        # definir si le jeu a commencer ou non
        self.is_playing = False
        self.all_players = pygame.sprite.Group()
        # generer notre joueur
        self.player = Player(self)
        self.all_players.add(self.player)
        # generer l'evenement
        self.comet_event = CometFallEvent(self)
        # definir un groupe de monsters
        self.all_monsters = pygame.sprite.Group()
        # gerer le son
        self.sound_manager = SoundManager()
        # mettre le score à zero
        self.score = 0
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def add_score(self, score=10):
        self.score += score

    def game_over(self):
        # remettre le jeu à neuf
        # retirer le monstre
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False
        self.score = 0
        # joueur le son
        self.sound_manager.play('game_over')

    def update(self, surface):
        # afficher le score sur l'ecran
        font = pygame.font.SysFont("monospace", 16, bold=True)
        score_text = font.render(f"Score : {self.score}", 1, (0, 0, 0),)
        surface.blit(score_text, (20, 20))
        # appliquer l'image de mon joeur
        surface.blit(self.player.image, self.player.rect)
        # actualiser la barre de vie du joueur
        self.player.update_health_bar(surface)
        # actualiser la barre d'evenment du jeu
        self.comet_event.update_ber(surface)
        # actualiser l'animation du joueur
        self.player.update_animation()
        # recuperer les projectiles que le joueur lance
        for projectile in self.player.all_projectille:
            projectile.move()
        # recuperer les monstres de notre jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(surface)
            monster.update_animation()

        # recuperer le comet du jeu
        for comet in self.comet_event.all_comets:
            comet.fall()

        # appliquer l'ensemble des image du projectile
        self.player.all_projectille.draw(surface)

        # appliquer l'ensemble des images du groupe monster
        self.all_monsters.draw(surface)

        # appliquer l'ensemble des image du groupe comet
        self.comet_event.all_comets.draw(surface)

        # pour verifier si le joueur souhaite aller à gauche ou à droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < surface.get_width() - 200:
            self.player.move_rigth()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()


    def spawn_monster(self, monster_name):
        self.all_monsters.add(monster_name.__call__(self))

    def check_collision(self, sprite, groupe):
        return pygame.sprite.spritecollide(sprite, groupe, False, pygame.sprite.collide_mask)
