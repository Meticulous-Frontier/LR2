init 2 python:
    config.label_overrides["pick_position"] = "pick_position_enhanced"

label pick_position_enhanced(the_person, allow_none = True, ignore_taboo = False):

    python:
        foreplay_positions = []
        oral_positions = []
        penetrative_positions = []
        anal_positions = []

        for position in list_of_positions:
            if position.skill_tag == "Foreplay":
                foreplay_positions.append([position.build_position_willingness_string(the_person), position])
            if position.skill_tag == "Oral":
                oral_positions.append([position.build_position_willingness_string(the_person), position])
            if position.skill_tag == "Vaginal" or position.skill_tag == "Anal":
                penetrative_positions.append([position.build_position_willingness_string(the_person), position])
            # if position.skill_tag == "Anal":
            #     anal_positions.append([position.build_position_willingness_string(the_person), position])
        foreplay_positions.append(["Nothing", "None"])

        foreplay_positions.insert(0, "Pick Foreplay")
        oral_positions.insert(0, "Pick Oral")
        penetrative_positions.insert(0, "Pick Penetrative")
        # anal_positions.insert(0, "Pick Anal")

    call screen main_choice_display([foreplay_positions, oral_positions, penetrative_positions]) #anal_positions
    #call screen pick_position_screen(the_person, allow_none = allow_none, ignore_taboo = ignore_taboo)
    if _return == "None":
        $ _return = None
    return _return
