init 5 python:
    add_label_hijack("normal_start", "activate_perk_mod_core")
    add_label_hijack("after_load", "update_perk_mod_core")

    Perk_Tutorial_Crisis = Action("Perk Tutorial",Perk_Tutorial_Crisis_requirement,"Perk_Tutorial_Crisis_label")


    def Perk_mod_initialization():
        global perk_system
        perk_system = Perks()
        mc.business.event_triggers_dict["perk_tutorial"] = 1
        mc.business.mandatory_crises_list.append(Perk_Tutorial_Crisis)
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
    if not perk_system.has_ability_perk("Time of Need"):
        if Perk_Tutorial_Crisis not in mc.business.mandatory_crises_list:
            $ mc.business.mandatory_crises_list.append(Perk_Tutorial_Crisis) 
    return
