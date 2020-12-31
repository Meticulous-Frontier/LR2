init 5 python:
    add_label_hijack("normal_start", "activate_fetish_serum_mod_core")
    add_label_hijack("normal_start", "update_fetish_serum_mod_core")

    def fetish_serum_mod_initialization():
        mc.business.mandatory_crises_list.append(fetish_serum_quest_intro)


        return


label activate_fetish_serum_mod_core(stack):
    python:
        fetish_serum_mod_initialization()
        head_researcher.add_action(fetish_serum_discuss)
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_fetish_serum_mod_core(stack):
    python:
        head_researcher.add_action(fetish_serum_discuss)
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return
