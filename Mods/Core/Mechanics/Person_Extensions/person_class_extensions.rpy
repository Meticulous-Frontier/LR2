init -1 python:
    import hashlib

    def remove_person_from_game(self):
        my_location = self.location
        if my_location:
            my_location.remove_person(self) # remove person from current location
        if self.home in list_of_places:
            # only remove home when not 'dungeon' or any other character has same home location
            if not self.home == dungeon and not any(x.home == self.home for x in known_people_in_the_game(excluded_people = [self])):
                list_of_places.remove(self.home) # remove home location from list_of_places
        if self.home in mc.known_home_locations:
            mc.known_home_locations.remove(self.home) # remove home location from known_home_locations

        if "people_to_process" in globals():
            found = find_in_list(lambda x: x[0].identifier == self.identifier, people_to_process)
            if found: # remove from processing list
                people_to_process.remove(found)

        # cleanup crisis events where person is in argument list
        for crisis_store in [mc.business.mandatory_crises_list, mc.business.mandatory_morning_crises_list]:
            for crisis in crisis_store[:]:
                args = crisis.args
                if not isinstance(args, list):
                    args = [args]

                if any(x for x in args if x == self):
                    crisis_store.remove(crisis)

        # remove from business teams
        for team in [mc.business.research_team, mc.business.market_team, mc.business.supply_team, mc.business.production_team, mc.business.hr_team]:
            if self in team:
                team.remove(self)

        # remove from business rooms
        for room in [mc.business.s_div, mc.business.r_div, mc.business.p_div, mc.business.m_div, mc.business.h_div]:
            if self in room.people:
                room.remove_person(self)

        # remove from strippers
        if self in stripclub_strippers:
            stripclub_strippers.remove(self)

        # other stripclub teams
        if "stripclub_bdsm_performers" in globals():
            for team in [stripclub_bdsm_performers, stripclub_waitresses]:
                if self in team:
                    team.remove(self)

        # remove from relationships array
        town_relationships.remove_all_relationships(self)

        self.base_outfit = None
        self.planned_outfit = None
        self.planned_uniform = None

        if self.wardrobe:
            for outfit in self.wardrobe.all_outfits:
                outfit.upper_body.clear()
                outfit.lower_body.clear()
                outfit.feet.clear()
                outfit.accessories.clear()
            self.wardrobe.outfits.clear()
            self.wardrobe.underwear_sets.clear()
            self.wardrobe.overwear_sets.clear()
            self.wardrobe = None

        if self.special_role:
            self.special_role.clear()
        if self.on_room_enter_event_list:
            self.on_room_enter_event_list.clear()
        if self.on_talk_event_list:
            self.on_talk_event_list.clear()
        if self.event_triggers_dict:
            self.event_triggers_dict.clear()
        if self.suggest_bag:
            self.suggest_bag.clear()
        if self.broken_taboos:
            self.broken_taboos.clear()
        if self.sex_record:
            self.sex_record.clear()
        if self.opinions:
            self.opinions.clear()
        if self.sexy_opinions:
            self.sexy_opinions.clear()

        # clear all references held by person object.
        self.schedule = None
        self.override_schedule = None
        self.home = None
        self.job = None
        self.relationship = None
        self.personality = None
        self.char = None
        self.body_images = None
        self.face_style = None
        #self.expression_images = None
        self.hair_colour = None
        self.hair_style = None
        self.pubes_style = None
        self.skin = None
        self.eyes = None
        self.serum_effects = None
        self.personal_region_modifiers = None
        self.situational_sluttiness = None
        self.situational_obedience = None
        # now let the Garbage Collector do the rest (we are no longer referenced in any objects).
        return

    Person.remove_person_from_game = remove_person_from_game

    @property
    def location(self): # Check what location a person is in e.g the_person.location == downtown. Use to trigger events?
        location = next((x for x in list_of_places if self in x.people), None)
        return (location if location else (self.home or downtown)) # fallback location for person is home else downtown

    Person.location = location

    def person_change_location(self, destination):
        self.location.move_person(self, destination)

    Person.change_location = person_change_location

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
            self._identifier = hashlib.md5(self.name + self.last_name + str(self.age)).hexdigest()
        return self._identifier

    # add follow_mc attribute to person class (without sub-classing)
    Person.identifier = property(get_person_identifier, None, None, "Unique identifier for person class.")

    # generic function to get a person by it's identifier
    def get_person_by_identifier(identifier):
        return next((x for x in all_people_in_the_game() if x.identifier == identifier), None)

    def get_person_bedroom(self):
        if not hasattr(self, "_bedroom"):
            if self.has_role(prostitute_role):
                self._bedroom = prostitute_bedroom
            else:
                self._bedroom = renpy.random.choice([generic_bedroom_1, generic_bedroom_2, generic_bedroom_3, generic_bedroom_4])
        return self._bedroom
    Person.bedroom = property(get_person_bedroom, None, None, "Her bedroom")

    # use dedicated locations, since each location has different objects
    def change_to_person_bedroom(self):
        mc.change_location(self.bedroom)
        mc.location.show_background()
        return

    Person.change_to_bedroom = change_to_person_bedroom

    # use dedicated locations, since each location has different objects
    def change_to_person_hallway(self):
        mc.change_location(her_hallway) # use generic hallway
        mc.location.show_background()
        return

    Person.change_to_hallway = change_to_person_hallway

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

    def get_person_is_patreon(self):
        if not hasattr(self, "_is_patreon"):
            self._is_patreon = False
        return self._is_patreon

    def set_person_is_patreon(self, value):
        self._is_patreon = value

    Person.is_patreon = property(get_person_is_patreon, set_person_is_patreon, None, "Identify person as Patreon reward character.")

    # work-outfit for strippers / waitresses and bdsm room performers

    def get_person_maid_outfit(self):
        if not hasattr(self, "_maid_outfit"):
            self._maid_outfit = None
        return self._maid_outfit

    def set_person_maid_outfit(self, value):
        self._maid_outfit = value

    def del_person_maid_outfit(self):
        del self._maid_outfit

    Person.maid_outfit = property(get_person_maid_outfit, set_person_maid_outfit, del_person_maid_outfit, "Store maid outfit for the day.")

    def get_person_location_outfit(self):
        if not hasattr(self, "_location_outfit"):
            self._location_outfit = None
        return self._location_outfit

    def set_person_location_outfit(self, value):
        self._location_outfit = value

    def del_person_location_outfit(self):
        del self._location_outfit

    Person.location_outfit = property(get_person_location_outfit, set_person_location_outfit, del_person_location_outfit, "Store outfit for specific location (only valid 1 timeslot).")

    # change idle position based on location
    def get_person_idle_pose(self):
        if not "downtown_bar" in globals(): # skip this when running tutorial
            return self._idle_pose

        if not hasattr(self, "_idle_pose"):
            self._idle_pose = renpy.random.choice(["stand2","stand3","stand4","stand5"])

        if renpy.call_stack_depth() < 2:
            # we are in the main menu (alternative idle_pose)
            if (self.is_employee() and self.is_at_work()) or self.location == downtown_bar:
                return "sitting"
            if self.location == gym:
                pose = self.event_triggers_dict.get("gym_pose", None)
                if not pose: # store preferred position in bdsm room (prevent switching on hover)
                    pose = renpy.random.choice(["missionary", "stand2", "back_peek", "stand4", "sitting"])
                    self.event_triggers_dict["gym_pose"] = pose
                return pose

        if self.has_role(caged_role):
            pose = self.event_triggers_dict.get("bdsm_room_pose", None)
            if not pose: # store preferred position in bdsm room (prevent switching on hover)
                pose = renpy.random.choice(["cowgirl", "kneeling1", "blowjob"])
                self.event_triggers_dict["bdsm_room_pose"] = pose
            return pose
        return self._idle_pose

    def set_person_idle_pose(self, value):
        self._idle_pose = value

    Person.idle_pose = property(get_person_idle_pose, set_person_idle_pose, None, "Overrides default idle pose behavior.")

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

    def get_person_tan_style(self):
        if not hasattr(self, "_tan_style"):
            self._tan_style = None
        return self._tan_style

    def set_person_tan_style(self, value):
        self._tan_style = value

    Person.tan_style = property(get_person_tan_style, set_person_tan_style, None, "The tan style to render for a person.")

    def get_person_available(self):
        if not hasattr(self, "_available"):
            self._available = True
        return self._available

    def set_person_available(self, value):
        self._available = value

    Person.available = property(get_person_available, set_person_available, None, "Mark a person available or not.")

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
        #self.expression_images = Expression("default", self.skin, self.face_style)
        return
    Person.match_skin = match_skin

    ## SET HAIRSTYLE VIA Clothing ITEM, maintain color etc.

    def set_hair_style(self, new_clothing):
        cs = renpy.current_screen()
        self.hair_style = new_clothing.get_copy()

        if cs:
            self.hair_colour = [cs.scope["selected_hair_colour_name"], [cs.scope["current_r"], cs.scope["current_g"], cs.scope["current_b"], cs.scope["current_a"]]]

    Person.set_hair_style = set_hair_style

    # SET PUBIC STYLE Clothing ITEM

    def set_pubic_style(self, new_clothing):
        cs = renpy.current_screen()
        self.pubes_style = new_clothing.get_copy()

        if cs:
            self.hair_colour = [cs.scope["selected_hair_colour_name"], [cs.scope["current_r"], cs.scope["current_g"], cs.scope["current_b"], cs.scope["current_a"]]]

    Person.set_pubic_style = set_pubic_style

    def person_pubes_description_string(self):
        if self.pubes_style == shaved_pubes:
            return "bald"
        if self.pubes_style == landing_strip_pubes:
            return "brazilian waxed"
        if self.pubes_style == default_pubes:
            return "hairy"
        return "neatly trimmed"

    Person.pubes_description = property(person_pubes_description_string, None, None, "Property that returns pussy pubes description for use in dialogs.")

    def person_tits_description_string(self):
        rank = self.rank_tits(self.tits)
        adjective = "perky"
        descriptor = "tits"

        if rank == 0:
            adjective = renpy.random.choice(["flat", "minute", "tiny"])
            descriptor = renpy.random.choice(["titties", "tits", "nipples"])
        elif rank >= 1 and rank <= 3:
            adjective = renpy.random.choice(["firm", "perky", "small"])
            descriptor = renpy.random.choice(["breasts", "tits", "boobs"])
        elif rank >= 4 and rank <= 6:
            adjective = renpy.random.choice(["shapely", "large", "big", "generous"])
            descriptor = renpy.random.choice(["breasts", "tits", "bosoms"])
        elif rank >= 7 and rank <= 9:
            adjective = renpy.random.choice(["large", "voluptuous", "colossal", "huge"])
            descriptor = renpy.random.choice(["breasts", "tits", "jugs", "melons"])

        return "{adj} {desc}".format(adj = adjective, desc = descriptor)

    Person.tits_description = property(person_tits_description_string, None, None, "Property that returns tits description for use in dialogs.")

    def person_formal_address(self):
        if self.job == nora_professor_job:
            return "Professor"
        if self.job in [doctor_job]:
            return "Doctor"
        if self.relationship == "Married":
            return "Mrs."
        elif self.age > 30:
            return "Ms."
        return "Miss"

    Person.formal_address = property(person_formal_address, None, None, "Property that returns Miss, Ms. or Mrs. based on age / martial status.")

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
            self.height = upper_limit

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
        happy_points += max(-20, self.obedience - 90) #A more obedient character is more likely to stay, even if they're unhappy. Even highly independant girls will stay if they are happy and/or paid well
        happy_points += self.salary - self.calculate_base_salary() #A real salary greater than her base is a bonus, less is a penalty. TODO: Make this dependent on salary fraction, not abosolute pay.
        happy_points += self.get_opinion_score("working") * 5 # Does she like working? It affects her happiness score.

        if self.days_employed < 14:
            happy_points += 14 - self.days_employed #Employees are much less likely to quit over the first two weeks.
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

    def generate_daughter_enhanced(self, force_live_at_home = False): #Generates a random person who shares a number of similarities to the mother
        age = renpy.random.randint(18, self.age-16)

        if renpy.random.randint(0,100) < 60:
            if self.has_role(pregnant_role):
                body_type = self.event_triggers_dict.get("pre_preg_body", None)
            else:
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
            if self.has_role(pregnant_role):
                tits = self.event_triggers_dict.get("pre_preg_tits", None)
            else:
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

        if force_live_at_home or renpy.random.randint(0,100) < 85 - age: #It is less likely she lives at home the older she is.
            start_home  = self.home
        else:
            start_home  = None


        the_daughter = make_person(last_name = self.last_name, age = age, body_type = body_type, face_style = face_style, tits = tits, height = height,
            hair_colour = hair_colour, skin = self.skin, eyes = eyes, start_home = start_home, force_random = True)

        if start_home is None:
            the_daughter.generate_home()
        else:
            the_daughter.set_schedule(the_location = start_home, the_times = [0,4])

        the_daughter.home.add_person(the_daughter)

        for sister in town_relationships.get_existing_children(self): #First find all of the other kids this person has
            town_relationships.update_relationship(the_daughter, sister, "Sister") #Set them as sisters

        town_relationships.update_relationship(self, the_daughter, "Daughter", "Mother") #Now set the mother/daughter relationship (not before, otherwise she's a sister to herself!)

        return the_daughter

    Person.generate_daughter = generate_daughter_enhanced

    def generate_mother_enhanced(self, lives_with_daughter = False): #Generates a random person who shares a number of similarities to the mother
        age = renpy.random.randint(self.age + 16, 55)

        if renpy.random.randint(0,100) < 60:
            if self.has_role(pregnant_role):
                body_type = self.event_triggers_dict.get("pre_preg_body", None)
            else:
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
            if self.has_role(pregnant_role):
                tits = self.event_triggers_dict.get("pre_preg_tits", None)
            else:
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
        else:
            the_mother.set_schedule(the_location = start_home, the_times = [0,4])

        the_mother.home.add_person(the_mother)

        for sister in town_relationships.get_existing_sisters(self): #First find all of the sisters this person has
            town_relationships.update_relationship(the_mother, sister, "Daughter", "Mother") #Set the mother/daughter relationship for the sisters
            the_mother.kids += 1 # increase child count per sister

        town_relationships.update_relationship(self, the_mother, "Mother", "Daughter") #Now set the mother/daughter relationship with person

        return the_mother

    Person.generate_mother = generate_mother_enhanced

    def person_is_willing(self, the_position, private = True, ignore_taboo = False):
        final_slut_requirement, final_slut_cap = the_position.calculate_position_requirements(self, ignore_taboo)
        # DON'T USE EFFECTIVE SLUTTINESS IN THIS FUNCTION
        # IT CAN HAVE THE MODIFIERS THAT THIS FUNCTION EMULATES
        # TO VALIDATE PRIOR TO ACTUALLY STARTING THE SEX LOOP
        # IT VALIDATES IF SHE IS WILLING BY HERSELF (NOT USING OBEDIENCE)

        # quick return if she hates any required opinion tags for the position
        for tag in the_position.opinion_tags:
            if self.get_opinion_score(tag) <= -2:
                return False

        # add modifiers
        if self.has_family_taboo():
            final_slut_requirement += (self.get_opinion_score("incest") - 2) * 5          # love incest negates requirement penalty

        if self.has_role(prostitute_role):
            final_slut_requirement -= 20        # prostitutes are more willing by nature
        elif self.relationship == "Girlfriend":
            final_slut_requirement -= (self.get_opinion_score("cheating on men") - 2) * 2  # love negates requirement penalty
        elif self.relationship == "Fiancée":
            final_slut_requirement -= (self.get_opinion_score("cheating on men") - 2) * 3  # love negates requirement penalty
        elif self.relationship == "Married":
            final_slut_requirement -= (self.get_opinion_score("cheating on men") - 2) * 5 # love negates requirement penalty

        if not private:
            multiplier = 5 if self.sluttiness < 50 else 2
            final_slut_requirement -= (self.get_opinion_score("public sex") - 2) * multiplier # love negates requirement penalty

        if self.love < 0:
            final_slut_requirement += self.love
        elif private:
            if self.has_role([girlfriend_role, affair_role]):               # girlfriend lowers requirement by love
                final_slut_requirement -= self.love
            elif self.is_family():
                final_slut_requirement -= __builtin__.int(self.love / 4.0)  # family lowers requirement by love / 4
            else:
                final_slut_requirement -= __builtin__.int(self.love / 2.0)  # default lowers requirement by love / 2

        final_slut_requirement -= __builtin__.min(__builtin__.int((self.happiness - 100)/4.0), 20) # happiness can lower requirement by up to 20 points

        if not ignore_taboo and the_position.associated_taboo:
            final_slut_requirement += 10    # taboo increases requirement by 10

        print("Position: " + the_position.name + "[Sluttiness: " + str(self.sluttiness) + ", Required: " + str(final_slut_requirement) + "]")
        if self.sluttiness >= final_slut_requirement:
            return True
        return False

    Person.is_willing = person_is_willing

    ## STRIP OUTFIT TO MAX SLUTTINESS EXTENSION
    # Strips down the person to a clothing their are comfortable with (starting with top, before bottom)
    # narrator_messages: narrator voice after each item of clothing stripped, use '[person.<title>]' for titles and '[strip_choice.name]' for clothing item.
        # Can be an array of messages for variation in message per clothing item or just a single string or None for silent stripping
    # scene manager parameter is filled from that class so that all people present in scene are drawn
    def strip_outfit_to_max_sluttiness(self, top_layer_first = True, exclude_upper = False, exclude_lower = False, exclude_feet = True, delay = 1, narrator_messages = None, display_transform = None, lighting = None, temp_sluttiness_boost = 0, position = None, emotion = None, scene_manager = None, wipe_scene = False):
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
        # renpy.say(None, strip_choice.name + "  (required: " + str(test_outfit.slut_requirement) +  ", sluttiness: " +  str(self.effective_sluttiness() + temp_sluttiness_boost) + ")")
        while strip_choice and self.judge_outfit(test_outfit, temp_sluttiness_boost):
            if delay > 0:
                self.draw_animated_removal(strip_choice, display_transform = display_transform, position = position, emotion = emotion, lighting = lighting, scene_manager = scene_manager, wipe_scene = wipe_scene) #Draw the strip choice being removed from our current outfit
                if msg_count == 0:
                    renpy.pause(delay) # if no message to show, wait a short while before automatically continue stripping
            else:
                test_outfit.remove_clothing(strip_choice)
            self.apply_outfit(test_outfit, ignore_base = True) #Swap our current outfit out for the test outfit.
            removed_something = True
            if msg_count > 0:   # do we need to show a random message and replace titles and outfit name
                msg_idx = renpy.random.randint(1, msg_count)
                msg = messages[msg_idx - 1]
                msg = msg.replace("[the_person.possessive_title]", self.possessive_title or "the unknown woman").replace("[the_person.title]", self.title or self.name).replace("[the_person.mc_title]", self.mc_title).replace("[strip_choice.name]", strip_choice.name).replace("[strip_choice.display_name]", strip_choice.display_name)
                renpy.say(None, msg)

            strip_choice = get_strip_choice_max(test_outfit, top_layer_first, exclude_upper, exclude_lower, exclude_feet)

        return removed_something

    # Monkey wrench Person class to have automatic strip function
    Person.strip_outfit_to_max_sluttiness = strip_outfit_to_max_sluttiness

    def strip_outfit_strip_list(self, strip_list, position = None, emotion = None, display_transform = None, lighting = None, scene_manager = None, wipe_scene = False, half_off_instead = False, delay = 1):
        if position is None:
            self.position = self.idle_pose

        if emotion is None:
            self.emotion = self.get_emotion()

        if lighting is None:
            lighting = mc.location.get_lighting_conditions()

        if display_transform is None:
            display_transform = character_right

        for item in strip_list:
            if delay > 0:
                self.draw_animated_removal(item, display_transform = display_transform, position = position, emotion = emotion, lighting = lighting, half_off_instead = half_off_instead, scene_manager = scene_manager, wipe_scene = wipe_scene) #Draw the strip choice being removed from our current outfit
                renpy.pause(delay)
            else:
                self.outfit.remove_clothing(item)
        return

    Person.strip_outfit_strip_list = strip_outfit_strip_list

    def strip_to_underwear(self, visible_enough = True, avoid_nudity = False, position = None, emotion = None, display_transform = None, lighting = None, scene_manager = None, wipe_scene = False, delay = 1):
        strip_list = self.outfit.get_underwear_strip_list(visible_enough = visible_enough, avoid_nudity = avoid_nudity)
        self.strip_outfit_strip_list(strip_list, position = position, emotion = emotion, display_transform = display_transform, lighting = lighting, scene_manager = scene_manager, wipe_scene = wipe_scene, delay = delay)
        return

    Person.strip_to_underwear = strip_to_underwear

    def strip_to_tits(self, visible_enough = True, prefer_half_off = False, position = None, emotion = None, display_transform = None, lighting = None, scene_manager = None, wipe_scene = False, delay = 1):
        half_off_instead = False
        if prefer_half_off and self.outfit.can_half_off_to_tits(visible_enough = visible_enough):
            strip_list = self.outfit.get_half_off_to_tits_list(visible_enough = visible_enough)
            half_off_instead = True
        else:
            strip_list = self.outfit.get_tit_strip_list(visible_enough = visible_enough)
        self.strip_outfit_strip_list(strip_list, position = position, emotion = emotion, display_transform = display_transform, lighting = lighting, half_off_instead = half_off_instead, scene_manager = scene_manager, wipe_scene = wipe_scene, delay = delay)
        return

    Person.strip_to_tits = strip_to_tits

    def strip_to_vagina(self, visible_enough = False, prefer_half_off = False, position = None, emotion = None, display_transform = None, lighting = None, scene_manager = None, wipe_scene = False, delay = 1):
        half_off_instead = False
        if prefer_half_off and self.outfit.can_half_off_to_vagina():
            strip_list = self.outfit.get_half_off_to_vagina_list(visible_enough = visible_enough)
            half_off_instead = True
        else:
            strip_list = self.outfit.get_vagina_strip_list(visible_enough = visible_enough)
        self.strip_outfit_strip_list(strip_list, position = position, emotion = emotion, display_transform = display_transform, lighting = lighting, half_off_instead = half_off_instead, scene_manager = scene_manager, wipe_scene = wipe_scene, delay = delay)
        return

    Person.strip_to_vagina = strip_to_vagina

    def strip_full_outfit(self, strip_feet = False, strip_accessories = False, position = None, emotion = None, display_transform = None, lighting = None, scene_manager = None, wipe_scene = False, delay = 1):
        strip_list = self.outfit.get_full_strip_list(strip_feet = strip_feet, strip_accessories = strip_accessories)
        self.strip_outfit_strip_list(strip_list, position = position, emotion = emotion, display_transform = display_transform, lighting = lighting, scene_manager = scene_manager, wipe_scene = wipe_scene, delay = delay)
        return

    Person.strip_full_outfit = strip_full_outfit

    def strip_outfit(self, top_layer_first = True, exclude_upper = False, exclude_lower = False, exclude_feet = True, delay = 1, display_transform = None, position = None, emotion = None, lighting = None, scene_manager = None, wipe_scene = False):
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

        if display_transform is None:
            display_transform = character_right

        strip_choice = self.outfit.remove_random_any(top_layer_first, exclude_upper, exclude_lower, exclude_feet, do_not_remove = True)
        while not strip_choice is None and extra_strip_check(self, top_layer_first, exclude_upper, exclude_lower, exclude_feet):
            if delay > 0:
                self.draw_animated_removal(strip_choice, display_transform = display_transform, position = position, emotion = emotion, lighting = lighting, scene_manager = scene_manager, wipe_scene = wipe_scene) #Draw the strip choice being removed from our current outfit
                renpy.pause(delay)
            else:
                self.outfit.remove_clothing(strip_choice)
            strip_choice = self.outfit.remove_random_any(top_layer_first, exclude_upper, exclude_lower, exclude_feet, do_not_remove = True)

        # special case where she is wearing a two-part item that blocks her vagina, but we need it be available
        if not exclude_lower and not self.outfit.vagina_available():
            strip_choice = self.outfit.remove_random_any(top_layer_first, False, exclude_lower, exclude_feet, do_not_remove = True)
            while not strip_choice is None:
                if delay > 0:
                    self.draw_animated_removal(strip_choice, display_transform = display_transform, position = position, emotion = emotion, lighting = lighting, scene_manager = scene_manager, wipe_scene = wipe_scene) #Draw the strip choice being removed from our current outfit
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

    def person_get_destination_extended(org_func):
        def get_destination_wrapper(person, specified_day = None, specified_time = None):
            if not person.available:  # special case to make people disappear (used in pregnancy)
                return purgatory

            # run original function
            return org_func(person, specified_day, specified_time)

        return get_destination_wrapper

    # wrap up the run_day function
    Person.get_destination = person_get_destination_extended(Person.get_destination)

    def run_move_enhanced(self,location):
        for serum in self.serum_effects: #Compute the effects of all of the serum that the girl is under.
            serum.run_on_move(self) #Run the serum's on_move function if one exists

        self.sexed_count = 0 #Reset the counter for how many times you've been seduced, you might be seduced multiple times in one day!
        self.location_outfit = None # Clear the current location outfit (only valid 1 timeslot)

        if time_of_day == 0: #Change outfit here, because crisis events might be triggered after run day function
            if self.next_day_outfit:
                self.planned_outfit = self.next_day_outfit
                self.next_day_outfit = None
            else:
                self.planned_outfit = None
            self.planned_uniform = None
            self.maid_outfit = None
            self.apply_planned_outfit() # let apply planned outfit select day outfit (if needed)

        destination = self.get_destination() #None destination means they have free time
        # changing outfits is handled by move_person wrapper function
        if destination:
            location.move_person(self, destination)
        else:
            location.move_person(self, get_random_from_list([x for x in list_of_places if x.public or x == self.home]))

        if self.should_wear_uniform(): #She's wearing a uniform
            if creative_colored_uniform_policy.is_active():
                self.change_happiness(max(-1,self.get_opinion_score("work uniforms")), add_to_log = False)
            else:
                self.change_happiness(self.get_opinion_score("work uniforms"), add_to_log = False)
            if self.planned_uniform and self.planned_uniform.slut_requirement > self.sluttiness*0.8: #A skimpy outfit/uniform is defined as the top 20% of a girls natural sluttiness.
                self.change_slut(self.get_opinion_score("skimpy uniforms"), 30, add_to_log = False)
        else:
            #A skimpy outfit is defined as the top 20% of a girls natural sluttiness.
            if self.planned_outfit and self.planned_outfit.slut_requirement > self.sluttiness * 0.80 and self.get_opinion_score("skimpy outfits") > -2:
                self.change_slut(1, max_modified_to = ((self.get_opinion_score("skimpy outfits") +1) * 10), add_to_log = False)

        #A conservative outfit is defined as the bottom 20% of a girls natural sluttiness.
        if self.sluttiness < 30 and self.outfit and self.outfit.slut_requirement < self.sluttiness * 0.20:
            # happiness won't go below 80 or over 120 by this trait and only affects in low sluttiness range, after that she won't care
            if self.happiness > 80 and self.happiness < 120:
                self.change_happiness(self.get_opinion_score("conservative outfits"), add_to_log = False)

        # lingerie only impacts to sluttiness level 30
        if self.outfit and (self.outfit.get_bra() or self.outfit.get_panties()):
            lingerie_bonus = 0
            if self.outfit.get_bra() and self.outfit.get_bra().slut_value > 1: #We consider underwear with an innate sluttiness of 2 or higher "lingerie" rather than just underwear.
                lingerie_bonus += self.get_opinion_score("lingerie")
            if self.outfit.get_panties() and self.outfit.get_panties().slut_value > 1:
                lingerie_bonus += self.get_opinion_score("lingerie")
            lingerie_bonus = __builtin__.int(lingerie_bonus/2.0)
            self.change_slut(lingerie_bonus, max_modified_to = 30, add_to_log = False)

        # not wearing underwear only impacts sluttiness to level 40
        if self.outfit and (not self.outfit.wearing_bra() or not self.outfit.wearing_panties()): #We need to determine how much underwear they are not wearing. Each piece counts as half, so a +2 "love" is +1 slut per chunk.
            underwear_bonus = 0
            if not self.outfit.wearing_bra():
                underwear_bonus += self.get_opinion_score("not wearing underwear")
            if not self.outfit.wearing_panties():
                underwear_bonus += self.get_opinion_score("not wearing underwear")
            underwear_bonus = __builtin__.int(underwear_bonus/2.0) #I believe this rounds towards 0. No big deal if it doesn't, very minor detail.
            self.change_slut(underwear_bonus, max_modified_to = 40, add_to_log = False)

        # showing the goods only impacts sluttiness to level 50
        if self.outfit and self.outfit.tits_visible():
            self.change_slut(self.get_opinion_score("showing her tits"), max_modified_to = 50, add_to_log = False)
        if self.outfit and self.outfit.vagina_visible():
            self.change_slut(self.get_opinion_score("showing her ass"), max_modified_to = 50, add_to_log = False)

        # showing everything only impacts sluttiness to level 60
        if self.outfit and self.outfit.full_access():
            self.change_slut(self.get_opinion_score("not wearing anything"), max_modified_to = 60, add_to_log = False)

        for lta_store in [self.on_room_enter_event_list, self.on_talk_event_list]:
            for an_action in [x for x in lta_store if isinstance(x, Limited_Time_Action)]:
                an_action.turns_valid -= 1
                if an_action.turns_valid <= 0:
                    lta_store.remove(an_action)

        for a_role in self.special_role:
            a_role.run_move(self)

    Person.run_move = run_move_enhanced

    # extend the default run day function
    def person_run_day_extended(org_func):
        def run_day_wrapper(person):
            # run original function
            org_func(person)
            # run extension code (clean up situational dictionaries)
            person.situational_sluttiness.clear()
            person.situational_obedience.clear()
            # dominant person slowly bleeds obedience on run_day (lowest point offset by love)
            if person.is_dominant():
                if person.obedience - person.love > 100 - (person.get_opinion_score("taking control") * 5):
                    person.change_obedience(-1, add_to_log = False)


        return run_day_wrapper

    # wrap up the run_day function
    Person.run_day = person_run_day_extended(Person.run_day)

    # extend default wants_creampie function
    def person_wants_creampie_extended(org_func):
        def wants_creampie_wrapper(person):
            # when breeding fetish, she always wants a creampie
            if person.has_breeding_fetish():
                return True
            return org_func(person)

        return wants_creampie_wrapper

    Person.wants_creampie = person_wants_creampie_extended(Person.wants_creampie)

    def person_call_dialogue_extended(org_func):
        def person_call_dialogue_wrapper(person, type, **extra_args):
            if type == "sex_review" and extra_args.get("the_report", {}).get("is_angry", False):
                renpy.say(person, "Now leave me alone, I'm done.")
            else:
                org_func(person, type, **extra_args)

        return person_call_dialogue_wrapper

    Person.call_dialogue = person_call_dialogue_extended(Person.call_dialogue)


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
            if topic in Person._sexy_opinions_list: # We didn't find the topic in existing opinions for person, check global list if it is sexy
                sexy_opinion = True
            sexy_opinion = False

        if sexy_opinion:
            self.sexy_opinions[topic] = [degree, discovered]

            if topic not in Person._sexy_opinions_list: # Appends to the opinion pool #TODO: should we add this to the game pool here? Prevents person specific opinions...
                Person._sexy_opinions_list.append(topic)
        else:
            self.opinions[topic] = [degree, discovered]
            if topic not in Person._opinions_list: # Appends to the opinion pool #TODO: should we add this to the game pool here? Prevents person specific opinions...
                Person._opinions_list.append(topic)

        if add_to_log:
            mc.log_event((self.title or self.name) + " " + opinion_score_to_string(degree) + " " + str(topic), "float_text_green")

    # Adds a function that edits and adds opinions. It also appends to the vanilla opinion pool.
    Person.add_opinion = add_opinion

    def get_opinion_score_enhanced(self, topic): #Like get_opinion_topic, but only returns the score and not a tuple. Use this when determining a persons reaction to a relavent event.
        if isinstance(topic, basestring):
            if topic in self.opinions:
                return self.opinions[topic][0]
            if topic in self.sexy_opinions:
                return self.sexy_opinions[topic][0]

        return_value = 0
        if isinstance(topic, list):
            for a_topic in topic:
                return_value += self.get_opinion_score(a_topic)
        return return_value

    Person.get_opinion_score = get_opinion_score_enhanced

    def update_opinion_with_score(self, topic, score, add_to_log = True):
        if topic in Person._sexy_opinions_list:
            if topic in self.sexy_opinions:
                self.sexy_opinions[topic][0] = score
            else:
                self.sexy_opinions[topic] = [score, add_to_log]

        if topic in Person._opinions_list:
            if topic in self.opinions:
                self.opinions[topic][0] = score
            else:
                self.opinions[topic] = [score, add_to_log]

        if add_to_log:
            mc.log_event((self.title or self.name) + " " + opinion_score_to_string(score) + " " + str(topic), "float_text_green")
        return

    Person.update_opinion_with_score = update_opinion_with_score

    ## Increase the opinion on a specific topic (opinion)
    def increase_opinion_score(self, topic, max_value = 2, add_to_log = True, weighted = False):
        score = self.get_opinion_score(topic)

        if score < 2 and score < max_value:
            if weighted:
                if renpy.random.randint(0,100) < self.suggestibility:
                    self.update_opinion_with_score(topic, score + 1, add_to_log)
            else:
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

    # Change the work skill of a person to a specified score
    def update_work_skill(self, skill, score, add_to_log = True):
        skill_name = None
        if skill == 0 or skill == "hr_skill":
            skill_name = "HR Skill"
            current = self.hr_skill
        elif skill == 1 or skill == "market_skill":
            skill_name = "Market Skill"
            current = self.market_skill
        elif skill == 2 or skill == "research_skill":
            skill_name = "Research Skill"
            current = self.research_skill
        elif skill == 3 or skill == "production_skill":
            skill_name = "Production Skill"
            current = self.production_skill
        elif skill == 4 or skill == "supply_skill":
            skill_name = "Supply Skill"
            current = self.supply_skill

        if skill_name == None:
            return

        if current == score:
            return
        if skill_name == "HR Skill":
            self.hr_skill = score
        elif skill_name == "Market Skill":
            self.market_skill = score
        elif skill_name == "Research Skill":
            self.research_skill = score
        elif skill_name == "Production Skill":
            self.production_skill = score
        elif skill_name == "Supply Skill":
            self.supply_skill = score

        self.sex_skills[skill] = score
        if add_to_log:
            mc.log_event((self.title or self.name) + " " + skill_name + " is now at level " + str(score), "float_text_green")
        return

    Person.update_work_skill = update_work_skill

    # returns the day of first employment in company (-1 for never employed)
    def get_employed_since(self):
        return self.event_triggers_dict.get("employed_since", -1)

    def set_employed_since(self, value):
        self.event_triggers_dict["employed_since"] = value

    Person.employed_since = property(get_employed_since, set_employed_since, None)

    # returns the total number of days employed in company (0 for not employed)
    def get_days_employed(self):
        if self.is_employee():
            return day - self.employed_since
        return 0

    Person.days_employed = property(get_days_employed, None, None)

    # increase skill of person by one until max_value is reached.
    def increase_work_skill(self, skill, max_value = 6, add_to_log = True):
        if skill == 0 or skill == "hr_skill":
            self.update_work_skill("hr_skill", min(max_value, self.hr_skill + 1), add_to_log = add_to_log)
        elif skill == 1 or skill == "market_skill":
            self.update_work_skill("market_skill", min(max_value, self.market_skill + 1), add_to_log = add_to_log)
        elif skill == 2 or skill == "research_skill":
            self.update_work_skill("research_skill", min(max_value, self.research_skill + 1), add_to_log = add_to_log)
        elif skill == 3 or skill == "production_skill":
            self.update_work_skill("production_skill", min(max_value, self.production_skill + 1), add_to_log = add_to_log)
        elif skill == 4 or skill == "supply_skill":
            self.update_work_skill("supply_skill", min(max_value, self.supply_skill + 1), add_to_log = add_to_log)

        return

    Person.increase_work_skill = increase_work_skill

    def decrease_work_skill(self, skill, add_to_log = True):
        if skill == 0 or skill == "hr_skill":
            self.update_work_skill("hr_skill", max(0, self.hr_skill - 1), add_to_log = add_to_log)
        elif skill == 1 or skill == "market_skill":
            self.update_work_skill("market_skill", max(0, self.market_skill - 1), add_to_log = add_to_log)
        elif skill == 2 or skill == "research_skill":
            self.update_work_skill("research_skill", max(max_value, self.research_skill - 1), add_to_log = add_to_log)
        elif skill == 3 or skill == "production_skill":
            self.update_work_skill("production_skill", max(max_value, self.production_skill - 1), add_to_log = add_to_log)
        elif skill == 4 or skill == "supply_skill":
            self.update_work_skill("supply_skill", max(max_value, self.supply_skill - 1), add_to_log = add_to_log)

        return

    Person.decrease_work_skill = decrease_work_skill

    # Change Multiple Stats for a person at once (less lines of code, better readability)
    def change_stats(self, obedience = None, happiness = None, arousal = None, love = None, slut = None, max_slut = None, max_love = None, energy = None, novelty = None, add_to_log = True):
        message = []
        if not happiness is None:
            self.change_happiness(happiness, add_to_log = False)
            message.append(("+" if happiness > 0 else "") + str(happiness) + " {image=happy_token_small}")
        if not obedience is None:
            self.change_obedience(obedience, add_to_log = False)
            message.append(("+" if obedience > 0 else "") + str(obedience) +" {image=triskelion_token_small}")
        if not arousal is None:
            self.change_arousal(arousal, add_to_log = False)
            message.append(("+" if arousal > 0 else "") + str(arousal) + " {image=arousal_token_small}")
        if not love is None:
            amount = self.change_love(love, max_love, add_to_log = False)
            if amount and amount != 0:
                message.append(("+" if amount > 0 else "") + str(amount) + " {image=red_heart_token_small}")
        if not slut is None:
            amount = self.change_slut(slut, max_slut, add_to_log = False)
            if amount and amount != 0:
                message.append(("+" if amount > 0 else "") + str(amount) + " {image=underwear_token_small}")
        if not energy is None:
            amount = self.change_energy(energy, add_to_log = False)
            if amount and amount != 0:
                message.append(("+" if amount > 0 else "") + str(amount) + " {image=energy_token_small}")
        if not novelty is None:
            amount = self.change_novelty(novelty, add_to_log = False)
            if amount and amount != 0:
                message.append(("+" if amount > 0 else "") + str(amount) + " Novelty")
        if add_to_log and message:
            display_name = self.create_formatted_title("???")
            if self.title:
                display_name = self.title
            mc.log_event(display_name + ": " + " ".join(message), "float_text_yellow")
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

    def person_change_slut_extended(org_func):
        def person_change_slut_wrapper(person, amount, max_modified_to = None, add_to_log = True):
            if max_modified_to:  # change max_modified_to based on suggestibility
                suggestibility_modifier = 0
                if person.suggestibility == 0:
                    pass
                elif person.suggestibility < 20:
                    suggestibility_modifier = __builtin__.int(person.suggestibility / 2.0)
                elif person.suggestibility < 60:
                    suggestibility_modifier = 10 + __builtin__.int((person.suggestibility - 20) / 4.0)
                elif person.suggestibility < 140:
                    suggestibility_modifier = 20 + __builtin__.int((person.suggestibility - 60) / 8.0)
                else:
                    suggestibility_modifier = 30
                max_modified_to += suggestibility_modifier

            # limit sluttiness to 100 -> read as 100%
            # there is no content for higher sluttiness values,
            # but it will impact the game negatively if it is over 100 (bored sex pos etc.)
            if not max_modified_to or max_modified_to > 100:
                max_modified_to = 100

            return org_func(person, amount, max_modified_to = max_modified_to, add_to_log = add_to_log)

        return person_change_slut_wrapper

    Person.change_slut = person_change_slut_extended(Person.change_slut)

    def person_change_love_extended(org_func):
        def person_change_love_wrapper(person, amount, max_modified_to = None, add_to_log = True):
            if max_modified_to:
                suggestibility_modifier = 0
                if person.suggestibility == 0:
                    pass
                elif person.suggestibility < 20:
                    suggestibility_modifier = __builtin__.int(person.suggestibility / 5.0)
                elif person.suggestibility < 60:
                    suggestibility_modifier = 2 + __builtin__.int(person.suggestibility / 10.0)
                elif person.suggestibility < 120:
                    suggestibility_modifier = 8 + __builtin__.int(person.suggestibility / 20.0)
                else:
                    suggestibility_modifier = 14
                max_modified_to += suggestibility_modifier

            return org_func(person, amount, max_modified_to = max_modified_to, add_to_log = add_to_log)

        return person_change_love_wrapper

    Person.change_love = person_change_love_extended(Person.change_love)

    ## CHANGE WILLPOWER EXTENSION
    # changes the willpower of a person by set amount
    def change_willpower(self, amount): #Logs change in willpower and shows new total.
        self.willpower += amount
        if self.willpower < 0:
            self.willpower = 0
        return self.willpower

    # attach to person object
    Person.change_willpower = change_willpower

    def draw_person_enhanced(self,position = None, emotion = None, special_modifier = None, show_person_info = True, lighting = None, background_fill = "auto", the_animation = None, animation_effect_strength = 1.0,
        draw_layer = "solo", display_transform = None, extra_at_arguments = None, display_zorder = None, wipe_scene = True): #Draw the person, standing as default if they aren't standing in any other position.

        validate_texture_memory()
        if position is None:
            position = self.idle_pose

        if emotion is None:
            emotion = self.get_emotion()

        if not can_use_animation():
            the_animation = None
        elif the_animation is None: # assign default animation when not passed and enabled
            if position in ["blowjob", "kneeling1"]:
                the_animation = blowjob_bob
            elif position in ["doggy", "standing_doggy", "back_peek"]:
                the_animation = ass_bob
            elif position in ["missionary"]:
                the_animation = missionary_bob
            else:
                the_animation = self.idle_animation

        if display_transform is None:
            display_transform = character_right

        if lighting is None:
            lighting = mc.location.get_lighting_conditions()

        if display_zorder is None:
            display_zorder = 0

        at_arguments = [display_transform, scale_person(self.height)]
        if not the_animation is None:
            at_arguments.append(basic_bounce(the_animation))

        if extra_at_arguments:
            if isinstance(extra_at_arguments, list):
                at_arguments.extend(extra_at_arguments)
            else:
                at_arguments.append(extra_at_arguments)

        self.hide_person(draw_layer = draw_layer)
        if wipe_scene:
            clear_scene() #Make sure no other characters are drawn either.
            if show_person_info:
                renpy.show_screen("person_info_ui",self)

        if the_animation:
            weight_mask = self.build_weight_mask(the_animation, position, animation_effect_strength)
            renpy.show(self.identifier, at_list=at_arguments, layer = draw_layer, what = ShaderPerson(self.build_person_displayable(position, emotion, special_modifier, lighting), weight_mask), tag = self.identifier)
        else:
            renpy.show(self.identifier, at_list=at_arguments, layer = draw_layer, what = self.build_person_displayable(position, emotion, special_modifier, lighting), tag = self.identifier)

    # replace the default draw_person function of the person class
    Person.draw_person = draw_person_enhanced
    # add location to store original personality
    Person.original_personality = None

    def draw_animated_removal_enhanced(self, the_clothing, position = None, emotion = None, show_person_info = True, special_modifier = None, lighting = None, background_fill = "auto", the_animation = None, animation_effect_strength = 1.0, half_off_instead = False,
        draw_layer = "solo", display_transform = None, extra_at_arguments = None, display_zorder = None, wipe_scene = True, scene_manager = None): #A special version of draw_person, removes the_clothing and animates it floating away. Otherwise draws as normal.

        if the_clothing is None:  #we need something to take off
            renpy.say("WARNING", "Draw animated removal called without passing a clothing item.")
            return

        if self.outfit is None:
            renpy.say("WARNING", self.name + " is not wearing any outfit to remove an item from, aborting draw animated removal.")
            return

        if position is None:
            position = self.idle_pose

        if emotion is None:
            emotion = self.get_emotion()

        if lighting is None:
            lighting = mc.location.get_lighting_conditions()

        if display_transform is None: # make sure we don't need to pass the position with each draw
            display_transform = character_right

        if not can_use_animation():
            the_animation = None
        elif the_animation is None:
            the_animation = self.idle_animation

        at_arguments = [display_transform, scale_person(self.height)]
        if not the_animation is None:
            at_arguments.append(basic_bounce(the_animation))
        if extra_at_arguments:
            if isinstance(extra_at_arguments, list):
                at_arguments.extend(extra_at_arguments)
            else:
                at_arguments.append(extra_at_arguments)

        if not isinstance(the_clothing, list):  # convert clothing to list, if not already
            the_clothing = [the_clothing]

        if display_zorder is None:
            display_zorder = 0

        if wipe_scene:
            clear_scene()

        if scene_manager is None and show_person_info:
            renpy.show_screen("person_info_ui",self)
        else:   # when we are called from the scene manager we have to draw the other characters
            scene_manager.draw_scene(exclude_list = [self])

        bottom_displayable = self.build_person_displayable(position, emotion, special_modifier, lighting, cache_item = False) # needs to be flattened for fade to work correctly
        for cloth in the_clothing:
            if half_off_instead:
                self.outfit.half_off_clothing(cloth) #Half-off the clothing
            else:
                self.outfit.remove_clothing(cloth) #Remove the clothing
        top_displayable = self.build_person_displayable(position, emotion, special_modifier, lighting, cache_item = False)

        self.hide_person()

        if the_animation:
            weight_mask = self.build_weight_mask(the_animation, position, animation_effect_strength)
            renpy.show(self.identifier, at_list=at_arguments, layer = draw_layer, what = ShaderPerson(top_displayable, weight_mask), zorder = display_zorder, tag = self.identifier)
            renpy.show(self.identifier + "_old", at_list= at_arguments + [clothing_fade], layer = draw_layer, what = ShaderPerson(bottom_displayable, weight_mask), zorder = display_zorder + 1, tag = self.identifier + "_old") #Overlay old and blend out
        else:
            renpy.show(self.identifier, at_list=at_arguments, layer = draw_layer, what = top_displayable, zorder = display_zorder, tag = self.identifier)
            renpy.show(self.identifier + "_old", at_list= at_arguments + [clothing_fade], layer = draw_layer, what = bottom_displayable, zorder = display_zorder + 1, tag = self.identifier + "_old") #Overlay old and blend out

        renpy.pause(.3) # slight pause between animations
        return

    Person.draw_animated_removal = draw_animated_removal_enhanced

    # cache the last 127 generated displayables
    global character_cache
    character_cache = LRUCacheDict(127, expiration = 0)

    def clean_cache(self):
        if not "character_cache" in globals():
            return

        partial = "ID:{}".format(self.identifier)
        obsolete = [x for x in character_cache.keys() if partial in x]
        for x in obsolete:
            del character_cache[x]

    Person.clean_cache = clean_cache

    def build_person_displayable_enhanced(self, position = None, emotion = None, special_modifier = None, lighting = None, hide_list = [], outfit = None, cache_item = True): #Encapsulates what is done when drawing a person and produces a single displayable.
        if position is None:
            position = self.idle_pose
        if emotion is None:
            emotion = self.get_emotion()
        if outfit is None:
            outfit = self.outfit

        forced_special_modifier = self.outfit.get_forced_modifier()
        if forced_special_modifier is not None:
            special_modifier = forced_special_modifier

        disp_key = "ID:{}_P:{}_E:{}_SM:{}_L:{}_O:{}".format(self.identifier, position, emotion, special_modifier, hash(tuple(x for x in map(hash, lighting))), outfit.hash())
        if disp_key in character_cache:
            return character_cache[disp_key]

        displayable_list = []
        displayable_list.append(self.body_images.generate_item_displayable(self.body_type,self.tits,position,lighting)) #Add the body displayable
        displayable_list.append(self.expression_images.generate_emotion_displayable(position,emotion, special_modifier = special_modifier, eye_colour = self.eyes[1], lighting = lighting)) #Get the face displayable
        if self.tan_style and self.tan_style.proper_name != "no_tan":
            displayable_list.append(self.tan_style.generate_item_displayable(self.body_type,self.tits, position, lighting = lighting)) # Add the tan
            if self.tan_style.has_extension:
                displayable_list.append(self.tan_style.has_extension.generate_item_displayable(self.body_type, self.tits, position, lighting = lighting)) # Add the tan
        displayable_list.append(self.pubes_style.generate_item_displayable(self.body_type, self.tits, position, lighting = lighting)) #Add in her pubes

        displayable_list.extend(outfit.generate_draw_list(self,position,emotion,special_modifier, lighting = lighting, hide_layers = hide_list))
        displayable_list.append(self.hair_style.generate_item_displayable("standard_body",self.tits,position, lighting = lighting)) #Get hair

        x_size, y_size = position_size_dict.get(position)
        composite_list = [(x_size,y_size)]

        for display in displayable_list:
            if isinstance(display, __builtin__.tuple):
                composite_list.extend(display)
            else:
                composite_list.append((0,0))
                composite_list.append(display)

        character_composite = Composite(*composite_list)

        if persistent.vren_display_pref == "Float" or persistent.vren_display_pref == "Frame":
            character_raw_body = im.Composite((x_size, y_size),
                (0,0), self.body_images.generate_raw_image(self.body_type,self.tits,position),
                #(0,0), self.expression_images.generate_raw_image(position, emotion, special_modifier = special_modifier),
                self.hair_style.crop_offset_dict.get(position,(0,0)), self.hair_style.generate_raw_image("standard_body", self.tits, position))

            blurred_image = im.Blur(character_raw_body, 6)
            aura_colour = self.get_display_colour_code()
            recoloured_blur = im.MatrixColor(blurred_image, im.matrix.colorize(aura_colour, aura_colour))

            final_composite = Composite((x_size, y_size), (0,0), recoloured_blur, (0,0), character_composite)
        else:
            final_composite = character_composite

        # Create a composite image using all of the displayables
        if cache_item:
            character_cache[disp_key] = Flatten(final_composite)
            return character_cache[disp_key]
        return Flatten(final_composite)

    Person.build_person_displayable = build_person_displayable_enhanced

    def person_call_extended(org_func):
        def person_call_wrapper(person, what, *args, **kwargs):
            global portrait_say
            portrait_say = person.build_person_portrait()
            org_func(person, what, *args, **kwargs)
            portrait_say = None # clear portrait when done

        return person_call_wrapper

    Person.__call__ = person_call_extended(Person.__call__)

    global portrait_cache
    portrait_cache = LRUCacheDict(100, expiration = 0)

    def build_person_portrait(self, special_modifier = None):
        position = "stand5"
        emotion = "happy"
        special_modifier = None
        lighting = [.98,.98,.98]

        disp_key = "P:{}_F:{}_H:{}_HC:{}_EC:{}".format(self.identifier,
            self.face_style, self.hair_style.name,
            hash(tuple(x for x in map(hash, self.hair_style.colour))),
            hash(tuple(x for x in map(hash, self.eyes[1]))))

        if disp_key in portrait_cache:
            return portrait_cache[disp_key]

        displayable_list = []
        displayable_list.append(self.expression_images.generate_emotion_displayable(position,emotion, special_modifier = special_modifier, eye_colour = self.eyes[1], lighting = lighting)) #Get the face displayable
        displayable_list.append(self.hair_style.generate_item_displayable("standard_body",self.tits,position, lighting = lighting)) #Get hair

        x_size, y_size = position_size_dict.get(position)
        composite_list = [(x_size,y_size)]

        for display in displayable_list:
            if isinstance(display, __builtin__.tuple):
                composite_list.extend(display)
            else:
                composite_list.append((0,0))
                composite_list.append(display)

        portrait_cache[disp_key] = AlphaMask(Flatten(Composite(*composite_list)), Image("portrait_mask.png"))
        return portrait_cache[disp_key]

    Person.build_person_portrait = build_person_portrait

    def hide_person_enhanced(self, draw_layer = "solo"): #Hides the person. Makes sure to hide all possible known tags for the character.
        # We keep track of tags used to display a character so that they can always be unique, but still tied to them so they can be hidden
        renpy.hide(self.identifier, draw_layer)
        renpy.hide(self.identifier + "_old", draw_layer)
        return

    Person.hide_person = hide_person_enhanced

    def person_is_at_work(self): #Checks to see if the character is at work.
        # special handling for college interns
        if self.has_role("College Intern") and self.location in [rd_division, p_division, m_division, office]:
            return True

        if self.has_role(maid_role):
            return not self.job.schedule.get_destination() is None

        # special handling for unique characters working at stripclub (use roles since unique chars only get role instead of job)
        if self.has_role([stripclub_stripper_role, stripclub_waitress_role, stripclub_bdsm_performer_role, stripclub_manager_role, stripclub_mistress_role]) \
            and self.location in [strip_club, bdsm_room]:
                return True

        if not self.job:
            return False

        # she works around town, so when the job has a scheduled location, she's at work
        if self == police_chief:
            return not self.job.schedule.get_destination() is None

        return self.location == self.job.job_location

    Person.is_at_work = person_is_at_work

    def is_person_at_mc_house(self):
        return self.location in [hall, bedroom, lily_bedroom, mom_bedroom, kitchen, home_bathroom, her_hallway, dungeon, home_shower]

    Person.is_at_mc_house = is_person_at_mc_house

    def is_person_home(self):
        return self.location == self.home

    Person.is_home = is_person_home

    ####### Begin cum extension functions ######

    # calculate generic arousal change for a person based on opinions during MC cum shot
    # with all favorable max gain is 12 arousal points
    def partner_generic_arousal(person):
        total_amount = 0
        if not mc.condom:
            total_amount += 2 * person.get_opinion_score("bareback sex")
        else:
            total_amount -= 2 * person.get_opinion_score("bareback sex")
        if person.relationship != "Single":
            total_amount += 2 * person.get_opinion_score("cheating on men")
        return total_amount

    def cum_in_vagina_extended(org_func):
        def cum_in_vagina_wrapper(person, add_to_record = True):
            # run original function
            org_func(person, add_to_record)
            # run extension code
            person.change_arousal(partner_generic_arousal(person) + 5 * person.get_opinion_score("creampies"), add_to_log = add_to_record)
        return cum_in_vagina_wrapper

    # wrap up the cum_in_vagina function
    Person.cum_in_vagina = cum_in_vagina_extended(Person.cum_in_vagina)

    def cum_in_ass_extended(org_func):
        def cum_in_ass_wrapper(person, add_to_record = True):
            # run original function
            org_func(person, add_to_record)
            # run extension code
            person.change_arousal(partner_generic_arousal(person) + 5 * person.get_opinion_score("anal creampies"), add_to_log = add_to_record)
        return cum_in_ass_wrapper

    # wrap up the cum_in_ass function
    Person.cum_in_ass = cum_in_ass_extended(Person.cum_in_ass)

    def cum_on_face_extended(org_func):
        def cum_on_face_wrapper(person, add_to_record = True):
            # run original function
            org_func(person, add_to_record)
            # run extension code
            mc.listener_system.fire_event("sex_cum_on_face", the_person = person)
            if "report_log" in globals() and add_to_record:   # add to report log if exists
                report_log["cum facials"] = report_log.get("cum facials", 0) + 1
            person.change_arousal(partner_generic_arousal(person) + 5 * person.get_opinion_score("cum facials"), add_to_log = add_to_record)
        return cum_on_face_wrapper

    # wrap up the cum_on_face function
    Person.cum_on_face = cum_on_face_extended(Person.cum_on_face)

    def cum_on_tits_extended(org_func):
        def cum_on_tits_wrapper(person, add_to_record = True):
            # run original function
            org_func(person, add_to_record)
            # run extension code
            mc.listener_system.fire_event("sex_cum_on_tits", the_person = person)
            if "report_log" in globals() and add_to_record:   # add to report log if exists
                report_log["cum on tits"] = report_log.get("cum on tits", 0) + 1
            person.change_arousal(partner_generic_arousal(person) + 5 * person.get_opinion_score("being covered in cum"), add_to_log = add_to_record)
        return cum_on_tits_wrapper

    # wrap up the cum_on_tits function
    Person.cum_on_tits = cum_on_tits_extended(Person.cum_on_tits)

    def cum_on_stomach_extended(org_func):
        def cum_on_stomach_wrapper(person, add_to_record = True):
            # run original function
            org_func(person, add_to_record)
            # run extension code
            mc.listener_system.fire_event("sex_cum_on_stomach", the_person = person)
            if "report_log" in globals() and add_to_record:   # add to report log if exists
                report_log["cum on stomach"] = report_log.get("cum on stomach", 0) + 1
            person.change_arousal(partner_generic_arousal(person) + 5 * person.get_opinion_score("being covered in cum"), add_to_log = add_to_record)
        return cum_on_stomach_wrapper

    # wrap up the cum_on_stomach function
    Person.cum_on_stomach = cum_on_stomach_extended(Person.cum_on_stomach)

    def cum_on_ass_extended(org_func):
        def cum_on_ass_wrapper(person, add_to_record = True):
            # run original function
            org_func(person, add_to_record)
            # run extension code
            mc.listener_system.fire_event("sex_cum_on_ass", the_person = person)
            if "report_log" in globals() and add_to_record:   # add to report log if exists
                report_log["cum on ass"] = report_log.get("cum on ass", 0) + 1
            person.change_arousal(partner_generic_arousal(person) + 5 * person.get_opinion_score("being covered in cum"), add_to_log = add_to_record)
        return cum_on_ass_wrapper

    # wrap up the cum_on_ass function
    Person.cum_on_ass = cum_on_ass_extended(Person.cum_on_ass)

    def cum_in_mouth_extended(org_func):
        def cum_in_mouth_wrapper(person, add_to_record = True):
            # run original function
            org_func(person, add_to_record)
            # run extension code
            if "report_log" in globals() and add_to_record:   # add to report log if exists
                report_log["drinking cum"] = report_log.get("drinking cum", 0) + 1
            person.change_arousal(partner_generic_arousal(person) + 5 * person.get_opinion_score("drinking cum"), add_to_log = add_to_record)
        return cum_in_mouth_wrapper

    # wrap up the cum_on_ass function
    Person.cum_in_mouth = cum_in_mouth_extended(Person.cum_in_mouth)


##################
# Role Functions #
##################
    def is_employee(self):
        return self.has_role(employee_role)
    Person.is_employee = is_employee

    def has_role_enhanced(self, role):
        if isinstance(role, basestring):
            return any(x for x in self.special_role if x.role_name == role) \
                or any(x for x in self.special_role if x.parent_role and x.parent_role.role_name == role)
        elif isinstance(role, list):
            return any(x in self.special_role for x in role) \
                or any(x.parent_role in self.special_role for x in role)

        return role in self.special_role \
            or role.parent_role in self.special_role \
            or any(x for x in self.special_role if x.check_looks_like(role))

    Person.has_role = has_role_enhanced

    def has_job_enhanced(self, job):
        if not self.job:
            return False

        if isinstance(job, basestring):
            return self.job.job_title == job
        elif isinstance(job, list):
            return self.job in job

        return self.job == job

    Person.has_job = has_job_enhanced

    def add_role(self, role):
        added = False
        if not role in self.special_role:
            self.special_role.append(role)
            added = True

        if not added:
            return False

        # special condition if she hates kissing, but becomes your girlfriend or paramour she would allow kissing
        if self.get_opinion_score("kissing") <= -2 and role in [girlfriend_role, affair_role, harem_role]:
            self.increase_opinion_score("kissing")

        # special situation if she gets girlfriend role, she loses affair role and SO
        if role == girlfriend_role:
            self.remove_role(affair_role)
            self.relationship = "Single" #Technically they aren't "single", but the MC has special roles for their girlfriend.
            self.SO_name = None

        if role == harem_role:
            self.remove_role(girlfriend_role)
            mc.business.event_triggers_dict["harem_mansion_unlocked"] = True
            #TODO: Add event with dialog to give info about unlocked harem mansion

        return added

    Person.add_role = add_role

    def remove_role(self, role, remove_all = False, remove_linked = True):
        if role in self.special_role:
            self.special_role.remove(role)
            if remove_linked:
                for linked_role in role.linked_roles:
                    self.remove_role(role, remove_all, remove_linked)
            return True
        return False

    Person.remove_role = remove_role

    # helper function to determine if person is dominant
    def is_dominant(self):
        if self.has_role(slave_role):   # slave is no longer dominant regardless of opinions / personality
            return False
        if self.get_opinion_score("taking control") > 0 and self.get_opinion_score("being submissive") <= 0:
            return True
        if self.personality == alpha_personality:
            return True
        return False
    Person.is_dominant = is_dominant

    def is_girlfriend(self):
        return self.has_role([girlfriend_role, harem_role])

    Person.is_girlfriend = is_girlfriend

    def is_affair(self):
        return self.has_role(affair_role)

    Person.is_affair = is_affair

    # helper function, to determine if person is available for crisis events
    # for now only girls giving birth are not available (but is extendable for future conditions)
    def person_is_available(self):
        return not self.is_giving_birth() and self.available

    Person.is_available = property(person_is_available, None, None)

    def person_has_job_role(self, job_role):
        if not self.job:
            return False

        if job_role in self.job.job_roles:
            return True
        return False

    Person.has_job_role = person_has_job_role

################################################
# Outfit functions - wear a specialized outfit #
################################################

    def person_is_wearing_uniform(self):
        return self.outfit == self.planned_uniform and self.planned_uniform != self.planned_outfit

    Person.is_wearing_uniform = person_is_wearing_uniform

    def person_should_wear_uniform_extended(org_func):
        def should_wear_uniform_wrapper(person):
            # run original function
            result = org_func(person)
            # run extension code
            if result and day%7 == 4 and casual_friday_uniform_policy.is_active():
                result = False
            if person.is_at_work() and person.job == doctor_job:
                result = True # force True for doctor
            return result

        return should_wear_uniform_wrapper

    # wrap up the should_wear_uniform function
    Person.should_wear_uniform = person_should_wear_uniform_extended(Person.should_wear_uniform)

    @property
    def current_planned_outfit(self):
        if self.should_wear_uniform() and self.planned_uniform:
            return self.planned_uniform
        elif self.location in [gym, university] and self.location_outfit:
            return self.location_outfit
        return self.planned_outfit

    Person.current_planned_outfit = current_planned_outfit

    def review_outfit_enhanced(self, dialogue = True, draw_person = True):
        if not self.has_cum_fetish():
            self.outfit.remove_all_cum()

        if not self.outfit.matches(self.current_planned_outfit) \
            and (__builtin__.len(self.location.people) > 1 \
            or (self.should_wear_uniform() and not self.is_wearing_uniform()) \
            or (self.outfit.slut_requirement > self.sluttiness)):
            self.apply_planned_outfit()
            if draw_person:
                self.draw_person()
            if dialogue:
                self.call_dialogue("clothing_review") # must be last call in function
        return

    Person.review_outfit = review_outfit_enhanced

    def apply_gym_outfit(self):
        if workout_wardrobe:
            self.location_outfit = self.personalize_outfit(workout_wardrobe.decide_on_outfit2(self))
            self.apply_outfit(self.location_outfit)
            # self.apply_outfit(workout_wardrobe.decide_on_outfit2(self))
        return

    Person.apply_gym_outfit = apply_gym_outfit

    def apply_university_outfit(self):
        if university_wardrobe:
            self.location_outfit = university_wardrobe.decide_on_outfit2(self)
            # get personal copy of outfit, so we don't change the university wardrobe (in any events)
            self.apply_outfit(self.location_outfit)
        return

    Person.apply_university_outfit = apply_university_outfit

    def apply_yoga_outfit(self):
        self.apply_planned_outfit()
        # strip to underwear or else pick workout outfit
        if self.effective_sluttiness("underwear_nudity") >= 60:
            # use her current planned underwear
            self.strip_to_underwear(delay = 0)
            # take off shoes and socks
            self.strip_outfit(delay = 0, exclude_upper = True, exclude_lower = True, exclude_feet = False)
            # add black slips
            self.outfit.add_feet(slips.get_copy(), colour_black)
        elif workout_wardrobe:
            self.apply_outfit(self.personalize_outfit(workout_wardrobe.decide_on_outfit2(self)))
            #self.apply_outfit(workout_wardrobe.decide_on_outfit2(self))
        return

    Person.apply_yoga_outfit = apply_yoga_outfit

    def apply_yoga_shoes(self):
        # for now, just apply a nude outfit with black slips
        outfit = Outfit("Nude")
        outfit.add_feet(slips.get_copy(), colour_black)
        self.apply_outfit(outfit)
        return

    Person.apply_yoga_shoes = apply_yoga_shoes

    def apply_planned_outfit(self, ignore_base = False, update_taboo = False):
        if time_of_day != 0:    # in timeslot 0 we pick new outfits
            self.restore_all_clothing() # restore half-off clothing items of current outfit.

        if self.should_wear_uniform():
            self.wear_uniform()
        elif self.location in [gym, university] and self.location_outfit:
            self.apply_outfit(self.location_outfit, ignore_base = ignore_base, update_taboo = update_taboo)
        else:
            if not self.planned_outfit: # extra validation to make sure we have a planned outfit
                self.planned_outfit = self.decide_on_outfit()

            self.apply_outfit(self.planned_outfit, ignore_base = ignore_base, update_taboo = update_taboo)
        return

    Person.apply_planned_outfit = apply_planned_outfit

    def person_wear_uniform(self):
        if self.planned_uniform:    # quick exit, use planned uniform
            self.apply_outfit(self.planned_uniform)
            return

        if self.event_triggers_dict.get("forced_uniform", False):
            uniform = self.event_triggers_dict.get("forced_uniform").get_copy()
        else:
            uniform_wardrobe = mc.business.get_uniform_wardrobe_for_person(self)
            if uniform_wardrobe:
                uniform = uniform_wardrobe.decide_on_uniform(self)
            else: # we have no valid wardrobe, pick an outfit from wardrobe as uniform
                uniform = self.wardrobe.decide_on_outfit2(self)

            if uniform and self.is_employee():  # only apply policies for employees
                if not creative_colored_uniform_policy.is_active() and personal_bottoms_uniform_policy.is_active():
                    (uniform, swapped) = WardrobeBuilder(self).apply_bottom_preference(self, uniform)
                elif creative_colored_uniform_policy.is_active():
                    uniform = WardrobeBuilder(self).personalize_outfit(uniform, max_alterations = 2, swap_bottoms = personal_bottoms_uniform_policy.is_active(), allow_skimpy = creative_skimpy_uniform_policy.is_active())

                if commando_uniform_policy.is_active():
                    for item in [x for x in uniform.get_upper_ordered() if x.underwear]:
                        uniform.remove_clothing(item)
                    for item in [x for x in uniform.get_lower_ordered() if x.underwear]:
                        uniform.remove_clothing(item)

            if uniform and self.job == doctor_job:  # add lab coat for doctors
                uniform.add_upper(lab_coat.get_copy(), colour_white)

        self.set_uniform(uniform, True)
        return

    Person.wear_uniform = person_wear_uniform

    def person_is_wearing_uniform_extended(org_func):
        def is_wearing_uniform_wrapper(person):
            # run extension code
            if casual_friday_uniform_policy.is_active() and day % 7 == 4:
                return False
            # run original function
            return org_func(person)

        return is_wearing_uniform_wrapper

    Person.is_wearing_uniform = person_is_wearing_uniform_extended(Person.is_wearing_uniform)

    def personalize_outfit(self, outfit, opinion_color = None, coloured_underwear = False, max_alterations = 0, main_colour = None, swap_bottoms = False, allow_skimpy = True):
        return WardrobeBuilder(self).personalize_outfit(outfit, opinion_color = opinion_color, coloured_underwear = coloured_underwear, max_alterations = max_alterations, main_colour = main_colour, swap_bottoms = swap_bottoms, allow_skimpy = allow_skimpy)

    Person.personalize_outfit = personalize_outfit

    def approves_outfit_color(self, outfit):
        return WardrobeBuilder(self).approves_outfit_color(outfit)

    Person.approves_outfit_color = approves_outfit_color

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

    def reset_opinions(self):
        self.opinions = {}

    Person.reset_opinions = reset_opinions

    def reset_sexy_opinions(self):
        self.sexy_opinions = {}

    Person.reset_sexy_opinions = reset_sexy_opinions

#########################################
# Add hash (unique id) to Person object #
#########################################

    def person__hash__(self):
        return hash(self.identifier)

    Person.__hash__ = person__hash__
    Person.hash = person__hash__

    def person__eq__(self, other):
        if isinstance(self, other.__class__):
            return hash(self.identifier) == hash(other.identifier)
        return False

    Person.__eq__ = person__eq__

    def person__ne__(self, other):
        if isinstance(self, other.__class__):
            return hash(self.identifier) != hash(other.identifier)
        return True

    Person.__ne__ = person__ne__

###################
# DEBUG FUNCTIONS *
###################

    # check if current outfit is an actual outfit in the wardrobe (should always be a copy)
    def validate_outfit(self):
        for outfit in self.wardrobe.outfits + self.wardrobe.overwear_sets + self.wardrobe.underwear_sets:
            if id(self.outfit) == id(outfit):
                renpy.say("WARNING", "Current outfit is not a copy of the wardrobe item.")
            elif id(self.planned_outfit) == id(outfit):
                renpy.say("WARNING", "Current planned outfit is not a copy of the wardrobe item.")
            elif id(self.planned_uniform) == id(outfit):
                renpy.say("WARNING", "Current uniform is not a copy of the wardrobe item.")
        return

    Person.validate_outfit = validate_outfit

##########################################
# Expose outfit methods on Person object #
##########################################
    # many coding errors are related to missing .outfit in the sequence to check a persons state based on her outfit
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

    def person_get_bra(self):
        return self.outfit.get_bra()

    Person.get_bra = person_get_bra

    def person_get_panties(self):
        return self.outfit.get_panties()

    Person.get_panties = person_get_panties

    def person_can_remove_bra(self):
        return self.outfit.can_remove_bra()

    Person.can_remove_bra = person_can_remove_bra

    def person_can_remove_panties(self):
        return self.outfit.can_remove_panties()

    Person.can_remove_panties = person_can_remove_panties

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

    def person_get_upper_top_layer(self):
        return self.outfit.get_upper_top_layer()

    Person.get_upper_top_layer = person_get_upper_top_layer

    def person_get_lower_top_layer(self):
        return self.outfit.get_lower_top_layer()

    Person.get_lower_top_layer = person_get_lower_top_layer

    def person_get_feet_top_layer(self):
        return self.outfit.get_feet_top_layer()

    Person.get_feet_top_layer = person_get_feet_top_layer

    def person_restore_all_clothing(self):
        return self.outfit.restore_all_clothing()

    Person.restore_all_clothing = person_restore_all_clothing

    def person_has_clothing(self, the_clothing):
        return self.outfit.has_clothing(the_clothing)

    Person.has_clothing = person_has_clothing

    def person_decide_on_outfit(self, sluttiness_modifier = 0.0):
        return self.wardrobe.decide_on_outfit2(self, sluttiness_modifier)

    Person.decide_on_outfit = person_decide_on_outfit

    def person_get_random_appropriate_outfit(self, guarantee_output = False):
        outfit = self.wardrobe.get_random_appropriate_outfit(sluttiness_limit = self.effective_sluttiness(), preferences = WardrobePreference(self))
        if guarantee_output and not outfit: # when no outfit and we need one, generate one
            outfit = self.generate_random_appropriate_outfit(swap_bottoms = False, allow_skimpy = self.sluttiness > 50)
        return outfit

    Person.get_random_appropriate_outfit = person_get_random_appropriate_outfit

    def person_generate_random_appropriate_outfit(self, outfit_type = "FullSets", swap_bottoms = False, allow_skimpy = False):
        return generate_random_appropriate_outfit(self, outfit_type = outfit_type, swap_bottoms = swap_bottoms, allow_skimpy = allow_skimpy)

    Person.generate_random_appropriate_outfit = person_generate_random_appropriate_outfit

    def person_get_full_strip_list(self, strip_feet = True, strip_accessories = False):
        return self.outfit.get_full_strip_list(strip_feet, strip_accessories)

    Person.get_full_strip_list = person_get_full_strip_list

    def person_get_underwear_strip_list(self, visible_enough = True, avoid_nudity = False):
        return self.outfit.get_underwear_strip_list(visible_enough, avoid_nudity)

    Person.get_underwear_strip_list = person_get_underwear_strip_list

    def person_can_half_off_to_tits(self, visible_enough = True):
        return self.outfit.can_half_off_to_tits(visible_enough)

    Person.can_half_off_to_tits = person_can_half_off_to_tits

    def person_get_half_off_to_tits_list(self, visible_enough = True):
        return self.outfit.get_half_off_to_tits_list(visible_enough)

    Person.get_half_off_to_tits_list = person_get_half_off_to_tits_list

    def person_get_tit_strip_list(self, visible_enough = True):
        return self.outfit.get_tit_strip_list(visible_enough)

    Person.get_tit_strip_list = person_get_tit_strip_list

    def person_can_half_off_to_vagina(self, visible_enough = True):
        return self.outfit.can_half_off_to_vagina(visible_enough)

    Person.can_half_off_to_vagina = person_can_half_off_to_vagina

    def person_get_half_off_to_vagina_list(self, visible_enough = True):
        return self.outfit.get_half_off_to_vagina_list(visible_enough)

    Person.get_half_off_to_vagina_list = person_get_half_off_to_vagina_list

    def person_get_vagina_strip_list(self, visible_enough = True):
        return self.outfit.get_vagina_strip_list(visible_enough)

    Person.get_vagina_strip_list = person_get_vagina_strip_list

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
            found = next((x for x in self.on_talk_event_list if x.effect == the_crisis or x.name == the_crisis), None)
            if found:
                self.on_talk_event_list.remove(found)

        if the_crisis in self.on_talk_event_list:
            self.on_talk_event_list.remove(the_crisis)
    Person.remove_on_talk_event = remove_on_talk_event

    def remove_on_room_enter_event(self, the_crisis):
        if isinstance(the_crisis, basestring):
            found = next((x for x in self.on_room_enter_event_list if x.effect == the_crisis or x.name == the_crisis), None)
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

    def is_giving_birth(self):
        return self.location == purgatory or not self.available

    Person.is_giving_birth = is_giving_birth

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

    def number_of_children_with_mc(self):
        return self.sex_record.get("Children with MC", 0)
    Person.number_of_children_with_mc = number_of_children_with_mc

    def has_child_with_mc(self):
        return self.sex_record.get("Children with MC", 0) > 0
    Person.has_child_with_mc = has_child_with_mc

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

    def pregnancy_chance_string(self): #Turns the difference of days from her ideal fertile day into a string
        if persistent.pregnancy_pref == 2: # On realistic pregnancy a girls chance to become pregnant fluctuates over the month.
            preg_chance = self.calculate_realistic_fertility()
        else:
            preg_chance = self.fertility_percent

        if self.event_triggers_dict.get("birth_control_status", None) is None:
            preg_chance *= .5   # coin toss
        elif not self.on_birth_control:
            preg_chance *= .9
        else:
            preg_chance *= (.1 + (self.bc_penalty / 10))

        # mc.log_event("Pregnancy chance: " + self.name + ": " + str(preg_chance), "float_text_grey")

        if preg_chance < 3:
            return "Very Safe"
        elif preg_chance < 5:
            return "Safe"
        elif preg_chance < 10:
            return "Normal"
        elif preg_chance < 20:
            return "Risky"
        elif preg_chance < 40:
            return "Very Risky"
        else:
            return "Extremely Risky"

    Person.pregnancy_chance_string = pregnancy_chance_string

##########################################
# Position Specific functions            #
##########################################

    def unlock_spanking(self, add_to_log = True):
        if self.can_be_spanked():
            return False
        self.event_triggers_dict["unlock_spanking"] = True
        if add_to_log:
            mc.log_event((self.title or self.name) + " can now be spanked during sex.",  "float_text_green")
        return True

    def can_be_spanked(self):
        return self.event_triggers_dict.get("unlock_spanking", False)

    Person.unlock_spanking = unlock_spanking
    Person.can_be_spanked = can_be_spanked

##########################################
# Girl in Charge Functions               #
##########################################

    def set_sex_goal(self, the_goal):
        self.event_triggers_dict["sex_goal"] = the_goal
        return

    def get_sex_goal(self):
        return self.event_triggers_dict.get("sex_goal", None)

    def reset_sex_goal(self):
        self.event_triggers_dict["sex_goal"] = None
        return

    Person.set_sex_goal = set_sex_goal
    Person.get_sex_goal = get_sex_goal
    Person.reset_sex_goal = reset_sex_goal

##################################################
#    Body descriptor python wrappers             #
##################################################

    def body_is_thin(self):
        return self.body_type == "thin_body"

    def body_is_average(self):
        return self.body_type == "standard_body"

    def body_is_thick(self):
        return self.body_type == "curvy_body"

    def body_is_pregnant(self):
        return self.body_type == "standard_preg_body"

    Person.body_is_thin = body_is_thin
    Person.body_is_average = body_is_average
    Person.body_is_thick = body_is_thick
    Person.body_is_pregnant = body_is_pregnant

    def can_clone(self):
        if not genetic_manipulation_policy.is_owned():
            return False
        if self.has_role(clone_role):
            return False
        if self in unique_character_list:
            return False
        return True
    Person.can_clone = can_clone

##################################################
#     Fetish related wrappers                    #
##################################################

    def get_fetish_count(self):
        return __builtin__.len([x for x in self.special_role if x in [anal_fetish_role, cum_fetish_role, breeding_fetish_role, exhibition_fetish_role]])

    def get_fetishes_description(self):
        return ", ".join([x for x in self.special_role if x in [anal_fetish_role, cum_fetish_role, breeding_fetish_role, exhibition_fetish_role]])

    def has_anal_fetish(self):
        return self.has_role(anal_fetish_role)

    def has_cum_fetish(self):
        return self.has_role(cum_fetish_role)

    def has_breeding_fetish(self):
        return self.has_role([breeder_role, breeding_fetish_role])

    def has_exhibition_fetish(self):
        return self.has_role(exhibition_fetish_role)

    Person.get_fetish_count = get_fetish_count
    Person.get_fetishes_description = get_fetishes_description

    Person.has_anal_fetish = has_anal_fetish
    Person.has_cum_fetish = has_cum_fetish
    Person.has_breeding_fetish = has_breeding_fetish
    Person.has_exhibition_fetish = has_exhibition_fetish

    def has_started_anal_fetish(self):
        return self.event_triggers_dict.get("anal_fetish_start", False)

    def has_started_breeding_fetish(self):
        return self.event_triggers_dict.get("breeding_fetish_start", False)

    def has_started_cum_fetish(self):
        return self.event_triggers_dict.get("cum_fetish_start", False)

    def has_started_exhibition_fetish(self):
        return self.event_triggers_dict.get("exhibition_fetish_start", False)

    Person.has_started_anal_fetish = has_started_anal_fetish
    Person.has_started_breeding_fetish = has_started_breeding_fetish
    Person.has_started_cum_fetish = has_started_cum_fetish
    Person.has_started_exhibition_fetish = has_started_exhibition_fetish

    #Additional functions

    def is_submissive(self):
        return self.get_opinion_score("being submissive") > 0 \
            or (self.get_opinion_score("being submissive") > -2 and self.obedience > 150)

    Person.is_submissive = is_submissive

    def facial_or_swallow(self):    #Use this function to determine if girl wants a facial or to swallow cum. If neither is preferred, return one at random.
        if self.has_cum_fetish():
            return renpy.random.choice(["swallow", "facial"])
        if self.get_opinion_score("cum facials") == self.get_opinion_score("drinking cum"):
            return renpy.random.choice(["swallow", "facial"])
        if self.get_opinion_score("cum facials") > self.get_opinion_score("drinking cum"):
            return "facial"
        return "swallow"

    Person.facial_or_swallow = facial_or_swallow

    def is_jealous(self):
        if not (self.is_girlfriend() or self.is_affair()):
            return False

        if self == sarah and sarah_threesomes_unlocked():
            return False
        if self.love > 90 or self.obedience > 200:
            return False
        return self.event_triggers_dict.get("is_jealous", True)

    Person.is_jealous = is_jealous

    def have_orgasm(self, the_position = None, the_object = None, half_arousal = True, force_trance = False, trance_chance_modifier = 0, sluttiness_increase_limit = 30, reset_arousal = False, add_to_log = True):
        mc.listener_system.fire_event("girl_climax", the_person = self, the_position = the_position, the_object = the_object)

        self.run_orgasm(show_dialogue = add_to_log, force_trance = force_trance, trance_chance_modifier = trance_chance_modifier, add_to_log = add_to_log, sluttiness_increase_limit = sluttiness_increase_limit, reset_arousal = reset_arousal)
        self.change_happiness(3, add_to_log = add_to_log)

        if "report_log" in globals():
            report_log["girl orgasms"] = report_log.get("girl orgasms", 0) + 1

        if half_arousal:
            self.change_arousal(-self.arousal/2, add_to_log = add_to_log)
        elif "report_log" in globals():
            self.change_arousal(-self.arousal/(report_log.get("girl orgasms", 0)+2), add_to_log = add_to_log)
        else:
            self.change_arousal(-self.arousal, add_to_log = add_to_log)
        return

    Person.have_orgasm = have_orgasm

    def favorite_colour(self):
        favored_colour = self.event_triggers_dict.get("favorite_colour", None)

        #check if current favourite is still in list_of favourites
        list_of_favorites = [x for x in WardrobeBuilder.color_prefs.keys() if self.get_opinion_score(x) == 2]
        if favored_colour in list_of_favorites:
            return favored_colour

        #If not, we need to find a favorite colour going forward.
        if len(list_of_favorites) > 0:
            self.event_triggers_dict["favorite_colour"] = renpy.random.choice(list_of_favorites)
        else:
            self.event_triggers_dict["favorite_colour"] = renpy.random.choice(WardrobeBuilder.color_prefs.keys())
            self.update_opinion_with_score(self.event_triggers_dict["favorite_colour"], 2, add_to_log = False)
        return self.favorite_colour()

    Person.favorite_colour = favorite_colour

    def is_single(self):
        return self.relationship == "Single" and not self.is_girlfriend()

    Person.is_single = is_single

    # just check if has any trance_role, when training_available = True also check if we can train her
    def is_in_trance(self, training_available = False):
        return self.has_role([trance_role, heavy_trance_role, very_heavy_trance_role]) and \
            (not training_available or self.event_triggers_dict.get("trance_training_available", True))

    Person.is_in_trance = is_in_trance

    def is_free_use(self):  #Use this function to determine if the girl is very slutty and basically down for anything.
        if self.sluttiness < 80:
            return False
        for x in self.sexy_opinions: #Doesn't hate any sexual actions.
            if self.get_opinion_score(x) < -1:
                return False
        if self.has_taboo("vaginal_sex") or self.has_taboo("anal_sex"):
            return False
        return True

    Person.is_free_use = is_free_use

#Intern functions

    def is_intern(self):
        if self.has_role(college_intern_role):
            return True
        return False
    Person.is_intern = is_intern

##### Roleplay functions. Used in scenarios where MC is roleplaying with someone, EG, girlfriend

    def change_to_lingerie(self):
        if self.event_triggers_dict.get("girlfriend_sleepover_lingerie", None):
            self.apply_outfit(self.event_triggers_dict.pop("girlfriend_sleepover_lingerie"))
        elif self.event_triggers_dict.get("favorite_lingerie", None):
            self.apply_outfit(self.event_triggers_dict.get("favorite_lingerie", None))
        elif len(self.wardrobe.underwear_sets) > 0:
            self.apply_outfit(get_random_from_list(self.wardrobe.underwear_sets))
        else:
            self.apply_outfit(lingerie_wardrobe.pick_random_outfit())
        return

    Person.change_to_lingerie = change_to_lingerie

    def roleplay_mc_title_swap(self, new_title):
        self.event_triggers_dict["backup_mc_title"] = self.mc_title
        self.set_mc_title(new_title)
        return

    def roleplay_mc_title_revert(self):
        self.mc_title = self.event_triggers_dict.get("backup_mc_title", mc.name)
        return

    def roleplay_title_swap(self, new_title):
        self.event_triggers_dict["backup_title"] = self.title
        self.set_title(new_title)
        return

    def roleplay_title_revert(self):
        self.title = self.event_triggers_dict.get("backup_title", self.name)
        return

    def roleplay_possessive_title_swap(self, new_title):
        self.event_triggers_dict["backup_possessive_title"] = self.possessive_title
        self.set_possessive_title(new_title)
        return

    def roleplay_possessive_title_revert(self):
        self.possessive_title = self.event_triggers_dict.get("backup_possessive_title", self.name)
        return

    def roleplay_personality_swap(self, personality):
        self.event_triggers_dict["backup_personality"] = self.personality
        self.personality = personality
        return

    def roleplay_personality_revert(self):
        self.personality = self.event_triggers_dict.get("backup_personality", relaxed_personality)
        return

    Person.roleplay_mc_title_swap = roleplay_mc_title_swap
    Person.roleplay_mc_title_revert = roleplay_mc_title_revert
    Person.roleplay_title_swap = roleplay_title_swap
    Person.roleplay_title_revert = roleplay_title_revert
    Person.roleplay_possessive_title_swap = roleplay_possessive_title_swap
    Person.roleplay_possessive_title_revert = roleplay_possessive_title_revert
    Person.roleplay_personality_swap = roleplay_personality_swap
    Person.roleplay_personality_revert = roleplay_personality_revert


###### Story and hint related functions ######

    def has_story_dict(self):
        if self.event_triggers_dict.get("story_dict", False):
            return True
        return False

    def get_story_dict(self):
        return self.event_triggers_dict.get("story_dict", None)

    Person.has_story_dict = has_story_dict
    Person.get_story_dict = get_story_dict

    def story_love_list(self):  #Note, this is a generic list and is meant to be overloaded on a per character basis.
        return ["This character's love progress menu has not yet been created."]

    def story_lust_list(self):
        return ["This character's lust progress menu has not yet been created."]

    def story_teamup_list(self):
        return [[" ", "No teamups have been written for this character yet!"]]

    def story_other_list(self):
        return [""] #There is some default info here, so no need to add a generic text description

    Person.story_love_list = story_love_list
    Person.story_lust_list = story_lust_list
    Person.story_teamup_list = story_teamup_list
    Person.story_other_list = story_other_list
    Person.story_character_description = ""
