init 5 python:
    add_label_hijack("normal_start", "activate_camilla_mod_core")
    add_label_hijack("after_load", "update_camilla_mod_core")


label activate_camilla_mod_core(stack):
    python:
        camilla_mod_initialization()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_camilla_mod_core(stack):
    python:
        if "camilla" not in globals():
            camilla_mod_initialization()
        execute_hijack_call(stack)
    return
