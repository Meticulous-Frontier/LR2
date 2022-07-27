init 1 python:
    def weekend_serum_dosage_duty_requirement(the_person):
        if not weekend_serum_dosage_policy.is_owned():
            return False
        else:
            return True

    def weekend_serum_dosage_policy_requirement():
        if daily_serum_dosage_policy.is_owned():
            return True
        else:
            return False

    def weekend_serum_dosage_duty_on_move(the_person):
        if the_person.event_triggers_dict.get("daily_serum_distributed", False):
            return #Give it to them first thing in the morning, but only once

        if not mc.business.is_weekend():
            return #Don't give it to them on work days.

        the_serum = None
        if the_person in mc.business.research_team:
            the_serum = mc.business.r_serum
        elif the_person in mc.business.market_team:
            the_serum = mc.business.m_serum
        elif the_person in mc.business.production_team:
            the_serum = mc.business.p_serum
        elif the_person in mc.business.supply_team:
            the_serum = mc.business.s_serum
        elif the_person in mc.business.hr_team:
            the_serum = mc.business.h_serum

        if the_serum is not None:
            the_person.event_triggers_dict["daily_serum_distributed"] = True
            should_give_serum = True
            for active_serum in the_person.serum_effects:
                if the_serum.is_same_design(active_serum):
                    if active_serum.duration - active_serum.duration_counter >= 3:
                        should_give_serum = False #Don't double-dose girls if they have the serum running and it will last the work day already
                        break

            if should_give_serum:
                if mc.business.inventory.get_serum_count(the_serum) > 0:
                    mc.business.inventory.change_serum(the_serum,-1)
                    the_person.give_serum(the_serum, add_to_log = False)
                else:
                    the_message = "Stockpile out of " + the_serum.name + " to give to staff."
                    mc.business.add_counted_message(the_message)

    weekend_serum_dosage_policy = Policy(name = "Weekend Serum Dosage",
        desc = "Mandatory serum testing is expanded into the weekend. Each employee will receive two doses of the selected serum for their department to take over the weekend, if enough are currently in the stockpile.",
        cost = 10000,
        toggleable = True,
        requirement = weekend_serum_dosage_policy_requirement,
        dependant_policies = daily_serum_dosage_policy)

    weekend_serum_dosage_duty = Duty("Weekend Serum Dose",
        "Receive a dose of serum from management at the start of every weekend, unless a previous dose will last the weekend. Serum type can be varied by department and set from the main office (daily serum dose).",
        requirement_function = weekend_serum_dosage_duty_requirement,
        on_move_function = weekend_serum_dosage_duty_on_move, #NOTE: A flag makes sure this is only triggered once per day.
        on_day_function = daily_serum_dosage_duty_on_day,
        only_at_work = False)

    serum_policies_list.append(weekend_serum_dosage_policy)
    general_duties_list.append(weekend_serum_dosage_duty)
