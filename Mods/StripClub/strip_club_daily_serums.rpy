init 5 python:
    def strip_club_give_daily_serum():
        if hasattr(mc.business, "strippers_serum") and mc.business.strippers_serum:
            strip_club_give_daily_serum_to_group(mc.business.strippers_serum, stripper_role)
        if hasattr(mc.business, "waitresses_serum") and mc.business.waitresses_serum:
            strip_club_give_daily_serum_to_group(mc.business.strippers_serum, waitress_role)
        if hasattr(mc.business, "manager_serum") and mc.business.manager_serum:
            strip_club_give_daily_serum_to_group(mc.business.manager_serum, [manager_role, mistress_role])
        if hasattr(mc.business, "bdsm_performers_serum") and mc.business.bdsm_performers_serum:
            strip_club_give_daily_serum_to_group(mc.business.bdsm_performers_serum, bdsm_performer_role)
        return

    def strip_club_give_daily_serum_to_group(group_serum, role):
        serum_count = mc.business.inventory.get_serum_count(group_serum)
        if not serum_count > 0:
            return

        for (person, place) in people_to_process:
            if person.is_employee() or not person.has_role(role):
                continue
            mc.business.inventory.change_serum(group_serum, -1)
            person.give_serum(copy.copy(group_serum), add_to_log = False)
            serum_count -= 1
            if serum_count == 0:
                break
        return


    add_label_hijack("advance_time_daily_serum_dosage_label", "advance_time_strip_club_daily_serum_dosage_label")

label advance_time_strip_club_daily_serum_dosage_label(stack):
    python:
        strip_club_give_daily_serum()
        execute_hijack_call(stack)

    return
