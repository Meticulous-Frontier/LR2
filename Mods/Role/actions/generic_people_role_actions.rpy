# NOTE: Not sure where to place these actions yet. Basically actions that could fit on any person regardless of role.
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

            "Back":
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
    $ work_station_destination = mc.business.get_employee_workstation(person).formalName
    "[person.title] heads over to the [work_station_destination]..."
    return


    # Schedule Person Labels

label schedule_menu(person): # TODO: Find a way to handle "None" instances of schedule to display formalName on Action.
    python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
        schedule_options = []
        for act in schedule_actions_list:
            schedule_options.append(act)
        schedule_options.append("Back")

    "You decide where [person.title] should be at throughout the day."
    while True:
        $ act_choice = call_formated_action_choice(schedule_options)
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
        "Early Morning Schedule Set: [room_choice.formalName]"
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
        "Morning Schedule Set: [room_choice.formalName]"
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
        "Afternoon Schedule Set: [room_choice.formalName]"
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
        "Evening Schedule Set: [room_choice.formalName]"
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
        "Night Schedule Set: [room_choice.formalName]"
        return

    # Follower Labels
label start_follow(person):
    "You tell [person.title] to follow you around."
    $ list_of_followers.append(the_person)
    return

label stop_follow(person):
    "You tell [person.title] to stop following you around."
    $ list_of_followers.remove(the_person)
    return
