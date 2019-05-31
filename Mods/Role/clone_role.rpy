init 2 python:
    def clone_recall_requirement(person):
        if person not in rd_division_basement.people:
            return True

    # Clone Recall - Brings the clone back to base
    clone_recall = Action("Recall clone", clone_recall_requirement, "clone_recall", menu_tooltip = "Bring the clone back to the lab for modifications")
    
    clone_role = Role("Clone", [clone_recall])



    # TODO: Create an outfit for clones to use.
    # TODO: Make an action to investigate a person and copy their wardrobe, give it to other people (clone)
    # TODO: Create a Room instance for clone(s) that does not overwrite interfere with person.home
