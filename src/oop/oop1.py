# Write classes for the following class hierarchy:
#
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

class Vehicle():
    # Main base
    pass


class FlightVehicle(Vehicle):
    # Vehicle is the base
    pass


class Airplane(FlightVehicle):
    # Flight Vehicle is the base
    pass


class Starship(FlightVehicle):
    # Flight Vehicle is the base
    pass


class GroundVehicle(Vehicle):
    # Vehicle is the base
    pass


class Car(GroundVehicle):
    # Ground Vehicle is the base
    pass


class Motorcycle(GroundVehicle):
    # Ground Vehicle is the base
    pass
