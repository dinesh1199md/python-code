

class Vehicle:
	def __init__(self, name, tyre):
		self.name = name
		self.tyre = tyre

	# a class method to create a Car object by name.
	@classmethod
	def checkBike(cls, name):
	    if(name=="Bike"):
		    return cls(name,2)

	# a static method to check if the Vehicle is car or not
	# @staticmethod
	# def isCar(name):
	# 	return name == "Car"


vehicle1 = Vehicle.checkBike('Bike')
vehicle2 = Vehicle('Car', 4)
print(vehicle1.tyre)
print(vehicle2.tyre)

# print the result
print(Vehicle.isCar("Car"))