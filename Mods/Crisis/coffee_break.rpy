## Coffee Break Crisis Mod by Tristimdorion
init -1 python:
    coffee_break_weight = 5

init 2 python:
    def coffee_break_requirement():
        if not mc.business.is_weekend():
            if mc.is_at_work():
                if time_of_day > 0 and time_of_day < 4: # only during morning afternoon or evening
                    if len(mc.business.get_requirement_employee_list(slut_required = 20)) >= 3:
                        return True
        return False

    def has_opinion(person, topic):
        return not person.get_opinion_topic(topic) is None

    def update_opinion(person, topic):
        if has_opinion(person, topic):
            person.increase_opinion_score(topic)
        else:
            person.add_opinion(topic, 1, sexy_opinion = True)
        return

    coffee_break_action = ActionMod("Coffee Break", coffee_break_requirement, "coffee_break_action_label",
        menu_tooltip = "A group of employees is having a coffee break.", category = "Business")
    crisis_list.append([coffee_break_action, coffee_break_weight])

label coffee_break_action_label:
    python:
        #Generate list of people with at least a little sluttiness, pick 3 for coffee machine encounters
        list_of_possible_people = mc.business.get_requirement_employee_list(slut_required = 20)
        person_one = get_random_from_list(list_of_possible_people)
        list_of_possible_people.remove(person_one)
        person_two = get_random_from_list(list_of_possible_people)
        list_of_possible_people.remove(person_two)
        person_three = get_random_from_list(list_of_possible_people)

    mc.name "As you are walking around the office, you see several employees at the coffee machine. They haven't noticed you, but you can hear what they are saying."   
    call coffee_break_chit_chat_label(person_one, person_two, person_three) from _call_coffee_break_chit_chat_label_1
    return

label coffee_break_chit_chat_label(person_one, person_two, person_three):
    $ person_one.draw_person(emotion = "default", character_placement = character_left_flipped)
    $ person_two.draw_person(emotion = "default", character_placement = character_center_flipped)
    $ person_three.draw_person(emotion = "default")

    if person_one.sluttiness > 40 and person_three.sluttiness > 40:
        person_one.char "Don't you think [the_person.mc_title] has a nice bulge in his pants."
        person_two.char "I bet the he is hung like a horse."
        person_three.char "I've always wanted to take some horse riding lessons."
    else:
        person_one.char "Don't you think [the_person.mc_title] is really good looking."
        person_two.char "I like how his butt flexes in his pants."
        person_three.char "To be honest, I much more prefer the other side."

    $ person_one.draw_person(emotion = "happy")
    $ person_two.draw_person(emotion = "happy")
    $ person_three.draw_person(emotion = "happy")
    "The girls start laughing at [person_three.title]'s last remark."

    person_one.char "That was very funny [person_three.name], but I have to get back to work."
    $ person_one.draw_person(position = "walking_away")
    "[person_one.title] walks off to her workstation."
    # remove person 1 from scene
    $ person_one.clear_scene()

    if person_two.sluttiness > 40 and person_three.sluttiness > 40:
        person_two.char "Oh, she's such a stickler for rules."
        person_three.char "Why don't we go break some rules together in the supply closet?"

        if person_two.sluttiness > 60 and person_three.sluttiness > 60:
            $ person_two.draw_person(position = "walking_away")
            $ person_three.draw_person(position = "walking_away")

            "You decide to follow them at a discrete distance."
            "As soon as they enter the supply closet you peek through the side window where [person_two.possessive_title] starts kissing [person_three.possessive_title]."

            $ person_two.draw_person(position = "kissing")
            $ person_three.draw_person(position = "kissing")

            "What's your next move?"
            menu:
                "Walk away":
                    $ change_scene_display(mc.location)
                    $ person_two.clear_scene()
                    $ person_three.clear_scene()
                    return
                "Join them":
                    mc.name "Hello girls... mind if I join your little party?"
                    $ person_two.draw_person(position = "stand_3")
                    $ person_three.draw_person(position = "stand_4")
                    person_three.char "Oh my, hello [person_three.mc_title], we didn't see you there."
                    "You tell the girls to take off their clothes." 
                    $ person_two.strip_outfit_to_max_sluttiness(temp_sluttiness_boost = 40, character_placement = character_center_flipped)
                    $ person_three.strip_outfit_to_max_sluttiness(temp_sluttiness_boost = 40)

                    $ person_two.clear_scene()
                    $ person_three.clear_scene()

                    # switch to SB ui
                    hide screen person_info_ui
                    show screen SB_two_person_info_ui(person_two, person_three)                   

                    $ SB_draw_two_person_scene(person_one = person_two, person_two = person_three, one_pos_x = 0.7, one_position = "stand_3", two_position = "stand_4")

                    call SB_threesome_description(person_two, person_three, SB_threesome_sixty_nine, make_floor(), 0, private = True, girl_in_charge = False)
                    $ SB_draw_two_person_scene(person_one = person_two, person_two = person_three, one_pos_x = 0.7)
                    person_two.char "Wow...this was...really good actually... You can join us anytime you want boss..."                   
                    $ SB_draw_two_person_scene(person_one = person_two, person_two = person_three, one_pos_x = 0.7, one_position = "walking_away", two_position = "walking_away")
                    "They pickup their clothes and leave you feeling very proud of yourself."

                    # cleanup scene
                    hide screen SB_two_person_info_ui

                    $ update_opinion(person_two, "threesomes")
                    $ person_two.reset_arousal()
                    $ person_two.review_outfit(show_review_message = False) #Make sure to reset her outfit so she is dressed properly.

                    $ update_opinion(person_three, "threesomes")
                    $ person_three.reset_arousal()
                    $ person_three.review_outfit(show_review_message = False) #Make sure to reset her outfit so she is dressed properly.

                    $ change_scene_display(mc.location)
                    $ renpy.scene("Active")

                    "Amazing you just fucked two of your employees, wondering if other girls in your company might also be up for this."
                    return
        else:
            person_two.char "Another time, [person_three.name], let's get back to work."
            $ person_two.draw_person(position = "walking_away")
            $ person_three.draw_person(position = "walking_away")

            "[person_two.title] grabs [person_three.title] by her arm and they walk down the corridor."
    else:
        person_two.char "Yeah, we better get going too."
        $ person_two.draw_person(position = "walking_away")
        $ person_three.draw_person(position = "walking_away")

        "You watch [person_two.title] and [person_three.title] walk away together."

    # remove person 2 from scene
    $ person_two.clear_scene()
    # remove person 3 from scene
    $ person_three.clear_scene()
    return
