import socket
import sys

port = int(sys.argv[1])
host = socket.gethostname()
horc = sys.argv[2]
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((host,port))
clientSocket.send(horc.encode())
connected = clientSocket.recv(1024).decode()
print(connected)
accepted = False
while accepted == False:
    intake = input("Enter Rock, Paper, or Scissors:")
    clientSocket.send(intake.encode())
    connected = clientSocket.recv(1024).decode()
    if(connected == "404 ERROR. Please try again"):
        print(connected)
        accepted = False
    elif(connected == "200 OK"):
        print(connected)
        accepted = True
print("Waiting for result...")
result = clientSocket.recv(1024).decode()
print(result)
