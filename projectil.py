import pygame


# definition de la classe qui va gerer la notion du projectil
class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load("assets/projectile.png")
        # redimension de l'image
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        # pour la rotation
        self.origin_image = self.image
        self.angle = 0

    # pour faire une roataton au niveau du projectile

    def rotate(self):
        self.angle += 7
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    # supprimeur de projectif

    def remove(self):
        self.player.all_projectille.remove(self)
    # deplacement du projectile

    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        # si le projectile rencontre un monstres
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove() # supprimer le projectile
            # infliger le degat
            monster.damage(self.player.attack)
        # pour effacer le projectile qui ne plus present sur l'ecran
        if self.rect.x > 1080:
            self.remove()
