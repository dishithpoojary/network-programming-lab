

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
##host="45.250.46.222"
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(50)                 # Now wait for client connection.
enter = True

while enter:
    c, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    inp = raw_input()
    c.send(str(inp))
##    print c.recv(1024)
    enter = False
    c.close()                # Close the connection



