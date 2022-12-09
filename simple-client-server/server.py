import socket

HOST = "localhost" # 127.0.0.1
PORT = 9090 # Connection Socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))

server.listen(5)

print("Server Is Up !!!")

while True:
    communication_socket, address = server.accept()
    print(f"Connected to {address}")
    message = communication_socket.recv(1024).decode("utf-8") # every message is encoded
    print(f"Message is: {message}")
    
    communication_socket.send("The message was received".encode("utf-8"))
    
    
