import socket
import threading
import sys
import random

pnum = 0

def connectionHandle(connection, addr):
    global pnum
    horc = 0
    print("New connection created!")
    horc = connection.recv(1024).decode()
    
    pnum = pnum+1
    localpnum = pnum
    pjoin = "Hello Player " + str(localpnum)
    connection.send(pjoin.encode())

    accepted = False

    while accepted == False:
        rps = connection.recv(1024).decode().lower()
        if(rps == "rock" or rps == "paper" or rps == "scissors"):
            connection.send("200 OK".encode())
            accepted = True
        else:
            connection.send("404 ERROR. Please try again".encode())

    input.append(rps)

    if(int(horc) == 1):
        choice = random.randrange(1,4)
        if(choice == 1):
            print("CPU choose rock")
            input.append("rock")
        if(choice == 2):
            print("CPU choose paper")
            input.append("paper")
        if(choice == 3):
            print("CPU choose scissors")
            input.append("scissors")


    print("Player " + str(localpnum) + " selected " + str(input[localpnum-1]))

    while True:
        if(len(input) == 2):
            if(input[0] == input[1]):
                connection.send("You tied".encode())
                break
            elif(input[0] == "rock" and input[1] == "scissors"):
                connection.send("Player 1 wins".encode())
                break
            elif(input[1] == "rock" and input[0] == "scissors"):
                connection.send("Player 2 wins".encode())
                break
            elif(input[0] == "paper" and input[1] == "rock"):
                connection.send("Player 1 wins".encode())
                break
            elif(input[1] == "paper" and input[0] == "rock"):
                connection.send("Player 2 wins".encode())
                break
            elif(input[0] == "scissors" and input[1] == "paper"):
                connection.send("Player 1 wins".encode())
                break
            elif(input[1] == "scissors" and input[0] == "paper"):
                connection.send("Player 2 wins".encode())
                break

    

print("Server is starting...")
port = int(sys.argv[1])
host = socket.gethostname()
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((host, port))

input = []

serverSocket.listen(1)
count = 0
while True:
    connection, addr = serverSocket.accept()

    thread = threading.Thread(target=connectionHandle, args=(connection,addr))
    thread.start()
    count = count +1
    if(count == 2):
        sys.exit()

