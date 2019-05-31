init -1 python:
    def change_location_enhanced(self,new_location):
        self.location = new_location

        # list of followers follow you around. Will go to scheduled room on time advance.
        for location in list_of_places:
            for person in location.people:
                if person in list_of_followers:
                    location.move_person(person, new_location)

        change_scene_display(new_location)


    MainCharacter.change_location = change_location_enhanced