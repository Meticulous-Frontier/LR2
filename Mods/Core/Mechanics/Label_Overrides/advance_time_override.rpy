# Overrides the default advance time function in the game
# it adds a increased chance for a crisis to occur when more time passed without a crisis
# it adds a way of preventing the same crisis popping up over and over, whilst others never get triggered by remembering a set of occurred events
init -1 python:
    def advance_time_next_requirement():
        return True

    def advance_time_end_of_day_requirement():
        return time_of_day == 0

    def advance_time_random_crisis_requirement():
        if time_of_day == 0:    # slot 0 is for morning crisis events
            return False
        if mandatory_event:
            return False        # already had a mandatory event, so no random event
        return renpy.random.randint(0,100) < crisis_chance

    # only trigger mandatory crisis events in timeslot 4 when in bedroom (actually end of day after pressing sleep button, required for dialog consistency)
    def advance_time_mandatory_crisis_requirement():
        return True

    def advance_time_bankrupt_check_requirement():
        return time_of_day == 4

    def advance_time_mandatory_morning_crisis_requirement():
        return time_of_day == 0

    def advance_time_random_morning_crisis_requirement():
        if time_of_day != 0:
            return False
        if mandatory_event:
            return False        # already had a mandatory event, so no random event
        return renpy.random.randint(0,100) < morning_crisis_chance

    def advance_time_people_run_day_requirement():
        return time_of_day == 4

    def advance_time_people_run_turn_requirement():
        return True

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
    crisis_base_chance = 30
    morning_crisis_base_chance = 15

    crisis_chance = crisis_base_chance
    morning_crisis_chance = morning_crisis_base_chance

    # some crisis events should always trigger (not tracked in crisis tracker and always available when is_action_enabled())
    excluded_crisis_tracker_events = [] # Check for the events existance since they can be found outside of the core files
    excluded_crisis_tracker_events_gc = ["work_relationship_change_crisis", "sister_phone_crisis_action", "mom_selfie_crisis", "late_for_work_action"]
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
        "advance_time_mandatory_morning_crisis_label", priority = 10, category = "Gameplay", allow_disable = False)

    advance_time_random_morning_crisis_action = ActionMod("Run random morning crisis events", advance_time_random_morning_crisis_requirement,
        "advance_time_random_morning_crisis_label", priority = 11, category = "Gameplay")

    # People run move Actions
    advance_time_people_run_move_action = ActionMod("Moves people to their destinations", advance_time_next_requirement,
        "advance_time_people_run_move_label", priority = 8, allow_disable = False)

    advance_time_action_list = [advance_time_people_run_turn_action, advance_time_people_run_day_action, advance_time_end_of_day_action, advance_time_next_action, advance_time_mandatory_crisis_action,
        advance_time_random_crisis_action, advance_time_mandatory_morning_crisis_action, advance_time_random_morning_crisis_action,
        advance_time_people_run_move_action, advance_time_bankrupt_check_action]

    # sort list on execution priority
    advance_time_action_list.sort(key = lambda x: x.priority)

    # actions that trigger events
    advance_time_event_action_list = [advance_time_mandatory_crisis_action, advance_time_random_crisis_action, advance_time_mandatory_morning_crisis_action, advance_time_random_morning_crisis_action]

    config.label_overrides["advance_time"] = "advance_time_enhanced"

    def update_crisis_tracker(active_crisis_list):
        for crisis in [x for x in active_crisis_list if x not in excluded_crisis_tracker_events and not x.effect in crisis_tracker_dict.keys()]:
            crisis_tracker_dict[crisis.effect] = 0
        return

    def get_sorted_active_and_filtered_mandatory_crisis_list(crisis_list):
        has_fetish = False
        active_crisis_list = []
        for crisis in [x for x in sorted(crisis_list, key = lambda x: x.priority, reverse = True) if x.is_action_enabled()]:
            if isinstance(crisis, Fetish_Action):
                if not has_fetish:
                    active_crisis_list.append(crisis)
                    has_fetish = True
            else:
                active_crisis_list.append(crisis)
        return active_crisis_list


    def find_next_crisis(active_crisis_list):
        update_crisis_tracker(active_crisis_list)

        # special handling for unlocking the unisex bathroom quest line faster (last stage should unlock around day 140)
        unisex_level = mc.business.unisex_restroom_unlocks.get("unisex_policy_unlock", 0)
        if unisex_restroom_crisis_requirement() and unisex_level > 0 and unisex_level < 6 and day > 20 + unisex_level * 20:
            crisis = next((x for x in active_crisis_list if x.effect == "unisex_restroom_action_label"), None)
            if crisis:
                return crisis

        # special handling for mall introductions during weekends (prioritize while we have unknown people in the mall)
        if day % 7 in [5, 6] and mall_introduction_requirement():
            crisis = next((x for x in active_crisis_list if x.effect == "mall_introduction_action_label"), None)
            if crisis:
                return crisis

        # append excluded events to list
        active_excluded_events = [x for x in excluded_crisis_tracker_events if x.is_action_enabled()]

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
        # renpy.say(None, "Run Crisis [" + str(__builtin__.len(key_list)) +"]: " + random_crisis)
        if random_crisis in crisis_tracker_dict.keys():
            crisis_tracker_dict[random_crisis] = average + 1     # set to min_value +1 to prevent the event from triggering a lot (its count maybe low due to being disabled)
        return next((x for x in active_crisis_list + active_excluded_events if x.effect == random_crisis), None)

    def get_crisis_from_crisis_list():
        return find_next_crisis([x[0] for x in crisis_list if x[1] > 0 and x[0].is_action_enabled()])

    def get_limited_time_action_for_person(person):
        return get_random_from_weighted_list([x for x in limited_time_event_pool if x[0].is_action_enabled(person)], return_everything = True)

    def get_morning_crisis_from_crisis_list():
        return find_next_crisis([x[0] for x in morning_crisis_list if x[1] > 0 and x[0].is_action_enabled()])

    def build_people_to_process():
        return [[y, x] for x in list_of_places for y in x.people]

    def update_party_schedules(people):
        # exclude unique characters as to not to interfere with story lines
        for person in [x[0] for x in people if not x[0] in unique_character_list]:
            create_party_schedule(person)
        return

    def clear_follow_mc_flag(people):
        for (person, place) in people:
            person.follow_mc = False
        return

    def advance_time_run_turn(people):
        for (person, place) in people: #Run the results of people spending their turn in their current location.
            person.run_turn()

        mc.business.run_turn()
        for project in mc.business.active_IT_projects:
            project.on_turn()
        mc.run_turn()
        if "quest_director" in globals():
            quest_director.run_turn()
        if "perk_system" in globals():
            perk_system.update()  #TEST to see if this is a good time for this.
        return

    def advance_time_run_day(people):
        for (person, place) in people:
            person.run_day()

        mc.run_day()
        mc.business.run_day()
        for project in mc.business.active_IT_projects:
            project.on_day()
        if "quest_director" in globals():
            quest_director.run_day()
        return

    def advance_time_run_move(people):
        renpy.execution.il_time = start_time + 10 # delay the infinite loop detector for 10 seconds
        for (person, place) in people: #Now move everyone to where the should be in the next time chunk. That may be home, work, etc.
            person.run_move(place)

        mc.business.run_move()
        for project in mc.business.active_IT_projects:
            project.on_move()
        return

    def advance_time_assign_limited_time_events(people):
        start_time = time.time()
        for (person, place) in [x for x in people if x[0].title or x[0].mc_title != "Stranger"]:
            if renpy.random.randint(0,100) < 10: #Only assign one to 10% of people, to cut down on the number of people we're checking.
                crisis = get_limited_time_action_for_person(person)
                if crisis:
                    if crisis[2] == "on_talk" and not crisis[0] in [x.the_action for x in person.on_talk_event_list if isinstance(x, Limited_Time_Action)]:
                        person.add_unique_on_talk_event(Limited_Time_Action(crisis[0], crisis[0].event_duration))
                    elif crisis[2] == "on_enter" and not crisis[0] in [x.the_action for x in person.on_room_enter_event_list if isinstance(x, Limited_Time_Action)]:
                        person.add_unique_on_room_enter_event(Limited_Time_Action(crisis[0], crisis[0].event_duration))
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
        #renpy.say(None, "advance_time_enhanced -> location: " + mc.location.name + ", time: [time_of_day]") # DEBUG
        count = 0 # NOTE: Count and Max might need to be unique for each label since it carries over.
        advance_time_max_actions = __builtin__.len(advance_time_action_list) # This list is automatically sorted by priority due to the class properties.
        people_to_process = build_people_to_process()
        clear_follow_mc_flag(people_to_process)
        mandatory_event = False

    while count < advance_time_max_actions:
        if not no_events or (not advance_time_action_list[count] in advance_time_event_action_list):
            if advance_time_action_list[count].is_action_enabled(): # Only run actions that have their requirement met.
                $ start_time = time.time()
                # $ renpy.say(None, "Run: " + advance_time_action_list[count].name)
                call expression advance_time_action_list[count].effect pass (*advance_time_action_list[count].args) from _call_advance_time_action_advance_time_enhanced
                if debug_log_enabled:
                    $ add_to_debug_log("Adv time: " + advance_time_action_list[count].name + " ({total_time:.3f})", start_time)

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
                renpy.say(None,"With no funds to pay your creditors you are forced to close your business and auction off all of your materials at a fraction of their value. Your story ends here.")
                renpy.full_restart()
            else:
                days_remaining = mc.business.max_bankrupt_days-mc.business.bankrupt_days
                renpy.say(None,"Warning! Your company is losing money and unable to pay salaries or purchase necessary supplies! You have [days_remaining] days to restore yourself to positive funds or you will be foreclosed upon!")
        else:
            mc.business.bankrupt_days = 0
    return

label advance_time_random_crisis_label():
    # "advance_time_random_crisis_label - timeslot [time_of_day]" #DEBUG
    $ crisis = get_crisis_from_crisis_list()
    if crisis:
        #$ mc.log_event("General [[" + str(__builtin__.len(possible_crisis_list)) + "]: " + crisis.name, "float_text_grey")
        $ crisis_chance = crisis_base_chance
        call expression crisis.effect pass (*crisis.args) from _call_random_crisis_advance_time
        if _return == "Advance Time":
            $ mandatory_advance_time = True
        if debug_log_enabled:
            $ add_to_debug_log("Random crisis: " + crisis.name)
        $ del crisis
    $ mc.location.show_background()
    show screen business_ui
    return

label advance_time_mandatory_crisis_label():
    # "advance_time_mandatory_crisis_label - timeslot [time_of_day]" #DEBUG
    python:
        active_crisis_list = get_sorted_active_and_filtered_mandatory_crisis_list(mc.business.mandatory_crises_list)
        crisis_count = 0

    while crisis_count < len(active_crisis_list):
        # remove from main list before we trigger
        if active_crisis_list[crisis_count] in mc.business.mandatory_crises_list: # extra check to see if crisis still in list
            $ mc.business.mandatory_crises_list.remove(active_crisis_list[crisis_count]) #Clean up the list.
        call expression active_crisis_list[crisis_count].effect pass (*active_crisis_list[crisis_count].args) from _call_mandatory_crisis_advance_time
        if _return == "Advance Time":
            $ mandatory_advance_time = True
        python:
            if debug_log_enabled:
                add_to_debug_log("Mandatory crisis: " + active_crisis_list[crisis_count].name)
            clear_scene()
            crisis_count += 1
            mandatory_event = True

    python: #Needs to be a different python block, otherwise the rest of the block is not called when the action returns.
        mc.location.show_background()
        del active_crisis_list
        crisis = None
    return

label advance_time_people_run_turn_label():
    # "advance_time_people_run_turn_label - timeslot [time_of_day]" #DEBUG
    python:
        renpy.suspend_rollback(True)
        mandatory_advance_time = False
        advance_time_run_turn(people_to_process)
        renpy.suspend_rollback(False)
    return

label advance_time_people_run_day_label():
    # "advance_time_people_run_day_label - timeslot [time_of_day]" # DEBUG
    python:
        renpy.suspend_rollback(True)
        advance_time_run_day(people_to_process)

        # update party schedules once a week (sunday night)
        if day%7 == 6:
            update_party_schedules(people_to_process)
        renpy.suspend_rollback(False)
    return

label advance_time_end_of_day_label():
    python:
        # we need to clear memory at least once a day (so the texture_cache gets cleared, it will throw an out of memory exception otherwise)
        renpy.free_memory()
        #$ renpy.profile_memory(.5, 1024)
        renpy.block_rollback()

    # "advance_time_end_of_day_label - timeslot [time_of_day]" # DEBUG
    call screen end_of_day_update() # We have to keep this outside of a python block, because the renpy.call_screen function does not properly fade out the text bar.

    python:
        # renpy.restart_interaction()
        mc.business.clear_messages()
        # increase morning crisis chance (once a day)
        morning_crisis_chance += 2

        mc.business.funds_yesterday = mc.business.funds
    return

label advance_time_mandatory_morning_crisis_label():
    # "advance_time_mandatory_morning_crisis_label  - timeslot [time_of_day]" # DEBUG
    #"advance_time_mandatory_morning_crisis_label" #DEBUG
    #Now we run mandatory morning crises. Nearly identical to normal crises, but these always trigger at the start of the day (ie when you wake up and before you have control of your character.)
    python:
        active_crisis_list = get_sorted_active_and_filtered_mandatory_crisis_list(mc.business.mandatory_morning_crises_list)
        crisis_count = 0

    while crisis_count < len(active_crisis_list):
        # remove from main list before we trigger
        if active_crisis_list[crisis_count] in mc.business.mandatory_morning_crises_list:
            $ mc.business.mandatory_morning_crises_list.remove(active_crisis_list[crisis_count]) #Clean up the list.

        call expression active_crisis_list[crisis_count].effect pass (*active_crisis_list[crisis_count].args) from _call_mandatory_morning_crisis_advance_time
        if _return == "Advance Time":
            $ mandatory_advance_time = True
        python:
            if debug_log_enabled:
                add_to_debug_log("Mandatory morning crisis: " + active_crisis_list[crisis_count].name)
            clear_scene()
            crisis_count += 1
            mandatory_event = True

    python: #Needs to be a different python block, otherwise the rest of the block is not called when the action returns.
        mc.location.show_background()
        del active_crisis_list
        crisis = None
    return

label advance_time_random_morning_crisis_label():
    # "advance_time_random_morning_crisis_label  - timeslot [time_of_day]" #DEBUG
    $ crisis = get_morning_crisis_from_crisis_list()
    if crisis:
        $ start_time = time.time()
        #$ mc.log_event("Morning: [[" + str(__builtin__.len(possible_morning_crises_list)) + "] : " +  crisis.name, "float_text_grey")
        $ morning_crisis_chance = morning_crisis_base_chance
        call expression crisis.effect pass (*crisis.args) from _call_random_morning_crisis_advance_time
        if _return == "Advance Time":
            $ mandatory_advance_time = True
        if debug_log_enabled:
            $ add_to_debug_log("Random morning crisis: " + crisis.name)
        $ del crisis
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

label advance_time_people_run_move_label():
    python:
        renpy.suspend_rollback(True)
        # "advance_time_people_run_move_label - timeslot [time_of_day]" #DEBUG
        advance_time_run_move(people_to_process)
        advance_time_assign_limited_time_events(people_to_process)
        renpy.suspend_rollback(False)
    return
