# Fix for sex mechanic for people who don't have the bugfix branch installed
# Enhancement for pick object (don't show list when only one object can be selected (auto-select it))
# Added condom ask enhancements (Original by BadRabbit)

init 5 python:
    config.label_overrides["fuck_person"] = "fuck_person_bugfix"
    config.label_overrides["check_position_willingness"] = "check_position_willingness_bugfix"
    config.label_overrides["watcher_check"] = "watcher_check_enhanced"
    config.label_overrides["condom_ask"] = "condom_ask_enhanced"
    config.label_overrides["pick_position"] = "pick_position_enhanced"
    config.label_overrides["girl_strip_event"] = "girl_strip_event_enhanced"

    record_opinion_map = {
        "Handjobs" : ["giving handjobs", "sex standing up"],
        "Kissing" : ["kissing"],
        "Fingered" : ["masturbating", "being fingered", "sex standing up"],
        "Tit Fucks" : ["giving tit fucks", "showing her tits"],
        "Blowjobs" : ["giving blowjobs"],
        "Cunnilingus": ["getting head"],
        "Vaginal Sex": ["vaginal sex", "missionary style sex", "lingerie"],
        "Anal Sex": ["anal sex", "doggy style sex", "bareback sex"],
        "Cum Facials": ["cum facials"],
        "Cum in Mouth": ["drinking cum"],
        "Cum Covered": ["being covered in cum"],
        "Vaginal Creampies": ["creampies"],
        "Anal Creampies": ["anal creampies"],
        "Threesomes": ["not wearing anything", "skimpy outfits", "skimpy uniforms"],
        "Spanking": ["not wearing underwear", "showing her ass"],
        "Insertions": ["big dicks", "public sex"],
    }

    record_skill_map = {
        "Kissing" : "Foreplay",
        "Tit Fucks" : "Foreplay",
        "Blowjobs" : "Oral",
        "Cunnilingus": "Oral",
        "Vaginal Sex": "Vaginal",
        "Anal Sex": "Anal",
    }

    def girl_choose_position_enhanced(person, ignore_taboo = False):
        position_option_list = []
        extra_positions = []
        # when she enjoys blow jobs, add one to her choices (to prevent always going to blowjob variant)
        if person.sex_skills["Oral"] >= 5 and person.get_opinion_score("giving blowjobs") > 1 and person.get_opinion_score("being submissive") > 1:
            extra_positions.append(skull_fuck)
        elif person.sex_skills["Oral"] > 3 and person.get_opinion_score("giving blowjobs") > 1:
            extra_positions.append(deepthroat)
        elif person.sex_skills["Oral"] > 2 and person.get_opinion_score("giving blowjobs") > 0:
            extra_positions.append(blowjob)

        # when she enjoys tit fucks, add it to her position choices
        if person.sex_skills["Foreplay"] > 2 and person.get_opinion_score("giving tit fucks") > 1:
            extra_positions.append(tit_fuck)

        for position in list_of_girl_positions + extra_positions:
            if allow_position(person, position) and mc.location.has_object_with_trait(position.requires_location) and (person.has_large_tits() or not position.requires_large_tits): #There is a valid object and if it requires large tits she has them.
                if position.her_position_willingness_check(person, ignore_taboo = ignore_taboo):
                    position_option_list.append([position, person.sex_skills[position.skill_tag]])

        return get_random_from_weighted_list(position_option_list)

    def girl_choose_object_enhanced(person, position):
        possible_object_list = []
        if position is None:
            person.clear_situational_slut("sex_object")
            person.clear_situational_obedience("sex_object")
            return None

        for an_object in mc.location.objects_with_trait(position.requires_location):
            possible_object_list.append(an_object)

        picked_object = get_random_from_list(possible_object_list)

        person.add_situational_slut("sex_object", picked_object.sluttiness_modifier, picked_object.name + " " + position.verbing)
        person.add_situational_obedience("sex_object",picked_object.obedience_modifier, picked_object.name + " " + position.verbing)
        return picked_object

    def cheating_check_get_watcher(person):
        other_people = [a_person for a_person in mc.location.people if a_person is not person] #Build a list with all the _other_ people in the room other than the one we're fucking.
        for a_person in other_people:
            if a_person.has_role(girlfriend_role) and the_position.slut_requirement > (a_person.sluttiness/2): #You can get away with stuff half as slutty as she would do
                caught_cheating_action = Action("Caught cheating action", caught_cheating_requirement, "caught_cheating_label", args = person)
                if not exists_in_room_enter_list(a_person, "caught_cheating_label"):
                    a_person.add_unique_on_room_enter_event(caught_cheating_action)
                    renpy.say("",a_person.title + " gasps when she sees what you and " + person.title + " are doing.")

            elif a_person.has_role(affair_role) and the_position.slut_requirement > ((a_person.sluttiness*2)/3): #You can get away with stuff two thirds as slutty as what she would do.
                caught_affair_cheating_action = Action("Caught affair cheating action", caught_affair_cheating_requirement, "caught_affair_cheating_label", args = person)
                if not exists_in_room_enter_list(a_person, "caught_affair_cheating_label"):
                    a_person.add_unique_on_room_enter_event(caught_affair_cheating_action)
                    renpy.say("",a_person.title + " gasps when she sees what you and " + person.title + " are doing.")

        return get_random_from_list(other_people) #Get a random person from the people in the area, if there are any.

    def apply_sex_modifiers(person):
        #Family situational modifiers
        if person.has_family_taboo(): #Check if any of the roles the person has belong to the list of family roles.
            person.add_situational_slut("taboo_sex", -20, "We're related, we shouldn't be doing this.")

        #Cheating modifiers
        person.discover_opinion("cheating on men")
        if person.has_role(prostitute_role):
            person.add_situational_slut("cheating", 20, "Prostitutes don't care about cheating")
        elif person.relationship == "Girlfriend":
            if person.get_opinion_score("cheating on men") > 0:
                person.add_situational_slut("cheating", person.get_opinion_score("cheating on men") * 5, "I'm cheating on my boyfriend!")
            else:
                person.add_situational_slut("cheating", -5 + (person.get_opinion_score("cheating on men") * -10), "I can't cheat on my boyfriend!")
        elif person.relationship == "Fiancée":
            if person.get_opinion_score("cheating on men") > 0:
                person.add_situational_slut("cheating", person.get_opinion_score("cheating on men") * 8, "I'm cheating on my fiancé!")
            else:
                person.add_situational_slut("cheating", -15 + (person.get_opinion_score("cheating on men") * -15), "I could never cheat on my fiancé!")
        elif person.relationship == "Married":
            if person.get_opinion_score("cheating on men") > 0:
                person.add_situational_slut("cheating", person.get_opinion_score("cheating on men") * 10, "I'm cheating on my husband!")
            else:
                person.add_situational_slut("cheating", -20 + (person.get_opinion_score("cheating on men") * -20), "I could never cheat on my husband!")

        #Privacy modifiers
        if not private:
            if person.effective_sluttiness() < 50:
                person.add_situational_slut("public_sex", -10 + person.get_opinion_score("public sex") * 5, "There are people watching...")
            else:
                person.add_situational_slut("public_sex", person.get_opinion_score("public sex") * 5, "There are people watching!")

        #Love modifiers. Always applies if negative, but only adds a bonus if you are in private.
        if person.love < 0:
            person.add_situational_slut("love_modifier", person.love, "I hate you, get away from me!")
        elif private:
            if person.has_role(girlfriend_role): #Girlfriend and affairs gain full Love
                person.add_situational_slut("love_modifier", person.love, "You're my special someone, I love you!")
            elif person.has_role(affair_role):
                person.add_situational_slut("love_modifier", person.love, "I have kept it a secret, but I love you!")
            elif person.has_family_taboo(): #Family now only gains 1/4 (but this now helps offset the taboo penalty)
                if person.has_role(mother_role):
                    person.add_situational_slut("love_modifier", __builtin__.int(person.love/4), "Even if it's wrong, a mother should do everything she can for her son!")
                elif person.has_role(sister_role):
                    person.add_situational_slut("love_modifier", __builtin__.int(person.love/4), "I love my brother, and even if it's wrong I want to be close to him!")
                else: #Generic family one
                    person.add_situational_slut("love_modifier", __builtin__.int(person.love/4), "I love you, even though we're related!")
            else: #If you aren't in a relationship with them only half their Love applies.
                person.add_situational_slut("love_modifier", __builtin__.int(person.love/2), "I really like you, let's see where this goes!")

        # Happiness modifiers
        happiness_effect = __builtin__.round((person.happiness - 100)/4.0)
        if happiness_effect <= -10:
            person.add_situational_slut("happiness_modifier", happiness_effect, "I'm so unhappy, I just don't want to do anything!")
        elif happiness_effect <= -5:
            person.add_situational_slut("happiness_modifier", happiness_effect, "I'm just not in the mood right now.")
        elif happiness_effect >= 5:
            person.add_situational_slut("happiness_modifier", happiness_effect, "I'm so happy, I'm up for anything!")
        elif happiness_effect >= 10:
            person.add_situational_slut("happiness_modifier", happiness_effect, "Today's a good day, let's see where this goes!")
        return

    def clear_sex_modifiers(person):
        # Teardown the sex modifiers
        person.clear_situational_slut("happiness_modifier")
        person.clear_situational_slut("love_modifier")
        person.clear_situational_slut("public_sex")
        person.clear_situational_slut("cheating")
        person.clear_situational_slut("taboo_sex")
        person.clear_situational_slut("sex_object")
        person.clear_situational_obedience("sex_object")
        return

    def allow_position(person, position):
        if position.opinion_tags:
            for opinion in position.opinion_tags:
                if person.get_opinion_score(opinion) == -2:
                    if person.has_role(slave_role) and person.obedience > 200: #A slave does what she is told.
                        return True
                    return False
        return True

    def update_person_sex_record(person, report_log):
        types_seen = []
        for position_type in report_log.get("positions_used",[]): #Note: Clears out duplicates
            if position_type.record_class and position_type.record_class not in types_seen:
                if not position_type.record_class in person.sex_record: # add missing sex_record key
                    person.sex_record[position_type.record_class] = 0
                person.sex_record[position_type.record_class] += 1
                types_seen.append(position_type.record_class)

        # enables slow corruption based on sex type (each category has a chance to increase sex stats / opinions)
        # also higher suggestibility has a higher chance of increasing the stats to a higher level
        tier = get_suggest_tier(person)
        gained_skill = False    # only one skill per session
        gained_opinion = False  # only one opinion per session
        renpy.random.shuffle(types_seen) # shuffle types seen so we don't know what skills and opinions are checked for increment first
        for record_class in types_seen:
            if not gained_skill and record_class in record_skill_map and renpy.random.randint(0,100) < 5 + (tier * 5):
                person.increase_sex_skill(record_skill_map[record_class], 2 + tier)
                gained_skill = True
            if not gained_opinion and record_class in record_opinion_map and renpy.random.randint(0,100) < 15 + (tier * 5):
                person.increase_opinion_score(get_random_from_list(record_opinion_map[record_class]), tier - 1)
                gained_opinion = True

        # record the last time we had sex
        person.sex_record["Last Sex Day"] = day
        return

    def pick_object_enhanced(person, position, forced_object = None):
        if position is None:
            person.clear_situational_slut("sex_object")
            person.clear_situational_obedience("sex_object")
            return None

        if forced_object:
            picked_object = forced_object
        else:
            object_option_list = []
            for loc_object in mc.location.objects:
                if loc_object.has_trait(position_choice.requires_location):
                    object_option_list.append([loc_object.get_formatted_name(), loc_object]) #Displays a list of objects in the room related to that position and their appropriate bonuses/penalties

            # if we have only one object to pick for position, select it automatically (saves the user for selecting the only obvious choice)
            if __builtin__.len(object_option_list) == 1:
                picked_object = object_option_list[0][1]
            else:
                picked_object = renpy.display_menu(object_option_list,True,"Choice")

        person.add_situational_slut("sex_object", picked_object.sluttiness_modifier, picked_object.name + " " + position.verbing)
        person.add_situational_obedience("sex_object",picked_object.obedience_modifier, picked_object.name + " " + position.verbing)
        return picked_object

    def build_round_choice_menu(person, position_choice, position_locked, object_choice, ignore_taboo = False):
        option_list = []
        option_list.append("Round Choices")
        if position_choice is not None:
            option_list.append(["Keep " + position_choice.verbing + " her","Continue"]) #NOTE: you're prevented from continuing if the energy cost would be too high by the pre-round checks.

            if not position_locked and object_choice:
                option_list.append(["Pause and change position\n-5 {image=arousal_token_small}","Change"])
                for position in position_choice.connections:
                    if allow_position(person, position) and object_choice.has_trait(position.requires_location):
                        appended_name = "Transition to " + position.build_position_willingness_string(person, ignore_taboo = ignore_taboo) #NOTE: clothing and energy checks are done inside of build_position_willingness, invalid position marked (disabled)
                        option_list.append([appended_name,position])

            if position_locked and object_choice:
                # allow transition to positions with same traits and skill requirements
                for position in position_choice.connections:
                    if isinstance(object_choice, Object): # Had an error with cousin's kissing blackmail where it would pass object_choice as a list, haven't looked further into it
                        if allow_position(person, position) and object_choice.has_trait(position.requires_location) and position_choice.skill_tag == position.skill_tag:
                            appended_name = "Transition to " + position.build_position_willingness_string(person, ignore_taboo = ignore_taboo) #NOTE: clothing and energy checks are done inside of build_position_willingness, invalid position marked (disabled)
                            option_list.append([appended_name, position])
            if not person.outfit.full_access():
                option_list.append(["Pause and strip her down","Strip"])

            if not hide_leave: #TODO: Double check that we can always get out
                option_list.append(["Stop " + position_choice.verbing + " her and leave", "Leave"]) #TODO: Have this appear differently depending on if you've cum yet, she's cum yet, or you've both cum.

        else:
            if not position_locked:
                option_list.append(["Pick a new position\n-5 {image=arousal_token_small}","Change"])
                if not person.outfit.full_access(): # only show strip option if we can choose another position
                    option_list.append(["Pause and strip her down","Strip"])
            if not hide_leave:
                option_list.append(["Stop and leave", "Leave"])
        return option_list

    def build_grouped_sex_position_menu(person, allow_none = True, ignore_taboo = False, prohibit_tags = []):
        positions = {
            "Foreplay" : ["Pick Foreplay"],
            "Oral" : ["Pick Oral"],
            "Vaginal" : ["Pick Vaginal"],
            "Anal" : ["Pick Anal"]
        }

        for position in sorted(list_of_positions, key = lambda x: x.name):
            if allow_position(person, position) and  mc.location.has_object_with_trait(position.requires_location) and (person.has_large_tits() or not position.requires_large_tits): #There is a valid object and if it requires large tits she has them.
                willingness = position.build_position_willingness_string(person, ignore_taboo = ignore_taboo)
                if position.skill_tag in prohibit_tags:
                    pass
                else:
                    positions[position.skill_tag].append([willingness, position])

        if allow_none:
            positions["Foreplay"].append(["Nothing", "Nothing"])

        return replace_unique_sex_positions(person, positions["Foreplay"], positions["Oral"], positions["Vaginal"], positions["Anal"], prohibit_tags = prohibit_tags)

    def replace_unique_sex_positions(person, foreplay_positions, oral_positions, vaginal_positions, anal_positions, prohibit_tags = []): #Use this function to get specific situations to replace or remove positions
        #First, filter out any positions this person doesn't accept
        #TODO move this to allow_position(), this probably very inefficient
        foreplay_positions = filter(person.event_triggers_dict.get("foreplay_position_filter", None),foreplay_positions)
        oral_positions = filter(person.event_triggers_dict.get("oral_position_filter", None),oral_positions)
        vaginal_positions = filter(person.event_triggers_dict.get("vaginal_position_filter", None),vaginal_positions)
        anal_positions = filter(person.event_triggers_dict.get("anal_position_filter", None),anal_positions)

        #Add unique character specific positions. #TODO tie this some kind of individual person function.
        # if person == salon_manager:
        #     if ophelia_get_special_bj_unlocked():
        #         oral_positions = filter(ophelia_oral_position_filter, oral_positions)
        #         willingness = Ophelia_blowjob.build_position_willingness_string(person, ignore_taboo = True)
        #         oral_positions.append([willingness, Ophelia_blowjob])
        return person.event_triggers_dict.get("unique_sex_positions", default_unique_sex_positions)(person, foreplay_positions, oral_positions, vaginal_positions, anal_positions, prohibit_tags)

    def default_unique_sex_positions(person, foreplay_positions, oral_positions, vaginal_positions, anal_positions, prohibit_tags = []):
        return [foreplay_positions, oral_positions, vaginal_positions, anal_positions]



label fuck_person_bugfix(the_person, private= True, start_position = None, start_object = None, skip_intro = False, girl_in_charge = False, self_strip = True, hide_leave = False, position_locked = False, report_log = None, affair_ask_after = True, ignore_taboo = False, asked_for_condom = False, prohibit_tags = []):
    # When called fuck_person starts a sex scene with someone. Sets up the encounter, mainly with situational modifiers.
    if report_log is None:
        $ report_log = defaultdict(int) #Holds information about the encounter: what positions were tried, how many rounds it went, who came and how many times, etc. Defaultdict sets values to 0 if they don't exist when accessed
        $ report_log["positions_used"] = [] #This is a list, not an int.

    $ finished = False #When True we exit the main loop (or never enter it, if we can't find anything to do)
    $ position_choice = start_position # initialize with start_position (in case girl is in charge or position is locked)
    $ object_choice = start_object # initialize with start_object (in case girl is in charge or position is locked)
    $ guy_orgasms_before_control = 0
    $ ask_for_condom = asked_for_condom
    $ ask_for_threesome = False
    $ use_condom = mc.condom if asked_for_condom else False
    $ stealth_orgasm = False
    $ stop_stripping = False

    #Privacy modifiers
    if mc.location.get_person_count() == 1 and not private:
        $ private = True #If we're alone in the space we're always Private, even if we had left the possibility for people being around.

    # $ renpy.say("", "Fuck Person Enhanced => start position: " + ("None" if start_position is None else start_position.name) + " , object: " + ("None" if start_object is None else start_object.name))
    $ apply_sex_modifiers(the_person)

    $ round_choice = "Change" # We start any encounter by letting them pick what position they want (unless something is forced or the girl is in charge)
    $ first_round = True
    $ has_taken_control = False
    while not finished:
        if girl_in_charge:
            if not position_choice is None and position_choice.skill_tag == "Foreplay" and not mc.recently_orgasmed and not first_round and not position_locked:
                # girl has got you hard again, now let her pick an actual sex position (clear foreplay position)
                if not the_person.vagina_visible(): # lets see if she is willing to go further
                    $ the_person.strip_outfit_to_max_sluttiness()
                $ position_choice = None

            # The girls decisions set round_choice here.
            if position_choice is None:
                $ position_choice = girl_choose_position_enhanced(the_person, ignore_taboo = ignore_taboo) #Can be none, if no option was available for her to take.
                if position_choice is not None:
                    # We need to make sure we're using an appropriate object
                    $ object_choice = girl_choose_object_enhanced(the_person, position_choice)
                    $ round_choice = "Change"

            if position_choice is None: #There's no position we can take
                "[the_person.title] can't think of anything more to do with you."
                $ round_choice = "Girl Leave"
            elif object_choice is None:
                "[the_person.title] looks around, but can't see anywhere to have fun with you."
                $ round_choice = "Girl Leave"
            elif report_log.get("guy orgasms", 0) > guy_orgasms_before_control and report_log.get("girl orgasms", 0) > 0: #Both parties have been satisfied
                the_person.char "Whew, that felt amazing. It's good to know it was as good for you as it was for me."
                $ round_choice = "Girl Leave"
            elif report_log.get("girl orgasms", 0) > 0 and not (the_person.love > 40 or the_person.obedience > 150): #She's cum and doesn't care about you finishing.
                the_person.char "Whew, that felt great. Thanks for the good time [the_person.mc_title]!"
                $ round_choice = "Girl Leave"
            elif report_log.get("girl orgasms", 0) > 1: # she's had her fill and doesn't care about you anymore
                the_person.char "Oh my god, I came so hard, thanks a lot [the_person.mc_title]!"
                $ round_choice = "Girl Leave"
            elif report_log.get("girl orgasms", 0) == 0 and the_person.energy < 15 :
                the_person.char "That was nice, but I'm tired. We will continue this another time."
                $ round_choice = "Girl Leave"
            else:
                if has_taken_control:
                    $ has_taken_control = False
                    $ the_person.call_dialogue("sex_take_control")

                if round_choice == "Change" and position_choice and object_choice:
                    # show dialog of girl changing position on her own
                    if the_person.has_taboo(position_choice.associated_taboo) and not ignore_taboo:
                        $ position_choice.call_taboo_break(the_person, mc.location, object_choice)
                        $ the_person.break_taboo(position_choice.associated_taboo)
                    else:
                        $ position_choice.call_transition(position_choice, the_person, mc.location, object_choice)
                $ round_choice = "Continue"
        else:
            # Forced actions (when the guy is in charge) go here and set round_choice.
            pass
            # if position_choice is None:
            #     $ round_choice = "Change" #Something has kicked our position out, so we need to ask the player what to do.

            # Note: There can be no chance based decisions in this section, because it loops on menu interactions, not on actual rounds of sex. Those go after the "change or continue" loop

        if round_choice is None: #If there is no set round_choice
            #TODO: Add a variant of this list when the girl is in control to ask if you want to resist or ask/beg for something.
            call screen enhanced_main_choice_display(build_menu_items([build_round_choice_menu(the_person, position_choice, position_locked, object_choice, ignore_taboo = ignore_taboo)]))
            $ round_choice = _return #This gets the players choice for what to do this round.

        # Now that a round_choice has been picked we can do something.
        if round_choice == "Change" or round_choice == "Continue":
            if round_choice == "Change": # If we are changing we first select and transition/intro the position, then run a round of sex. If we are continuing we ignroe all of that
                if start_position is None: #The first time we get here,
                    call pick_position(the_person, ignore_taboo = ignore_taboo, prohibit_tags = prohibit_tags) from _call_pick_position_bugfix
                    $ position_choice = _return
                else:
                    $ position_choice = start_position

                $ object_choice = pick_object_enhanced(the_person, position_choice, forced_object = start_object)

                if position_choice and object_choice:
                    call check_position_willingness_bugfix(the_person, position_choice, ignore_taboo = ignore_taboo, skip_dialog = True) from _call_check_position_willingness_bugfix
                    if not _return == 1: #If she wasn't willing for whatever reason (too slutty a position, not willing to wear a condom) we clear our settings and try again.
                        if _return == -1: # angry reject ends interactions
                            $ finished = True
                        $ position_choice = None
                        $ object_choice = None
                        call clear_object_effects(the_person) from _call_clear_object_effects_bugfix


                if position_choice and object_choice:
                    if skip_intro:
                        $ skip_intro = False  # turn off skip, for when we get here the second time.
                    elif first_round:
                        $ the_person.draw_person() #Draw her standing until we pick a new position
                        if not ignore_taboo and the_person.has_taboo(position_choice.associated_taboo):
                            # call mod taboo break
                            $ position_choice.call_transition_taboo_break(None, the_person, mc.location, object_choice)
                            $ the_person.break_taboo(position_choice.associated_taboo)
                        else:
                            $ position_choice.call_intro(the_person, mc.location, object_choice)
                    else:
                        $ the_person.change_arousal(-5) #Changing position lowers your arousal slightly
                        $ mc.change_arousal(-5)
                        if not ignore_taboo and the_person.has_taboo(position_choice.associated_taboo):
                            # call mod taboo break
                            $ position_choice.call_transition_taboo_break(None, the_person, mc.location, object_choice)
                            $ the_person.break_taboo(position_choice.associated_taboo)
                        else:
                            $ position_choice.call_transition(None, the_person, mc.location, object_choice)
                    # redraw after transition not before
                    $ position_choice.redraw_scene(the_person)

            $ start_position = None #Clear start positions/objects so they aren't noticed next round.
            $ start_object = None
            # $ renpy.say("", "Continue round => Position: " + position_choice.name + ", object: " + object_choice.name)
            if position_choice and object_choice: #If we have both an object and a position we're good to go, otherwise we loop and they have a chance to choose again.
                call sex_description(the_person, position_choice, object_choice, private = private, report_log = report_log) from _call_sex_description_bugfix
                $ first_round = False
                if not finished:    # when we switched to threesome finished is True
                    if mc.condom and mc.recently_orgasmed: # you orgasmed so you used your condom.
                        $ mc.condom = False
                    if position_choice.requires_hard and mc.recently_orgasmed:
                        "Your post orgasm cock softens, stopping you from [position_choice.verbing] [the_person.possessive_title] for now."
                        $ position_choice = None
                    elif position_choice.guy_energy > mc.energy:
                        if girl_in_charge:
                            "You're too exhausted to let [the_person.possessive_title] keep [position_choice.verbing] you."
                        else:
                            "You're too exhausted to continue [position_choice.verbing] [the_person.possessive_title]."
                        $ position_choice = None
                    elif position_choice.girl_energy > the_person.energy:
                        #TODO: Add some differentiated dialgoue depending on the position.
                        #TODO: Add "no energy" transitions where you keep fucking her anyways. (double TODO: Add a way of "breaking" her like this)
                        if not girl_in_charge:
                            the_person.char "I'm exhausted [the_person.mc_title], I can't keep this up..."
                        $ position_choice = None
                    elif not position_locked: #Nothing major has happened that requires us to change positions, we can have girls take over, strip
                        if not stop_stripping:
                            call girl_strip_event(the_person, position_choice, object_choice) from _call_girl_strip_event_bugfix


        elif isinstance(round_choice, Position): #The only non-strings on the list are positions we are changing to
            call check_position_willingness_bugfix(the_person, round_choice, ignore_taboo = ignore_taboo) from _call_check_position_willingness_bugfix_1
            if _return:
                $ round_choice.redraw_scene(the_person)
                if not ignore_taboo and the_person.has_taboo(round_choice.associated_taboo):
                    # call mod taboo break
                    $ position_choice.call_transition_taboo_break(round_choice, the_person, mc.location, object_choice)
                    $ the_person.break_taboo(round_choice.associated_taboo)
                else:
                    $ position_choice.call_transition(round_choice, the_person, mc.location, object_choice)
                $ position_choice = round_choice

            else: #If she wasn't willing we keep going with what we were doing, so just loop around.
                if _return == -1: # angry reject ends interactions
                    $ finished = True

        elif round_choice == "Strip":
            call strip_menu(the_person, (position_choice.verbing if isinstance(position_choice, Position) else "wooing")) from _call_strip_menu_bugfix
            $ stop_stripping = False

        elif round_choice == "Leave":
            $ finished = True # Unless something stops us the encounter is over and we can end

            # In 13% of the cases she takes control regardless of obedience, but only when she came only once
            # higher chance when she likes taking control lower when she doesn't
            if the_person.energy >= 30 and report_log.get("girl orgasms", 0) < 2 and (renpy.random.randint(0, __builtin__.int(the_person.arousal)) + 50 + the_person.get_opinion_score("taking control") * 20 > the_person.obedience or renpy.random.randint(1, 7 - (the_person.get_opinion_score("taking control") * 2)) == 1):
                $ the_person.change_obedience(-3)
                $ girl_in_charge = True
                $ finished = False
                $ stop_stripping = False    # allow her to strip again
                $ guy_orgasms_before_control = report_log.get("guy orgasms", 0)
                $ has_taken_control = True #After successful position and object choice she will let you know she wants to keep going.
                $ position_choice = None #She picks the position now, because she has her own list of possibilities

            elif the_person.energy >= 30 and (the_person.arousal > the_person.max_arousal - 30) and (report_log.get("girl orgasms", 0) == 0) and report_log.get("beg finish", 0) == 0: #Within 30 of orgasming and she hasn't cum yet
                # They're close to their orgasm and beg you to help them finish.
                $ the_person.call_dialogue("sex_beg_finish")
                menu:
                    "Give her what she wants":
                        $ the_person.change_obedience(2)
                        $ report_log["beg finish"] = report_log.get("beg finish", 0) + 1
                        $ finished = False
                        $ position_locked = False

                    "Stop and leave":
                        $ the_person.call_dialogue("sex_end_early")

            elif report_log.get("beg finish", 0) > 0 and report_log.get("girl orgasms", 0) == 0: #You promised to make her cum but didn't
                $ the_person.change_stats(obedience = -5, happiness = -10, love = -3)
                the_person.char "But you promised..."
                #TODO: Add some personality specific dialgoue for this

            else: # You end the encounter and nothing special happens.
                #TODO: Add some personality specific dialogue
                pass

        elif round_choice == "Girl Leave":
            $ finished = True
        $ round_choice = None #Get rid of our round choice at the end of the round to prepare for the next one. By doing this at the end instead of the begining of the loop we can set a mandatory choice for the first one.

    python:
        clear_sex_modifiers(the_person)

        report_log["end arousal"] = the_person.arousal
        if report_log.get("girl orgasms",0) > 0 or report_log.get("girl one orgasms", 0) > 0:
            the_person.arousal = 0 # If she came she's satisfied.
        else:
            the_person.change_arousal(-the_person.arousal/2) #Otherwise they are half as aroused as you leave them.

        mc.condom = False
        mc.recently_orgasmed = False

    if affair_ask_after and private and ask_girlfriend_requirement(the_person) is True and not the_person.relationship == "Single":
        if the_person.love >= 60 and the_person.sluttiness >= 30 - (the_person.get_opinion_score("cheating on men") * 5) and report_log.get("girl orgasms",0) >= 1: #If she loves you enoguh, is moderately slutty, and you made her cum
            call affair_check(the_person, report_log) from _call_affair_check_bugfix

    python:
        update_person_sex_record(the_person, report_log)
        position_choice = None
        object_choice = None

    # We return the report_log so that events can use the results of the encounter to figure out what to do.
    return report_log

label check_position_willingness_bugfix(the_person, the_position, ignore_taboo = False, skip_dialog = False): #Returns if hte person is willing to do this position or not, and charges the appropriate happiness hit if they needed obedience to be willing.
    $ willing = 1

    $ the_taboo = the_position.associated_taboo
    if ignore_taboo:
        $ the_taboo = None

    $ final_slut_requirement, final_slut_cap = the_position.calculate_position_requirements(the_person, ignore_taboo)

    if the_person.effective_sluttiness(the_taboo) >= final_slut_requirement:
        if not (skip_dialog or the_person.has_taboo(the_taboo)):
            $ the_person.call_dialogue("sex_accept")

    elif the_person.effective_sluttiness(the_taboo) + (the_person.obedience-100) >= final_slut_requirement:
        # She's willing to be commanded to do it. Reduce her happiness by the difference (increase arousal if she likes being submissive)
        python:
            happiness_drop = the_person.effective_sluttiness(the_taboo) - final_slut_requirement #Our initial conditions mean this is a negative number
            the_person.change_arousal(the_person.get_opinion_score("being submissive")*2)
            the_person.discover_opinion("being submissive")
            the_person.change_happiness(happiness_drop)

        if not the_person.has_taboo(the_taboo):
            $ the_person.call_dialogue("sex_obedience_accept")

    elif the_person.effective_sluttiness(the_taboo) > final_slut_requirement * .6:
        # She's not willing to do it, but gives you a soft reject.
        $ the_person.call_dialogue("sex_gentle_reject")
        $ willing = 0

    else:
        # You're nowhere close to the required sluttiness, lose some love for even trying and end interaction
        python:
            ran_num = the_person.effective_sluttiness(the_taboo) - final_slut_requirement #A negative number
            ran_num = __builtin__.round(ran_num/5)
            the_person.change_love(ran_num)
            willing = -1

        $ the_person.call_dialogue("sex_angry_reject")

    if willing == 1 and (the_position.skill_tag == "Vaginal" or the_position.skill_tag == "Anal") and not mc.condom: #We might need a condom, which means she might say no. TODO: Add an option to pull _off_ a condom while having sex.
        if not ask_for_condom:
            $ ask_for_condom = True
            if the_person.effective_sluttiness("condomless_sex") < the_person.get_no_condom_threshold() + 50:
                # she is not slutty enough and we have the condom dialog
                call condom_ask_enhanced(the_person) from _call_condom_ask_bugfix
                $ willing = _return
                $ use_condom = mc.condom
            else:
                # she is so slutty we are going to fuck her raw (we don't care anymore)
                if the_position.skill_tag == "Vaginal":
                    mc.name "I'm going to fuck your little pussy raw."
                else:
                    mc.name "I'm going to fuck your slutty asshole raw."
        elif use_condom:  # you already determined you are going to fuck her with condom
            "You quickly put on another condom and continue to fuck her."
            $ mc.condom = True

    return willing

label condom_ask_enhanced(the_person):
    $ condom_threshold = the_person.get_no_condom_threshold()

    if the_person.has_role(cum_internal_role):
        "[the_person.possessive_title] eyes your cock greedily. You could put a condom on if you wanted."
        menu:
            "Put on a condom":
                "You pull a condom out of your wallet and tear open the package."
                "[the_person.title] takes a hold of the condom in your hand."
                if the_person.knows_pregnant():
                    the_person.char "I'm already pregnant. It's a bit late for that, isn't it?"
                elif the_person.on_birth_control:
                    the_person.char "I'm on the pill so we really don't need one of those." # even if she is or not - she'll say it
                else:
                    the_person.char "You don't really need that thing, do you?"
                the_person.char "I want your cum inside me and this is going to stop that."
                menu:
                    "Insist on condom":
                        mc.name "I think a condom is a good idea."
                        if the_person.get_opinion_score("taking control") > -1:
                            the_person.char "OK. Let me put this another way."
                            "[the_person.title] grabs the condom and throws it off to the side."
                            the_person.char "Either we fuck and you come inside me or we don't fuck at all."
                            menu:
                                "Fuck her raw":
                                    mc.name "Fine."
                                    the_person.char "I knew you would make the right choice."
                                "Don't":
                                    mc.name "If it's that important to you let's just do something else."
                                    return 0
                        else:
                            the_person.char "OK."
                            call put_on_condom_routine(the_person) from _call_put_on_condom_routine_8
                    "Fuck her raw":
                        return 1
            "Don't":
                return 1

    elif the_person.has_role(prostitute_role):
        if the_person.love < 50:
            the_person.char "Are you remembering that I'm a 'working girl'?"
            the_person.char "That means 'safety first' - always."
            the_person.char "We're going to have to use one of these."
            "She gets out a condom."
            if the_person.knows_pregnant():
                the_person.char "Me being pregnant doesn't change that."
            the_person.char "But don't you worry."
            the_person.char "You're going to feel EVERY thing we do."
            menu:
                "Put on condom":
                    call put_on_condom_routine(the_person) from _call_put_on_condom_routine_1

                "Refuse and do something else":
                    "[the_person.title] doesn't seem like she's going to change her mind."
                    mc.name "If it's that important to you let's just do something else."
                    return 0

        elif the_person.sex_record.get("Vaginal Creampies", 0) < 5 and the_person.sex_record.get("Anal Creampies", 0) < 5:
            the_person.char "Normally we would have to use one of these."
            "She gets out a condom."
            if the_person.knows_pregnant():
                the_person.char "Would you like to fuck this pregnant whore without one?"
            else:
                the_person.char "But maybe not. What do you think?"
            menu:
                "Condom":
                    mc.name "Let's cover this bad boy up."
                    call put_on_condom_routine(the_person) from _call_put_on_condom_routine_2

                "No condom":
                    mc.name "I like fucking you like nature intended."
                    if the_person.get_opinion_score("bareback sex") > 0:
                        the_person.char "Good choice. I hate those things but I have to use them."
                    if the_person.get_opinion_score("creampies") < 0 or the_person.get_opinion_score("anal creampies") < 0 or not the_person.on_birth_control:
                        the_person.char "Just make sure to pull out when you cum, okay?"
                    if not the_person.on_birth_control:
                        the_person.char "I'm not using any birth control at the moment."

                "[the_person.title] smiles at you."

        else:
            the_person.char "I know you like to do me bare."
            if the_person.knows_pregnant():
                the_person.char "Would you like to shower my baby with your cum?"
            else:
                the_person.char "So maybe no condom today?"
            menu:
                "Agree no condom":
                    if the_person.get_opinion_score("bareback sex") > 0:
                        the_person.char "Good choice. I hate those things but I have to use them."
                    if the_person.get_opinion_score("creampies") < 0 or the_person.get_opinion_score("anal creampies") < 0 or not the_person.on_birth_control:
                        the_person.char "Just make sure to pull out when you cum, okay?"
                    if not the_person.on_birth_control:
                        the_person.char "I'm not using any birth control at the moment."

                    "[the_person.title] smiles at you."
                "Use condom":
                    mc.name "I still think that it's good idea."
                    the_person.char "Alright."

                    call put_on_condom_routine(the_person) from _call_put_on_condom_routine_3

    elif the_person.effective_sluttiness() < condom_threshold:
        # they demand you put on a condom.
        #TODO: Make this dialogue personality based
        if the_person.knows_pregnant():
            if the_person.get_opinion_score("bareback sex") < 0:
                the_person.char "You can't get me {i}more{/i} pregnant, but I really don't like bare sex."
            else:
                the_person.char "Although i'm pregnant, I would like you to wear a condom anyway."
        elif the_person.get_opinion_score("bareback sex") > 0 or the_person.get_opinion_score("creampies") > 0 or the_person.get_opinion_score("anal creampies") > 0:
            the_person.char "I hate to say it, but you really should wear a condom."
        else:
            the_person.char "Do you have a condom? You're going to have to put one on."

        menu:
            "Put on a condom":
                call put_on_condom_routine(the_person) from _call_put_on_condom_routine_4

            "Refuse and do something else":
                "[the_person.title] doesn't seem like she's going to change her mind."
                mc.name "If it's that important to you let's just do something else."
                return 0

        if the_person.get_opinion_score("bareback sex") < 0 :
            the_person.char "There we go, a nice big rubbery cock."

    elif the_person.effective_sluttiness() < condom_threshold + 20:
        # They suggest you put on a condom.
        if the_person.knows_pregnant():
            if the_person.get_opinion_score("bareback sex") < 0:
                the_person.char "You can't get me {i}more{/i} pregnant, but I don't like bare sex. I think that you should put on a condom."
            else:
                the_person.char "There's not much point in a condom now that i'm pregnant."
        elif the_person.get_opinion_score("creampies") > 0 and the_person.get_opinion_score("bareback sex") > 0: # likes everything a condom stops
            $ the_person.discover_opinion("creampies")
            $ the_person.discover_opinion("bareback sex")
            the_person.char "We should use a condom, though I don't really see why."
        elif the_person.get_opinion_score("creampies") < 0 and the_person.get_opinion_score("bareback sex") > 0: #no to pie yes to ride
            the_person.char "We should use a condom, I don't want you to come inside me."
        elif the_person.get_opinion_score("bareback sex") < 0:
            the_person.char "We should use a condom, I think that that would be the best idea."
        else:
            the_person.char "Do you think you should put a condom on? Maybe it's a good idea."
        menu:
            "Agree to put on a condom":
                mc.name "I think you're right."
                call put_on_condom_routine(the_person) from _call_put_on_condom_routine_5

            "Fuck her raw":
                mc.name "No way. I want to feel you wrapped around me."
                if the_person.has_taboo("condomless_sex"):
                    $ the_person.call_dialogue("condomless_sex_taboo_break")
                else:
                    if the_person.get_opinion_score("bareback sex") > 0:
                        the_person.char "Tell me about it, nothing beats skin on skin."
                    if the_person.get_opinion_score("creampies") < 0 or not the_person.on_birth_control:
                        the_person.char "Just make sure to pull out when you cum, okay?"
                    if not the_person.on_birth_control:
                        the_person.char "I'm not using any birth control at the moment."

    else:
        if the_person.get_opinion_score("bareback sex") < 0 or the_person.get_opinion_score("creampies") < 0 or the_person.get_opinion_score("anal creampies") < 0:
            the_person.char "I think that we should use a condom."
        menu:
            "Put on a condom":
                if the_person.get_opinion_score("taking control") > 0 and the_person.get_opinion_score("bareback sex") > 0: # likes it bare and is not a pushover
                    "[the_person.title] takes a hold of your hand."
                    the_person.char "You don't really need that, do you?"
                    menu:
                        "Insist on condom":
                            mc.name "I think a condom is a good idea."
                            if the_person.get_opinion_score("taking control") > 1:
                                the_person.char "OK. Let me put this another way."
                                "[the_person.title] grabs the condom and throws it off to the side."
                                the_person.char "Either you fuck me raw or we don't fuck at all."
                                menu:
                                    "Fuck her raw":
                                        mc.name "Fine."
                                        the_person.char "I knew you would make the right choice."
                                    "Don't":
                                        mc.name "If it's that important to you let's just do something else."
                                        return 0
                            else:
                                the_person.char "Fine, lets make this quick!"

                                call put_on_condom_routine(the_person) from _call_put_on_condom_routine_9

                        "Relent":
                            mc.name "I suppose not."
                            the_person.char "Thanks, [the_person.mc_title]."

                elif the_person.get_opinion_score("bareback sex") > 0 or the_person.get_opinion_score("creampies") > 0 or the_person.get_opinion_score("anal creampies") > 0:
                    if the_person.knows_pregnant():
                        the_person.char "Remember that I'm pregnant, do we really need one of those now?"
                    elif the_person.on_birth_control:
                        the_person.char "I'm on the pill, do we really need one of those?"
                    else:
                        the_person.char "Really? I don't like using a condom."
                    menu:
                        "Insist on condom":
                            mc.name "I think a condom is a good idea."
                            call put_on_condom_routine(the_person) from _call_put_on_condom_routine_7

                        "Relent":
                            mc.name "I suppose not."
                            the_person.char "Thanks, [the_person.mc_title]."

                else:
                    call put_on_condom_routine(the_person) from _call_put_on_condom_routine_6

            "Fuck her raw":
                if the_person.has_taboo("condomless_sex"):
                    $ the_person.call_dialogue("condomless_sex_taboo_break")
                else:
                    if the_person.get_opinion_score("bareback sex") > 0:
                        the_person.char "Tell me about it, nothing beats skin on skin."
                    else:
                        the_person.char "I'm not a big fan of bare sex, but if you like it that way."
                    if the_person.get_opinion_score("creampies") < 0 or the_person.get_opinion_score("anal creampies") < 0 or not the_person.on_birth_control:
                        the_person.char "Just make sure to pull out when you cum, okay?"
                    if not the_person.on_birth_control:
                        the_person.char "I'm not using any birth control at the moment."

    if not mc.condom:
        $ the_person.break_taboo("condomless_sex")

    return 1

label put_on_condom_routine(the_person):
    if the_person.sex_skills["Oral"] > 3 and the_person.get_opinion_score("giving blowjobs") > 1: #Knows what she's doing
        "[the_person.title] gets a condom out of their own bag and opens it."
        "She carefully puts it in her mouth, behind her teeth."
        "She starts bobbing up and down on your cock."
        "As she goes down on your dick she unrolls the condom onto it with her mouth."
        if the_person.get_opinion_score("being submissive") > 0:
            "She keeps going to the very base of your cock, deep-throating you and entirely covering your cock."
        else:
            "Once she has rolled on about two thirds of the condom she brings her head back up and rolls the rest on with her hand."
    elif the_person.get_opinion_score("giving handjobs") > 0:
        "You pull out a condom from your wallet and rip open the package."
        the_person.char "Let me help with that."
        "[the_person.title] takes the condom out of your hand."
        "She holds it at the top of your cock with one hand as she strokes further and further with the other hand, rolling the condom down onto it."
    elif the_person.get_opinion_score("bareback sex") < 0: # condoms are good
        if the_person.get_opinion_score("taking control") > 0:
            the_person.char "Good choice."
            "You roll the condom onto your cock as [the_person.title] watches eagerly."
        else:
            "[the_person.title] watches eagerly while you roll the condom on."
    elif the_person.get_opinion_score("bareback sex") > 0:
        "You pull out a condom from your wallet and rip open the package. [the_person.title] watches disappointedly while you slide it on."
    else:
        "You pull out a condom from your wallet and rip open the package. [the_person.title] watches while you slide it on."

    $ mc.condom = True
    return


label watcher_check_enhanced(the_person, the_position, the_object, the_report): # Check to see if anyone is around to comment on the characters having sex.
    $ watcher = cheating_check_get_watcher(the_person)
    if watcher:
        # you only get one chance for starting a threesome per public sex action (avoid spamming threesome question)
        # threesome has no watcher loop, so all watching stops when threesome has started.
        # TODO: add watchers to threesome core
        if not ask_for_threesome and willing_to_threesome(the_person, watcher):
            $ watcher.draw_person()
            watcher.char "Oh my good, that looks amazing..."
            if can_join_threesome(watcher, the_person, the_position.position_tag):
                the_person.char "Can I... can I join you? I want some too!"
                $ ask_for_threesome = True
                menu:
                    "Let her join":
                        watcher.char "Yes! Thank you [watcher.mc_title]!"
                        $ scene_manager = Scene()
                        $ scene_manager.add_actor(the_person, position = the_position.position_tag)
                        $ scene_manager.add_actor(watcher, character_placement = character_center_flipped)
                        watcher.char "Let me take off some clothes."
                        $ scene_manager.strip_actor_outfit(watcher)
                        call join_threesome(the_person, watcher, the_position.position_tag) from _call_join_threesome_watcher_check_enhanced
                        $ report_log = _return
                        python:
                            scene_manager.clear_scene()
                            if report_log.get("girl two orgasms", 0) > 0:
                                watcher.arousal = 0 # If she came she's satisfied.
                            else:
                                watcher.change_arousal(-watcher.arousal/2) #Otherwise they are half as aroused as you leave them.
                            finished = True
                            del watcher
                        return
                    "Not this time":
                        the_person.char "Aww, okay. Maybe next time..."
                        $ the_person.change_obedience(3)

        $ the_relationship = town_relationships.get_relationship(watcher, the_person)
        if the_relationship and the_relationship.get_type() in ["Mother", "Daughter", "Sister", "Cousin", "Niece", "Aunt", "Grandmother", "Granddaughter"]:
            call relationship_sex_watch(watcher, town_relationships.get_relationship_type(watcher, the_person).lower(), the_position) from _call_relationship_sex_watch
            $ the_position.redraw_scene(the_person)
            call relationship_being_watched(the_person, watcher, town_relationships.get_relationship_type(the_person, watcher).lower(), the_position) from _call_relationship_being_watched
            $ the_person.change_arousal(the_person.get_opinion_score("public sex"))
            $ the_person.discover_opinion("public sex")
        else:
            # NOTE: the dialogue here often draws the person talking with various emotions or positions, so we redraw the scene after we call them.
            $ watcher.call_dialogue("sex_watch", the_sex_person = the_person, the_position = the_position) #Get the watcher's reaction to the people having sex. This might include dialogue calls from other personalities as well!
            $ the_position.redraw_scene(the_person)
            $ the_person.call_dialogue("being_watched", the_watcher = watcher, the_position = the_position) #Call her response to the person watching her.
            $ the_person.change_arousal(the_person.get_opinion_score("public sex"))
            $ the_person.discover_opinion("public sex")
        $ the_relationship = None
    $ del watcher
    return

label relationship_sex_watch(the_person, the_relation, the_position):
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry")
        the_person.char "Oh my god [the_relation], I can't believe you're doing that here in front of everyone. Don't either of you have any decency?"
        $ the_person.change_stats(obedience = -2, happiness = -1)
        "[the_person.title] looks away while you and her [the_relation] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement - 10:
        $ the_person.draw_person()
        $ the_person.change_happiness(-1)
        "[the_person.title] shakes her head and tries to avoid watching you and her [the_relation] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement:
        $ the_person.draw_person()
        $ change_report = the_person.change_slut_temp(1)
        "[the_person.title] tries to avert her gaze, but keeps glancing over while you and her [the_relation] [the_position.verb]."

    elif the_person.sluttiness > the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person()
        the_person.char "Oh my..."
        $ change_report = the_person.change_slut_temp(2)
        "[the_person.title] watches quietly while you and her [the_relation] [the_position.verb]."

    else:
        $ the_person.draw_person(emotion = "happy")
        the_person.char "Glad to see you two are having a good time. [the_person.mc_title], careful you aren't too rough with my [the_relation]."
        "[the_person.title] watches quietly while you and her [the_relation] [the_position.verb]."
    return

label relationship_being_watched(the_person, the_watcher, the_relation, the_position):
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        the_person.char "I can handle it [the_person.mc_title], you can be rough with me."
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by her [the_relation] watching you and her [the_position.verb]."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        the_person.char "Don't listen to my [the_relation], I'm having a great time. Look, she can't stop peeking over."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by her [the_relation] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        the_person.char "Oh god, having you watch us like this..."
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by her [the_relation] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        the_person.char "[the_person.mc_title], maybe we shouldn't be doing this here..."
        $ the_person.change_stats(arousal = -1, slut_temp = -1)
        "[the_person.title] seems uncomfortable with her [the_relation] nearby."

    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        the_person.char "Oh my god, having you watch us do this feels so dirty. I think I like it!"
        $ the_person.change_stats(arousal = 1, slut_temp = 1)
        "[the_person.title] seems more comfortable [the_position.verbing] you with her [the_relation] around."

    return

label girl_strip_event_enhanced(the_person, the_position, the_object):
    # first we determine if we should strip at all (when we have full access there is no need for this blocking dialog)
    if the_person.outfit.full_access():
        return

    python:
        the_clothing = the_person.choose_strip_clothing_item()
        ran_num = the_person.effective_sluttiness() - the_person.outfit.slut_requirement
        ran_num += the_person.get_opinion_score("not wearing anything") * 5

    if renpy.random.randint(0,100) < ran_num and the_clothing:
        if renpy.random.randint(0,100) < the_person.obedience - the_person.arousal:
            $ the_position.call_strip_ask(the_person, the_clothing, mc.location, the_object)
        else:
            $ the_position.call_strip(the_person, the_clothing, mc.location, the_object) #If a girl's outfit is less slutty than she is currently feeling (with arousal factored in) she will want to strip stuff off.

        $ the_person.update_outfit_taboos()

        if the_person.outfit.has_clothing(the_clothing):
            # you told her not to strip, so we will not ask again until player initiates stripping
            $ stop_stripping = True

    $ the_clothing = None
    return

# call after striping to show the stripping taboo break dialog
label break_strip_outfit_taboos(the_person):
    $ taboo_broken = False
    if the_person.outfit.tits_visible() and the_person.outfit.vagina_visible():
        "Once she's done stripping [the_person.possessive_title] is practically naked."
        if the_person.has_taboo(["bare_pussy", "bare_tits"]):
            "She makes a vain attempt to keep herself covered with her hands, but soon enough seems to be comfortable being nude in front of you."
            $ the_person.break_taboo("bare_pussy")
            $ the_person.break_taboo("bare_tits")
            $ taboo_broken = True
    elif the_person.outfit.tits_visible():
        "Once she's done stripping [the_person.possessive_title] has her nice [the_person.tits] tits out on display."
        if the_person.has_taboo("bare_tits"):
            if the_person.has_large_tits():
                "She makes a hopeless attempt to cover her large tits with her hands, but comes to the realization it's pointless."
            else:
                "She tries to hide her tits from you with her hands, but quickly realizes how impractical that would be."
            "Soon enough she doesn't even mind having them out."
            $ the_person.break_taboo("bare_tits")
            $ taboo_broken = True
    elif the_person.outfit.vagina_visible():
        "Once she's done stripping [the_person.possessive_title] has her pretty little pussy out on display for everyone."
        if the_person.has_taboo("bare_pussy"):
            "She tries to hide herself from you with her hand, but quickly realizes how impractical that would be."
            "Soon enough she doesn't seem to mind."
            $ the_person.break_taboo("bare_pussy")
            $ taboo_broken = True
    else:
        "[the_person.possessive_title] finishes stripping and looks back at you."
        if (the_person.outfit.wearing_panties() and not the_person.outfit.panties_covered()) or (the_person.outfit.wearing_bra() and not the_person.outfit.bra_covered()):
            if the_person.has_taboo("underwear_nudity"):
                "She seems nervous at first, but quickly gets used to being in her underwear in front of you."
                $ the_person.break_taboo("underwear_nudity")
                $ taboo_broken = True
    return taboo_broken

label pick_position_enhanced(the_person, allow_none = True, ignore_taboo = False, prohibit_tags = []):
    call screen enhanced_main_choice_display(build_menu_items(build_grouped_sex_position_menu(the_person, allow_none = allow_none, ignore_taboo = ignore_taboo, prohibit_tags = prohibit_tags)))
    $ position_choice = _return
    return None if position_choice == "Nothing" else position_choice
