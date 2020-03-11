# Fix for sex mechanic for people who don't have the bugfix branch installed
# Enhancement for pick object (don't show list when only one object can be selected (auto-select it))
# Added condom ask enhancements (Original by BadRabbit)

init 5 python:
    config.label_overrides["fuck_person"] = "fuck_person_bugfix"
    config.label_overrides["check_position_willingness"] = "check_position_willingness_bugfix"
    config.label_overrides["pick_object"] = "pick_object_enhanced"
    config.label_overrides["watcher_check"] = "watcher_check_enhanced"
    config.label_overrides["condom_ask"] = "condom_ask_enhanced"

    def girl_choose_position_enhanced(person, ignore_taboo = False):
        position_option_list = []
        for position in list_of_girl_positions:
            if mc.location.has_object_with_trait(position.requires_location):
                if position.her_position_willingness_check(the_person, ignore_taboo = ignore_taboo):
                    position_option_list.append(position)
        return get_random_from_list(position_option_list)

    def girl_choose_object_enhanced(person, position):
        possible_object_list = []
        if position is None:
            person.clear_situational_slut("sex_object")
            person.clear_situational_obedience("sex_object")
            return None

        for an_object in mc.location.objects_with_trait(position.requires_location):
            possible_object_list.append(an_object)

        picked_object = get_random_from_list(possible_object_list)

        person.add_situational_slut("sex_object", picked_object.sluttiness_modifier, position.verbing + " on a " + picked_object.name)
        person.add_situational_obedience("sex_object",picked_object.obedience_modifier, position.verbing + " on a " + picked_object.name)
        return picked_object

    def cheating_check_get_watcher(the_person):
        other_people = [person for person in mc.location.people if person is not the_person] #Build a list with all the _other_ people in the room other than the one we're fucking.
        for a_person in other_people:
            if girlfriend_role in a_person.special_role and the_position.slut_requirement > (a_person.sluttiness/2): #You can get away with stuff half as slutty as she would do
                caught_cheating_action = Action("Caught cheating action", caught_cheating_requirement, "caught_cheating_label", args = the_person)
                if not exists_in_room_enter_list(a_person, "caught_cheating_label"):
                    a_person.on_room_enter_event_list.append(caught_cheating_action)
                    renpy.say("",a_person.title + " gasps when she sees what you and " + the_person.title + " are doing.")

            elif affair_role in a_person.special_role and the_position.slut_requirement > ((a_person.sluttiness*2)/3): #You can get away with stuff two thirds as slutty as what she would do.
                caught_affair_cheating_action = Action("Caught affair cheating action", caught_affair_cheating_requirement, "caught_affair_cheating_label", args = the_person)
                if not exists_in_room_enter_list(a_person, "caught_affair_cheating_label"):
                    a_person.on_room_enter_event_list.append(caught_affair_cheating_action)
                    renpy.say("",a_person.title + " gasps when she sees what you and " + the_person.title + " are doing.")

        return get_random_from_list(other_people) #Get a random person from the people in the area, if there are any.

    def apply_sex_modifiers(the_person):
        #Family situational modifiers
        if the_person.has_family_taboo(): #Check if any of the roles the person has belong to the list of family roles.
            the_person.add_situational_slut("taboo_sex", -20, "We're related, we shouldn't be doing this.")

        #Cheating modifiers
        the_person.discover_opinion("cheating on men")
        if prostitute_role in the_person.special_role:
            the_person.add_situational_slut("cheating", 20, "Prostitutes don't care about cheating")
        elif the_person.relationship == "Girlfriend":
            if the_person.get_opinion_score("cheating on men") > 0:
                the_person.add_situational_slut("cheating", the_person.get_opinion_score("cheating on men") * 5, "I'm cheating on my boyfriend!")
            else:
                the_person.add_situational_slut("cheating", -5 + (the_person.get_opinion_score("cheating on men") * -10), "I can't cheat on my boyfriend!")
        elif the_person.relationship == "Fiancée":
            if the_person.get_opinion_score("cheating on men") > 0:
                the_person.add_situational_slut("cheating", the_person.get_opinion_score("cheating on men") * 8, "I'm cheating on my fiancé!")
            else:
                the_person.add_situational_slut("cheating", -15 + (the_person.get_opinion_score("cheating on men") * -15), "I could never cheat on my fiancé!")
        elif the_person.relationship == "Married":
            if the_person.get_opinion_score("cheating on men") > 0:
                the_person.add_situational_slut("cheating", the_person.get_opinion_score("cheating on men") * 10, "I'm cheating on my husband!")
            else:
                the_person.add_situational_slut("cheating", -20 + (the_person.get_opinion_score("cheating on men") * -20), "I could never cheat on my husband!")

        #Privacy modifiers
        if not private:
            if the_person.sluttiness < 50:
                the_person.add_situational_slut("public_sex", -10 + the_person.get_opinion_score("public sex") * 5, "There are people watching...")
            else:
                the_person.add_situational_slut("public_sex", the_person.get_opinion_score("public sex") * 5, "There are people watching!")

        #Love modifiers. Always applies if negative, but only adds a bonus if you are in private.
        if the_person.love < 0:
            the_person.add_situational_slut("love_modifier", the_person.love, "I hate you, get away from me!")
        elif private:
            if girlfriend_role in the_person.special_role: #Girlfriend and affairs gain full Love
                the_person.add_situational_slut("love_modifier", the_person.love, "You're my special someone, I love you!")
            elif affair_role in the_person.special_role:
                the_person.add_situational_slut("love_modifier", the_person.love, "We may keep it a secret, but I love you!")
            elif the_person.has_family_taboo(): #Family now only gains 1/4 (but this now helps offset the taboo penalty)
                if mother_role in the_person.special_role:
                    the_person.add_situational_slut("love_modifier", __builtin__.int(the_person.love/4), "Even if it's wrong, a mother should do everything she can for her son!")
                elif sister_role in the_person.special_role:
                    the_person.add_situational_slut("love_modifier", __builtin__.int(the_person.love/4), "I love my brother, and even if it's wrong I want to be close to him!")
                else: #Generic family one
                    the_person.add_situational_slut("love_modifier", __builtin__.int(the_person.love/4), "I love you, even though we're related!")
            else: #If you aren't in a relationship with them only half their Love applies.
                the_person.add_situational_slut("love_modifier", __builtin__.int(the_person.love/2), "I really like you, let's see where this goes!")
        return

    def clear_sex_modifiers(the_person):
        # Teardown the sex modifiers
        the_person.clear_situational_slut("love_modifier")
        the_person.clear_situational_slut("public_sex")
        the_person.clear_situational_slut("cheating")
        the_person.clear_situational_slut("taboo_sex")
        the_person.clear_situational_slut("sex_object")
        the_person.clear_situational_obedience("sex_object")
        return

    def update_person_sex_record(the_person, report_log):
        types_seen = []
        for position_type in report_log.get("positions_used",[]): #Note: Clears out duplicates
            if position_type.record_class and position_type.record_class not in types_seen:
                the_person.sex_record[position_type.record_class] += 1
                types_seen.append(position_type.record_class)
        return

    def build_round_choice_menu(the_person, position_choice, ignore_taboo = False):
        option_list = []
        if position_choice is not None:
            option_list.append(["Keep " + position_choice.verbing + " her.","Continue"]) #NOTE: you're prevented from continuing if the energy cost would be too high by the pre-round checks.

            if not position_locked and object_choice:
                option_list.append(["Pause and change position.\n-5 {image=arousal_token_small}","Change"])
                for position in position_choice.connections:
                    if object_choice.has_trait(position.requires_location):
                        appended_name = "Transition to " + position.build_position_willingness_string(the_person, ignore_taboo = ignore_taboo).replace("{size=22}", "{size=12}") #NOTE: clothing and energy checks are done inside of build_position_willingness, invalid position marked (disabled)
                        option_list.append([appended_name,position])

            if position_locked and object_choice:
                # allow transition to positions with same traits and skill requirements
                for position in position_choice.connections:
                    if isinstance(object_choice, Object): # Had an error with cousin's kissing blackmail where it would pass object_choice as a list, haven't looked further into it
                        if object_choice.has_trait(position.requires_location) and position_choice.skill_tag == position.skill_tag:
                            appended_name = "Transition to " + position.build_position_willingness_string(the_person, ignore_taboo = ignore_taboo).replace("{size=22}", "{size=12}") #NOTE: clothing and energy checks are done inside of build_position_willingness, invalid position marked (disabled)
                            option_list.append([appended_name, position])

            option_list.append(["Pause and strip her down.","Strip"])

            if not hide_leave: #TODO: Double check that we can always get out
                option_list.append(["Stop " + position_choice.verbing + " her and leave.", "Leave"]) #TODO: Have this appear differently depending on if you've cum yet, she's cum yet, or you've both cum.

        else:
            if not position_locked:
                option_list.append(["Pick a new position.\n-5 {image=arousal_token_small}","Change"])
            if not hide_leave:
                option_list.append(["Stop and leave.", "Leave"])
        option_list.insert(0, "Round Choices")
        return option_list

label fuck_person_bugfix(the_person, private= True, start_position = None, start_object = None, skip_intro = False, girl_in_charge = False, hide_leave = False, position_locked = False, report_log = None, affair_ask_after = True, ignore_taboo = False):
    # When called fuck_person starts a sex scene with someone. Sets up the encounter, mainly with situational modifiers.
    if report_log is None:
        $ report_log = defaultdict(int) #Holds information about the encounter: what positions were tried, how many rounds it went, who came and how many times, etc. Defaultdict sets values to 0 if they don't exist when accessed
        $ report_log["positions_used"] = [] #This is a list, not an int.

    $ finished = False #When True we exit the main loop (or never enter it, if we can't find anything to do)
    $ position_choice = start_position # initialize with start_position (in case girl is in charge or position is locked)
    $ object_choice = start_object # initialize with start_object (in case girl is in charge or position is locked)
    $ guy_orgasms_before_control = 0
    $ ask_for_condom = False
    $ use_condom = False

    # $ renpy.say("", "Fuck Person Enhanced => start position: " + ("None" if start_position is None else start_position.name) + " , object: " + ("None" if start_object is None else start_object.name))
    $ apply_sex_modifiers(the_person)

    $ round_choice = "Change" # We start any encounter by letting them pick what position they want (unless something is forced or the girl is in charge)
    $ first_round = True
    $ has_taken_control = False
    while not finished:
        if girl_in_charge:
            if not position_choice is None and position_choice.skill_tag == "Foreplay" and not mc.recently_orgasmed:
                # girl has got you hard again, now let her pick an actual sex position (clear foreplay position)
                $ position_choice = None

            # The girls decisions set round_choice here.
            if position_choice is None:
                $ position_choice = girl_choose_position_enhanced(the_person, ignore_taboo = ignore_taboo) #Can be none, if no option was available for her to take.
                if position_choice is not None:
                    # We need to make sure we're using an appropriate object
                    $ object_choice = girl_choose_object_enhanced(the_person, position_choice)
                    if object_choice and not has_taken_control:
                        # show dialog of girl changing position on her own
                        $ position_choice.call_transition(round_choice, the_person, mc.location, object_choice)
            if position_choice is None: #There's no position we can take
                "[the_person.title] can't think of anything more to do with you."
                $ round_choice = "Girl Leave"
            elif object_choice is None:
                "[the_person.title] looks around, but can't see anywhere to have fun with you."
                $ round_choice = "Girl Leave"
            elif report_log.get("guy orgasms", 0) > guy_orgasms_before_control and report_log.get("girl orgasms", 0) > 0: #Both parties have been satisfied
                the_person.char "Whew, that felt amazing. It's good to know it was as good for you as it was for me."
                $ round_choice = "Girl Leave"
            elif report_log.get("girl orgasms", 0) > 0 and the_person.love < 10 and the_person.obedience < 110: #She's cum and doesn't care about you finishing.
                the_person.char "Whew, that felt great. Thanks for the good time [the_person.mc_title]!"
                $ round_choice = "Girl Leave"
            elif report_log.get("girl orgasms", 0) == 0 and the_person.energy < 15 :
                the_person.char "That was nice, but i'm tired. We will continue this another time."
                $ round_choice = "Girl Leave"
            elif has_taken_control:
                $ has_taken_control = False
                $ the_person.call_dialogue("sex_take_control")
                $ position_choice.call_transition(round_choice, the_person, mc.location, object_choice)
                $ round_choice = "Continue"
            else:
                # Don't show control message, it breaks the flow, because it pops up every round.
                #"[the_person.possessive_title] is in control, and keeps on [position_choice.verbing] you."
                $ round_choice = "Continue"
        else:
            # Forced actions (when the guy is in charge) go here and set round_choice.
            pass
            # if position_choice is None:
            #     $ round_choice = "Change" #Something has kicked our position out, so we need to ask the player what to do.

            # Note: There can be no chance based decisions in this section, because it loops on menu interactions, not on actual rounds of sex. Those go after the "change or continue" loop

        if round_choice is None: #If there is no set round_choice
            #TODO: Add a variant of this list when the girl is in control to ask if you want to resist or ask/beg for something.
            if "build_menu_items" in globals():
                call screen main_choice_display(build_menu_items([build_round_choice_menu(the_person, position_choice, ignore_taboo = ignore_taboo)]))
            else:
                call screen main_choice_display([build_round_choice_menu(the_person, position_choice, ignore_taboo = ignore_taboo)])
            $ round_choice = _return #This gets the players choice for what to do this round.

        # Now that a round_choice has been picked we can do something.
        if round_choice == "Change" or round_choice == "Continue":
            if round_choice == "Change": # If we are changing we first select and transition/intro the position, then run a round of sex. If we are continuing we ignroe all of that
                if start_position is None: #The first time we get here,
                    call pick_position(the_person, ignore_taboo = ignore_taboo) from _call_pick_position_bugfix
                    $ position_choice = _return
                else:
                    $ position_choice = start_position

                call pick_object_enhanced(the_person, position_choice, forced_object = start_object) from _call_pick_object_bugfix
                $ object_choice = _return

                if position_choice and object_choice:
                    call check_position_willingness_bugfix(the_person, position_choice, ignore_taboo = ignore_taboo, skip_dialog = True) from _call_check_position_willingness_bugfix
                    if not _return: #If she wasn't willing for whatever reason (too slutty a position, not willing to wear a condom) we clear our settings and try again.
                        $ position_choice = None
                        $ object_choice = None
                        call clear_object_effects(the_person) from _call_clear_object_effects_bugfix

                if position_choice and object_choice:
                    $ position_choice.redraw_scene(the_person)
                    if skip_intro:
                        pass
                    elif first_round:
                        $ the_person.draw_person() #Draw her standing until we pick a new position
                        if the_person.has_taboo(position_choice.associated_taboo) and not ignore_taboo:
                            $ position_choice.call_taboo_break(the_person, mc.location, object_choice)
                            $ the_person.break_taboo(position_choice.associated_taboo)
                        else:
                            $ position_choice.call_intro(the_person, mc.location, object_choice)
                    else:
                        $ the_person.change_arousal(-5) #Changing position lowers your arousal slightly
                        $ mc.change_arousal(-5)
                        if the_person.has_taboo(position_choice.associated_taboo) and not ignore_taboo:
                            $ position_choice.call_taboo_break(the_person, mc.location, object_choice)
                            $ the_person.break_taboo(position_choice.associated_taboo)
                        else:
                            $ position_choice.call_transition(None, the_person, mc.location, object_choice)

            $ start_position = None #Clear start positions/objects so they aren't noticed next round.
            $ start_object = None
            # $ renpy.say("", "Continue round => Position: " + position_choice.name + ", object: " + object_choice.name)
            if position_choice and object_choice: #If we have both an object and a position we're good to go, otherwise we loop and they have a chance to choose again.
                call sex_description(the_person, position_choice, object_choice, private = private, report_log = report_log) from _call_sex_description_bugfix
                $ first_round = False
                if mc.condom and mc.recently_orgasmed: # you orgasmed so you used your condom.
                    $ mc.condom = False
                if position_choice.requires_hard and mc.recently_orgasmed:
                    "Your post orgasm cock softens, stopping you from [position_choice.verbing] [the_person.possessive_title] for now."
                    $ position_choice = None
                elif position_choice.guy_energy > mc.energy:
                    "You're too exhausted to continue [position_choice.verbing] [the_person.possessive_title]."
                    $ position_choice = None
                elif position_choice.girl_energy > the_person.energy:
                    #TODO: Add some differentiated dialgoue depending on the position.
                    #TODO: Add "no energy" transitions where you keep fucking her anyways. (double TODO: Add a way of "breaking" her like this)
                    if not girl_in_charge:
                        the_person.char "I'm exhausted [the_person.mc_title], I can't keep this up..."
                    $ position_choice = None
                elif not position_locked: #Nothing major has happened that requires us to change positions, we can have girls take over, strip
                    call girl_strip_event(the_person, position_choice, object_choice) from _call_girl_strip_event_bugfix


        elif isinstance(round_choice, Position): #The only non-strings on the list are positions we are changing to
            call check_position_willingness_bugfix(the_person, round_choice, ignore_taboo = ignore_taboo) from _call_check_position_willingness_bugfix_1
            if _return:
                $ round_choice.redraw_scene(the_person)
                if the_person.has_taboo(position_choice.associated_taboo) and not ignore_taboo:
                    $ position_choice.call_taboo_break(the_person, mc.location, object_choice)
                    $ the_person.break_taboo(position_choice.associated_taboo)
                else:
                    $ position_choice.call_transition(round_choice, the_person, mc.location, object_choice)
                $ position_choice = round_choice

            else: #If she wasn't willing we keep going with what we were doing, so just loop around.
                pass

        elif round_choice == "Strip":
            call strip_menu(the_person, (position_choice.verbing if isinstance(position_choice, Position) else "wooing")) from _call_strip_menu_bugfix

        elif round_choice == "Leave":
            $ finished = True # Unless something stops us the encounter is over and we can end

            # only consider continue when the girl and the mc have enough energy
            if the_person.energy > 15 and mc.energy > 15:
                # In 13% of the cases she takes control regardless of obedience
                # higher chance when she likes taking control lower when she doesn't
                if renpy.random.randint(0,the_person.arousal) + 50 + the_person.get_opinion_score("taking control") * 20 > the_person.obedience or renpy.random.randint(1, 7 - (the_person.get_opinion_score("taking control") * 2)) == 1: #She's disobedient and will take control of the encounter. disobed disobd
                    $ the_person.change_obedience(-3)
                    $ girl_in_charge = True
                    $ finished = False
                    $ guy_orgasms_before_control = report_log.get("guy orgasms", 0)
                    $ has_taken_control = True #After successful position and object choice she will let you know she wants to keep going.
                    $ position_choice = None #She picks the position now, because she has her own list of possibilities

                elif (the_person.arousal > the_person.max_arousal - 30) and (report_log.get("girl orgasms", 0) == 0) and report_log.get("beg finish", 0) == 0: #Within 30 of orgasming and she hasn't cum yet
                    # They're close to their orgasm and beg you to help them finish.
                    $ the_person.call_dialogue("sex_beg_finish")
                    menu:
                        "Give her what she wants.":
                            $ the_person.change_obedience(2)
                            $ report_log["beg finish"] = report_log.get("beg finish", 0) + 1
                            $ finished = False
                            $ position_locked = False

                        "Stop and leave.":
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
        if report_log.get("girl orgasms",0) > 0:
            the_person.arousal = 0 # If she came she's satisfied.
        else:
            the_person.change_arousal(-the_person.arousal/2) #Otherwise they are half as aroused as you leave them.

        mc.condom = False
        mc.recently_orgasmed = False

    if affair_ask_after and private and ask_girlfriend_requirement(the_person) is True and not the_person.relationship == "Single":
        if the_person.love >= 60 and the_person.sluttiness >= 30 - (the_person.get_opinion_score("cheating on men") * 5) and report_log.get("girl orgasms",0) >= 1: #If she loves you enoguh, is moderately slutty, and you made her cum
            call affair_check(the_person, report_log) from _call_affair_check_bugfix

    $ update_person_sex_record(the_person, report_log)

    # We return the report_log so that events can use the results of the encounter to figure out what to do.
    return report_log

label check_position_willingness_bugfix(the_person, the_position, ignore_taboo = False, skip_dialog = False): #Returns if hte person is willing to do this position or not, and charges the appropriate happiness hit if they needed obedience to be willing.
    $ willing = True

    $ the_taboo = the_position.associated_taboo
    if ignore_taboo:
        $ the_taboo = None

    if the_person.effective_sluttiness(the_taboo) >= the_position.slut_requirement:
        if not (skip_dialog or the_person.has_taboo(the_taboo)):
            $ the_person.call_dialogue("sex_accept")

    elif the_person.effective_sluttiness(the_taboo) + (the_person.obedience-100) >= the_position.slut_requirement:
        # She's willing to be commanded to do it. Reduce her happiness by the difference (increase arousal if she likes being submissive)
        python:
            happiness_drop = the_person.effective_sluttiness(the_position.associated_taboo) - the_position.slut_requirement #Our initial conditions mean this is a negative number
            the_person.change_arousal(the_person.get_opinion_score("being submissive")*2)
            the_person.discover_opinion("being submissive")
            the_person.change_happiness(happiness_drop)

        if the_person.has_taboo(the_taboo):
            pass #If there is a taboo being broken we have special taboo break dialogue called from the position.
        else:
            $ the_person.call_dialogue("sex_obedience_accept")

    elif the_person.effective_sluttiness(the_taboo) > the_position.slut_requirement/2:
        # She's not willing to do it, but gives you a soft reject.
        $ the_person.call_dialogue("sex_gentle_reject")
        $ willing = False

    else:
        # You're nowhere close to the required sluttiness, lose some love for even trying.
        python:
            love_loss = the_person.effective_sluttiness(the_taboo) - the_position.slut_requirement #A negative number
            love_loss = round(love_loss/5)
            the_person.change_love(love_loss)
            willing = False

        $ the_person.call_dialogue("sex_angry_reject")

    if willing and (the_position.skill_tag == "Vaginal" or the_position.skill_tag == "Anal") and not mc.condom: #We might need a condom, which means she might say no. TODO: Add an option to pull _off_ a condom while having sex.
        if not ask_for_condom:
            $ ask_for_condom = True
            if the_person.effective_sluttiness() < the_person.get_no_condom_threshold() + 50:
                # she is not slutty enough and we have the condom dialog
                call condom_ask(the_person) from _call_condom_ask_bugfix
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

    if SB_check_fetish(the_person, cum_internal_role):
        "[the_person.possessive_title] eyes your cock greedily. You could put a condom on if you wanted."
        menu:
            "Put on a condom":
                "You pull a condom out of your wallet and tear open the package."
                "[the_person.title] takes a hold of the condom in your hand."
                the_person.char "I want your cum inside me and this is going to stop that."
                the_person.char "You don't really need that, do you?"
                menu:
                    "Insist on condom":
                        mc.name "I think a condom is a good idea."
                        if the_person.get_opinion_score("taking control") > -1:
                            the_person.char "OK. Let me put this another way."
                            "[the_person.title] grabs the condom and throws it off to the side."
                            the_person.char "Either we fuck and you come inside me or we don't fuck at all."
                            menu:
                                "Fuck her raw.":
                                    mc.name "Fine."
                                    the_person.char "I knew you would make the right choice."
                                "Don't":
                                    mc.name "If it's that important to you let's just do something else."
                                    return False
                        else:
                            the_person.char "OK."
                            $ mc.condom = True
                    "Fuck her raw":
                        return True
            "Don't":
                return True

    elif prostitute_role in the_person.special_role:
        if the_person.love < 50:
            the_person.char "Are you remembering that I'm a 'working girl'?"
            the_person.char "That means 'safety first' - always."
            the_person.char "We're going to have to use one of these."
            "She gets out a condom."
            the_person.char "But don't you worry."
            the_person.char "You're going to feel EVERY thing we do."
            menu:
                "Put on condom":
                    call put_on_condom_routine(the_person) from _call_put_on_condom_routine_1

                "Refuse and do something else.":
                    "[the_person.title] doesn't seem like she's going to change her mind."
                    mc.name "If it's that important to you let's just do something else."
                    return False


        elif the_person.sex_record.get("Vaginal Creampies", 0) < 5:
            the_person.char "Normally we would have to use one of these."
            "She gets out a condom."
            the_person.char "But maybe not. What do you think?"
            menu:
                "Condom":
                    call put_on_condom_routine(the_person) from _call_put_on_condom_routine_2

                "No condom":
                    if the_person.get_opinion_score("bareback sex") > 0:
                        the_person.char "Good choice. I hate those things but I have to use them."
                    if the_person.get_opinion_score("creampies") < 0:
                        the_person.char "Just make sure to pull out when you cum, okay?"


        else:
            the_person.char "I know you like to do me bare."
            the_person.char "So maybe no condom today?"
            menu:
                "Agree no condom":
                    if the_person.get_opinion_score("bareback sex") > 0:
                        the_person.char "Good choice. I hate those things but I have to use them."
                    if the_person.get_opinion_score("creampies") < 0:
                        the_person.char "Just make sure to pull out when you cum, okay?"
                    "[the_person.title] smiles at you."
                "Use condom":
                    mc.name "I still think that it's good idea."
                    the_person.char "Alright."

                    call put_on_condom_routine(the_person) from _call_put_on_condom_routine_3

    elif the_person.effective_sluttiness() < condom_threshold:
        # they demand you put on a condom.
        #TODO: Make this dialogue personality based
        if the_person.get_opinion_score("bareback sex") > 0 or the_person.get_opinion_score("creampies") > 0:
            the_person.char "I hate do say it, but you really should wear a condom."
        else:
            the_person.char "Do you have a condom? You're going to have to put one on."

        menu:
            "Put on a condom.":
                call put_on_condom_routine(the_person) from _call_put_on_condom_routine_4

            "Refuse and do something else.":
                "[the_person.title] doesn't seem like she's going to change her mind."
                mc.name "If it's that important to you let's just do something else."
                return False

        if the_person.get_opinion_score("bareback sex") < 0 :
            the_person.char "There we go, a nice big rubbery cock."

    elif the_person.effective_sluttiness() < condom_threshold + 20:
        # They suggest you put on a condom.
        if the_person.get_opinion_score("creampies") > 0 and the_person.get_opinion_score("bareback sex") > 0: # likes everything a condom stops
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
                if the_person.get_opinion_score("bareback sex") > 0:
                    the_person.char "Tell me about it - nothing beats skin on skin."
                if the_person.get_opinion_score("creampies") < 0:
                    the_person.char "Just make sure to pull out when you cum, okay?"

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
                                    "Fuck her raw.":
                                        mc.name "Fine."
                                        the_person.char "I knew you would make the right choice."
                                    "Don't":
                                        mc.name "If it's that important to you let's just do something else."
                                        return False
                            else:
                                the_person.char "Fine, just make it quick!"
                                "[the_person.title] watches impatiently while you roll the condom on."
                                $ mc.condom = True
                        "Relent":
                            mc.name "I suppose not."
                            the_person.char "Thanks, [the_person.mc_title]."
                else:
                    call put_on_condom_routine(the_person) from _call_put_on_condom_routine_6

            "Fuck her raw":
                if the_person.get_opinion_score("creampies") < 0:
                    the_person.char "Alright, but don't want cum inside."

    return True #If we make it to the end of the scene everything is fine and sex can continue. If we returned false we should go back to the position select, as if we asked for something to extreme.

label put_on_condom_routine(the_person):
    if the_person.sex_skills["Oral"] > 3 and the_person.get_opinion_score("giving blowjobs") > 1: #Knows what she's doing
        "[the_person.title] gets a condom out of their own bag and opens it."
        "She carefully puts it in her mouth, behind her teeth."
        "She starts bobbing up and down on your cock."
        "As she goes down on your dick she unrolls the condom onto it with her mouth."
        if the_person.get_opinion_score("being submissive") > 0:
            "She keeps going to the very base of your cock, deepthroating you and entirely covering your cock."
        else:
            "Once she has rolled on about two thirds of the condom she brings her head back up and rolls the rest on with her hand."
    elif the_person.get_opinion_score("giving handjobs") > 0:
        "You pull out a condom from your wallet and rip open the package."
        the_person.char "Let me help with that."
        "[the_person.title] takes the condom out of your hand."
        "She holds it at the top of your cock with one hand as she strokes further and further with the other hand, rolling the condom down onto it."
    elif the_person.get_opinion_score("bareback sex") < 0: # dislikes everything a condom stops
        if the_person.get_opinion_score("taking control") > 0:
            the_person.char "Good choice."
            "You roll the condom onto your cock as [the_person.title] watches eagerly."
        else:
            "[the_person.title] watches impatiently while you roll the condom on."
    elif the_person.get_opinion_score("bareback sex") > 0:
        "You pull out a condom from your wallet and rip open the package. [the_person.title] watches disappointedly while you slide it on."
    else:
        "You pull out a condom from your wallet and rip open the package. [the_person.title] watches while you slide it on."

    $ mc.condom = True
    return

label pick_object_enhanced(the_person, the_position, forced_object = None):
    if the_position is None:
        return None

    $ object_option_list = []
    if the_position is None:
        $ the_person.clear_situational_slut("sex_object")
        $ the_person.clear_situational_obedience("sex_object")
        return None

    python:
        if forced_object:
            #renpy.say("", "Pick object forced: " + forced_object.name)
            picked_object = forced_object
        else:
            for object in mc.location.objects:
                if object.has_trait(position_choice.requires_location):
                    object_option_list.append([object.get_formatted_name(),object]) #Displays a list of objects in the room related to that position and their appropriate bonuses/penalties

            # if we have only one object to pick for position, select it automatically (saves the user for selecting the only obvious choice)
            if len(object_option_list) == 1:
                picked_object = object_option_list[0][1]
            else:
                picked_object = renpy.display_menu(object_option_list,True,"Choice")

            #renpy.say("", "Pick object: " + picked_object.name)
        del object_option_list

    $ the_person.add_situational_slut("sex_object", picked_object.sluttiness_modifier, the_position.verbing + " on a " + picked_object.name)
    $ the_person.add_situational_obedience("sex_object",picked_object.obedience_modifier, the_position.verbing + " on a " + picked_object.name)
    return picked_object

label watcher_check_enhanced(the_person, the_position, the_object, the_report): # Check to see if anyone is around to comment on the characters having sex.
    $ watcher = cheating_check_get_watcher(the_person)
    if watcher:
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
