# Fix for sex mechanic for people who don't have the bugfix branch installed

init 5 python:
    config.label_overrides["fuck_person"] = "fuck_person_bugfix"
    config.label_overrides["check_position_willingness"] = "check_position_willingness_bugfix"

label fuck_person_bugfix(the_person, private= True, start_position = None, start_object = None, skip_intro = False, girl_in_charge = False, hide_leave = False, position_locked = False, report_log = None, affair_ask_after = True):
    # When called fuck_person starts a sex scene with someone. Sets up the encounter, mainly with situational modifiers.
    if report_log is None:
        $ report_log = defaultdict(int) #Holds information about the encounter: what positiosn were tried, how many rounds it went, who came and how many times, etc. Defaultdict sets values to 0 if they don't exist when accessed
        $ report_log["positions_used"] = [] #This is a list, not an int.

    $ finished = False #When True we exit the main loop (or never enter it, if we can't find anything to do)
    $ position_choice = None
    $ object_choice = None

    #Family situational modifiers
    if the_person.has_family_taboo(): #Check if any of the roles the person has belong to the list of family roles.
        $ the_person.add_situational_slut("taboo_sex", -20, "We're related, we shouldn't be doing this.")

    #Cheating modifiers
    $ the_person.discover_opinion("cheating on men")
    if the_person.relationship == "Girlfriend":
        if the_person.get_opinion_score("cheating on men") > 0:
            $ the_person.add_situational_slut("cheating", the_person.get_opinion_score("cheating on men") * 5, "I'm cheating on my boyfriend!")
        else:
            $ the_person.add_situational_slut("cheating", -5 + (the_person.get_opinion_score("cheating on men") * -10), "I can't cheat on my boyfriend!")
    elif the_person.relationship == "Fiancée":
        if the_person.get_opinion_score("cheating on men") > 0:
            $ the_person.add_situational_slut("cheating", the_person.get_opinion_score("cheating on men") * 8, "I'm cheating on my fiancé!")
        else:
            $ the_person.add_situational_slut("cheating", -15 + (the_person.get_opinion_score("cheating on men") * -15), "I could never cheat on my fiancé!")
    elif the_person.relationship == "Married":
        if the_person.get_opinion_score("cheating on men") > 0:
            $ the_person.add_situational_slut("cheating", the_person.get_opinion_score("cheating on men") * 10, "I'm cheating on my husband!")
        else:
            $ the_person.add_situational_slut("cheating", -20 + (the_person.get_opinion_score("cheating on men") * -20), "I could never cheat on my husband!")

    #Privacy modifiers
    if not private:
        if the_person.sluttiness < 50:
            $ the_person.add_situational_slut("public_sex", -10 + the_person.get_opinion_score("public sex") * 5, "There are people watching...")
        else:
            $ the_person.add_situational_slut("public_sex", the_person.get_opinion_score("public sex") * 5, "There are people watching!")

    #Love modifiers. Always applies if negative, but only adds a bonus if you are in private.
    if the_person.love < 0:
        $ the_person.add_situational_slut("love_modifier", the_person.love, "I hate you, get away from me!")
    elif private:
        if girlfriend_role in the_person.special_role: #Girlfriend and affairs gain full Love
            $ the_person.add_situational_slut("love_modifier", the_person.love, "You're my special someone, I love you!")
        elif affair_role in the_person.special_role:
            $ the_person.add_situational_slut("love_modifier", the_person.love, "We may keep it a secret, but I love you!")
        elif the_person.has_family_taboo(): #Family now only gains 1/4 (but this now helps offset the taboo penalty)
            if mother_role in the_person.special_role:
                $ the_person.add_situational_slut("love_modifier", __builtin__.int(the_person.love/4), "Even if it's wrong, a mother should do everything she can for her son!")
            elif sister_role in the_person.special_role:
                $ the_person.add_situational_slut("love_modifier", __builtin__.int(the_person.love/4), "I love my brother, and even if it's wrong I want to be close to him!")
            else: #Generic family one
                $ the_person.add_situational_slut("love_modifier", __builtin__.int(the_person.love/4), "I love you, even though we're related!")
        else: #If you aren't in a relationship with them only half their Love applies.
            $ the_person.add_situational_slut("love_modifier", __builtin__.int(the_person.love/2), "I really like you, let's see where this goes!")

    $ round_choice = "Change" # We start any encounter by letting them pick what position they want (unless something is forced or the girl is in charge)
    $ first_round = True
    while not finished:
        if girl_in_charge:
            # The girls decisions set round_choice here.
            if position_choice is None:
                call girl_choose_position(the_person) from _call_girl_choose_position_bugfix #Get her to pick a position based on what's available #TODO: This function
                $ position_choice = _return #Can be none, if no option was available for her to take.
            if position_choice is None: #There's no position we can take
                "[the_person.title] can't think of anything more to do with you."
                $ round_choice = "Girl Leave"
            elif report_log.get("guy orgasms", 0) > 0 and report_log.get("girl orgasms", 0) > 0: #Both parties have been satisfied
                the_person.char "Whew, that felt amazing. It's good to know it was as good for you as it was for me."
                $ round_choice = "Girl Leave"
            elif report_log.get("girl orgasms", 0) > 0 and the_person.love < 10 and the_person.obedience < 110: #She's cum and doesn't care about you finishing.
                the_person.char "Whew, that felt great. Thanks for the good time [the_person.mc_title]!"
                $ round_choice = "Girl Leave"
            else:
                "[the_person.possessive_title] is in control, and keeps on [position_choice.verbing] you."
                $ round_choice = "Continue"
        else:
            # Forced actions (when the guy is in charge) go here and set round_choice.
            pass
            # if position_choice is None:
            #     $ round_choice = "Change" #Something has kicked our position out, so we need to ask the player what to do.

            # Note: There can be no chance based decisions in this section, because it loops on menu interactions, not on actual rounds of sex. Those go after the "change or continue" loop

        if round_choice is None: #If there is no set round_choice
            #TODO: Add a varient of this list when the girl is in control to ask if you want to resist or ask/beg for something.
            $ option_list = []
            python:
                if position_choice is not None:
                    option_list.append(["Keep " + position_choice.verbing + " her.","Continue"]) #Note: you're prevented from continuing if the energy cost would be too high by the pre-round checks.
                    option_list.append(["Pause and strip her down.","Strip"])

                    if not position_locked and object_choice:
                        option_list.append(["Pause and change position.\n-5 {image=gui/extra_images/arousal_token.png}","Change"])
                        for position in position_choice.connections:
                            if object_choice.has_trait(position.requires_location):
                                appended_name = "Transition to " + position.build_position_willingness_string(the_person) #Note: clothing and energy checks are done inside of build_position_willingness, invalid positiosn marked (disabled)
                                option_list.append([appended_name,position])

                    if not hide_leave: #TODO: Double check that we can always get out
                        option_list.append(["Stop " + position_choice.verbing + " her and leave.", "Leave"]) #TODO: Have this appear differently depending on if you've cum yet, she's cum yet, or you've both cum.

                else:
                    if not position_locked:
                        option_list.append(["Pick a new position.\n-5 {image=gui/extra_images/arousal_token.png}","Change"])
                    if not hide_leave:
                        option_list.append(["Stop and leave.", "Leave"])

            $ round_choice = renpy.display_menu(option_list,True,"Choice") #This gets the players choice for what to do this round.


        # Now that a round_choice has been picked we can do something.
        if round_choice == "Change" or round_choice == "Continue":
            if round_choice == "Change": # If we are changing we first select and transition/intro the position, then run a round of sex. If we are continuing we ignroe all of that
                if start_position is None: #The first time we get here,
                    call pick_position(the_person) from _call_pick_position_bugfix
                    $ position_choice = _return
                else:
                    $ position_choice = start_position

                call pick_object(the_person, position_choice, forced_object = start_object) from _call_pick_object_bugfix
                $ object_choice = _return

                if position_choice and object_choice:
                    call check_position_willingness_bugfix(the_person, position_choice, skip_dialog = True) from _call_check_position_willingness_bugfix
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
                        $ position_choice.call_intro(the_person, mc.location, object_choice)
                    else:
                        $ the_person.change_arousal(-5) #Changing position lowers your arousal slightly
                        $ mc.change_arousal(-5)
                        $ position_choice.call_transition(None, the_person, mc.location, object_choice)

            $ start_position = None #Clear start positions/objects so they aren't noticed next round.
            $ start_object = None
            if position_choice and object_choice: #If we have both an object and a position we're good to go, otherwise we loop and they have a chance to choose again.
                call sex_description(the_person, position_choice, object_choice, private = private, report_log = report_log) from _call_sex_description_bugfix
                $ first_round = False
                if position_choice.requires_hard and mc.recently_orgasmed:
                    "Your post orgasm cock softens, stopping you from [position_choice.verbing] [the_person.possessive_title] for now."
                    $ position_choice = None
                elif position_choice.guy_energy > mc.energy:
                    "You're too exhausted to continue [position_choice.verbing] [the_person.possessive_title]."
                    $ position_choice = None
                elif position_choice.girl_energy > the_person.energy:
                    #TODO: Add some differentiated dialgoue depending on the position.
                    #TODO: Add "no energy" transitions where you keep fucking her anyways. (double TODO: Add a way of "breaking" her like this)
                    the_person.char "I'm exhausted [the_person.mc_title], I can't keep this up..."
                    $ position_choice = None
                else: #Nothing major has happened that requires us to change positions, we can have girls take over, strip
                    call girl_strip_event(the_person, position_choice, object_choice) from _call_girl_strip_event_bugfix


        elif isinstance(round_choice, Position): #The only non-strings on the list are positions we are changing to
            call check_position_willingness_bugfix(the_person, round_choice) from _call_check_position_willingness_bugfix_1
            if _return:
                $ round_choice.redraw_scene(the_person)
                $ position_choice.call_transition(round_choice, the_person, mc.location, object_choice)
                $ position_choice = round_choice

            else: #If she wasn't willing we keep going with what we were doing, so just loop around.
                pass

        elif round_choice == "Strip":
            call strip_menu(the_person, position_choice.verbing) from _call_strip_menu_bugfix

        elif round_choice == "Leave":
            $ finished = True # Unless something stops us the encounter is over and we can end
            if renpy.random.randint(0,the_person.arousal) + 50 > the_person.obedience: #She's disobedient and will take control of the encounter. disobed disobd
                $ the_person.call_dialogue("sex_take_control")
                $ the_person.change_obedience(-3)
                $ girl_in_charge = True
                $ finished = False
                $ position_choice = None #She picks the position now, because she has her own list of possibilities

            elif (the_person.arousal > the_person.max_arousal - 30) and (report_log.get("girl orgasms", 0) == 0) and report_log.get("beg finish", 0) == 0: #Within 30 of orgasming and she hasn't cum yet
                # They're close to their orgasm and beg you to help them finish.
                $ the_person.call_dialogue("sex_beg_finish")
                menu:
                    "Give her what she wants.":
                        $ the_person.change_obedience(2)
                        if "beg finished" in report_log:
                            $ report_log["beg finish"] += 1
                        $ finished = False

                    "Stop and leave.":
                        $ the_person.call_dialogue("sex_end_early")

            elif report_log.get("beg finish", 0) > 0 and report_log.get("girl orgasms", 0) == 0: #You promised to make her cum but didn't
                $ the_person.change_obedience(-5)
                $ the_person.change_happiness(-10)
                $ the_person.change_love(-3)
                the_person.char "But you promised..."
                #TODO: Add some personality specific dialgoue for this

            else: # You end the encounter and nothing special happens.
                #TODO: Add some personality specfic dialogue
                pass




        elif round_choice == "Girl Leave":
            $ finished = True
        $ round_choice = None #Get rid of our round choice at the end of the round to prepare for the next one. By doing this at the end instead of the begining of the loop we can set a mandatory choice for the first one.


    # Teardown the sex modifiers
    $ the_person.clear_situational_slut("love_modifier")
    $ the_person.clear_situational_slut("cheating")
    $ the_person.clear_situational_slut("taboo_sex")
    $ the_person.clear_situational_slut("sex_object")
    $ the_person.clear_situational_obedience("sex_object")

    $ report_log["end arousal"] = the_person.arousal
    if report_log.get("girl orgasms",0) > 0:
        $ the_person.arousal = 0 # If she came she's satisfied.
    else:
        $ the_person.change_arousal(-the_person.arousal/2) #Otherwise they are half as aroused as you leave them.


    $ mc.condom = False
    $ mc.recently_orgasmed = False

    if affair_ask_after and private and ask_girlfriend_requirement(the_person) is True and not the_person.relationship == "Single":
        if the_person.love >= 60 and the_person.sluttiness >= 30 - (the_person.get_opinion_score("cheating on men") * 5) and report_log.get("Climaxes",0) >= 1: #If she loves you enoguh, is moderately slutty, and you made her cum
            call affaire_check(the_person, report_log) from _call_affaire_check_bugfix


    python: #Log all of the different classes of sex, but only once per class.
        types_seen = []
        for position_type in report_log.get("positions_used",[]): #Note: Clears out duplicates
            if position_type.record_class and position_type.record_class not in types_seen:
                the_person.sex_record[position_type.record_class] += 1
                types_seen.append(position_type.record_class)

    # We return the report_log so that events can use the results of the encounter to figure out what to do.
    return report_log

label check_position_willingness_bugfix(the_person, the_position, skip_dialog = False): #Returns if hte person is willing to do this position or not, and charges the appropriate happiness hit if they needed obedience to be willing.
    $ willing = True
    if the_person.effective_sluttiness() >= the_position.slut_requirement:
        if not skip_dialog:
            $ the_person.call_dialogue("sex_accept")

    elif the_person.effective_sluttiness() + (the_person.obedience-100) >= the_position.slut_requirement:
        # She's willing to be commanded to do it. Reduce her happiness by the difference (increase arousal if she likes being submissive)
        $ happiness_drop = the_person.effective_sluttiness() - the_position.slut_requirement #Our initial conditions mean this is a negative number
        $ the_person.change_arousal(the_person.get_opinion_score("being submissive")*2)
        $ the_person.discover_opinion("being submissive")
        $ the_person.change_happiness(happiness_drop)
        $ the_person.call_dialogue("sex_obedience_accept")
        $ willing = True

    elif the_person.effective_sluttiness() > the_position.slut_requirement/2:
        # She's not willing to do it, but gives you a soft reject.
        $ the_person.call_dialogue("sex_angry_reject")
        $ willing = False

    else:
        # You're nowhere close to the required sluttiness, lose some love for even trying.
        $ love_loss = the_person.effective_sluttiness() - the_position.slut_requirement #A negative number
        $ love_loss = round(love_loss/5)
        $ the_person.change_love(love_loss)
        $ the_person.call_dialogue("sex_gentle_reject")
        $ willing = False

    if willing and the_position.skill_tag == "Vaginal" and not mc.condom: #We might need a condom, which means she might say no. TODO: Add an option to pull _off_ a condom while having sex.
        call condom_ask(the_person) from _call_condom_ask_bugfix
        $ willing = _return

    return willing
