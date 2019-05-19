# Overrides the default advance time function in the game
# it adds a increased chance for a crisis to occur when more time passed without a crisis
# it adds a way of preventing the same crisis popping up over and over, whilst others never get triggered by remembering a set of occured events
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

    config.label_overrides["advance_time"] = "advance_time_enhanced"

label advance_time_enhanced:
    # 1) Turns are processed _before_ the time is advanced.
    # 1a) crises are processed if they are triggered.
    # 2) Time is advanced, day is advanced if required.
    # 3) People go to their next intended location.
    # Note: This will require breaking people's turns into movement and actions.
    # Then: Add research crisis when serum is finished, requiring additional input from the player and giving the chance to test a serum on the R&D staff.

    $ mc.can_skip_time = False #Ensure the player cannot skip time during crises.

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

    $ count = 0
    $ max = len(mc.business.mandatory_crises_list)
    $ clear_list = []
    while count < max: #We need to keep this in a renpy loop, because a return call will always return to the end of an entire python block.
        $crisis = mc.business.mandatory_crises_list[count]
        if crisis.is_action_enabled():
            $ crisis.call_action()
            $ renpy.scene("Active")
            $ clear_list.append(crisis)
        $ count += 1

    $ renpy.show(mc.location.name,what=mc.location.background_image) #Make sure we're showing the correct background for our location, which might have been temporarily changed by a crisis.

    python: #Needs to be a different python block, otherwise the rest of the block is not called when the action returns.
        for crisis in clear_list:
            mc.business.mandatory_crises_list.remove(crisis) #Clean up the list.

    if renpy.random.randint(0,100) < crisis_chance: #ie. run crisis at set chance.
        python:
            while len(crisis_tracker) > (len(crisis_list) // 3): # release old tracked events
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
    else:
        $ crisis_chance += 1    # increase chance when no event occurred

    $ renpy.scene("Active")
    $ renpy.scene()
    $ renpy.show(mc.location.name,what=mc.location.background_image) #Make sure we're showing the correct background for our location, which might have been temporarily changed by a crisis.
    hide screen person_info_ui
    show screen business_ui

    if time_of_day == 4: ##First, determine if we're going into the next chunk of time. If we are, advance the day and run all of the end of day code.
        python:
            for (people,place) in people_to_process:
                people.run_day()

        $ mc.run_day()
        $ mc.business.run_day()

        $ time_of_day = 0
        $ day += 1

        if mc.business.funds < 0:
            $ mc.business.bankrupt_days += 1
            if mc.business.bankrupt_days == mc.business.max_bankrupt_days:
                $ renpy.say("","With no funds to pay your creditors you are forced to close your business and auction off all of your materials at a fraction of their value. Your story ends here.")
                $ renpy.full_restart()
            else:
                $ days_remaining = mc.business.max_bankrupt_days-mc.business.bankrupt_days
                $ renpy.say("","Warning! Your company is losing money and unable to pay salaries or purchase necessary supplies! You have [days_remaining] days to restore yourself to positive funds or you will be foreclosed upon!")
        else:
            $ mc.business.bankrupt_days = 0

        call screen end_of_day_update() # We have to keep this outside of a python block, because the renpy.call_screen function does not properly fade out the text bar.
        $ mc.business.clear_messages()

        if renpy.random.randint(0,100) < morning_crisis_chance: #ie. run crisis at set chance.
            python:
                while len(morning_crisis_tracker) > (len(morning_crisis_list) // 2): # release old tracked events
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
        else:
            $ morning_crisis_chance += 2    # increase chance when no event occurred

    else:
        $ time_of_day += 1 ##Otherwise, just run the end of day code.

    if time_of_day == 1 and daily_serum_dosage_policy.is_owned(): #It is the start of the work day, give everyone their daily dose of serum
        $ mc.business.give_daily_serum()

    python:
        for (people,place) in people_to_process: #Now move everyone to where the should be in the next time chunk. That may be home, work, etc.
            people.run_move(place)

    $ mc.can_skip_time = True #Now give the player the ability to skip time again, because they should be back in control.
    return    