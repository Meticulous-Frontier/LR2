init 10 python:  # load quest tracker last on stack (higher init number is later on stack)
    add_label_hijack("normal_start", "activate_side_character_mod_core")
    add_label_hijack("after_load", "update_side_character_mod_core")

    def side_character_init():
        base_unavail_list = []
        for person in unique_character_list:
            base_unavail_list.append(person.identifier)
        mc.business.event_triggers_dict["side_character_unavail_list"] = base_unavail_list
        return

    def side_character_set_unavail(the_person):
        mc.business.event_triggers_dict["side_character_unavail_list"].append(the_person.identifier)
        return

    def side_character_is_unavail(the_person):
        return the_person.identifier in mc.business.event_triggers_dict.get("side_character_unavail_list", [])


label activate_side_character_mod_core(stack):
    python:
        side_character_init()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_side_character_mod_core(stack):
    python:
        if mc.business.event_triggers_dict.get("side_character_unavail_list", None) == None:
            side_character_init()

        execute_hijack_call(stack)
    return
