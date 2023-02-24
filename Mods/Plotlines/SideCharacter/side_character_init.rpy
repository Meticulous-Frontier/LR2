init 10 python:  # load quest tracker last on stack (higher init number is later on stack)
    add_label_hijack("normal_start", "activate_side_character_mod_core")
    add_label_hijack("after_load", "update_side_character_mod_core")

    def side_character_init():
        base_unavail_list = []
        for person in unique_character_list:
            base_unavail_list.append(person.identifier)
        mc.business.event_triggers_dict["side_character_unavail_list"] = base_unavail_list
        return

    def side_character_set_unavail(person):
        mc.business.event_triggers_dict["side_character_unavail_list"].append(person.identifier)
        return

    def side_character_is_unavail(person):
        return person.identifier in mc.business.event_triggers_dict.get("side_character_unavail_list", [])

    def side_character_unavail_list():
        return [x for x in known_people_in_the_game() if x.identifier in mc.business.event_triggers_dict.get("side_character_unavail_list", [])]


label activate_side_character_mod_core(stack):
    python:
        side_character_init()
        # continue on the hijack stack if needed
        mc.business.add_mandatory_crisis(cuckold_employee_init)
        mc.business.add_mandatory_crisis(chemist_daughter_init)
        execute_hijack_call(stack)
    return

label update_side_character_mod_core(stack):
    python:
        if mc.business.event_triggers_dict.get("side_character_unavail_list", None) is None:
            side_character_init()
        if cuckold_employee_get() is None:
            mc.business.add_mandatory_crisis(cuckold_employee_init)
        if chemist_daughter_employee_get() is None:
            mc.business.add_mandatory_crisis(chemist_daughter_init)
        execute_hijack_call(stack)
    return
