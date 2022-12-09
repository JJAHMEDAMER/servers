import socket

SERVER_IP = "localhost"
CONNECTION_PORT = 9090

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP,CONNECTION_PORT))

message = "hi"
encoded_message = message.encode("utf-8")
client.send(encoded_message)

response = client.recv(1024)
decoded_response = response.decode("utf-8")
print(decoded_response)