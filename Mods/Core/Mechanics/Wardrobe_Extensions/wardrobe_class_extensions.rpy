init -1 python:
    # Get an overwear outfit that is considered appropriate based on sluttines and preferences.
    def get_random_appropriate_overwear_enhanced(self, sluttiness_limit, sluttiness_min = 0, preferences = None):
        if preferences == None:
            preferences = WardrobePreference()

        valid_overwear = []
        for overwear in self.overwear_sets:
            if preferences.evaluate_outfit(overwear, sluttiness_limit, sluttiness_min):
                valid_overwear.append(overwear)

        the_outfit = get_random_from_list(valid_overwear)
        if the_outfit:
            return the_outfit.get_copy()
        else:
            return None

    Wardrobe.get_random_appropriate_overwear = get_random_appropriate_overwear_enhanced

    # Get a copy of a full outfit that is considered appropriate based on sluttiness and preferences.
    def get_random_appropriate_outfit_enhanced(self, sluttiness_limit, sluttiness_min = 0, preferences = None): 
        if preferences == None:
            preferences = WardrobePreference()

        valid_outfits = []
        for outfit in self.outfits:
            if preferences.evaluate_outfit(outfit, sluttiness_limit, sluttiness_min):
                valid_outfits.append(outfit)

        the_outfit = get_random_from_list(valid_outfits)
        if the_outfit:
            return the_outfit.get_copy()
        else:
            return None

    Wardrobe.get_random_appropriate_outfit = get_random_appropriate_outfit_enhanced

    def get_random_appropriate_underwear_enhanced(self, sluttiness_limit, sluttiness_min = 0, preferences = None): #Get an underwear outfit that is considered appropriate (based on underwear sluttiness, not full outfit sluttiness)
        if preferences == None:
            preferences = WardrobePreference()

        valid_underwear = []
        for underwear in self.underwear_sets:
            if preferences.evaluate_underwear(underwear, sluttiness_limit, sluttiness_min):
                valid_underwear.append(underwear)

        if not valid_underwear:
            for underwear in self.underwear_sets:
                if underwear.get_underwear_slut_score() <= sluttiness_limit and underwear.get_underwear_slut_score() >= sluttiness_min:
                    valid_underwear.append(underwear)

        if valid_underwear:
            return get_random_from_list(valid_underwear).get_copy()
        else:
            return None

    Wardrobe.get_random_appropriate_underwear = get_random_appropriate_underwear_enhanced

    def pick_outfit_with_lowest_sluttiness(self):
        selected_outfit = None
        for outfit in self.outfits:
            if selected_outfit == None or outfit.get_full_outfit_slut_score() < selected_outfit.get_full_outfit_slut_score():
                selected_outfit = outfit

        return outfit.get_copy() # Get a copy of _any_ full outfit in this character's wardrobe.

    Wardrobe.pick_outfit_with_lowest_sluttiness = pick_outfit_with_lowest_sluttiness

    def calculate_minimum_sluttiness(person, target_sluttiness):
        minimum_sluttiness = target_sluttiness - person.sluttiness # raise minimum sluttiness by the amount over normal sluttiness
        if target_sluttiness > 40 and minimum_sluttiness == 0: # when there is no minimum sluttiness, increase it when the girl is slutty
            minimum_sluttiness = (target_sluttiness - 40) // 2
        if minimum_sluttiness > 40: # prevent minimum sluttiness from going too high (late game, high sluttiness)
            minimum_sluttiness = 40
        if target_sluttiness > 100 and minimum_sluttiness < 30: # when very slutty, don't bother with non-sexy clothes.
            minimum_sluttiness = 30
        return minimum_sluttiness

    def build_assembled_outfit(outfit_under, outfit_over):
        assembled_outfit = outfit_under.get_copy()
        assembled_outfit.name = outfit_under.name + " + " + outfit_over.name

        # renpy.say("", "Assembled outfit: " + assembled_outfit.name)

        for upper in outfit_over.upper_body:
            assembled_outfit.upper_body.append(upper.get_copy())

        for lower in outfit_over.lower_body:
            assembled_outfit.lower_body.append(lower.get_copy())

        for feet_wear in outfit_over.feet:
            assembled_outfit.feet.append(feet_wear.get_copy())

        for acc in outfit_over.accessories:
            assembled_outfit.accessories.append(acc.get_copy())

        assembled_outfit.update_slut_requirement()
        return assembled_outfit


    # Girls choose the work uniform based on sluttiness and opinion modifiers instead of random
    # Creates a uniform out of the clothing items from this wardrobe. 
    # When no company parts are available a girls personal wardrobe will be used for constructed uniforms.
    def decide_on_uniform_enhanced(self, person): 
        conservative_score = person.get_opinion_score("conservative outfits") / 20 # high impact on sluttiness
        skimpy_uniform_score = person.get_opinion_score("skimpy uniforms") / 20
        work_uniforms_score = person.get_opinion_score("work uniforms") / 30 # low impact on sluttiness
        marketing_score = 0
        # girls working in marketing know they make more sales when wearing a sluttier outfit, so this affects their uniform choice
        if male_focused_marketing_policy.is_owned() and mc.business.get_employee_title(person) == "Marketing":
            marketing_score = .1

        # modify target sluttiness based on opinions
        target_sluttiness = person.sluttiness * (1 + skimpy_uniform_score + work_uniforms_score + marketing_score - conservative_score)
        minimum_sluttiness = calculate_minimum_sluttiness(person, target_sluttiness)

        preferences = WardrobePreference(person)

        if len(self.outfits) > 0:
            #We have some full body outfits we mgiht use. 50/50 to use that or a constructed outfit.
            outfit_choice = renpy.random.randint(0,100)
            chance_to_use_full = 50 #Like normal outfits a uniform hasa 50/50 chance of being a full outfit or an assembled outfit if both are possible.

            #If we roll use full or we don't have the parts to make an assembled outfit.
            if outfit_choice > chance_to_use_full or len(self.underwear_sets + self.overwear_sets) == 0:
                full_outfit = None
                count = 0

                while not full_outfit and count < 4:    # Try to find a valid uniform by stretching the sluttiness range, returns none when not succesfull
                    full_outfit = self.get_random_appropriate_outfit(target_sluttiness + (count * 2), minimum_sluttiness - (count * 10), preferences)
                    count += 1

                if not full_outfit: # fallback if we cannot find anything for our sluttiness or preferences
                    full_outfit = self.pick_outfit_with_lowest_sluttiness()

                return full_outfit
                
        elif len(self.underwear_sets + self.overwear_sets) == 0:
            #We have nothing else to make a uniform out of. Return None and let the pick uniform function handle that.
            return None

        #If we get to here we are assembling an outfit out of underwear or overwear.
        uniform_over = None
        count = 0
        while not uniform_over and count < 4:   # Try to find a valid uniform by stretching the sluttiness range, returns none when not succesfull
            uniform_over = self.get_random_appropriate_overwear(target_sluttiness + (count * 2), minimum_sluttiness - (count * 10), preferences)
            count += 1

        if uniform_over:
            slut_limit_remaining = target_sluttiness - uniform_over.get_overwear_slut_score()
            if slut_limit_remaining < 0:
                slut_limit_remaining = 0

            #We got a top, now get a bottom.
            uniform_under = self.get_random_appropriate_underwear(slut_limit_remaining, preferences = preferences)
            if not uniform_under:
                #We need to get a bottom from her personal wardrobe. We also want to make sure it's something she would personally wear.
                uniform_under = person.wardrobe.get_random_appropriate_underwear(slut_limit_remaining, preferences = preferences)

        else:
            #There are no tops, so we're going to try and get a bottom and use one of the persons tops.
            uniform_under = self.get_random_appropriate_underwear(target_sluttiness, minimum_sluttiness, preferences)
            if not uniform_under:
                # no underwear that fits sluttiness, get one from her personal wardrobe
                uniform_under = person.wardrobe.get_random_appropriate_underwear(target_sluttiness, preferences = preferences)

            if uniform_under:
                slut_limit_remaining = target_sluttiness - uniform_under.get_underwear_slut_score()
                if slut_limit_remaining < 0:
                    slut_limit_remaining = 0 #If the outfit is so slutty we're not comfortable in it we'll try and wear the most conservative overwear we can.

                uniform_over = person.wardrobe.get_random_appropriate_overwear(slut_limit_remaining, preferences = preferences)

        #At this point we have our under and over, if at all possible.
        if not uniform_over or not uniform_under:
            return None #Something's gone wrong and we don't have one of our sets. return None and let the uniform gods sort it out.

        return build_assembled_outfit(uniform_under, uniform_over)

    # replace default uniform descission function
    Wardrobe.decide_on_uniform = decide_on_uniform_enhanced

    # An outfit selector that takes personal preferences into account
    def decide_on_outfit_enhanced(self, person, sluttiness_modifier = 0.0):
        conservative_score = person.get_opinion_score("conservative outfits") / 20 # high impact on sluttiness
        skimpy_outfit_score = person.get_opinion_score("skimpy outfits") / 20

        target_sluttiness = person.sluttiness * (1 + skimpy_outfit_score + sluttiness_modifier - conservative_score)
        minimum_sluttiness = calculate_minimum_sluttiness(person, target_sluttiness)

        preferences = WardrobePreference(person)

        if len(self.outfits) > 0:
            #We have some full body outfits we might use. 50/50 to use that or a constructed outfit.
            outfit_choice = renpy.random.randint(0,100)
            chance_to_use_full = 50 # 50/50 chance of being a full outfit or an assembled outfit if both are possible.

            #If we roll use full or we don't have the parts to make an assembled outfit.
            if outfit_choice > chance_to_use_full or len(self.underwear_sets + self.overwear_sets) == 0:
                full_outfit = None
                count = 0
                while not full_outfit and count < 4:    # Try to find a valid outfit by stretching the sluttiness range, returns none when not succesfull               
                    full_outfit = self.get_random_appropriate_outfit(target_sluttiness + (count * 2), minimum_sluttiness - (count * 10), preferences)
                    count += 1

                if not full_outfit: # fallback if we cannot find anything for our sluttiness or preferences
                    full_outfit = self.pick_outfit_with_lowest_sluttiness()

                return full_outfit
                
        elif len(self.underwear_sets + self.overwear_sets) == 0:
            #We have nothing else to make a uniform out of. Use default builder function.
            return default_wardrobe.build_appropriate_outfit(target_sluttiness, minimum_sluttiness)

        #If we get to here we are assembling an outfit out of underwear or overwear.
        outfit_over = None
        count = 0
        while not outfit_over and count < 4:   # Try to find a valid uniform by stretching the sluttiness range, returns none when not succesfull
            outfit_over = self.get_random_appropriate_overwear(target_sluttiness + (count * 5), minimum_sluttiness - (count * 10), preferences)
            count += 1

        if outfit_over:
            slut_limit_remaining = target_sluttiness - outfit_over.get_overwear_slut_score()
            if slut_limit_remaining < 0:
                slut_limit_remaining = 0

            #We got a top, now get a bottom.
            outfit_under = self.get_random_appropriate_underwear(slut_limit_remaining, preferences = preferences)
            if not outfit_under:
                #We need to get a bottom from the default wardrobe. We also want to make sure it's something she would personally wear.
                outfit_under = default_wardrobe.get_random_appropriate_underwear(slut_limit_remaining, preferences = preferences)
        else:
            #There are no tops, so we're going to try and get a bottom and use one of the default wardrobe tops.
            outfit_under = self.get_random_appropriate_underwear(target_sluttiness, minimum_sluttiness, preferences)
            if not outfit_under:
                # no underwear that fits sluttiness, get one from the default wardrobe
                outfit_under = default_wardrobe.get_random_appropriate_underwear(target_sluttiness, preferences = preferences)

            if outfit_under:
                slut_limit_remaining = target_sluttiness - outfit_under.get_underwear_slut_score()
                if slut_limit_remaining < 0:
                    slut_limit_remaining = 0 #If the outfit is so slutty we're not comfortable in it we'll try and wear the most conservative overwear we can.

                outfit_over = person.wardrobe.get_random_appropriate_overwear(slut_limit_remaining, preferences = preferences)
                if not outfit_over:
                    outfit_over = default_wardrobe.get_random_appropriate_overwear(slut_limit_remaining, preferences = preferences)

        #At this point we have our under and over, if at all possible.
        if not outfit_over or not outfit_under:
            return default_wardrobe.build_appropriate_outfit(target_sluttiness, minimum_sluttiness) # Use default builder to create an outfit

        return build_assembled_outfit(outfit_under, outfit_over)

    Wardrobe.decide_on_outfit2 = decide_on_outfit_enhanced

# add some overwear with boots
init 2 python:
    business_overwear_1 = Outfit("Business Overwear 1")
    business_overwear_1.add_upper(sleeveless_top.get_copy(),colour_white)
    business_overwear_1.add_upper(suit_jacket.get_copy(),colour_black)
    business_overwear_1.add_accessory(gold_earings.get_copy(),colour_white)
    business_overwear_1.add_feet(tall_boots.get_copy(),colour_black)
    business_overwear_1.add_lower(capris.get_copy(),colour_black)
    default_wardrobe.add_overwear_set(business_overwear_1)

    business_overwear_2 = Outfit("Business Overwear 2")
    business_overwear_2.add_upper(sweater.get_copy(),colour_white)
    business_overwear_2.add_accessory(gold_earings.get_copy(),colour_white)
    business_overwear_2.add_accessory(modern_glasses.get_copy(),colour_white)
    business_overwear_2.add_feet(tall_boots.get_copy(),colour_black)
    business_overwear_2.add_lower(pencil_skirt.get_copy(),colour_black)
    default_wardrobe.add_overwear_set(business_overwear_2)

    sexy_overwear_7 = Outfit("Sexy Overwear 7")
    sexy_overwear_7.add_upper(belted_top.get_copy(),colour_white)
    sexy_overwear_7.add_accessory(gold_earings.get_copy(),colour_white)
    sexy_overwear_7.add_feet(tall_boots.get_copy(),colour_black)
    sexy_overwear_7.add_lower(mini_skirt.get_copy(),colour_black)
    default_wardrobe.add_overwear_set(sexy_overwear_7)

    sexy_overwear_8 = Outfit("Sexy Overwear 8")
    sexy_overwear_8.add_upper(two_part_dress.get_copy(),colour_white)
    sexy_overwear_8.add_accessory(gold_earings.get_copy(),colour_white)
    sexy_overwear_8.add_feet(tall_boots.get_copy(),colour_white)
    default_wardrobe.add_overwear_set(sexy_overwear_8)
