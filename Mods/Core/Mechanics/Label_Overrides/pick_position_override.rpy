init 2 python:
    config.label_overrides["pick_position"] = "pick_position_enhanced"

label pick_position_enhanced(the_person, allow_none = True, ignore_taboo = False):

    call screen pick_position_screen(the_person, allow_none = allow_none, ignore_taboo = ignore_taboo)
    if _return == "None":
        $ _return = None
    return _return
