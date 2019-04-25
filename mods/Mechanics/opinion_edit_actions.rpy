init -1 python:

    esy_mod_init = False

init 1 python: # Create a role that enables the action. TODO: Consider creating a serum trait that is low cost and enables this so that it will be more natural in the game world.
                                                       #TODO: Move role(s) and exclusive actions into the correct folder(s)
    receptive_role = Role("Receptive", [])

init 2 python: # Defines actions and requirements for the mod to start.


    def esy_mod_init_requirement():
        if esy_mod_init == False:
            return True
        return False

    esy_mod_init_action = Action("Add [esy_action]", esy_mod_init_requirement, "esy_mod_init_label",
        menu_tooltip = "Activates the mod")

    mod_list.append(esy_mod_init_action)

label esy_mod_init_label(): # This label runs once on mod startup.

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

init 2 python: # Define actions and requirements for the actual mod here.

    def influence_opinion_requirement(the_person): # Shows only if the_person has been affected by suggestibility serum.
        if the_person.suggestibility > 0:
            return True
        else:
            return False

    influence_opinion = Action("Influence an opinion", influence_opinion_requirement, "influence_opinion_start_label",
        menu_tooltip = "Influence an opinion")
