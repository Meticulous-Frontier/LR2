# I'll want to use transition into using appendable Action lists when the content is laid down.

init 3 python:

    def security_overview_requirment():
        return True

    security_overview_action = Action("Security Overview", security_overview_requirment, "security_overview",
    menu_tooltip = "Oversee your business, employees plus more.")

    m_division_basement.actions.append(security_overview_action)

label security_overview():

    $ create_room_label_list()
    $ m_division.labels.append("m_division_observation")
    $ rd_division.labels.append("rd_division_observation")

    $ business_rooms = [m_division, p_division, rd_division, office, lobby]

    "You seat yourself at the control panel."
    "From here you can run investigations, watch the CCTV... (tooltip)Unlock more options by investing."
    menu security_menu:

        # NOTE: Rework to be using call_formated_action_choice and display as a modular list.

        "Watch CCTV":
            "Select location to observe"
            python:
                    the_rooms = []
                    for room in business_rooms:
                        the_rooms.append(room)

                    tuple_list = format_rooms(the_rooms, "Observe: ")

                    tuple_list.append(["Back","Back"])
                    room_choice = renpy.display_menu(tuple_list,True,"Choice")
                    if room_choice == "Back":
                        renpy.jump("security_menu")

                    for observ in room_choice.labels:
                        renpy.call(observ)

        "Investigate an employee":
            "Select who you want to investigate"
            python: # First we select which employee we want

                    tuple_list = format_person_list(mc.business.get_employee_list(), draw_hearts = True) #The list of people to show. e.g mc.location.people
                    tuple_list.append(["Back","Back"]) # Have a back button to exit the choice list.
                    person_choice = renpy.display_menu(tuple_list,True,"Choice") # Turns person_choice into the selected person (Choice).

                    if person_choice == "Back":
                        renpy.jump("security_menu") # Where to go if you hit "Back".
        #            else:
        #                renpy.say("","You send a shipment of clothes to " + person_choice.name) #Add flavor text to what is about to happen. e.g "You tell the_person to go visit Starbuck for training".
        #                renpy.say("", "Delivery has been made")

            call investigate_person(person_choice)# What to do if "Back" was not the choice taken.
#            jump game_loop # Return to the game_loop or a label that will bring you back to the game loop

        "Back":
            return

label rd_division_observation(): # TODO: This is being called due to an error in return, figure out where.
    "Research Division"
    return
label m_division_observation():
    "Marketing division"
    return

label investigate_person(person_choice):
    $ the_person = person_choice
    menu: # NOTE: Rework to be using call_formated_action_choice and display as a modular list.
        "Find home {image=gui/heart/Time_Advance.png}" if the_person.home not in mc.known_home_locations:
            "You use Gowgl possible locations and find a match"
            $ learn_home(the_person)
            $ advance_time()
            return

        "Find home (disabled) \n{size=22}Already known{/size}" if the_person.home in mc.known_home_locations:
            pass

        "Investigate opinions {image=gui/heart/Time_Advance.png}" if the_person.get_random_opinion(False, True): # TODO: Add a disabled slug if all opinions are CURRENTLY discovered.
            $ the_person.discover_opinion(the_person.get_random_opinion(False, True))
            "You discover something about [the_person.char]"
            $ advance_time()
            return

        "Investigate opinions (disabled) \n{size=22}All opinions known{/size}" if the_person.get_random_opinion(False, True) == None:
            pass
        "Back":
            return
