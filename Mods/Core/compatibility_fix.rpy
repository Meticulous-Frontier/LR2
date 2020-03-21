#init -100 python:
    # Fix compatibility of save games.

init 5 python: # add to stack later then other mods
    add_label_hijack("normal_start", "activate_compatibility_fix")
    add_label_hijack("after_load", "update_compatibility_fix")

init -1 python:
    # override some of the default settings to improve performance
    config.image_cache_size = 12
    config.image_cache_size_mb = 1024


label activate_compatibility_fix(stack):
    # make sure we store the crisis tracker in the save game
    $ crisis_tracker_dict = {}

    $ execute_hijack_call(stack)
    return

label update_compatibility_fix(stack):
    if not "crisis_tracker_dict" in globals():
        $ crisis_tracker_dict = {}

    $ execute_hijack_call(stack)
    return


