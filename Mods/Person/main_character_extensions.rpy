init -1 python:

    # overrides the default MC run turn function
    def run_turn(self):
        self.listener_system.fire_event("time_advance")
        self.change_arousal(-20)

        # Adds mandatory roles to every person in the game
        for person in all_people_in_the_game(excluded_people = []):
            for role in apply_mandatory_roles:
                if role not in person.special_role:
                    person.special_role.append(role)
        return

    MainCharacter.run_turn = run_turn
