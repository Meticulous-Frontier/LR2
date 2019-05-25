## Coffee Break Crisis Mod by Tristimdorion
init -1 python:
    coffee_break_weight = 8     # slightly higher weight, cause it has more stories than one...

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

    coffee_break_action = ActionMod("Coffee Break Crisis", coffee_break_requirement, "coffee_break_action_label",
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
        story = renpy.random.randint(1, 2)

    mc.name "As you are walking around the office, you see several employees at the coffee machine. They haven't noticed you, but you can hear what they are saying."
    if (story == 1):
        call coffee_break_chit_chat_label(person_one, person_two, person_three) from _call_coffee_break_chit_chat_label_1
    else:
        call coffee_break_food_delivery_label(person_one, person_two, person_three) from _call_coffee_break_food_delivery_label_1

    # TODO: Add more stories that start at the coffee machine

    return

label coffee_break_food_delivery_label(person_one, person_two, person_three):
    $ person_one.draw_person(emotion = "default", character_placement = character_left_flipped)
    $ person_two.draw_person(emotion = "default", character_placement = character_center_flipped)
    $ person_three.draw_person(emotion = "default")

    python:
        loser_index = renpy.random.randint(0, 2)
        if loser_index == 0:
            loser = person_one
            winner_one = person_two
            winner_two = person_three
        elif loser_index == 1:
            loser = person_two
            winner_one = person_one
            winner_two = person_three
        else:
            loser = person_three
            winner_one = person_one
            winner_two = person_two

    winner_one.char "Ok, listen up girls, whoever gets the shortest straw will pickup the food from the delivery guy in the lobby."
    $ winner_two.draw_person(emotion  = "happy")
    "[winner_two.possessive_title] draws a long straw."
    winner_one.char "Right, [loser.name], it's between you and me now, pick one."
    $ winner_one.draw_person(emotion = "happy")
    $ loser.draw_person(emotion = "sad")
    "[loser.possessive_title] draws the short straw."
    winner_two.char "Don't forget [loser.name], you have to take of some clothes before you pickup the food."
    if loser.sluttiness >= 40:
        $ loser.draw_person(emotion = "happy")
        loser.char "Great, let's give this guy a show!"
        $ loser.change_slut_temp(5)

        if loser.sluttiness >= 60:
            $ winner_one.draw_person(position = "walking_away")
            $ winner_two.draw_person(position = "walking_away")
            "As [loser.possessive_title] turns around, she walks right into you."
            loser.char "Hey [mc.name] do you mind helping me out real quick?"
            $ winner_one.clear_scene()
            $ winner_two.clear_scene()

            menu:
                "Help her":
                    loser.char "Awesome! Cum on my face real quick. The delivery guy just pulled into the parking lot."
                    $ loser.draw_person(position = 'blowjob')
                    "[loser.possessive_title] gives you a quick blowjob and you splatter your cum all over her face, she smears it around and into her hair for added effect."
                    $ loser.cum_on_face()
                    $ loser.draw_person(position = 'standing')
                    loser.char "Thanks, these delivery boys love it when I do this."
                "Refuse":
                    loser.char "Aww you're no fun, [loser.mc_title]. If he makes me pay this time it's your fault."

            "You watch as [loser.possessive_title] strips down."
            $ loser.strip_outfit_to_max_sluttiness()
            # TODO: Figure out how to keep the cum on the face, just calling the cum_on_face() method does not work ????
            "She gives you a wink and turns around to pickup the food."
            $ loser.draw_person(position = 'walking_away')

            if loser.sluttiness >= 90 and loser.outfit.vagina_visible():
                "When [loser.possessive_title] reaches the lobby she pulls the sweaty guy into an empty office."
                loser.char "I left my purse at my desk. I can go get it... or maybe I could pay another way."
                $ loser.draw_person(position = 'standing_doggy')
                "[loser.possessive_title] turns around and presents herself, the sweaty guy quickly drops his pants and pushes his cock against her pussy."
                loser.char "Oh, hard already. We must be getting so predictable."
                "The delivery man begins thrusting as hard and fast as he can. He seems to be in a hurry to finish and get back to work."
                loser.char "Ah yes, fill me up. Fuck me you sweaty pig."
                "His face turns bright red as he pushes [loser.possessive_title]'s face into the desk."
                loser.char "Oh yes. I'm cumming!"
                $ loser.change_slut_temp(3)
                $ loser.change_slut_core(3)
                "He finishes leaving her quivering against the desk. As he walks away he says: 'Enjoy your food, slut!'"
                $ loser.cum_on_ass()               
                "She gathers her clothes and takes the food back to her colleagues. "
                $ loser.draw_person(position = "walking_away")
                "While enjoying the view you decide to go back to work."
            else:
                $ loser.draw_person(position = "back_peek")
                "Seems he has seen this before since he doesn't move a muscle when she looks back in your direction."
                $ loser.draw_person(position = "waling_away")
                "While enjoying the view you decide to go back to work."
        else:
            "You watch as [loser.possessive_title] strips down as she walks down to the lobby."
            $ loser.draw_person(position = "walking_away")
            $ loser.strip_outfit_to_max_sluttiness()
            "You decide to go back to work and let the girls sort this out."

    else:
        loser.char "This is not fair [winner_one.name], you wanted me to loose."
        winner_one.char "No I didn't. And you know the rules!"
        $ loser.draw_person(emotion = "angry")
        loser.char "Fine, I'll do it but only my top and if I get it a third time in a row I swear..."
        $ loser.strip_outfit_to_max_sluttiness(exclude_lower = True, temp_sluttiness_increase = 20)
        "[loser.possessive_title] sheepishly walks down the lobby trying to cover her breasts."
        $ loser.draw_person(position = 'walking_away')
        "The other girls stand back and watch, giggling amongst themselves."
        $ loser.change_slut_temp(5)
        $ loser.clear_scene()
        "You walk up to [winner_one.possessive_title] and [winner_two.possessive_title]."
        mc.name "Ok, girls you had your fun, now back to work."
        winner_two.char "Yes [winner_two.mc_title], right away."
        $ winner_one.draw_person(position = "walking_away")
        $ winner_two.draw_person(position = "walking_away")
        $ winner_one.change_happiness(2)
        $ winner_two.change_happiness(2)
        "Although not professional, you can't help but smile and enjoy the situation."

    $ loser.review_outfit(show_review_message = False)  # makes sure she's properly dressed again.
    $ loser.clear_scene()
    $ winner_one.clear_scene()
    $ winner_two.clear_scene()
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
                    $ person_two.strip_outfit_to_max_sluttiness(temp_sluttiness_increase = 40, character_placement = character_center_flipped)
                    $ person_three.strip_outfit_to_max_sluttiness(temp_sluttiness_increase = 40)

                    $ person_two.clear_scene()
                    $ person_three.clear_scene()

                    hide screen person_info_ui
                    show screen SB_two_person_info_ui(person_two, person_three)                   

                    $ SB_draw_two_person_scene(person_one = person_two, person_two = person_three, one_pos_x = 0.7, one_position = "stand_3", two_position = "stand_4")

                    call SB_threesome_description(person_two, person_three, SB_threesome_sixty_nine, make_floor(), 0, private = True, girl_in_charge = False)
                    $ SB_draw_two_person_scene(person_one = person_two, person_two = person_three, one_pos_x = 0.7)
                    person_two.char "Wow...this was...really good actually... You can join us anytime you want boss..."                   
                    $ SB_draw_two_person_scene(person_one = person_two, person_two = person_three, one_pos_x = 0.7, one_position = "walking_away", two_position = "walking_away")
                    "They pickup their clothes and leave you feeling very proud of yourself."

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

            "[person_two.title] grabs [person_three.title] by her arm and they are off."
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
