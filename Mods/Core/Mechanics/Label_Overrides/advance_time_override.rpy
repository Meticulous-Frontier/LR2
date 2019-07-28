# Overrides the default advance time function in the game
# it adds a increased chance for a crisis to occur when more time passed without a crisis
# it adds a way of preventing the same crisis popping up over and over, whilst others never get triggered by remembering a set of occured events
init -1 python:
    bedroom_not_required_labels = ["dinner_date", "invest_rep_visit_label", "advanced_serum_stage_2_label", "serum_creation_crisis_label", "quitting_crisis_label"]

    # fix for date requirement triggered in wrong timeslot
    def dinner_date_requirement(day_of_week): #Used for a mandatory crisis that triggers on the next Friday in time chunk 3.
        if time_of_day == 4 and day%7 == day_of_week: #Day of week is a nubmer from 0 to 6, where 0 is Monday.
            return True
        return False

    def advance_time_requirement():
        return True

    def advance_time_next_requirement():
        return True # We always want to increase the time_of_day value unless it is night time in which case the end of day action is triggered.

    def advance_time_end_of_day_requirement(): # NOTE: Make sure to assign a False return value if you want to do checks towards is_action_enabled()
        return time_of_day == 4 # If it's night then run the end of day label.

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

init 5 python:
    global crisis_chance
    global morning_crisis_chance

    global crisis_base_chance
    global morning_crisis_base_chance

    crisis_base_chance = 8
    morning_crisis_base_chance = 4

    crisis_tracker = []
    morning_crisis_tracker = []

    crisis_chance = crisis_base_chance
    morning_crisis_chance = morning_crisis_base_chance

    advance_time_people_to_process_action = ActionMod("Creates a list of people to process", advance_time_requirement,
        "advance_time_people_to_process_label", priority = 0, allow_disable = False)
    advance_time_end_of_day_action = ActionMod("Ends the day if time_of_day is 4", advance_time_end_of_day_requirement,
        "advance_time_end_of_day_label", priority = 1, allow_disable = False)
    advance_time_next_action = ActionMod("Advances into the next time slot", advance_time_next_requirement,
        "advance_time_next_label", priority = advance_time_end_of_day_action.priority + 1, # End of day calculations take priority
        allow_disable = False)
    advance_time_mandatory_crisis_action = ActionMod("Run mandatory crisis events", advance_time_mandatory_crisis_requirement,
        "advance_time_mandatory_crisis_label", priority = advance_time_next_action.priority + 1, category = "Gameplay", allow_disable = False)
    advance_time_random_crisis_action = ActionMod("Run random crisis events", advance_time_random_crisis_requirement,
        "advance_time_random_crisis_label", priority = advance_time_next_action.priority + 1, category = "Gameplay")
    advance_time_mandatory_morning_crisis_action = ActionMod("Run mandatory morning crisis events", advance_time_mandatory_morning_crisis_requirement,
        "advance_time_mandatory_morning_crisis_label", priority = advance_time_next_action.priority + 1, category = "Gameplay", allow_disable = False)
    advance_time_random_morning_crisis_action = ActionMod("Run random morning crisis events", advance_time_random_morning_crisis_requirement,
        "advance_time_random_morning_crisis_label", priority = advance_time_next_action.priority + 1, category = "Gameplay")
    advance_time_daily_serum_dosage_action = ActionMod("Employees daily Serum", advance_time_daily_serum_dosage_requirement,
        "advance_time_daily_serum_dosage_label", priority = 0, allow_disable = False)
    advance_time_people_run_move_action = ActionMod("Moves people_to_process to their destinations", advance_time_requirement,
        "advance_time_people_run_move_label", priority = advance_time_people_to_process_action.priority + advance_time_next_action.priority + 1, # NOTE: Depends on people_to_process being up to date.
        allow_disable = False)
    advance_time_bankrupt_check_action = ActionMod("Determines if it is game over due to having gone bankrupt.", advance_time_bankrupt_check_requirement,
        "advance_time_bankrupt_check_label", priority = 0, category = "Gameplay")

    advance_time_action_list = [advance_time_people_to_process_action, advance_time_end_of_day_action, advance_time_next_action, advance_time_mandatory_crisis_action,
        advance_time_random_crisis_action, advance_time_mandatory_morning_crisis_action, advance_time_random_morning_crisis_action, advance_time_daily_serum_dosage_action,
        advance_time_people_run_move_action, advance_time_bankrupt_check_action]

    config.label_overrides["advance_time"] = "advance_time_enhanced"

label advance_time_enhanced:
    # 1) Turns are processed _before_ the time is advanced.
    # 1a) crises are processed if they are triggered.
    # 2) Time is advanced, day is advanced if required.
    # 3) People go to their next intended location.
    # Note: This will require breaking people's turns into movement and actions.
    # Then: Add research crisis when serum is finished, requiring additional input from the player and giving the chance to test a serum on the R&D staff.

    $ mc.can_skip_time = False #Ensure the player cannot skip time during crises.

    #"advance_time_enhanced" # DEBUG
    python:
        advance_time_count = 0 # NOTE: Count and Max might need to be unique for each label since it carries over.
        advance_time_max_actions = len(advance_time_action_list) # This list is automatically sorted by priority due to the class properties.
        advance_time_action_list_sorted = sorted(advance_time_action_list, key = lambda x: x.priority)

    while advance_time_count < advance_time_max_actions:
        $ act = advance_time_action_list_sorted[advance_time_count]
        if act.is_action_enabled(): # Only run actions that have their requirement met.

            $ act.call_action()
            $ renpy.scene("Active")

        $ advance_time_count += 1

    # increase crisis chance (every time slot)
    $ crisis_chance += 1
    $ mc.can_skip_time = True #Now give the player the ability to skip time again, because they should be back in control.
    return

label advance_time_bankrupt_check_label():
    if mc.business.funds < 0:
        #"advance_time_bankrupt_check_label" # DEBUG
        $ mc.business.bankrupt_days += 1
        if mc.business.bankrupt_days == mc.business.max_bankrupt_days:
            $ renpy.say("","With no funds to pay your creditors you are forced to close your business and auction off all of your materials at a fraction of their value. Your story ends here.")
            $ renpy.full_restart()
        else:
            $ days_remaining = mc.business.max_bankrupt_days-mc.business.bankrupt_days
            $ renpy.say("","Warning! Your company is losing money and unable to pay salaries or purchase necessary supplies! You have [days_remaining] days to restore yourself to positive funds or you will be foreclosed upon!")
    else:
        $ mc.business.bankrupt_days = 0
    return

label advance_time_end_of_day_label():
    # make sure we run all required action before switching to next day
    call advance_time_mandatory_crisis_label from _call_advance_time_mandatory_crisis_label_advance_time_end_of_day_label

    #"advance_time_end_of_day_label" # DEBUG
    #if time_of_day == 4: ##First, determine if we're going into the next chunk of time. If we are, advance the day and run all of the end of day code. NOTE: We can do checks like these with Action.requirements
    python:
        for (people,place) in people_to_process:
            people.run_day()

    $ mc.run_day()
    $ mc.business.run_day()

    $ day += 1

    call screen end_of_day_update() # We have to keep this outside of a python block, because the renpy.call_screen function does not properly fade out the text bar.
    $ mc.business.clear_messages()

    # increase morning crisis chance (once a day)
    $ morning_crisis_chance += 2
    return

label advance_time_random_crisis_label():
    #"advance_time_random_crisis_label" #DEBUG
    python:
        # how many crisis events are disabled?
        disabled = 0
        for action_mod in action_mod_list:
            if hasattr(action_mod, "is_crisis") and action_mod.is_crisis and not action_mod.enabled:
                if not hasattr(action_mod, "is_morning_crisis") or not action_mod.is_morning_crisis:
                    disabled += 1

        while len(crisis_tracker) > ((len(crisis_list) - disabled) // 3): # release old tracked events
            del crisis_tracker[0]

        possible_crisis_list = []
        for crisis in crisis_list:
            ic = [c[0] for c in crisis_list].index(crisis[0]) # get index of crisis
            if not ic in crisis_tracker: # skip events in tracker list
                if crisis[0].is_action_enabled(): #Get the first element of the weighted tuple, the action.
                    possible_crisis_list.append(crisis) #Build a list of valid crises from ones that pass their requirement.

        renpy.random.shuffle(possible_crisis_list)    # shuffle the list in random order

    $ the_crisis = get_random_from_weighted_list(possible_crisis_list)

    if the_crisis:
        #$ mc.log_event("General [[" + str(len(possible_crisis_list)) + "]: " + the_crisis.name, "float_text_grey")
        $ crisis_chance = crisis_base_chance
        $ crisis_tracker.append([c[0] for c in crisis_list].index(the_crisis)) # add crisis index to recent crisis list
        $ the_crisis.call_action()

    $ change_scene_display(mc.location) #Make sure we're showing the correct background for our location, which might have been temporarily changed by a crisis.

    show screen business_ui
    return

label advance_time_mandatory_crisis_label():
    #"advance_time_mandatory_crisis_label" #DEBUG
    python:
        mandatory_crisis_count = 0
        mandatory_crisis_max = len(mc.business.mandatory_crises_list)
        clear_list = []

    while mandatory_crisis_count < mandatory_crisis_max: #We need to keep this in a renpy loop, because a return call will always return to the end of an entire python block.
        $ crisis = mc.business.mandatory_crises_list[mandatory_crisis_count]
        # most mandatory crisis are triggerd from bedroom after sleep button, some are excluded by the bedroom_not_required list
        if crisis.is_action_enabled() and (crisis.effect in bedroom_not_required_labels or mc.location == bedroom):
            $ crisis.call_action()
            $ renpy.scene("Active")
            $ clear_list.append(crisis)
        $ mandatory_crisis_count += 1

    python: #Needs to be a different python block, otherwise the rest of the block is not called when the action returns.
        change_scene_display(mc.location) #Make sure we're showing the correct background for our location, which might have been temporarily changed by a crisis.
        for crisis in clear_list:
            mc.business.mandatory_crises_list.remove(crisis) #Clean up the list.
    return

label advance_time_people_to_process_label():
    #"advance_time_people_to_process_label" #DEBUG
    python:
        people_to_process = [] #This is a master list of turns of need to process, stored as tuples [character,location]. Used to avoid modifying a list while we iterate over it, and to avoid repeat movements.
        for place in list_of_places:
            for people in place.people:
                people_to_process.append([people,place])

    python:
        for (people,place) in people_to_process: #Run the results of people spending their turn in their current location.
            people.run_turn()
        mc.business.run_turn()
        mc.run_turn()
    return

label advance_time_mandatory_morning_crisis_label():
    #"advance_time_mandatory_morning_crisis_label" #DEBUG
    #Now we run mandatory morning crises. Nearly identical to normal crises, but these always trigger at the start of the day (ie when you wake up and before you have control of your character.)
    python:

        mandatory_morning_crisis_count = 0
        mandatory_morning_crisis_max = len(mc.business.mandatory_morning_crises_list)
        clear_list = []

    while mandatory_morning_crisis_count < mandatory_morning_crisis_max: #We need to keep this in a renpy loop, because a return call will always return to the end of an entire python block.
        $crisis = mc.business.mandatory_morning_crises_list[mandatory_morning_crisis_count]
        if crisis.is_action_enabled():
            $ crisis.call_action()
            $ renpy.scene("Active")
            $ clear_list.append(crisis)
        $ mandatory_morning_crisis_count += 1

    python: #Needs to be a different python block, otherwise the rest of the block is not called when the action returns.
        change_scene_display(mc.location) #Make sure we're showing the correct background for our location, which might have been temporarily changed by a crisis.
        for crisis in clear_list:
            mc.business.mandatory_morning_crises_list.remove(crisis) #Clean up the list.
    return

label advance_time_random_morning_crisis_label():
    #"advance_time_random_morning_crisis_label" #DEBUG
    python:
        # how many crisis events are disabled?
        morning_disabled = 0
        for action_mod in action_mod_list:
            if hasattr(action_mod, "is_crisis") and action_mod.is_crisis and not action_mod.enabled:
                if hasattr(action_mod, "is_morning_crisis") and action_mod.is_morning_crisis:
                    morning_disabled += 1

        while len(morning_crisis_tracker) > ((len(morning_crisis_list) - morning_disabled) // 2): # release old tracked events
            del morning_crisis_tracker[0]

        possible_morning_crises = []
        for crisis in morning_crisis_list:
            ic = [c[0] for c in morning_crisis_list].index(crisis[0]) # get index of crisis
            if not ic in morning_crisis_tracker: # skip events in tracker list
                if crisis[0].is_action_enabled(): #Get the first element of the weighted tuple, the action.
                    possible_morning_crises.append(crisis) # Build a list of valid crises from ones that pass their requirement.

        renpy.random.shuffle(possible_morning_crises)    # shuffle the list in random order

    $ the_morning_crisis = get_random_from_weighted_list(possible_morning_crises)

    if the_morning_crisis:
        #$ mc.log_event("Morning: [[" + str(len(possible_morning_crises)) + "] : " +  the_morning_crisis.name, "float_text_grey")
        $ morning_crisis_chance = morning_crisis_base_chance
        $ morning_crisis_tracker.append([c[0] for c in morning_crisis_list].index(the_morning_crisis)) # add crisis index to recent crisis list
        $ the_morning_crisis.call_action()
    return

label advance_time_next_label():
    #"advance_time_next_label" #DEBUG
    if time_of_day == 4: # NOTE: Take care of resetting it to 0 here rather than during end_day_label
        $ time_of_day = 0
    else:
        $ time_of_day += 1 ##Otherwise, just run the end of day code.
    return

label advance_time_daily_serum_dosage_label():
    #"advance_time_daily_serum_dosage_label, hands out daily_serums" #DEBUG
    $ mc.business.give_daily_serum()
    return

label advance_time_people_run_move_label():
    #"advance_time_people_run_move_label" #DEBUG
    python:
        for (people,place) in people_to_process: #Now move everyone to where the should be in the next time chunk. That may be home, work, etc.
            people.run_move(place)
    return
