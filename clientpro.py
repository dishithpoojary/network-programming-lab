
import socket               

s = socket.socket()         
host = socket.gethostname() 
port = 12345                
s.connect((host, port))

protocol = 'tcp'
color = (255,0,255)
##color = s.receive(1024)
##bandwidth = int(s.receive(1024))
##sim = int(s.receive(1024))


##print inp

##arr = list(map(str,inp.strip().split(" ")))

##protocol = arr[0]

    
num,speed = 50,5
test = 1
once = False
ack_sending = False
packet_count = 0
packet_transfer = False


import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (800,100)

import pygame
pygame.init()
white = (255,255,255)
display_width = 500
display_height  = 500
x,y = -150,250
cr = 10
counter = 0
end_packet_transfer = False
clock = pygame.time.Clock()

##pygame.time.delay(500/(speed*30)*1000)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('client')
gameDisplay.fill(white)
pygame.display.update()
##import time
##time.sleep(500/(speed*30))

gameOver = True

while gameOver == True:

    gameDisplay.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = False

    if test == 1:
        if once == False:
            inp = s.recv(1024)
            once = True

        x+=speed 
        if x>=350:
            end_packet_transfer = True

        if not end_packet_transfer:
            pygame.draw.rect(gameDisplay,color,[x,y,5,5])

        if end_packet_transfer:
            test  = 0
            
        if end_packet_transfer:
            if inp == 'syn':
                print "Tcp connection establishment request detected...."
                print "sending an SYN ack..."
                ack_sending = True
                once  = False
                end_packet_transfer = False
                 

    if ack_sending == True:
        if once == False:
            x = 250
            once = True

        x-=speed 
        if x<=-10:
            end_packet_transfer = True

        if not end_packet_transfer:
            pygame.draw.rect(gameDisplay,color,[x,y,5,5])

        if end_packet_transfer:
            s.send("SYN ack")
            ack_sending = False
            once = False
            packet_transfer = True

    if packet_transfer == True:      
        if counter>900/speed:
            if once == False:
                end_packet_transfer = False
                x = -(num*20)
                once = True
            
            if x+num*20>=350:
                num-=1
                
            if not end_packet_transfer:
                for _ in range(0,num):
                    pygame.draw.rect(gameDisplay,color,[x+_*20,y,5,5])
                    
            x+=speed 
            if x>=350:
                end_packet_transfer = True
                
        counter+=1
        
    pygame.draw.circle(gameDisplay,(255,200,150),(350,250),cr,0)
    cr+=1
    if cr >= 30:
        cr=10
            
   
    clock.tick(30)
    pygame.display.update()

