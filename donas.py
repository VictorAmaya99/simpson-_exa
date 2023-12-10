import pygame

class Dona(pygame.sprite.Sprite):
    def __init__(self, size, coordenate, path_imagen):
        self.coordenate = coordenate
        self.image = pygame.transform.scale(pygame.image.load(path_imagen).convert_alpha(), size)
        self.rect = self.image.get_rect()
        self.rect.topleft = coordenate
        self.active = True

    def update(self):
        self.rect.y += 5