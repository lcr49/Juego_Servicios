#!/usr/bin/env python
import sys, pygame
from pygame.locals import *
 
alto = 640
ancho = 480
class Trofeo(pygame.sprite.Sprite):
    def __init__(self):#inicializa la clase
        pygame.sprite.Sprite.__init__(self)
        self.image = cargarImagen("imagenes/trofeo.png")#imagen muñeco
        self.rect = self.image.get_rect()#dimensiones de la imagen
        self.rect.centerx = 610
        self.rect.centery = 376 #posicion el muñeco en la imagen
        self.speed = 0.5#velocidad con la que se mueve el muñeco
        
 
def gameOver(self):
    screen = pygame.display.set_mode((alto, ancho)) 
    background_image = cargarImagen('imagenes/gameOver.png')
    pygame.display.set_caption("Laurita Game")
 
    clock = pygame.time.Clock()
 
    while True:
        time = clock.tick(60)
        keys = pygame.key.get_pressed()
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
        
        screen.blit(background_image, (0, 0))

        pygame.display.flip()
    return 0 

def ganar(self):
    screen = pygame.display.set_mode((alto, ancho)) 
    background_image = cargarImagen('imagenes/ganar.png')
    pygame.display.set_caption("Laurita Game")
 
    clock = pygame.time.Clock()
 
    while True:
        time = clock.tick(60)
        keys = pygame.key.get_pressed()
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
        
        screen.blit(background_image, (0, 0))

        pygame.display.flip()
    return 0 
    
class Caramelo(pygame.sprite.Sprite):
    def __init__(self,x ,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = cargarImagen("imagenes/caramelo.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = ancho / x
        self.rect.centery = alto / y
        self.speed = [0, -0.3]
 

    def actualizar(self, time, galleta):
        self.rect.centery += self.speed[0] * time
        self.rect.centery += self.speed[1] * time
        if self.rect.top <= 0 or self.rect.bottom >= ancho:
            self.speed[1] = -self.speed[1]
            self.rect.centery += self.speed[1] * time
        if pygame.sprite.collide_rect(self, galleta):
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[1] * time
            gameOver(self) 
   

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
                
    def actualizarGalleta(self, time, trofeo):
        if pygame.sprite.collide_rect(self, trofeo):
            ganar(self)             
                

def cargarImagen(filename, transparent=False):  
    image = pygame.image.load(filename)       
    return image.convert_alpha()
 
def main():
    screen = pygame.display.set_mode((alto, ancho)) 
    background_image = cargarImagen('imagenes/fondo3.png')
    pygame.display.set_caption("Laurita Game")
    galleta = Galleta()
    trofeo = Trofeo()
    caramelo = Caramelo(1.05,1.99)
    caramelo1 = Caramelo(1.20,2.99)
    caramelo3 = Caramelo(1.50,9.99)
    caramelo5 = Caramelo(2.99,1.99)
    caramelo6 = Caramelo(5.95,1.40)
 
    clock = pygame.time.Clock()
 
    while True:
        time = clock.tick(60)
        keys = pygame.key.get_pressed()
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
        
        galleta.mover(time, keys)
        galleta.actualizarGalleta(time, trofeo)
        caramelo.actualizar(time, galleta)
        caramelo1.actualizar(time, galleta)
        caramelo3.actualizar(time, galleta)
        caramelo5.actualizar(time, galleta)
        caramelo6.actualizar(time, galleta)
         
        screen.blit(background_image, (0, 0))
        screen.blit(galleta.image, galleta.rect)
        screen.blit(trofeo.image, trofeo.rect)
        screen.blit(caramelo.image, caramelo.rect)
        screen.blit(caramelo1.image, caramelo1.rect)
        screen.blit(caramelo3.image, caramelo3.rect)
        screen.blit(caramelo5.image, caramelo5.rect)
        screen.blit(caramelo6.image, caramelo6.rect)
        pygame.display.flip()
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()