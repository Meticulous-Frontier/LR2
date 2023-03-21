init -1 python:
    def change_location_enhanced(self, new_location, show_background = True):
        if isinstance(new_location, Room):
            self.location = new_location
            for person in [x for x in all_people_in_the_game() if x.follow_mc]:
                person.change_location(new_location)
            if show_background:
                self.location.show_background()
        return

    MainCharacter.change_location = change_location_enhanced

    def has_dungeon(self):
        return mc.business.event_triggers_dict.get("dungeon_owned", False) == True

    MainCharacter.has_dungeon = has_dungeon

    def is_home(self):
        return self.location in [hall, bedroom, lily_bedroom, mom_bedroom, kitchen, home_bathroom, dungeon, home_shower]

    MainCharacter.is_home = is_home

    def is_at_work_enhanced(self): #Checks to see if the main character is at work, generally used in crisis checks.
        return self.location in [lobby, self.business.m_div, self.business.p_div, self.business.r_div, self.business.s_div, self.business.h_div, ceo_office, testing_room]

    MainCharacter.is_at_work = is_at_work_enhanced

    def is_home_improvement_in_progress():
        return mc.business.event_triggers_dict.get("home_improvement_in_progress", False) == True

    def is_dungeon_unlocked():
        return mc.business.event_triggers_dict.get("dungeon_unlocked", False) == True

    def change_locked_clarity_enhanced(self, amount, add_to_log = True): #TODO: Decide if we need a max locked clarity thing to gate progress in some way.
        if "perk_system" in globals() and perk_system is not None:
            amount = amount * get_clarity_multiplier()
            if perk_system.get_ability_flag("Lustful Priorities"):
                amount += 5

        amount = __builtin__.int(__builtin__.round(amount))
        self.locked_clarity += amount

        arousal = amount * .2
        if arousal > 5:
            arousal = 5
        self.change_arousal(arousal)

        if add_to_log and amount != 0:
            log_string = "You: " + ("+" if amount > 0 else "") + str(amount) + " {image=lust_eye_token_small} " + ("+" if arousal > 0 else "") + str(arousal)+ " {image=arousal_token_small}"
            mc.log_event(log_string, "float_text_blue")

            effect_strength = __builtin__.min((amount/80.0) + 0.4, 1.0)
            renpy.show_screen("border_pulse", effect_strength, _transient = True)
        return

    MainCharacter.change_locked_clarity = change_locked_clarity_enhanced

    def main_character_change_stats(self, arousal = None, locked_clarity = None, energy = None, add_to_log = True):
        message = []
        if not arousal is None:
            self.change_arousal(arousal)
            message.append(("+" if arousal > 0 else "") + str(arousal) + " {image=arousal_token_small}")
        if not locked_clarity is None:
            self.change_locked_clarity(locked_clarity, add_to_log = False)
            message.append(("+" if locked_clarity > 0 else "") + str(locked_clarity) + " {image=lust_eye_token_small}")
        if not energy is None:
            amount = self.change_energy(energy, add_to_log = False)
            if amount and amount != 0:
                message.append(("+" if amount > 0 else "") + str(amount) + " {image=energy_token_small}")
        if add_to_log and message:
            mc.log_event("You: " + " ".join(message), "float_text_yellow")
            if not locked_clarity is None and persistent.clarity_messages:
                effect_strength = __builtin__.min((amount/80.0) + 0.4, 1.0)
                renpy.show_screen("border_pulse", effect_strength, _transient = True)

    MainCharacter.change_stats = main_character_change_stats
