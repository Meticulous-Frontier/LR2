init -1 python:
    def change_location_enhanced(self, new_location):
        self.location = new_location

        for person in [x for x in all_people_in_the_game() if x.follow_mc]:
            person.change_location(new_location)
        return

    MainCharacter.change_location = change_location_enhanced

    def has_dungeon(self):
        return mc.business.event_triggers_dict.get("dungeon_owned", False) == True

    MainCharacter.has_dungeon = has_dungeon

    def is_at_work(self): #Checks to see if the main character is at work, generally used in crisis checks.
        return self.location in [self.business.m_div, self.business.p_div, self.business.r_div, self.business.s_div, self.business.h_div]

    MainCharacter.is_at_work = is_at_work

    def is_home(self):
        return self.location in [hall, bedroom, kitchen, lily_bedroom, mom_bedroom, dungeon]

    MainCharacter.is_home = is_home

    def change_locked_clarity_enhanced(self, amount, add_to_log = True): #TODO: Decide if we need a max locked clarity thing to gate progress in some way.
        amount = __builtin__.int(__builtin__.round(amount * get_clarity_mult()))
        self.locked_clarity += amount
        log_string = ""
        if amount > 0:
            log_string += "You: +" + str(amount) + " Locked Clarity"
        else:
            log_string += "You: " + str(amount) + " Locked Clarity"
        if add_to_log and amount != 0:
            mc.log_event(log_string, "float_text_blue")

            effect_strength = (amount/80.0) + 0.4
            if effect_strength > 1.0:
                effect_strength = 1.0
            renpy.show_screen("border_pulse", effect_strength, _transient = True)
        return
