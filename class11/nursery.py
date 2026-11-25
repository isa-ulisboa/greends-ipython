# nursery.py: starting script for Class 11
# Class Tray of Class 9 (3.1 and 3.2).


class Tray:
    MAX_PLANTS = 50   # class variable: the same for all trays

    def __init__(self, species, n_plants=0):
        if n_plants < 0 or n_plants > Tray.MAX_PLANTS:
            raise ValueError(f"n_plants must be between 0 and {Tray.MAX_PLANTS}")
        self.species = species
        self.n_plants = n_plants

    def add_plants(self, n):
        if self.n_plants + n > Tray.MAX_PLANTS:
            raise ValueError(f"there is only room for {Tray.MAX_PLANTS - self.n_plants} more plants")
        self.n_plants += n

    def remove_plants(self, n):
        if n > self.n_plants:
            raise ValueError(f"the tray only has {self.n_plants} plants")
        self.n_plants -= n

    def __str__(self):
        return f"{self.n_plants} {self.species} plants"
