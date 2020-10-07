init 5 python:
    def strip_club_give_daily_serum():
        for (person, place) in people_to_process:
            if person.is_employee():
                continue

            if person.has_role(stripper_role) and getattr(mc.business, "strippers_serum", None):
                strip_club_give_daily_serum_to_person(person, mc.business.strippers_serum)
            if person.has_role(waitress_role) and getattr(mc.business, "waitresses_serum", None):
                strip_club_give_daily_serum_to_person(person, mc.business.strippers_serum)
            if person.has_role([manager_role, mistress_role]) and getattr(mc.business, "manager_serum", None):
                strip_club_give_daily_serum_to_person(person, mc.business.manager_serum)
            if person.has_role(bdsm_performer_role) and getattr(mc.business, "bdsm_performers_serum", None):
                strip_club_give_daily_serum_to_person(person, mc.business.bdsm_performers_serum)
        return

    def strip_club_give_daily_serum_to_person(person, group_serum):
        if not mc.business.inventory.get_serum_count(group_serum) > 0:
            return

        mc.business.inventory.change_serum(group_serum, -1)
        person.give_serum(copy.copy(group_serum), add_to_log = False)
        return


    add_label_hijack("advance_time_daily_serum_dosage_label", "advance_time_strip_club_daily_serum_dosage_label")

label advance_time_strip_club_daily_serum_dosage_label(stack):
    python:
        strip_club_give_daily_serum()
        execute_hijack_call(stack)
    return
