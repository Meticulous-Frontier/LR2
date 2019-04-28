# I'll want to use transition into using appendable Action lists when the content is laid down.
init -1 python:
    security_actions = []
    cctv_actions = []
    investigation_actions = []

init 3 python: # Put this behind a mod init to ensure compatability


    def security_overview_requirement():
        return True

    security_overview_action = Action("Security Overview", security_overview_requirement, "security_overview",
    menu_tooltip = "Oversee your business, employees plus more.")
    m_division_basement.actions.append(security_overview_action)


    def investigation_requirement():
        return True

    investigate_employee_action = Action("Investigate an employee", investigation_requirement, "investigate_employee_label",
        menu_tooltip = "Find out information about the selected person.")
    security_actions.append(investigate_employee_action)

    investigation_opinions_action = Action("Find opinions", investigation_requirement, "investigation_opinions_label",
        menu_tooltip = "Find the likes and dislikes of a person")
    investigation_actions.append(investigation_opinions_action)

    investigation_home_action = Action("Find home location.", investigation_requirement, "investigation_home_label",
        menu_tooltip = "Adds the home location to the list of known homes.")
    investigation_actions.append(investigation_home_action)

    def cctv_requirement():
        return True

    cctv_action = Action("Watch CCTV", cctv_requirement, "cctv_label",
        menu_tooltip = "Check what's happening via the CCTV system.")
    security_actions.append(cctv_action)

    def observation_requirement():
        return True

    m_division_observation_action = Action("Observe the [m_division.formalName]", observation_requirement, "m_division_observation_label",
        menu_tooltip = "See what's going on in ")
    cctv_actions.append(m_division_observation_action)

    p_division_observation_action = Action("Observe the [p_division.formalName]", observation_requirement, "p_division_observation_label",
        menu_tooltip = "See what's going on in ")
    cctv_actions.append(p_division_observation_action)

    rd_division_observation_action = Action("Observe the [rd_division.formalName]", observation_requirement, "rd_division_observation_label",
        menu_tooltip = "See what's going on in ")
    cctv_actions.append(rd_division_observation_action)

    s_division_observation_action = Action("Observe the Supply Division", observation_requirement, "s_division_observation_label",
        menu_tooltip = "See what's going on in ")
    cctv_actions.append(s_division_observation_action)

    office_observation_action = Action("Observe the [office.formalName]", observation_requirement, "office_observation_label",
        menu_tooltip = "See what's going on in ")
    cctv_actions.append(office_observation_action)




label security_overview():


#    "You seat yourself at the control panel."
#    "From here you can run investigations, watch the CCTV... (tooltip)Unlock more options by investing."

    python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
            security_options = []
            for act in security_actions:
                security_options.append(act)
            security_options.append("Back")
            act_choice = call_formated_action_choice(security_options)

            if act_choice == "Back":
                renpy.jump("game_loop")
            else:
                act_choice.call_action()



label cctv_label():
    "Select location to observe"
    python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
            cctv_options = []
            for act in cctv_actions:
                cctv_options.append(act)
            cctv_options.append("Back")
            act_choice = call_formated_action_choice(cctv_options)

            if act_choice == "Back":
                renpy.jump("security_overview")
            else:
                act_choice.call_action()


label m_division_observation_label():
    $ randint = renpy.random.randint(1, 5)
    "[m_division.formalName]"

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

    jump cctv_label

label p_division_observation_label():
    "[p_division.formalName]"
    jump cctv_label

label rd_division_observation_label():
    "[rd_division.formalName]"
    jump cctv_label

label s_division_observation_label():
    "Supply Division"
    jump cctv_label

label office_observation_label():
    "[office.formalName]"
    jump cctv_label

label investigate_employee_label():
    "Select who you want to investigate"
    python: # First we select which employee we want

            tuple_list = format_person_list(mc.business.get_employee_list(), draw_hearts = True) #The list of people to show. e.g mc.location.people
            tuple_list.append(["Back","Back"]) # Have a back button to exit the choice list.
            person_choice = renpy.display_menu(tuple_list,True,"Choice") # Turns person_choice into the selected person (Choice).

            if person_choice == "Back":
                renpy.jump("security_overview") # Where to go if you hit "Back".

    call investigate_person(person_choice)# What to do if "Back" was not the choice taken.




label investigate_person(person_choice):
    $ the_person = person_choice

    python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
            investigative_options = []
            for act in investigation_actions:
                investigative_options.append(act)
            investigative_options.append("Back")
            act_choice = call_formated_action_choice(investigative_options)

            if act_choice == "Back":
                renpy.jump("security_overview")
            else:
                act_choice.call_action()




label investigation_home_label():
    "You conveniently find [the_person.name]'s adress in the yellow pages."
    $ learn_home(the_person)
    $ advance_time()
    call investigate_person(the_person)

label investigation_opinions_label():

    $ the_person.discover_opinion(the_person.get_random_opinion(False, True))
    "You discover something about [the_person.name]"
    $ advance_time()
    call investigate_person(the_person)










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
#            jump investigate_employee_label
