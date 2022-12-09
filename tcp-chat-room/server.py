import socket
import threading

SERVER_IP = "localhost" # "127.0.0.1"
CONNECTION_PORT = 9090     

def received(communication_port):
    while True:
        received_message = communication_port.recv(1024) # encoded
        decoded_message = received_message.decode("utf-8")        

        # Print message in the server
        print(f"The received message is: {decoded_message}")
        
        broadCast(decoded_message)

    
def broadCast(message):
    encoded_message = message.encode("utf-8")
    for client in clients_port_list:
        client.send(encoded_message)
        
def main():
    while True:
        communication_port, address = server.accept() # Accepts every connection
        
        clients_port_list.append(communication_port) # add user to client list
        print(f"Connected to {address}")
        
        communication_port.send("NICK".encode("utf-8"))
        nickname = communication_port.recv(1024).decode("utf-8")
        clients_nickname_list.append(nickname)
        print(f"{address} nickname is: {nickname}")
        
        broadCast(f"{nickname} joined the server")
        communication_port.send("Connected to the server".encode("utf-8"))
        
        received_thread = threading.Thread(target=received, args=(communication_port,))
        received_thread.start()
        

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_IP,CONNECTION_PORT))
server.listen()

clients_port_list = []
clients_nickname_list = []

print("Server Is Up !!!")
main()