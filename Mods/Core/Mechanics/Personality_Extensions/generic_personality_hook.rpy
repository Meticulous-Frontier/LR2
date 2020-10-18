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
        title = None, possessive_title = None, mc_title = None, relationship = None, kids = None, SO_name = None, base_outfit = None,
        force_random = False, forced_opinions = None, forced_sexy_opinions = None):

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

        # when not using bugfix, remove the employed_since key from event trigger dictionary (this should only be used for employees)
        if return_character.event_triggers_dict.get("employed_since", -1) != -1:
            del return_character.event_triggers_dict["employed_since"]

        update_person_opinions(return_character)
        update_random_person(return_character)

        # apply forced opinions after we 'update opinions', so we don't override them there
        if forced_opinions and isinstance(forced_opinions, list):
            for opinion in forced_opinions:
                return_character.opinions[opinion[0]] = [opinion[1], opinion[2]]

        if forced_sexy_opinions and isinstance(forced_sexy_opinions, list):
            for opinion in forced_sexy_opinions:
                return_character.sexy_opinions[opinion[0]] = [opinion[1], opinion[2]]

        if not starting_wardrobe:
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

        # fix opinion contradictions (one cannot exclude other)
        fix_opinion_contradiction(person, "drinking cum", "giving blowjobs")
        fix_opinion_contradiction(person, "creampies", "bareback sex")
        fix_opinion_contradiction(person, "anal creampies", "bareback sex")
        fix_opinion_contradiction(person, "skimpy outfits", "showing her tits")
        fix_opinion_contradiction(person, "skimpy outfits", "showing her ass")
        fix_opinion_contradiction(person, "skimpy outfits", "high heels")
        fix_opinion_contradiction(person, "masturbating", "being fingered")

        # fix opinion exclusion (one excludes other)
        fix_opinion_exclusion(person, "lingerie", "not wearing underwear")
        fix_opinion_exclusion(person, "skimpy outfits", "not wearing anything")
        fix_opinion_exclusion(person, "being submissive", "taking control")
        fix_opinion_exclusion(person, "the colour red", "the colour pink") # red and pink clash
        fix_opinion_exclusion(person, "the colour red", "the colour purple") # red and purple clash
        fix_opinion_exclusion(person, "the colour pink", "the colour purple") # pink and purple clash
        fix_opinion_exclusion(person, "the colour blue", "the colour purple") # pink and purple clash
        fix_opinion_exclusion(person, "the colour orange", "the colour yellow") # orange and yellow clash

        # set work opinions (based on stats / skills)
        set_work_opinion(person, "research work", person.int, person.research_skill)
        set_work_opinion(person, "marketing work", person.charisma, person.market_skill)
        set_work_opinion(person, "HR work", person.charisma, person.hr_skill)
        set_work_opinion(person, "supply work", person.focus, person.supply_skill)
        set_work_opinion(person, "production work", person.focus, person.production_skill)
        return

    def set_work_opinion(person, skill, stat_level, skill_level):
        known = True # renpy.random.randint(0, 2) == 1
        if skill_level < 2 and stat_level < 3:
            person.opinions[skill] = [-2, known]
        elif skill_level < 3 and stat_level < 4:
            person.opinions[skill] = [-1, known]
        elif skill_level > 4 and stat_level > 5:
            person.opinions[skill] = [2, known]
        elif skill_level > 3 and stat_level > 4:
            person.opinions[skill] = [1, known]
        elif skill in person.opinions:
            del person.opinions[skill]
        return

    # when she doesn't like base_topic, she should not like / love related topic (invert likeness of related topic)
    def fix_opinion_contradiction(person, base_topic, related_topic):
        # first skew related to positive base
        if person.get_opinion_score(base_topic) > 0 and person.get_opinion_score(related_topic) < 0:
            person.update_opinion_with_score(related_topic, -person.get_opinion_score(related_topic), add_to_log = False)
        if person.get_opinion_score(base_topic) < 0 and person.get_opinion_score(related_topic) > 0:
            person.update_opinion_with_score(related_topic, -person.get_opinion_score(related_topic), add_to_log = False)
        return

    def fix_opinion_exclusion(person, base_topic, related_topic):
        if person.get_opinion_score(base_topic) > 0 and person.get_opinion_score(related_topic) > 0:
            person.update_opinion_with_score(related_topic, -person.get_opinion_score(related_topic), add_to_log = False)
        if person.get_opinion_score(base_topic) < 0 and person.get_opinion_score(related_topic) < 0:
            person.update_opinion_with_score(related_topic, -person.get_opinion_score(related_topic), add_to_log = False)
        return

    def ensure_opinion_on_subject(person, opinions):
        if not any(x[0] in person.opinions for x in opinions):
            the_opinion_key = get_random_from_list(opinions)
            degree = get_random_from_list([-2,-1,1,2])
            person.opinions[the_opinion_key] = [degree, False]
        return

    def ensure_sexy_opinion_on_subject(person, opinions):
        if not any(x[0] in person.opinions for x in opinions):
            the_opinion_key = get_random_from_list(opinions)
            degree = get_random_from_list([-2,-1,1,2])
            person.sexy_opinions[the_opinion_key] = [degree, False]
        return

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
        return

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
        # turn alpha personality on or off
        update_alpha_personality(person)
        # A person could have dialog even if we don't know her
        if person.possessive_title is None:
            person.set_possessive_title("The unknown woman")
        return

    def update_cougar_personality(person):
        if "cougar_personality" in globals() and "unique_character_list" in globals():
            # change personality to cougar if we meet age requirement
            if find_in_list(lambda x: x.effect == "cougar_personality_dummy_label", action_mod_list).enabled:
                if  person.age > 45 and person not in unique_character_list:
                    if not person.personality is cougar_personality:
                        person.original_personality = person.personality
                        person.personality = cougar_personality
                        # mc.log_event((person.title or person.name) + "  A:" + str(person.age) + ": " + person.personality.personality_type_prefix, "float_text_grey")
            else:
                if person.personality is cougar_personality:
                    if person not in unique_character_list:
                        if not (person.original_personality is None or person.original_personality == cougar_personality):
                            person.personality = person.original_personality
                        else:
                            new_personality = get_random_from_list(list_of_personalities)
                            person.personality = new_personality
                        # mc.log_event((person.title or person.name) + " D:" + str(person.age) + ": " + person.personality.personality_type_prefix, "float_text_grey")
        return

    def update_alpha_personality(person):
        if "alpha_personality" in globals() and "unique_character_list" in globals():
            # change personality to alpha if we meet requirements
            if find_in_list(lambda x: x.effect == "alpha_personality_dummy_label", action_mod_list).enabled:
                if person.age > 25 and person.charisma >= 5 and person.int >= 4 and person.get_opinion_score("taking control") > 0 and person not in unique_character_list:
                    if not person.personality is alpha_personality:
                        person.original_personality = person.personality
                        person.personality = alpha_personality
                        # mc.log_event((person.title or person.name) + "  A:" + str(person.age) + ": " + person.personality.personality_type_prefix, "float_text_grey")
            else:
                if person.personality is alpha_personality:
                    if person not in unique_character_list:
                        if not (person.original_personality is None or person.original_personality == alpha_personality):
                            person.personality = person.original_personality
                        else:
                            new_personality = get_random_from_list(list_of_personalities)
                            person.personality = new_personality
                        # mc.log_event((person.title or person.name) + " D:" + str(person.age) + ": " + person.personality.personality_type_prefix, "float_text_grey")
        return


    def rebuild_wardrobe(person, force = False):
        # skip personalized wardrobes
        if not force and not person.wardrobe.name.startswith(person.name + "'s Wardrobe"):
            return

        base_wardrobe = Wardrobe("[person.name]_[person.last_name]_wardrobe")
        preferences = WardrobePreference(person)
        outfit_builder = WardrobeBuilder(person)

        for outfit in renpy.random.sample(default_wardrobe.outfits, __builtin__.len(default_wardrobe.outfits)):
            if outfit.has_overwear() and preferences.evaluate_outfit(outfit, 999) and outfit_builder.approves_outfit_color(outfit):
                base_wardrobe.add_outfit(outfit.get_copy())
            if __builtin__.len(base_wardrobe.outfits) > 7:
                break

        for overwear in renpy.random.sample(default_wardrobe.overwear_sets, __builtin__.len(default_wardrobe.overwear_sets)):
            if overwear.is_suitable_overwear_set() and preferences.evaluate_outfit(overwear, 999) and outfit_builder.approves_outfit_color(overwear):
                base_wardrobe.add_overwear_set(overwear.get_copy())
            if __builtin__.len(base_wardrobe.overwear_sets) > 7:
                break

        for underwear in renpy.random.sample(default_wardrobe.underwear_sets, __builtin__.len(default_wardrobe.underwear_sets)):
            if underwear.is_suitable_underwear_set() and preferences.evaluate_outfit(underwear, 999) and outfit_builder.approves_outfit_color(underwear):
                base_wardrobe.add_underwear_set(underwear.get_copy())
            if __builtin__.len(base_wardrobe.underwear_sets) > 7:
                break

        # ensure we have at least 3 auto generated outfits by removing surplus, but keep the most decent outfit from default wardrobe
        while __builtin__.len(base_wardrobe.outfits) > 5:
            base_wardrobe.remove_outfit(sorted(base_wardrobe.outfits, key = lambda x: x.slut_requirement)[renpy.random.randint(1,__builtin__.len(base_wardrobe.outfits)-1)])
        while __builtin__.len(base_wardrobe.overwear_sets) > 5:
            base_wardrobe.remove_outfit(sorted(base_wardrobe.overwear_sets, key = lambda x: x.slut_requirement)[renpy.random.randint(1,__builtin__.len(base_wardrobe.overwear_sets)-1)])
        while __builtin__.len(base_wardrobe.underwear_sets) > 5:
            base_wardrobe.remove_outfit(sorted(base_wardrobe.underwear_sets, key = lambda x: x.slut_requirement)[renpy.random.randint(1,__builtin__.len(base_wardrobe.underwear_sets)-1)])

        person.wardrobe = base_wardrobe

        # add make-up to base outfit (based on pref)
        add_make_up_to_outfit(person, person.base_outfit)

        enhance_existing_wardrobe(person, 8)
        return

    def create_bimbo():
        # add one bimbo to the game (on start of game)
        person = make_person(age=renpy.random.randint(25, 35), tits="DD", body_type = "standard_body", face_style = "Face_4", skin = "tan",
            hair_colour = ["platinum blonde", [0.789, 0.746, 0.691,1]], hair_style = messy_hair, eyes = ["light blue", [0.60, 0.75, 0.98, 1.0]], personality = bimbo_personality, force_random = True)
        person.generate_home()
        person.home.add_person(person)
        return

    def create_alpha_personality():
        person = make_person(age = renpy.random.randint(25,35), personality = alpha_personality, relationship = "Single", stat_array = [5, 4, 3], force_random = True,
            forced_opinions = [["high heels", 2, False], ["skimpy outfits", 2, False], ["the colour black", 2, False], ["the colour pink", -2, False], ["the colour green", -2, False]],
            forced_sexy_opinions = [["being submissive", -1, False], ["taking control", 2, False]])
        person.generate_home()
        person.home.add_person(person)
        return

    def create_hooker(add_to_game = True):
        person = make_person(start_sluttiness = renpy.random.randint(25, 40), force_random = True, forced_opinions = [
                ["flirting", 2, True],
                ["skirts", 2, True],
                ["high heels", 2, True],
                ["pants", -2, False],
                ["makeup", 1, True],
                ["skimpy outfits", 2, True],
                ["the colour red", 2, False],
                ["the colour yellow", 2, False],
                ["the colour black", -2, False],
                ["the colour white", -2, False],
                ["the colour green", -2, False],
            ], forced_sexy_opinions = [
                ["being submissive", 1, False],
                ["bareback sex", -2, True],
                ["giving blowjobs", 2, False],
                ["vaginal sex", 2, False],
                ["public sex", 2, False],
                ["showing her tits", 1, False],
            ])
        person.set_mc_title("Sir")
        person.add_role(prostitute_role)
        if add_to_game:
            person.generate_home()
            person.home.add_person(person)
        return person

    def create_stripper():
        person = make_person(start_sluttiness = renpy.random.randint(15,30), force_random = True, forced_opinions = [
                ["skimpy outfits", 2, True],
                ["high heels", 2, True],
            ], forced_sexy_opinions = [
                ["showing her tits", 2, True],
                ["showing her ass", 2, True],
                ["taking control", 2, True],
            ])
        person.set_mc_title("Honey")
        person.generate_home()
        person.home.add_person(person)
        return person

    def update_characters():
        for person in all_people_in_the_game(unique_character_list):
            update_person_opinions(person)
            update_random_person(person)
            rebuild_wardrobe(person)
            update_person_outfit(person, -0.2) # choose a less slutty outfit as planned outfit
        return

    def update_special_characters_opinions():
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

    def update_lingerie_wardrobe():
        global lingerie_wardrobe
        lingerie_wardrobe = lingerie_wardrobe.merge_wardrobes(wardrobe_from_xml("Lingerie_Extended_Wardrobe"))
        return

    unique_character_list = []  # global not stored variable (since not defined in label function)

    def create_unique_character_list():
        # use extend when adding a list to another list
        unique_character_list.extend([mom, lily, aunt, cousin, stephanie, alexia, nora, emily, christina])

        # mod unique characters (check for existence first)
        if "salon_manager" in globals():
            unique_character_list.append(salon_manager)

        if "starbuck" in globals():
            unique_character_list.append(starbuck)

        if "sarah" in globals():
            unique_character_list.append(sarah)

        if "dawn" in globals():
            unique_character_list.append(dawn)

        if "candace" in globals():
            unique_character_list.append(candace)

        if "ashley" in globals():
            unique_character_list.append(ashley)

        if "erica" in globals():
            unique_character_list.append(erica)

        # disable for now, random outfits remove uniqueness of character in story line
        # make sure unique characters have at least six outfits / overwear sets to choose from
        #python:
        #    for person in unique_character_list:
        #        enhance_existing_wardrobe(person, 6)
        return

    def update_stripclub_strippers():
        for person in stripclub_strippers:
            person.location().people.remove(person)
            list_of_places.remove(person.home)
            person.remove_person_from_game()
        stripclub_strippers.clear()

        for i in __builtin__.range(0,4):
            person = create_stripper()
            person.set_schedule(strip_club, times = [3,4])
            stripclub_strippers.append(person)
        return

    def update_main_character_actions():
        if "main_character_actions_list" in globals():
            for action in main_character_actions_list:
                if action not in mc.main_character_actions:
                    mc.main_character_actions.append(action)
        return


label activate_generic_personality(stack):
    python:
        create_unique_character_list()

        create_bimbo()

        # create two random people with the alpha personality (they have a very low chance of being created at random)
        for i in __builtin__.range(2):
            create_alpha_personality()

        # add two random hookers to the game (on start of game)
        for i in __builtin__.range(2):
            create_hooker()

        update_main_character_actions()

        update_characters()

        update_special_characters_opinions()

        update_unique_character_wardrobes()

        update_lingerie_wardrobe()

        update_stripclub_strippers()

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_generic_personality(stack):
    python:
        create_unique_character_list()

        update_main_character_actions()

        update_lingerie_wardrobe()

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return
