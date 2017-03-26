# network-programming-lab
(under development)
The main aim is to create a real time network simulator which shows the communication

between two nodes using two separate computers over a computer network.

It shows the behaviour of a computer network in real time. The application offers a

Graphical User Interface(GUI) which displays the transfer of packets between the two

nodes. The properties of the packets that are transferred can also be manipulated. Some

properties are :

1. Type of Protocol used(TCP/UDP)

2. Colour

3. Bandwidth Delay

4. Packet Size

and similar properties.

The GUI will contain subtle animation which will make it easier to understand the

simulation of the network. The GUI is easy to use and no code will be needed to be

written. The animation and GUI are written in Python using the following libraries:

• tkinter - To develop the GUI of the application

• Pygame - For the animation

• Socket – For socket programming

The user has to input the packet properties using the GUI. Socket is used to establish the

connection between the two nodes(computers). The packets are transferred in real time

over the network and Pygame is used to display the animated transfer.