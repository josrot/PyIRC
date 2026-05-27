import socketserver
from dotenv import load_dotenv
import os

class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print(f"{self.client_address[0]} wrote: {self.data}")
        self.request.sendall(self.data)

if __name__ == "__main__":
    load_dotenv()
    host = os.environ['HOST']
    port = int(os.environ['PORT'])
    with socketserver.TCPServer((host, port), TCPHandler) as server:
        print(f"Server listening on {host}:{port}")
        server.serve_forever()