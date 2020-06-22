import pygame
import random
import tkinter as tk
import math
from tkinter import messagebox

pygame.init()

fps = 30

fpsclock = pygame.time.Clock()

# create the window
screen = pygame.display.set_mode ((500, 500))

# Title and icon
pygame.display.set_caption("snake")

# snake and controls
screenwidth = 500
screenheight = 500
width = 20
height = 20
black = (0, 0, 0)
snake_y = 250
snake_x = 250
food_y = int(random.uniform(0, 500))
food_x = int(random.uniform(500, 0))


# creates the objects food and snake
# main game Loop for the snake
running = True
while running:
    screen.fill(black)
    key = pygame.key.get_pressed()
    vel = 5
    # movement
    if key[pygame.K_LEFT] and snake_x > vel - 2:
        snake_x -= vel
    if key[pygame.K_RIGHT] and snake_x < screenwidth - vel - width + 2:
        snake_x += vel
    if key[pygame.K_UP] and snake_y > vel - 2:
        snake_y -= vel
    if key[pygame.K_DOWN] and snake_y < screenheight - vel - height + 5:
        snake_y += vel

    pygame.draw.rect(screen,(255,255,255),(snake_x,snake_y, width,height))
    pygame.draw.rect(screen,(255,20,60),(food_x,food_y,width,height))

    # stops the game if you press the x
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # updates the game
    pygame.display.update()
    fpsclock.tick(fps)
