#!/usr/bin/env python
import sys, pygame
from pygame.locals import *
 
alto = 640
ancho = 480

class Galleta(pygame.sprite.Sprite):
    def __init__(self):#inicializa la clase
        pygame.sprite.Sprite.__init__(self)
        self.image = cargarImagen("imagenes/galleta.png")#imagen muñeco
        self.rect = self.image.get_rect()#dimensiones de la imagen
        self.rect.centerx = 30
        self.rect.centery = 360 #posicion el muñeco en la imagen
        self.speed = 0.5#velocidad con la que se mueve el muñeco
        
    def mover(self, time, keys):
        if self.rect.left >= 0:
            if keys[K_LEFT]:#si tienes la tecla izquierda pulsada se mueve
                self.rect.centerx -= self.speed * time
        if self.rect.right <= alto:
            if keys[K_RIGHT]:#si tienes la tecla derecha pulsada se mueve
                self.rect.centerx += self.speed * time
        

def cargarImagen(filename, transparent=False):  
    image = pygame.image.load(filename)       
    return image.convert_alpha()
 
def main():
    screen = pygame.display.set_mode((alto, ancho)) 
    background_image = cargarImagen('imagenes/fondo3.png')
    pygame.display.set_caption("Laurita Game")
    galleta = Galleta()
 
    clock = pygame.time.Clock()
 
    while True:
        time = clock.tick(60)
        keys = pygame.key.get_pressed()
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
 
        galleta.mover(time, keys)
        screen.blit(background_image, (0, 0))
        screen.blit(galleta.image, galleta.rect)
        pygame.display.flip()
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()