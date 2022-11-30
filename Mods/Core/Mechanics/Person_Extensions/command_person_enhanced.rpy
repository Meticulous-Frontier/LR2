
init 2 python:
    def give_panties_requirement(person):
        if person.obedience < 110:
            return "Requires: 110 Obedience"
        if person.effective_sluttiness() < 30 and person.love < 30:
            return "Requires: 30 Sluttiness or 30 Love"
        return True

    def make_onlyfans_together_requirement(person):
        if person.obedience < 150:
            return "Requires: 150 Obedience"
        if not the_person.has_role(onlyfans_role):
            return "No OnlyFans Account"
        return True

    def bend_over_your_desk_requirement(person):
        if not the_person.is_employee():
            return False
        if mc.business.event_triggers_dict.get("employee_over_desk_unlock", False):
            if person.obedience < 130:
                return "Requires: 130 Obedience"
            else:
                return True
        return False

    # extend the bugfix build_command_person_actions_menu function
    def build_command_person_actions_menu2(the_person):
        result = build_command_person_actions_menu(the_person)
        make_onlyfans_together_action = Action("Make a OnlyFans video together", requirement = make_onlyfans_together_requirement, effect = "make_onlyfans_together_label", args = the_person, requirement_args = the_person,
            menu_tooltip = "Order " + the_person.title + " to make a OnlyFans video together with you.", priority = -5)
        bend_over_your_desk_action = Action("Bend her over her desk", requirement = bend_over_your_desk_requirement, effect = "bend_over_your_desk_label", args = the_person, requirement_args = the_person,
            menu_tooltip = "Order " + the_person.title + " to bend over her desk so you can enjoy her ass.", priority = -5)
        result.insert(7, make_onlyfans_together_action)
        result.insert(7, bend_over_your_desk_action)
        return result

    # this only works when we can enhance the menu from the bugfix
    if "build_command_person_actions_menu" in globals():
        config.label_overrides["command_person"] = "command_person_enhanced"

label command_person_enhanced(the_person):
    mc.name "[the_person.title], I want you to do something for me."
    the_person "Yes [the_person.mc_title]?"

    if mod_installed:
        call screen enhanced_main_choice_display(build_menu_items([build_command_person_actions_menu2(the_person)]))
    else:
        call screen main_choice_display([build_command_person_actions_menu2(the_person)])

    if _return != "Return":
        $ _return.call_action()
    return
