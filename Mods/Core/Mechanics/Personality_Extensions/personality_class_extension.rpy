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

    def rebuild_response_dictionary(self):
        self.response_dict = {}
        for ending in self.response_label_ending:
            if renpy.has_label(self.personality_type_prefix + "_" + ending):
                self.response_dict[ending] = self.personality_type_prefix + "_" + ending
            elif default_prefix is not None and renpy.has_label(self.default_prefix + "_" + ending):
                self.response_dict[ending] = self.default_prefix + "_" + ending
            else:
                self.response_dict[ending] = "relaxed_" + ending
        return

    Personality.rebuild_response_dictionary = rebuild_response_dictionary

    def get_dialogue_enhanced(self, the_person, type, **extra_args):
        target = self.response_dict[type]
        if not renpy.has_label(target): # self repairing personality response dictionary (helps with upgrades / changes to personality files)
            self.rebuild_response_dictionary()
            target = self.response_dict[type]

        renpy.call(target, the_person, **extra_args)
        return

    Personality.get_dialogue = get_dialogue_enhanced

    def get_base_personality_prefix(self):
        if self.default_prefix:
            return self.default_prefix
        return self.personality_type_prefix

    Personality.base_personality_prefix = property(get_base_personality_prefix, None, None, "Returns one of the base personality types.")



init 4 python:
    list_of_extra_personalities = [] # Personalities not included in list_of_personalities

    def update_list_of_extra_personalities():
        if "starbuck_personality" in globals():
            if starbuck_personality not in list_of_extra_personalities:
                list_of_extra_personalities.append(starbuck_personality)
        if "FA_personality" in globals():
            if FA_personality not in list_of_extra_personalities:
                list_of_extra_personalities.append(FA_personality)
        if "Sarah_personality" in globals():
            if Sarah_personality not in list_of_extra_personalities:
                list_of_extra_personalities.append(Sarah_personality)
        if "hotwife_personality" in globals():
            if hotwife_personality not in list_of_extra_personalities:
                list_of_extra_personalities.append(hotwife_personality)
        if "athlete_personality" in globals():
            if athlete_personality not in list_of_extra_personalities:
                list_of_extra_personalities.append(athlete_personality)
        if "nora_personality" in globals():
            if nora_personality not in list_of_extra_personalities:
                list_of_extra_personalities.append(nora_personality)
        if "aunt_personality" in globals():
            if aunt_personality not in list_of_extra_personalities:
                list_of_extra_personalities.append(aunt_personality)
        if "cousin_personality" in globals():
            if cousin_personality not in list_of_extra_personalities:
                list_of_extra_personalities.append(cousin_personality)
        if "cougar_personality" in globals():
            if cougar_personality not in list_of_extra_personalities:
                list_of_extra_personalities.append(cougar_personality)
        if "alpha_personality" in globals():
            if alpha_personality not in list_of_extra_personalities:
                list_of_extra_personalities.append(alpha_personality)
        return

    add_label_hijack("normal_start", "update_extra_personalities_list")
    add_label_hijack("after_load", "update_extra_personalities_list")

init 1299 python:
    if hasattr(Personality, "response_label_ending"):
        Personality.response_label_ending.append("sex_toy_taboo_break")
        Personality.response_label_ending.append("roleplay_taboo_break")
        Personality.response_label_ending.append("sleepover_yourplace_response")
        Personality.response_label_ending.append("sleepover_herplace_response")
        Personality.response_label_ending.append("sleepover_yourplace_sex_start")
        Personality.response_label_ending.append("sleepover_herplace_sex_start")
        Personality.response_label_ending.append("sleepover_impressed_response")
        Personality.response_label_ending.append("sleepover_good_response")
        Personality.response_label_ending.append("sleepover_bored_response")
        Personality.response_label_ending.append("lingerie_shopping_tame_response")
        Personality.response_label_ending.append("lingerie_shopping_excited_response")
        Personality.response_label_ending.append("lingerie_shopping_wow_response")
        Personality.response_label_ending.append("GIC_finish_response")

init 1400 python:
    # update default personalities with extra opinions (not in base game)
    relaxed_personality.common_likes.append("high heels")
    introvert_personality.common_likes.append("boots")
    introvert_personality.common_dislikes.append("high heels")
    reserved_personality.common_likes.append("dresses")
    reserved_personality.common_dislikes.append("skirts")
    wild_personality.common_likes.append("high heels")
    wild_personality.common_likes.append("dresses")

label update_extra_personalities_list(stack):
    $ update_list_of_extra_personalities()
    $ execute_hijack_call(stack)
    return
