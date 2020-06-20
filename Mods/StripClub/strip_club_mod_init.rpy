init 5 python:
    add_label_hijack("normal_start", "activate_strip_club_mod_core")
    add_label_hijack("after_load", "update_strip_club_mod_core")


label activate_strip_club_mod_core(stack):
    python:
        init_strip_club_mod()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_strip_club_mod_core(stack):
    python:
        # add strip club mod to existing save game
        if mc.business.event_triggers_dict.get("foreclosed_stage", -99) == -99:
            init_strip_club_mod()

        # no extra code yet
        execute_hijack_call(stack)
    return
