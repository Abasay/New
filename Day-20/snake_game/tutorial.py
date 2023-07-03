class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("INhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()
        

    def breathe(self):
        super().breathe()
        print("doing this in the water")

    def swim(self):
        print("moving in the water.")