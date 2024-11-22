import sys

class Tray:
    def __init__(self,species,number_of_plants):
        if int(number_of_plants) < 1:
            sys.exit('Number of plants has to be at least one')
        if type(species)!=str:
            sys.exit('Species should be a string')
        self.species=species
        self.number_of_plants=number_of_plants
        self.is_usable=True

    def is_empty(self):
        return self.number_of_plants == 0

    def __repr__(self):
        return f'This tray has {self.number_of_plants} {self.species}'

class SingleUseTray(Tray):
    def __init__(self,species,number_of_plants):
        super().__init__(species,number_of_plants)

    def remove_plants(self): # self refers to the object of the class
        if not self.is_usable:
            sys.exit('This tray cannot be used anymore')
        self.is_usable=False
        return [Plant(self.species) for _ in range(self.number_of_plants)]

    # example of polymorphism 
    def __repr__(self):
        return f'This single use tray has {self.number_of_plants} {self.species}'


class MultipleUseTray(Tray):
    def __init__(self,species,number_of_plants):
        super().__init__(species,number_of_plants)
        self.number_of_uses=0

    def remove_plants(self, number): # self refers to the object of the class
        if number > self.number_of_plants:
            sys.exit(f'The tray only contains {self.number_of_plants} {self.species}')
        self.number_of_plants = self.number_of_plants-number
        return [Plant(self.species) for _ in range(number)]

    def add_seeds(self,number):
        if (number>0):
            self.number_of_plants += number

class Plant:
    def __init__(self,species):
        if type(species)!=str:
            sys.exit('Species should be a string')
        self.species=species

    def __repr__(self):
        return f'{self.species}'


# create tray objects
stray=SingleUseTray('Rose',3)
mtray=MultipleUseTray('Lily',4)
# remove and add to the trays
plants_from_stray=stray.remove_plants()
mtray.add_seeds(2)
plants_from_mtray=mtray.remove_plants(5)
# print tray contents
print(stray)
print(mtray)

