#Use this file to initialize all the teamup files and reset their tiers each time the game loads, etc.
init 5 python:
    add_label_hijack("normal_start", "activate_teamup_mod_core")
    add_label_hijack("after_load", "update_teamup_mod_core")

    def teamup_mod_initialization():
        kaya_erica_teamup_init()
        return

label activate_teamup_mod_core(stack):
    python:
        teamup_mod_initialization()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_teamup_mod_core(stack):
    python:
        if "kaya_erica_teamup" not in globals():
            teamup_mod_initialization()
        else:
            kaya_erica_teamup.compile_scenes(kaya_erica_teamup)
        execute_hijack_call(stack)
    return
