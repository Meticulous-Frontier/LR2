init -1 python:
    def change_location_enhanced(self,new_location):
              
        self.location = new_location       
        
        # list of followers follow you around. Will go to scheduled room on time advance.¨
        # Added extra checks to make sure it runs through everything and moves all people in list, not only first.
        for room in list_of_places:
            for person in room.people:
                for person in list_of_followers:
                    if person in list_of_followers:
                        if person in room.people:
                            room.move_person(person, new_location)

        change_scene_display(new_location)


    MainCharacter.change_location = change_location_enhanced