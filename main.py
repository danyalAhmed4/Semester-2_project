import socket
import pickle
import threading

from Firestation import station

station = station()
    
HEADER = 2048
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 12345
ADDR = (SERVER, PORT)
    
#Server Socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Binding our socket
server.bind(ADDR)

#The handle_client function receives data in a loop until the complete HEADER bytes have been received. 
#If the client closes the connection before sending the complete data, or if the data sent is not the same amount as specified in header.
#A check would be done on each iteration to see if any data has arrived and if there is none.
#The loop will exit and the function will return.
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
        
#Using the thread module to allow for multi threading of connections. 
#This means that for multiple clients the handle_client function will be called on a seperate thread.
#This allows for multiple clients to send their files at once.
#Without waiting for the previous connection to end.
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[NO OF CONNECTIONS]:{threading.active_count()-1}')


server_start()