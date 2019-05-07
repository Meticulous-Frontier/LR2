init 1 python:
    clone_role = Role("Clone", [])


    def clone_rename_requirement(person):
        if person in rd_division_basement.people:
            return True

    clone_rename = Action("Rename clone", clone_rename_requirement, "clone_rename",
        menu_tooltip = "Give the clone a new name")

    if clone_rename not in clone_role.actions:
        clone_role.actions.append(clone_rename)

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

    if clone_schedule not in clone_role.actions:
        clone_role.actions.append(clone_schedule)

    def clone_hire_requirement(person):
        if person not in mc.business.get_employee_list():
            return True

    clone_hire = Action("Employ clone", clone_hire_requirement, "clone_hire",
        menu_tooltip = "Hire the clone to work for you in your business.")

    if clone_hire not in clone_role.actions:
        clone_role.actions.append(clone_hire)

    # Schedule Actions
    schedule_actions_list = []
    def schedule_early_morning_requirement():
        return True
    schedule_early_morning = Action("Early Morning: [person.schedule[0].formalName]", schedule_early_morning_requirement, "schedule_early_morning",
        menu_tooltip = "Schedule where [person.title] should be during the Early Morning.")
    schedule_actions_list.append(schedule_early_morning)

    def schedule_morning_requirement():
        return True
    schedule_morning = Action("Morning: [person.schedule[1].formalName]", schedule_morning_requirement, "schedule_morning",
        menu_tooltip = "Schedule where [person.title] should be during the Morning.")
    schedule_actions_list.append(schedule_morning)

    def schedule_afternoon_requirement():
        return True
    schedule_afternoon = Action("Afternoon: [person.schedule[2].formalName]", schedule_afternoon_requirement, "schedule_afternoon",
        menu_tooltip = "Schedule where [person.title] should be during the Afternoon.")
    schedule_actions_list.append(schedule_afternoon)

    def schedule_evening_requirement():
        return True
    schedule_evening = Action("Evening: [person.schedule[3].formalName]", schedule_evening_requirement, "schedule_evening",
        menu_tooltip = "Schedule where [person.title] should be during the Evening.")
    schedule_actions_list.append(schedule_evening)

    def schedule_night_requirement():
        return True
    schedule_night = Action("Night: [person.schedule[4].formalName]", schedule_night_requirement, "schedule_night",
        menu_tooltip = "Schedule where [person.title] should be during the Night.")
    schedule_actions_list.append(schedule_night)

label clone_rename(person):
    "You tell [person.title] that it is to be renamed."
    while True:
        menu clone_rename_menu:
            "Name: [person.name]":
                $ clone_name = str(renpy.input("Name: ", person.name))
                $ person.name = clone_name

            "Last name: [person.last_name]":
                $ clone_last_name = str(renpy.input("Last name: ", person.last_name))
                $ person.last_name = clone_last_name

            "Title: [person.title]":
                $ clone_title = str(renpy.input("Title: ", person.title))
                $ person.title = clone_title

            "Back: ":
                return

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

label schedule_early_morning():

    python: # First we select which employee we want

            tuple_list = format_rooms(list_of_places) #TODO: Create a list that excludes homes not in mc.known_home_locations
            tuple_list.append(["Back","Back"]) # Have a back button to exit the choice list.
            room_choice = renpy.display_menu(tuple_list,True,"Choice") # Turns person_choice into the selected person (Choice).

    if room_choice == "Back":
        return
    else:
        $ person.schedule[0] = room_choice
        return

label schedule_morning():


    python: # First we select which employee we want

            tuple_list = format_rooms(list_of_places) #TODO: Create a list that excludes homes not in mc.known_home_locations
            tuple_list.append(["Back","Back"]) # Have a back button to exit the choice list.
            room_choice = renpy.display_menu(tuple_list,True,"Choice") # Turns person_choice into the selected person (Choice).

    if room_choice == "Back":
        return
    else:
        $ person.schedule[1] = room_choice
        return

label schedule_afternoon():

    python: # First we select which employee we want

            tuple_list = format_rooms(list_of_places) #TODO: Create a list that excludes homes not in mc.known_home_locations
            tuple_list.append(["Back","Back"]) # Have a back button to exit the choice list.
            room_choice = renpy.display_menu(tuple_list,True,"Choice") # Turns person_choice into the selected person (Choice).

    if room_choice == "Back":
        return # Where to go if you hit "Back".
    else:
        $ person.schedule[2] = room_choice
        return



label schedule_evening():

    python: # First we select which employee we want

            tuple_list = format_rooms(list_of_places) #TODO: Create a list that excludes homes not in mc.known_home_locations
            tuple_list.append(["Back","Back"]) # Have a back button to exit the choice list.
            room_choice = renpy.display_menu(tuple_list,True,"Choice") # Turns person_choice into the selected person (Choice).

    if room_choice == "Back":
        return # Where to go if you hit "Back".
    else:
        $ person.schedule[3] = room_choice
        return



label schedule_night():
    python: # First we select which employee we want

            tuple_list = format_rooms(list_of_places) #TODO: Create a list that excludes homes not in mc.known_home_locations
            tuple_list.append(["Back","Back"]) # Have a back button to exit the choice list.
            room_choice = renpy.display_menu(tuple_list,True,"Choice") # Turns person_choice into the selected person (Choice).

    if room_choice == "Back":
        return # Where to go if you hit "Back".
    else:
        $ person.schedule[4] = room_choice
        return



label clone_hire(person):
    "You complete the nessesary paperwork and hire [person.title]. What division do you assign them to?"
    menu:
        "Research and Development.":
            $ mc.business.add_employee_research(person)
            $ mc.location.move_person(person, mc.business.r_div)
            $ person.set_work([1,2,3], mc.business.r_div)

        "Production.":
            $ mc.business.add_employee_production(person)
            $ mc.location.move_person(person, mc.business.p_div)
            $ person.set_work([1,2,3], mc.business.p_div)

        "Supply Procurement.":
            $ mc.business.add_employee_supply(person)
            $ mc.location.move_person(person, mc.business.s_div)
            $ person.set_work([1,2,3], mc.business.s_div)

        "Marketing.":
            $ mc.business.add_employee_marketing(person)
            $ mc.location.move_person(person, mc.business.m_div)
            $ person.set_work([1,2,3], mc.business.m_div)

        "Human Resources.":
            $ mc.business.add_employee_hr(person)
            $ mc.location.move_person(person, mc.business.h_div)
            $ person.set_work([1,2,3], mc.business.h_div)

        "Back":
            return

    $ person.special_role.append(employee_role)
    $ work_station_destination = mc.business.get_employee_workstation(the_person).formalName
    "[person.title] heads over to the [work_station_destination]..."
    return
