# Factory Method Design Pattern: 
# This Python program illustrates the Factory Method design pattern for an ice cream vending machine:
# Abstract `IceCream` class defines ice cream types with `serve_ice_cream` method.
# Concrete `VanillaIceCream` and `ChocolateIceCream` implement `IceCream`.
# `IceCreamVendingMachine` declares `create_ice_cream` as an abstract method.
# `SimpleIceCreamVendingMachine` implements `create_ice_cream` to produce ice cream instances.

from abc import ABC, abstractmethod

# Abstract Product
# IceCream is an abstract class
class IceCream(ABC):
    @abstractmethod
    def serve_ice_cream(self):
        pass

# Concrete Products
# Concrete implementation of IceCream
class VanillaIceCream(IceCream):
    def serve_ice_cream(self):
        return "Vanilla Ice Cream"

# Another concrete implementation of IceCream
class ChocolateIceCream(IceCream):
    def serve_ice_cream(self):
        return "Chocolate Ice Cream"

# Creator (Abstract Factory)
class IceCreamVendingMachine(ABC):
    @abstractmethod
    def create_ice_cream(self):
        pass

# Concrete Creator
class SimpleIceCreamVendingMachine(IceCreamVendingMachine):
    def create_ice_cream(self, flavor):
        if flavor.lower() == "vanilla":
            return VanillaIceCream()
        elif flavor.lower() == "chocolate":
            return ChocolateIceCream()
        else:
            raise ValueError("Invalid ice cream flavor")

# Usage
vending_machine = SimpleIceCreamVendingMachine()
vanilla_ice_cream = vending_machine.create_ice_cream("Vanilla")
chocolate_ice_cream = vending_machine.create_ice_cream("Chocolate")

print(vanilla_ice_cream.serve_ice_cream())  # Output: Vanilla Ice Cream
print(chocolate_ice_cream.serve_ice_cream())  # Output: Chocolate Ice Cream
