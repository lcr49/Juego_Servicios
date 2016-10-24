#!/usr/bin/env python

import sys, pygame
from pygame.locals import *
 

ancho = 640
alto = 480

 
def cargarImagen(filename, transparent=False):  
    image = pygame.image.load(filename)       
    return image.convert_alpha()
  
def main():
    screen = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Laurita Game")
 
    background_image = cargarImagen('imagenes/fondo3.png')
 
    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
 
        screen.blit(background_image, (0, 0))
        pygame.display.flip()
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()