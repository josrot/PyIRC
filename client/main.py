import socket
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    host = os.environ['HOST']
    port = int(os.environ['PORT'])
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((host, port))
        client.send("Hello, world.".encode())
        response = client.recv(1024)
        print(response.decode())

if __name__ == '__main__':
    main()