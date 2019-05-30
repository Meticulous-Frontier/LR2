init -1 python:

    # overrides the default MC run turn function
    def run_turn_enhanced(self):
        self.listener_system.fire_event("time_advance")
        self.change_arousal(-20)

        # Adds mandatory roles to every person in the game
        for person in all_people_in_the_game(excluded_people = []):
            for role in apply_mandatory_roles:
                if role not in person.special_role:
                    person.special_role.append(role)
        return

    MainCharacter.run_turn = run_turn_enhanced

    def change_location_enhanced(self,new_location):
        self.location = new_location

        # list of followers follow you around. Will go to scheduled room on time advance.
        for location in list_of_places:
            for person in location.people:
                if person in list_of_followers:
                    location.move_person(person, new_location)

        change_scene_display(new_location)


    MainCharacter.change_location = change_location_enhanced