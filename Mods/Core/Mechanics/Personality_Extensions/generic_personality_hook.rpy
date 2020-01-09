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
        rebuild_wardrobe(return_character)
        update_person_outfit(return_character, -0.5) # choose a less slutty outfit as planned outfit

        return return_character


    def update_person_opinions(person):
        # make sure we have an opinion about one of the clothing categories
        ensure_opinion_on_subject(person, ["dresses", "pants", "skirts"])

        # make sure we have an opinion about shoes and makeup
        ensure_opinion_on_subject(person, ["boots", "high heels", "makeup"])

        # make sure we have an opinion about clothing to wear
        ensure_sexy_opinion_on_subject(person, ["skimpy outfits", "not wearing underwear", "showing her tits", "showing her ass", "skimpy uniforms"])

        # do we have sexual preferences / dislikes?
        ensure_opinion_on_sexual_preference(person, "Foreplay", ["kissing", "being fingered", "giving handjobs"])
        ensure_opinion_on_sexual_preference(person, "Oral", ["giving blowjobs", "getting head", "drinking cum" ])
        ensure_opinion_on_sexual_preference(person, "Vaginal", ["missionary style sex", "vaginal sex", "creampies"])
        ensure_opinion_on_sexual_preference(person, "Anal", ["anal sex", "anal creampies", "doggy style sex"])

        return

    def ensure_opinion_on_subject(person, opinions):
        if not any(x[0] in person.opinions for x in opinions):
            the_opinion_key = get_random_from_list(opinions)
            degree = get_random_from_list([-2,-1,1,2])
            person.opinions[the_opinion_key] = [degree, False]

    def ensure_sexy_opinion_on_subject(person, opinions):
        if not any(x[0] in person.opinions for x in opinions):
            the_opinion_key = get_random_from_list(opinions)
            degree = get_random_from_list([-2,-1,1,2])
            person.sexy_opinions[the_opinion_key] = [degree, False]

    def ensure_opinion_on_sexual_preference(person, sex_skill, opinions):
        if not any(x[0] in person.sexy_opinions for x in opinions):
            the_opinion_key = get_random_from_list(opinions)
            if person.sex_skills[sex_skill] >= 3: # positive skew
                degree = get_random_from_list([1,2])
            elif person.sex_skills[sex_skill] < 1: # negative skew
                degree = get_random_from_list([-2, -1])
            else: # random
                degree = get_random_from_list([-2,-1,1,2])
            person.sexy_opinions[the_opinion_key] = [degree, False]

    # make sure new character has a more appropriate outfit to wear
    def update_person_outfit(person, sluttiness_modifier = 0.0):
        if not person in unique_character_list:
            person.planned_outfit = person.wardrobe.decide_on_outfit2(person, sluttiness_modifier) # Use enhanced outfit selector
            person.apply_outfit(person.planned_outfit)
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

        base_wardrobe = Wardrobe("[person.name]_[person.last_name]_wardrobe")
        preferences = WardrobePreference(person)

        for outfit in default_wardrobe.outfits:
            if not preferences.evaluate_outfit(outfit, 999):
                continue
            base_wardrobe.add_outfit(outfit.get_copy())
            if len(base_wardrobe.outfits) > 8:  # quick exit when we have enough
                break

        for underwear in default_wardrobe.underwear_sets:
            if not preferences.evaluate_underwear(underwear, 999):
                continue
            base_wardrobe.add_underwear_set(underwear.get_copy())
            if len(base_wardrobe.underwear_sets) > 8:   # quick exit when we have enough
                break

        for overwear in default_wardrobe.overwear_sets:
            if not preferences.evaluate_outfit(overwear, 999):
                continue
            base_wardrobe.add_overwear_set(overwear.get_copy())
            if len(base_wardrobe.overwear_sets) > 8:    # quick exit when we have enough
                break

        # ensure we have at least 3 auto generated outfits by removing surplus, but keep the 2 most decent outfits from default wardrobe
        while len(base_wardrobe.outfits) > 5:
            base_wardrobe.remove_outfit(sorted(base_wardrobe.outfits, key = lambda x: x.slut_requirement)[renpy.random.randint(2,len(base_wardrobe.outfits)-1)])

        while len(base_wardrobe.underwear_sets) > 5:
            base_wardrobe.remove_outfit(sorted(base_wardrobe.underwear_sets, key = lambda x: x.slut_requirement)[renpy.random.randint(2,len(base_wardrobe.underwear_sets)-1)])

        while len(base_wardrobe.overwear_sets) > 5:
            base_wardrobe.remove_outfit(sorted(base_wardrobe.overwear_sets, key = lambda x: x.slut_requirement)[renpy.random.randint(2,len(base_wardrobe.overwear_sets)-1)])

        person.wardrobe = base_wardrobe

        enhance_existing_wardrobe(person, 8)
        return

label activate_generic_personality(stack):
    call create_unique_character_list from _call_create_unique_character_list_activate

    python:
        # add one bimbo to the game (on start of game)
        the_person = create_random_person(age=renpy.random.randint(25, 35), tits="DD", body_type = "standard_body", face_style = "Face_4", skin = "tan",
            hair_colour = ["platinum blonde", [0.789, 0.746, 0.691,1]], hair_style = messy_hair, eyes = ["light blue", [0.60, 0.75, 0.98, 1.0]], personality = bimbo_personality)
        the_person.generate_home()
        the_person.home.add_person(the_person)

        # add mc actions
        for action in main_character_actions_list:
            if action not in mc.main_character_actions:
                mc.main_character_actions.append(action)

        # update characters in game
        for person in all_people_in_the_game():
            update_random_person(person)

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

        # add mc actions
        for action in main_character_actions_list:
            if action not in mc.main_character_actions:
                mc.main_character_actions.append(action)

        # update characters in game (save game)
        for person in all_people_in_the_game():
            update_random_person(person)

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label create_unique_character_list:
    # original unique game characters
    $ unique_character_list = [mom, lily, aunt, cousin, stephanie, alexia, nora]

    # mod unique characters (check for existence first)
    if "salon_manager" in globals():
        $ unique_character_list.append(salon_manager)

    if "starbuck" in globals():
        $ unique_character_list.append(starbuck)

    if "sarah" in globals():
        $ unique_character_list.append(sarah)

    # disable for now, random outfits remove uniqueness of character in story line
    # make sure unique characters have at least six outfits / overwear sets to choose from
    #python:
    #    for person in unique_character_list:
    #        enhance_existing_wardrobe(person, 6)

    return
