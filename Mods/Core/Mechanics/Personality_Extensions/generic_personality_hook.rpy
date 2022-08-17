# Generic Personality Hook by Tristimdorion
# overrides the default make person function in the game
# so we can add / change person characteristics based on custom personalities.
# if you need person customizations, extend the hijacked labels
init 2:
    default persistent.low_memory_wardrobes = True

init 10 python: # add to stack later then other mods
    add_label_hijack("normal_start", "activate_generic_personality")
    add_label_hijack("after_load", "update_generic_personality")

init 2 python:
    # This will be called in game when a person is created original function in script.rpy
    def make_person(name = None, name_list = None, last_name = None, last_name_list = None, age = None, age_range = None, body_type = None, body_type_list = None, face_style = None, face_style_list = None, tits = None, tits_range = None, height = None, height_range = None,
        hair_colour = None, hair_colour_list = None, hair_style = None, hair_style_list = None, pubes_colour = None, pubes_colour_list = None, pubes_style = None, pubes_style_list = None, skin = None, skin_list = None, eyes = None, eyes_list = None, job = None, job_list = None,
        personality = None, personality_list = None, custom_font = None, custom_font_list = None, name_color = None, name_color_list = None, dial_color = None, dial_color_list = None, starting_wardrobe = None, starting_wardrobe_list = None, stat_array = None, stat_range_array = None, skill_array = None, skill_range_array = None,
        sex_skill_array = None, sex_skill_range_array = None, sluttiness = None, sluttiness_range = None, obedience = None, obedience_range = None, happiness = None, happiness_range = None, love = None, love_range = None, start_home = None,
        title = None, title_list = None, possessive_title = None, possessive_title_list = None, mc_title = None, mc_title_list = None, relationship = None, relationship_list = None, kids = None, kids_range = None, kids_floor = None, kids_ceiling = None, SO_name = None, SO_name_list = None, base_outfit = None, base_outfit_list = None,
        generate_insta = None, generate_dikdok = None, generate_onlyfans = None,
        suggestibility = None, suggestibility_range = None, work_experience = None, work_experience_range = None,
        tan_style = None, force_random = False, forced_opinions = None, forced_sexy_opinions = None, type = 'random'):

        return_character = None
        if not force_random and renpy.random.randint(1,100) < 20:
            return_character = get_premade_character()

        if personality is None: # we need a personality to set the bonus suggest
            if personality_list is None:
                personality = get_random_personality()
            else:
                personality =  get_random_from_list(personality_list)

        if skin is None:
            if skin_list is None:
                skin_style = Person.get_random_skin()
            else:
                skin_style = get_random_from_list(skin_list).get_copy()


        if pubes_style is None:
            if pubes_style_list is None:
                pubes_style = Person.get_random_pubes_style()
            else:
                pubes_style = get_random_from_list(pubes_style_list).get_copy()

        if hair_style is None:
            if hair_style_list is None:
                hair_style = Person.get_random_hair_style()
            else:
                hair_style = get_random_from_list(hair_style_list).get_copy()

        if age_range is None:
            age_range = [Person.get_age_floor(), Person.get_age_ceiling()]
        elif (age_range[0] > age_range[1]): #Make sure range is correct order
            age_range.reverse()

        if suggestibility is None:
            if suggestibility_range is None:
                suggestibility_range = [Person.get_suggestibility_floor(),Person.get_suggestibility_ceiling()]

            suggestibility = renpy.random.randint(suggestibility_range[0],suggestibility_range[1])

            if personality.base_personality_prefix == wild_personality.personality_type_prefix:
                suggestibility += 5
            elif personality.base_personality_prefix == bimbo_personality.personality_type_prefix:
                suggestibility += 10
            elif personality.base_personality_prefix == relaxed_personality.personality_type_prefix:
                suggestibility += 3
            elif personality.base_personality_prefix == introvert_personality.personality_type_prefix:
                suggestibility -= 3
            elif personality.base_personality_prefix == reserved_personality.personality_type_prefix:
                suggestibility -= 5

            if suggestibility < 0:
                suggestibility = 0

        if age is None: # use linear decreasing distribution in age range (more young than old)
            age = int(floor(abs(renpy.random.random() - renpy.random.random()) * (1 + age_range[1] - age_range[0]) + age_range[0]))

        if relationship is None:
            if relationship_list is None:
                if age < 21:
                    relationship = get_random_from_weighted_list([["Single", 70], ["Girlfriend", 30]])
                elif age < 26:
                    relationship = get_random_from_weighted_list([["Single", 30], ["Girlfriend", 50], ["Fiancée", 20]])
                elif age < 31:
                    relationship = get_random_from_weighted_list([["Single", 10], ["Girlfriend", 30], ["Fiancée", 40], ["Married", 20]])
                else:
                    relationship = get_random_from_weighted_list([["Single", 80 - age], ["Girlfriend", 100 - age], ["Fiancée", age * 3], ["Married", age * 4]])

        if mc_title is None:
            mc_title = "Stranger"

        if return_character is None: #Either we aren't getting a pre-made, or we are out of them.
            return_character = create_random_person(name = name, name_list = name_list, last_name = last_name, last_name_list = last_name_list, age = age, age_range = age_range, body_type = body_type, body_type_list = body_type_list, face_style = face_style, face_style_list = face_style_list, tits = tits, tits_range = tits_range, height = height, height_range = height_range,
            hair_colour = hair_colour, hair_colour_list = hair_colour_list, hair_style = hair_style, hair_style_list = hair_style_list, pubes_colour = pubes_colour, pubes_colour_list = pubes_colour_list, pubes_style = pubes_style, pubes_style_list = pubes_style_list, skin = skin, skin_list = skin_list, eyes = eyes, eyes_list = eyes_list, job = job, job_list = job_list,
            personality = personality, personality_list = personality_list, custom_font = custom_font, custom_font_list = custom_font_list, name_color = name_color, name_color_list = name_color_list, dial_color = dial_color, dial_color_list = dial_color_list, starting_wardrobe = starting_wardrobe, starting_wardrobe_list = starting_wardrobe_list, stat_array = stat_array, stat_range_array = stat_range_array, skill_array = skill_array, skill_range_array = skill_range_array,
            sex_skill_array = sex_skill_array, sex_skill_range_array = sex_skill_range_array, sluttiness = sluttiness, sluttiness_range = sluttiness_range, obedience = obedience, obedience_range = obedience_range, happiness = happiness, happiness_range = happiness_range, love = love, love_range = love_range, start_home = start_home,
            title = title, title_list = title_list, possessive_title = possessive_title, possessive_title_list = possessive_title_list, mc_title = mc_title, mc_title_list = mc_title_list, relationship = relationship, relationship_list = relationship_list, kids = kids, kids_range = kids_range, kids_floor = kids_floor, kids_ceiling = kids_ceiling, SO_name = SO_name, SO_name_list = SO_name_list, base_outfit = base_outfit, base_outfit_list = base_outfit_list,
            generate_insta = generate_insta, generate_dikdok = generate_dikdok, generate_onlyfans = generate_onlyfans,
            suggestibility = suggestibility, suggestibility_range = suggestibility_range, work_experience = work_experience, work_experience_range = work_experience_range, type = type)

        if tan_style is None:
            if renpy.random.randint(0, 1) == 1: # 50% chance on random tan (could be no_tan)
                return_character.tan_style = get_random_from_list(tan_list)
            if return_character.tan_style == no_tan:
                return_character.tan_style = None
        else:
            return_character.tan_style = tan_style

        # when not using bugfix, remove the employed_since key from event trigger dictionary (this should only be used for employees)
        if return_character.event_triggers_dict.get("employed_since", -1) != -1:
            del return_character.event_triggers_dict["employed_since"]

        update_person_opinions(return_character)
        update_random_person(return_character)

        # apply forced opinions after we 'update opinions', so we don't override them there
        if forced_opinions and isinstance(forced_opinions, list):
            return_character.reset_opinions()
            for opinion in forced_opinions:
                return_character.opinions[opinion[0]] = [opinion[1], opinion[2]]

        if forced_sexy_opinions and isinstance(forced_sexy_opinions, list):
            return_character.reset_sexy_opinions()
            for opinion in forced_sexy_opinions:
                return_character.sexy_opinions[opinion[0]] = [opinion[1], opinion[2]]

        if not starting_wardrobe:
            rebuild_wardrobe(return_character)
        update_person_outfit(return_character, -0.2) # choose a less slutty outfit as planned outfit

        if return_character.type == 'random':
            create_party_schedule(return_character)

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
        fix_opinion_contradiction(person, "drinking cum", ["giving blowjobs"])
        fix_opinion_contradiction(person, "bareback sex", ["creampies", "anal creampies"])
        fix_opinion_contradiction(person, "skimpy outfits", ["showing her tits", "showing her ass", "high heels"])
        fix_opinion_contradiction(person, "masturbating", ["being fingered"])

        # fix opinion exclusion (one excludes other)
        fix_opinion_exclusion(person, "lingerie", ["not wearing underwear", "not wearing anything"])
        fix_opinion_exclusion(person, "skimpy outfits", ["not wearing anything", "conservative outfits"])
        fix_opinion_exclusion(person, "being submissive", ["taking control"])
        fix_opinion_exclusion(person, "the colour red", ["the colour pink", "the colour purple"]) # red and pink/purple clash
        fix_opinion_exclusion(person, "the colour pink", ["the colour purple", "the colour red"]) # pink and purple/red clash
        fix_opinion_exclusion(person, "the colour purple", ["the colour pink", "the colour red", "the colour blue"]) # purple and pink/red/blue clash
        fix_opinion_exclusion(person, "the colour blue", ["the colour purple"]) # pink and purple clash
        fix_opinion_exclusion(person, "the colour orange", ["the colour yellow"]) # orange and yellow clash

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
    def fix_opinion_contradiction(person, base_topic, related_topics):
        for related_topic in related_topics:
            # first skew related to positive base
            if person.get_opinion_score(base_topic) > 0 and person.get_opinion_score(related_topic) < 0:
                person.update_opinion_with_score(related_topic, -person.get_opinion_score(related_topic), add_to_log = False)
            if person.get_opinion_score(base_topic) < 0 and person.get_opinion_score(related_topic) > 0:
                person.update_opinion_with_score(related_topic, -person.get_opinion_score(related_topic), add_to_log = False)
        return

    def fix_opinion_exclusion(person, base_topic, related_topics):
        for related_topic in related_topics:
            if person.get_opinion_score(base_topic) > 0 and person.get_opinion_score(related_topic) > 0:
                person.update_opinion_with_score(related_topic, -person.get_opinion_score(related_topic), add_to_log = False)
            if person.get_opinion_score(base_topic) < 0 and person.get_opinion_score(related_topic) < 0:
                person.update_opinion_with_score(related_topic, -person.get_opinion_score(related_topic), add_to_log = False)
        return

    def ensure_opinion_on_subject(person, opinions):
        if not any(x[0] in person.opinions for x in opinions):
            the_opinion_key = get_random_from_list(opinions)
            degree = renpy.random.choice([-2,-1,1,2])
            person.opinions[the_opinion_key] = [degree, False]
        return

    def ensure_sexy_opinion_on_subject(person, opinions):
        if not any(x[0] in person.opinions for x in opinions):
            the_opinion_key = get_random_from_list(opinions)
            degree = renpy.random.choice([-2,-1,1,2])
            person.sexy_opinions[the_opinion_key] = [degree, False]
        return

    def ensure_opinion_on_sexual_preference(person, sex_skill, opinions):
        if not any(x[0] in person.sexy_opinions for x in opinions):
            the_opinion_key = get_random_from_list(opinions)
            if person.sex_skills[sex_skill] >= 3: # positive skew
                degree = renpy.random.choice([1,2])
            elif person.sex_skills[sex_skill] < 1: # negative skew
                degree = renpy.random.choice([-2, -1])
            else: # random
                degree = renpy.random.choice([-2,-1,1,2])
            person.sexy_opinions[the_opinion_key] = [degree, False]
        return

    # make sure new character has a more appropriate outfit to wear
    def update_person_outfit(person, sluttiness_modifier = 0.0):
        if not "unique_character_list" in globals() or not person in unique_character_list:
            person.planned_outfit = person.decide_on_outfit(sluttiness_modifier) # Use enhanced outfit selector
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
        if not force and persistent.low_memory_wardrobes:
            person.wardrobe = base_wardrobe
            return

        preferences = WardrobePreference(person)
        outfit_builder = WardrobeBuilder(person)

        for outfit in renpy.random.sample(default_wardrobe.outfits, __builtin__.len(default_wardrobe.outfits)):
            if not outfit.has_clothing(sweater_dress) and outfit.has_overwear() and preferences.evaluate_outfit(outfit, 999) and outfit_builder.approves_outfit_color(outfit):
                base_wardrobe.add_outfit(outfit.get_copy())
            if __builtin__.len(base_wardrobe.outfits) > 5:
                break

        for overwear in renpy.random.sample(default_wardrobe.overwear_sets, __builtin__.len(default_wardrobe.overwear_sets)):
            if not outfit.has_clothing(sweater_dress) and overwear.is_suitable_overwear_set() and preferences.evaluate_outfit(overwear, 999) and outfit_builder.approves_outfit_color(overwear):
                base_wardrobe.add_overwear_set(overwear.get_copy())
            if __builtin__.len(base_wardrobe.overwear_sets) > 5:
                break

        for underwear in renpy.random.sample(default_wardrobe.underwear_sets, __builtin__.len(default_wardrobe.underwear_sets)):
            if underwear.is_suitable_underwear_set() and preferences.evaluate_outfit(underwear, 999) and outfit_builder.approves_outfit_color(underwear):
                base_wardrobe.add_underwear_set(underwear.get_copy())
            if __builtin__.len(base_wardrobe.underwear_sets) > 5:
                break

        # ensure we have at least 2 base wardrobe outfits by removing surplus, but keep the most decent outfit from default wardrobe
        while __builtin__.len(base_wardrobe.outfits) > 3:
            base_wardrobe.remove_outfit(sorted(base_wardrobe.outfits, key = lambda x: x.slut_requirement)[renpy.random.randint(1,__builtin__.len(base_wardrobe.outfits)-1)])
        while __builtin__.len(base_wardrobe.overwear_sets) > 3:
            base_wardrobe.remove_outfit(sorted(base_wardrobe.overwear_sets, key = lambda x: x.slut_requirement)[renpy.random.randint(1,__builtin__.len(base_wardrobe.overwear_sets)-1)])
        while __builtin__.len(base_wardrobe.underwear_sets) > 3:
            base_wardrobe.remove_outfit(sorted(base_wardrobe.underwear_sets, key = lambda x: x.slut_requirement)[renpy.random.randint(1,__builtin__.len(base_wardrobe.underwear_sets)-1)])

        person.wardrobe = base_wardrobe

        # add make-up to base outfit (based on pref)
        add_make_up_to_outfit(person, person.base_outfit)

        # add some auto generated outfits (max 4 outfits per category)
        enhance_existing_wardrobe(person, 4)
        return

    def get_party_destinations():
        party_destinations = []

        if not "downtown_bar" in globals():     # skip party locations while running tutorial
            return party_destinations

        def add_party_destination_by_room(room):    # add correct room object from list_of_places (prevents people disappearing)
            found = find_in_list(lambda x: x.name == room.name, list_of_places)
            if found:
                party_destinations.append(found)

        for room in [downtown_bar, downtown_hotel, downtown]:
            add_party_destination_by_room(room)

        if "get_strip_club_foreclosed_stage" in globals():
            if not strip_club_is_closed():
                add_party_destination_by_room(strip_club)
                if mc.business.event_triggers_dict.get("strip_club_has_bdsm_room", False):
                    add_party_destination_by_room(bdsm_room)
        else:
            add_party_destination_by_room(strip_club)

        return party_destinations


    def create_party_schedule(person):
        if not "Schedule" in globals():
            return

        if person in unique_character_list:
            return  # don't touch unique characters
        if person.has_role([stripper_role, stripclub_stripper_role, stripclub_waitress_role, stripclub_bdsm_performer_role, stripclub_mistress_role, stripclub_manager_role]) or person in stripclub_strippers:
            return  # no party for the working girls
        if person.pregnancy_is_visible():
            return  # no party for girls who already show the baby bump

        # clear old party schedule (clear after stripper check as to not clear her override schedule during foreclosed phase)
        person.set_override_schedule(None, the_times = [4])

        count = 0
        party_destinations = get_party_destinations()
        if person.get_opinion_score("Mondays") > 0:
            person.set_override_schedule(renpy.random.choice(party_destinations), the_days = [0], the_times=[4])
            count += 1
        if person.get_opinion_score("Fridays") > 0:
            person.set_override_schedule(renpy.random.choice(party_destinations), the_days = [4], the_times=[4])
            count += 1
        if person.get_opinion_score("the weekend") > 0:
            person.set_override_schedule(renpy.random.choice(party_destinations), the_days = [5], the_times=[4])
            person.set_override_schedule(renpy.random.choice(party_destinations), the_days = [6], the_times=[4])
            count += 2

        while count < 2:
            rnd_day = renpy.random.randint(0, 6)
            person.set_override_schedule(renpy.random.choice(party_destinations), the_days = [rnd_day], the_times=[4])
            count += 1
        return

    def create_bimbo():
        # add one bimbo to the game (on start of game)
        person = make_person(age=renpy.random.randint(21, 35), tits="DD", face_style = "Face_4", skin = "tan", stat_array = [4, 1, 2],
            hair_colour = ["platinum blonde", [.789, .746, .691, 1]], hair_style = messy_hair, eyes = ["light blue", [0.60, 0.75, 0.98, 1.0]], personality = bimbo_personality, force_random = True,
            forced_opinions = [["high heels", 2, False]],
            forced_sexy_opinions = [["skimpy outfits", 2, False]])
        person.generate_home()
        person.home.add_person(person)
        return

    def create_alpha_personality():
        person = make_person(age = renpy.random.randint(25,35), personality = alpha_personality, relationship = "Single", stat_array = [5, 4, 3], force_random = True,
            forced_opinions = [["high heels", 2, False], ["the colour black", 2, False], ["the colour pink", -2, False], ["the colour green", -2, False]],
            forced_sexy_opinions = [["skimpy outfits", 2, False], ["being submissive", -1, False], ["taking control", 2, False]])
        person.generate_home()
        person.home.add_person(person)
        return

    def create_hooker(add_to_game = True):
        person = make_person(sluttiness = renpy.random.randint(25, 40), force_random = True, forced_opinions = [
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
        person.set_mc_title("Honey")
        person.change_job(prostitute_job)
        if add_to_game:
            person.generate_home()
            person.home.add_person(person)
        return person

    def create_stripper():
        person = make_person(sluttiness = renpy.random.randint(15,30),
            job = stripper_job,
            force_random = True,
            forced_opinions = [
                ["skimpy outfits", 2, True],
                ["high heels", 2, True],
            ], forced_sexy_opinions = [
                ["showing her tits", 2, True],
                ["showing her ass", 2, True],
                ["taking control", 2, True],
            ])
        update_person_opinions(person) # add random opinions
        update_random_person(person)
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
            create_party_schedule(person)

        # setup christina as Trophy Wife
        trophy_wife = Job("Trophy Wife", critical_job_role)
        christina.change_job(trophy_wife)
        return

    def update_special_characters_opinions():
        for person in unique_character_list:
            update_person_opinions(person)

        if "list_of_unique_characters" in globals():
            # update random characters in game
            for person in list_of_unique_characters:
                person.is_patreon = True
                update_person_opinions(person)
                update_random_person(person)
                # rebuild_wardrobe(person) # Don't change their wardrobe, it's personalized
                update_person_outfit(person, -0.2) # choose a less slutty outfit as planned outfit
                create_party_schedule(person)
        return

    def get_premade_character():
        if len(list_of_unique_characters) == 0: # no more pre-made left
            return None

        person = renpy.random.choice(list_of_unique_characters)

        # improve stats for pre-made characters to be on par with random generated characters
        if recruitment_skill_improvement_policy.is_active():
            person.hr_skill += renpy.random.randint(1, 2)
            person.market_skill += renpy.random.randint(1, 2)
            person.research_skill += renpy.random.randint(1, 2)
            person.production_skill += renpy.random.randint(1, 2)
            person.supply_skill += renpy.random.randint(1, 2)

        if recruitment_stat_improvement_policy.is_active():
            person.charisma += renpy.random.randint(1, 2)
            person.int += renpy.random.randint(1, 2)
            person.focus += renpy.random.randint(1, 2)

        update_person_opinions(person)  # fixes pre-made character opinions and contradictions

        list_of_unique_characters.remove(person)
        return person

    def update_unique_character_wardrobes():
        # Extend unique character wardrobes
        mom.wardrobe = mom.wardrobe.merge_wardrobes(wardrobe_from_xml("Mom_Extended_Wardrobe"), keep_primary_name = True)
        lily.wardrobe = lily.wardrobe.merge_wardrobes(wardrobe_from_xml("Lily_Extended_Wardrobe"), keep_primary_name = True)

        # remove strange outfits (they should not be in her wardrobe at all)
        mom.wardrobe.remove_outfit("Mom_Apron")
        mom.wardrobe.remove_outfit("lingerie_1")
        lily.wardrobe.remove_outfit("pink_lingerie")
        stephanie.wardrobe.remove_outfit("Nude")
        return

    unique_character_list = []  # global not stored variable (since not defined in label function)

    def create_unique_character_list():
        # use extend when adding a list to another list
        unique_character_list.extend([mom, lily, aunt, cousin, stephanie, alexia, nora, emily, christina, city_rep])

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

        if "camilla" in globals():
            unique_character_list.append(camilla)

        if "kaya" in globals():
            unique_character_list.append(kaya)

        if "ellie" in globals():
            unique_character_list.append(ellie)

        if "sakari" in globals():
            unique_character_list.append(sakari)

        if "myra" in globals():
            unique_character_list.append(myra)

        return

    def update_stripclub_strippers():
        # create new set of stripper characters
        for person in stripclub_strippers[:]:   #use copy of array
            person.job.quit_function = stripper_quit # override quit function to prevent new generation
            person.quit_job()
            person.remove_person_from_game()

        # make sure we have the original quit_function on the stripper_job
        stripper_job.quit_function = stripper_replace

        for i in __builtin__.range(0,4):
            person = create_stripper()

        # make sure one of the strippers an alpha-personality (simplifies stripclub story-line)
        alpha_stripper = get_random_from_list([x for x in stripclub_strippers if x.age >= 25 and not x.personality == alpha_personality])
        if alpha_stripper:
            alpha_stripper.original_personality = alpha_stripper.personality
            alpha_stripper.personality = alpha_personality
            alpha_stripper.charisma = 5
            alpha_stripper.int = 6
            alpha_stripper.update_opinion_with_score(2, "taking control", False)
            alpha_stripper.update_opinion_with_score(-1, "being submissive", False)
        return

    def update_main_character_actions():
        if "main_character_actions_list" in globals():
            for action in main_character_actions_list:
                if action not in mc.main_character_actions:
                    mc.main_character_actions.append(action)

            # cleanup (remove next version)
            found = next((x for x in mc.main_character_actions if x.effect in ["mc_hire_person_label", "mc_pay_to_strip_label"]), None)
            if found:
                mc.main_character_actions.remove(found)
        return

    def update_stephanie_opinions():
        # boost her research stats (to increase research boost at game start)
        stephanie.research_skill = 6
        stephanie.focus = 5

        # set opinions to make initial game work
        stephanie.opinions["research work"] = [2, True]  # she loves research work
        stephanie.opinions["small talk"] = [1, False]  # she likes small talk
        stephanie.opinions["flirting"] = [1, False]  # she likes flirting

        # make sure she has no opinion on conservative outfits (affects happiness)
        if any("conservative outfits" in s for s in stephanie.opinions):
            del stephanie.opinions["conservative outfits"]

        stephanie.sexy_opinions["kissing"] = [1, False]  # she likes kissing
        stephanie.sexy_opinions["vaginal sex"] = [2, False] # she likes having sex
        return

    def update_alexia_opinions():
        # boost her marketing stats
        alexia.market_skill = 6
        alexia.charisma = 5

        alexia.opinions["marketing work"] = [2, True]   # she loves marketing
        alexia.opinions["flirting"] = [1, False]  # she likes flirting

        # make sure she has no opinion on conservative outfits (affects happiness)
        if any("conservative outfits" in s for s in stephanie.opinions):
            del stephanie.opinions["conservative outfits"]

        alexia.sexy_opinions["kissing"] = [1, False]  # she likes kissing
        alexia.sexy_opinions["cheating on men"] = [-2, False]  # she loves her boyfriend
        return

    def get_titles_extended(org_func):
        def get_titles_wrapper(person):
            list_of_titles = org_func(person)

            if person not in unique_character_list:
                if person.love > 30 and person.height > 1.1:
                    list_of_titles.append("Sexy Legs")
                    list_of_titles.append("Sky High")

                if person.love > 30 and person.height < 0.8:
                    list_of_titles.append("Tinkerbell")
                    list_of_titles.append("Little Lady")

                if person.love > 30 and person.sluttiness > 20 and person.get_opinion_score("high heels") >= 2:
                    list_of_titles.append("Killer Heels")

                if person.sluttiness > 80:
                    list_of_titles.append("Whore")

                if person.sluttiness > 50 and person.has_job(stripper_job):
                    list_of_titles.append("Pole-Slut")
                if person.love > 50 and person.has_job(stripclub_mistress_job):
                    list_of_titles.append("Milady")
                if person.sluttiness > 60 and person.has_job(stripclub_mistress_job):
                    list_of_titles.append("Mistress")

            return list(set(list_of_titles))

        return get_titles_wrapper

    # wrap original function
    Person.get_titles = get_titles_extended(Person.get_titles)

    def get_possessive_titles_extended(org_func):
        def get_possessive_titles_wrapper(person):
            list_of_titles = org_func(person)

            if person not in unique_character_list:
                if person.sluttiness > 80:
                    list_of_titles.append("Your whore")

                if person.has_job(stripper_job):
                    list_of_titles.append("Your exotic dancer")
                if person.love > 50 and person.has_job(stripclub_mistress_job):
                    list_of_titles.append("Your burlesque queen")
                if person.sluttiness > 50 and person.has_job(stripclub_mistress_job):
                    list_of_titles.append("Your kinky Mistress")
                if person.has_job(stripclub_waitress_job):
                    list_of_titles.append("Your waitress")
                if person.sluttiness > 50 and person.has_job(stripclub_manager_job):
                    list_of_titles.append("Your naughty Manager")

            return list(set(list_of_titles))

        return get_possessive_titles_wrapper

    Person.get_possessive_titles = get_possessive_titles_extended(Person.get_possessive_titles)

    def generate_random_mothers_and_daughters():
        for person in [x for x in all_people_in_the_game(excluded_people = unique_character_list) if x.age > 35 or x.age < 25]:
            if renpy.random.randint(0, 1) == 1:
                if person.age > 35:
                    for count in range(0, renpy.random.randint(1, 3)):
                        person.generate_daughter(True)
                else:
                    person.generate_mother(True)

    def generate_random_sisters_cousins_nieces():
        mothers = [x for x in all_people_in_the_game(excluded_people = unique_character_list) if town_relationships.get_existing_child_count(x) > 0]
        linked_mothers = []

        def get_new_mother_from_list():
            available_mothers = [x for x in mothers if x not in linked_mothers]
            if not available_mothers:
                return None
            mother = renpy.random.choice(available_mothers)
            linked_mothers.append(mother)
            return mother

        for i in range(4):
            mother = get_new_mother_from_list()
            other_mother = get_new_mother_from_list()

            if not mother or not other_mother:
                break

            town_relationships.update_relationship(mother, other_mother, "Sister")
            for cousin in town_relationships.get_existing_children(mother):
                town_relationships.update_relationship(other_mother, cousin, "Niece", "Aunt")
                for other_cousin in town_relationships.get_existing_children(other_mother):
                    town_relationships.update_relationship(cousin, other_cousin, "Cousin")
                    town_relationships.update_relationship(mother, other_cousin, "Niece", "Aunt")
        return

init 2 python:
    global lingerie_wardrobe
    lingerie_wardrobe = lingerie_wardrobe.merge_wardrobes(wardrobe_from_xml("Lingerie_Extended_Wardrobe"), keep_primary_name = True)

    global prostitute_wardrobe
    prostitute_wardrobe = wardrobe_from_xml("Prostitute_Wardrobe")

label activate_generic_personality(stack):
    python:
        create_unique_character_list()

        for i in __builtin__.range(2):
            create_bimbo()

        # create two random people with the alpha personality (they have a very low chance of being created at random)
        for i in __builtin__.range(3):
            create_alpha_personality()

        # add two random hookers to the game (on start of game)
        for i in __builtin__.range(3):
            create_hooker()

        update_main_character_actions()

        update_characters()

        update_special_characters_opinions()

        update_unique_character_wardrobes()

        update_stripclub_strippers()

        update_stephanie_opinions()
        update_alexia_opinions()

        generate_random_mothers_and_daughters()

        generate_random_sisters_cousins_nieces()

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_generic_personality(stack):
    python:
        create_unique_character_list()

        update_main_character_actions()

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return
