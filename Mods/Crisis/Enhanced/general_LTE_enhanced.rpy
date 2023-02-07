init 5 python:
    add_label_hijack("normal_start", "update_general_LTE")
    add_label_hijack("after_load", "update_general_LTE")

init 2 python:
    def work_spank_opportunity_all_employees_requirement(the_person):
        if not the_person.is_at_work():
            return False

        # special case for college inters
        if the_person.has_role("College Intern") and not the_person.location == university:
            return True

        return the_person.has_role(employee_role)


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
