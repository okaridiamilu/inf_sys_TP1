class Dog:
    kind = "Canine"
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_strick(self, trick):
        self.tricks.append(trick)

d = Dog("Fido")
e = Dog("Buddy")
print(d.kind)
print(e.kind)
print(d.name)  
print(e.name)