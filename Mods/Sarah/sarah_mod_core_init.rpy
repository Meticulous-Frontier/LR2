init 5 python:
    add_label_hijack("normal_start", "activate_sarah_mod_core")
    add_label_hijack("after_load", "update_sarah_mod_core")


label activate_sarah_mod_core(stack):
    python:
        Sarah_mod_initialization() 
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_sarah_mod_core(stack):
    python:
        # assign correct weight to relative recruitment status
        if get_HR_director_tag("business_HR_relative_recruitment", 0) == 2:
            update_hire_daughter_crisis(10)
        if get_HR_director_tag("business_HR_relative_recruitment", 0) == 1:
            update_hire_daughter_crisis(2)
        execute_hijack_call(stack)
    return
