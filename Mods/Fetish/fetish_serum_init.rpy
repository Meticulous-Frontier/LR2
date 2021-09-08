init 5 python:
    add_label_hijack("normal_start", "activate_fetish_serum_mod_core")
    add_label_hijack("normal_start", "update_fetish_serum_mod_core")

    def fetish_serum_mod_initialization():
        fetish_serum_quest_intro = Action("Nanobot Discovery", fetish_serum_quest_intro_requirement, "fetish_serum_quest_intro_label")
        mc.business.mandatory_crises_list.append(fetish_serum_quest_intro)
        return


label activate_fetish_serum_mod_core(stack):
    python:
        fetish_serum_mod_initialization()
        head_researcher.add_action(fetish_serum_discuss)
        mother_role.add_action(fetish_mom_kitchen)
        breeder_role = breeding_fetish_role
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_fetish_serum_mod_core(stack):
    python:
        head_researcher.add_action(fetish_serum_discuss)
        mother_role.add_action(fetish_mom_kitchen)
        breeder_role = breeding_fetish_role
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return
