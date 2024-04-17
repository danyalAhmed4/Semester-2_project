import time

class Report:
    def __init__(self, Name, Cnic, Location, contact_info, type_E) -> None:
        self.Name = Name
        self.Cnic = Cnic
        self.location = Location
        self.contact = contact_info
        self.type = type_E
        self.timestamp = time.asctime()
        
def main():
    ...
    
if __name__ == "__main__":
    main()        