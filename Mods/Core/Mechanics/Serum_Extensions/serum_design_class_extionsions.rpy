init 1 python:
    # Checks if the SerumDesign contains a specific trait based on its name.
    def has_trait(self, the_trait):
        return next((x for x in self.traits + self.side_effects if x == the_trait), None) != None

    SerumDesign.has_trait = has_trait
