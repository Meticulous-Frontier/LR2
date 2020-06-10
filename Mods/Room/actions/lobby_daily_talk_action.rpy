## Employee Review Mod by Mattt
# Compliment/Insult all employees based on their happiness
init 3 python:

    def daily_talk_requirement():
        if not "daily_talk_employees" in mc.business.event_triggers_dict:
            mc.business.event_triggers_dict["daily_talk_employees"] = None
        if mc.business.get_employee_count() > 0 and mc.business.event_triggers_dict["daily_talk_employees"] != day and mc.business.is_open_for_business():
            return True
        return False

    def daily_talk_initialization(self):
        lobby.add_action(self)
        return

    def daily_talk_update_employee_stats():
        for person in mc.business.get_employee_list():
            person.event_triggers_dict["day_last_employee_interaction"] = day
            if person.obedience > 150 and person.love * 2 + 89 < person.obedience:
                person.change_love(1)
                person.change_happiness(mc.charisma)
            elif person.happiness > 120 and person.love >= 12:
                person.change_obedience(mc.charisma)
                person.change_happiness(-5)
                person.change_love(-2)
            else:
                person.change_love(1)
                person.change_happiness(mc.charisma)

        mc.business.event_triggers_dict["daily_talk_employees"] = day
        return

    daily_talk_action = ActionMod("Talk with Employees {image=gui/heart/Time_Advance.png}", daily_talk_requirement, "daily_talk_employees", initialization = daily_talk_initialization,
        menu_tooltip = "Compliment Work (Happiness <= 120 or Love < 12) / Insult Work (Happiness > 120)", category = "Business")

label daily_talk_employees:

    "You tell all of your employees to meet you in the [lobby.formalName] for a daily chat."
    $ daily_talk_update_employee_stats()

    call advance_time from daily_talk_employees_1

    return
