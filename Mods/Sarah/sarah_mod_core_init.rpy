init 5 python:
    add_label_hijack("normal_start", "activate_sarah_mod_core")


label activate_sarah_mod_core(stack):
    call HR_director_mod_init from _call_initialize_sarah_1
    # continue on the hijack stack if needed
    $ execute_hijack_call(stack)
    return
