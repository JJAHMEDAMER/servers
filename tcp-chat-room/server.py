import socket

SERVER_IP = "localhost" # "127.0.0.1"
CONNECTION_PORT = 9090 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_IP,CONNECTION_PORT))

server.listen(5)

print("Server Is Up !!!")

while True:
    connection_port, address = server.accept() # Accepts every connection
    print(f"Connected to {address}")
    
    received_message = connection_port.recv(1024) # encoded
    decoded_message = received_message.decode("utf-8")
    print(f"The received message is: {decoded_message}")
    
    connection_port.send("The message is received".encode("utf-8"))
    
