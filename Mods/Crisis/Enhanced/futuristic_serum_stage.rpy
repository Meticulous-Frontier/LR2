init 5 python:
    config.label_overrides["futuristic_serum_stage_2_label"] = "futuristic_serum_stage_2_enhanced_label"

    def show_satisfying_people_information(person):
        my_string = "The following people currently satisfy the requirements: "
        satisfying_list = mc.business.get_requirement_employee_list(slut_required = 50, obedience_required = 130, exclude_list = [person])
        if satisfying_list:
            for person in satisfying_list:
                my_string += person.name + " " + person.last_name + ", "
        else:
            my_string = "There is currently nobody in your company who meets these requirements."
        renpy.say(None, my_string)
        return


label futuristic_serum_stage_2_enhanced_label(the_person):
    if __builtin__.len(mc.business.get_requirement_employee_list(slut_required = 50, obedience_required = 130)) <= 3: # If you don't have enough people who meet the requirements just get an update.
        mc.name "I'm still working on getting your test subjects ready. Could you remind me what you need?"
        the_person "To learn anything useful I need at least three girls who have been seriously affected by our serums. I need them to be obedient and open to some intimate testing procedures."
        "[the_person.title] requires three employees who satisfy the following requirements: Sluttiness 50+ and Obedience 130+"
        $ show_satisfying_people_information(the_person)
        the_person "Noted. I'll get back to you when I have your test subjects ready."
        return

    mc.name "[the_person.title], I have your group of test subjects ready."
    the_person "Excellent, let me know who to call down and I'll begin as soon as possible."
    $ possible_picks = mc.business.get_requirement_employee_list(slut_required = 50, obedience_required = 130, exclude_list = [the_person])
    call screen employee_overview(white_list = possible_picks, person_select = True)
    $ pick_1 = _return
    call screen employee_overview(white_list = possible_picks, black_list = [pick_1], person_select = True)
    $ pick_2 = _return
    call screen employee_overview(white_list = possible_picks, black_list = [pick_1,pick_2], person_select = True)
    $ pick_3 = _return
    "[the_person.title] looks over the files of the employees you suggested and nods approvingly."
    the_person "I think they will do. You're sure you want me to bring in [pick_1.name], [pick_2.name], and [pick_3.name] for testing?"
    menu:
        "Begin the testing":
            pass

        "Reconsider":
            mc.name "On second thought, I don't think I want them involved. I'll think about it and come back."
            the_person "I'll be here."
            return

    mc.name "Yes, you may begin."
    $ the_person.draw_person(emotion = "happy")
    the_person "Excellent!"
    "[the_person.title] gets her phone out and calls all three girls down to the lab. It doesn't take long for them all to assemble."
    the_person "The testing might take some time sir, I'll get started right now and have all my findings recorded. Come by later and we can review any discoveries."
    "[the_person.title] turns to the other girls."

    python:
        scene_manager = Scene()

        scene_manager.add_actor(pick_1, position = "stand4", display_transform = character_center_flipped)
        scene_manager.add_actor(pick_2, position = "stand3", display_transform = character_left_flipped)
        scene_manager.add_actor(pick_3, position = "stand2", display_transform = character_right)

    the_person "Well then, we have some special testing to get through today! Who would like to go first?"
    $ go_first = pick_1
    if pick_2.obedience > go_first.obedience:
        $ go_first = pick_2
    if pick_3.obedience > go_first.obedience:
        $ go_first = pick_3

    $ scene_manager.update_actor(go_first, position = "stand5", emotion = "happy")

    "[go_first.name] raises her hand and [the_person.title] smiles and grabs her clipboard."
    the_person "Very good."

    python:
        if go_first != pick_3:
            scene_manager.remove_actor(pick_3)
        if go_first != pick_1:
            scene_manager.remove_actor(pick_1)
        if go_first != pick_2:
            scene_manager.remove_actor(pick_2)

        scene_manager.add_actor(the_person, position="stand4", emotion="happy", display_transform = scene_manager.get_free_position_tuple()[1])

    the_person "Are you ready [go_first.name]? Come with me, you two can wait here until we're done."

    $ scene_manager.update_actor(go_first, position = "walking_away")
    $ scene_manager.update_actor(the_person, position = "walking_away")

    "[the_person.title] leads [go_first.title] into a side office, and you decide to leave her to her work."
    #TODO: Expand this event for more sexy stuff.

    python:
        mc.business.research_tier = 3
        mc.log_event("Max Research Tier Unlocked", "float_text_grey")
        scene_manager.clear_scene()
        del pick_1
        del pick_2
        del pick_3
        del go_first
        del possible_picks

    call advance_time from _call_advance_time_serum_stage_2_enhanced
    return
