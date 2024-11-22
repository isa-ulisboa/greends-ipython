class Tray:
    def __init__(self, seed_type, num_of_seeds):
        # Public attributes
        self.seed_type = seed_type
        self.num_of_seeds = num_of_seeds
        
        # Private attribute (encapsulation)
        self.__growth_stage = "Seed"

    # Public getter method to access the current growth stage
    def get_growth_stage(self):
        return self.__growth_stage

    # Public setter method to change the growth stage
    def set_growth_stage(self, stage):
        valid_stages = ["Seed", "Sprout", "Seedling", "Mature Plant"]
        if stage in valid_stages:
            self.__growth_stage = stage
        else:
            print(f"Invalid growth stage: {stage}")

    # Public method to simulate plant growth
    def grow_plants(self):
        if self.__growth_stage == "Seed":
            self.__growth_stage = "Sprout"
        elif self.__growth_stage == "Sprout":
            self.__growth_stage = "Seedling"
        elif self.__growth_stage == "Seedling":
            self.__growth_stage = "Mature Plant"
        else:
            print("Plants are already fully grown!")

# Example usage
tray = Tray("Tomato", 30)
print("Seed Type:", tray.seed_type)
print("Number of Seeds:", tray.num_of_seeds)
print("Current Growth Stage:", tray.get_growth_stage())

# Using the setter to update growth stage
tray.set_growth_stage("Seedling")
print("Growth Stage after setter:", tray.get_growth_stage())

# Simulate plant growth
tray.grow_plants()
print("Growth Stage after growing:", tray.get_growth_stage())
