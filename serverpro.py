
import socket               

s = socket.socket()         
host = socket.gethostname() 
port = 12345                
s.bind((host, port))        
s.listen(5)                 
c, addr = s.accept()     

print 'Got connection from', addr
protocol = 'tcp'
color = (255,0,255)
##color = input("Enter the packet color:")
##color = "("+color+")"
##c.send(str(color))
##
##bandwidth = int(input("Enter the bandhwidth:"))
##c.send(str(bandwidth))
##
##sim = int(input("Enter the simulation time:"))
##c.send(str(sim))



##    print c.recv(1024)


##arr = list(map(str,inp.strip().split(" ")))
num,speed = 50,5

once = False 
test = 1
ack_receiving = False
packet_count = 0
packet_transfer = False

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,100)

import pygame

pygame.init()
white = (255,255,255)
display_width = 500
display_height  = 500
x,y = 150,250
cr = 10
end_packet_transfer = False
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('server')

gameOver = True
while gameOver == True:
   
    gameDisplay.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = False

            
    if test == 1:
        if once == False:
            print "Syn packet sent for connection establishment...."
            print "Wating for acknowledgement..."
            once = True

        x+=speed 
        if x>=510:
            end_packet_transfer = True
            
        if not end_packet_transfer:
            pygame.draw.rect(gameDisplay,color,[x,y,5,5])

        if end_packet_transfer == True:
            c.send("syn")
            ack = c.recv(1024)
            ack_receiving = True
            once = False
            end_packet_transfer = False     
            test  = 0

    if ack_receiving == True:
        if once == False:
            x = 510
            once = True

        x-=speed 
        if x<=150:
            end_packet_transfer =True

        if not end_packet_transfer:
            pygame.draw.rect(gameDisplay,color,[x,y,5,5])

        if end_packet_transfer==True:
            print 'Syn ack received'
            print "Establishing tcp connection..."
            ack_receiving = False
            packet_transfer = True
            once = False
            
    
    if packet_transfer == True:
        if once == False:
            end_packet_transfer = False
            x = -num*20
            once = True
            
        if packet_count < num:
            packet_count+=1

        if not end_packet_transfer:
            for _ in range(0,num):
                pygame.draw.rect(gameDisplay,color,[x+_*20,y,5,5])
                
        x+=speed
        if x>=510:
            end_packet_transfer = True
            
    pygame.draw.rect(gameDisplay,(255,255,255),[0,y,150,10])
    pygame.draw.circle(gameDisplay,(255,200,150),(150,250),cr,0)
    cr+=1
    if cr >= 30:
        cr=10

    clock.tick(30)
    pygame.display.update()      

c.close()

