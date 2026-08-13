class Vehicle:
    def __init__(self, brand, speed, fuel):
        self.brand=brand
        self.speed=speed
        self.fuel=fuel 
        
    def display(self):
        print("Brand:",self.brand)
        print("Speed:",self.speed)
        print("Fuel:",self.fuel)
        
class Car(Vehicle):
    def __init__(self, brand, speed, fuel, doors):
        super().__init__(brand, speed, fuel)
        self.doors=doors 
        
    def display(self):
        super().display()
        print("Doors:",self.doors)
        
class Bike(Vehicle):
    def __init__(self, brand, speed, fuel, gear):
        super().__init__(brand, speed, fuel)
        self.gear=gear 
        
    def display(self):
        super().display()
        print("gear:",self.gear)
        
class Truck(Vehicle):
    def __init__(self, brand, speed, fuel, cap):
        super().__init__(brand, speed, fuel)
        self.cap=cap
        
    def display(self):
        super().display()
        print("capacity:",self.cap)
        
car = Car("Toyota", 180, "Petrol", 4)
bike = Bike("Yamaha", 120, "Petrol", True)
truck = Truck("Volvo", 100, "Diesel", 20)

print("Car Details")
car.display()
