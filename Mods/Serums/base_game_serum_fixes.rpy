init 10 python:
    add_label_hijack("after_load", "update_base_serums")

    def massive_pregnancy_accelerator_on_turn(the_person, the_serum, add_to_log):
        if not the_person.has_role(pregnant_role):
            return

        if the_person.event_triggers_dict.get("preg_announce_day", day) -1 > day:
            the_person.event_triggers_dict["preg_announce_day"] = the_person.event_triggers_dict.get("preg_announce_day", day) - 1
        if the_person.event_triggers_dict.get("preg_tits_date", day) - 1 > day:
            if the_person.event_triggers_dict.get("preg_tits_date", day) -1 > the_person.event_triggers_dict.get("preg_announce_day", 9999):
                the_person.event_triggers_dict["preg_tits_date"] = the_person.event_triggers_dict.get("preg_tits_date", day) - 1
        if the_person.event_triggers_dict.get("preg_transform_day", day) - 1 > day:
            if the_person.event_triggers_dict.get("preg_transform_day", day)-1 > the_person.event_triggers_dict.get("preg_tits_date", 9999):
                the_person.event_triggers_dict["preg_transform_day"] = the_person.event_triggers_dict.get("preg_transform_day", day) - 1
        if the_person.event_triggers_dict.get("preg_finish_announce_day", day) - 1 > day:
            if the_person.event_triggers_dict.get("preg_finish_announce_day", day) -1 > the_person.event_triggers_dict.get("preg_transform_day", 9999):
                the_person.event_triggers_dict["preg_finish_announce_day"] = the_person.event_triggers_dict.get("preg_finish_announce_day", day) - 1
        return

    def pregnancy_accelerator_on_day(the_person, the_serum, add_to_log):
        if not the_person.has_role(pregnant_role):
            return

        if the_person.event_triggers_dict.get("preg_announce_day", day) -1 > day:
            the_person.event_triggers_dict["preg_announce_day"] = the_person.event_triggers_dict.get("preg_announce_day", day) - 1
        if the_person.event_triggers_dict.get("preg_tits_date", day) - 1 > day:
            if the_person.event_triggers_dict.get("preg_tits_date", day) -1 > the_person.event_triggers_dict.get("preg_announce_day", 9999):
                the_person.event_triggers_dict["preg_tits_date"] = the_person.event_triggers_dict.get("preg_tits_date", day) - 1
        if the_person.event_triggers_dict.get("preg_transform_day", day) - 1 > day:
            if the_person.event_triggers_dict.get("preg_transform_day", day)-1 > the_person.event_triggers_dict.get("preg_tits_date", 9999):
                the_person.event_triggers_dict["preg_transform_day"] = the_person.event_triggers_dict.get("preg_transform_day", day) - 1
        if the_person.event_triggers_dict.get("preg_finish_announce_day", day) - 1 > day:
            if the_person.event_triggers_dict.get("preg_finish_announce_day", day) -1 > the_person.event_triggers_dict.get("preg_transform_day", 9999):
                the_person.event_triggers_dict["preg_finish_announce_day"] = the_person.event_triggers_dict.get("preg_finish_announce_day", day) - 1
        return

    def pregnancy_decelerator_on_day(the_person, the_serum, add_to_log):
        if not the_person.has_role(pregnant_role):
            return

        if the_person.event_triggers_dict.get("preg_announce_day", day) > day:
            the_person.event_triggers_dict["preg_announce_day"] = the_person.event_triggers_dict.get("preg_announce_day", day) + 1
        if the_person.event_triggers_dict.get("preg_tits_date", day) > day:
            the_person.event_triggers_dict["preg_tits_date"] = the_person.event_triggers_dict.get("preg_tits_date", day) + 1
        if the_person.event_triggers_dict.get("preg_transform_day", day) > day:
            the_person.event_triggers_dict["preg_transform_day"] = the_person.event_triggers_dict.get("preg_transform_day", day) + 1
        if the_person.event_triggers_dict.get("preg_finish_announce_day", day) > day:
            the_person.event_triggers_dict["preg_finish_announce_day"] = the_person.event_triggers_dict.get("preg_finish_announce_day", day) + 1
        return

    def fix_base_game_serums(): # fix existing save games
        mpa = next((x for x in list_of_traits if x == massive_pregnancy_accelerator), None)
        if mpa:
            mpa.on_turn = massive_pregnancy_accelerator_on_turn
        pa = next((x for x in list_of_traits if x == pregnancy_accelerator_trait), None)
        if pa:
            pa.on_day = pregnancy_accelerator_on_day
        pd = next((x for x in list_of_traits if x == pregnancy_decelerator_trait), None)
        if pd:
            pd.on_day = pregnancy_decelerator_on_day
        return


label update_base_serums(stack):
    $ fix_base_game_serums()
    $ execute_hijack_call(stack)
    return
