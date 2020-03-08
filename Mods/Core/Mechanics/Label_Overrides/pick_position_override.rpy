init 2 python:
    config.label_overrides["pick_position"] = "pick_position_enhanced"

    def build_grouped_sex_position_menu(the_person, allow_none = True, ignore_taboo = False):
        foreplay_positions = []
        oral_positions = []
        vaginal_positions = []
        anal_positions = []

        for position in sorted(list_of_positions, key = lambda x: x.name):
            willingness = position.build_position_willingness_string(the_person, ignore_taboo = ignore_taboo).replace("{size=22}", "{size=12}")
            if position.skill_tag == "Foreplay":
                foreplay_positions.append([willingness, position])
            if position.skill_tag == "Oral":
                oral_positions.append([willingness, position])
            if position.skill_tag == "Vaginal":
                vaginal_positions.append([willingness, position])
            if position.skill_tag == "Anal":
                anal_positions.append([willingness, position])
        
        if allow_none:
            foreplay_positions.append(["Nothing", "None"])

        foreplay_positions.insert(0, "Pick Foreplay")
        oral_positions.insert(0, "Pick Oral")
        vaginal_positions.insert(0, "Pick Vaginal")
        anal_positions.insert(0, "Pick Anal")
        return [foreplay_positions, oral_positions, vaginal_positions, anal_positions]

label pick_position_enhanced(the_person, allow_none = True, ignore_taboo = False):
    if "build_menu_items" in globals():
        call screen main_choice_display(build_menu_items(build_grouped_sex_position_menu(the_person, allow_none = allow_none, ignore_taboo = ignore_taboo)))
    else:
        call screen main_choice_display(build build_grouped_sex_position_menu(the_person, allow_none = allow_none, ignore_taboo = ignore_taboo))
    $ position_choice = _return
    return None if position_choice == "None" else position_choice
