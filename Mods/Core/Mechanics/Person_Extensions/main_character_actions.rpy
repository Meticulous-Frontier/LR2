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
        excluded_roles = ["stripper_role", "stripclub_waitress_role", "stripclub_bdsm_performer_role", "stripclub_manager_role", "stripclub_mistress_role", "candace_role", "college_intern_role"]
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
        if person in unique_character_list:
            return False

        if person.base_outfit and person.base_outfit.has_glasses():
            if person.love < 20: # you need have some connection with her to offer this
                return False
            if person.love < 30:
                return "Requires: 30 Love"
            if not mc.business.has_funds(5000):
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

    def do_a_favor_requirement(person):
        if mc.energy < 15:
            return "Requires: 15{image=gui/extra_images/energy_token.png}"
        if person.days_since_event("obedience_favor", set_if_none = True) >= TIER_0_TIME_DELAY:
            return True
        return "Asked for a favor too recently"

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
    # DISABLED: This functionality is now supported by the base-game
    # mc_hire_person_action = ActionMod("Employ", mc_hire_person_requirement, "mc_hire_person_label", menu_tooltip = "Hire [the_person.title] to work for you in your business.", category = "Generic People Actions")

    # Rename Person | Opens a menu that allows you to change first and last name plus a (non- appended) custom the_person.title
    mc_rename_person_action = ActionMod("Rename", mc_action_rename_person_requirement, "mc_rename_person_label", menu_tooltip = "Change the name of [the_person.title].", category = "Generic People Actions", initialization = init_action_mod_disabled)

    # Spend the Night | Allows you to sleep in the home of a person you have increased the love stat.
    mc_spend_the_night_action = ActionMod("Spend the night with girl", mc_action_spend_the_night_requirement, "mc_spend_the_night_label", menu_tooltip = "Allows you to sleep in this location.", category = "Generic People Actions", initialization = init_action_mod_disabled)

    # Pay to Strip | Allows you to enter the pay_strip label used in certain events if requirements are met.
    # DISABLED: Stripping is now supported in the base game (conditions apply)
    # pay_to_strip_action = ActionMod("Pay her to strip", mc_action_pay_to_strip_requirement, "mc_pay_to_strip_label", menu_tooltip = "Pay [the_person.title] to give you a strip tease.", category = "Generic People Actions", initialization = init_action_mod_disabled)

    mc_lasik_surgery_action = ActionMod("Pay for LASIK surgery\n{color=#ff0000}{size=18}Costs: $5000{/size}{/color}", mc_action_lasik_surgery_person_requirement, "mc_action_lasik_surgery_label", menu_tooltip = "You don't like [the_person.title] wearing glasses, offer to pay for LASIK surgery.", category = "Generic People Actions")

    mc_remove_person_action = ActionMod("Remove from game", mc_remove_person_requirement, "mc_remove_person_label", menu_tooltip = "You are not interested in [the_person.title]. This will remove her from the game.", category = "Generic People Actions", initialization = init_action_mod_disabled)

    main_character_actions_list = [mc_schedule_person_action, mc_start_follow_action, mc_stop_follow_action, mc_rename_person_action, mc_spend_the_night_action, mc_lasik_surgery_action, mc_remove_person_action]

    do_a_favor_action = Action("Ask for a Favor   {color=#FFFF00}-15{/color} {image=gui/extra_images/energy_token.png}", do_a_favor_requirement, "do_a_favor_label",
        menu_tooltip = "Ask for a favor. Successfully asking for a favor tends to build obedience in your relationship.")
    chat_actions.append(do_a_favor_action)


label mc_pay_to_strip_label(person):
    # strip a copy of the current outfit (so review outfit can restore the original outfit)
    $ person.outfit = person.outfit.get_copy()

    call strip_tease(the_person, for_pay = True) from _call_pay_strip_scene_generic_people_role

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
    $ the_person.change_stats(happiness = 5, love = 3)
    call advance_time from _call_advance_time_spend_the_night
    return


label mc_rename_person_label(person):
    "You tell [person.possessive_title] that you are giving her a new name."
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
        if not mc.business.has_funds(person.calculate_base_salary() * 10):
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
            $ mc.business.add_employee_research(the_person)

        "Production":
            $ mc.business.add_employee_production(the_person)

        "Supply Procurement":
            $ mc.business.add_employee_supply(the_person)

        "Marketing":
            $ mc.business.add_employee_marketing(the_person)

        "Human Resources":
            $ mc.business.add_employee_hr(the_person)

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
        $ person.set_schedule(room_choice, the_times = [time_slot])
        $ renpy.say(None, time_names[time_slot] + " Schedule Set: [room_choice.formal_name]")
        return

# Follower Labels
label mc_start_follow_label(person):
    "You tell [person.title] to follow you around."

    $ the_person.follow_mc = True
    person "Ok, let's go."
    jump game_loop      # exit talk menu

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
        the_person.change_stats(happiness = 10, love = 5, max_love = 80)
        mc.business.change_funds(-5000)
        the_person.base_outfit.remove_glasses()
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

#Obedience Actions
label do_a_favor_label(the_person):
    mc.name "Hey. I was wondering if you would be willing to do me a favor."
    if the_person.obedience < 70:
        "[the_person.possessive_title] scoffs and rolls her eyes."
        the_person "Probably not, but shoot your shot, [the_person.mc_title]."
    elif the_person.obedience < 100:
        the_person "Maybe, what do you need?"
    elif the_person.obedience < 130:
        "[the_person.possessive_title] smiles."
        the_person "If I have time. What do you need?"
    else:
        "[the_person.possessive_title] smiles wide."
        the_person "Anything for you, [the_person.mc_title]."
    menu:
        "Small Favor":
            $ mc.change_energy(-15)
            $ favor_success = True
            if mc_at_home():
                mc.name "Hey, I'm a little short. Any chance I can borrow $5 to grab some coffee?"
                if favor_success:
                    the_person "Uhh, yeah I guess that would be okay."
                    "[the_person.possessive_title] grabs her purse and hands you a $5 bill from it."
                    mc.name "Thanks!"
                    $ mc.business.change_funds(5)
                    if the_person.obedience < 130:
                        $ the_person.change_obedience(1)
                else:
                    the_person "I'm not your personal bank account, [the_person.mc_title]."
                    mc.name "Ah, sorry."
            elif mc.is_at_work():
                mc.name "I accidentally left my wallet at home. Can I borrow $5 to grab something from the vending machine?"
                if favor_success:
                    the_person "Oh, sure. I'm sure you're good for it, right?"
                    mc.name "Of course."
                    $ mc.business.change_funds(5)
                    if the_person.obedience < 130:
                        $ the_person.change_obedience(1)
                else:
                    the_person "Aren't you supposed to be paying me? Sorry, I don't carry cash, anyway..."
                    mc.name "Right, sorry."
            else:
                mc.name "Hey, I left my wallet at home. Can you spot me $5 for a coffee?"
                if favor_success:
                    the_person "Oh, sure. I'm sure you're good for it, right?"
                    mc.name "Of course."
                    $ mc.business.change_funds(5)
                    if the_person.obedience < 130:
                        $ the_person.change_obedience(1)
                else:
                    the_person "Sorry, I don't carry cash [the_person.mc_title]"
                    mc.name "Right, sorry."

        "Moderate Favor" if the_person.days_since_event("obedience_med_favor", set_if_none = True) > TIER_1_TIME_DELAY:
            $ mc.change_energy(-15)
            $ favor_success = True  #calculate this instead of assuming true
            if not mc.phone.has_number(the_person):
                mc.name "I was just wondering if I could get your number."
                if favor_success:
                    the_person "I suppose that would be okay. Just no drunk 3 am phone calls, okay?"
                    mc.name "Of course."
                    "You grab your phone and quickly put her number in as she lists it off for you."
                    $ mc.phone.register_number(the_person)
                    if the_person.obedience < 150:
                        $ the_person.change_obedience(2)
                else:
                    the_person "Yeah right, I don't think we're close enough for something like that."
                    "Ouch."
            else:
                mc.name "You look amazing in that outfit. Can I snap a picture to update your profile on my phone?"
                if favor_success:
                    the_person "Yeah, I can do that!"
                    $ the_person.draw_person(position = "stand3")
                    "You quickly snap a picture of [the_person.possessive_title]"
                    $ the_person.draw_person(position = the_person.idle_pose)
                    if the_person.obedience < 150:
                        $ the_person.change_obedience(2)
                else:
                    the_person "Sorry, I'm not here to play dress up for you."
                    "Ouch."
            $ the_person.set_event_day("obedience_med_favor")
        "Large Favor" if the_person.days_since_event("obedience_large_favor", set_if_none = True) > TIER_2_TIME_DELAY and mc.phone.has_number(the_person):
            $ mc.change_energy(-15)
            $ favor_success = True  #calculate this instead of assuming true
            if the_person.is_family():
                if mc_at_home():
                    mc.name "Hey, can I ask for a huge favor?"
                    the_person "Umm, maybe. What do you need?"
                    if time_of_day < 2:
                        mc.name "I really need to get going, could you pack me a lunch? I don't think I have time today."
                    else:
                        mc.name "Can you get the trash and the dishes tonight? I know it's my turn, but I have work stuff I really need to get done."
                    if favor_success:
                        the_person "I... yeah I guess I can do that. Just this once?"
                        mc.name "Of course."

                        if the_person.obedience < 160:
                            $ the_person.change_obedience(3)
                    else:
                        the_person "Nope! the world doesn't revolve around you, find a way to get it done yourself!"
                else:
                    mc.name "Hey, can I ask for a favor?"
                    the_person "Umm, maybe?"
                    mc.name "I accidentally left my wallet at home, but I need to grab some food at the office today."
                    mc.name "Can you front me $20?"
                    if favor_success:
                        the_person "I... yeah I guess I can do that. Try not to make a habit out of this, okay?"
                        mc.name "Of course."
                        $ mc.business.change_funds(20)
                        if the_person.obedience < 160:
                            $ the_person.change_obedience(3)
                    else:
                        the_person "No way! If I give you money I'll never see it again!"
            elif not the_person.home in mc.known_home_locations:
                mc.name "Can I get your address? It would be handy to have."
                if favor_success:
                    the_person "I guess. Just no unannounced 3 am booty calls, okay?"
                    mc.name "Of course."
                    $ the_person.learn_home()
                    if the_person.obedience < 160:
                        $ the_person.change_obedience(3)
                else:
                    the_person "Yeah right! That is need to know information only, mister."
                    mc.name "Ah, okay..."
            elif the_person.has_role(instapic_role):
                mc.name "Your instapics have been so hot lately. Could you take a few more today? I like to check it when I go to bed."
                if favor_success:
                    the_person "Oh! I'm glad you like them. Yeah I could do that."
                    mc.name "Great! I appreciate it."
                    $ the_person.event_triggers_dict["insta_generate_pic"] = True
                    if the_person.obedience < 160:
                        $ the_person.change_obedience(3)
                else:
                    the_person "Ummm, I just post when I get the chance. Sorry I'm not sure if I'll get around to it today or not."
                    mc.name "Ah, okay."
            else:
                mc.name "You look amazing today. Have you ever thought about starting an Instapic account?"
                mc.name "You really should. I know I would check it out!"
                if favor_success:
                    the_person "You know, I had been considering doing that. I think you've convinced me, I'll do it later!"
                    mc.name "Great! I can't wait to see you post!"
                    $ the_person.event_triggers_dict["insta_known"] = True
                    $ the_person.add_role(instapic_role)
                    if the_person.obedience < 160:
                        $ the_person.change_obedience(3)
                else:
                    the_person "Sorry, I'm not really into social media."
                    mc.name "Okay, well if you ever change your mind, you would be great!"
            $ the_person.set_event_day("obedience_large_favor")
        "Nevermind":
            mc.name "Nevermind, it's okay."
            return
    $ the_person.set_event_day("obedience_favor")
    return
