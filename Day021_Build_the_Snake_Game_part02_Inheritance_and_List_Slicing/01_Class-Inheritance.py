# Topic: Class Inheritance
# The process of inheriting behavior and appearance from an existing class is known as "class Inheritance"


# scenario01
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale.")

class Fish:

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.swim()

# scenario02
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)

# scenario03
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")


nemo = Fish()
nemo.breathe()