# Overrides the default advance time function in the game
# it adds a increased chance for a crisis to occur when more time passed without a crisis
# it adds a way of preventing the same crisis popping up over and over, whilst others never get triggered by remembering a set of occurred events
init -1 python:
    import gc

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
        return time_of_day == 1 and daily_serum_dosage_policy.is_active() and mc.business.is_work_day() # This runs if you have the corresponding policy

    def advance_time_people_run_day_requirement():
        return time_of_day == 4

    def advance_time_people_run_turn_requirement():
        return True

    def advance_time_stay_wet_requirement():
        return stay_wet_action.enabled

    def advance_time_collar_person_requirement():
        return collar_slave_action.enabled

    def advance_time_mandatory_vibe_action_requirement():
        # Only run while employees are at work.
        if mc.business.is_open_for_business():
            return mandatory_vibe_policy.is_active()
        return False

    def jump_game_loop():
        # make sure we empty the call stack before jumping to main loop
        while renpy.call_stack_depth() > 1:
            renpy.pop_call()
        renpy.jump("game_loop")

init 5 python:
    global crisis_chance
    global morning_crisis_chance

    global crisis_base_chance
    global morning_crisis_base_chance

    # some crisis events have impact on game dynamic and should be allowed to trigger often
    crisis_base_chance = 20
    morning_crisis_base_chance = 10

    crisis_chance = crisis_base_chance
    morning_crisis_chance = morning_crisis_base_chance

    # some crisis events should always trigger (not tracked in crisis tracker and always available when is_action_enabled())
    excluded_crisis_tracker_events = [] # Check for the events existance since they can be found outside of the core files
    excluded_crisis_tracker_events_gc = ["work_relationship_change_crisis", "sister_phone_crisis_action", "mom_selfie_crisis", "late_for_work_action", "cousin_tease_crisis"]
    for crisis in excluded_crisis_tracker_events_gc:
        if crisis in globals():
            excluded_crisis_tracker_events.append(globals()[crisis])

    mandatory_advance_time = False

    advance_time_people_run_turn_action = ActionMod("Run people turn", advance_time_people_run_turn_requirement,
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

    advance_time_people_run_move_action = ActionMod("Moves people to their destinations", advance_time_next_requirement,
        "advance_time_people_run_move_label", priority = 15, allow_disable = False)

    # Slave Role Advance Time Actions
    advance_time_stay_wet_action = ActionMod("Execute slave 'stay wet'", advance_time_stay_wet_requirement,
        "advance_time_stay_wet_label", priority = 20, allow_disable = False, menu_tooltip = "People with 'stay_wet = True' have their minimum arousal set to 50%")

    advance_time_collar_person_action = ActionMod("Execute slave 'collar'", advance_time_collar_person_requirement,
        "advance_time_collar_person_label", allow_disable = False, priority = 22, menu_tooltip = "Allows the collar_slave_action to do what it is intended to.")

    # Mandatory Vibe Company Action
    advance_time_mandatory_vibe_company_action = ActionMod("Attach vibes to outfits", advance_time_mandatory_vibe_action_requirement,
        "advance_time_mandatory_vibe_company_label", priority = 2, enabled = False, allow_disable = False, category = "Business")

    advance_time_action_list = [advance_time_people_run_turn_action, advance_time_people_run_day_action, advance_time_end_of_day_action, advance_time_next_action, advance_time_mandatory_crisis_action,
        advance_time_random_crisis_action, advance_time_mandatory_morning_crisis_action, advance_time_random_morning_crisis_action, advance_time_daily_serum_dosage_action,
        advance_time_people_run_move_action, advance_time_bankrupt_check_action, advance_time_mandatory_vibe_company_action]

    if "slave_role" in globals():
        if advance_time_stay_wet_action not in advance_time_action_list:
            advance_time_action_list.append(advance_time_stay_wet_action)
        if advance_time_collar_person_action not in advance_time_action_list:
            advance_time_action_list.append(advance_time_collar_person_action)

    # sort list on execution priority
    advance_time_action_list.sort(key = lambda x: x.priority)

    # actions that trigger events
    advance_time_event_action_list = [advance_time_mandatory_crisis_action, advance_time_random_crisis_action, advance_time_mandatory_morning_crisis_action, advance_time_random_morning_crisis_action]

    config.label_overrides["advance_time"] = "advance_time_enhanced"

    def update_crisis_tracker(active_crisis_list):
        for crisis in [x for x in active_crisis_list if x not in excluded_crisis_tracker_events]:
            if not (crisis.effect in crisis_tracker_dict.keys()):
                crisis_tracker_dict[crisis.effect] = 0
        return

    def find_next_crisis(active_crisis_list):
        update_crisis_tracker(active_crisis_list)

        # append excluded events to list
        active_excluded_events = []
        for ex_crisis in excluded_crisis_tracker_events:
            if ex_crisis.is_action_enabled():
                active_excluded_events.append(ex_crisis)

        # get active events from crisis_tracker_dict (only those with lowest counter)
        tracker_info = { key:value for (key,value) in crisis_tracker_dict.items() if key in [x.effect for x in active_crisis_list] }
        key_list = [] # sometimes tracker_info is empty, to prevent error only choose from active_excluded_events
        if tracker_info.items():
            min_value = __builtin__.min(tracker_info.items(), key=lambda x: x[1])[1]
            average = __builtin__.int(__builtin__.sum(x[1] for x in tracker_info.items())/len(tracker_info.items()))
            key_list = [key for (key, value) in tracker_info.items() if value == min_value]

        # add active events from exclusion list to possible events list
        if __builtin__.len(key_list) == 0 or __builtin__.len(key_list) > __builtin__.len(active_excluded_events):
            # when the key_list is getting smaller we are exhausting the possible crisis events
            # if we keep adding the excluded items, they will start to occur more and more frequent (>50%)
            # so we don't add them anymore, until we are back to a more comprehensive list of events
            key_list.extend([x.effect for x in active_excluded_events])

        random_crisis = get_random_from_list(key_list)
        # renpy.say("", "Run Crisis [" + str(__builtin__.len(key_list)) +"]: " + random_crisis)
        if random_crisis in crisis_tracker_dict.keys():
            crisis_tracker_dict[random_crisis] = average + 1     # set to min_value +1 to prevent the event from triggering a lot (its count maybe low due to being disabled)
        return find_in_list(lambda x: x.effect == random_crisis, active_crisis_list + active_excluded_events)

    def get_crisis_from_crisis_list():
        possible_crisis_list = []
        for crisis in crisis_list:
            if crisis[1] > 0 and crisis[0].is_action_enabled(): #Get the first element of the weighted tuple, the action.
                possible_crisis_list.append(crisis[0]) #Build a list of valid crises from ones that pass their requirement.

        return find_next_crisis(possible_crisis_list)
        #renpy.say("", str(__builtin__.len(possible_crisis_list)) + " - ".join((o[0].name) for o in possible_crisis_list))

        #return get_random_from_weighted_list(possible_crisis_list)

    def get_limited_time_action_for_person(person):
        possible_crisis_list = []
        for crisis in limited_time_event_pool:
            if crisis[0].is_action_enabled(person): #Get the first element of the weighted tuple, the action.
                possible_crisis_list.append(crisis) #Build a list of valid crises from ones that pass their requirement.
        #renpy.random.shuffle(possible_crisis_list)    # shuffle the list in random order
        return get_random_from_weighted_list(possible_crisis_list, return_everything = True)


    def get_morning_crisis_from_crisis_list():
        possible_morning_crises_list = []
        for crisis in morning_crisis_list:
            if crisis[1] > 0 and crisis[0].is_action_enabled(): #Get the first element of the weighted tuple, the action.
                possible_morning_crises_list.append(crisis[0]) # Build a list of valid crises from ones that pass their requirement.

        return find_next_crisis(possible_morning_crises_list)
        #renpy.random.shuffle(possible_morning_crises_list)    # shuffle the list in random order
        #return get_random_from_weighted_list(possible_morning_crises_list)

    def build_people_to_process():
        people = [] #This is a master list of turns of need to process, stored as tuples [character,location]. Used to avoid modifying a list while we iterate over it, and to avoid repeat movements.
        for place in list_of_places:
            for person in place.people:
                people.append([person, place])
        return people

    def update_party_schedules(people):
        for (person, place) in people:
            if not person in unique_character_list: # exclude unique characters as to not to interfere with story lines
                create_party_schedule(person)
        return

    def advance_time_run_turn(people):
        for (person, place) in people: #Run the results of people spending their turn in their current location.
            person.run_turn()
        mc.business.run_turn()
        mc.run_turn()
        if "quest_director" in globals():
            quest_director.run_turn()
        return

    def advance_time_run_day(people):
        for (person, place) in people:
            person.run_day()

        mc.run_day()
        mc.business.run_day()
        if "quest_director" in globals():
            quest_director.run_day()
        return

    def advance_time_run_move(people):
        for (person, place) in people: #Now move everyone to where the should be in the next time chunk. That may be home, work, etc.
            person.run_move(place)
            if person.follow_mc: # move follower to mc location
                person.location().move_person(person, mc.location)
        return

    def advance_time_assign_limited_time_events(people):
        for (person, place) in people:
            if person.mc_title != "Stranger" and renpy.random.randint(0,100) < 12: #Only assign one to 12% of people, to cut down on the number of people we're checking.
                crisis = get_limited_time_action_for_person(person)
                if crisis:
                    #renpy.notify("Created event: " + crisis[0].name + " for " + people.name)
                    if crisis[2] == "on_talk" and __builtin__.len(person.on_talk_event_list) == 0: # prevent multiple on talk events for person
                        person.add_unique_on_talk_event(Limited_Time_Action(crisis[0], crisis[0].event_duration))
                    elif crisis[2] == "on_enter":
                        if not exists_in_room_enter_list(person, crisis[0].effect): # prevent adding the same event twice
                            person.add_unique_on_room_enter_event(Limited_Time_Action(crisis[0], crisis[0].event_duration))
        return

    def advance_time_slave_stay_wet(people):
        for (person, place) in [x for x in people if x[0].stay_wet and x[0].arousal < 50]:
            person.arousal = 50
        return

    def advance_time_slave_collar(people):
        for (person,place) in [x for x in people if x[0].slave_collar and x[0].obedience < 130]:
            person.obedience = 130
        return

    def advance_time_mandatory_vibe():
        if mc.business.is_open_for_business():
            for person in [x for x in mc.business.get_employee_list() if x.arousal < 30]:
                person.arousal = 30
        return

label advance_time_move_to_next_day(no_events = True):
    $ current_day = day
    while day == current_day:
        call advance_time_enhanced(no_events = no_events, jump_to_game_loop = False) from _call_advance_time_advance_time_move_to_next_day
    return

label advance_time_enhanced(no_events = False, jump_to_game_loop = True):
    # 1) Turns are processed _before_ the time is advanced.
    # 1a) crises are processed if they are triggered.
    # 2) Time is advanced, day is advanced if required.
    # 3) People go to their next intended location.
    # Note: This will require breaking people's turns into movement and actions.
    # Then: Add research crisis when serum is finished, requiring additional input from the player and giving the chance to test a serum on the R&D staff.

    python:
        #renpy.say("", "advance_time_enhanced -> location: " + mc.location.name + ", time: [time_of_day]") # DEBUG
        count = 0 # NOTE: Count and Max might need to be unique for each label since it carries over.
        advance_time_max_actions = __builtin__.len(advance_time_action_list) # This list is automatically sorted by priority due to the class properties.
        people_to_process = build_people_to_process()

    while count < advance_time_max_actions:
        if not no_events or (not advance_time_action_list[count] in advance_time_event_action_list):
            if advance_time_action_list[count].is_action_enabled(): # Only run actions that have their requirement met.
                # $ renpy.say("", "Run: " + act.name)
                $ advance_time_action_list[count].call_action()
                $ clear_scene()

        $ count += 1

    python:
        # increase crisis chance (every time slot)
        crisis_chance += 1
        mc.location.show_background()
        x = None
        c = None
        people_to_process = []
        person = None
        # save game
        if time_of_day == 0:
            renpy.force_autosave(take_screenshot = True, block = False)

    if mandatory_advance_time and not time_of_day == 4: #If a crisis has told us to advance time after it we do so (not when night to prevent spending night at current location).
        call advance_time from _call_advance_time_advance_time_enhanced
    if no_events or not jump_to_game_loop:
        return

    $ jump_game_loop()
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
    $ crisis = get_crisis_from_crisis_list()
    if crisis:
        #$ mc.log_event("General [[" + str(__builtin__.len(possible_crisis_list)) + "]: " + crisis.name, "float_text_grey")
        $ crisis_chance = crisis_base_chance
        $ crisis.call_action()
        if _return == "Advance Time":
            $ mandatory_advance_time = True
        $ del crisis
    $ mc.location.show_background()
    show screen business_ui
    return

label advance_time_mandatory_crisis_label():
    # "advance_time_mandatory_crisis_label - timeslot [time_of_day]" #DEBUG
    python:
        mandatory_crisis_count = 0
        mandatory_crisis_max = __builtin__.len(mc.business.mandatory_crises_list)
        clear_list = []

    while mandatory_crisis_count < mandatory_crisis_max: #We need to keep this in a renpy loop, because a return call will always return to the end of an entire python block.
        if mandatory_crisis_count < __builtin__.len(mc.business.mandatory_crises_list): # extra check to make sure index still exists
            $ crisis = mc.business.mandatory_crises_list[mandatory_crisis_count]
            if crisis.is_action_enabled():
                $ crisis.call_action()
                if _return == "Advance Time":
                    $ mandatory_advance_time = True
                $ clear_scene()
                $ clear_list.append(crisis)
            $ del crisis
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
        advance_time_run_turn(people_to_process)
    return

label advance_time_people_run_day_label():
    # "advance_time_people_run_day_label - timeslot [time_of_day]" # DEBUG
    #if time_of_day == 4: ##First, determine if we're going into the next chunk of time. If we are, advance the day and run all of the end of day code. NOTE: We can do checks like these with Action.requirements
    $ advance_time_run_day(people_to_process)
    # we need to clear memory at least once a week (so the texture_cache gets cleared, it will throw an out of memory exception otherwise)
    # we clear the memory every day when not using high memory mode regardless of setting.
    if persistent.use_free_memory or persistent.memory_mode < 2 or day%7 == 6:
        $ renpy.free_memory()
    $ gc.collect()
    #$ renpy.profile_memory(.5, 1024)
    $ renpy.block_rollback()

    # update party schedules once a week (sunday night)
    if day%7 == 6:
        $ update_party_schedules(people_to_process)
    return

label advance_time_end_of_day_label():
    # "advance_time_end_of_day_label - timeslot [time_of_day]" # DEBUG
    call screen end_of_day_update() # We have to keep this outside of a python block, because the renpy.call_screen function does not properly fade out the text bar.

    python:
        mc.business.clear_messages()
        # increase morning crisis chance (once a day)
        morning_crisis_chance += 2
        if "perk_system" in globals():
            perk_system.update()  #TEST to see if this is a good time for this.
        mc.business.funds_yesterday = mc.business.funds
    return

label advance_time_mandatory_morning_crisis_label():
    # "advance_time_mandatory_morning_crisis_label  - timeslot [time_of_day]" # DEBUG
    #"advance_time_mandatory_morning_crisis_label" #DEBUG
    #Now we run mandatory morning crises. Nearly identical to normal crises, but these always trigger at the start of the day (ie when you wake up and before you have control of your character.)
    python:
        mandatory_morning_crisis_count = 0
        mandatory_morning_crisis_max = __builtin__.len(mc.business.mandatory_morning_crises_list)
        clear_list = []

    while mandatory_morning_crisis_count < mandatory_morning_crisis_max: #We need to keep this in a renpy loop, because a return call will always return to the end of an entire python block.
        $ crisis = mc.business.mandatory_morning_crises_list[mandatory_morning_crisis_count]
        if crisis.is_action_enabled():
            $ crisis.call_action()
            if _return == "Advance Time":
                $ mandatory_advance_time = True
            $ clear_scene()
            $ clear_list.append(crisis)
        $ mandatory_morning_crisis_count += 1
        $ del crisis

    python: #Needs to be a different python block, otherwise the rest of the block is not called when the action returns.
        mc.location.show_background()
        for crisis in clear_list:
            mc.business.mandatory_morning_crises_list.remove(crisis) #Clean up the list.

        del clear_list
    return

label advance_time_random_morning_crisis_label():
    # "advance_time_random_morning_crisis_label  - timeslot [time_of_day]" #DEBUG
    $ the_morning_crisis = get_morning_crisis_from_crisis_list()
    if the_morning_crisis:
        #$ mc.log_event("Morning: [[" + str(__builtin__.len(possible_morning_crises_list)) + "] : " +  the_morning_crisis.name, "float_text_grey")
        $ morning_crisis_chance = morning_crisis_base_chance
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
    $ advance_time_run_move(people_to_process)
    $ advance_time_assign_limited_time_events(people_to_process)
    return

label advance_time_stay_wet_label():
    $ advance_time_slave_stay_wet(people_to_process)
    return

label advance_time_collar_person_label():
    $ advance_time_slave_collar(people_to_process)
    return

label advance_time_mandatory_vibe_company_label():
    $ advance_time_mandatory_vibe()
    return
