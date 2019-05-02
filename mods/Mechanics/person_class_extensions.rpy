 init -1 python:
 
    ## CHANGE HEIGHT EXTENSION
    # Returns True when the persons height has changed; otherwise False
    # chance is probability percentage that height change for amount will occur (used by serums)
    def change_height(self, amount, chance):
        if amount == 0 or (height == .8 and amount < 0) or (height == 1 and amount > 0):
            return False

        if renpy.random.randint(0, 100) <= chance:
            self.height += amount
        else:
            return False

        if self.height > 1:
            self.height == 1
        
        if self.height < .8:
            self.height = .8
        
        return True
    
    # attach change height function to the Person class
    Person.change_height = change_height

    ## CHANGE WEIGHT EXTENSION
    # Returns True when the persons body type has changed; otherwise False
    # chance is probability percentage that weight change for amount will occur (used by serums)
    def change_weight(self, amount, chance):
        check_person_weight_attribute(self)
        if (amount == 0):
            return False

        if renpy.random.randint(0, 100) <= chance:
            self.weight += amount
        
        # maximum and minimum weight are dependant on height
        max_weight = self.height * 100
        min_weight = self.height * 50
        switch_point_low = self.height * 68
        switch_point_high = self.height * 83

        if (amount > 0):
            if self.weight > switch_point_low + 3 and self.body_type == "thin_body":
                self.body_type = "standard_body"
                return True
            if self.weight > switch_point_high + 3 and self.body_type == "standard_body":
                self.body_type = "curvy_body"
                return True
            if self.weight > max_weight: #Maximum weight
                self.weight = max_weight
            return False

        if (amount < 0):
            if self.weight < min_weight:  #Minimum weight
                self.weight = min_weight
                return False
            if self.weight < switch_point_low - 3 and self.body_type == "standard_body":
                self.body_type = "thin_body"        
                return True
            if self.weight < switch_point_high - 3 and self.body_type == "curvy_body":
                self.body_type = "standard_body"
                return True
            return False
    
    # attach change weight function to the Person class
    Person.change_weight = change_weight

    ## LEARN HOME EXTENSION
    def learn_home(self): # Adds the_person.home to mc.known_home_locations allowing it to be visited without having to go through date label
        if not self.home in mc.known_home_locations:
            mc.known_home_locations.append(self.home)
            return True # Returns true if it succeeds
        return False # Returns false otherwise, so it can be used for checks.

    # Adds learn_home function to the_person.
    Person.learn_home = learn_home

    ## STRIP OUTFIT TO MAX SLUTTINES EXTENSION
    # Strips down the person to a clothing their are comfortable with (starting with top, before bottom)
    # optional: clothing_message narrator voice after each item use '##clothing##'' in message for clothing item stripped, use '##person_name##' for self name.
    #           Can be an array of messages for variation in message per clothing item
    # note: at least 1 item gets removed regardsless of sluttiness 
    def strip_outfit_to_max_sluttiness(self, top_layer_first = True, exclude_feet = True, narrator_message = None):
        # internal function to strip top clothing first.
        def get_strip_choice_upper_first(person, top_layer_first = True, exclude_feet = True, do_not_remove = True):
            strip_choice = person.outfit.remove_random_upper(top_layer_first, do_not_remove)
            if strip_choice is None:
                strip_choice = person.outfit.remove_random_any(top_layer_first, exclude_feet, do_not_remove)
            return strip_choice
        def get_narrator_message(message):
            if isinstance(message, basestring):
                return message
            else:
                msg_choice_index = renpy.random.randint(1,len(message))
                return message[msg_choice_index - 1]           

        strip_choice = get_strip_choice_upper_first(self, top_layer_first, exclude_feet, do_not_remove = True)
        while not strip_choice is None:
            self.draw_animated_removal(strip_choice)
            if narrator_message:
                message = get_narrator_message(narrator_message)
                renpy.say(None, message.replace("##person_name##", self.name).replace("##clothing##", strip_choice.name))
            if self.judge_outfit(self.outfit):
                strip_choice = get_strip_choice_upper_first(self, top_layer_first, exclude_feet, do_not_remove = True)
            else:
                strip_choice = None
        return

    # Monkey wrench Person class to have automatic strip function
    Person.strip_outfit_to_max_sluttiness = strip_outfit_to_max_sluttiness

    ## RESET OUTFIT EXTENSION
    # Restores the outfit the person was wearing prior to an event (if changed by event)
    def reset_outfit(self):
        self.outfit = self.planned_outfit.get_copy()
        return

    # Adds reset_outfit function to Person class
    Person.reset_outfit = reset_outfit

    ## ADD OPINION EXTENSION
    ## Adds add_opinion function to Person class
    def add_opinion(self, opinion, degree, discovered = None, sexy_opinion = False, add_to_log = True): # Gives a message stating the opinion has been changed.
        opinion = opinion
        degree = degree
        discovered = discovered
        sexy_opinion = sexy_opinion # False for normal, True for Sexy

        if discovered is None and opinion in self.opinions[0]:  # we passed None for discovered so use existing discovered info
            discovered = self.opinions[opinion][1]

        if discovered is None and opinion in self.sexy_opinions[0]: # we passed None for discovered so use existing discovered info
            discovered = self.sexy_opinions[opinion][1]
        
        if discovered is None: # we didn't find any discovery information for opinion, so it's new and we passed None, so default set to false
            discovered = False

        if sexy_opinion == False:
            self.opinions[opinion] = [degree, discovered]

            if opinion not in opinions_list: # Appends to the opinion pool #TODO: should we add this to the game pool here? Prevents person specific opinions...
                opinions_list.append(opinion)

        elif sexy_opinion == True:
            self.sexy_opinions[opinion] = [degree, discovered]

            if opinion not in sexy_opinions_list: # Appends to the opinion pool #TODO: should we add this to the game pool here? Prevents person specific opinions...
                sexy_opinions_list.append(opinion)

        if add_to_log:
            mc.log_event(self.name + " " + opinion_score_to_string(degree) + " " + str(opinion), "float_text_green")
        return

    # Adds a function that edits and adds opinions. It also appends to the vanilla opinion pool.
    Person.add_opinion = add_opinion

    ## CHANGE WILLPOWER EXTENSION
    # changes the willpower of a person by set amount
    def change_willpower(self, amount): #Logs change in willpower and shows new total.
        self.willpower += amount
        if self.willpower < 0:
            self.willpower = 0
        return person.willpower

    # attach to person object
    Person.change_willpower = change_willpower



#######################################
# HELPER METHODS FOR CLASS EXTENSIONS #
#######################################

    # Check if weight property exists on person, if not, add based on body type
    def check_person_weight_attribute(person):
        if not hasattr(person, "weight"):
            if (person.body_type == "thin_body"):
                setattr(person, "weight", 60 * person.height)   # default weight thin body
            elif (person.body_type == "standard_body"):
                setattr(person, "weight", 75 * person.height)   # default weight standard body
            else:
                setattr(person, "weight", 90 * person.height)   # default weight curvy body
        return

    # calculates current player mental powers
    def player_willpower():
        mc.power = 0

        mc.power += int(mc.charisma*5) # Positive character modifiers
        mc.power += int(mc.current_stamina*1.5)
        return mc.power

    # calculates current willpower of a person
    def calculate_willpower(person):
        willpower = int(person.focus * 10 + person.happiness * 0.2 - person.obedience * 0.1 - person.love * 0.2 - person.suggestibility * 0.5)

        if willpower < 0:
            willpower = 0
        return willpower

    # log will power to event log in ui
    def log_willpower(person):
        message = (person.title or person.name) + ": "
        if (person is mc):
            message += str(person.power)
        else:
            message += str(person.willpower)
        message += " Willpower"
        mc.log_event(message, "float_text_blue")
        return
