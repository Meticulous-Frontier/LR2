## Coffee Break Crisis Mod by Tristimdorion
init -1 python:
    coffee_break_weight = 5

init 2 python:
    def coffee_break_requirement():
        if time_of_day > 0 and time_of_day < 4: # only during morning afternoon or evening
            if not mc.business.is_weekend() and mc.is_at_work():
                return __builtin__.len([x for x in mc.business.get_employee_list() if x.effective_sluttiness() > 20]) >= 3
        return False

    coffee_break_action = ActionMod("Coffee Break", coffee_break_requirement, "coffee_break_action_label",
        menu_tooltip = "A group of employees is having a coffee break.", category = "Business", is_crisis = True, crisis_weight = coffee_break_weight)

label coffee_break_action_label:
    $ (person_one, person_two, person_three) = get_random_employees(3, slut_required = 20)
    if person_one is None:
        return

    $ mc.change_location(lobby)
    $ mc.location.show_background()
    "As you are walking around the office, you see several employees at the coffee machine. They haven't noticed you, but you can hear what they are saying."
    call coffee_break_chit_chat_label(person_one, person_two, person_three) from _call_coffee_break_chit_chat_label_1
    python:     # Release variables
        del person_one
        del person_two
        del person_three
        mc.location.show_background()
    return

label coffee_break_chit_chat_label(person_one, person_two, person_three):
    python:
        scene_manager = Scene()
        scene_manager.add_actor(person_one, emotion="default", display_transform = character_left_flipped)
        scene_manager.add_actor(person_two, emotion="default", display_transform = character_center_flipped)
        scene_manager.add_actor(person_three, emotion="default")

    if person_one.sluttiness > 70 and person_three.sluttiness > 70:
        person_one "Last night, I was dreaming of sucking [person_one.mc_title]'s big cock."
        person_two "I would mind a giving that meat stick some affection myself."
        person_three "That would be perfect, when you two are done, I can tame and ride that monster."
    elif person_one.sluttiness > 40 and person_three.sluttiness > 40:
        person_one "Don't you think [person_one.mc_title] has a nice bulge in his pants."
        person_two "I bet that he is hung like a horse."
        person_three "I've always wanted to take some horse riding lessons."
    else:
        person_one "Don't you think [person_one.mc_title] is really good looking."
        person_two "I like how his butt flexes in his pants."
        person_three "To be honest, I much more prefer the other side."

    python:
        scene_manager.update_actor(person_one, emotion="happy")
        scene_manager.update_actor(person_two, emotion="happy")
        scene_manager.update_actor(person_three, emotion="happy")

    "The girls start laughing at [person_three.title]'s last remark."

    person_one "That was very funny [person_three.name], but I have to get back to work."

    $ scene_manager.update_actor(person_one, position = "walking_away")

    "[person_one.title] walks off to her workstation."
    # remove person 1 from scene
    $ scene_manager.remove_actor(person_one)

    if person_two.sluttiness > 40 and person_three.sluttiness > 40:
        person_two "Oh, she's such a stickler for rules."
        person_three "Why don't we go break some rules together in the supply closet?"

        if person_two.sluttiness > 60 and person_three.sluttiness > 60:
            $ scene_manager.update_actor(person_two, position = "walking_away")
            $ scene_manager.update_actor(person_three, position = "walking_away")

            "You decide to follow them at a discrete distance."
            "As soon as they enter the supply closet you peek through the side window where [person_two.possessive_title] starts kissing [person_three.possessive_title]."

            $ scene_manager.update_actor(person_two, position = "kissing")
            $ scene_manager.update_actor(person_three, position = "kissing")
            $ mc.change_locked_clarity(20)

            "What's your next move?"
            menu:
                "Walk away":
                    python:
                        mc.location.show_background()
                        scene_manager.clear_scene()
                    return

                "Join them\n{color=#ff0000}{size=18}Requires: Both girls open to threesomes{/color}{/size} (disabled)" if not if willing_to_threesome(person_two, person_three):
                    pass

                "Join them" if willing_to_threesome(person_two, person_three):
                    mc.name "Hello girls... mind if I join your little party?"
                    $ scene_manager.update_actor(person_two, position = "stand3")
                    $ scene_manager.update_actor(person_three, position = "stand4")
                    person_three "Oh my, hello [person_three.mc_title], we didn't see you there."
                    "You tell the girls to take off their clothes."

                    python:
                        scene_manager.strip_actor_outfit_to_max_sluttiness(person_two, temp_sluttiness_boost = 50)
                        scene_manager.strip_actor_outfit_to_max_sluttiness(person_three, temp_sluttiness_boost = 50)

                    call start_threesome(person_two, person_three) from _call_coffee_break_threesome_test_3

                    person_two "Wow...this was...really good actually... You can join us anytime you want boss..."
                    $ scene_manager.update_actor(person_two, position = "walking_away", display_transform = character_center_flipped)
                    $ scene_manager.update_actor(person_three, position = "walking_away", display_transform = character_right)
                    "They pick up their clothes and leave you feeling very proud of yourself."

                    # cleanup scene
                    $ scene_manager.clear_scene()
                    $ person_two.increase_opinion_score("threesomes")
                    $ person_two.reset_arousal()
                    $ person_two.apply_planned_outfit()

                    $ person_three.increase_opinion_score("threesomes")
                    $ person_three.reset_arousal()
                    $ person_three.apply_planned_outfit()

                    $ town_relationships.improve_relationship(person_two, person_three)

                    "Amazing you just fucked two of your employees, wondering if other girls in your company might also be up for this."
        else:
            person_two "Another time, [person_three.name], let's get back to work."

            $ scene_manager.update_actor(person_two, position = "walking_away")
            $ scene_manager.update_actor(person_three, position = "walking_away")

            $ town_relationships.improve_relationship(person_two, person_three)

            "[person_two.title] grabs [person_three.title] by her arm and they walk down the corridor."
    else:
        person_two "Yeah, we better get going too."
        $ scene_manager.update_actor(person_two, position = "walking_away")
        $ scene_manager.update_actor(person_three, position = "walking_away")

        $ town_relationships.improve_relationship(person_two, person_three)

        "You watch [person_two.title] and [person_three.title] walk away together."

    # clear scene
    $ mc.location.show_background()
    $ scene_manager.clear_scene()
    return
