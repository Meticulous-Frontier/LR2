init 2 python:
    def clone_recall_requirement(person):
        if person not in rd_division_basement.people:
            return True

    # Clone Recall - Brings the clone back to base
    clone_recall = Action("Recall clone", clone_recall_requirement, "clone_recall",
        menu_tooltip = "Bring the clone back to the lab for modifications")
    if clone_recall not in clone_role.actions:
        clone_role.actions.append(clone_recall)

# Labels
label clone_recall(person):
    "You order [person.title] back to [rd_division_basement.name]"

    $ mc.location.move_person(person, rd_division_basement)

    person.char "Okay, [person.mc_title]. I'll head there next."
    return
