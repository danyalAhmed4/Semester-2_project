import socket

def handle_client(server):
    server.listen()
    while True:
        client_socket, client_address = server.accept()
        print(client_socket)
        print(client_address)
    
def server_start():
    ...

def main():
    
    HEADER = 128
    SERVER = socket.gethostbyname(socket.gethostname())
    PORT = 12345
    ADDR = (SERVER, PORT)
    
    #Server Socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Binding our socket
    server.bind(ADDR)
    
    handle_client(server)

if __name__ == "__main__":
    main()
    
