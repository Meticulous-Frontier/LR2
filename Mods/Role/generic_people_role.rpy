init 2 python:
    # Schedule Person | Allows you to modify the schedule of the_person. Change requirement to be dependent on obedience?
    schedule_actions_list = [] # NOTE: Use this list to display all the schedule actions.
    # Follow Me | Allows you to put a person in a list_of_followers that comes along with you upon every location change (follow normal schedule on time advance, might want to remove them from the list during that, although they will come back if not)
    list_of_followers = []

    # Schedule Person Requirements
    def schedule_person_requirement(person):
        if person.obedience >= 130:
            return True
    def schedule_early_morning_requirement():
        return True
    def schedule_morning_requirement():
        return True
    def schedule_afternoon_requirement():
        return True
    def schedule_evening_requirement():
        return True
    def schedule_night_requirement():
        if person.obedience >=150:
            return True
        else:
            return "Requires: 150 Obedience"

    # Follow Me Requirements
    def start_follow_requirement(person):
        if person not in list_of_followers:
            if person.obedience >= 110:
                return True
    def stop_follow_requirement(person):
        if person in list_of_followers:
            return True

    # Hire Person Requirements
    def hire_person_requirement(person):
        if person not in mc.business.get_employee_list():
            return True

    # Rename Person Requirements
    def rename_person_requirement(person):
        if person.obedience >= 150:
            return True

    # Schedule Actions
    schedule_person_action = Action("Schedule [the_person.title]", schedule_person_requirement, "schedule_menu", menu_tooltip = "Schedule where the person should be throughout the day.")
    schedule_early_morning_action = Action("Early Morning", schedule_early_morning_requirement, "schedule_early_morning", menu_tooltip = "Schedule where the person should be during the Early Morning.")
    schedule_actions_list.append(schedule_early_morning_action)
    schedule_morning_action = Action("Morning", schedule_morning_requirement, "schedule_morning", menu_tooltip = "Schedule where the person should be during the Morning.")
    schedule_actions_list.append(schedule_morning_action)
    schedule_afternoon_action = Action("Afternoon", schedule_afternoon_requirement, "schedule_afternoon", menu_tooltip = "Schedule where the person should be during the Afternoon.")
    schedule_actions_list.append(schedule_afternoon_action)
    schedule_evening_action = Action("Evening", schedule_evening_requirement, "schedule_evening", menu_tooltip = "Schedule where the person should be during the Evening.")
    schedule_actions_list.append(schedule_evening_action)
    schedule_night_action = Action("Night", schedule_night_requirement, "schedule_night", menu_tooltip = "Schedule where the person should be during the Night.")
    schedule_actions_list.append(schedule_night_action)

    start_follow_action= Action("Follow me.", start_follow_requirement, "start_follow", menu_tooltip = "Have the person follow you around.")
    stop_follow_action = Action("Stop following me.", stop_follow_requirement, "stop_follow", menu_tooltip = "Have the person stop following you.")

    # Hire Person | Allows you to hire a person if they are not already hired. (Moves them to the appropriate division, no duplicates)
    hire_person_action = Action("Employ [the_person.title]\n Costs: $300", hire_person_requirement, "hire_person", menu_tooltip = "Hire the the person to work for you in your business. Costs $300")
    # Rename Person | Opens a menu that allows you to change first and last name plus a (non- appended) custom the_person.title
    rename_person_action = Action("Rename [the_person.title]", rename_person_requirement, "rename_person", menu_tooltip = "Change the name of the person.")

    generic_people_role = Role("Generic", [schedule_person_action, start_follow_action, stop_follow_action, hire_person_action, rename_person_action]) # This role is meant to not display in the person_ui_hud

    # NOTE: This extension of "any person" can be toggled from the Action Mod Core menu under "Misc", listed as Generic People Actions
