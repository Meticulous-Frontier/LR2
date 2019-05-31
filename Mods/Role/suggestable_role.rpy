# if suggestability is enabled now depends on the lysergide_n2o_serum
# the serum adds the role action to a person and removes it when
# the serum wears off

init 2 python: # Define actions and requirements for the actual mod here.

    def influence_opinion_requirement(person): # Shows only if person has been affected by suggestibility serum.
        if person.suggestibility > 0:
            return True
        else:
            return False

    influence_opinion_action = Action("Influence an opinion", influence_opinion_requirement, "influence_opinion_label",
        menu_tooltip = "Influence a persons opinion about a specific topic")

    suggestable_role = Role("Suggestable", [influence_opinion_action])

