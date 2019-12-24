init 5 python:
    add_label_hijack("normal_start", "activate_sarah_mod_core")


label activate_sarah_mod_core(stack):
    $ Sarah_mod_initialization() 
    # continue on the hijack stack if needed
    $ execute_hijack_call(stack)
    return
