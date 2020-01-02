init 2 python:
    # Schedule Person | Allows you to modify the schedule of the_person. Change requirement to be dependent on obedience?
    schedule_actions_list = [] # NOTE: Use this list to display all the schedule actions.

    # Schedule Person Requirements
    def mc_schedule_person_requirement(person):
        if person.obedience >= 130 and not person in unique_character_list:
            return True
        return False

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
    def mc_start_follow_requirement(person):
        return not person.follow_mc and person.obedience >= 110

    def mc_stop_follow_requirement(person):
        return person.follow_mc

    # Hire Person Requirements
    def mc_hire_person_requirement(person):
        if person not in mc.business.get_employee_list() + unique_character_list:
            return True
        return False

    # Rename Person Requirements
    def mc_action_rename_person_requirement(person):
        if person.obedience >= 120:
            return True
        return False

    # Spend the Night Requirements
    def mc_action_spend_the_night_requirement(person):
        if time_of_day is 4 and person.love > 50 and mc.location is person.home: #Has to be night, need to have some love and be in the_person's home location
            return True
        return False

    # Pay Strip Requirements
    def mc_action_pay_to_strip_requirement(person):
        if not person is lily:
            if (person.obedience >= 130 and person.sluttiness >= 15) or (person.sluttiness >= 25 and person.get_opinion_score("not wearing anything") > 0) or person.obedience >= 150 or person.sluttiness >= 50:
                if len(mc.location.people) > 1:
                    return "Must be alone with " + person.title
                return True
        return False

init 5 python:
    # Schedule Actions
    mc_schedule_person_action = ActionMod("Schedule [the_person.title]", mc_schedule_person_requirement, "mc_schedule_menu_label", menu_tooltip = "Schedule where the person should be throughout the day.", category = "Generic People Actions")

    schedule_early_morning_action = Action("Early Morning", schedule_early_morning_requirement, "mc_schedule_person_label", args = [0], menu_tooltip = "Schedule where the person should be during the Early Morning.")
    schedule_actions_list.append(schedule_early_morning_action)

    schedule_morning_action = Action("Morning", schedule_morning_requirement, "mc_schedule_person_label", args = [1], menu_tooltip = "Schedule where the person should be during the Morning.")
    schedule_actions_list.append(schedule_morning_action)

    schedule_afternoon_action = Action("Afternoon", schedule_afternoon_requirement, "mc_schedule_person_label", args = [2], menu_tooltip = "Schedule where the person should be during the Afternoon.")
    schedule_actions_list.append(schedule_afternoon_action)

    schedule_evening_action = Action("Evening", schedule_evening_requirement, "mc_schedule_person_label", args = [3], menu_tooltip = "Schedule where the person should be during the Evening.")
    schedule_actions_list.append(schedule_evening_action)

    schedule_night_action = Action("Night", schedule_night_requirement, "mc_schedule_person_label", args = [4], menu_tooltip = "Schedule where the person should be during the Night.")
    schedule_actions_list.append(schedule_night_action)

    mc_start_follow_action = ActionMod("Follow me.", mc_start_follow_requirement, "mc_start_follow_label", menu_tooltip = "Have the person follow you around.", category = "Generic People Actions")
    mc_stop_follow_action = ActionMod("Stop following me.", mc_stop_follow_requirement, "mc_stop_follow_label", menu_tooltip = "Have the person stop following you.", allow_disable = False, category = "Generic People Actions")

    # Hire Person | Allows you to hire a person if they are not already hired. (Moves them to the appropriate division, no duplicates)
    mc_hire_person_action = ActionMod("Employ [the_person.title]", mc_hire_person_requirement, "mc_hire_person_label", menu_tooltip = "Hire the the person to work for you in your business.", category = "Generic People Actions")

    # Rename Person | Opens a menu that allows you to change first and last name plus a (non- appended) custom the_person.title
    mc_rename_person_action = ActionMod("Rename [the_person.title]", mc_action_rename_person_requirement, "mc_rename_person_label", menu_tooltip = "Change the name of the person.", category = "Generic People Actions")

    # Spend the Night | Allows you to sleep in the home of a person you have increased the love stat.
    mc_spend_the_night_action = ActionMod("Spend the night with [the_person.possessive_title]", mc_action_spend_the_night_requirement, "mc_spend_the_night_label", menu_tooltip = "Allows you to sleep in this location.", category = "Generic People Actions")

    # Pay to Strip | Allows you to enter the pay_strip label used in certain events if requirements are met.
    pay_to_strip_action = ActionMod("Pay [the_person.title] to strip", mc_action_pay_to_strip_requirement, "mc_pay_to_strip_label", menu_tooltip = "Pay the person to give you a strip tease.", category = "Generic People Actions")

    main_character_actions_list = [mc_schedule_person_action, mc_start_follow_action, mc_stop_follow_action, mc_hire_person_action, mc_rename_person_action, mc_spend_the_night_action, pay_to_strip_action]


label mc_pay_to_strip_label(person):
    # strip a copy of the current outfit (so review outfit can restore the original outfit)
    $ person.outfit = person.outfit.get_copy()

    call pay_strip_scene(person) from _call_pay_strip_scene_generic_people_role

    # reset the person outfit to the one prior to the strip
    python:
        outfit_sluttiness = person.outfit.slut_requirement
        person.review_outfit(dialogue = False)
        person.draw_person(emotion = "happy")

    if person.sluttiness > outfit_sluttiness:
        "She slowly puts her clothes back on, while looking at you seductively."
    else:
        "She quickly puts her clothes back on."
    return

# NOTE: Not sure where to place these actions yet. Basically actions that could fit on any person regardless of role.
label mc_spend_the_night_label(person): # Consider adding the sleep_action to the_person's room, but stats jump all over the place so doesn't necessarily make sense.
    "You go to sleep in [person.home.name]."
    $ person.change_love(5)
    $ person.change_happiness(5)
    call advance_time from _call_advance_time_spend_the_night
    return


label mc_rename_person_label(person):
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
                $ new_title = str(renpy.input("Title: ", remove_display_tags(person.title)))
                $ person.set_title(new_title)

            "Possessive Title: [person.possessive_title]":
                $ new_title = str(renpy.input("Possessive Title: ", remove_display_tags(person.possessive_title)))
                $ person.set_possessive_title(new_title)

            "Your Title: [person.mc_title]":
                $ new_title = str(renpy.input("Your Title: ", person.mc_title))
                $ person.set_mc_title(new_title)

            "Back":
                return

# Hire Person Labels
label mc_hire_person_label(person):

    python:
        if mc.business.funds < person.calculate_base_salary():
            renpy.say("", "Hiring [person.title] will cost you $" + str(person.calculate_base_salary()) + " and put you in debt due to low funds.")
        else:
            renpy.say("", "Hiring [person.title] will cost you $" + str(person.calculate_base_salary()) + ", do you wish to proceed?")

    menu:
        "Yes":
            pass
        "No":
            return

    "You complete the necessary paperwork and hire [person.title]. What division do you assign them to?"
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
    $ mc.business.change_funds(- person.calculate_base_salary())

    $ person.event_triggers_dict["employed_since"] = day
    $ mc.business.listener_system.fire_event("new_hire", the_person = person)
    $ person.special_role.append(employee_role)

    $ work_station_destination = mc.business.get_employee_workstation(person).formalName
    "[person.title] heads over to the [work_station_destination]..."
    return


    # Schedule Person Labels

label mc_schedule_menu_label(person): # TODO: Find a way to handle "None" instances of schedule to display formalName on Action.
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
            $ act_choice.call_action(person)

label mc_schedule_person_label(*args):
    #$ person = the_person
    $ time_slot = args[0]
    python:
        tuple_list = format_rooms(build_schedule_location_list(person))
        tuple_list.append(["Back","Back"]) # Have a back button to exit the choice list.
        room_choice = renpy.display_menu(tuple_list,True,"Choice") # Turns person_choice into the selected person (Choice).

    if room_choice == "Back":
        return
    else:
        $ person.schedule[time_slot] = room_choice
        $ renpy.say("", time_names[time_slot] + " Schedule Set: [room_choice.formalName]")
        return

# Follower Labels
label mc_start_follow_label(person):
    "You tell [person.title] to follow you around."

    #if the_person.get_opinion_score("being submissive"):

    $ the_person.follow_mc = True
    $ the_person.personality.get_dialogue(the_person, "seduction_accept_crowded")

    return

label mc_stop_follow_label(person):
    python:
        if the_person.schedule[time_of_day] is the_person.home:
            schedule_destination = "my room."
        else:
            schedule_destination = "somewhere else." # If their destination is not their home it tends to be None so can't reliably use destination.formalName

    "You tell [person.title] to stop following you around."

    $ the_person.follow_mc = False

    $ the_person.draw_person(position = "walking_away")

    $ the_person.run_move(mc.location) # This will trigger stat changes based on clothing, but shouldn't be problematic although it can be exploited.

    the_person.title "Okay [the_person.mc_title], I'll head over to [schedule_destination]"


    return
