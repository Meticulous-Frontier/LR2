init 5 python:
    add_label_hijack("normal_start", "update_general_LTE")
    add_label_hijack("after_load", "update_general_LTE")

init 2 python:
    def work_spank_opportunity_all_employees_requirement(person):
        # she needs to be a little aroused (reduce number of events)
        if person.arousal < (person.max_arousal * .2):
            return False

        return person.is_at_work() and (person.is_employee() or person.is_strip_club_employee() or person.is_intern())

    def replace_work_spank_opportunity_requirement():
        found = next((x for x in limited_time_event_pool if x[0].effect == "work_spank_opportunity"), None)
        if found:
            found[0].requirement = work_spank_opportunity_all_employees_requirement
        return

label update_general_LTE(stack):
    python:
        replace_work_spank_opportunity_requirement()
        execute_hijack_call(stack)
    return
