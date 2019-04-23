# Creates a role for the salon and corresponding actions.

init 1 python:
    salon_manager_role = Role("Salon Manager", [])


init 2 python:

    # Salon Manager Actions

    #salon_in_business_action = Action() # Opens a salon room in the business itself.

    def cut_hair_requirement(the_person):
        for role in the_person.special_role:
            if cut_hair_action in role.actions:
                return True
        else:
            return False

    cut_hair_action = Action("Change hairstyle", cut_hair_requirement, "cut_hair_label",
        menu_tooltip = "Customize hair style and color")

    if cut_hair_action not in salon_manager_role.actions:
        salon_manager_role.actions.append(cut_hair_action)

label cut_hair_label(the_person):
    "You ask [the_person.name] if you can change their style up a bit."
    $ the_person.draw_person()
    the_person.name "Sure, I don't see why not. You paying for it?"
    call hair_style(the_person)
    return
