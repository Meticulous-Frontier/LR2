# Creates a role for the salon and corresponding actions.

init 1 python:
    salon_manager_role = Role("Salon Manager", [])


init 2 python:

    # Salon Manager Actions

    #salon_in_business_action = Action() # Opens a salon room in the business itself.

    def cut_hair_requirement(person):
        for role in person.special_role:
            if cut_hair_action in role.actions:
                return True
        else:
            return False

    cut_hair_action = Action("Change hairstyle", cut_hair_requirement, "cut_hair_label",
        menu_tooltip = "Customize hair style and color")

    if cut_hair_action not in salon_manager_role.actions:
        salon_manager_role.actions.append(cut_hair_action)

label cut_hair_label(person):
    python:
        hair_style_check = person.hair_style #If hair_style_check is different than person.hair_style it means a "purchase" has been made.
        hair_color_check = person.hair_colour
    "You ask [person.title] if you can change their style up a bit."
    $ person.draw_person()
    person.char "Sure, I don't see why not. Let me get my kit."
    call screen hair_creator(the_person)
    $ person.draw_person(position = "stand2")
    person.char "Better now?"
    $renpy.scene("Active")
    return
