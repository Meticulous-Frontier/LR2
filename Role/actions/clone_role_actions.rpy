init 2 python:
    # Actions


    def clone_recall_requirement(person):
        if person not in rd_division_basement.people:
            return True

    clone_recall = Action("Recall clone", clone_recall_requirement, "clone_recall",
        menu_tooltip = "Bring the clone back to the lab for modifications")

    if clone_recall not in clone_role.actions:
        clone_role.actions.append(clone_recall)

    def clone_schedule_requirement(person):
        return True

    clone_schedule = Action("Schedule clone", clone_schedule_requirement, "clone_schedule",
        menu_tooltip = "Schedule where the clone should be throughout the day.")

init 3 python:
    if clone_schedule not in clone_role.actions:
        clone_role.actions.append(clone_schedule)


    if rename_person not in clone_role.actions:
        clone_role.actions.append(rename_person)

    if hire_person not in clone_role.actions:
        clone_role.actions.append(hire_person)

# Labels
label clone_recall(person):
    "You order [person.title] back to [rd_division_basement.name]"

    $ mc.location.move_person(person, rd_division_basement)

    person.char "Okay, [person.mc_title]. I'll head there next."
    return

label clone_schedule(person):
    "You decide where [person.title] should be at throughout the day."
    while True:
        python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
                schedule_options = []
                for act in schedule_actions_list:
                    schedule_options.append(act)
                schedule_options.append("Back")
                act_choice = call_formated_action_choice(schedule_options)

        if act_choice == "Back":
            return
        else:
            $ act_choice.call_action()
