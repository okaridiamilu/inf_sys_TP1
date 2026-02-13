class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag


class Myclass:
    i = 19
    def display_i(self):
        print(self.i)


c = Myclass()
print(c.i)
print(c.display_i())

if __name__ == "__main__":
    cl = Complex(12,9)
