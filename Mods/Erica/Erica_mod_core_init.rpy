init 5 python:
    add_label_hijack("normal_start", "activate_erica_mod_core")
    add_label_hijack("after_load", "update_erica_mod_core")


label activate_erica_mod_core(stack):
    python:
        erica_mod_initialization()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_erica_mod_core(stack):
    python:

        execute_hijack_call(stack)
    return
