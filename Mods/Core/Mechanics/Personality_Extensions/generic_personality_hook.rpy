# Generic Personality Hook by Tristimdorion
# overrides the default make person function in the game
# so we can add / change person characteristics based on custom personalities.
# if you need person customizations, extend the hijacked labels

init 10 python: # add to stack later then other mods
    add_label_hijack("normal_start", "activate_generic_personality")
    add_label_hijack("after_load", "update_generic_personality")

init -1 python:
    # This will be called in game when a person is created original function in script.rpy
    def make_person(name = None, last_name = None, age = None, body_type = None, face_style = None, tits = None, height = None,
        hair_colour = None, hair_style = None, pubes_colour = None, pubes_style = None, skin = None, eyes = None, job = None,
        personality = None, custom_font = None, name_color = None, dial_color = None, starting_wardrobe = None, stat_array = None, skill_array = None, sex_array = None,
        start_sluttiness = None, start_obedience = None, start_happiness = None, start_love = None, start_home = None,
        title = None, possessive_title = None, mc_title = None, relationship = None, kids = None, SO_name = None, base_outfit = None, force_random = False):

        return_character = None
        if not force_random and renpy.random.randint(1,100) < 20:
            return_character = get_premade_character()

        if height is None:
            height = 0.825 + (renpy.random.random()/7)

        if return_character is None: #Either we aren't getting a pre-made, or we are out of them.
            # Use larger height range of person object (not full)
            return_character = create_random_person(name = name, last_name = last_name, age = age, body_type = body_type, face_style = face_style, tits = tits, height = height,
                hair_colour = hair_colour, hair_style = hair_style, pubes_colour = pubes_colour, pubes_style = pubes_style, skin = skin, eyes = eyes, job = job,
                personality = personality, custom_font = custom_font, name_color = name_color, dial_color = dial_color, starting_wardrobe = starting_wardrobe, stat_array = stat_array, skill_array = skill_array, sex_array = sex_array,
                start_sluttiness = start_sluttiness, start_obedience = start_obedience, start_happiness = start_happiness, start_love = start_love, start_home = start_home,
                title = title, possessive_title = possessive_title, mc_title = mc_title, relationship = relationship, kids = kids, SO_name = SO_name, base_outfit = base_outfit)

        update_person_opinions(return_character)
        update_random_person(return_character)
        rebuild_wardrobe(return_character)
        update_person_outfit(return_character, -0.2) # choose a less slutty outfit as planned outfit

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
        if not "unique_character_list" in globals() or not person in unique_character_list:
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
        if "cougar_personality" in globals() and "unique_character_list" in globals():
            # change personality to cougar if we meet age requirement
            if find_in_list(lambda x: x.effect == "cougar_personality_dummy_label", action_mod_list).enabled:
                if  person.age > 45 and person not in unique_character_list:
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
        if not person.wardrobe.name.startswith(person.name + "'s Wardrobe"):
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

        # add make-up to base outfit (based on pref)
        add_make_up_to_outfit(person, person.base_outfit)

        enhance_existing_wardrobe(person, 8)
        return

    def create_bimbo():
        # add one bimbo to the game (on start of game)
        the_person = make_person(age=renpy.random.randint(25, 35), tits="DD", body_type = "standard_body", face_style = "Face_4", skin = "tan",
            hair_colour = ["platinum blonde", [0.789, 0.746, 0.691,1]], hair_style = messy_hair, eyes = ["light blue", [0.60, 0.75, 0.98, 1.0]], personality = bimbo_personality)
        the_person.generate_home()
        the_person.home.add_person(the_person)
        return

    def create_hooker():
        the_person = make_person(start_sluttiness = renpy.random.randint(25, 40))
        the_person.sexy_opinions["bareback sex"] = [-2, False]
        the_person.set_mc_title("Sir")
        the_person.special_role.append(prostitute_role)
        the_person.generate_home()
        the_person.home.add_person(the_person)
        return

    def update_characters():
        # update characters in game
        for person in all_people_in_the_game(unique_character_list):
            update_random_person(person)

        # update default special characters opinions
        for person in unique_character_list:
            update_person_opinions(person)

        if "list_of_premade_characters" in globals():
            # update random characters in game
            for person in list_of_premade_characters:
                update_person_opinions(person)
                update_random_person(person)
                rebuild_wardrobe(person)
                update_person_outfit(person, -0.2) # choose a less slutty outfit as planned outfit
        return

    def update_unique_character_wardrobes():
        # Extend unique character wardrobes
        mom.wardrobe = mom.wardrobe.merge_wardrobes(wardrobe_from_xml("Mom_Extended_Wardrobe"))
        lily.wardrobe = lily.wardrobe.merge_wardrobes(wardrobe_from_xml("Lily_Extended_Wardrobe"))

        # remove strange outfits (they should not be in her wardrobe at all)
        mom.wardrobe.outfits.remove(find_in_list(lambda x: x.name == "Mom_Apron", mom.wardrobe.outfits))
        mom.wardrobe.outfits.remove(find_in_list(lambda x: x.name == "lingerie_1", mom.wardrobe.outfits))
        lily.wardrobe.outfits.remove(find_in_list(lambda x: x.name == "pink_lingerie", lily.wardrobe.outfits))
        stephanie.wardrobe.outfits.remove(find_in_list(lambda x: x.name == "Nude", stephanie.wardrobe.outfits))
        return

    unique_character_list = []  # global not stored variable (since not defined in label function)

    def create_unique_character_list():
        # use extend when adding a list to another list
        unique_character_list.extend([mom, lily, aunt, cousin, stephanie, alexia, nora])

        # mod unique characters (check for existence first)
        if "salon_manager" in globals():
            unique_character_list.append(salon_manager)

        if "starbuck" in globals():
            unique_character_list.append(starbuck)

        if "sarah" in globals():
            unique_character_list.append(sarah)

        if "dawn" in globals():
            unique_character_list.append(dawn)

        # disable for now, random outfits remove uniqueness of character in story line
        # make sure unique characters have at least six outfits / overwear sets to choose from
        #python:
        #    for person in unique_character_list:
        #        enhance_existing_wardrobe(person, 6)
        return

label activate_generic_personality(stack):
    python:
        create_unique_character_list()

        create_bimbo()

        # add two random hookers to the game (on start of game)
        for i in range(2):
            create_hooker()

        # add mc actions
        for action in main_character_actions_list:
            if action not in mc.main_character_actions:
                mc.main_character_actions.append(action)

        update_characters()

        update_unique_character_wardrobes()

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_generic_personality(stack):
    python:
        create_unique_character_list()

        # add mc actions
        for action in main_character_actions_list:
            if action not in mc.main_character_actions:
                mc.main_character_actions.append(action)

        # update characters in game (save game)
        for person in all_people_in_the_game(unique_character_list):
            update_random_person(person)

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return
