import socket
import threading

SERVER_IP = "localhost"
CONNECTION_PORT = 9090

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP,CONNECTION_PORT))

nickname_input = input("Enter your nickname: ")


def receive_message():
    while True:
        received_message = client.recv(1024)
        decoded_message = received_message.decode("utf-8")
        
        if (decoded_message == "NICK" ):
            client.send(nickname_input.encode("utf-8"))
        else:
            print(decoded_message)
        
def getInput():
    while True:
        message_input = input("Enter Message: ")
        client.send(message_input.encode("utf-8"))

receive_message_thread = threading.Thread(target=receive_message)
receive_message_thread.start()

getInput_thread = threading.Thread(target=getInput)
getInput_thread.start()
