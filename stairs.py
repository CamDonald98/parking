
#
import pygame
import settings as opt

import logging
info = logging.info
debug = logging.debug
error = logging.error
warning = logging.warning
collide = pygame.sprite.spritecollide

from vec import Vec2d as Vector

class Stairs(pygame.sprite.Sprite):
    oid = 0
    def __init__(self, world, pos):
        self._layer = opt.STAIRS_LAYER
        self.groups = world.all_sprites, world.stairs
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.oid = Stairs.oid
        Stairs.oid += 1
        self.world = world
        self.image = pygame.image.load("img/stairs-0.png")
        self.image = self.image.convert_alpha()
        #self.image = pygame.transform.scale(self.image,(100,200))
        self.rect = self.image.get_rect()
        self.pos = Vector(pos)

        ##get_windows_size --> larghezza altezza 

    def update(self):
        self.rect.center = self.pos
