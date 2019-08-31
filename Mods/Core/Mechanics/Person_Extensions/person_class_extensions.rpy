init -1:
    python:
        def location(self): # Check what location a person is in e.g the_person.location() == downtown. Use to trigger events?
            for location in list_of_places:
                if self in location.people:
                    return location

        Person.location = location

        def add_follower(self): # Adds follower |
            if self not in list_of_followers:
                list_of_followers.append(self)
            return
        Person.add_follower = add_follower

        def remove_follower(self):
            if self in list_of_followers:
                list_of_followers.remove(self)
            return
        Person.remove_follower = remove_follower

        ## MATCH SKIN COLOR
        # Matches skin, body, face and expression images based on input of skin color
        def match_skin(self, color):
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

        ## CHANGE HEIGHT EXTENSION
        # Returns True when the persons height has changed; otherwise False
        # chance is probability percentage that height change for amount will occur (used by serums)
        def change_height(self, amount, chance):
            if amount == 0 or (self.height == .8 and amount < 0) or (self.height == 1 and amount > 0):
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

        def is_employee(self):
            employment_title = mc.business.get_employee_title(self)
            if employment_title != "None":
                return True
            return False

        Person.is_employee = is_employee

        def create_home_location(self):
            # check if we already have a home, if so exit
            if self.home:
                return

            self.home = Room(self.name + "'s home", self.name + "'s home", [], apartment_background, [], [], [], False, [0.5,0.5], visible = False, hide_in_known_house_map = False)
            self.home.link_locations_two_way(downtown)
            self.home.add_object(make_wall())
            self.home.add_object(make_floor())
            self.home.add_object(make_bed())
            self.home.add_object(make_window())
            list_of_places.append(self.home)

            # set the person schedule
            self.schedule = {0:self.home,1:None,2:None,3:None,4:self.home}
            return

        Person.create_home_location = create_home_location

        ## LEARN HOME EXTENSION
        def learn_home(self): # Adds the_person.home to mc.known_home_locations allowing it to be visited without having to go through date label
            if not self.home in mc.known_home_locations:
                mc.known_home_locations.append(self.home)
                return True # Returns true if it succeeds
            return False # Returns false otherwise, so it can be used for checks.

        # Adds learn_home function to the_person.
        Person.learn_home = learn_home

        ## STRIP OUTFIT TO MAX SLUTTINESS EXTENSION
        # Strips down the person to a clothing their are comfortable with (starting with top, before bottom)
        # narrator_messages: narrator voice after each item of clothing stripped, use '[person.<title>]' for titles and '[strip_choice.name]' for clothing item.
            # Can be an array of messages for variation in message per clothing item or just a single string or None for silent stripping
        # scene manager parameter is filled from that class so that all people present in scene are drawn
        def strip_outfit_to_max_sluttiness(self, top_layer_first = True, exclude_upper = False, exclude_lower = False, exclude_feet = True, narrator_messages = None, character_placement = None, temp_sluttiness_boost = 0, position = None, emotion = None, scene_manager = None):
            # internal function to strip top clothing first.
            def get_strip_choice_upper_first(outfit, top_layer_first = True, exclude_upper = False, exclude_lower = False, exclude_feet = True):
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
            msg_count = len(messages)

            test_outfit = self.outfit.get_copy()
            removed_something = False

            strip_choice = get_strip_choice_upper_first(test_outfit, top_layer_first, exclude_upper, exclude_lower, exclude_feet)
            # renpy.say("", strip_choice.name + "  (required: " + str(test_outfit.slut_requirement) +  ", sluttiness: " +  str(self.effective_sluttiness() + temp_sluttiness_boost) + ")")
            while strip_choice and self.judge_outfit(test_outfit, temp_sluttiness_boost):
                self.draw_animated_removal(strip_choice, character_placement = character_placement, position = position, emotion = emotion, scene_manager = scene_manager) #Draw the strip choice being removed from our current outfit
                self.outfit = test_outfit.get_copy() #Swap our current outfit out for the test outfit.
                if msg_count > 0:   # do we need to show a random message and replace titles and outfit name
                    msg_idx = renpy.random.randint(1, msg_count)
                    msg = messages[msg_idx - 1]
                    msg = msg.replace("[the_person.possessive_title]", self.possessive_title).replace("[the_person.title]", self.title).replace("[the_person.mc_title]", self.mc_title).replace("[strip_choice.name]", strip_choice.name)
                    renpy.say(None, msg)
                else:
                    renpy.pause(1) # if no message to show, wait a short while before automatically continue stripping

                strip_choice = get_strip_choice_upper_first(test_outfit, top_layer_first, exclude_upper, exclude_lower, exclude_feet)

            return removed_something

        # Monkey wrench Person class to have automatic strip function
        Person.strip_outfit_to_max_sluttiness = strip_outfit_to_max_sluttiness

        # BUGFIXED: Judge Outfit function uses the_person instead of self to check effective sluttiness
        #Judge an outfit and determine if it's too slutty or not. Can be used to judge other people's outfits to determine if she thinks they look like a slut.
        def judge_outfit_extension(self, outfit, temp_sluttiness_boost = 0):
            outfit.update_slut_requirement()    # reevaluate sluttiness requirement
            # renpy.say("", "Judge Outfit:  " + str(outfit.slut_requirement) +  "  (validation sluttiness: " +  str(self.effective_sluttiness() + temp_sluttiness_boost) + ")")
            return outfit.slut_requirement < (self.effective_sluttiness() + temp_sluttiness_boost)

        Person.judge_outfit = judge_outfit_extension

        # Person.run_move with fixes for "followers" to exclude them since it causes issues in certain circumstances.
        def run_move_followers_fix(self,location): #Move to the appropriate place for the current time unit, ie. where the player should find us.

            #Move the girl the appropriate location on the map. For now this is either a division at work (chunks 1,2,3) or downtown (chunks 0,5). TODO: add personal homes to all girls that you know above a certain amount.

            self.sexed_count = 0 #Reset the counter for how many times you've been seduced, you might be seduced multiple times in one day!

            if time_of_day == 0: #It's a new day, get a new outfit out to wear!
                self.planned_outfit = self.wardrobe.decide_on_outfit2(self) # Use enhanced outfit selector
                self.outfit = self.planned_outfit.get_copy()
                self.planned_uniform = None

            destination = self.schedule[time_of_day] #None destination means they have free time
            if destination == self.work and not mc.business.is_open_for_business(): #NOTE: Right now we give everyone time off based on when the mc has work scheduled.
                destination = None

            if destination is not None: #We have somewhere scheduled to be for this time chunk. Let's move over there.
                if self not in list_of_followers: # NOTE: For the followers fix we only care about having them stay with the MC. Let the rest carry on as per usual.
                    location.move_person(self, destination) #Always go where you're scheduled to be.
                if self.schedule[time_of_day] == self.work: #We're going to work.
                    if self.should_wear_uniform(): #Get a uniform if we should be wearing one.
                        self.wear_uniform()
                        self.change_happiness(self.get_opinion_score("work uniforms"),add_to_log = False)
                        if self.planned_uniform and self.planned_uniform.slut_requirement > self.sluttiness*0.75: #A skimpy outfit/uniform is defined as the top 25% of a girls natural sluttiness.
                            self.change_slut_temp(self.get_opinion_score("skimpy uniforms"), add_to_log = False)

                elif destination == self.home:
                    self.outfit = self.planned_outfit.get_copy() #We're at home, so we can get back into our casual outfit.

                #NOTE: There is no else here because all of the destination should be set. If it's just a location they travel there and that's the end of it.

            else:
                #She finds somewhere to burn some time
                self.outfit = self.planned_outfit.get_copy() #Get changed back into our proper outfit if we aren't in it already.
                available_locations = [] #Check to see where is public (or where you are white listed) and move to one of those locations randomly
                for potential_location in list_of_places:
                    if potential_location.public:
                        available_locations.append(potential_location)
                if self not in list_of_followers:
                    location.move_person(self, get_random_from_list(available_locations))

            #We do uniform/outfit checks in run move because it happens at the _start_ of the time chunk. The girl looks forward to wearing her outfit (or dreads it) rather than responds to actually doing it.
            if self.outfit and self.planned_outfit.slut_requirement > self.sluttiness*0.75: #A skimpy outfit is defined as the top 25% of a girls natural sluttiness.
                self.change_slut_temp(self.get_opinion_score("skimpy outfits"), add_to_log = False)
            elif self.outfit and self.planned_outfit.slut_requirement < self.sluttiness*0.25: #A conservative outfit is defined as the bottom 25% of a girls natural sluttiness.
                self.change_happiness(self.get_opinion_score("conservative outfits"), add_to_log = False)

            if self.outfit.tits_available() and self.outfit.tits_visible() and self.outfit.vagina_available() and self.outfit.vagina_visible():
                self.change_slut_temp(self.get_opinion_score("not wearing anything"), add_to_log = False)

            if not self.outfit.wearing_bra() or not self.outfit.wearing_panties(): #We need to determine how much underwear they are not wearing. Each piece counts as half, so a +2 "love" is +1 slut per chunk.
                underwear_bonus = 0
                if not self.outfit.wearing_bra():
                    underwear_bonus += self.get_opinion_score("not wearing underwear")
                if not self.outfit.wearing_panties():
                    underwear_bonus += self.get_opinion_score("not wearing underwear")
                underwear_bonus = __builtin__.int(underwear_bonus/2.0) #I believe this rounds towards 0. No big deal if it doesn't, very minor detail.
                self.change_slut_temp(underwear_bonus, add_to_log = False)

            if self.outfit.tits_visible():
                self.change_slut_temp(self.get_opinion_score("showing her tits"), add_to_log = False)
            if self.outfit.vagina_visible():
                self.change_slut_temp(self.get_opinion_score("showing her ass"), add_to_log = False)

            if self.outfit.get_bra() or self.outfit.get_panties():
                lingerie_bonus = 0
                if self.outfit.get_bra() and self.outfit.get_bra().slut_value > 1: #We consider underwear with an innate sluttiness of 2 or higher "lingerie" rather than just underwear.
                    lingerie_bonus += self.get_opinion_score("lingerie")
                if self.outfit.get_panties() and self.outfit.get_panties().slut_value > 1:
                    lingerie_bonus += self.get_opinion_score("lingerie")
                lingerie_bonus = __builtin__.int(lingerie_bonus/2.0)
                self.change_slut_temp(lingerie_bonus, add_to_log = False)

        Person.run_move = run_move_followers_fix # Excludes followers from moving, but maintain outfit calculations.

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

        ## Increase the opinion on a specific topic (opinion)
        def increase_opinion_score(self, topic, add_to_log = True):
            sexy_opinion = False
            if topic in sexy_opinions_list:
                sexy_opinion = True
            elif not topic in opinions_list:
                return # unknown opinion, so exit function

            score = 0
            if sexy_opinion:
                score = self.sexy_opinions[topic][0]
            else:
                score = self.opinions[topic][0]

            if score < 2:
                score += 1

            if sexy_opinion:
                self.sexy_opinions[topic][0] = score
            else:
                self.opinions[topic][0] = score

            if add_to_log:
                mc.log_event((self.title or self.name) + " " + opinion_score_to_string(score) + " " + str(topic), "float_text_green")
            return
        # Add increase opinion function to person class
        Person.increase_opinion_score = increase_opinion_score

        ## Decrease the opinion on a specific topic (opinion)
        def decrease_opinion_score(self, topic, add_to_log = True):
            sexy_opinion = False
            if topic in sexy_opinions_list:
                sexy_opinion = True
            elif not topic in opinions_list:
                return # unknown opinion, so exit function

            score = 0
            if sexy_opinion:
                score = self.sexy_opinions[topic][0]
            else:
                score = self.opinions[topic][0]

            if score > -2:
                score -= 1

            if sexy_opinion:
                self.sexy_opinions[topic][0] = score
            else:
                self.opinions[topic][0] = score

            if add_to_log:
                mc.log_event((self.title or self.name) + " " + opinion_score_to_string(score) + " " + str(topic), "float_text_green")
            return
        # Add decrease opinion function to person class
        Person.decrease_opinion_score = decrease_opinion_score

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

        ## CHANGE WILLPOWER EXTENSION
        # changes the willpower of a person by set amount
        def change_willpower(self, amount): #Logs change in willpower and shows new total.
            self.willpower += amount
            if self.willpower < 0:
                self.willpower = 0
            return person.willpower

        # attach to person object
        Person.change_willpower = change_willpower

        def review_outfit_enhanced(self, show_review_message = True):
            self.outfit.remove_all_cum()

            if self.should_wear_uniform():
                self.wear_uniform() # Reset uniform
            else:
                self.outfit.update_slut_requirement()
                if self.outfit.slut_requirement > self.sluttiness and show_review_message:
                    self.call_dialogue("clothing_review")
                self.outfit = self.planned_outfit.get_copy()    #restore outfit

        Person.review_outfit = review_outfit_enhanced

        def draw_person_enhanced(self,position = None, emotion = None, special_modifier = None, show_person_info = True, character_placement = None, from_scene = False): #Draw the person, standing as default if they aren't standing in any other position.
            if position is None:
                position = self.idle_pose

            if emotion is None:
                emotion = self.get_emotion()

            if character_placement is None: # make sure we don't need to pass the position with each draw
                character_placement = character_right

            # sometimes there is no outfit set, causeing the generate drawlist to fail, not sure why, but try to fix it here.
            if self.outfit is None:
                if self.planned_outfit is None:
                    self.planned_outfit = self.wardrobe.decide_on_outfit2(self) # Use enhanced outfit function
                self.outfit = self.planned_outfit.get_copy()
                self.review_outfit(show_review_message = False)

            # if normal draw person call, clear scene
            if not from_scene:
                renpy.scene("Active")
                if show_person_info:
                    renpy.show_screen("person_info_ui",self)

            final_image = self.build_person_displayable(position, emotion, special_modifier, show_person_info)
            renpy.show(self.name,at_list=[character_placement, scale_person(self.height)],layer="Active",what=final_image,tag=(self.name + self.last_name + str(self.age)))

        # replace the default draw_person function of the person class
        Person.draw_person = draw_person_enhanced
        # add location to store original personality
        Person.original_personality = None

        def draw_animated_removal_enhanced(self, the_clothing, position = None, emotion = None, special_modifier = None, character_placement = None, scene_manager = None): #A special version of draw_person, removes the_clothing and animates it floating away. Otherwise draws as normal.
            #Note: this function includes a call to remove_clothing, it is not needed seperately.
            if position is None:
                position = self.idle_pose

            bottom_displayable = [] #Displayables under the piece of clothing being removed.
            top_displayable = []

            if emotion is None:
                emotion = self.get_emotion()

            if character_placement is None: # make sure we don't need to pass the position with each draw
                character_placement = character_right

            renpy.scene("Active") # clear layer for new draw action
            if scene_manager is None:
                renpy.show_screen("person_info_ui",self)
            else:   # when we are called from the scenemanager we have to draw the other characters
                scene_manager.draw_scene_without(self)

            bottom_displayable.append(self.expression_images.generate_emotion_displayable(position,emotion, special_modifier = special_modifier)) #Get the face displayable, also always under clothing.

            bottom_displayable.append(self.body_images.generate_item_displayable(self.body_type,self.tits,position))  #Body is always under clothing
            size_render = renpy.render(bottom_displayable[1], 10, 10, 0, 0) #We need a render object to check the actual size of the body displayable so we can build our composite accordingly.
            the_size = size_render.get_size()
            x_size = __builtin__.int(the_size[0])
            y_size = __builtin__.int(the_size[1])

            bottom_clothing, split_clothing, top_clothing = self.outfit.generate_split_draw_list(the_clothing, self, position, emotion, special_modifier) #Gets a split list of all of our clothing items.
            #We should remember that middle item can be None.
            for item in bottom_clothing:
                bottom_displayable.append(item)

            for item in top_clothing:
                top_displayable.append(item)

            top_displayable.append(self.hair_style.generate_item_displayable("standard_body",self.tits,position)) #Hair is always on top

            #Now we build our two composites, one for the bottom image and one for the top.
            composite_bottom_params = [(x_size,y_size)]
            for display in bottom_displayable:
                composite_bottom_params.append((0,0))
                composite_bottom_params.append(display)

            composite_top_params = [(x_size,y_size)]
            for display in top_displayable:
                composite_top_params.append((0,0))
                composite_top_params.append(display)

            final_bottom = Composite(*composite_bottom_params)
            final_top = Composite(*composite_top_params)

            renpy.show("Bottom Composite", at_list=[character_placement, scale_person(self.height)], layer="Active", what=final_bottom, tag=self.name+"Bottom")
            if split_clothing: #Only show this if we actually had something returned to us.
                renpy.show("Removed Item", at_list=[character_placement, scale_person(self.height), clothing_fade], layer="Active", what=split_clothing, tag=self.name+"Middle")
                self.outfit.remove_clothing(the_clothing)
            renpy.show("Top Composite", at_list=[character_placement, scale_person(self.height)], layer="Active", what=final_top, tag=self.name+"Top")

        Person.draw_animated_removal = draw_animated_removal_enhanced

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
            if (person is mc):
                message = "Your: " + str(person.power)
            else:
                message = (person.title or person.name) + ": " + str(person.willpower)
            message += " Willpower"
            mc.log_event(message, "float_text_blue")
            return
