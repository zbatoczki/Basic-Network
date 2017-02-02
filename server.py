#!/usr/bin/python3

#Write a server program
#(optional) use a telnet connection to communicate with the server
#use PuTTY for Windows

import socket
from random import randint

def get_input() :
    s = (clientSocket.recv(1024)).decode('ascii')
    s = s.strip('\n')
    s = s.lower() #set to lowercase
    return s

def play():
    cpuInput = moves[randint(1,3)]
    playerInput = get_input()
    results = ''
    if(playerInput == cpuInput) :
        results = 'It\'s a draw!'
    elif(playerInput == 'rock'):
        if(cpuInput == 'paper'):
            results = 'You lose!'
        else:
            results = 'You win!'
            score += 1
    elif(playerInput == 'paper'):
        if(cpuInput == 'scissors'):
            results = 'You lose!'
        else:
            results = 'You win!'
            score += 1
    elif(playerInput == 'scissors'):
        if(cpuInput == 'rock'):
            results = 'You lose!'
        else:
            results = 'You win!'
            score += 1

moves = {1:'rock', 2:'paper', 3:'scissors'}
score = 0

#create socket object
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#get local host
host = socket.gethostname()
print(host)
port = 5000

#bind port
serverSocket.bind((host, port))

#set number of connections to accept
serverSocket.listen(1) #only one connection will be accepted

#establish connection
print('Waiting for client...')
clientSocket, addr = serverSocket.accept()
print("Got a connection from %s" % str(addr))
#provide main menu
#recieves main menu action 'PLAY' 'SCORE' or 'QUIT'
msg = 'WELCOME!' + "\r\n" + '>PLAY >SCORE >QUIT' + "\r\n"
clientSocket.send(msg.encode('ascii'))


while True:
    userInput = get_input()
    if(userInput == 'quit') :
        break
    elif(userInput == 'score'):
        msg = 'YOUR SCORE: %d\r\n' % score
        clientSocket.send(msg.encode('ascii'))
    elif(userInput == 'play') :
        play()
    else :
        msg = 'Input error. Please try again\r\n'
        clientSocket.send(msg.encode('ascii'))
    
goodbye = 'Thanks for playing!'
clientSocket.send(goodbye.encode('ascii'))
clientSocket.close()

