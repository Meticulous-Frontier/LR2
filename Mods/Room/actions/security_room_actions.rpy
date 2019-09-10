# I'll want to use transition into using appendable Action lists when the content is laid down.
# TODO: A) Make a requirement fo reach room or B) Find a way to display Cost only while requirement is met
init -1 python:
    security_room_actions = []
    security_room_cctv_actions = []
    security_room_investigation_actions = []

init 3 python: # Put this behind a mod init to ensure compatibility


    def security_overview_requirement():
        return True

    security_overview_action = Action("Security Overview", security_overview_requirement, "security_overview",
    menu_tooltip = "Oversee your business, employees plus more.")



    def investigation_requirement():
        if len(mc.business.get_employee_list()) > 0:
            return True
        return "No employees"

    investigation_employee_action = Action("Investigate an employee", investigation_requirement, "investigation_employee_label",
        menu_tooltip = "Find out information about the selected person.")
    security_room_actions.append(investigation_employee_action)

    def investigation_opinion_requirement():
        if the_person.get_random_opinion(False, True) == None:
            return "All opinions discovered"
        else:
            return True

    investigation_opinions_action = Action("Find opinions. {image=gui/heart/Time_Advance.png}", investigation_opinion_requirement, "investigation_opinions_label",
        menu_tooltip = "Find the likes and dislikes of a person")
    security_room_investigation_actions.append(investigation_opinions_action)

    def investigation_home_requirement():
        if the_person.home in mc.known_home_locations:
            return "Home discovered"
        else:
            return True

    investigation_home_action = Action("Find home location. {image=gui/heart/Time_Advance.png}", investigation_home_requirement, "investigation_home_label",
        menu_tooltip = "Adds the home location to the list of known homes.")
    security_room_investigation_actions.append(investigation_home_action)

    def cctv_requirement():
        return True

    cctv_action = Action("Watch CCTV", cctv_requirement, "cctv_label",
        menu_tooltip = "Check what's happening via the CCTV system.")
    security_room_actions.append(cctv_action)

    def observation_requirement():
        return True

    m_division_observation_action = Action("Observe the [m_division.formalName]", observation_requirement, "m_division_observation_label",
        menu_tooltip = "See what's going on in ")
    security_room_cctv_actions.append(m_division_observation_action)

    p_division_observation_action = Action("Observe the [p_division.formalName]", observation_requirement, "p_division_observation_label",
        menu_tooltip = "See what's going on in ")
    security_room_cctv_actions.append(p_division_observation_action)

    rd_division_observation_action = Action("Observe the [rd_division.formalName]", observation_requirement, "rd_division_observation_label",
        menu_tooltip = "See what's going on in ")
    security_room_cctv_actions.append(rd_division_observation_action)

    s_division_observation_action = Action("Observe the Supply Division", observation_requirement, "s_division_observation_label",
        menu_tooltip = "See what's going on in ")
    security_room_cctv_actions.append(s_division_observation_action)

    office_observation_action = Action("Observe the [office.formalName]", observation_requirement, "office_observation_label",
        menu_tooltip = "See what's going on in ")
    security_room_cctv_actions.append(office_observation_action)




label security_overview():


#    "You seat yourself at the control panel."
#    "From here you can run investigations, watch the CCTV... (tooltip)Unlock more options by investing."
    while True:
        python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
                security_options = []
                for act in security_room_actions:
                    security_options.append(act)
                security_options.append("Back")
                act_choice = call_formated_action_choice(security_options)

        if act_choice == "Back":
            return
        else:
            $ act_choice.call_action()



label cctv_label():
    "Select location to observe"
    while True:
        python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
                cctv_options = []
                for act in security_room_cctv_actions:
                    cctv_options.append(act)
                cctv_options.append("Back")
                act_choice = call_formated_action_choice(cctv_options)

        if act_choice == "Back":
            return
        else:
            $ act_choice.call_action()



label m_division_observation_label():
    "[m_division.formalName]"
    if len(m_division.people) < 1:
        "CCTV" "No one is around and nothing of interested seems to be going on."

    python:
        randint = renpy.random.randint(1, 5)

    if randint == 1:
        "Var 1"
    elif randint == 2:
        "Var 2"
    elif randint == 3:
        "Var 3"
    elif randint == 4:
        "Var 4"
    elif randint == 5:
        "Var 5"
    else:
        "Nani!?"

    return

label p_division_observation_label():
    "[p_division.formalName]"
    if len(m_division.people) < 1:
        "CCTV" "No one is around and nothing of interested seems to be going on."
    return

label rd_division_observation_label():
    "[rd_division.formalName]"
    if len(m_division.people) < 1:
        "CCTV" "No one is around and nothing of interested seems to be going on."

    return

label s_division_observation_label():
    "Supply Division"
    if len(m_division.people) < 1:
        "CCTV" "No one is around and nothing of interested seems to be going on."

    return

label office_observation_label():
    "[office.formalName]"
    if len(m_division.people) < 1:
        "CCTV" "No one is around and nothing of interested seems to be going on."
    return

label investigation_employee_label():
    while True:
        $ people_list = ["Investigate"]
        $ people_list.extend(known_people_in_the_game([mc]) + ["Back"])
        call screen main_choice_display([people_list])
        $ person_choice = _return
        $ del people_list        

        if person_choice == "Back":
            return # Where to go if you hit "Back".
        else:
            call investigate_person(person_choice) from _call_investigate_person# What to do if "Back" was not the choice taken.

label investigate_person(person_choice = the_person): # Need to default to the_person for return calls.
    $ the_person = person_choice
    while True:
        python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
                investigative_options = []
                for act in security_room_investigation_actions:
                    investigative_options.append(act)
                investigative_options.append("Back")
                act_choice = call_formated_action_choice(investigative_options)

        if act_choice == "Back":
            return
        else:
            $ act_choice.call_action()

label investigation_home_label():
    "You conveniently find [the_person.name]'s address in the yellow pages."
    $ learn_home(the_person)
    
    # call advance_time from _call_advance_time_investigation_home_label

    return

label investigation_opinions_label():

    $ the_person.discover_opinion(the_person.get_random_opinion(False, True))
    "You discover something about [the_person.name]"
    # call advance_time from _call_advance_time_investigation_opinions_label

    return










#    menu: # NOTE: Rework to be using call_formated_action_choice and display as a modular list.
#        "Find home {image=gui/heart/Time_Advance.png}" if the_person.home not in mc.known_home_locations:
#
#
#        "Find home (disabled) \n{size=22}Already known{/size}" if the_person.home in mc.known_home_locations:
#            pass
#
#        "Investigate opinions {image=gui/heart/Time_Advance.png}" if the_person.get_random_opinion(False, True): # TODO: Add a disabled slug if all opinions are CURRENTLY discovered.
#            $ the_person.discover_opinion(the_person.get_random_opinion(False, True))
#            "You discover something about [the_person.char]"
#            $ advance_time()
#            return
#
#        "Investigate opinions (disabled) \n{size=22}All opinions known{/size}" if the_person.get_random_opinion(False, True) == None:
#            pass
#        "Back":
#            jump investigation_employee_label
