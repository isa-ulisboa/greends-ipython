class Plant:
    def __init__(self, species):
        self.species = species

class Tray:
    def __init__(self, species, count):
        self.species = species
        self.count = count  # Number of plants of the same species in the tray

    def add_plants(self, number):
        """Add plants to the tray."""
        self.count += number

    def remove_plants(self, number):
        """Remove plants from the tray. Returns the number removed."""
        if number > self.count:
            removed = self.count
            self.count = 0
        else:
            self.count -= number
            removed = number
        return removed

    def __repr__(self):
        return f"Tray(species={self.species}, count={self.count})"

class Pot:
    def __init__(self, species):
        self.species = species

class Nursery:
    def __init__(self):
        self.trays = []  # A list of trays in the nursery
        self.pots = []  # A list of pots in the nursery
        self.tray_inventory = {}  # Dictionary to track inventory of each species in the nursery
        self.pot_inventory = {}  # Dictionary to track inventory of each species in the nursery

    def add_tray(self, species, count):
        # Add a tray of a given species and count.
        tray = Tray(species, count)
        self.trays.append(tray)
        # Update the inventory
        if species in self.tray_inventory:
            self.tray_inventory[species] += count
        else:
            self.tray_inventory[species] = count

    def remove_plants_from_tray(self, species, count):
        # Remove plants of a given species from trays.
        removed_count = 0
        for tray in self.trays:
            if tray.species == species:
                number_removed = tray.remove_plants(count)
                removed_count += number_removed
                count -= number_removed
                if number_removed > count:
                    break
        # Update the inventory
        if species in self.tray_inventory:
            self.tray_inventory[species] -= removed_count
            if self.tray_inventory[species] <= 0:
                del self.tray_inventory[species]

    def get_inventory(self):
        """Returns the current inventory of plants in the nursery."""
        return self.tray_inventory

# Create a nursery
nursery = Nursery()

# Add trays to the nursery
nursery.add_tray('Tomato', 20)
nursery.add_tray('Cucumber', 15)
nursery.add_tray('Tomato', 30)

# View the nursery's inventory
print(nursery.get_inventory())  # {'Tomato': 50, 'Cucumber': 15}

# Remove some plants from a tray
nursery.remove_plants_from_tray('Tomato', 40)

# View updated inventory
print(nursery.get_inventory())  # {'Tomato': 40, 'Cucumber': 15}

# View the trays to see how many plants are left
print(nursery.trays)  # [Tray(species=Tomato, count=10), Tray(species=Cucumber, count=15), Tray(species=Tomato, count=30)]
