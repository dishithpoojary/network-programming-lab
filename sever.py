

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
    protocol = raw_input("Enter the type of protocol: ")
    
##    packetcolor = raw_input("Enter the packet color: ")
##    bandwidth  = raw_input("Enter the bandwidth: ")
##    sim_time  = raw_input("Enter simulation time: ")
##    number_of_packet = raw_input("Enter the number of packets: ")
##
##    inp = typeofprotocol + " " + packetcolor + " " + bandwidth + " " + sim_time + " " + number_of_packet

    inp = protocol
    c.send(str(inp))

    if protocol == "tcp":
        print "Syn packet sent for connection establishment...."
        print "Wating for acknowledgement..."
        print c.recv(1024)+" received"
        print "Establishing tcp connection..."
        
    

##    print c.recv(1024)
    enter = False
    c.close()                # Close the connection

arr = list(map(str,inp.strip().split(" ")))
num,speed = 10,2

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,100)

import pygame
pygame.init()
white = (255,255,255)
display_width = 500
display_height  = 500
x,y = 150,250
cr = 10
end_packet_trasfer = False
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
    if x>=500:
        end_packet_trasfer = True
        
    if not end_packet_trasfer:
        for _ in range(num):
            pygame.draw.rect(gameDisplay,(0,255,0),[x+_*20,y,5,5])

    pygame.draw.circle(gameDisplay,(255,200,150),(150,250),cr,0)

    cr+=1
    if cr >= 30:
        cr=10

    clock.tick(30)
    pygame.display.update()      



