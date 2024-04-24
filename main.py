import socket
import pickle
import threading

from Firestation import firestation

station = firestation()
    
HEADER = 1024
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 12345
ADDR = (SERVER, PORT)
    
#Server Socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Binding our socket
server.bind(ADDR)


def handle_client(conn, addr):
    
    connected = True
    while connected:
        data = conn.recv(HEADER)
        class_definition, received_data = pickle.loads(data)
        received_object = class_definition(*received_data)
        station.file_report(received_object)
    
def server_start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.active_count()}')


server_start()