class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class FireMen(Person):
    def __init__(self, name, age, experience, id):
        super().__init__(name, age)
        self.experience = experience
        self.id = id
        self.is_deployed = False
    
    def deployment(self):
        if self.is_deployed is False:
            self.is_deployed = True
            return True
        
        else:
            return self.is_deployed
    

class policeMan(Person):
    def __init__(self, name, age, experience, id):
        super().__init__(name, age)
        self.experience = experience
        self.id = id
        
    def emergencyCall(self):
        print("Police Have been deployed")
        
class Medic(Person):
    ...

def main():
    ...
    
if __name__ == "__main__":
    main()
    

