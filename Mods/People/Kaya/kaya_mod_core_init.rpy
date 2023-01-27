init 5 python:
    add_label_hijack("normal_start", "activate_kaya_mod_core")
    add_label_hijack("after_load", "update_kaya_mod_core")


label activate_kaya_mod_core(stack):
    python:

        kaya_mod_initialization()
        erica_kaya_teamup_init()
        if erica_kaya_teamup not in list_of_progression_scenes:
            list_of_progression_scenes.append(erica_kaya_teamup)
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_kaya_mod_core(stack):
    python:
        if "kaya" not in globals():
            kaya_mod_initialization()
        elif not kaya.has_role(generic_student_role):
            kaya.add_role(generic_student_role)
        if "erica_kaya_teamup" not in globals():
            erica_kaya_teamup_init()
        if not isinstance(erica_kaya_teamup, Progression_Scene):
            erica_kaya_teamup_init()
        erica_kaya_teamup.compile_scenes(erica_kaya_teamup)
        if erica_kaya_teamup not in list_of_progression_scenes:
            list_of_progression_scenes.append(erica_kaya_teamup)
        execute_hijack_call(stack)
    return
