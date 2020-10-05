## Stripclub storyline Mod by Corrado
#  BDSM performers role definition.
#  The role is appended to BDSM performers after they start to work for you.

init 3305 python:
    BDSM_performer_wardrobe = wardrobe_from_xml("BDSM_Wardrobe")

    bdsm_performer_role = Role("BDSM performer", [promote_to_manager_action, strip_club_stripper_fire_action, strip_club_stripper_performance_review_action], hidden = False)

label advance_time_BDSM_performers_daily_serum_dosage_label(stack):
    python:
        if hasattr(mc.business, "bdsm_performers_serum"):
            if mc.business.bdsm_performers_serum:
                serum_count = mc.business.inventory.get_serum_count(mc.business.bdsm_performers_serum)
                if serum_count > 0:
                    for (person,place) in people_to_process:
                        if person.is_employee() or not person.has_role(bdsm_performer_role):
                            continue
                        mc.business.inventory.change_serum(mc.business.bdsm_performers_serum,-1)
                        person.give_serum(copy.copy(mc.business.bdsm_performers_serum), add_to_log = False)
                        serum_count -= 1
                        if serum_count == 0:
                            break

        execute_hijack_call(stack)

init 5 python:
    add_label_hijack("advance_time_daily_serum_dosage_label", "advance_time_BDSM_performers_daily_serum_dosage_label")
