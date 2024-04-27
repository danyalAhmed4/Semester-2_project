import socket
import pickle
import threading

from Firestation import firestation

station = firestation()
    
HEADER = 2048
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
        data = b''
        while len(data) < HEADER:
            chunk = conn.recv(HEADER - len(data))
            if not chunk:
                break
            data += chunk
        if not data:
            break
        received_object = pickle.loads(data)
        station.file_report(received_object)
    
def server_start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[NO OF CONNECTIONS]:{threading.active_count()-1}')


server_start()