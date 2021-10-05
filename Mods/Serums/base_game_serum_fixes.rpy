init 2 python:
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
