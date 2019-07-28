# Add object comparison and hash function to the Personality class

init -1 python:
    # Compare on personality type prefix when comparing to another personality otherwise use hash function
    def personality_compare(self,other): 
        if isinstance(other, Personality):
            if self.personality_type_prefix == other.personality_type_prefix:
                return 0

        if self.__hash__() < other.__hash__(): #Use hash values to break ties.
            return -1
        else:
            return 1

    Personality.__cmp__ = personality_compare

    def personality_hash(self):
        return hash(self.personality_type_prefix)

    Personality.__hash__ = personality_hash


    def main_character_change_location(self,new_location):
        self.location = new_location
        change_scene_display(new_location)
        return

    MainCharacter.change_location = main_character_change_location