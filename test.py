import pygame
from pyp2p.net import *
import time


alice = Net(passive_bind="192.168.0.45", passive_port=44444, interface="eth0:2", node_type="passive", debug=1)
alice.start()
alice.bootstrap()
alice.advertise()

#Event loop.
while 1:
    for con in alice:
        for reply in con:
            print(reply)

    time.sleep(1)

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

display_width = 800
display_height  = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither')

gameOver = True

while gameOver == True:
    gameDisplay.fill(white)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = False
      
pygame.quit()
quit()
