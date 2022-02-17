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

    def is_home(self):
        return self.location in [hall, bedroom, kitchen, lily_bedroom, mom_bedroom, dungeon]

    MainCharacter.is_home = is_home

    def is_home_improvement_in_progress():
        return mc.business.event_triggers_dict.get("home_improvement_in_progress", False) == True

    def is_dungeon_unlocked():
        return mc.business.event_triggers_dict.get("dungeon_unlocked", False) == True

    def main_character_change_locked_clarity_extended(org_func):
        def change_locked_clarity_wrapper(main_character, amount, add_to_log = True):
            # run extension code
            if "perk_system" in globals():
                amount = amount * get_clarity_multiplier()
                amount = __builtin__.int(amount)
                if perk_system.get_ability_flag("Lustful Priorities"):
                    amount += 5

            # run original function
            org_func(main_character, amount, add_to_log = add_to_log)

        return change_locked_clarity_wrapper

    MainCharacter.change_locked_clarity = main_character_change_locked_clarity_extended(MainCharacter.change_locked_clarity)
