init 5 python:
    add_label_hijack("normal_start", "activate_ashley_mod_core")
    add_label_hijack("after_load", "update_ashley_mod_core")


label activate_ashley_mod_core(stack):
    python:
        ashley_mod_initialization()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_ashley_mod_core(stack):
    python:
        if "ashley" not in globals():
            ashley_mod_initialization()
        else:
            if not ashley.event_triggers_dict.get("story_dict", False):
                ashley.event_triggers_dict["story_dict"] = True
                ashley.love_messages = ["This menu may be broken.", "", "", "", ""]
                ashley.lust_messages = ["This menu may be broken.", "", "", "", ""]
                ashley.obedience_messages = ["This menu may be broken.", "", "", "", ""]
                ashley.other_messages = ["This menu may be broken.", "", "", "", ""]
                ashley.teamup_messages = ["This menu may be broken.", ""]
                ashley.love_step = 0
                ashley.obedience_step = 0
                ashley.lust_step = 0
        global list_of_upgraded_mc_serums
        for trait in list_of_mc_traits:
            trait.on_load()
        mc_serum_load_selected_list()
        execute_hijack_call(stack)
    return
