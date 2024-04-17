import time

class report:
    def __init__(self, Name, Cnic, Location, type_E) -> None:
        self.Name = Name
        self.Cnic = Cnic
        self.location = Location
        self.timestamp = time.localtime()
        (self.year, self.month, self.date) = self.timestamp[0], self.timestamp[1], self.timestamp[3]
        self.type = type_E
        

obj = report("Umer", 1223, "Karachi", "Fire")

print(obj.year)        