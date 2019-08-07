# Genric Personality Hook by Tristimdorion
# overrides the default make person function in the game
# so we can add / change person characteristics based on custom personalities.
# if you need person customizations, extend the hijacked labels

init 5 python:
    add_label_hijack("normal_start", "activate_generic_personality")
    add_label_hijack("after_load", "update_generic_personality")

init -1 python:
    # This will be called in game when a person is created orginal function in script.rpy
    def make_person():
        split_proportion = 20 #1/5 characters generated will be a premade character.
        return_character = None
        if renpy.random.randint(1,100) < split_proportion:
            return_character = get_premade_character()

        if return_character is None: #Either we aren't getting a premade, or we are out of them.
            # Use larger height range of person object (not full)
            return_character = create_random_person(height = 0.825 + (renpy.random.random()/7))

        update_random_person(return_character)
        update_person_roles(return_character)
        rebuild_wardrobe(return_character)
        update_person_outfit(return_character)

        return return_character

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

        makeup_list = [light_eye_shadow, heavy_eye_shadow, blush, lipstick]
        hide_ass_list = [lace_skirt, long_skirt, lab_coat, suitpants, two_part_dress, long_tshirt, camisole]
        hide_tits_list = [lab_coat, dress_shirt, long_sleeve_blouse, tie_sweater, long_sweater, bath_robe]
        boots_list = [boot_heels, tall_boots, thigh_high_boots]
        high_heels_list = [sandle_heels, pumps, heels, high_heels, boot_heels, thigh_high_boots]

        exclude_skirts, exclude_pants = get_skirt_and_pants_preference(person)
        lingerie = person.get_opinion_score("lingerie") > 0
        no_lingerie = person.get_opinion_score("lingerie") < 0
        skimpy_outfits = person.get_opinion_score("skimpy outfits") > 0 or person.get_opinion_score("conservative outfits") < 0
        conservative_outfits = person.get_opinion_score("conservative outfits") > 0
        make_up = person.get_opinion_score("makeup") > 0
        no_make_up = person.get_opinion_score("makeup") < 0
        show_tits = person.get_opinion_score("showing her tits") > 0
        no_show_tits = person.get_opinion_score("showing her tits") < 0
        show_ass = person.get_opinion_score("showing her ass") > 0
        no_show_ass = person.get_opinion_score("showing her ass") < 0
        minimum_items = person.get_opinion_score("not wearing anything")
        no_underwear = person.get_opinion_score("not wearing underwear")
        prefer_boots = person.get_opinion_score("boots") > 0
        no_boots = person.get_opinion_score("boots") < 0
        prefer_high_heels = person.get_opinion_score("high heels") > 0
        no_high_heels = person.get_opinion_score("high heels") < 0

        # renpy.say("",  person.name + "  " + person.last_name + ": " + (exclude_skirts and "no skirts, " or "") + (exclude_pants and "no pants, " or "") + (lingerie and "lingerie, " or "") 
        #     + (skimpy_outfits and "skimpy outfits, " or "") + (conservative_outfits and "conservative outfits, " or "") + (make_up and "make-up, " or "") + (no_make_up and "no make-up, " or "")
        #     + (prefer_boots and "boots, " or "") + (no_boots and "no boots, " or "") + (prefer_high_heels and "high heels, " or "") + (no_high_heels and "no heels, " or ""))

        base_wardrobe = Wardrobe(default_wardrobe.name)
        for outfit in default_wardrobe.outfits:
            if len(outfit.upper_body + outfit.lower_body + outfit.feet) < 2 - minimum_items:
                continue
            if exclude_skirts and (any(outfit.has_clothing(item) for item in skirts_list) or any(outfit.has_clothing(item) for item in dress_list)):
                continue
            if exclude_pants and any(outfit.has_clothing(item) for item in pants_list):
                continue
            if conservative_outfits and (outfit.vagina_visible() or outfit.tits_visible() or not outfit.bra_covered() or not outfit.panties_covered() or not outfit.wearing_panties() or not outfit.wearing_bra()):
                continue
            if skimpy_outfits and (outfit.slut_requirement < 15 or any(item.slut_value < 1 for item in outfit.feet)):
                continue
            if (show_tits and any(outfit.has_clothing(item) for item in hide_tits_list)) or (no_show_tits and not any(outfit.has_clothing(item) for item in hide_tits_list)):
                continue
            if (show_ass and any(outfit.has_clothing(item) for item in hide_ass_list)) or (no_show_ass and not any(outfit.has_clothing(item) for item in hide_ass_list)):
                continue
            if (no_make_up and any(outfit.has_clothing(item) for item in makeup_list)) or (make_up and not any(outfit.has_clothing(item) for item in makeup_list)):
                continue
            if (prefer_high_heels and not any(outfit.has_clothing(item) for item in high_heels_list)) or (no_high_heels and any(outfit.has_clothing(item) for item in high_heels_list)):
                continue
            if (prefer_boots and not any(outfit.has_clothing(item) for item in boots_list)) or (no_boots and any(outfit.has_clothing(item) for item in boots_list)):
                continue

            base_wardrobe.add_outfit(outfit.get_copy())

        for underwear in default_wardrobe.underwear_sets:
            if (not no_underwear and len(underwear.upper_body + underwear.lower_body + underwear.feet) < 1) or len(underwear.upper_body + underwear.lower_body + underwear.feet) > 1:
                continue
            if lingerie and (any(item.slut_value < 1 for item in underwear.lower_body) or any(item.slut_value < 1 for item in underwear.upper_body) or not underwear.wearing_panties()):
                continue
            if (no_lingerie or conservative_outfits) and (any(item.slut_value > 1 for item in underwear.lower_body) or any(item.slut_value > 1 for item in underwear.upper_body)):
                continue
            # there is no underwear with makeup
            #if (no_make_up and any(item in underwear.accessories for item in makeup_list)) or (make_up and not any(item in underwear.accessories for item in makeup_list)):
            #    continue

            base_wardrobe.add_underwear_set(underwear.get_copy())

        for overwear in default_wardrobe.overwear_sets:
            if len(overwear.upper_body + overwear.lower_body + overwear.feet) < 2 - minimum_items:
                continue
            if exclude_skirts and (any(overwear.has_clothing(item) for item in skirts_list) or any(overwear.has_clothing(item) for item in dress_list)):
                continue
            if exclude_pants and any(overwear.has_clothing(item) for item in pants_list):
                continue
            if conservative_outfits and (overwear.vagina_visible() or overwear.tits_visible() or not overwear.bra_covered() or not overwear.panties_covered() or not outfit.wearing_panties() or not outfit.wearing_bra()):
                continue
            if skimpy_outfits and (overwear.slut_requirement < 25 or any(item.slut_value < 1 for item in outfit.feet)):
                continue
            if (show_tits and any(overwear.has_clothing(item) for item in hide_tits_list)) or (no_show_tits and not any(overwear.has_clothing(item) for item in hide_tits_list)):
                continue
            if (show_ass and any(overwear.has_clothing(item) for item in hide_ass_list)) or (no_show_ass and not any(overwear.has_clothing(item) for item in hide_ass_list)):
                continue
            if (prefer_high_heels and not any(overwear.has_clothing(item) for item in high_heels_list)) or (no_high_heels and any(overwear.has_clothing(item) for item in high_heels_list)):
                continue
            if (prefer_boots and not any(overwear.has_clothing(item) for item in boots_list)) or (no_boots and any(overwear.has_clothing(item) for item in boots_list)):
                continue

            # renpy.say("", "Add overwear: " + overwear.name + "(Sluttiness: " + str(overwear.slut_requirement) + ")")
            base_wardrobe.add_overwear_set(overwear.get_copy())

        while len(base_wardrobe.outfits) > 6:
            base_wardrobe.remove_outfit(get_random_from_list(base_wardrobe.outfits))

        while len(base_wardrobe.underwear_sets) > 6:
            base_wardrobe.remove_outfit(get_random_from_list(base_wardrobe.underwear_sets))

        while len(base_wardrobe.overwear_sets) > 6:
            base_wardrobe.remove_outfit(get_random_from_list(base_wardrobe.overwear_sets))

        person.wardrobe = base_wardrobe
        return

label activate_generic_personality(stack):
    call create_unique_character_list from _call_create_unique_character_list_activate

    python:
        # add one bimbo to the game (on start of game)
        the_person = create_random_person(age=renpy.random.randint(25, 35), tits="DD", body_type = "standard_body", face_style = "Face_4", skin = "tan",
            hair_colour = "platinum blonde", hair_style = messy_hair, eyes = "blue", personality = bimbo_personality)
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
