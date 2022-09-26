init 5 python:
    add_label_hijack("normal_start", "activate_erica_mod_core")
    add_label_hijack("after_load", "update_erica_mod_core")

    add_label_hijack("instantiate_jobs", "erica_instantiate_jobs")


label activate_erica_mod_core(stack):
    python:
        erica_mod_initialization()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_erica_mod_core(stack):
    if "erica" not in globals():
        call erica_instantiate_jobs([])
        python:
            erica_mod_initialization()
    # TODO: remove when breaking save compatibility
    elif not erica.has_role(generic_student_role):
        $ erica.add_role(generic_student_role)
    
    $execute_hijack_call(stack)
    return
