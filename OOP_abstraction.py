'''
Use an abstract base class (ABC) from Python’s abc module. 
This will enforce that all subclasses of Tray must implement the report_status method. 
'''

import sys
from abc import ABC, abstractmethod

class Tray(ABC):
    def __init__(self, species, number_of_plants):
        if int(number_of_plants) < 1:
            sys.exit('Number of plants has to be at least one')
        if type(species) != str:
            sys.exit('Species should be a string')
        self.species = species
        self.number_of_plants = number_of_plants
        self.is_usable = True

    def is_empty(self):
        return self.number_of_plants == 0

    # Abstract method that must be implemented by subclasses
    @abstractmethod
    def report_status(self):
        pass

class SingleUseTray(Tray):
    def __init__(self, species, number_of_plants):
        super().__init__(species, number_of_plants)

    def remove_plants(self):
        if not self.is_usable:
            sys.exit('This tray cannot be used anymore')
        self.is_usable = False
        return [Plant(self.species) for _ in range(self.number_of_plants)]

    # Implementation of the abstract method
    def report_status(self):
        if not self.is_usable:
            return "This single-use tray has been used and is now empty."
        else:
            return f"This single-use tray contains {self.number_of_plants} {self.species} plants and is ready to use."

class MultipleUseTray(Tray):
    def __init__(self, species, number_of_plants):
        super().__init__(species, number_of_plants)
        self.number_of_uses = 0

    def remove_plants(self, number):
        if number > self.number_of_plants:
            sys.exit(f'The tray only contains {self.number_of_plants} {self.species}')
        self.number_of_plants -= number
        return [Plant(self.species) for _ in range(number)]

    def add_seeds(self, number):
        if number > 0:
            self.number_of_plants += number

    # Implementation of the abstract method
    def report_status(self):
        if self.is_empty():
            return "This multiple-use tray is empty but can be refilled with seeds."
        else:
            return f"This multiple-use tray has {self.number_of_plants} {self.species} plants and is reusable."

class Plant:
    def __init__(self, species):
        if type(species) != str:
            sys.exit('Species should be a string')
        self.species = species

    def __repr__(self):
        return f'{self.species}'

# Create tray objects
stray = SingleUseTray('Rose', 3)
mtray = MultipleUseTray('Lily', 4)

# Remove and add to the trays
plants_from_stray = stray.remove_plants()
mtray.add_seeds(2)
plants_from_mtray = mtray.remove_plants(5)

# Print tray status reports
print(stray.report_status())
print(mtray.report_status())
