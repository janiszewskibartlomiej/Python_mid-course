class DuckBehaviour:
    def fly(self):
        print("Ja lecę")

    def say(self):
        print("Kwa Kwa")

    def go(self):
        print("Chodzę")

class Duck(DuckBehaviour):
    def __init__(self,age,breed):
        self.age = age
        self.breed = breed

class Toy:
    def __init__(self,color, material):
        self.color = color
        self.material = material

class DuckToy(Toy, DuckBehaviour):
    pass

#DRY = Do not Reply Yourself