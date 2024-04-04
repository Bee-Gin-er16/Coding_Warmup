#OP1
class Vehicle: 
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle(240, 18)
print(modelX.max_speed, modelX.mileage)

#OP2
class Vehicle:
    pass

#OP3
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

b = Bus('School Volvo',180,12)
print(f'Vehicle Name: {b.name} Speed: {b.max_speed} Mileage {b.mileage}')

#OP4
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    #Default capacity is 50 if class argument for capacity is not given
    def __init__(self, name, max_speed, mileage, capacity=50):
        super().__init__(name, max_speed, mileage)
        self.capacity = capacity

    def seating_capacity(self):
        return super().seating_capacity(self.capacity) + ' (method for Bus)'
    
b1 = Bus('Porsche', 200, 18, 200)
b2 = Bus('volvo', 250, 20)
print(b1.seating_capacity())
print(b2.seating_capacity())

#OP5
class Vehicle:
    color = 'white'
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        # self.color = 'white' alternative default class props

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

b1 = Bus('Bussy', 200, 30)
c1 = Car('Cussy', 500,  40)
print(f'Bus color: {b1.color} \nCar color: {c1.color}')

#OP6
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    
    def fare(self):
        return super().fare() + (0.1 * super().fare())

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())

#OP7
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
print(type(School_bus))

#OP8
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
print(isinstance(School_bus, Vehicle))

