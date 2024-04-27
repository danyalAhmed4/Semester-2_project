import socket
import pickle

from person import Person
from report import Report
import tkinter as tk

HEADER = 2048
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 12345
ADDR = (SERVER, PORT)
class Caller(Person):
    def __init__(self, name, cnic, location, contact_info, type_e):
        super().__init__(name)
        self.cnic = cnic
        self.location = location
        self.contact_info = contact_info
        self.type = type_e

    def caller_report(self):
        self.caller_report = Report(self.name, self.cnic, self.location, self.contact_info, self.type)
        return self.caller_report
        

#Function to handle the submission of the form
def submit_form():
    #Getting User Inputs
    name = name_entry.get()
    cnic = cnic_entry.get()
    location = location_entry.get()
    contact_info = contact_info_entry.get()
    type_e = type_e_var.get()

    caller = Caller(name, cnic, location, contact_info, type_e)

    report = caller.caller_report()

    #Serialize the Report object using pickle.
    #This means that the object is converted into a byte stream that can be sent by TCP/IP.
    #The benefits of this are that it makes objects persistant, and it allows for communication via sockets.
    #cons are that it is not secure, and that there might be compatibility issues with older versions of python.
    data = pickle.dumps(report)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect(ADDR)

    client_socket.sendall(data)

    client_socket.close()

    #closing the window
    window.destroy()

#creating a Tkinter window
window = tk.Tk()

#creating a frame to group related widgets together
frame = tk.Frame(window, bg='#DEDEDE', width=300, height=200)
frame.pack(padx=10, pady=10)

#creating a label and entry for the different inputs
name_label = tk.Label(frame, text="Name:", bg='#DEDEDE')
name_label.pack(side="top")
name_entry = tk.Entry(frame)
name_entry.pack(side="top")

cnic_label = tk.Label(frame, text="CNIC:", bg='#DEDEDE')
cnic_label.pack(side="top")
cnic_entry = tk.Entry(frame)
cnic_entry.pack(side="top")

location_label = tk.Label(frame, text="Location:", bg='#DEDEDE')
location_label.pack(side="top")
location_entry = tk.Entry(frame)
location_entry.pack(side="top")

contact_info_label = tk.Label(frame, text="Contact Info:", bg='#DEDEDE')
contact_info_label.pack(side="top")
contact_info_entry = tk.Entry(frame)
contact_info_entry.pack(side="top")

#dropdown box for various emergencies
type_e_var = tk.StringVar(window)
type_e_var.set("Select Emergency Type")
type_e_options = ["Fire", "Injury", "Crime"]
type_e_menu = tk.OptionMenu(frame, type_e_var, *type_e_options)
type_e_menu.pack(side="top", pady=20)

#submit button that calls the submit_form function when clicked
submit_button = tk.Button(window, text="Submit", font=("Arial", 12), command=submit_form)
submit_button.pack(pady=1)

#get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

#calculate the window width and height
window_width = 295
window_height = 300

#calculate the x and y coordinates to center the window on the screen
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

#setting the window geometry to be centered on the screen, and the background color of the window
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.config(bg="#DEDEDE")

#Tkinter event loop
window.mainloop()