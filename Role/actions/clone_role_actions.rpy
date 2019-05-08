init 3 python:
    def clone_recall_requirement(person):
        if person not in rd_division_basement.people:
            return True

    def clone_actions_requirement():
        True

    def clone_actions_initialization(self):
        renpy.call("clone_role_actions_creation")
        return


    clone_actions = ActionMod("Clone Role Actions", clone_actions_requirement, "clone_actions_dummy", initialization = clone_actions_initialization,
        menu_tooltip = "Enables Special Actions for Clones created in the [rd_division_basement.formalName]", category = "Role Actions")

label clone_actions_dummy():
    return

label clone_role_actions_creation():
    # Clone Recall - Brings the clone back to base
    $ clone_recall = Action("Recall clone", clone_recall_requirement, "clone_recall",
        menu_tooltip = "Bring the clone back to the lab for modifications")
    if clone_recall not in clone_role.actions:
        $ clone_role.actions.append(clone_recall)
    return
# Labels
label clone_recall(person):
    "You order [person.title] back to [rd_division_basement.name]"

    $ mc.location.move_person(person, rd_division_basement)

    person.char "Okay, [person.mc_title]. I'll head there next."
    return
