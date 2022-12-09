import socket

SERVER_IP = "localhost" # "127.0.0.1"

CONNECTION_PORT = 9090

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, CONNECTION_PORT))

print("Client is Up !!!")

message = input("Type a message: ")
client.send(message.encode("utf-8"))
print(client.recv(1024).decode("utf-8"))
