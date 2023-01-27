init 5 python:
    add_label_hijack("normal_start", "activate_ashley_mod_core")
    add_label_hijack("after_load", "update_ashley_mod_core")


label activate_ashley_mod_core(stack):
    python:
        ashley_mod_initialization()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_ashley_mod_core(stack):
    python:
        for trait in list_of_mc_traits:
            trait.on_load()
        mc_serum_load_selected_list()
        execute_hijack_call(stack)
    return
