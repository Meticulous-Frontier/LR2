# Genric Personality Hook by Tristimdorion
# overrides the default make person function in the game
# so we can add / change person characteristics based on custom personalities.
# if you need person customizations, extend the hijacked labels

init 5 python:
    add_label_hijack("normal_start", "activate_generic_personality")
    add_label_hijack("after_load", "update_generic_personality")

init 1 python:
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

        return return_character

    # change the random person based other characteristics of personality
    def update_random_person(person):
        update_cougar_personality(person)
        # A person could have dialog even if we don't know her
        if person.possessive_title is None:
            person.set_possessive_title("The unknown woman")
        return

    # bind the generic people role actions to the people in the game
    def update_person_roles(person):
        # Adds mandatory roles to person (use name to find since object compare does not work (not implemented in Role class))
        if find_in_list(lambda x: x.role_name == generic_people_role.role_name, person.special_role) is None:
            person.special_role.append(generic_people_role)
        return

    def update_cougar_personality(person):
        # change personality to cougar if we meet age requirement
        cougar_mod = find_in_list(lambda x: x.effect == cougar_personality_action.effect, ActionMod._instances)

        if not cougar_mod is None and cougar_mod.enabled:
            if person not in list_of_unique_characters + [mom, lily, aunt, cousin, stephanie] and person.age > 45:
                if not person.personality is cougar_personality:
                    person.original_personality = person.personality
                    person.personality = cougar_personality
                    # mc.log_event((person.title or person.name) + "  A:" + str(person.age) + ": " + person.personality.personality_type_prefix, "float_text_grey")
        else:
            if person.personality is cougar_personality:
                if person not in list_of_unique_characters + [mom, lily, aunt, cousin, stephanie]:
                    if not (person.original_personality is None or person.original_personality.personality_type_prefix == "cougar"):
                         person.personality = person.original_personality
                    else:
                        new_personality = get_random_from_list(list_of_personalities)
                        person.personality = new_personality
                    # mc.log_event((person.title or person.name) + " D:" + str(person.age) + ": " + person.personality.personality_type_prefix, "float_text_grey")
        return


label activate_generic_personality(stack):
    python:
        for person in all_people_in_the_game():
            update_random_person(person)
            update_person_roles(person)

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_generic_personality(stack):
    python:
        # fix for old save games:
        if not find_in_list(lambda x: x.personality_type_prefix == cougar_personality.personality_type_prefix, list_of_personalities) is None:
            list_of_personalities.remove(cougar_personality)

        for person in all_people_in_the_game():
            update_random_person(person)
            update_person_roles(person)

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return
