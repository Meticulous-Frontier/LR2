## Stripclub storyline Mod by Corrado
#  Waitresses role definition.
#  The role is appended to waitresses after they start to work for you.

init 3304 python:
    waitress_wardrobe = wardrobe_from_xml("Waitresses_Wardrobe")

    waitress_role = Role("Waitress", [promote_to_manager_action, strip_club_stripper_fire_action, strip_club_stripper_performance_review_action], hidden = False)

label advance_time_waitresses_daily_serum_dosage_label(stack):
    python:
        if hasattr(mc.business, "waitresses_serum"):
            if mc.business.waitresses_serum:
                serum_count = mc.business.inventory.get_serum_count(mc.business.waitresses_serum)
                if serum_count > 0:
                    for (person,place) in people_to_process:
                        if employee_role in person.special_role:
                            continue
                        if not waitress_role in person.special_role:
                            continue
                        mc.business.inventory.change_serum(mc.business.waitresses_serum,-1)
                        person.give_serum(copy.copy(mc.business.waitresses_serum), add_to_log = False)
                        serum_count -= 1
                        if serum_count == 0:
                            break

        execute_hijack_call(stack)

init 5 python:
    add_label_hijack("advance_time_daily_serum_dosage_label", "advance_time_waitresses_daily_serum_dosage_label")
