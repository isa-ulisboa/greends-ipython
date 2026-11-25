# nursery.py: starting script for Class 11
# Classes Tray and Inventory of Class 9 (Parts 3 and 4).


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


class Inventory:
    def __init__(self, name):
        self.name = name
        self.trays = {}   # tray name -> Tray object

    def add_tray(self, tray_name, tray):
        self.trays[tray_name] = tray

    def get_tray(self, tray_name):
        return self.trays[tray_name]

    def remove_tray(self, tray_name):
        if tray_name not in self.trays:
            raise ValueError(f"there is no tray {tray_name}")
        del self.trays[tray_name]

    def list_all_trays(self):
        for tray_name, tray in self.trays.items():
            print(f"{tray_name}: {tray}")

    def n_plants(self):
        return sum(tray.n_plants for tray in self.trays.values())

    def plants_by_species(self):
        counts = {}
        for tray in self.trays.values():
            counts[tray.species] = counts.get(tray.species, 0) + tray.n_plants
        return counts

    def empty_trays(self):
        return [tray_name for tray_name, tray in self.trays.items() if tray.n_plants == 0]

    def total_value(self, prices):
        return sum(tray.n_plants * prices[tray.species] for tray in self.trays.values())

    def __str__(self):
        return f"{self.name}: {len(self.trays)} trays"
