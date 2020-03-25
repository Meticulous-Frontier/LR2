# Add object comparison and hash function to the Personality class

init -1 python:
    # Compare on personality type prefix when comparing to another personality otherwise use hash function
    def personality_compare(self,other):
        if isinstance(self, other.__class__):
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
    Personality.hash = personality_hash

    def personality_eq(self, other):
        if isinstance(self, other.__class__):
            return self.personality_type_prefix == other.personality_type_prefix
        return False

    Personality.__eq__ = personality_eq

    def personality_ne(self, other):
        if isinstance(self, other.__class__):
            return self.personality_type_prefix != other.personality_type_prefix
        return True

    Personality.__ne__ = personality_ne

init 4 python:
    list_of_extra_personalities = [] # Personalities not included in list_of_personalities

    add_label_hijack("normal_start", "update_extra_personalities_list")
    add_label_hijack("after_load", "update_extra_personalities_list")

label update_extra_personalities_list(stack):

    if "starbuck_personality" in globals():
        if starbuck_personality not in list_of_extra_personalities:
            $ list_of_extra_personalities.append(starbuck_personality)
    if "FA_personality" in globals():
        if FA_personality not in list_of_extra_personalities:
            $ list_of_extra_personalities.append(FA_personality)
    if "Sarah_personality" in globals():
        if Sarah_personality not in list_of_extra_personalities:
            $ list_of_extra_personalities.append(Sarah_personality)
    if "hotwife_personality" in globals():
        if hotwife_personality not in list_of_extra_personalities:
            $ list_of_extra_personalities.append(hotwife_personality)
    if "athlete_personality" in globals():
        if athlete_personality not in list_of_extra_personalities:
            $ list_of_extra_personalities.append(athlete_personality)
    if "nora_personality" in globals():
        if nora_personality not in list_of_extra_personalities:
            $ list_of_extra_personalities.append(nora_personality)
    if "aunt_personality" in globals():
        if aunt_personality not in list_of_extra_personalities:
            $ list_of_extra_personalities.append(aunt_personality)
    if "cousin_personality" in globals():
        if cousin_personality not in list_of_extra_personalities:
            $ list_of_extra_personalities.append(cousin_personality)

    $ execute_hijack_call(stack)
