class Calculator:
    def __init__(self,num):
        self.number = num

    def square(self):
        print(f"The value of {self.number} sqaure is {self.number **2}")

    def squareroot(self):
        print(f"The value of {self.number} squareroot is {self.number **0.5} ")

    def cube(self):
        print(f"The value of {self.number} cube is {self.numb **3}")

    @staticmethod
    def greet(self):
        print("This is the best calculator in the world")

a=Calculator(9)
a.square()
a.squareroot()
a.cube()
