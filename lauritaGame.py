#!/usr/bin/env python

import sys, pygame
from pygame.locals import *
 

ancho = 640
alto = 480

class Galleta(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = cargarImagen("imagenes/galleta.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = 30
        self.rect.centery = 360
        self.speed = [0.5, -0.5]
         
def cargarImagen(filename, transparent=False):  
    image = pygame.image.load(filename)       
    return image.convert_alpha()
  
def main():
    screen = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Laurita Game")
    background_image = cargarImagen('imagenes/fondo3.png')
    #creamos objetos
    galleta = Galleta()
 
    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
        #ponemos en ventana
        screen.blit(background_image, (0, 0))
        screen.blit(galleta.image, galleta.rect)
        pygame.display.flip()
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()