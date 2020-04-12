
init 2 python:
    def employee_find_out_home_location_requirement(the_person):
        if the_person.obedience > 120 and the_person.effective_sluttiness() > 30:
            return not the_person.home in mc.known_home_locations
        return False

    employee_find_out_home_location_action = Action("Have a personal chat.", employee_find_out_home_location_requirement, "employee_find_out_home_location_label",
        menu_tooltip = "Have a chat with an employee and find our more about her, including her home address.")


init 5 python:
    add_label_hijack("normal_start", "activate_employee_role_enhancement")
    add_label_hijack("after_load", "activate_employee_role_enhancement")


label employee_find_out_home_location_label(the_person):
    $ the_person.draw_person(position = "sitting")
    "You walk up to [the_person.possessive_title], who is sitting at her work station."

    mc.name "Hey [the_person.title], how long have you been working for me?"
    $ ran_num = (day - the_person.event_triggers_dict.get("employed_since", 0)) // 7
    if ran_num == 0:
        the_person.char "I just started working here, is there something wrong?"
    elif ran_num == 1:
        the_person.char "Its about a week now, why do you ask?"
    else:
        the_person.char "It must be about [ran_num] weeks now, why do you ask?"
    
    mc.name "I don't think we ever had a personal talk, just to get to know each other."
    the_person.char "Oh, that's very nice of you, I would love to have a chat."
    $ the_person.change_happiness(5)

    mc.name "So tell me a little about yourself, [the_person.title]."

    $ ran_num = renpy.random.randint(2, (the_person.age - 18) * 12)
    $ opinion = "months"
    if ran_num > 23:
        $ ran_num = ran_num // 12
        $ opinion = "years"

    if the_person.relationship == "Single":
        the_person.char "I'm still single and living at home with my parents."
    elif the_person.relationship == "Girlfriend":
        the_person.char "My boyfriend is [the_person.SO_name] and we have been going out for about [ran_num] [opinion]."
    elif the_person.relationship == "Fiancée":
        the_person.char "I'm engaged to my sweetheart [the_person.SO_name], we have been together for about [ran_num] [opinion]."
    elif the_person.relationship == "Married":
        the_person.char "I'm married and my husband's name is [the_person.SO_name], we have been married for about [ran_num] [opinion]."

    if the_person.kids == 0:
        the_person.char "I've got no children and to be honest I don't plan on getting any soon."
    elif the_person.kids == 1:
        if the_person.age < 35:
            the_person.char "I've an adorable little boy, a little cheeky, just like his dad."
        else:
            the_person.char "I've a wonderful daughter and I'm very proud of her, she has been a joy in my life."
    else:
        the_person.char "I have [the_person.kids] children and I love them all very much."

    mc.name "That sounds wonderful, [the_person.title], and were do you live?"

    if the_person.relationship == "Single" and the_person.kids == 0:
        $ ran_num = renpy.random.randint(4, 8)
        $ opinion = get_random_from_list(["Peach Trees", "Nakatomi Plaza", "La Fortuna", "Villa Bonita", "St. Germaine"])
        the_person.char "I have a nice little place in the [opinion] apartment block on the [ran_num]th floor."
    else:
        $ opinion = get_random_from_list(["Lyon Estates just south of Hill Valley", "Bristol Avenue in Brentwood", "Carnarvon Park in Newbury", "Quimby Street in Cullen"])
        the_person.char "We have a beautiful home at the [opinion]."

    "You just learned her home address and can visit her anytime you want."
    if not the_person.home in mc.known_home_locations:
        $ mc.known_home_locations.append(the_person.home) #You know where she lives and can visit her.

    mc.name "Well, well, that is indeed a great place to live. Thank you for the talk, i'm sorry to cut this short, but I do have to get back to work."
    the_person.char "Any time [the_person.mc_title], I really enjoyed our little parley."

    $ renpy.scene("Active")
    return

label activate_employee_role_enhancement(stack):
    python:
        if not employee_find_out_home_location_action in employee_role.actions:
            employee_role.actions.append(employee_find_out_home_location_action)

        execute_hijack_call(stack)
    return