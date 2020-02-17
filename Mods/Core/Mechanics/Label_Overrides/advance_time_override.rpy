# Overrides the default advance time function in the game
# it adds a increased chance for a crisis to occur when more time passed without a crisis
# it adds a way of preventing the same crisis popping up over and over, whilst others never get triggered by remembering a set of occurred events
init -1 python:
    def advance_time_next_requirement():
        return True

    def advance_time_end_of_day_requirement():
        return time_of_day == 0

    def advance_time_random_crisis_requirement():
        return time_of_day != 0 and renpy.random.randint(0,100) < crisis_chance

    # only trigger mandatory crisis events in timeslot 4 when in bedroom (actually end of day after pressing sleep button, required for dialog consistency)
    def advance_time_mandatory_crisis_requirement():
        return True

    def advance_time_bankrupt_check_requirement():
        return time_of_day == 4

    def advance_time_mandatory_morning_crisis_requirement():
        return time_of_day == 0

    def advance_time_random_morning_crisis_requirement():
        return time_of_day == 0 and renpy.random.randint(0,100) < morning_crisis_chance

    def advance_time_daily_serum_dosage_requirement():
        return time_of_day == 1 and daily_serum_dosage_policy.is_owned() # This runs if you have the corresponding policy

    def advance_time_people_run_day_requirement():
        return time_of_day == 4

    def advance_time_people_run_turn_requirement():
        return True

init 5 python:
    global crisis_chance
    global morning_crisis_chance

    global crisis_base_chance
    global morning_crisis_base_chance

    # some crisis events have impact on game dynamic and should be allowed to trigger often
    excluded_crisis_tracker_events = [work_relationship_change_crisis, unisex_restroom_crisis_action]

    crisis_base_chance = 8
    morning_crisis_base_chance = 4

    crisis_tracker = []
    morning_crisis_tracker = []

    crisis_chance = crisis_base_chance
    morning_crisis_chance = morning_crisis_base_chance

    mandatory_advance_time = False

    advance_time_people_run_turn_action = ActionMod("End of day run people", advance_time_people_run_turn_requirement,
        "advance_time_people_run_turn_label", priority = 1, allow_disable = False)

    advance_time_mandatory_crisis_action = ActionMod("Run mandatory crisis events", advance_time_mandatory_crisis_requirement,
        "advance_time_mandatory_crisis_label", priority = 2, category = "Gameplay", allow_disable = False)
    advance_time_random_crisis_action = ActionMod("Run random crisis events", advance_time_random_crisis_requirement,
        "advance_time_random_crisis_label", priority = 3, category = "Gameplay")

    advance_time_people_run_day_action = ActionMod("End of day run people", advance_time_people_run_day_requirement,
        "advance_time_people_run_day_label", priority = 4, allow_disable = False)

    advance_time_next_action = ActionMod("Advances into the next time slot", advance_time_next_requirement,
        "advance_time_next_label", priority = 5, allow_disable = False)

    advance_time_bankrupt_check_action = ActionMod("Determines if it is game over due to having gone bankrupt.", advance_time_bankrupt_check_requirement,
        "advance_time_bankrupt_check_label", priority = 6, category = "Gameplay")

    advance_time_end_of_day_action = ActionMod("Ends the day if time_of_day is 4", advance_time_end_of_day_requirement,
        "advance_time_end_of_day_label", priority = 7, allow_disable = False)

    advance_time_mandatory_morning_crisis_action = ActionMod("Run mandatory morning crisis events", advance_time_mandatory_morning_crisis_requirement,
        "advance_time_mandatory_morning_crisis_label", priority = 8, category = "Gameplay", allow_disable = False)

    advance_time_random_morning_crisis_action = ActionMod("Run random morning crisis events", advance_time_random_morning_crisis_requirement,
        "advance_time_random_morning_crisis_label", priority = 9, category = "Gameplay")

    advance_time_daily_serum_dosage_action = ActionMod("Employees daily Serum", advance_time_daily_serum_dosage_requirement,
        "advance_time_daily_serum_dosage_label", priority = 10, allow_disable = False)

    # NOTE: Depends on people_to_process being up to date.
    advance_time_people_run_move_action = ActionMod("Moves people_to_process to their destinations", advance_time_next_requirement,
        "advance_time_people_run_move_label", priority = 15, allow_disable = False)

    advance_time_action_list = [advance_time_people_run_turn_action, advance_time_people_run_day_action, advance_time_end_of_day_action, advance_time_next_action, advance_time_mandatory_crisis_action,
        advance_time_random_crisis_action, advance_time_mandatory_morning_crisis_action, advance_time_random_morning_crisis_action, advance_time_daily_serum_dosage_action,
        advance_time_people_run_move_action, advance_time_bankrupt_check_action]

    config.label_overrides["advance_time"] = "advance_time_enhanced"

    def get_crisis_from_crisis_list():
        possible_crisis_list = []
        for crisis in crisis_list:
            ic = [c[0] for c in crisis_list].index(crisis[0]) # get index of crisis
            if not ic in crisis_tracker: # skip events in tracker list
                if crisis[0].is_action_enabled(): #Get the first element of the weighted tuple, the action.
                    possible_crisis_list.append(crisis) #Build a list of valid crises from ones that pass their requirement.
        renpy.random.shuffle(possible_crisis_list)    # shuffle the list in random order
        return get_random_from_weighted_list(possible_crisis_list)

    def get_limited_time_action_for_person(person):
        possible_crisis_list = []
        for crisis in limited_time_event_pool:
            if crisis[0].is_action_enabled(person): #Get the first element of the weighted tuple, the action.
                possible_crisis_list.append(crisis) #Build a list of valid crises from ones that pass their requirement.
        renpy.random.shuffle(possible_crisis_list)    # shuffle the list in random order
        return get_random_from_weighted_list(possible_crisis_list, return_everything = True)


    def get_morning_crisis_from_crisis_list():
        possible_morning_crises_list = []
        for crisis in morning_crisis_list:
            ic = [c[0] for c in morning_crisis_list].index(crisis[0]) # get index of crisis
            if not ic in morning_crisis_tracker: # skip events in tracker list
                if crisis[0].is_action_enabled(): #Get the first element of the weighted tuple, the action.
                    possible_morning_crises_list.append(crisis) # Build a list of valid crises from ones that pass their requirement.
        renpy.random.shuffle(possible_morning_crises_list)    # shuffle the list in random order
        return get_random_from_weighted_list(possible_morning_crises_list)

    def cleanup_crisis_tracker():
        while len(crisis_tracker) > 6: # release old tracked events
            del crisis_tracker[0]
        return

    def cleanup_morning_crisis_tracker():
        while len(morning_crisis_tracker) > 2: # release old tracked events
            del morning_crisis_tracker[0]
        return

label advance_time_enhanced:
    # 1) Turns are processed _before_ the time is advanced.
    # 1a) crises are processed if they are triggered.
    # 2) Time is advanced, day is advanced if required.
    # 3) People go to their next intended location.
    # Note: This will require breaking people's turns into movement and actions.
    # Then: Add research crisis when serum is finished, requiring additional input from the player and giving the chance to test a serum on the R&D staff.

    python:
        #renpy.say("", "advance_time_enhanced -> location: " + mc.location.name + ", time: [time_of_day]") # DEBUG
        advance_time_count = 0 # NOTE: Count and Max might need to be unique for each label since it carries over.
        advance_time_max_actions = len(advance_time_action_list) # This list is automatically sorted by priority due to the class properties.
        advance_time_action_list_sorted = sorted(advance_time_action_list, key = lambda x: x.priority)

    while advance_time_count < advance_time_max_actions:
        $ act = advance_time_action_list_sorted[advance_time_count]
        if act.is_action_enabled(): # Only run actions that have their requirement met.
            $ act.call_action()
            $ renpy.scene("Active")

        $ advance_time_count += 1

    python:
        # increase crisis chance (every time slot)
        crisis_chance += 1
        renpy.free_memory()
        mc.location.show_background()
        x = None
        c = None

    if mandatory_advance_time: #If a crisis has told us to advance time after it we do so.
        call advance_time from _call_advance_time_advance_time_enhanced
    $ people_to_process = []
    return

label advance_time_enhanced_next_day_no_events:
    call advance_time_next_label() from _call_advance_time_next_label_no_events
    call advance_time_people_run_day_label() from _call_advance_time_people_run_day_label_no_events
    if advance_time_bankrupt_check_action.enabled:
        call advance_time_bankrupt_check_label() from _call_advance_time_bankrupt_check_label_no_events
    call advance_time_end_of_day_label() from _call_advance_time_end_of_day_label_no_events
    return

label advance_time_bankrupt_check_label():
    python:
        if mc.business.funds < 0:
            # "advance_time_bankrupt_check_label" # DEBUG
            mc.business.bankrupt_days += 1
            if mc.business.bankrupt_days == mc.business.max_bankrupt_days:
                renpy.say("","With no funds to pay your creditors you are forced to close your business and auction off all of your materials at a fraction of their value. Your story ends here.")
                renpy.full_restart()
            else:
                days_remaining = mc.business.max_bankrupt_days-mc.business.bankrupt_days
                renpy.say("","Warning! Your company is losing money and unable to pay salaries or purchase necessary supplies! You have [days_remaining] days to restore yourself to positive funds or you will be foreclosed upon!")
        else:
            mc.business.bankrupt_days = 0
    return

label advance_time_random_crisis_label():
    # "advance_time_random_crisis_label - timeslot [time_of_day]" #DEBUG
    $ cleanup_crisis_tracker()
    $ the_crisis = get_crisis_from_crisis_list()
    if the_crisis:
        #$ mc.log_event("General [[" + str(len(possible_crisis_list)) + "]: " + the_crisis.name, "float_text_grey")
        $ crisis_chance = crisis_base_chance
        if not the_crisis in excluded_crisis_tracker_events:
            $ crisis_tracker.append([c[0] for c in crisis_list].index(the_crisis)) # add crisis index to recent crisis list
        if _return == "Advance Time":
            $ mandatory_advance_time = True
        $ the_crisis.call_action()
        $ del the_crisis
    $ mc.location.show_background()
    show screen business_ui
    return

label advance_time_mandatory_crisis_label():
    # "advance_time_mandatory_crisis_label - timeslot [time_of_day]" #DEBUG
    python:
        mandatory_crisis_count = 0
        mandatory_crisis_max = len(mc.business.mandatory_crises_list)
        clear_list = []

    while mandatory_crisis_count < mandatory_crisis_max: #We need to keep this in a renpy loop, because a return call will always return to the end of an entire python block.
        if mandatory_crisis_count < len(mc.business.mandatory_crises_list): # extra check to make sure index still exists
            $ the_crisis = mc.business.mandatory_crises_list[mandatory_crisis_count]
            if the_crisis.is_action_enabled():
                $ the_crisis.call_action()
                if _return == "Advance Time":
                    $ mandatory_advance_time = True
                $ renpy.scene("Active")
                $ clear_list.append(the_crisis)
            $ del the_crisis
        $ mandatory_crisis_count += 1

    python: #Needs to be a different python block, otherwise the rest of the block is not called when the action returns.
        mc.location.show_background()
        for crisis in clear_list:
            if crisis in mc.business.mandatory_crises_list: # extra check to see if crisis still in list
                mc.business.mandatory_crises_list.remove(crisis) #Clean up the list.

        del clear_list
    return

label advance_time_people_run_turn_label():
    # "advance_time_people_run_turn_label - timeslot [time_of_day]" #DEBUG
    python:
        mandatory_advance_time = False

        people_to_process = [] #This is a master list of turns of need to process, stored as tuples [character,location]. Used to avoid modifying a list while we iterate over it, and to avoid repeat movements.
        for place in list_of_places:
            for person in place.people:
                people_to_process.append([person, place])

        for (person, place) in people_to_process: #Run the results of people spending their turn in their current location.
            person.run_turn()
        mc.business.run_turn()
        mc.run_turn()

    return

label advance_time_people_run_day_label():
    # "advance_time_people_run_day_label - timeslot [time_of_day]" # DEBUG
    #if time_of_day == 4: ##First, determine if we're going into the next chunk of time. If we are, advance the day and run all of the end of day code. NOTE: We can do checks like these with Action.requirements
    python:
        for (person, place) in people_to_process:
            person.run_day()

        mc.run_day()
        mc.business.run_day()
    return

label advance_time_end_of_day_label():
    # "advance_time_end_of_day_label - timeslot [time_of_day]" # DEBUG
    call screen end_of_day_update() # We have to keep this outside of a python block, because the renpy.call_screen function does not properly fade out the text bar.

    python:
        mc.business.clear_messages()
        # increase morning crisis chance (once a day)
        morning_crisis_chance += 2
        perk_system.update()  #TEST to see if this is a good time for this.
    return

label advance_time_mandatory_morning_crisis_label():
    # "advance_time_mandatory_morning_crisis_label  - timeslot [time_of_day]" # DEBUG
    #"advance_time_mandatory_morning_crisis_label" #DEBUG
    #Now we run mandatory morning crises. Nearly identical to normal crises, but these always trigger at the start of the day (ie when you wake up and before you have control of your character.)
    python:
        mandatory_morning_crisis_count = 0
        mandatory_morning_crisis_max = len(mc.business.mandatory_morning_crises_list)
        clear_list = []

    while mandatory_morning_crisis_count < mandatory_morning_crisis_max: #We need to keep this in a renpy loop, because a return call will always return to the end of an entire python block.
        $ the_crisis = mc.business.mandatory_morning_crises_list[mandatory_morning_crisis_count]
        if the_crisis.is_action_enabled():
            $ the_crisis.call_action()
            if _return == "Advance Time":
                $ mandatory_advance_time = True
            $ renpy.scene("Active")
            $ clear_list.append(the_crisis)
        $ mandatory_morning_crisis_count += 1
        $ del the_crisis

    python: #Needs to be a different python block, otherwise the rest of the block is not called when the action returns.
        mc.location.show_background()
        for crisis in clear_list:
            mc.business.mandatory_morning_crises_list.remove(crisis) #Clean up the list.

        del clear_list
    return

label advance_time_random_morning_crisis_label():
    # "advance_time_random_morning_crisis_label  - timeslot [time_of_day]" #DEBUG
    $ cleanup_morning_crisis_tracker()
    $ the_morning_crisis = get_morning_crisis_from_crisis_list()
    if the_morning_crisis:
        #$ mc.log_event("Morning: [[" + str(len(possible_morning_crises_list)) + "] : " +  the_morning_crisis.name, "float_text_grey")
        $ morning_crisis_chance = morning_crisis_base_chance
        if not the_morning_crisis in excluded_crisis_tracker_events:
            $ morning_crisis_tracker.append([c[0] for c in morning_crisis_list].index(the_morning_crisis)) # add crisis index to recent crisis list
        $ the_morning_crisis.call_action()
        if _return == "Advance Time":
            $ mandatory_advance_time = True
        $ del the_morning_crisis
    $ mc.location.show_background()
    return

label advance_time_next_label():
    # "advance_time_next_label  - timeslot [time_of_day]" #DEBUG
    python:
        if time_of_day == 4: # NOTE: Take care of resetting it to 0 here rather than during end_day_label
            time_of_day = 0
            day += 1
        else:
            time_of_day += 1 ##Otherwise, just run the end of day code.
    return

label advance_time_daily_serum_dosage_label():
    # "advance_time_daily_serum_dosage_label - timeslot [time_of_day]" #DEBUG
    $ mc.business.give_daily_serum()
    return

label advance_time_people_run_move_label():
    # "advance_time_people_run_move_label - timeslot [time_of_day]" #DEBUG
    python:
        for (person, place) in people_to_process: #Now move everyone to where the should be in the next time chunk. That may be home, work, etc.
            person.run_move(place)
            if person.follow_mc: # move follower to mc location
                person.location().move_person(person, mc.location)

            if person.title is not None: #We don't assign events to people we haven't met.
                if renpy.random.randint(0,100) < 12: #Only assign one to 12% of people, to cut down on the number of people we're checking.
                    the_crisis = get_limited_time_action_for_person(person)
                    if the_crisis is not None:
                        limited_time_event = Limited_Time_Action(the_crisis[0], the_crisis[0].event_duration) #Wraps the action so that we can have an instanced duration counter and add/remove it easily.\
                        #renpy.notify("Created event: " + the_crisis[0].name + " for " + people.name)
                        if the_crisis[2] == "on_talk" and len(person.on_talk_event_list) == 0: # prevent multiple on talk events for person
                            person.on_talk_event_list.append(limited_time_event)

                        elif the_crisis[2] == "on_enter" and len(person.on_room_enter_event_list) == 0: # prevent multiple on enter events for person
                            person.on_room_enter_event_list.append(limited_time_event)

    return
