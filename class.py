import os

class Car:   #en klass har alltid stor bokstav
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color =color

    def view_cars(self):
        return f"{self.make} - {self.model} ({self.color})"

os.system("cls")


cars = [] #lista



def display_cars():
    os.system("cls")
    print("/nLIST OF CARS")
    for car in cars:
        print(car.show())

os.system("cls")
# List to store all car instances
cars = []

while True:
    print("\nADD A CAR")
    make = input("Enter make: ")
    model = input("Enter model: ")
    color = input("Enter color (Type nothing to quit): ")

    if color == "":
        break

    # Create a new Car instance and add it to the 1list
    cars.append(Car(make, model, color))

    #View all cars added
    display_cars()


   

