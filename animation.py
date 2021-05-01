import pygame


# contenir le mechaanisme des animations

class AnimateSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, self.size)
        self.current_image = 0
        self.images = animations.get(sprite_name)
        self.animation = False

    # metthode pour demarrer l'animation
    def start_animation(self):
        self.animation = True

    # pour animer les sprites
    def animate(self, loop=False):
            # verifier si l'animation est sur vraie
            if self.animation:
                # passer à l'image suivante
                self.current_image += 1

                # verifier si on atteint la fin de l'animation
                if self.current_image >= len(self.images):
                    # remettre l'animation au depart
                    self.current_image = 0
                    if loop is False:
                        # desactivation de l'animation
                        self.animation = False
                # modififer l'image precendant par la suivante
                self.image = self.images[self.current_image]
                self.image = pygame.transform.scale(self.image, self.size)


# definir une fonction pour charger les images d'un sprite
def load_animation_image(sprite_name):
    # charger les 24 images de ce sprite
    images = []
    # charger les images
    path = f'assets/{sprite_name}/{sprite_name}'

    # boulcer sur chaque iamges
    for num in range (1, 24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    return images

# definir un dico qui va contenir les images chargées
animations = {
    'mummy': load_animation_image('mummy'),
    'player': load_animation_image('player'),
    'alien': load_animation_image('alien')
}
