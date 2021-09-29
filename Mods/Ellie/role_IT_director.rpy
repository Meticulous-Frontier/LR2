init 1 python:
    def set_IT_director_tag(key, value):
        if mc.business.it_director:
            mc.business.it_director.IT_tags[key] = value

    def get_IT_director_tag(key, default = None):
        if mc.business.it_director:
            return mc.business.it_director.IT_tags.get(key, default)

    def update_IT_projects_requirement(the_person):
        if mc.business.is_open_for_business():
            return True
        return False

    def IT_director_on_turn(the_person):
        if the_person.location == mc.business.r_div:
            mc.business.IT_increase_project_progress(amount = (the_person.int * 2) + (the_person.focus))

        if mc.business.IT_project_in_progress:
            the_person.set_alt_schedule(mc.business.r_div, days = [0, 1, 2, 3, 4], times = [1,2,3])
        else:
            the_person.set_alt_schedule(None, days = [0, 1, 2, 3, 4], times = [1,2,3])

        return

    # def IT_director_on_move(the_person):
    #     if mc.business.is_open_for_business() and mc.business.IT_project_in_progress:


    update_IT_projects_action = Action("Review IT Projects", update_IT_projects_requirement, "update_IT_projects_label",
        menu_tooltip = "Start, change, activate, or deactivate IT projects.", priority = 5)

    IT_director_role = Role("IT Director", [update_IT_projects_action], on_turn = IT_director_on_turn)



label update_IT_projects_label(the_person):
    mc.name "I'd like to review the IT projects."
    the_person "Ok. Here's what we have going on right now [the_person.mc_title]"
    call screen it_project_screen()
    the_person "Got it. Is there anything else I can do for you [the_person.mc_title]?"
    return
