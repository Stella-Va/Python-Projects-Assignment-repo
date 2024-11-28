#Create a program that includes animals or vehicles with the same action (like move()). 
# However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).


class Vehicle:
    def move(self):
        pass  # This is a placeholder method to be overridden by subclasses

# Subclass 1: Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass 2: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Subclass 3: Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# Subclass 4: Bicycle
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚲")

def test_move(vehicle):
    vehicle.move()  # This will call the specific move() method based on the type of vehicle

if __name__ == "__main__":
    car = Car()
    plane = Plane()
    boat = Boat()
    bicycle = Bicycle()

    # Test the move() method for each vehicle type
    print("Testing different vehicles' move() methods:\n")
    
    vehicles = [car, plane, boat, bicycle]
    
    for vehicle in vehicles:
        test_move(vehicle)
