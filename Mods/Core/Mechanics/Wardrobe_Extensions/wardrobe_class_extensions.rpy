init -1 python:
    def get_all_outfits(self):
        return self.outfits + self.underwear_sets + self.overwear_sets

    Wardrobe.all_outfits = property(get_all_outfits, None, None, "Returns all outfits in wardrobe")

    # Get an overwear outfit that is considered appropriate based on sluttiness and preferences.
    def get_random_appropriate_overwear_enhanced(self, sluttiness_limit, sluttiness_min = 0, guarantee_output = False, preferences = None, depth = 0):
        if preferences is None:
            preferences = WardrobePreference()

        if sluttiness_min < 0:
            sluttiness_min = 0

        valid_overwear = [x for x in self.overwear_sets if preferences.evaluate_outfit(x, sluttiness_limit, sluttiness_min)]
        if not valid_overwear:  # when we find no valid items, only validate sluttiness score
            valid_overwear = [x for x in self.overwear_sets if x.get_overwear_slut_score() <= sluttiness_limit and x.get_overwear_slut_score() >= sluttiness_min]

        if valid_overwear:
            return renpy.random.choice(valid_overwear).get_copy()
        elif guarantee_output:
            if depth < 2:
                return self.get_random_appropriate_overwear(sluttiness_limit+5, sluttiness_min-5, guarantee_output, preferences, depth + 1)

            return self.pick_overwear_with_lowest_sluttiness() or Outfit("Nothing")
        return None

    Wardrobe.get_random_appropriate_overwear = get_random_appropriate_overwear_enhanced

    # Get a copy of a full outfit that is considered appropriate based on sluttiness and preferences.
    def get_random_appropriate_outfit_enhanced(self, sluttiness_limit, sluttiness_min = 0, guarantee_output = False, preferences = None, depth = 0):
        if preferences is None:
            preferences = WardrobePreference()

        if sluttiness_min < 0:
            sluttiness_min = 0

        valid_outfits = [x for x in self.outfits if preferences.evaluate_outfit(x, sluttiness_limit, sluttiness_min)]

        if not valid_outfits: # when we find no valid items, only validate sluttiness score
            valid_outfits = [x for x in self.outfits if x.get_full_outfit_slut_score() <= sluttiness_limit and x.get_full_outfit_slut_score() >= sluttiness_min]

        if valid_outfits:
            return renpy.random.choice(valid_outfits).get_copy()
        elif guarantee_output:
            if depth < 2:
                return self.get_random_appropriate_outfit(sluttiness_limit+5, sluttiness_min-5, guarantee_output, preferences, depth + 1)

            return self.pick_outfit_with_lowest_sluttiness() or Outfit("Nothing")
        return None

    Wardrobe.get_random_appropriate_outfit = get_random_appropriate_outfit_enhanced

    def get_random_appropriate_underwear_enhanced(self, sluttiness_limit, sluttiness_min = 0, guarantee_output = False, preferences = None, depth = 0): #Get an underwear outfit that is considered appropriate (based on underwear sluttiness, not full outfit sluttiness)
        if preferences is None:
            preferences = WardrobePreference()

        if sluttiness_min < 0:
            sluttiness_min = 0

        valid_underwear = [x for x in self.underwear_sets if preferences.evaluate_underwear(x, sluttiness_limit, sluttiness_min)]

        if not valid_underwear: # when we find no valid items, only validate sluttiness score
            valid_underwear = [x for x in self.underwear_sets if x.get_underwear_slut_score() <= sluttiness_limit and x.get_underwear_slut_score() >= sluttiness_min]

        if valid_underwear:
            return renpy.random.choice(valid_underwear).get_copy()
        elif guarantee_output: # If an output is guaranteed we always return an Outfit object (even if it is empty). Otherwise we return None to indicate failure to find something.
            if depth < 2: #Sets an effective recursion limit.
                return self.get_random_appropriate_underwear(sluttiness_limit+5, sluttiness_min-5, guarantee_output, preferences, depth + 1)

            return self.pick_underwear_with_lowest_sluttiness() or Outfit("Nothing")
        return None

    Wardrobe.get_random_appropriate_underwear = get_random_appropriate_underwear_enhanced

    def pick_outfit_with_lowest_sluttiness(self):
        if not self.outfits:
            return None
        return min(self.outfits, key=lambda x: x.get_full_outfit_slut_score()).get_copy()

    Wardrobe.pick_outfit_with_lowest_sluttiness = pick_outfit_with_lowest_sluttiness

    def pick_overwear_with_lowest_sluttiness(self):
        if not self.overwear_sets:
            return None
        return min(self.overwear_sets, key=lambda x: x.get_overwear_slut_score()).get_copy()

    Wardrobe.pick_overwear_with_lowest_sluttiness = pick_overwear_with_lowest_sluttiness

    def pick_underwear_with_lowest_sluttiness(self):
        if not self.underwear_sets:
            return None
        return min(self.underwear_sets, key=lambda x: x.get_underwear_slut_score()).get_copy()

    Wardrobe.pick_underwear_with_lowest_sluttiness = pick_underwear_with_lowest_sluttiness

    def wardrobe_remove_outfit(self, outfit):
        for outfit_set in [self.outfits, self.underwear_sets, self.overwear_sets]:
            if isinstance(outfit, basestring):
                found = next((x for x in outfit_set if x.name == outfit), None)
                if found:
                    outfit_set.remove(found)
            elif outfit in outfit_set:
                outfit_set.remove(outfit)

    Wardrobe.remove_outfit = wardrobe_remove_outfit

    def wardrobe_has_outfit_with_name(self, the_name):
        return any(x for x in self.all_outfits if x.name == the_name)

    Wardrobe.has_outfit_with_name = wardrobe_has_outfit_with_name

    def wardrobe_get_outfit_with_name(self, the_name):
        found = next((x for x in self.all_outfits if x.name == the_name), None)
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
        assembled_outfit = outfit_over.get_copy()

        for upper in outfit_under.upper_body:
            assembled_outfit.add_upper(upper.get_copy())

        for lower in outfit_under.lower_body:
            assembled_outfit.add_lower(lower.get_copy())

        for feet_wear in outfit_under.feet:
            assembled_outfit.add_feet(feet_wear.get_copy())

        for acc in outfit_under.accessories:
            assembled_outfit.add_accessory(acc.get_copy())

        assembled_outfit.build_outfit_name()

        return assembled_outfit

    def generate_random_appropriate_outfit(person, outfit_type = "FullSets", sluttiness = None):
        wardrobe_builder = WardrobeBuilder(person)
        if sluttiness is None:
            sluttiness = person.sluttiness
        base_sluttiness = __builtin__.max(sluttiness - 15, 0) # first 15 points of sluttiness don't impact outfit builder
        min_sluttiness = __builtin__.min(base_sluttiness / 18, 5) if sluttiness > 50 else 0 # prevent override of person preferences until she's slutty enough not to care
        return wardrobe_builder.build_outfit(outfit_type, __builtin__.min(base_sluttiness / 7, 12), min_sluttiness)

    # Combines business wardrobe with employee's personal wardrobe
    def build_uniform_wardrobe(self, personal_wardrobe, slut_limit = 999, underwear_limit = 999, limited_to_top = False):
        def _filter_full_outfits(full_outfits, slut_limit = 999):
            return [x for x in full_outfits if x.get_full_outfit_slut_score() <= slut_limit]

        def _filter_underwear_sets(underwear_sets, underwear_limit = 999):
            return [x for x in underwear_sets if x.get_underwear_slut_score() <= underwear_limit]

        def _filter_overwear_sets(overwear_sets, slut_limit = 999):
            return [x for x in overwear_sets if x.get_overwear_slut_score() <= slut_limit]

        full_outfits = []
        underwear_sets = []
        overwear_sets = []

        if self.overwear_sets:
            overwear_sets = _filter_overwear_sets(self.overwear_sets, slut_limit)
        if not self.overwear_sets:
            overwear_sets = _filter_overwear_sets(personal_wardrobe.overwear_sets, slut_limit)

        if limited_to_top:
            return Wardrobe("Valid Uniform Wardrobe", full_outfits, underwear_sets, overwear_sets)

        if self.outfits:
            full_outfits = _filter_full_outfits(self.outfits, slut_limit)
        if not full_outfits:
            full_outfits = _filter_full_outfits(personal_wardrobe.outfits, slut_limit)

        if self.underwear_sets:
            underwear_sets = _filter_underwear_sets(self.underwear_sets, underwear_limit)
        if not self.underwear_sets:
            underwear_sets = _filter_underwear_sets(personal_wardrobe.underwear_sets, underwear_limit)

        return Wardrobe("Valid Uniform Wardrobe", full_outfits, underwear_sets, overwear_sets)

    Wardrobe.build_uniform_wardrobe = build_uniform_wardrobe

    # Girls choose the work uniform based on sluttiness and opinion modifiers instead of random
    # Creates a uniform out of the clothing items from this wardrobe.
    # When no company parts are available a girls personal wardrobe will be used for constructed uniforms.
    def decide_on_uniform_enhanced(self, person):
        slut_limit = 999
        valid_wardrobe = None
        if (person.is_employee() or person.is_intern()) and dress_code_policy.is_active():
            slut_limit, underwear_limit, limited_to_top = mc.business.get_uniform_limits()
            valid_wardrobe = self.build_uniform_wardrobe(person.wardrobe, slut_limit, underwear_limit, limited_to_top)
        else:
            valid_wardrobe = self.build_uniform_wardrobe(person.wardrobe)

        sluttiness_modifier = person.get_opinion_score("work uniforms") / 40.0 # low impact on sluttiness

        uniform = valid_wardrobe.decide_on_outfit2(person, sluttiness_modifier = sluttiness_modifier, slut_limit = slut_limit)

        if uniform and (person.is_employee() or person.is_intern()):  # only apply policies for employees
            if creative_colored_uniform_policy.is_active():
                uniform = WardrobeBuilder(person).personalize_outfit(uniform,
                    swap_bottoms = personal_bottoms_uniform_policy.is_active(),
                    allow_skimpy = creative_skimpy_uniform_policy.is_active())
            elif personal_bottoms_uniform_policy.is_active():
                (uniform, _swapped) = WardrobeBuilder(person).apply_bottom_preference(person, uniform)
            elif easier_access_policy.is_active(): # only when creative and relaxed are not active
                uniform.make_easier_access()

            if commando_uniform_policy.is_active(): # always applied, overrides uniform
                uniform.remove_bra_and_panties()

        if uniform and person.job == doctor_job:
            uniform.add_upper(lab_coat.get_copy(), colour_white)

        uniform.build_outfit_name()

        print("Picked uniform: {} ({})".format(uniform.name, uniform.get_full_outfit_slut_score()))

        return uniform

    # replace default uniform decision function
    Wardrobe.decide_on_uniform = decide_on_uniform_enhanced

    # An outfit selector that takes personal preferences into account
    def decide_on_outfit_enhanced(self, person, sluttiness_modifier = 0.0, slut_limit = 999):
        conservative_score = person.get_opinion_score("conservative outfits") / 20.0
        skimpy_outfit_score = person.get_opinion_score("skimpy outfits") / 20.0
        marketing_score = 0
        # girls working in marketing know they make more sales when wearing a sluttier outfit, so this affects their uniform choice
        if mc.business.is_work_day() and male_focused_marketing_policy.is_active() and person in mc.business.market_team:
            marketing_score = .05

        target_sluttiness = __builtin__.int(person.sluttiness * (1.0 + skimpy_outfit_score + marketing_score + sluttiness_modifier - conservative_score))
        target_sluttiness = __builtin__.min(target_sluttiness, slut_limit)

        minimum_sluttiness = calculate_minimum_sluttiness(person, target_sluttiness)

        if not self.outfits and not self.underwear_sets and not self.overwear_sets:
            #We have nothing to make a outfit out of. Use default builder function.
            return generate_random_appropriate_outfit(person, sluttiness = target_sluttiness)

        preferences = WardrobePreference(person)

        if self.outfits:
            #We have some full body outfits we might use. 50/50 to use that or a constructed outfit.
            outfit_choice = renpy.random.randint(0,100)
            chance_to_use_full = (50 / 12.0) * __builtin__.len(self.outfits)   # when 12 outfits chance is 50%.
            if chance_to_use_full > 60: # cap at 60%
                chance_to_use_full = 60

            #If we roll use full or we don't have the parts to make an assembled outfit.
            if outfit_choice < chance_to_use_full or not (self.underwear_sets or self.overwear_sets):

                full_outfit = self.get_random_appropriate_outfit(target_sluttiness, minimum_sluttiness, preferences = preferences)

                if not full_outfit: # fallback if we cannot find anything for our sluttiness or preferences
                    full_outfit = self.pick_outfit_with_lowest_sluttiness()

                if full_outfit:
                    return full_outfit.get_copy()

        #If we get to here we are assembling an outfit out of underwear or overwear.
        outfit_over = self.get_random_appropriate_overwear(target_sluttiness, minimum_sluttiness, preferences = preferences)
        outfit_under = None

        if outfit_over:
            slut_limit_remaining = target_sluttiness - outfit_over.get_overwear_slut_score()
            if slut_limit_remaining < 10:
                slut_limit_remaining = 10  # don't expect 0 sluttiness underwear to be in wardrobe.

            outfit_under = self.get_random_appropriate_underwear(slut_limit_remaining, preferences = preferences)

            if not outfit_under:
                outfit_under = self.pick_underwear_with_lowest_sluttiness()

            if not outfit_under:
                # renpy.say(None, "Unable to find underwear in wardrobe, pick any underwear from personal wardrobes.")
                outfit_under = generate_random_appropriate_outfit(person, outfit_type = "UnderwearSets", sluttiness = slut_limit_remaining)

        else:
            #There are no tops, so we're going to try and get a bottom and use one of the persons tops.
            outfit_under = self.get_random_appropriate_underwear(target_sluttiness, preferences = preferences)

            if not outfit_under:
                outfit_under = self.pick_underwear_with_lowest_sluttiness()

            if not outfit_under:
                # renpy.say(None, "Unable to find underwear in wardrobe, pick any underwear from personal wardrobes.")
                outfit_under = generate_random_appropriate_outfit(person, outfit_type = "UnderwearSets", sluttiness = target_sluttiness)

            if outfit_under:
                slut_limit_remaining = target_sluttiness - outfit_under.get_underwear_slut_score()
                if slut_limit_remaining < 10:
                    slut_limit_remaining = 10 # don't expect 0 sluttiness overwear to be in personal wardrobe.

                outfit_over = self.get_random_appropriate_overwear(slut_limit_remaining, preferences = preferences)

                if not outfit_over:
                    outfit_over = self.pick_overwear_with_lowest_sluttiness()

                if not outfit_over:
                    # renpy.say(None, "Unable to find overwear in uniform wardrobe, pick any underwear from personal wardrobes.")
                    outfit_over = generate_random_appropriate_outfit(person, outfit_type = "OverwearSets", sluttiness = slut_limit_remaining)

        #At this point we have our under and over, if at all possible.
        if not outfit_over or not outfit_under:
            # Something's gone wrong and we don't have one of our sets. Last attempt on getting a full outfit from any wardrobe.
            return generate_random_appropriate_outfit(person, sluttiness = target_sluttiness)

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
