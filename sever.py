

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
enter = True

while enter:
    c, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    inp = raw_input()
    c.send(str(inp))
##    print c.recv(1024)
    enter = False
    c.close()                # Close the connection

arr = list(map(int,inp.strip().split(" ")))
num,speed = arr

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,100)

import pygame
pygame.init()
white = (255,255,255)
display_width = 500
display_height  = 500
x,y = 100,200
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('server')

gameOver = True
while gameOver == True:
    gameDisplay.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = False
    x+=speed
    for _ in range(num):
        pygame.draw.rect(gameDisplay,(0,255,0),[x+_*20,y,10,10])


    clock.tick(30)
    pygame.display.update()      



