import time

class report:
    def __init__(self, Name, Cnic, Location, type_E) -> None:
        self.Name = Name
        self.Cnic = Cnic
        self.location = Location
        self.timestamp = time.asctime()
        self.type = type_E
        

obj = report("Umer", 1223, "Karachi", "Fire")

print(obj.timestamp)        