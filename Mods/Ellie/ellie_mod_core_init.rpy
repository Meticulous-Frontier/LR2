init 5 python:
    add_label_hijack("normal_start", "activate_ellie_mod_core")
    add_label_hijack("after_load", "update_ellie_mod_core")


label activate_ellie_mod_core(stack):
    python:
        ellie_mod_initialization()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_ellie_mod_core(stack):
    python:
        if "ellie" not in globals():
            ellie_mod_initialization()
        execute_hijack_call(stack)
    return
