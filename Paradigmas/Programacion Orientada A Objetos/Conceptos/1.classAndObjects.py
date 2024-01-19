
# New class

class CellPhone:
    
    # Class attributes, constructor method    
    def __init__(self, brand, model, camera):
        self.brand = brand
        self.model = model
        self.camera = camera
    
    # Class method
    def call(self):
        print("Calling...")
    
    def message(self):
        print("Sending message...")
    
    def camera(self):
        print("Taking photo...")
    
    def video(self):
        print("Recording video...")
    
    def music(self):
        print("Playing music...")
        
    def radio(self):
        print("Playing radio...")
    
    def internet(self):
        print("Browsing internet...")
        
    def games(self):
        print("Playing games...")

# Class instance
        
CellPhone1 = CellPhone("Tecno", "Spark 10 pro", "50MP")


# print(CellPhone1.brand)
# print(CellPhone1.model)
# print(CellPhone1.camera)

# CellPhone1.call()
CellPhone1.message()