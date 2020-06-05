# Write classes for the following class hierarchy:


#
## Base Class - vehicle
#
class Vehicle:
  pass


# Inherit Vehicle class
class FlightVehicle(Vehicle): 
  pass

# Inherit FlightVehicle class 
class Airplane(FlightVehicle):
  pass

# Inherit FlightVehicle class 
class Starship(FlightVehicle):
  pass

# Inherit Vehicle class
class GroundVehicle(Vehicle):
  pass

# Inherit GroundVehicle class 
class Car(GroundVehicle):
  pass

# Inherit GroundVehicle class
class Motorcycle(GroundVehicle):
  pass

#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
