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

    def IT_project_complete_requirement():
        if mc.business.is_open_for_business() and mc.is_at_work():
            return True
        return False

    def IT_director_on_turn(the_person):
        if the_person.location == mc.business.r_div:
            mc.business.IT_increase_project_progress(amount = (the_person.int * 2) + (the_person.focus))

        if mc.business.IT_project_in_progress:
            the_person.set_override_schedule(mc.business.r_div, the_days = [0, 1, 2, 3, 4], the_times = [1,2,3])
        else:
            the_person.set_override_schedule(None, the_days = [0, 1, 2, 3, 4], the_times = [1,2,3])

        return

    # def IT_director_on_move(the_person):
    #     if mc.business.is_open_for_business() and mc.business.IT_project_in_progress:


    update_IT_projects_action = Action("Review IT Projects", update_IT_projects_requirement, "update_IT_projects_label",
        menu_tooltip = "Start, change, activate, or deactivate IT projects.", priority = 5)
    IT_project_complete_action = Action("IT Project Complete", IT_project_complete_requirement, "IT_project_complete_label")

    IT_director_role = Role("IT Director", [update_IT_projects_action], on_turn = IT_director_on_turn)



label update_IT_projects_label(the_person):
    mc.name "I'd like to review the IT projects."
    the_person "Ok. Here's what we have going on right now [the_person.mc_title]."
    call screen it_project_screen()
    the_person "Got it. Is there anything else I can do for you [the_person.mc_title]?"
    return

label IT_project_complete_label():
    $ the_person = mc.business.it_director
    if the_person == None:
        return
    $ the_person.draw_person()
    "[the_person.possessive_title] tracks you down while you are working."
    the_person "Hey [the_person.mc_title], just wanted to let you know I finished up with that project you had me working on."
    "You take a moment to review your completed projects and decide if you want her to start something different."
    call screen it_project_screen()
    "When you finish reviewing her projects, [the_person.title] gets back to work."

    return
