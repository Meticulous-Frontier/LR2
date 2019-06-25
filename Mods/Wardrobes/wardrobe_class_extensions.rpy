init -1 python:
    
    # Get an overwear outfit that is considered appropriate based on sluttines and preferences.
    def get_random_appropriate_overwear(self, sluttiness_limit, sluttiness_min = 0, exclude_skirts = False, exclude_pants = False):
        valid_overwear = []
        for overwear in self.overwear_sets:
            if overwear.get_overwear_slut_score() <= sluttiness_limit and overwear.get_overwear_slut_score() >= sluttiness_min:
                if exclude_skirts:
                    if not [clothing for clothing in overwear.lower_body if clothing in skirts_list]:
                        valid_overwear.append(overwear)
                elif exclude_pants:
                    if not [clothing for clothing in overwear.lower_body if clothing in pants_list]:
                        valid_overwear.append(overwear)
                else:
                    valid_overwear.append(overwear)

        the_outfit = get_random_from_list(valid_overwear)
        if the_outfit:
            return the_outfit.get_copy()
        else:
            return None

    Wardrobe.get_random_appropriate_overwear = get_random_appropriate_overwear

    # Get a copy of a full outfit that is considered appropriate based on sluttiness and preferences.
    def get_random_appropriate_outfit_enhanced(self, sluttiness_limit, sluttiness_min = 0, exclude_skirts = False, exclude_pants = False): 
        valid_outfits = []
        for outfit in self.outfits:
            if outfit.slut_requirement >= sluttiness_min and outfit.slut_requirement <= sluttiness_limit:
                if exclude_skirts:
                    if not [clothing for clothing in outfit.lower_body if clothing in skirts_list]:
                        valid_outfits.append(outfit)
                elif exclude_pants:
                    if not [clothing for clothing in outfit.lower_body if clothing in pants_list]:
                        valid_outfits.append(outfit)
                else:
                    valid_outfits.append(outfit)

        the_outfit = get_random_from_list(valid_outfits)
        if the_outfit:
            return the_outfit.get_copy()
        else:
            return None

    Wardrobe.get_random_appropriate_outfit = get_random_appropriate_outfit_enhanced


    # Girls choose the work uniform based on sluttiness and opinion modifiers instead of random
    # Creates a uniform out of the clothing items from this wardrobe. 
    # When no company parts are available a girls personal wardrobe will be used for constructed uniforms.
    def decide_on_uniform_enhanced(self, person): 
        conservative_score = person.get_opinion_score("conservative outfits") / 10 # high impact on sluttiness
        skimpy_uniform_score = person.get_opinion_score("skimpy uniforms") / 10
        work_uniforms_score = person.get_opinion_score("work uniforms") / 20 # low impact on sluttiness
        marketing_score = 0
        # girls working in marketing know they make more sales when wearing a sluttier outfit, so this affects their uniform choice
        if male_focused_marketing_policy.is_owned() and mc.business.get_employee_title(person) == "Marketing":
            marketing_score = .2

        skirts_score = person.get_opinion_score("skirts")
        pants_score = person.get_opinion_score("pants")
        exclude_skirts = skirts_score < 0 or pants_score > 0
        exclude_pants = pants_score < 0 or skirts_score > 0

        # break tigh when they don't like both.
        if exclude_skirts and exclude_pants:
            if pants_score < skirts_score or skirts_score == pants_score:  # favor skirts
                exclude_skirts = False
            else:
                exclude_pants = False

        # modify target sluttiness based on opinions
        target_sluttiness = person.sluttiness * (1 + skimpy_uniform_score + work_uniforms_score + marketing_score - conservative_score)
        minimum_sluttiness = target_sluttiness - person.sluttiness # raise minimum sluttiness by the amount over normal sluttiness
        if target_sluttiness > 40 and minimum_sluttiness == 0: # when there is no minimum sluttiness, increase it when the girl is slutty
            minimum_sluttiness = (target_sluttiness - 40) // 2
        if minimum_sluttiness > 40: # prevent minimum sluttiness from going too high (late game, high sluttiness)
            minimum_sluttiness = 40
        if target_sluttiness > 100 and minimum_sluttiness < 30: # when very slutty, don't bother with non-sexy clothes.
            minimum_sluttiness = 30

        if len(self.outfits) > 0:
            #We have some full body outfits we mgiht use. 50/50 to use that or a constructed outfit.
            outfit_choice = renpy.random.randint(0,100)
            chance_to_use_full = 50 #Like normal outfits a uniform hasa 50/50 chance of being a full outfit or an assembled outfit if both are possible.

            #If we roll use full or we don't have the parts to make an assembled outfit.
            if outfit_choice > chance_to_use_full or len(self.underwear_sets + self.overwear_sets) == 0:
                full_outfit = None
                count = 0
                while not full_outfit and count < 4:    # Try to find a valid uniform by stretching the sluttiness range, returns none when not succesfull               
                    full_outfit = self.get_random_appropriate_outfit(target_sluttiness + (count * 5), minimum_sluttiness - (count * 10), exclude_skirts, exclude_pants)
                    count += 1

                if not full_outfit: # fallback if we cannot find anything for our sluttiness or preferences
                    full_outfit = self.pick_random_outfit()

                return full_outfit
                
        elif len(self.underwear_sets + self.overwear_sets) == 0:
            #We have nothing else to make a uniform out of. Return None and let the pick uniform function handle that.
            return None

        #If we get to here we are assembling an outfit out of underwear or overwear.
        uniform_over = None
        count = 0
        while not uniform_over and count < 4:   # Try to find a valid uniform by stretching the sluttiness range, returns none when not succesfull
            uniform_over = self.get_random_appropriate_overwear(target_sluttiness + (count * 5), minimum_sluttiness - (count * 10), exclude_skirts, exclude_pants)
            count += 1

        if uniform_over:
            slut_limit_remaining = target_sluttiness - uniform_over.get_overwear_slut_score()
            if slut_limit_remaining < 0:
                slut_limit_remaining = 0

            #We got a top, now get a bottom.
            uniform_under = self.get_random_appropriate_underwear(slut_limit_remaining)
            if not uniform_under:
                #We need to get a bottom from her personal wardrobe. We also want to make sure it's something she would personally wear.
                uniform_under = person.wardrobe.get_random_appropriate_underwear(slut_limit_remaining)

        else:
            #There are no tops, so we're going to try and get a bottom and use one of the persons tops.
            uniform_under = self.get_random_appropriate_underwear(target_sluttiness, minimum_sluttiness)
            if not uniform_under:
                # no underwear that fits sluttiness, get one from her personal wardrobe
                uniform_under = person.wardrobe.get_random_appropriate_underwear(target_sluttiness)

            if uniform_under:
                slut_limit_remaining = target_sluttiness - uniform_under.get_underwear_slut_score()
                if slut_limit_remaining < 0:
                    slut_limit_remaining = 0 #If the outfit is so slutty we're not comfortable in it we'll try and wear the most conservative overwear we can.

                uniform_over = person.wardrobe.get_random_appropriate_overwear(slut_limit_remaining, exclude_skirts = exclude_skirts, exclude_pants = exclude_pants)

        #At this point we have our under and over, if at all possible.
        if not uniform_over or not uniform_under:
            return None #Something's gone wrong and we don't have one of our sets. return None and let the uniform gods sort it out.

        assembled_uniform = uniform_under.get_copy()
        assembled_uniform.name = uniform_under.name + " + " + uniform_over.name

        # renpy.say("", "Assembled outfit: " + assembled_uniform.name)

        for upper in uniform_over.upper_body:
            assembled_uniform.upper_body.append(upper.get_copy())

        for lower in uniform_over.lower_body:
            assembled_uniform.lower_body.append(lower.get_copy())

        for feet_wear in uniform_over.feet:
            assembled_uniform.feet.append(feet_wear.get_copy())

        for acc in uniform_over.accessories:
            assembled_uniform.accessories.append(acc.get_copy())

        assembled_uniform.update_slut_requirement()
        return assembled_uniform

    # replace default uniform descission function
    Wardrobe.decide_on_uniform = decide_on_uniform_enhanced