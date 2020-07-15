init -1 python:
    import hashlib

    def remove_person_from_game(self):
        my_location = self.location()
        if my_location:
            my_location.remove_person(self) # remove person from current location
        if self.home in list_of_places:
            list_of_places.remove(self.home) # remove home location from list_of_places
        if self.home in mc.known_home_locations: 
            mc.known_home_locations.remove(self.home) # remove home location from known_home_locations

        if "people_to_process" in globals():
            found = find_in_list(lambda x: x[0].name == self.name and x[0].last_name == self.last_name and x[0].age == self.age, people_to_process)
            if found: # remove from processing list
                people_to_process.remove(found)

        # remove from business teams
        for team in [mc.business.research_team, mc.business.market_team, mc.business.supply_team, mc.business.production_team, mc.business.hr_team]:
            if self in team:
                team.remove(self)

        # remove from business rooms
        for room in [mc.business.s_div, mc.business.r_div, mc.business.p_div, mc.business.m_div, mc.business.h_div]:
            if self in room.people:
                room.people.remove(self)

        # remove from strippers
        if self in stripclub_strippers:
            stripclub_strippers.remove(self)
        
        # other stripclub teams
        if "stripclub_bdsm_performers" in globals():
            for team in [stripclub_strippers, stripclub_bdsm_performers, stripclub_waitresses]:
                if self in team:
                    team.remove(self)

        # remove from relationships array
        town_relationships.remove_all_relationships(self)

        self.base_outfit = None
        self.planned_outfit = None
        self.planned_uniform = None

        for outfit in self.wardrobe.outfits + self.wardrobe.underwear_sets + self.wardrobe.overwear_sets:
            outfit.upper_body.clear()
            outfit.lower_body.clear()
            outfit.feet.clear()
            outfit.accessories.clear()

        self.wardrobe.outfits.clear()
        self.wardrobe.underwear_sets.clear()
        self.wardrobe.overwear_sets.clear()
        self.wardrobe = None

        self.special_role.clear()
        self.on_room_enter_event_list.clear()
        self.on_talk_event_list.clear()
        self.event_triggers_dict.clear()
        self.suggest_bag.clear()
        self.broken_taboos.clear()
        self.sex_record.clear()
        self.opinions.clear()
        self.sexy_opinions.clear()
        self.broken_taboos.clear()
        self.schedule.clear()

        # clear all references held by person object.
        self.home = None
        self.work = None
        self.schedule = None
        self.job = None
        self.relationship = None
        self.personality = None
        self.char = None
        self.body_images = None
        self.face_style = None
        self.expression_images = None
        self.hair_colour = None
        self.hair_style = None
        self.pubes_style = None
        self.skin = None
        self.eyes = None
        self.serum_effects = None
        self.idle_animation = None
        self.personal_region_modifiers = None
        self.on_room_enter_event_list = None
        self.on_talk_event_list = None
        self.event_triggers_dict = None
        self.situational_sluttiness = None
        self.situational_obedience = None
        # now let the Garbage Collector do the rest (we are no longer referenced in any objects).
        return

    Person.remove_person_from_game = remove_person_from_game

    def location(self): # Check what location a person is in e.g the_person.location() == downtown. Use to trigger events?
        for location in list_of_places:
            if self in location.people:
                return location

    Person.location = location

    def get_follow_me(self):
        if not hasattr(self, "_follow_me"):
            self._follow_me = False
        return self._follow_me

    def set_follow_me(self, value):
        self._follow_me = value

    def del_follow_me(self):
        del self._follow_me

    # add follow_mc attribute to person class (without sub-classing)
    Person.follow_mc = property(get_follow_me, set_follow_me, del_follow_me, "I'm the follow_me property.")

    def get_person_identifier(self):
        if not hasattr(self, "_identifier"):
            self._identifier = hashlib.md5(self.name + self.last_name + str(renpy.random.randint(10000, 90000000))).hexdigest()
        return self._identifier

    # don't allow set
    # def set_person_identifier(self, value):
    #     self._identifier = value

    # don't allow delete
    # def del_person_identifier(self):
    #     del self._identifier

    # add follow_mc attribute to person class (without sub-classing)
    Person.identifier = property(get_person_identifier, None, None, "Unique identifier for person class.")

    def get_person_next_day_outfit(self):
        if not hasattr(self, "_next_day_outfit"):
            self._next_day_outfit = None
        return self._next_day_outfit

    def set_person_next_day_outfit(self, value):
        self._next_day_outfit = value

    def del_person_next_day_outfit(self):
        del self._next_day_outfit

    # add follow_mc attribute to person class (without sub-classing)
    Person.next_day_outfit = property(get_person_next_day_outfit, set_person_next_day_outfit, del_person_next_day_outfit, "Allow for forcing the next day outfit a girl will wear (set planned outfit).")

    def get_person_weight(self):
        if not hasattr(self, "_weight"):
            if self.body_type == "thin_body":
                self._weight = 60 * self.height
            elif self.body_type == "standard_body":
                self._weight = 75 * self.height
            else:
                self._weight = 90 * self.height
        return self._weight

    def set_person_weight(self, value):
        self._weight = value

    def del_person_weight(self):
        del self.weight

    Person.weight = property(get_person_weight, set_person_weight, del_person_weight, "The weight of the person in KG.")

    def get_person_stripper_salary(self):
        if not hasattr(self, "_stripper_salary"):
            self._stripper_salary = 0
        return self._stripper_salary

    def set_person_stripper_salary(self, value):
        self._stripper_salary = value

    def del_person_stripper_salary(self):
        del self._stripper_salary

    Person.stripper_salary = property(get_person_stripper_salary, set_person_stripper_salary, del_person_stripper_salary, "The salary when person is stripping.")

    ## MATCH SKIN COLOR
    # Matches skin, body, face and expression images based on input of skin color
    def match_skin(self, color):
        if " skin" in color: # If using the_person.body_images.name as a reference, remove the " skin" part.
            color = color[:-5]

        self.skin = str(color)
        if self.skin == "white":
            self.body_images = white_skin
        elif self.skin == "tan":
            self.body_images = tan_skin
        elif self.skin == "black":
            self.body_images = black_skin
        self.expression_images = Expression("default", self.skin, self.face_style)
        return
    Person.match_skin = match_skin


    ## SET HAIRSTYLE VIA Clothing ITEM, maintain color etc.

    def set_hair_style(self, new_clothing):
        cs = renpy.current_screen()
        self.hair_style = new_clothing

        if cs:
            self.hair_colour = [cs.scope["selected_hair_colour_name"], [cs.scope["current_r"], cs.scope["current_g"], cs.scope["current_b"], cs.scope["current_a"]]]

    Person.set_hair_style = set_hair_style

    # SET PUBIC STYLE Clothing ITEM

    def set_pubic_style(self, new_clothing):
        cs = renpy.current_screen()
        self.pubes_style = new_clothing

        if cs:
            self.hair_colour = [cs.scope["selected_hair_colour_name"], [cs.scope["current_r"], cs.scope["current_g"], cs.scope["current_b"], cs.scope["current_a"]]]

    Person.set_pubic_style = set_pubic_style

    ## CHANGE HEIGHT EXTENSION
    # Returns True when the persons height has changed; otherwise False
    # chance is probability percentage that height change for amount will occur (used by serums)
    def change_height(self, amount, chance):
        lower_limit = 1 - .2
        upper_limit = 1

        if amount == 0 or (self.height == lower_limit and amount < 0) or (self.height == upper_limit and amount > 0):
            return False

        if renpy.random.randint(0, 100) <= chance:
            self.height += amount
        else:
            return False

        if self.height > upper_limit:
            self.height == upper_limit

        if self.height < lower_limit:
            self.height = lower_limit

        return True

    # attach change height function to the Person class
    Person.change_height = change_height

    ## CHANGE WEIGHT EXTENSION
    # Returns True when the persons body type has changed; otherwise False
    # chance is probability percentage that weight change for amount will occur (used by serums)
    def change_weight(self, amount, chance):
        if (amount == 0):
            return False

        if renpy.random.randint(0, 100) <= chance:
            self.weight += amount

        # maximum and minimum weight are dependant on height
        max_weight = (self.height) * 100
        min_weight = (self.height) * 50
        switch_point_low = (self.height) * 68
        switch_point_high = (self.height) * 83

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

    ## HAPPINESS SCORE ENHANCED VERSION
    # Takes into account their liking for working (if she doesn't she is more likely to quit)
    def get_job_happiness_score_enhanced(self):
        happy_points = self.happiness - 100 #Happiness over 100 gives a bonus to staying, happiness less than 100 gives a penalty
        happy_points += self.obedience - 95 #A more obedient character is more likely to stay, even if they're unhappy. Default characters can be a little disobedint without any problems.
        happy_points += self.salary - self.calculate_base_salary() #A real salary greater than her base is a bonus, less is a penalty. TODO: Make this dependent on salary fraction, not abosolute pay.
        happy_points += self.get_opinion_score("working") * 5 # Does she like working? It affects her happiness score.

        if (day - self.event_triggers_dict.get("employed_since",0)) < 14:
            happy_points += 14 - (day - self.event_triggers_dict.get("employed_since",0)) #Employees are much less likely to quit over the first two weeks.
        return happy_points

    Person.get_job_happiness_score = get_job_happiness_score_enhanced

    ## LEARN HOME EXTENSION
    def learn_home(self): # Adds the_person.home to mc.known_home_locations allowing it to be visited without having to go through date label
        if not self.home in mc.known_home_locations + [lily_bedroom, mom_bedroom, aunt_bedroom, cousin_bedroom]:
            mc.known_home_locations.append(self.home)
            return True # Returns true if it succeeds
        return False # Returns false otherwise, so it can be used for checks.

    # Adds learn_home function to the_person.
    Person.learn_home = learn_home

    def get_known_opinion_list(self, include_sexy = False, include_normal = True, only_positive = False, only_negative = False): #Gets the topic string of a random opinion this character holds. Includes options to include known opinions and sexy opinions. Returns None if no valid opinion can be found.
        the_dict = {} #Start our list of valid opinions to be listed as empty

        if include_normal: #if we include normal opinions build a dict out of the two
            the_dict = dict(the_dict, **self.opinions)

        if include_sexy: #If we want sexy opinions add them in too.
            the_dict = dict(the_dict, **self.sexy_opinions)

        unknown_keys = []
        for k in the_dict: #Go through each value in our combined normal and sexy opinion dict
            if not the_dict[k][1]: #Check if we know about it...
                unknown_keys.append(k) #We build a temporary list of keys to remove because otherwise we are modifying the dict while we traverse it.
        for del_key in unknown_keys:
            del the_dict[del_key]

        remove_keys = []
        if only_positive:
            for k in the_dict:
                if self.get_opinion_score(k) <= 0:
                    remove_keys.append(k)

        if only_negative:
            for k in the_dict:
                if self.get_opinion_score(k) > 0:
                    remove_keys.append(k)

        for del_key in remove_keys:
            del the_dict[del_key]

        return the_dict.keys()

    Person.get_known_opinion_list = get_known_opinion_list

    def generate_daughter_enhanced(self): #Generates a random person who shares a number of similarities to the mother
        age = renpy.random.randint(18, self.age-16)

        if renpy.random.randint(0,100) < 60:
            body_type = self.body_type
        else:
            body_type = None

        if renpy.random.randint(0,100) < 40: #Slightly lower for facial similarities to keep characters looking distinct
            face_style = self.face_style
        else:
            face_style = None

        if renpy.random.randint(0,100) < 30: #30% of the time they share hair colour (girls dye their hair a lot)
            hair_colour = self.hair_colour
        else:
            hair_colour = None

        if renpy.random.randint(0,100) < 60: # 60% they share the same breast size
            tits = self.tits
        else:
            tits = None

        if renpy.random.randint(0,100) < 60: #Share the same eye colour
            eyes = self.eyes
        else:
            eyes = None

        if renpy.random.randint(0,100) < 80: #Have heights that roughly match (mostly)
            height = self.height * (renpy.random.randint(95,105)/100.0)
            if height > 1.0:
                height = 1.0
            elif height < 0.8:
                height = 0.8
        else:
            height = None

        if renpy.random.randint(0,100) < 85 - age: #It is less likely she lives at home the older she is.
            start_home  = self.home
        else:
            start_home  = None


        the_daughter = make_person(last_name = self.last_name, age = age, body_type = body_type, face_style = face_style, tits = tits, height = height,
            hair_colour = hair_colour, skin = self.skin, eyes = eyes, start_home = start_home, force_random = True)

        if start_home is None:
            the_daughter.generate_home()
        the_daughter.home.add_person(the_daughter)

        for sister in town_relationships.get_existing_children(self): #First find all of the other kids this person has
            town_relationships.update_relationship(the_daughter, sister, "Sister") #Set them as sisters

        town_relationships.update_relationship(self, the_daughter, "Daughter", "Mother") #Now set the mother/daughter relationship (not before, otherwise she's a sister to herself!)

        return the_daughter

    Person.generate_daughter = generate_daughter_enhanced

    def generate_mother_enhanced(self, lives_with_daughter = False): #Generates a random person who shares a number of similarities to the mother
        age = renpy.random.randint(self.age + 16, 55)

        if renpy.random.randint(0,100) < 60:
            body_type = self.body_type
        else:
            body_type = None

        if renpy.random.randint(0,100) < 40: #Slightly lower for facial similarities to keep characters looking distinct
            face_style = self.face_style
        else:
            face_style = None

        if renpy.random.randint(0,100) < 30: #30% of the time they share hair colour (girls dye their hair a lot)
            hair_colour = self.hair_colour
        else:
            hair_colour = None

        if renpy.random.randint(0,100) < 60: # 60% they share the same breast size
            tits = self.tits
        else:
            tits = None

        if renpy.random.randint(0,100) < 60: #Share the same eye colour
            eyes = self.eyes
        else:
            eyes = None

        if renpy.random.randint(0,100) < 80: #Have heights that roughly match (mostly)
            height = self.height * (renpy.random.randint(95,105)/100.0)
            if height > 1.0:
                height = 1.0
            elif height < 0.8:
                height = 0.8
        else:
            height = None

        if lives_with_daughter:
            start_home  = self.home
        else:
            start_home  = None

        the_mother = make_person(last_name = self.last_name, age = age, body_type = body_type, face_style = face_style, tits = tits, height = height,
            hair_colour = hair_colour, skin = self.skin, eyes = eyes, start_home = start_home, force_random = True)

        # set children fixed to one, to prevent circular relative creations (like create mom, has 3 children, so we can start hiring her other daughters)
        the_mother.kids = 1

        if start_home is None:
            the_mother.generate_home()
        the_mother.home.add_person(the_mother)

        for sister in town_relationships.get_existing_sisters(self): #First find all of the sisters this person has
            town_relationships.update_relationship(the_mother, sister, "Daughter", "Mother") #Set the mother/daughter relationship for the sisters
            the_mother.kids += 1 # increase child count per sister

        town_relationships.update_relationship(self, the_mother, "Mother", "Daughter") #Now set the mother/daughter relationship with person

        return the_mother

    Person.generate_mother = generate_mother_enhanced

    ## STRIP OUTFIT TO MAX SLUTTINESS EXTENSION
    # Strips down the person to a clothing their are comfortable with (starting with top, before bottom)
    # narrator_messages: narrator voice after each item of clothing stripped, use '[person.<title>]' for titles and '[strip_choice.name]' for clothing item.
        # Can be an array of messages for variation in message per clothing item or just a single string or None for silent stripping
    # scene manager parameter is filled from that class so that all people present in scene are drawn
    def strip_outfit_to_max_sluttiness(self, top_layer_first = True, exclude_upper = False, exclude_lower = False, exclude_feet = True, delay = 1, narrator_messages = None, character_placement = None, lighting = None, temp_sluttiness_boost = 0, position = None, emotion = None, scene_manager = None):
        # internal function to strip top clothing first.
        def get_strip_choice_max(outfit, top_layer_first, exclude_upper, exclude_lower, exclude_feet):
            strip_choice = None
            if not exclude_upper:
                strip_choice = outfit.remove_random_upper(top_layer_first)
            if strip_choice is None:
                strip_choice = outfit.remove_random_any(top_layer_first, exclude_upper, exclude_lower, exclude_feet)
            return strip_choice

        def get_messages(narrator_messages):
            messages = []
            if not narrator_messages:
                pass
            elif not isinstance(narrator_messages, list):
                messages = [narrator_messages]
            else:
                messages = narrator_messages
            return messages

        messages = get_messages(narrator_messages)
        msg_count = __builtin__.len(messages)

        test_outfit = self.outfit.get_copy()
        removed_something = False

        strip_choice = get_strip_choice_max(test_outfit, top_layer_first, exclude_upper, exclude_lower, exclude_feet)
        # renpy.say("", strip_choice.name + "  (required: " + str(test_outfit.slut_requirement) +  ", sluttiness: " +  str(self.effective_sluttiness() + temp_sluttiness_boost) + ")")
        while strip_choice and self.judge_outfit(test_outfit, temp_sluttiness_boost):
            if delay > 0:
                self.draw_animated_removal(strip_choice, character_placement = character_placement, position = position, emotion = emotion, lighting = lighting, scene_manager = scene_manager) #Draw the strip choice being removed from our current outfit
                if msg_count == 0:
                    renpy.pause(delay) # if no message to show, wait a short while before automatically continue stripping
            else:
                test_outfit.remove_clothing(strip_choice)
            self.apply_outfit(test_outfit, ignore_base = True) #Swap our current outfit out for the test outfit.
            removed_something = True
            if msg_count > 0:   # do we need to show a random message and replace titles and outfit name
                msg_idx = renpy.random.randint(1, msg_count)
                msg = messages[msg_idx - 1]
                msg = msg.replace("[the_person.possessive_title]", self.possessive_title or "the unknown woman").replace("[the_person.title]", self.title or self.name).replace("[the_person.mc_title]", self.mc_title).replace("[strip_choice.name]", strip_choice.name)
                renpy.say(None, msg)

            strip_choice = get_strip_choice_max(test_outfit, top_layer_first, exclude_upper, exclude_lower, exclude_feet)

        return removed_something

    # Monkey wrench Person class to have automatic strip function
    Person.strip_outfit_to_max_sluttiness = strip_outfit_to_max_sluttiness

    def strip_outfit_to_underwear(self, delay = 1, character_placement = None, position = None, emotion = None, lighting = None, scene_manager = None):
        if position is None:
            self.position = self.idle_pose

        if emotion is None:
            self.emotion = self.get_emotion()

        if lighting is None:
            lighting = mc.location.get_lighting_conditions()

        if character_placement is None:
            self.character_placement = character_right

        strip_choice = self.outfit.remove_random_upper(True, do_not_remove = True)
        while not strip_choice is None and self.outfit.bra_covered():
            if delay > 0:
                self.draw_animated_removal(strip_choice, character_placement = character_placement, position = position, emotion = emotion, lighting = lighting, scene_manager = scene_manager) #Draw the strip choice being removed from our current outfit
                renpy.pause(delay)
            else:
                self.outfit.remove_clothing(strip_choice)
            strip_choice = self.outfit.remove_random_upper(True, do_not_remove = True)

        strip_choice = self.outfit.remove_random_lower(True, do_not_remove = True)
        while not strip_choice is None and self.outfit.panties_covered():
            if delay > 0:
                self.draw_animated_removal(strip_choice, character_placement = character_placement, position = position, emotion = emotion, lighting = lighting, scene_manager = scene_manager) #Draw the strip choice being removed from our current outfit
                renpy.pause(delay)
            else:
                self.outfit.remove_clothing(strip_choice)
            strip_choice = self.outfit.remove_random_lower(True, do_not_remove = True)

    Person.strip_outfit_to_underwear = strip_outfit_to_underwear

    def strip_outfit(self, top_layer_first = True, exclude_upper = False, exclude_lower = False, exclude_feet = True, delay = 1, character_placement = None, position = None, emotion = None, lighting = None, scene_manager = None):
        def extra_strip_check(person, top_layer_first, exclude_upper, exclude_lower, exclude_feet):
            done = exclude_upper or person.outfit.tits_available()
            if done and (exclude_lower or person.outfit.vagina_available()):
                if done and (exclude_feet or person.outfit.feet_available()):
                    return False

            return True # not done continue stripping

        if position is None:
            self.position = self.idle_pose

        if emotion is None:
            self.emotion = self.get_emotion()

        if lighting is None:
            lighting = mc.location.get_lighting_conditions()

        if character_placement is None:
            self.character_placement = character_right

        strip_choice = self.outfit.remove_random_any(top_layer_first, exclude_upper, exclude_lower, exclude_feet, do_not_remove = True)
        while not strip_choice is None and extra_strip_check(self, top_layer_first, exclude_upper, exclude_lower, exclude_feet):
            if delay > 0:
                self.draw_animated_removal(strip_choice, character_placement = character_placement, position = position, emotion = emotion, lighting = lighting, scene_manager = scene_manager) #Draw the strip choice being removed from our current outfit
                renpy.pause(delay)
            else:
                self.outfit.remove_clothing(strip_choice)
            strip_choice = self.outfit.remove_random_any(top_layer_first, exclude_upper, exclude_lower, exclude_feet, do_not_remove = True)

        # special case where she is wearing a two-part item that blocks her vagina, but we need it be available
        if not exclude_lower and not self.outfit.vagina_available():
            strip_choice = self.outfit.remove_random_any(top_layer_first, False, exclude_lower, exclude_feet, do_not_remove = True)
            while not strip_choice is None:
                if delay > 0:
                    self.draw_animated_removal(strip_choice, character_placement = character_placement, position = position, emotion = emotion, lighting = lighting, scene_manager = scene_manager) #Draw the strip choice being removed from our current outfit
                    renpy.pause(delay)
                else:
                    self.outfit.remove_clothing(strip_choice)
                strip_choice = self.outfit.remove_random_any(top_layer_first, False, exclude_lower, exclude_feet, do_not_remove = True)

    Person.strip_outfit = strip_outfit

    def choose_strip_clothing_item(self):
        clothing = None
        # If she has a preference (even a least-bad preference) she'll strip that down first.
        if self.get_opinion_score("showing her tits") > self.get_opinion_score("showing her ass"):
            clothing = self.outfit.remove_random_any(exclude_feet = True, exclude_lower = True, do_not_remove = True)
        elif self.get_opinion_score("showing her tits") < self.get_opinion_score("showing her ass"):
            clothing = self.outfit.remove_random_any(exclude_feet = True, exclude_upper = True, do_not_remove = True)
        if clothing is None: #Either our previous checks failed to produce anything OR they were equal
            clothing = self.outfit.remove_random_any(exclude_feet = True, do_not_remove = True)
        return clothing

    Person.choose_strip_clothing_item = choose_strip_clothing_item

    def run_move_enhanced(self,location):
        self.sexed_count = 0 #Reset the counter for how many times you've been seduced, you might be seduced multiple times in one day!

        if time_of_day == 0: #It's a new day, get a new outfit out to wear!
            if self.next_day_outfit:
                self.planned_outfit = self.next_day_outfit
                self.next_day_outfit = None
            else:
                self.planned_outfit = self.wardrobe.decide_on_outfit2(self)
            self.apply_outfit(self.planned_outfit)
            self.planned_uniform = None

        destination = self.schedule[time_of_day] #None destination means they have free time
        if destination == self.work and not mc.business.is_open_for_business(): #NOTE: Right now we give everyone time off based on when the mc has work scheduled.
            destination = None

        if destination is not None: #We have somewhere scheduled to be for this time chunk. Let's move over there.
            if self.schedule[time_of_day] == self.work: #We're going to work.
                if self.should_wear_uniform(): #Get a uniform if we should be wearing one.
                    self.wear_uniform()
                    self.change_happiness(self.get_opinion_score("work uniforms"),add_to_log = False)
                    # only changes sluttiness in low sluttiness range after that she won't care anymore
                    if self.sluttiness < 40 and self.planned_uniform and self.planned_uniform.slut_requirement > self.sluttiness*0.75: #A skimpy outfit/uniform is defined as the top 25% of a girls natural sluttiness.
                        self.change_slut_temp(self.get_opinion_score("skimpy uniforms"), add_to_log = False)

            elif not location is destination: # only change outfit if we change location
                self.apply_planned_outfit() #We're at home, so we can get back into our casual outfit.

            # some girls like to go out at night (bar or stripclub)
            if time_of_day == 4 and destination is self.home and renpy.random.randint(0, 100) <= 10:
                party_destinations = [downtown_bar]
                if "get_strip_club_foreclosed_stage" in globals():
                    if get_strip_club_foreclosed_stage() < 1 or get_strip_club_foreclosed_stage() >= 5: # only when stripclub is open for business
                        party_destinations.append(strip_club)
                    if mc.business.event_triggers_dict.get("strip_club_has_bdsm_room", False):
                        party_destinations.append(bdsm_room)
                else:
                    party_destinations.append(strip_club)

                location.move_person(self, get_random_from_list(party_destinations))
            else:
                # location might change outfit, so moved call to end of this loop
                location.move_person(self, destination) #Always go where you're scheduled to be.

        else:
            #She finds somewhere to burn some time
            if not location is destination: # only change outfit if we change location
                self.apply_planned_outfit() #Get changed back into our proper outfit if we aren't in it already.
            available_locations = [] #Check to see where is public (or where you are white listed) and move to one of those locations randomly
            for potential_location in list_of_places:
                if potential_location.public:
                    available_locations.append(potential_location)
            location.move_person(self, get_random_from_list(available_locations))

        #A skimpy outfit is defined as the top 25% of a girls natural sluttiness.
        if self.sluttiness < 40 and self.outfit and self.outfit.slut_requirement > self.sluttiness * 0.75:
            self.change_slut_temp(self.get_opinion_score("skimpy outfits"), add_to_log = False)

        #A conservative outfit is defined as the bottom 25% of a girls natural sluttiness.
        if self.sluttiness < 40 and self.outfit and self.outfit.slut_requirement < self.sluttiness * 0.25:
            # happiness won't go below 80 or over 120 by this trait and only affects in low sluttiness range, after that she won't care
            if self.happiness > 80 and self.happiness < 120:
                self.change_happiness(self.get_opinion_score("conservative outfits"), add_to_log = False)

        # lingerie only impacts to sluttiness level 40
        if self.sluttiness < 40 and self.outfit and (self.outfit.get_bra() or self.outfit.get_panties()):
            lingerie_bonus = 0
            if self.outfit.get_bra() and self.outfit.get_bra().slut_value > 1: #We consider underwear with an innate sluttiness of 2 or higher "lingerie" rather than just underwear.
                lingerie_bonus += self.get_opinion_score("lingerie")
            if self.outfit.get_panties() and self.outfit.get_panties().slut_value > 1:
                lingerie_bonus += self.get_opinion_score("lingerie")
            lingerie_bonus = __builtin__.int(lingerie_bonus/2.0)
            self.change_slut_temp(lingerie_bonus, add_to_log = False)

        # not wearing underwear only impacts sluttiness to level 60
        if self.sluttiness < 60 and self.outfit and (not self.outfit.wearing_bra() or not self.outfit.wearing_panties()): #We need to determine how much underwear they are not wearing. Each piece counts as half, so a +2 "love" is +1 slut per chunk.
            underwear_bonus = 0
            if not self.outfit.wearing_bra():
                underwear_bonus += self.get_opinion_score("not wearing underwear")
            if not self.outfit.wearing_panties():
                underwear_bonus += self.get_opinion_score("not wearing underwear")
            underwear_bonus = __builtin__.int(underwear_bonus/2.0) #I believe this rounds towards 0. No big deal if it doesn't, very minor detail.
            self.change_slut_temp(underwear_bonus, add_to_log = False)

        # showing the goods only impacts sluttiness to level 80
        if self.sluttiness < 80 and self.outfit and self.outfit.tits_visible():
            self.change_slut_temp(self.get_opinion_score("showing her tits"), add_to_log = False)
        if self.sluttiness < 80 and self.outfit and self.outfit.vagina_visible():
            self.change_slut_temp(self.get_opinion_score("showing her ass"), add_to_log = False)

        # showing everything only impacts sluttiness to level 80
        if self.sluttiness < 80 and self.outfit and self.outfit.full_access():
            self.change_slut_temp(self.get_opinion_score("not wearing anything"), add_to_log = False)

        for event_list in [self.on_room_enter_event_list, self.on_talk_event_list]: #Go through both of these lists and curate them, ie trim out events that should have expired.
            removal_list = [] #So we can iterate through without removing and damaging the list.
            for an_action in event_list:
                if isinstance(an_action, Limited_Time_Action): #It's a LTA holder, so it has a turn counter
                    an_action.turns_valid += -1
                    if an_action.turns_valid <= 0:
                        removal_list.append(an_action)

            for action_to_remove in removal_list:
                event_list.remove(action_to_remove)

    Person.run_move = run_move_enhanced

    # extend the default run day function
    def person_run_day_extended(org_func):
        def run_day_wrapper(person):
            # run original function
            org_func(person)
            # run extension code (clean up situational dictionaries)
            person.situational_sluttiness.clear()
            person.situational_obedience.clear()

        return run_day_wrapper

    # wrap up the run_day function
    Person.run_day = person_run_day_extended(Person.run_day)

    # BUGFIX: Remove suggest effect
    # Sometimes an effect is no longer in bag causing an exception, fix: check if effect exists before trying to remove
    def remove_suggest_effect_fixed(self, amount):
        self.change_suggest(- __builtin__.max(self.suggest_bag or [0])) #Subtract the max
        if amount in self.suggest_bag:
            self.suggest_bag.remove(amount)
        self.change_suggest(__builtin__.max(self.suggest_bag or [0])) # Add the new max. If we were max, it is now lower, otherwise it cancels out.

    Person.remove_suggest_effect = remove_suggest_effect_fixed

    ## ADD OPINION EXTENSION
    ## Adds add_opinion function to Person class
    def add_opinion(self, topic, degree, discovered = None, sexy_opinion = None, add_to_log = True): # Gives a message stating the opinion has been changed.
        if topic in self.opinions:  # we passed None for discovered so use existing discovered info
            if sexy_opinion is None:
                sexy_opinion = False
            if discovered is None:
                discovered = self.opinions[topic][1]

        if topic in self.sexy_opinions: # we passed None for discovered so use existing discovered info
            if sexy_opinion is None:
                sexy_opinion = True
            if discovered is None:
                discovered = self.sexy_opinions[topic][1]

        if discovered is None: # we didn't find any discovery information for opinion, so it's new and we passed None, so default set to false
            discovered = False
        if sexy_opinion is None:
            if topic in sexy_opinions_list: # We didn't find the topic in existing opinions for person, check global list if it is sexy
                sexy_opinion = True
            sexy_opinion = False

        if sexy_opinion:
            self.sexy_opinions[topic] = [degree, discovered]

            if topic not in sexy_opinions_list: # Appends to the opinion pool #TODO: should we add this to the game pool here? Prevents person specific opinions...
                sexy_opinions_list.append(topic)
        else:
            self.opinions[topic] = [degree, discovered]
            if topic not in opinions_list: # Appends to the opinion pool #TODO: should we add this to the game pool here? Prevents person specific opinions...
                opinions_list.append(topic)

        if add_to_log:
            mc.log_event((self.title or self.name) + " " + opinion_score_to_string(degree) + " " + str(topic), "float_text_green")

    # Adds a function that edits and adds opinions. It also appends to the vanilla opinion pool.
    Person.add_opinion = add_opinion

    def update_opinion_with_score(self, topic, score, add_to_log = True):
        if topic in sexy_opinions_list:
            if topic in self.sexy_opinions:
                self.sexy_opinions[topic][0] = score
            else:
                self.sexy_opinions[topic] = [score, add_to_log]

        if topic in opinions_list:
            if topic in self.opinions:
                self.opinions[topic][0] = score
            else:
                self.opinions[topic] = [score, add_to_log]

        if add_to_log:
            mc.log_event((self.title or self.name) + " " + opinion_score_to_string(score) + " " + str(topic), "float_text_green")
        return

    Person.update_opinion_with_score = update_opinion_with_score

    ## Increase the opinion on a specific topic (opinion)
    def increase_opinion_score(self, topic, max_value = 2, add_to_log = True):
        score = self.get_opinion_score(topic)

        if score < max_value:
            self.update_opinion_with_score(topic, score + 1, add_to_log)
        return

    # Add increase opinion function to person class
    Person.increase_opinion_score = increase_opinion_score

    ## Decrease the opinion on a specific topic (opinion)
    def decrease_opinion_score(self, topic, add_to_log = True):
        score = self.get_opinion_score(topic)

        if score > -2:
            self.update_opinion_with_score(topic, score - 1, add_to_log)
        return

    # Add decrease opinion function to person class
    Person.decrease_opinion_score = decrease_opinion_score

    ##Max the opinion on a specific topic (opinion)
    def max_opinion_score(self, topic, add_to_log = True):
        score = self.get_opinion_score(topic)
        if score != 2:
            self.update_opinion_with_score(topic, 2, add_to_log)
        return

    # Add max opinion function to person class
    Person.max_opinion_score = max_opinion_score

    # Change the sex skill of a person to specified score.
    def update_sex_skill(self, skill, score, add_to_log = True):
        if skill not in self.sex_skills:
            return

        current = self.sex_skills[skill]
        if current == score:
            return

        self.sex_skills[skill] = score
        if add_to_log:
            mc.log_event((self.title or self.name) + " " + skill.lower() + " skill is now at level " + str(score), "float_text_green")
        return

    Person.update_sex_skill = update_sex_skill

    # increase sex skill of person by one until max_value is reached.
    def increase_sex_skill(self, skill, max_value = 5, add_to_log = True):
        if skill not in self.sex_skills:
            return

        score = self.sex_skills[skill]
        if score < max_value:
            self.update_sex_skill(skill, score + 1, add_to_log)
        return

    Person.increase_sex_skill = increase_sex_skill

    # decrease sex skill of person by one while greater than zero.
    def decrease_sex_skill(self, skill, add_to_log = True):
        if skill not in self.sex_skills:
            return

        score = self.sex_skills[skill]
        if score > 0:
            self.update_sex_skill(skill, score - 1, add_to_log)
        return

    Person.decrease_sex_skill = decrease_sex_skill

    # Change Multiple Stats for a person at once (less lines of code, better readability)
    def change_stats(self, obedience = None, happiness = None, arousal = None, love = None, slut_temp = None, slut_core = None, add_to_log = True):
        if not obedience is None:
            self.change_obedience(obedience, add_to_log)
        if not happiness is None:
            self.change_happiness(happiness, add_to_log)
        if not arousal is None:
            self.change_arousal(arousal, add_to_log)
        if not love is None:
            self.change_love(love, add_to_log)
        if not slut_temp is None:
            self.change_slut_temp(slut_temp, add_to_log)
        if not slut_core is None:
            self.change_slut_core(slut_core, add_to_log)
        return

    Person.change_stats = change_stats

    # returns number of hearts of sluttiness for easy scene building.
    def sluttiness_tier(self):
        if self.sluttiness < 20:
            return 0
        if self.sluttiness < 40:
            return 1
        if self.sluttiness < 60:
            return 2
        if self.sluttiness < 80:
            return 3
        if self.sluttiness < 100:
            return 4
        else:
            return 5

    Person.sluttiness_tier = sluttiness_tier

    ## CHANGE WILLPOWER EXTENSION
    # changes the willpower of a person by set amount
    def change_willpower(self, amount): #Logs change in willpower and shows new total.
        self.willpower += amount
        if self.willpower < 0:
            self.willpower = 0
        return person.willpower

    # attach to person object
    Person.change_willpower = change_willpower

    def review_outfit_enhanced(self, dialogue = True):
        self.outfit.remove_all_cum()
        self.outfit.update_slut_requirement()

        if self.should_wear_uniform():
            self.wear_uniform() # Reset uniform
        elif self.outfit.slut_requirement > self.sluttiness:
            self.apply_planned_outfit()
            if dialogue:
                self.call_dialogue("clothing_review") # must be last call in function

    Person.review_outfit = review_outfit_enhanced

    def draw_person_enhanced(self,position = None, emotion = None, special_modifier = None, show_person_info = True, lighting = None, background_fill = "#0026a5", the_animation = None, animation_effect_strength = 1.0, character_placement = None, from_scene = False): #Draw the person, standing as default if they aren't standing in any other position.
        if position is None:
            position = self.idle_pose

        if position == "standing_doggy":
            position = "doggy"

        if emotion is None:
            emotion = self.get_emotion()

        if not can_use_animation():
            the_animation = None
        elif the_animation is None:
            the_animation = self.idle_animation

        if character_placement is None: # make sure we don't need to pass the position with each draw
            character_placement = character_right

        if lighting is None:
            lighting = mc.location.get_lighting_conditions()

        if not from_scene:
            renpy.scene("Active")
            if show_person_info:
                renpy.show_screen("person_info_ui",self)

        final_image = Flatten(self.build_person_displayable(position, emotion, special_modifier, lighting, background_fill))
        renpy.show(self.name + self.last_name,at_list=[character_placement, scale_person(self.height)],layer="Active",what=final_image,tag=self.name + self.last_name)

        if the_animation:
            global person_being_drawn
            person_being_drawn = self

            global current_draw_number
            current_draw_number += 1

            global prepared_animation_arguments
            prepared_animation_arguments = [the_animation, position, emotion, special_modifier, lighting, background_fill, animation_effect_strength, show_person_info, current_draw_number] #Effectively these are being stored and passed to draw_person_animation once take_animation_screenshot returns the surface
            renpy.invoke_in_thread(self.prepare_animation_screenshot_render, position, emotion, special_modifier, lighting, background_fill, current_draw_number) #This thread prepares the render. When it is finished it is caught by the interact_callback function take_animation_screenshot

    # replace the default draw_person function of the person class
    Person.draw_person = draw_person_enhanced
    # add location to store original personality
    Person.original_personality = None

    def draw_animated_removal_enhanced(self, the_clothing, position = None, emotion = None, special_modifier = None, lighting = None, background_fill = "#0026a5", the_animation = None, animation_effect_strength = 1.0, character_placement = None, scene_manager = None): #A special version of draw_person, removes the_clothing and animates it floating away. Otherwise draws as normal.
        #Note: this function includes a call to remove_clothing, it is not needed seperately.
        if position is None:
            position = self.idle_pose

        if position == "standing_doggy":
            position = "doggy"

        if emotion is None:
            emotion = self.get_emotion()

        if lighting is None:
            lighting = mc.location.get_lighting_conditions()

        if character_placement is None: # make sure we don't need to pass the position with each draw
            character_placement = character_right

        if not can_use_animation():
            the_animation = None
        elif the_animation is None:
            the_animation = self.idle_animation

        renpy.scene("Active") # clear layer for new draw action
        if scene_manager is None:
            renpy.show_screen("person_info_ui",self)
        else:   # when we are called from the scene manager we have to draw the other characters
            scene_manager.draw_scene_without(self)

        if the_animation:
            # Normally we would display a quick flat version, but we can assume we are already looking at the girl pre-clothing removal.
            bottom_displayable = Flatten(self.build_person_displayable(position, emotion, special_modifier, lighting, background_fill, no_frame = True)) #Get the starting image without the frame
            self.outfit.remove_clothing(the_clothing) #Remove the clothing
            top_displayable = Flatten(self.build_person_displayable(position, emotion, special_modifier, lighting, background_fill, no_frame = True)) #Get the top image without the frame

            x_size, y_size = position_size_dict.get(position)
            bottom_render = bottom_displayable.render(x_size, y_size, 0, 0)
            top_render = top_displayable.render(x_size, y_size, 0, 0)

            global current_draw_number
            current_draw_number += 1

            global prepared_animation_arguments
            prepared_animation_arguments = [the_animation, position, emotion, special_modifier, lighting, background_fill, animation_effect_strength, show_person_info, current_draw_number]

            global person_being_drawn
            person_being_drawn = self
            renpy.invoke_in_thread(self.prepare_animation_screenshot_render_multi, position, bottom_render, top_render, current_draw_number)

        else:
            bottom_displayable = Flatten(self.build_person_displayable(position, emotion, special_modifier, lighting, background_fill))
            self.outfit.remove_clothing(the_clothing)
            top_displayable = Flatten(self.build_person_displayable(position, emotion, special_modifier, lighting, background_fill))

            renpy.show(self.name+self.last_name+"_new", at_list=[character_placement, scale_person(self.height)], layer = "Active", what = top_displayable, tag = self.name + self.last_name +"_new")
            renpy.show(self.name+self.last_name+"_old", at_list=[character_placement, scale_person(self.height), clothing_fade], layer = "Active", what = bottom_displayable, tag = self.name + self.last_name +"_old")
        return

    Person.draw_animated_removal = draw_animated_removal_enhanced

    ####### Begin cum extension functions ######

    def cum_on_face_extended(org_func):
        def cum_on_face_wrapper(person):
            # run original function
            org_func(person)
            # run extension code
            mc.listener_system.fire_event("sex_cum_on_face", the_person = person)

        return cum_on_face_wrapper

    # wrap up the cum_on_face function
    Person.cum_on_face = cum_on_face_extended(Person.cum_on_face)

    def cum_on_tits_extended(org_func):
        def cum_on_tits_wrapper(person):
            # run original function
            org_func(person)
            # run extension code
            mc.listener_system.fire_event("sex_cum_on_tits", the_person = person)

        return cum_on_tits_wrapper

    # wrap up the cum_on_tits function
    Person.cum_on_tits = cum_on_tits_extended(Person.cum_on_tits)

    def cum_on_stomach_extended(org_func):
        def cum_on_stomach_wrapper(person):
            # run original function
            org_func(person)
            # run extension code
            mc.listener_system.fire_event("sex_cum_on_stomach", the_person = person)

        return cum_on_stomach_wrapper

    # wrap up the cum_on_stomach function
    Person.cum_on_stomach = cum_on_stomach_extended(Person.cum_on_stomach)

    def cum_on_ass_extended(org_func):
        def cum_on_ass_wrapper(person):
            # run original function
            org_func(person)
            # run extension code
            mc.listener_system.fire_event("sex_cum_on_ass", the_person = person)

        return cum_on_ass_wrapper

    # wrap up the cum_on_ass function
    Person.cum_on_ass = cum_on_ass_extended(Person.cum_on_ass)


##################
# Role Functions #
##################
    def is_employee(self):
        return self.has_role(employee_role)
    Person.is_employee = is_employee

    def has_role(self, role):
        if isinstance(role, basestring):
            return not find_in_list(lambda x: x.role_name == role, self.special_role) is None
        elif isinstance(role, list):
            return any(x in self.special_role for x in role)
        else:
            return role in self.special_role
    Person.has_role = has_role

    def add_role(self, role):
        added = False
        if not role in self.special_role:
            self.special_role.append(role)
            added = True

        # special situation if she gets girlfriend role, she loses affair role and SO
        if role is girlfriend_role:
            self.remove_role(affair_role)
            self.relationship = "Single" #Technically they aren't "single", but the MC has special roles for their girlfriend.
            self.SO_name = None

        return added
    Person.add_role = add_role

    def remove_role(self, role):
        if role in self.special_role:
            self.special_role.remove(role)
            return True
        return False
    Person.remove_role = remove_role

################################################
# Outfit functions - wear a specialized outfit #
################################################

    def apply_gym_outfit(self):
        # get personal copy of outfit, so we don't change the gym wardrobe (in any events)
        self.apply_outfit(workout_wardrobe.decide_on_outfit2(self).get_copy())
        return

    Person.apply_gym_outfit = apply_gym_outfit

    def apply_university_outfit(self):
        # get personal copy of outfit, so we don't change the university wardrobe (in any events)
        self.apply_outfit(university_wardrobe.decide_on_outfit2(self).get_copy())
        return

    Person.apply_university_outfit = apply_university_outfit

    def apply_planned_outfit(self):
        if self.should_wear_uniform():
            self.wear_uniform()
        else:
            self.apply_outfit(self.planned_outfit)
        return

    Person.apply_planned_outfit = apply_planned_outfit

######################################
# Extend give serum for added goal #
######################################

    def give_serum_extended(org_func):
        def give_serum_wrapper(person, the_serum_design, add_to_log = True):
            # run original function
            org_func(person, the_serum_design, add_to_log)
            # run extension code
            mc.listener_system.fire_event("give_random_serum", the_person = person)

        return give_serum_wrapper

    # wrap up the give_serum function
    Person.give_serum = give_serum_extended(Person.give_serum)


#######################################
# HELPER METHODS FOR CLASS EXTENSIONS #
#######################################

    # calculates current player mental powers
    def player_willpower():
        mc.power = 0

        mc.power += __builtin__.int(mc.charisma*5) # Positive character modifiers
        mc.power += __builtin__.int((mc.energy / 20) * 1.5)
        return mc.power

    # calculates current willpower of a person
    def calculate_willpower(person):
        willpower = __builtin__.int(person.focus * 10 + person.happiness * 0.2 - person.obedience * 0.1 - person.love * 0.2 - person.suggestibility * 0.5)

        if willpower < 0:
            willpower = 0
        return willpower

    # log will power to event log in ui
    def log_willpower(person):
        if (person is mc):
            message = "Your: " + str(person.power)
        else:
            message = (person.title or person.name) + ": " + str(person.willpower)
        message += " Willpower"
        mc.log_event(message, "float_text_blue")
        return

#########################################
# Add hash (unique id) to Person object #
#########################################

    def person__hash__(self):
        return hash((self.name, self.last_name, self.age))

    Person.__hash__ = person__hash__
    Person.hash = person__hash__

    def person__eq__(self, other):
        if isinstance(self, other.__class__):
            return hash((self.name, self.last_name, self.age)) == hash((other.name, other.last_name, other.age))
        return False

    Person.__eq__ = person__eq__

    def person__ne__(self, other):
        if isinstance(self, other.__class__):
            return hash((self.name, self.last_name, self.age)) != hash((other.name, other.last_name, other.age))
        return True

    Person.__ne__ = person__ne__

##########################################
# Expose outfit methods on Person object #
##########################################
    # many coding errors are related to missing .oufit in the sequence to check a persons state based on her outfit
    # these extension methods on the Person class just redirect it to the outfit class, so the code still works as intended

    def person_tits_available(self):
        return self.outfit.tits_available()

    Person.tits_available = person_tits_available

    def person_tits_visible(self):
        return self.outfit.tits_visible()

    Person.tits_visible = person_tits_visible

    def person_vagina_available(self):
        return self.outfit.vagina_available()

    Person.vagina_available = person_vagina_available

    def person_vagina_visible(self):
        return self.outfit.vagina_visible()

    Person.vagina_visible = person_vagina_visible

    def person_underwear_visible(self):
        return self.outfit.underwear_visible()

    Person.underwear_visible = person_underwear_visible

    def person_wearing_bra(self):
        return self.outfit.wearing_bra()

    Person.wearing_bra = person_wearing_bra

    def person_wearing_panties(self):
        return self.outfit.wearing_panties()

    Person.wearing_panties = person_wearing_panties

    def person_bra_covered(self):
        return self.outfit.bra_covered()

    Person.bra_covered = person_bra_covered

    def person_panties_covered(self):
        return self.outfit.panties_covered()

    Person.panties_covered = person_panties_covered

    def person_has_mouth_cum(self):
        return self.outfit.has_mouth_cum()

    Person.has_mouth_cum = person_has_mouth_cum

    def person_has_tits_cum(self):
        return self.outfit.has_tits_cum()

    Person.has_tits_cum = person_has_tits_cum

    def person_has_stomach_cum(self):
        return self.outfit.has_stomach_cum()

    Person.has_stomach_cum = person_has_stomach_cum

    def person_has_face_cum(self):
        return self.outfit.has_face_cum()

    Person.has_face_cum = person_has_face_cum

    def person_has_ass_cum(self):
        return self.outfit.has_ass_cum()

    Person.has_ass_cum = person_has_ass_cum

    def person_has_creampie_cum(self):
        return self.outfit.has_creampie_cum()

    Person.has_creampie_cum =person_has_creampie_cum

##########################################
# Unique crisis addition functions       #
##########################################
    # Use these extensions to add only unique crisis. Checks to see if the event has already been added, so it won't duplicate.
    def add_unique_on_talk_event(self, the_crisis):
        if the_crisis not in self.on_talk_event_list:
            self.on_talk_event_list.append(the_crisis)
    Person.add_unique_on_talk_event = add_unique_on_talk_event

    def add_unique_on_room_enter_event(self, the_crisis):
        if the_crisis not in self.on_room_enter_event_list:
            self.on_room_enter_event_list.append(the_crisis)
    Person.add_unique_on_room_enter_event = add_unique_on_room_enter_event

    def remove_on_talk_event(self, the_crisis):
        if isinstance(the_crisis, basestring):
            found = find_in_list(lambda x: x.effect == the_crisis, self.on_talk_event_list)
            if found:
                self.on_talk_event_list.remove(found)

        if the_crisis in self.on_talk_event_list:
            self.on_talk_event_list.remove(the_crisis)
    Person.remove_on_talk_event = remove_on_talk_event

    def remove_on_room_enter_event(self, the_crisis):
        if isinstance(the_crisis, basestring):
            found = find_in_list(lambda x: x.effect == the_crisis, self.on_room_enter_event_list)
            if found:
                self.on_room_enter_event_list.remove(found)

        if the_crisis in self.on_room_enter_event_list:
            self.on_room_enter_event_list.remove(the_crisis)
    Person.remove_on_room_enter_event = remove_on_room_enter_event

##########################################
# Pregnancy Functions                    #
##########################################

    def is_pregnant(self):
        if self.has_role(pregnant_role):
            return True
        return False
    Person.is_pregnant = is_pregnant

    def knows_pregnant(self):
        if self.is_pregnant():
            return self.event_triggers_dict.get("preg_knows", False)
        return False
    Person.knows_pregnant = knows_pregnant

    def is_lactating(self):
        if self.lactation_sources > 0:
            return True
        return False
    Person.is_lactating = is_lactating

    def get_due_day(self):
        if self.is_pregnant():
            return self.event_triggers_dict.get("preg_finish_announce_day", 0)
        return -1
    Person.get_due_day = get_due_day

    def pregnancy_is_visible(self):
        if self.is_pregnant():
            return day > self.pregnancy_show_day()
        return False
    Person.pregnancy_is_visible = pregnancy_is_visible

    def pregnancy_show_day(self):
        if self.is_pregnant():
            return self.event_triggers_dict.get("preg_transform_day", 0)
        return -1
    Person.pregnancy_show_day = pregnancy_show_day

    def is_mc_father(self):
        return self.event_triggers_dict.get("preg_mc_father", True)
    Person.is_mc_father = is_mc_father

    def is_highly_fertile(self):
        if self.is_pregnant():
            return False
        if persistent.pregnancy_pref < 2:
            return False
        day_difference = __builtin__.abs((day % 30) - self.ideal_fertile_day) # Gets the distance between the current day and the ideal fertile day.
        if day_difference > 15:
            day_difference = 30 - day_difference #Wrap around to get correct distance between months.
        if day_difference < 4:
            return True
        return False

    Person.is_highly_fertile = is_highly_fertile

    def effective_fertility_percent(self):
        if persistent.pregnancy_pref == 2: # On realistic pregnancy a girls chance to become pregnant fluctuates over the month.
            day_difference = abs((day % 30) - self.ideal_fertile_day) # Gets the distance between the current day and the ideal fertile day.
            if day_difference > 15:
                day_difference = 30 - day_difference #Wrap around to get correct distance between months.
            multiplier = 2 - (float(day_difference)/10.0) # The multiplier is 2 when the day difference is 0, 0.5 when the day difference is 15.
            modified_fertility = self.fertility_percent * multiplier
        else:
            modified_fertility = self.fertility_percent        
        return modified_fertility

    Person.effective_fertility_percent = effective_fertility_percent