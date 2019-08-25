# Creates a role for the salon and corresponding actions.
init 2 python:

    # Salon Manager Actions

    # salon_in_business_action = Action() # Opens a salon room in the business itself.

    def cut_hair_requirement(person):
        for role in person.special_role:
            if cut_hair_action in role.actions:
                return True
        else:
            return False

    cut_hair_action = Action("Change hairstyle", cut_hair_requirement, "cut_hair_label", menu_tooltip = "Customize hair style and color")

    salon_manager_role = Role("Salon Manager", [cut_hair_action])


label cut_hair_label(person):
    python:
        hair_style_check = person.hair_style #If hair_style_check is different than person.hair_style it means a "purchase" has been made.
        hair_color_check = person.hair_colour
    "You ask [person.title] if she could change her hairstyle a bit."
    $ person.draw_person()
    person.char "Sure, [person.mc_title], I don't see why not. Let me get my kit."

    call screen hair_creator(person, hair_style_check, hair_color_check)

    $ person.draw_person(position = "stand2")
    if hair_style_check != person.hair_style or hair_color_check != person.hair_colour: # Anything was changed
        person.char "Better now?"
        $ person.draw_person(emotion = "happy")
        mc.name "You look wonderful, [person.possessive_title]!"
    else:
        person.char "It seems you preferred my old look, [the_person.mc_title]."

    $ renpy.scene("Active")
    return
