import pygame
import neat
import os
import time
import random

# Setting windows dimensions for the game and loading all the sprites needed
WIN_WIDTH = 600
WIN_HEIGHT = 800

BIRDS_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))), pygame.transform.scale2x(
    pygame.image.load(os.path.join('imgs', 'bird2.png'))), pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png')))]
PIP_IMG = pygame.transform.scale2x(
    pygame.image.load(os.path.join('imgs', 'pipe.png')))
BASE_IMG = pygame.transform.scale2x(
    pygame.image.load(os.path.join('imgs', 'base.png')))
BG_IMG = pygame.transform.scale2x(
    pygame.image.load(os.path.join('imgs', 'bg.png')))


# Creating the key elements of the game: bird, pipe and base

class Bird:
    IMGS = BIRDS_IMGS
    MAX_ROTATION = 25
    ROTATION_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y
    
    def move(self):
        