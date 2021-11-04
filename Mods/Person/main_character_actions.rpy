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
        excluded_roles = ["stripper_role", "waitress_role", "bdsm_performer_role", "manager_role", "mistress_role", "candace_role", "college_intern_role"]
        for role in excluded_roles:
            if role in globals():
                if person.has_role(globals()[role]):
                    return False

        if person not in mc.business.get_employee_list() + unique_character_list:
            if mc.business.get_employee_count() >= mc.business.max_employee_count:
                return "At employee limit"
            return True
        return False

    def mc_action_lasik_surgery_person_requirement(person):
        if big_glasses in person.base_outfit.accessories or modern_glasses in person.base_outfit.accessories:
            if person in unique_character_list:
                return False
            if mc.business.funds < 5000:
                return "Not enough money"
            return True
        return False

    # Rename Person Requirements
    def mc_action_rename_person_requirement(person):
        if person.obedience >= 120:
            return True
        return False

    # Spend the Night Requirements
    def mc_action_spend_the_night_requirement(person):
        if time_of_day == 4 and person.love > 50 and mc.location is person.home: #Has to be night, need to have some love and be in the_person's home location
            return True
        return False

    def mc_remove_person_requirement(person):
        return person in known_people_in_the_game(unique_character_list)

    # Pay Strip Requirements
    def mc_action_pay_to_strip_requirement(person):
        if not person is lily:
            if (person.obedience >= 130 and person.sluttiness >= 15) or (person.sluttiness >= 25 and person.get_opinion_score("not wearing anything") > 0) or person.obedience >= 150 or person.sluttiness >= 50:
                if mc.location.get_person_count() > 1:
                    return "Must be alone with " + person.title
                return True
        return False

    # Obsolete remove next version
    def mc_ask_take_serum_requirement(person):
        return True #Consider only allow asking non employees to take serum.


init 5 python:
    # Schedule Actions
    mc_schedule_person_action = ActionMod("Change Schedule", mc_schedule_person_requirement, "mc_schedule_menu_label", menu_tooltip = "Schedule where [the_person.title] should be throughout the day.", category = "Generic People Actions", initialization = init_action_mod_disabled)

    schedule_early_morning_action = Action("Early Morning", schedule_early_morning_requirement, "mc_schedule_person_label", args = [0], menu_tooltip = "Schedule where [the_person.title] should be during the Early Morning.")
    schedule_actions_list.append(schedule_early_morning_action)

    schedule_morning_action = Action("Morning", schedule_morning_requirement, "mc_schedule_person_label", args = [1], menu_tooltip = "Schedule where [the_person.title] should be during the Morning.")
    schedule_actions_list.append(schedule_morning_action)

    schedule_afternoon_action = Action("Afternoon", schedule_afternoon_requirement, "mc_schedule_person_label", args = [2], menu_tooltip = "Schedule where [the_person.title] should be during the Afternoon.")
    schedule_actions_list.append(schedule_afternoon_action)

    schedule_evening_action = Action("Evening", schedule_evening_requirement, "mc_schedule_person_label", args = [3], menu_tooltip = "Schedule where [the_person.title] should be during the Evening.")
    schedule_actions_list.append(schedule_evening_action)

    schedule_night_action = Action("Night", schedule_night_requirement, "mc_schedule_person_label", args = [4], menu_tooltip = "Schedule where [the_person.title] should be during the Night.")
    schedule_actions_list.append(schedule_night_action)

    mc_start_follow_action = ActionMod("Follow me", mc_start_follow_requirement, "mc_start_follow_label", menu_tooltip = "Ask [the_person.title] to follow you around.", category = "Generic People Actions")
    mc_stop_follow_action = ActionMod("Stop following me", mc_stop_follow_requirement, "mc_stop_follow_label", menu_tooltip = "Have [the_person.title] stop following you.", allow_disable = False, category = "Generic People Actions")

    # Hire Person | Allows you to hire a person if they are not already hired. (Moves them to the appropriate division, no duplicates)
    mc_hire_person_action = ActionMod("Employ", mc_hire_person_requirement, "mc_hire_person_label", menu_tooltip = "Hire [the_person.title] to work for you in your business.", category = "Generic People Actions")

    # Rename Person | Opens a menu that allows you to change first and last name plus a (non- appended) custom the_person.title
    mc_rename_person_action = ActionMod("Rename", mc_action_rename_person_requirement, "mc_rename_person_label", menu_tooltip = "Change the name of [the_person.title].", category = "Generic People Actions", initialization = init_action_mod_disabled)

    # Spend the Night | Allows you to sleep in the home of a person you have increased the love stat.
    mc_spend_the_night_action = ActionMod("Spend the night with girl", mc_action_spend_the_night_requirement, "mc_spend_the_night_label", menu_tooltip = "Allows you to sleep in this location.", category = "Generic People Actions", initialization = init_action_mod_disabled)

    # Pay to Strip | Allows you to enter the pay_strip label used in certain events if requirements are met.
    pay_to_strip_action = ActionMod("Pay her to strip", mc_action_pay_to_strip_requirement, "mc_pay_to_strip_label", menu_tooltip = "Pay [the_person.title] to give you a strip tease.", category = "Generic People Actions", initialization = init_action_mod_disabled)

    mc_lasik_surgery_action = ActionMod("Pay for LASIK surgery\n{color=#ff0000}{size=18}Costs: $5000{/size}{/color}", mc_action_lasik_surgery_person_requirement, "mc_action_lasik_surgery_label", menu_tooltip = "You don't like [the_person.title] wearing glasses, offer to pay for LASIK surgery.", category = "Generic People Actions")

    mc_remove_person_action = ActionMod("Remove from game", mc_remove_person_requirement, "mc_remove_person_label", menu_tooltip = "You are not interested in [the_person.title]. This will remove her from the game.", category = "Generic People Actions", initialization = init_action_mod_disabled)

    main_character_actions_list = [mc_schedule_person_action, mc_start_follow_action, mc_stop_follow_action, mc_hire_person_action, mc_rename_person_action, mc_spend_the_night_action, mc_lasik_surgery_action, pay_to_strip_action, mc_remove_person_action]


label mc_pay_to_strip_label(person):
    # strip a copy of the current outfit (so review outfit can restore the original outfit)
    $ person.outfit = person.outfit.get_copy()

    call pay_strip_scene(person) from _call_pay_strip_scene_generic_people_role

    # reset the person outfit to the one prior to the strip
    python:
        person.apply_planned_outfit()
        person.draw_person(emotion = "happy")

    if person.sluttiness > person.outfit.slut_requirement:
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
    "You tell [person.possessive_title!l] that you are giving her a new name."
    while True:
        menu rename_person_menu:
            "Name: [person.name]":
                $ newname = str(renpy.input("Name: ", person.name))
                $ person.name = newname.replace("[", "[[")
                $ person.home.formal_name = person.name + " " + person.last_name + " home"

            "Last name: [person.last_name]":
                $ new_last_name = str(renpy.input("Last name: ", person.last_name))
                $ person.last_name = new_last_name.replace("[", "[[")
                $ person.home.formal_name = person.name + " " + person.last_name + " home"

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
        if mc.business.funds < (person.calculate_base_salary() * 10):
            renpy.say(None, "Hiring [person.title] will cost you $" + str(person.calculate_base_salary() * 10) + " and put you in debt due to low funds.")
        else:
            renpy.say(None, "Hiring [person.title] will cost you $" + str(person.calculate_base_salary() * 10) + ", do you wish to proceed?")

    menu:
        "Yes":
            pass
        "No":
            return

    "You complete the necessary paperwork and hire [person.title]. What division do you assign them to?"
    menu:
        "Research and Development":
            $ mc.business.hire_person(the_person, "Research")

        "Production":
            $ mc.business.hire_person(the_person, "Production")

        "Supply Procurement":
            $ mc.business.hire_person(the_person, "Supply")

        "Marketing":
            $ mc.business.hire_person(the_person, "Marketing")

        "Human Resources":
            $ mc.business.hire_person(the_person, "HR")

        "Back":
            return

    $ mc.business.change_funds(- (person.calculate_base_salary() * 10))
    "You have hired [person.title], she will start working as soon as possible."
    return


    # Schedule Person Labels

label mc_schedule_menu_label(person): # TODO: Find a way to handle "None" instances of schedule to display formal_name on Action.
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

    $ del schedule_options
    return

label mc_schedule_person_label(*args):
    #$ person = the_person
    $ time_slot = args[0]
    python:
        tuple_list = format_rooms(build_schedule_location_list(person))
        tuple_list.append(["Back","Back"]) # Have a back button to exit the choice list.
        room_choice = renpy.display_menu(tuple_list,True,"Choice") # Turns person_choice into the selected person (Choice).
        del tuple_list

    if room_choice == "Back":
        return
    else:
        $ person.set_schedule(room_choice, times = [time_slot])
        $ renpy.say(None, time_names[time_slot] + " Schedule Set: [room_choice.formal_name]")
        return

# Follower Labels
label mc_start_follow_label(person):
    "You tell [person.title] to follow you around."

    #if the_person.get_opinion_score("being submissive"):

    $ the_person.follow_mc = True
    $ the_person.call_dialogue("seduction_accept_crowded")

    return

label mc_stop_follow_label(person):
    python:
        if the_person.get_destination() is the_person.home:
            schedule_destination = "my room"
        elif the_person.get_destination():
            schedule_destination = "the " + the_person.get_destination().formal_name
        else:
            schedule_destination = "somewhere else"

    "You tell [person.title] to stop following you around."

    $ the_person.follow_mc = False

    $ the_person.draw_person(position = "walking_away")

    $ the_person.run_move(mc.location) # This will trigger stat changes based on clothing, but shouldn't be problematic although it can be exploited.

    the_person.title "Okay [the_person.mc_title], I'll head over to [schedule_destination]."


    return
# Lasik surgery Labels
label mc_action_lasik_surgery_label(the_person):
    mc.name "[the_person.title], your have beautiful eyes, but they are always hidden behind your glasses."
    the_person "Don't you like them? I can wear different glasses tomorrow."
    mc.name "I mean, that I really would like to see you without any glasses."
    if renpy.random.randint(1,2) == 1:
        the_person "I'm sorry, but I can't wear lenses."
        mc.name "That's fine."
    else:
        the_person "If you like, I can start wearing lenses."
        mc.name "I don't think that's the right solution."
    mc.name "I made an appointment for you in the clinic for a LASIK surgery where your eyesight will be corrected."
    "[the_person.title] gives you a spontaneous hug."
    $ the_person.draw_person(position = "kissing")
    the_person "You make me so happy [the_person.mc_title], thank you so much!"
    python:
        the_person.change_happiness(10)
        the_person.change_love(5, max_modified_to = 80)
        mc.business.change_funds(-5000)
        the_person.base_outfit.accessories.remove(filter(lambda x : x in [big_glasses, modern_glasses], the_person.base_outfit.accessories)[0])
    $ the_person.draw_person()
    return

label mc_remove_person_label(person):
    menu:
        "Are you sure?":
            $ person.remove_person_from_game()
            $ jump_game_loop()
        "Reconsider":
            pass
    return
