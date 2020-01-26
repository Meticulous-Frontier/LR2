init 5 python:
    add_label_hijack("normal_start", "activate_perk_mod_core")
    add_label_hijack("after_load", "update_perk_mod_core")

    def Perk_mod_initialization():
        global perk_system
        perk_system = Perks()
        return

label activate_perk_mod_core(stack):
    python:
        Perk_mod_initialization()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_perk_mod_core(stack):
    python:
        try:
            perk_system
        except NameError:
            Perk_mod_initialization()
        execute_hijack_call(stack)
    return
