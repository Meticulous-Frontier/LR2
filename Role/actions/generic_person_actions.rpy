# NOTE: Not sure where to place these actions yet. Basically actions that could fit on any person regardless of role.
init 2 python:
    # Rename Person | Opens a menu that allows you to change first and last name plus a (non- appended) custom the_person.title
    def rename_person_requirement(person):
        return True

    rename_person = Action("Rename [the_person.title]", rename_person_requirement, "rename_person",
        menu_tooltip = "Give the [the_person.title] a new name")

    # Hire Person | Allows you to hire a person if they are not already hired. (Moves them to the appropriate division, no duplicates)
    def hire_person_requirement(person):
        if person not in mc.business.get_employee_list():
            return True

    hire_person = Action("Employ [the_person.title]", hire_person_requirement, "hire_person",
        menu_tooltip = "Hire the [the_person.title] to work for you in your business.")


    # Schedule Person | Allows you to modify the schedule of the_person. Change requirement to be dependent on obedience?
    schedule_actions_list = [] # NOTE: Use this list to display all the schedule actions.
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

    # Rename Person Labels
label rename_person(person):
    "You tell [person.possessive_title] that you are giving her a new name."
    while True:
        menu rename_person_menu:
            "Name: [person.name]":
                $ newname = str(renpy.input("Name: ", person.name))
                $ person.name = newname

            "Last name: [person.last_name]":
                $ new_last_name = str(renpy.input("Last name: ", person.last_name))
                $ person.last_name = new_last_name

            "Title: [person.title]":
                $ new_title = str(renpy.input("Title: ", person.title))
                $ person.title = new_title

            "Back: ":
                return

# Hire Person Labels
label hire_person(person):
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


    # Schedule Person Labels
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
