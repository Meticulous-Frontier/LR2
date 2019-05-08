# NOTE: Not sure where to place these actions yet. Basically actions that could fit on any person regardless of role.
init -1 python:
    apply_mandatory_roles = []

init 2 python:
    # Definitions
    # Schedule Person
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

    # Follow Me
    def start_follow_requirement(person):
        if person not in list_of_followers:
            if person.obedience >= 110:
                return True
    def stop_follow_requirement(person):
        if person in list_of_followers:
            return True

    # Hire Person
    def hire_person_requirement(person):
        if person not in mc.business.get_employee_list():
            return True

    # Rename Person
    def rename_person_requirement(person):
        if person.obedience >= 150:
            return True

    # Schedule Person | Allows you to modify the schedule of the_person. Change requirement to be dependent on obedience?
    schedule_actions_list = [] # NOTE: Use this list to display all the schedule actions.

    schedule_person = Action("Schedule [person.title]", schedule_person_requirement, "schedule_menu",
        menu_tooltip = "Schedule where the target should be throughout the day.")

    schedule_early_morning = Action("Early Morning: [person.schedule[0].formalName]", schedule_early_morning_requirement, "schedule_early_morning",
        menu_tooltip = "Schedule where the target should be during the Early Morning.")
    schedule_actions_list.append(schedule_early_morning)


    schedule_morning = Action("Morning: [person.schedule[1].formalName]", schedule_morning_requirement, "schedule_morning",
        menu_tooltip = "Schedule where the target should be during the Morning.")
    schedule_actions_list.append(schedule_morning)


    schedule_afternoon = Action("Afternoon: [person.schedule[2].formalName]", schedule_afternoon_requirement, "schedule_afternoon",
        menu_tooltip = "Schedule where the target should be during the Afternoon.")
    schedule_actions_list.append(schedule_afternoon)


    schedule_evening = Action("Evening: [person.schedule[3].formalName]", schedule_evening_requirement, "schedule_evening",
        menu_tooltip = "Schedule where the target should be during the Evening.")
    schedule_actions_list.append(schedule_evening)


    schedule_night = Action("Night: [person.schedule[4].formalName]", schedule_night_requirement, "schedule_night",
        menu_tooltip = "Schedule where the target should be during the Night.")
    schedule_actions_list.append(schedule_night)

    # Follow Me | Allows you to put a person in a list_of_followers that comes along with you upon every location change (follow normal schedule on time advance, might want to remove them from the list during that, although they will come back if not)
    list_of_followers = []
    follower_actions = []

    start_follow = Action("Follow me.", start_follow_requirement, "start_follow",
        menu_tooltip = "Have the target follow you around.")
    follower_actions.append(start_follow)

    stop_follow = Action("Stop following me.", stop_follow_requirement, "stop_follow",
        menu_tooltip = "Have the target stop following.")
    follower_actions.append(stop_follow)

    # Hire Person | Allows you to hire a person if they are not already hired. (Moves them to the appropriate division, no duplicates)
    person_utility_actions = []
    hire_person = Action("Employ [the_person.title]\n Costs: $300", hire_person_requirement, "hire_person",
        menu_tooltip = "Hire the the target to work for you in your business. Costs $300")
    person_utility_actions.append(hire_person)
    # Rename Person | Opens a menu that allows you to change first and last name plus a (non- appended) custom the_person.title
    rename_person = Action("Rename [the_person.title]", rename_person_requirement, "rename_person",
        menu_tooltip = "Give the [the_person.title] a new name")
    person_utility_actions.append(rename_person)

    # Setup
    if generic_people_role not in apply_mandatory_roles:
        apply_mandatory_roles.append(generic_people_role)
    if schedule_person not in generic_people_role.actions:
        generic_people_role.actions.append(schedule_person)
    for act in follower_actions:
        if act not in generic_people_role.actions:
            generic_people_role.actions.append(act)
    for act in person_utility_actions:
        if act not in generic_people_role.actions:
            generic_people_role.actions.append(act)
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

            "Possessive Title: [person.possessive_title]":
                $ new_title = str(renpy.input("Possessive Title: ", person.possessive_title))
                $ person.possessive_title = new_title

            "Your Title: [person.mc_title]":
                $ new_title = str(renpy.input("Your Title: ", person.mc_title))
                $ person.mc_title = new_title

            "Back: ":
                return

# Hire Person Labels
label hire_person(person):
    if mc.business.funds < 300:
        "Hiring [person.title] will cost you $300 and put you in debt due to low funds."
    else:
        "Hiring [person.title] will cost you $300, do you wish to proceed?"
    menu:
        "Yes":
            pass
        "No":
            return
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
    $ mc.business.pay(-300)
    $ person.special_role.append(employee_role)
    $ work_station_destination = mc.business.get_employee_workstation(the_person).formalName
    "[person.title] heads over to the [work_station_destination]..."
    return


    # Schedule Person Labels

label schedule_menu(person):
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

    # Follower Labels
label start_follow(person):
    "You tell [the_person.title] to follow you around."
    $ list_of_followers.append(the_person)
    return
label stop_follow(person):
    "You tell [the_person.title] to stop following you around."
    $ list_of_followers.remove(the_person)
    return
