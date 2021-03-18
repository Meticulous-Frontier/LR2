init -1 python:
    # Get an overwear outfit that is considered appropriate based on sluttiness and preferences.
    def get_random_appropriate_overwear_enhanced(self, sluttiness_limit, sluttiness_min = 0, guarantee_output = False, preferences = None):
        if preferences is None:
            preferences = WardrobePreference()

        if sluttiness_min < 0:
            sluttiness_min = 0

        valid_overwear = []
        for overwear in self.overwear_sets:
            if preferences.evaluate_outfit(overwear, sluttiness_limit, sluttiness_min):
                valid_overwear.append(overwear)

        if not valid_overwear:  # when we find no valid items, only validate sluttiness score
            for overwear in self.overwear_sets:
                if overwear.get_overwear_slut_score() <= sluttiness_limit and overwear.get_overwear_slut_score() >= sluttiness_min:
                    valid_overwear.append(overwear)

        the_outfit = get_random_from_list(valid_overwear)
        if the_outfit:
            return the_outfit.get_copy()
        else:
            if guarantee_output:
                if sluttiness_limit < 120:
                    return self.get_random_appropriate_overwear(sluttiness_limit+5, sluttiness_min-5, guarantee_output, preferences)
                else:
                    return Outfit("Nothing")
            return None

    Wardrobe.get_random_appropriate_overwear = get_random_appropriate_overwear_enhanced

    # Get a copy of a full outfit that is considered appropriate based on sluttiness and preferences.
    def get_random_appropriate_outfit_enhanced(self, sluttiness_limit, sluttiness_min = 0, guarantee_output = False, preferences = None):
        if preferences is None:
            preferences = WardrobePreference()

        if sluttiness_min < 0:
            sluttiness_min = 0

        valid_outfits = []
        for outfit in self.outfits:
            if preferences.evaluate_outfit(outfit, sluttiness_limit, sluttiness_min):
                valid_outfits.append(outfit)

        if not valid_outfits: # when we find no valid items, only validate sluttiness score
            for outfit in self.outfits:
                if outfit.get_full_outfit_slut_score() <= sluttiness_limit and outfit.get_full_outfit_slut_score() >= sluttiness_min:
                    valid_outfits.append(outfit)

        the_outfit = get_random_from_list(valid_outfits)
        if the_outfit:
            return the_outfit.get_copy()
        else:
            if guarantee_output:
                if sluttiness_limit < 120:
                    return self.get_random_appropriate_outfit(sluttiness_limit+5, sluttiness_min-5, guarantee_output, preferences)
                else:
                    return Outfit("Nothing")
            return None

    Wardrobe.get_random_appropriate_outfit = get_random_appropriate_outfit_enhanced

    def get_random_appropriate_underwear_enhanced(self, sluttiness_limit, sluttiness_min = 0, guarantee_output = False, preferences = None): #Get an underwear outfit that is considered appropriate (based on underwear sluttiness, not full outfit sluttiness)
        if preferences is None:
            preferences = WardrobePreference()

        if sluttiness_min < 0:
            sluttiness_min = 0

        valid_underwear = []
        for underwear in self.underwear_sets:
            if preferences.evaluate_underwear(underwear, sluttiness_limit, sluttiness_min):
                valid_underwear.append(underwear)

        if not valid_underwear: # when we find no valid items, only validate sluttiness score
            for underwear in self.underwear_sets:
                if underwear.get_underwear_slut_score() <= sluttiness_limit and underwear.get_underwear_slut_score() >= sluttiness_min:
                    valid_underwear.append(underwear)

        if valid_underwear:
            return get_random_from_list(valid_underwear).get_copy()
        else:
            if guarantee_output: # If an output is guaranteed we always return an Outfit object (even if it is empty). Otherwise we return None to indicate failure to find something.
                if sluttiness_limit < 120: #Sets an effective recursion limit.
                    return self.get_random_appropriate_underwear(sluttiness_limit+5, sluttiness_min-5, guarantee_output, preferences)
                else:
                    return Outfit("Nothing")

            else:
                return None

    Wardrobe.get_random_appropriate_underwear = get_random_appropriate_underwear_enhanced

    def pick_outfit_with_lowest_sluttiness(self):
        selected_outfit = None
        for outfit in self.outfits:
            if selected_outfit is None or outfit.get_full_outfit_slut_score() < selected_outfit.get_full_outfit_slut_score():
                selected_outfit = outfit

        return selected_outfit.get_copy() # Get a copy of _any_ full outfit in this character's wardrobe.

    Wardrobe.pick_outfit_with_lowest_sluttiness = pick_outfit_with_lowest_sluttiness

    def pick_overwear_with_lowest_sluttiness(self):
        selected_overwear = None
        for overwear in self.overwear_sets:
            if selected_overwear is None or overwear.get_overwear_slut_score() < selected_overwear.get_overwear_slut_score():
                selected_overwear = overwear

        if selected_overwear:
            return selected_overwear.get_copy()
        return None

    Wardrobe.pick_overwear_with_lowest_sluttiness = pick_overwear_with_lowest_sluttiness

    def pick_underwear_with_lowest_sluttiness(self):
        selected_underwear = None
        for underwear in self.underwear_sets:
            if selected_underwear is None or underwear.get_underwear_slut_score() < selected_underwear.get_underwear_slut_score():
                selected_underwear = underwear

        if selected_underwear:
            return selected_underwear.get_copy()
        return None

    Wardrobe.pick_underwear_with_lowest_sluttiness = pick_underwear_with_lowest_sluttiness

    def wardrobe_remove_outfit(self, outfit):
        for store in [self.outfits, self.underwear_sets, self.overwear_sets]:
            if isinstance(outfit, basestring):
                found = find_in_list(lambda x: x.name == outfit, store)
                if found:
                    store.remove(found)
            elif outfit in store:
                store.remove(outfit)

    Wardrobe.remove_outfit = wardrobe_remove_outfit

    def wardrobe_has_outfit_with_name(self, the_name):
        return any(x for x in self.outfits + self.underwear_sets + self.overwear_sets if x.name == the_name)

    Wardrobe.has_outfit_with_name = wardrobe_has_outfit_with_name

    def wardrobe_get_outfit_with_name(self, the_name):
        found = next((x for x in self.outfits + self.underwear_sets + self.overwear_sets if x.name == the_name), None)
        if found:
            return found.get_copy()
        return None

    Wardrobe.get_outfit_with_name = wardrobe_get_outfit_with_name


    def calculate_minimum_sluttiness(person, target_sluttiness):
        minimum_sluttiness = target_sluttiness - person.sluttiness # raise minimum sluttiness by the amount over normal sluttiness
        if target_sluttiness > 40 and minimum_sluttiness == 0: # when there is no minimum sluttiness, increase it when the girl is slutty
            minimum_sluttiness = (target_sluttiness - 40) // 2
        if minimum_sluttiness > 40: # prevent minimum sluttiness from going too high (late game, high sluttiness)
            minimum_sluttiness = 40
        if target_sluttiness > 100 and minimum_sluttiness < 20: # when very slutty, don't bother with non-sexy clothes.
            minimum_sluttiness = 20 + minimum_sluttiness
        return minimum_sluttiness

    def build_assembled_outfit(outfit_under, outfit_over):
        assembled_outfit = outfit_under.get_copy()
        assembled_outfit.name = outfit_under.name + " + " + outfit_over.name

        # renpy.say(None, "Assembled outfit: " + assembled_outfit.name)

        for upper in outfit_over.upper_body:
            assembled_outfit.upper_body.append(upper.get_copy())

        for lower in outfit_over.lower_body:
            assembled_outfit.lower_body.append(lower.get_copy())

        for feet_wear in outfit_over.feet:
            assembled_outfit.feet.append(feet_wear.get_copy())

        for acc in outfit_over.accessories:
            assembled_outfit.accessories.append(acc.get_copy())
        return assembled_outfit

    def get_random_appropriate_outfit_from_wardrobes(wardrobe, person, slut_limit_remaining, preferences):
        # We also want to make sure it's something she would personally wear.
        # current wardrobe
        outfit = wardrobe.get_random_appropriate_outfit(slut_limit_remaining, preferences = preferences)
        if not outfit:
            # We need to get a bottom from her personal wardrobe.
            outfit = person.wardrobe.get_random_appropriate_outfit(slut_limit_remaining, preferences = preferences)
            if not outfit:
                # Dive into the default wardrobe
                outfit = default_wardrobe.get_random_appropriate_outfit(slut_limit_remaining, preferences = preferences)

        return outfit

    def get_random_appropriate_underwear_from_wardrobes(wardrobe, person, slut_limit_remaining, preferences):
        # We also want to make sure it's something she would personally wear.
        # current wardrobe
        underwear = wardrobe.get_random_appropriate_underwear(slut_limit_remaining, preferences = preferences)
        if not underwear:
            # We need to get a bottom from her personal wardrobe.
            underwear = person.wardrobe.get_random_appropriate_underwear(slut_limit_remaining, preferences = preferences)
            if not underwear:
                # Dive into the default wardrobe
                underwear = default_wardrobe.get_random_appropriate_underwear(slut_limit_remaining, preferences = preferences)
        return underwear

    def get_random_appropriate_overwear_from_wardrobes(wardrobe, person, slut_limit_remaining, preferences):
        # We also want to make sure it's something she would personally wear.
        # current wardrobe
        overwear = wardrobe.get_random_appropriate_overwear(slut_limit_remaining, preferences = preferences)
        if not overwear:
            # We need to get a bottom from her personal wardrobe.
            overwear = person.wardrobe.get_random_appropriate_overwear(slut_limit_remaining, preferences = preferences)
            if not overwear:
                # Dive into the default wardrobe
                overwear = default_wardrobe.get_random_appropriate_overwear(slut_limit_remaining, preferences = preferences)
        return overwear

    def build_valid_uniform_wardrobe(self, person):
        valid_full_outfits = [] #We begin by building lists of all the uniform pieces that might be valid given our current uniform rules. This allows for the rules to update without requring any changes to the uniform wardrobe directly.
        valid_underwear_sets = []
        valid_overwear_sets = []

        slut_limit, underwear_limit, limited_to_top = mc.business.get_uniform_limits()

        if not limited_to_top:
            for full_outfit in self.outfits:
                if full_outfit.get_full_outfit_slut_score() <= slut_limit:
                    valid_full_outfits.append(full_outfit)

        if not limited_to_top:
            for an_underwear_set in self.underwear_sets:
                if an_underwear_set.get_underwear_slut_score() <= underwear_limit:
                    valid_underwear_sets.append(an_underwear_set)

        for an_overwear_set in self.overwear_sets:
            if an_overwear_set.get_overwear_slut_score() <= slut_limit:
                valid_overwear_sets.append(an_overwear_set)

        return Wardrobe("Valid Uniform Wardrobe", valid_full_outfits, valid_underwear_sets, valid_overwear_sets)

    Wardrobe.build_valid_uniform_wardrobe = build_valid_uniform_wardrobe

    # Girls choose the work uniform based on sluttiness and opinion modifiers instead of random
    # Creates a uniform out of the clothing items from this wardrobe.
    # When no company parts are available a girls personal wardrobe will be used for constructed uniforms.
    def decide_on_uniform_enhanced(self, person):
        conservative_score = person.get_opinion_score("conservative outfits") / 20.0 # high impact on sluttiness
        skimpy_uniform_score = person.get_opinion_score("skimpy uniforms") / 20.0
        work_uniforms_score = person.get_opinion_score("work uniforms") / 40.0 # low impact on sluttiness
        marketing_score = 0
        # girls working in marketing know they make more sales when wearing a sluttier outfit, so this affects their uniform choice
        if male_focused_marketing_policy.is_active() and mc.business.get_employee_title(person) == "Marketing":
            marketing_score = .05

        # modify target sluttiness based on opinions
        target_sluttiness = __builtin__.int(person.sluttiness * (1 + skimpy_uniform_score + work_uniforms_score + marketing_score - conservative_score))
        minimum_sluttiness = calculate_minimum_sluttiness(person, target_sluttiness)

        valid_wardrobe = self.build_valid_uniform_wardrobe(person)
        preferences = WardrobePreference(person)

        # renpy.say(None, person.name + " " + person.last_name + " [outfits: " + str(__builtin__.len(valid_wardrobe.outfits)) + " - overwear: " + str(__builtin__.len(valid_wardrobe.overwear_sets)) + " - underwear: " + str(__builtin__.len(valid_wardrobe.underwear_sets)))

        if __builtin__.len(valid_wardrobe.outfits) > 0:
            #We have some full body outfits we might use. 50/50 to use that or a constructed outfit.
            outfit_choice = renpy.random.randint(0,100)
            chance_to_use_full = 50 #Like normal outfits a uniform hasa 50/50 chance of being a full outfit or an assembled outfit if both are possible.

            #If we roll use full or we don't have the parts to make an assembled outfit.
            if outfit_choice > chance_to_use_full or __builtin__.len(valid_wardrobe.underwear_sets + valid_wardrobe.overwear_sets) == 0:
                full_outfit = None
                count = 0

                while not full_outfit and count < 2:    # Try to find a valid uniform by stretching the sluttiness range, returns none when not successful
                    full_outfit = valid_wardrobe.get_random_appropriate_outfit(target_sluttiness + (count * 5), minimum_sluttiness - (count * 10), preferences = preferences)
                    count += 1

                if not full_outfit: # fallback if we cannot find anything for our sluttiness or preferences
                    full_outfit = valid_wardrobe.pick_outfit_with_lowest_sluttiness()

                if full_outfit:
                    return full_outfit.get_copy()

        if __builtin__.len(valid_wardrobe.underwear_sets + valid_wardrobe.overwear_sets) == 0:
            #We have nothing else to make a uniform out of. Return None and let the pick uniform function handle that.
            full_outfit = get_random_appropriate_outfit_from_wardrobes(valid_wardrobe, person, target_sluttiness, None)
            if full_outfit:
                return full_outfit.get_copy()
            else:
                return default_outfit.get_copy()

        #If we get to here we are assembling an outfit out of underwear or overwear.
        uniform_over = None
        uniform_under = None
        count = 0

        while not uniform_over and count < 2:   # Try to find a valid uniform by stretching the sluttiness range, returns none when not successful
            uniform_over = valid_wardrobe.get_random_appropriate_overwear(target_sluttiness + (count * 5), minimum_sluttiness - (count * 10), preferences = preferences)
            count += 1

        if uniform_over:
            slut_limit_remaining = target_sluttiness - uniform_over.get_overwear_slut_score()
            if slut_limit_remaining < 10:
                slut_limit_remaining = 10 # don't expect 0 sluttiness underwear to be in wardrobe.

            uniform_under = valid_wardrobe.get_random_appropriate_underwear(slut_limit_remaining, preferences = preferences)

            if not uniform_under:
                uniform_under = valid_wardrobe.pick_underwear_with_lowest_sluttiness()

            if not uniform_under:
                # renpy.say(None, "Unable to find underwear in uniform wardrobe, pick any underwear from personal wardrobe.")
                uniform_under = get_random_appropriate_underwear_from_wardrobes(self, person, slut_limit_remaining, preferences)

        else:
            #There are no tops, so we're going to try and get a bottom and use one of the persons tops.
            uniform_under = valid_wardrobe.get_random_appropriate_underwear(target_sluttiness, preferences = preferences)

            if not uniform_under:
                uniform_under = valid_wardrobe.pick_underwear_with_lowest_sluttiness()

            if not uniform_under:
                # renpy.say(None, "Unable to find underwear in uniform wardrobe, pick any underwear from personal wardrobe.")
                uniform_under = get_random_appropriate_underwear_from_wardrobes(self, person, target_sluttiness, preferences)

            if uniform_under:
                slut_limit_remaining = target_sluttiness - uniform_under.get_underwear_slut_score()
                if slut_limit_remaining < 10:
                    slut_limit_remaining = 10 # don't expect 0 sluttiness overwear to be in personal wardrobe.

                uniform_over = valid_wardrobe.get_random_appropriate_overwear(slut_limit_remaining, preferences = preferences)

            if not uniform_over:
                uniform_over = valid_wardrobe.pick_overwear_with_lowest_sluttiness()

            if not uniform_over:
                # renpy.say(None, "Unable to find overwear in uniform wardrobe, pick any underwear from personal wardrobe.")
                uniform_over = get_random_appropriate_overwear_from_wardrobes(self, person, target_sluttiness, preferences)

        #At this point we have our under and over, if at all possible.
        if not uniform_over or not uniform_under:
            # renpy.say(None, "Failed to find any combined uniform, select generic outfit.")
            # Something's gone wrong and we don't have one of our sets. Last attempt on getting a full outfit from any wardrobe.
            full_outfit = get_random_appropriate_outfit_from_wardrobes(self, person, target_sluttiness, None)
            if full_outfit:
                return full_outfit.get_copy()
            else:
                return default_outfit.get_copy()

        return build_assembled_outfit(uniform_under, uniform_over)

    # replace default uniform decision function
    Wardrobe.decide_on_uniform = decide_on_uniform_enhanced

    # An outfit selector that takes personal preferences into account
    def decide_on_outfit_enhanced(self, person, sluttiness_modifier = 0.0):
        conservative_score = person.get_opinion_score("conservative outfits") / 20.0
        skimpy_outfit_score = person.get_opinion_score("skimpy outfits") / 20.0
        marketing_score = 0
        # girls working in marketing know they make more sales when wearing a sluttier outfit, so this affects their uniform choice
        if mc.business.is_work_day() and male_focused_marketing_policy.is_active() and person in mc.business.market_team:
            marketing_score = .05

        target_sluttiness = __builtin__.int(person.core_sluttiness * (1.0 + skimpy_outfit_score + marketing_score + sluttiness_modifier - conservative_score))
        minimum_sluttiness = calculate_minimum_sluttiness(person, target_sluttiness)
        preferences = WardrobePreference(person)

        if __builtin__.len(self.outfits) > 0:
            #We have some full body outfits we might use. 50/50 to use that or a constructed outfit.
            outfit_choice = renpy.random.randint(0,100)
            chance_to_use_full = (50 / 12.0) * __builtin__.len(self.outfits)   # when 12 outfits chance is 50%.
            if chance_to_use_full > 60: # cap at 60%
                chance_to_use_full = 60

            #If we roll use full or we don't have the parts to make an assembled outfit.
            if outfit_choice < chance_to_use_full or __builtin__.len(self.underwear_sets + self.overwear_sets) == 0:
                full_outfit = None
                count = 0
                while not full_outfit and count < 2:    # Try to find a valid outfit by stretching the sluttiness range, returns none when not successful
                    full_outfit = self.get_random_appropriate_outfit(target_sluttiness + (count * 5), minimum_sluttiness - (count * 10), preferences = preferences)
                    count += 1

                if not full_outfit: # fallback if we cannot find anything for our sluttiness or preferences
                    full_outfit = self.pick_outfit_with_lowest_sluttiness()

                if full_outfit:
                    return full_outfit.get_copy()

        if __builtin__.len(self.underwear_sets + self.overwear_sets) == 0:
            #We have nothing else to make a outfit out of. Use default builder function.
            full_outfit = get_random_appropriate_outfit_from_wardrobes(self, person, target_sluttiness, None)
            if full_outfit:
                return full_outfit.get_copy()
            else:
                return Outfit("Nude")

        #If we get to here we are assembling an outfit out of underwear or overwear.
        outfit_over = None
        count = 0
        while not outfit_over and count < 2:   # Try to find a valid uniform by stretching the sluttiness range, returns none when not successful
            outfit_over = self.get_random_appropriate_overwear(target_sluttiness + (count * 5), minimum_sluttiness - (count * 10), preferences = preferences)
            count += 1

        if outfit_over:
            slut_limit_remaining = target_sluttiness - outfit_over.get_overwear_slut_score()
            if slut_limit_remaining < 10:
                slut_limit_remaining = 10  # don't expect 0 sluttiness underwear to be in wardrobe.

            outfit_under = self.get_random_appropriate_underwear(slut_limit_remaining, preferences = preferences)

            if not outfit_under:
                outfit_under = self.pick_underwear_with_lowest_sluttiness()

            if not outfit_under:
                # renpy.say(None, "Unable to find underwear in wardrobe, pick any underwear from personal wardrobes.")
                outfit_under = get_random_appropriate_underwear_from_wardrobes(self, person, slut_limit_remaining, preferences)

        else:
            #There are no tops, so we're going to try and get a bottom and use one of the persons tops.
            outfit_under = self.get_random_appropriate_underwear(target_sluttiness, preferences = preferences)

            if not outfit_under:
                outfit_under = self.pick_underwear_with_lowest_sluttiness()

            if not outfit_under:
                # renpy.say(None, "Unable to find underwear in wardrobe, pick any underwear from personal wardrobes.")
                outfit_under = get_random_appropriate_underwear_from_wardrobes(self, person, target_sluttiness, preferences)

            if outfit_under:
                slut_limit_remaining = target_sluttiness - outfit_under.get_underwear_slut_score()
                if slut_limit_remaining < 10:
                    slut_limit_remaining = 10 # don't expect 0 sluttiness overwear to be in personal wardrobe.

                outfit_over = self.get_random_appropriate_overwear(slut_limit_remaining, preferences = preferences)

            if not outfit_over:
                outfit_over = self.pick_overwear_with_lowest_sluttiness()

            if not outfit_over:
                # renpy.say(None, "Unable to find overwear in uniform wardrobe, pick any underwear from personal wardrobes.")
                outfit_over = get_random_appropriate_overwear_from_wardrobes(self, person, target_sluttiness, preferences)

        #At this point we have our under and over, if at all possible.
        if not outfit_over or not outfit_under:
            # Something's gone wrong and we don't have one of our sets. Last attempt on getting a full outfit from any wardrobe.
            full_outfit = get_random_appropriate_outfit_from_wardrobes(self, person, target_sluttiness, None)
            if full_outfit:
                return full_outfit.get_copy()
            else:
                return Outfit("Nude")

        return build_assembled_outfit(outfit_under, outfit_over)

    Wardrobe.decide_on_outfit2 = decide_on_outfit_enhanced

init 2 python:
    # add some overwear with boots
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

    # add some outfit with makeup
    business_outfit_4 = Outfit("Business Outfit 4")
    business_outfit_4.add_upper(sweater.get_copy(),colour_white)
    business_outfit_4.add_upper(bralette.get_copy(),colour_white)
    business_outfit_4.add_accessory(gold_earings.get_copy(),colour_white)
    business_outfit_4.add_accessory(modern_glasses.get_copy(),colour_white)
    business_outfit_4.add_accessory(lipstick.get_copy(),colour_red)
    business_outfit_4.add_feet(slips.get_copy(),colour_black)
    business_outfit_4.add_lower(suitpants.get_copy(),colour_black)
    business_outfit_4.add_lower(panties.get_copy(),colour_white)
    default_wardrobe.add_outfit(business_outfit_4)

    business_outfit_5 = Outfit("Business Outfit 5")
    business_outfit_5.add_upper(sweater.get_copy(),colour_white)
    business_outfit_5.add_upper(bralette.get_copy(),colour_white)
    business_outfit_5.add_accessory(lipstick.get_copy(),colour_red)
    business_outfit_5.add_feet(heels.get_copy(),colour_black)
    business_outfit_5.add_lower(pencil_skirt.get_copy(),colour_black)
    business_outfit_5.add_lower(panties.get_copy(),colour_white)
    default_wardrobe.add_outfit(business_outfit_5)
