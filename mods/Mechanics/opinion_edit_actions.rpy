init -1 python:

    esy_mod_init = False

init 1 python:
    receptive_role = Role("Receptive", [])

init 2 python:

    def esy_mod_init_requirement():
        if esy_mod_init == False:
            return True
        return False

    esy_mod_init_action = Action("Add [esy_action]", esy_mod_init_requirement, "esy_mod_init_label",
        menu_tooltip = "Activates the mod")
    mod_list.append(esy_mod_init_action)

init 2 python:

    # Requirements for actions collect them here

    def influence_opinion_requirement(the_person):
        if the_person.suggestibility > 0:
            return True
        else:
            return False

    influence_opinion = Action("Influence an opinion", influence_opinion_requirement, "influence_opinion_label",
        menu_tooltip = "Influence an opinion")

label esy_mod_init_label():

    python:
        for place in list_of_places:
            for people in place.people:
                if receptive_role not in people.special_role:
                    people.special_role.append(receptive_role)
        if influence_opinion not in receptive_role.actions:
            receptive_role.actions.append(influence_opinion)

        esy_mod_init = True

    if esy_mod_init:
        "Expanded Suggestability enabled"
    return
