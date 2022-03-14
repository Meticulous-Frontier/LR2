init 10 python:
    add_label_hijack("normal_start", "update_base_serums")
    add_label_hijack("after_load", "update_base_serums")

    def massive_pregnancy_accelerator_on_turn_enhanced(the_person, the_serum, add_to_log):
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

    def pregnancy_accelerator_on_day_enhanced(the_person, the_serum, add_to_log):
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

    def pregnancy_decelerator_on_day_enhanced(the_person, the_serum, add_to_log):
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

    def self_generating_serum_on_remove(the_person, the_serum, add_to_log):
        generated_serum = copy.copy(the_serum)
        generated_serum.duration -= 1
        generated_serum.duration_counter = 0

        if generated_serum.duration > 1: # when duration is one, the serum fizzles out
            the_person.give_serum(generated_serum, add_to_log = False)
        return


    def fix_base_game_serums(): # fix existing save games
        mpa = next((x for x in list_of_traits if x == massive_pregnancy_accelerator), None)
        if mpa:
            mpa.on_turn = massive_pregnancy_accelerator_on_turn_enhanced
        pa = next((x for x in list_of_traits if x == pregnancy_accelerator_trait), None)
        if pa:
            pa.on_day = pregnancy_accelerator_on_day_enhanced
        pd = next((x for x in list_of_traits if x == pregnancy_decelerator_trait), None)
        if pd:
            pd.on_day = pregnancy_decelerator_on_day_enhanced

        sgs = next((x for x in list_of_traits if x == self_generating_serum), None)
        if sgs:
            sgs.duration = 3
            sgs.positive_slug = "+3 Turn Duration, Long Lasting Duration"
            sgs.negative_slug = ""
            sgs.desc = "Inserts instructions for the creation of this serum into the subject's cells, allowing them to create a copy of the serum in the body, each copy will decrease its duration by 1, until it fades away."
            sgs.on_remove = self_generating_serum_on_remove
        return


label update_base_serums(stack):
    $ fix_base_game_serums()
    $ execute_hijack_call(stack)
    return
