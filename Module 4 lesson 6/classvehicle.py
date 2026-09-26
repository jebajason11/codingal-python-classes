class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle(120, 36)
print("Model Max Speed:", modelX.max_speed)
print("Model Mileage:", modelX.mileage)

modelY = Vehicle(200, 6)
print("Model Max Speed:", modelY.max_speed)
print("Model Mileage:", modelY.mileage)
        