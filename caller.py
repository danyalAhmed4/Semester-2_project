from person import Person

from report import Report

import socket
import pickle

class caller(Person):
    def __init__(self, name, age, cnic, location, contact_info, type):
        super().__init__(name, age)
        self.cnic = cnic
        self.location = location
        self.contact_info = contact_info
        self.type = type
        
    def caller_report(self):
        self.caller_report = Report(self.name, self.cnic, self.location, self.contact_info, self.type)
        
        
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 12345
ADDR = (SERVER, PORT)

#client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connection
client_socket.connect(ADDR)

report_example = Report('umer', '21234', 'karachi', '03132271030', 'fire')

data = pickle.dumps(report_example)

client_socket.sendall(data)

client_socket.close()