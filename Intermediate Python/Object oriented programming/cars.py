
class Car:
    runs = True

    def __init__(self):
        print("new car!")

    def start(self, name):
        self.name = name
        if self.runs:
            print(f"{self.name} car is started")
        else:
            print(f"{self.name} car is started")
        

my_subaru = Car()  
my_subaru.start("Subaru")