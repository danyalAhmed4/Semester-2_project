import socket
import pickle
import threading

import Firestation

def handle_client(conn, addr):
    ...
    
def server_start(server):
    server.listen()
    while True:
        client_socket, client_address = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.activeCount() - 1}')

def main():
    
    HEADER = 1024
    SERVER = socket.gethostbyname(socket.gethostname())
    PORT = 12345
    ADDR = (SERVER, PORT)
    
    #Server Socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Binding our socket
    server.bind(ADDR)
    
    server_start(server)

if __name__ == "__main__":
    main()
    
