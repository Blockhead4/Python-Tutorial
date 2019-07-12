import gettext
import math
import random
import sys
from time import sleep

import pygame
from pygame.locals import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
YELLOW = (250, 250, 20)
BLUE = (20, 20, 250)

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('PySpaceShip: 우주 암석 피하기 게임')
pygame.display.set_icon(pygame.image.load('wprp.png'))
fps_clock = pygame.time.Clock()
FPS = 60
score = 0

default_font = pygame.font.Font('NanumGothic.ttf', 28)
background_img = pygame.image.load('background.jpg')
explosion_sound = pygame.mixer.Sound('explosion.wav')
warp_sound = pygame.mixer.Sound('warp.wav')
pygame.mixer.music.load('Inner_Sanctum.mp3')

class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super(Spaceship, self).__init__()
        self.image = pygame.image.load('spaceship.png')
        self.rect = self.image.get_rect()
        self.centerx = self.rect.centerx
        self.centery = self.rect.centery

    def set_pos(self, x, y):
        self.rect.x = x - self.centerx
        self.rect.y = y - self.centery

    def collide(self, sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self, sprite):
                return sprite

class Rock(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, hspeed, vspeed):
        super(Rock, self).__init__()
        rocks = ('rocks01.png', 'rocks02.png', 'rocks03.png', 'rocks04.png', 'rocks05.png',
                 'rocks06.png', 'rocks07.png', 'rocks08.png', 'rocks09.png', 'rocks10.png',
                 'rocks11.png', 'rocks12.png', 'rocks13.png', 'rocks14.png', 'rocks15.png',
                 'rocks16.png', 'rocks17.png', 'rocks18.png', 'rocks19.png', 'rocks20.png',
                 'rocks21.png', 'rocks22.png', 'rocks23.png', 'rocks24.png', 'rocks25.png',
                 'rocks26.png', 'rocks27.png', 'rocks28.png', 'rocks29.png', 'rocks30.png',)
        
        self.image = pygame.image.load(random.choice(rocks))
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.hspeed = hspeed
        self.vspeed = vspeed

    def set_direction(self):
        if self.hspeed > 0:
            self.image = pygame.transform.rotate(self.image, 270)
        elif self.hspeed < 0:
            self.image = pygame.transform.rotate(self.image, 90)
        elif self.vspeed > 0:
            self.image = pygame.transform.rotate(self.image, 180)
    
    def update(self):
        self.rect.x += self.hspeed
        self.rect.y += self.vspeed
        if self.collide():
            self.kill()

    def collide(self):
        if self.rect.x < 0 - self.rect.height or self.rect.x > WINDOW_WIDTH:
            return True
        elif self.rect.y < 0 - self.rect.height or self.rect.y > WINDOW_HEIGHT:
            return True
    