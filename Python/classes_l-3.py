class Vehicle:
    """docstring"""
    
    def __init__(self, color, doors, tires, vtype, weight):
        """Constructor"""
        self.color = color
        self.doors = doors
        self.tires = tires
        self.vtype = vtype
        self.weight = weight
    
    def brake(self):
        """
        Stop the car
        """
        return "%s braking" % self.vtype
    
    def drive(self):
        """
        Drive the car
        """
        return "I'm driving a %s %s весом %s тонн!" % (self.color, self.vtype, self.weight)
 
 
class Car(Vehicle):
    """
    The Car class
    """
 
    #----------------------------------------------------------------------
    def brake(self):
        """
        Override brake method
        """
        return "The car class is breaking slowly!"
 
 
if __name__ == "__main__":
    car = Car("yellow", 2, 4, "car", 3.2)
    car.brake()
    print(car.brake())
    print(car.drive())
    'The car class is breaking slowly!'
    "I'm driving a yellow car!"




