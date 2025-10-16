class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle is starting.")

    def stop(self):
        print("Vehicle is stopping.")

class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors

    def start(self):
        print("Car is starting.")

    def stop(self):
        print("Car is stopping.")

    
class Motorcycle(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)

    # def start_bike(self):
    #     print("Motorcycle is starting.")

    # def stop_bike(self):
    #     print("Motorcycle is stopping.")

#have to change the name of method to same as parent class in order for polymorphism to be in play.

    def start(self):
        print("Motorcycle is starting.")

    def stop(self):
        print("Motorcycle is stopping.")

class Plane(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors

    def start(self):
        print("Plane is starting.")

    def stop(self):
        print("Plane is stopping.")
        
#Create list of vehicles to inspect
vehicles: list[Vehicle] = [
    Car("Ford", "Fusion", 2008, 5),
    Motorcycle("Honda", "Scoopy", 2018),
    Plane("Boeing", "747", 2015, 16)
]

for vehicle in vehicles:
    print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
    vehicle.start()
    vehicle.stop()
    
#no longer need to do if instance, else raise code, as we had "list[Vehicle] =" earlier in our code that guarantees that the object is of Vehicle class type.

    # if isinstance(vehicle, Vehicle):
    #     print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
    #     vehicle.start()
    #     vehicle.stop()
    # else:
    #     raise Exception("Object is not a valid vehicle")


#LOop through list of vehicles and inspect them
# for vehicle in vehicles:
#     if isinstance(vehicle, Car):
#         print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
#         vehicle.start()
#         vehicle.stop()
#     elif isinstance(vehicle, Motorcycle):
#         print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
#         vehicle.start_bike()
#         vehicle.stop_bike()
#     else:
#         raise Exception("Object is not a valid vehicle")
