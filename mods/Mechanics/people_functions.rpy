init -1 python:
    def all_people_in_the_game(excluded_people = None): # Pass excluded_people as array of people [mc, lily]
        all_people = []
        for location in list_of_places:
            for person in location.people:
                if person not in excluded_people:
                    all_people.append(person)
        return all_people

    def get_random_person_in_the_game(excluded_people = None): # Pass excluded_people as array of people [mc, lily]
        all_people = all_people_in_the_game(excluded_people)
        return get_random_from_list(all_people)

    def learn_home(self): # Adds the_person.home to mc.known_home_locations allowing it to be visited without having to go through date label
        if not self.home in mc.known_home_locations:
            mc.known_home_locations.append(self.home)
            return True # Returns true if it succeeds
        return False # Returns false otherwise, so it can be used for checks.

    # Adds learn_home function to the_person.
    Person.learn_home = learn_home

    # Strips down the person to a clothing their are comfortable with
    # optional: clothing_message narrator voice after each item use '##clothing##'' in message for clothing item stripped, use '##person_name##' for self nanme.
    # note: at least 1 item gets removed regardsless of sluttiness
    def strip_outfit_to_max_sluttiness(self, top_layer_first = True, exclude_feet = True, narrator_message = None):
        strip_choice = self.outfit.remove_random_upper(top_layer_first, exclude_feet, do_not_remove = True)
        if not narrator_message is None:
            narrator_message = narrator_message.replace("##person_name##", self.name)
        while not strip_choice is None:
            self.draw_animated_removal(strip_choice)
            if not narrator_message is None:
                renpy.say(None, narrator_message.replace("##clothing##", strip_choice.name))
            if self.judge_outfit(self.outfit):
                strip_choice = self.outfit.remove_random_upper(top_layer_first, exclude_feet, do_not_remove = True)
                if strip_choice is None:
                    strip_choice = self.outfit.remove_random_any(top_layer_first, exclude_feet, do_not_remove = True)
            else:
                strip_choice = None
        return


    # Monkey wrench Person class to have automatic strip function
    Person.strip_outfit_to_max_sluttiness = strip_outfit_to_max_sluttiness

    def reset_outfit(self):
        self.outfit = self.planned_outfit.get_copy()
        return

    # Monkey wrench Person class to have reset outfit function
    Person.reset_outfit = reset_outfit

    def add_opinion(self, opinion, degree, discovered, sexy_opinion = False, add_to_log = True): # Gives a message stating the opinion has been changed.

        opinion = opinion
        degree = degree
        discovered = discovered
        sexy_opinion = sexy_opinion # False for normal, True for Sexy

        if sexy_opinion == False:
            self.opinions[opinion] = [degree, discovered]

            if opinion not in opinions_list: # Appends to the opinion pool
                opinions_list.append(opinion)

        elif sexy_opinion == True:
            self.sexy_opinions[opinion] = [degree, discovered]

            if opinion not in sexy_opinions_list: # Appends to the opinion pool
                sexy_opinions_list.append(opinion)
        if degree == -2:
            log_string = "Hates " + str(opinion)

        elif degree == -1:
            log_string = "Dislikes " + str(opinion)

        elif degree == 0:
            log_string = "Indifferent to " + str(opinion)

        elif degree == 1:
            log_string = "Likes " + str(opinion)

        elif degree == 2:
            log_string = "Loves " + str(opinion)

        if add_to_log:
            mc.log_event(self.name + ": " + log_string, "float_text_green")
        return
    # Adds a function that edits and adds opinions. It also appends to the vanilla opinion pool.
    Person.add_opinion = add_opinion
