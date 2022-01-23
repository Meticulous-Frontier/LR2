init 5 python:
    add_label_hijack("normal_start", "activate_vanilla_progress_screens_mod_core")
    add_label_hijack("after_load", "activate_vanilla_progress_screens_mod_core")


label activate_vanilla_progress_screens_mod_core(stack):
    python:
        lily_progress_screen_activation()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return
