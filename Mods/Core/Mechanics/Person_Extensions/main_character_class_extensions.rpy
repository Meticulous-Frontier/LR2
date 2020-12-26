init -1 python:
    def change_location_enhanced(self, new_location):
        self.location = new_location

        for person in [x for x in all_people_in_the_game([mc]) if x.follow_mc]:
            person.location.move_person(person, new_location)
        return

    MainCharacter.change_location = change_location_enhanced

    def has_dungeon(self):
        return mc.business.event_triggers_dict.get("dungeon_owned", False) == True

    MainCharacter.has_dungeon = has_dungeon
