# Enables extra functions for SerumDesign / SerumTraits.
init 2 python:
   
   # Checks if the SerumDesign contains a specific trait based on its name.
   def has_trait(self, the_trait): 
      for trait in self.traits or trait in self.side_effects:
         if trait.name == the_trait.name:
            return trait
   SerumDesign.has_trait = has_trait