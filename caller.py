from person import Person

import socket

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 12345
ADDR = (SERVER, PORT)

#client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connection
client_socket.connect(ADDR)

class caller(Person):
    def __init__(self, name, age, cnic, location, contact_info):
        super().__init__(name, age)
        self.cnic = cnic
        self.location = location
        self.contact_info = contact_info
        
