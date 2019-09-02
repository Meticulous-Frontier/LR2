# Generic Personality Hook by Tristimdorion
# overrides the default make person function in the game
# so we can add / change person characteristics based on custom personalities.
# if you need person customizations, extend the hijacked labels

init 5 python:
    add_label_hijack("normal_start", "activate_generic_personality")
    add_label_hijack("after_load", "update_generic_personality")

init -1 python:
    # This will be called in game when a person is created original function in script.rpy
    def make_person():
        return_character = None
        if renpy.random.randint(1,100) < 20:
            return_character = get_premade_character()

        if return_character is None: #Either we aren't getting a pre-made, or we are out of them.
            # Use larger height range of person object (not full)
            return_character = create_random_person(height = 0.825 + (renpy.random.random()/7))

        update_person_opinions(return_character)
        update_random_person(return_character)
        update_person_roles(return_character)
        rebuild_wardrobe(return_character)
        update_person_outfit(return_character)

        return return_character


    def update_person_opinions(person):
        # make sure we have an opinion about one of the clothing categories
        if not any(x[0] in person.opinions for x in ["dresses", "pants", "skirts"]):
            the_opinion_key = get_random_from_list(["dresses", "pants", "skirts"])
            degree = get_random_from_list([-2,-1,1,2])
            person.opinions[the_opinion_key] = [degree, False]

        # make sure we have an opinion about shoes and makeup
        if not any(x[0] in person.opinions for x in ["boots", "high heels", "makeup"]):
            the_opinion_key = get_random_from_list(["boots", "high heels", "makeup"])
            degree = get_random_from_list([-2,-1,1,2])
            person.opinions[the_opinion_key] = [degree, False]

        # make sure we have an opinion about basic sex acts
        if not any(x[0] in person.sexy_opinions for x in ["kissing", "masturbating", "giving blowjobs", "being fingered"]):
            the_opinion_key = get_random_from_list(["kissing", "masturbating", "giving blowjobs", "being fingered"])
            degree = get_random_from_list([-2,-1,1,2])
            person.sexy_opinions[the_opinion_key] = [degree, False]

        # make sure we have an opinion about clothing to wear
        if not any(x[0] in person.sexy_opinions for x in ["skimpy outfits", "not wearing underwear", "showing her tits", "showing her ass", "skimpy uniforms"]):
            the_opinion_key = get_random_from_list(["skimpy outfits", "not wearing underwear", "showing her tits", "showing her ass", "skimpy uniforms"])
            degree = get_random_from_list([-2,-1,1,2])
            person.sexy_opinions[the_opinion_key] = [degree, False]
        return

    # make sure new character has a more appropriate outfit to wear
    def update_person_outfit(person):
        if not person in unique_character_list:
            person.planned_outfit = person.wardrobe.decide_on_outfit2(person) # Use enhanced outfit selector
            person.outfit = person.planned_outfit.get_copy()
            person.planned_uniform = None
        return

    # change the random person based other characteristics of personality
    def update_random_person(person):
        # turn cougars on or off
        update_cougar_personality(person)
        # A person could have dialog even if we don't know her
        if person.possessive_title is None:
            person.set_possessive_title("The unknown woman")
        return

    # bind the generic people role actions to the people in the game
    def update_person_roles(person):
        # Adds mandatory roles to person
        if "generic_people_role" in globals():
            if find_in_list(lambda x: x == generic_people_role, person.special_role) is None:
                person.special_role.append(generic_people_role)

            # enable role actions based on configuration settings
            for role_action in find_in_list(lambda x: x == generic_people_role, person.special_role).actions:
                found = find_in_list(lambda x: x == role_action, action_mod_list)
                if found:
                    role_action.enabled = found.enabled
                    del found
        return

    def update_cougar_personality(person):
        if "cougar_personality" in globals():
            # change personality to cougar if we meet age requirement
            if find_in_list(lambda x: x.effect == "cougar_personality_dummy_label", action_mod_list).enabled:
                if person not in unique_character_list and person.age > 45:
                    if not person.personality == cougar_personality:
                        person.original_personality = person.personality
                        person.personality = cougar_personality
                        # mc.log_event((person.title or person.name) + "  A:" + str(person.age) + ": " + person.personality.personality_type_prefix, "float_text_grey")
            else:
                if person.personality == cougar_personality:
                    if person not in unique_character_list:
                        if not (person.original_personality is None or person.original_personality == cougar_personality):
                            person.personality = person.original_personality
                        else:
                            new_personality = get_random_from_list(list_of_personalities)
                            person.personality = new_personality
                        # mc.log_event((person.title or person.name) + " D:" + str(person.age) + ": " + person.personality.personality_type_prefix, "float_text_grey")
        return

    def rebuild_wardrobe(person):
        # skip personalized wardrobes
        if not person.wardrobe.name == "Master_Default_Wardrobe":
            return

        base_wardrobe = Wardrobe(default_wardrobe.name)
        preferences = WardrobePreference(person)

        for outfit in default_wardrobe.outfits:
            if not preferences.evaluate_outfit(outfit, 999):
                continue
            base_wardrobe.add_outfit(outfit.get_copy())

        for underwear in default_wardrobe.underwear_sets:
            if not preferences.evaluate_underwear(underwear, 999):
                continue
            base_wardrobe.add_underwear_set(underwear.get_copy())

        for overwear in default_wardrobe.overwear_sets:
            if not preferences.evaluate_outfit(overwear, 999):
                continue
            base_wardrobe.add_overwear_set(overwear.get_copy())

        outfit_builder = WardrobeBuilder(person)
        slut_scores = [1, 3, 5, 6, 10, 12]

        while len(base_wardrobe.outfits) > 7:
            base_wardrobe.remove_outfit(sorted(base_wardrobe.outfits, key = lambda x: x.slut_requirement)[renpy.random.randint(2,len(base_wardrobe.outfits)-1)])

        while len(base_wardrobe.outfits) < 6:    # add some generated outfits
            base_wardrobe.add_outfit(outfit_builder.build_outfit("FullSets", slut_scores[len(base_wardrobe.outfits)]))

        # add one generated outfit
        base_wardrobe.add_outfit(outfit_builder.build_outfit("FullSets", 12))

        while len(base_wardrobe.underwear_sets) > 7:
            base_wardrobe.remove_outfit(sorted(base_wardrobe.underwear_sets, key = lambda x: x.slut_requirement)[renpy.random.randint(2,len(base_wardrobe.underwear_sets)-1)])

        while len(base_wardrobe.underwear_sets) < 6:    # add some generated outfits
            base_wardrobe.add_underwear_set(outfit_builder.build_outfit("UnderwearSets", slut_scores[len(base_wardrobe.underwear_sets)]))

        # add one generated underwear
        base_wardrobe.add_underwear_set(outfit_builder.build_outfit("UnderwearSets", 12))

        while len(base_wardrobe.overwear_sets) > 7:
            base_wardrobe.remove_outfit(sorted(base_wardrobe.overwear_sets, key = lambda x: x.slut_requirement)[renpy.random.randint(2,len(base_wardrobe.overwear_sets)-1)])

        while len(base_wardrobe.overwear_sets) < 6:    # add some generated outfits
            base_wardrobe.add_overwear_set(outfit_builder.build_outfit("OverwearSets", slut_scores[len(base_wardrobe.overwear_sets)]))

        # add one generated overwear
        base_wardrobe.add_overwear_set(outfit_builder.build_outfit("OverwearSets", 12))

        person.wardrobe = base_wardrobe
        return

label activate_generic_personality(stack):
    call create_unique_character_list from _call_create_unique_character_list_activate

    python:
        # add one bimbo to the game (on start of game)
        the_person = create_random_person(age=renpy.random.randint(25, 35), tits="DD", body_type = "standard_body", face_style = "Face_4", skin = "tan",
            hair_colour = "platinum blonde", hair_style = messy_hair, eyes = "blue", personality = bimbo_personality)
        the_person.generate_home()
        the_person.home.add_person(the_person)

        # update characters in game
        for person in all_people_in_the_game():
            update_random_person(person)
            update_person_roles(person)

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_generic_personality(stack):
    call create_unique_character_list from _call_create_unique_character_list_update

    python:
        # fix for old save games (can be removed in future):
        if "cougar_personality" in globals():
            if not find_in_list(lambda x: x == cougar_personality, list_of_personalities) is None:
                list_of_personalities.remove(cougar_personality)

        # update characters in game (save game)
        for person in all_people_in_the_game():
            update_random_person(person)
            update_person_roles(person)

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label create_unique_character_list:
    # original unique game characters
    $ unique_character_list = [mom, lily, aunt, cousin, stephanie, alexia, nora]

    # mod unique characters (check for existance first)
    if "salon_manager" in globals():
        $ unique_character_list.append(salon_manager)

    if "starbuck" in globals():
        $ unique_character_list.append(starbuck)
    return
