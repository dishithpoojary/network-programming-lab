
#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
inp = s.recv(1024)

print inp

arr = list(map(int,inp.strip().split(" ")))
num,speed = arr

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (800,100)

import pygame
pygame.init()
white = (255,255,255)
display_width = 500
display_height  = 500
x,y = -100,200
counter = 0
clock = pygame.time.Clock()

##pygame.time.delay(500/(speed*30)*1000)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('client')
gameDisplay.fill(white)

##import time
##time.sleep(500/(speed*30))

gameOver = True
while gameOver == True:
    gameDisplay.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = False

    if counter>500/speed:      
        x+=speed
        for _ in range(num):
            pygame.draw.rect(gameDisplay,(0,255,0),[x+_*20,y,10,10])
            
    counter+=1
    clock.tick(30)
    pygame.display.update()

