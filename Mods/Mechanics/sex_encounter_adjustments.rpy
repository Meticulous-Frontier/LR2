init 5 python:
   config.label_overrides["sex_description"] = "sex_description_enhanced" # Less tedious logic, more time to have sex.
   config.label_overrides["fuck_person"] = "fuck_person_enhanced" # Option to not be forced to continue sex on high sluttiness characters.

label fuck_person_enhanced(the_person, private=True, start_position = None, start_object = None, skip_intro = False, girl_in_charge = False, hide_leave = False):
    #Use a situational modifier to change sluttiness before having sex.
    $ use_love = True
    if any(relationship in [sister_role,mother_role,aunt_role,cousin_role] for relationship in the_person.special_role): #Check if any of the roles the person has belong to the list of family roles.
        $ the_person.add_situational_slut("taboo_sex", -20, "We're related, we shouldn't be doing this.")
        $ use_love = False

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

    if not private:
        $ use_love = False
        if the_person.sluttiness < 50:
            $ the_person.add_situational_slut("public_sex", -10 + the_person.get_opinion_score("public sex") * 5, "There are people watching...")
        else:
            $ the_person.add_situational_slut("public_sex", the_person.get_opinion_score("public sex") * 5, "There are people watching!")

    if use_love or the_person.love < 0:
        if the_person.love > 0:
            $ the_person.add_situational_slut("love_modifier", the_person.love, "I love you and want you close to me!")
        else:
            $ the_person.add_situational_slut("love_modifier", the_person.love, "I hate you, get away from me!")


    python:
        tuple_list = []
        if start_position and (start_position in list_of_positions or start_position in list_of_girl_positions):
            position_choice = start_position
        else:
            if girl_in_charge:
                for position in list_of_girl_positions:
                    if mc.location.has_object_with_trait(position.requires_location):
                        if position.check_clothing(the_person):
                            if position.slut_requirement <= the_person.effective_sluttiness():
                                tuple_list.append(position)
                position_choice = get_random_from_list(tuple_list)
                if not position_choice: #TODO: Add a way for them to decide to actually leave here.
                    position_choice = "Girl Leave" #Needs to be a different flag because "Leave" triggers all of the checks for a girl to convince you to keep going.


            else:
                for position in list_of_positions:
                    if mc.location.has_object_with_trait(position.requires_location):
                        #Note: clothing checks are done in the build_position_willingness_string() check, where it markes them as obstructed and (disabled).
                        tuple_list.append([position.build_position_willingness_string(the_person), position])

                if not hide_leave: #Some events don't let you leave.
                    tuple_list.append(["Leave","Leave"]) #Stop having sex, since cumming is now a locked in thing.
                position_choice = renpy.display_menu(tuple_list,True,"Choice")


    if not position_choice == "Leave":
        python:
            tuple_list = []
            if start_object and start_object in mc.location.objects:
                object_choice = start_object
            elif girl_in_charge:
                for object in mc.location.objects:
                    if object.has_trait(position_choice.requires_location):
                        tuple_list.append (object)

                tuple_list.sort(key = lambda obj: obj.sluttiness_modifier, reverse = True)
                object_choice = tuple_list[0] #We know there was a valid object or the position couldn't have been selected. Get the most slutty object possible.

            else:
                renpy.say("","Where do you do it?")

                for object in mc.location.objects:
                    if object.has_trait(position_choice.requires_location):
                        tuple_list.append([object.get_formatted_name(),object]) #Displays a lsit of objects in the room related to that position and their appropriate bonuses/penalties

                object_choice = renpy.display_menu(tuple_list,True,"Choice")
            the_person.add_situational_slut("sex_object",object_choice.sluttiness_modifier,"using a " + object_choice.name)
            the_person.add_situational_obedience("sex_object",object_choice.obedience_modifier, "using a " + object_choice.name)
        $ start_round = 0
        if skip_intro:
            $ start_round = 1
        call sex_description(the_person, position_choice, object_choice, start_round, private=private, girl_in_charge = girl_in_charge) from _call_sex_description_fuck_person_enhanced

    else: #The position choice was "Leave" and we want to add some extra stuff.
        if the_person.effective_sluttiness() > 60:
            if renpy.random.randint(0,the_person.arousal) + 50 < the_person.obedience:
                $ the_person.call_dialogue("sex_take_control")
                $ the_person.change_obedience(-3)
                
                menu:
                  "Apologize profously for having made a mess and bid your farewells.": # I got work to do, bills to pay alright. Can't be used as a toy all day.
                     if the_person.get_opinion_score("being submissive") > 0 or the_person.arousal > 80:
                        $ the_person.call_dialogue("sex_beg_finish")
                        menu:
                           "Keep going.":
                              $ the_person.change_obedience(2)
                              call fuck_person_enhanced(the_person, private, start_position, start_object, skip_intro = True, girl_in_charge = girl_in_charge, hide_leave = True) from _call_fuck_person_enhanced #Redo all of this but don't let them leave. Start position and start_object will normally be None

                           "Leave.":
                              $ the_person.call_dialogue("sex_end_early")
                     else:
                        $ the_person.call_dialogue("sex_end_early")

                  "See where this is going":
                     call fuck_person_enhanced(the_person, private, start_position, start_object, skip_intro = True, girl_in_charge = True) from _call_fuck_person_enhanced_1

            elif the_person.arousal > 80:
                # They're close to their orgasm and beg you to help them finish.
                $ the_person.call_dialogue("sex_beg_finish")
                menu:
                    "Keep going.":
                        $ the_person.change_obedience(2)
                        call fuck_person_enhanced(the_person, private, start_position, start_object, skip_intro = True, girl_in_charge = girl_in_charge, hide_leave = True) from _call_fuck_person_enhanced_2 #Redo all of this but don't let them leave. Start position and start_object will normally be None

                    "Leave.":
                        $ the_person.call_dialogue("sex_end_early")

            else: #They're slutty but they just say they're sad to end.
                $ the_person.call_dialogue("sex_end_early")
        else:
            $ the_person.call_dialogue("sex_end_early")


    $ the_person.clear_situational_slut("love_modifier")
    $ the_person.clear_situational_slut("cheating")
    $ the_person.clear_situational_slut("taboo_sex")
    $ the_person.clear_situational_slut("sex_object")
    $ the_person.clear_situational_obedience("sex_object")
    $ mc.condom = False
    return


   
label sex_description_enhanced(the_person, the_position, the_object, round, private = True, girl_in_charge = False):
   #NOTE: the private variable decides if you are in private or not relative to the location you are in. If True other people in the room do not get a chance to interact.

   ##Describe the current round

   ## FIRST ROUND EXCLUSIVE STUFF ##
    if round == 0: ##First round means you just started, so do intro stuff before we get on with it. Also where we check to see if they are into having this type of sex.
        if the_person.effective_sluttiness() >= the_position.slut_requirement: #The person is slutty enough to want to have sex like this.
            $ the_person.call_dialogue("sex_accept")
            if the_position.skill_tag == "Vaginal": #She may demand you put on a condom.
                call condom_ask(the_person) from _call_condom_ask_sex_description_enhanced_1
                if not _return:
                    call fuck_person_enhanced(the_person, private, girl_in_charge = girl_in_charge) from _call_fuck_person_sex_description_enhanced_1
                    return

            $ the_position.call_intro(the_person, mc.location, the_object, round)
            $ the_position.redraw_scene(the_person)

        else: #The person isn't slutty enough for this. First, try and use obedience. If you still fail, but by a little, she rebukes you but you keep seducing her. Otherwise, the entire thing ends.
            if the_person.effective_sluttiness() + (the_person.obedience-100) >= the_position.slut_requirement:
                #You can use obedience to do it.
                $ the_person.call_dialogue("sex_obedience_accept")
                if the_position.skill_tag == "Vaginal":
                    call condom_ask(the_person) from _call_condom_ask_sex_description_enhanced_2
                    if not _return:
                        call fuck_person_enhanced(the_person, private, girl_in_charge = girl_in_charge) from _call_fuck_person_sex_description_enhanced_2
                        return
                $ the_position.redraw_scene(the_person)
                $ change_amount = the_position.slut_requirement - the_person.sluttiness
                $ the_person.change_happiness(-change_amount) #She looses happiness equal to the difference between her sluttiness and the requirement. ie the amount obedience covered.
                $ the_position.call_intro(the_person, mc.location, the_object, round)
                $ the_position.redraw_scene(the_person)
            else:
               #No amount of obedience will help here. How badly did you screw up?
                if the_person.effective_sluttiness() < the_position.slut_requirement/2: #Badly, not even half way to what you needed
                    $ the_position.redraw_scene(the_person,emotion="angry")
                    $ the_person.change_happiness(-5) #She's pissed you would even try that
                    $ the_person.call_dialogue("sex_angry_reject")
                    return #Don't do anything else, just return.
                else:
                    $ the_person.call_dialogue("sex_gentle_reject")
                    call fuck_person_enhanced(the_person, private, girl_in_charge = girl_in_charge) from _call_fuck_person_sex_description_enhanced_3 #Gives you a chance to fuck them some other way, but this path is ended by the return right after you finish having sex like that.
                    return
   
    if round > 1 or round == 0:
        ## ONCE WE HAVE DONE FIRST ROUND CHECKS WE GO HERE ##
        $ the_position.call_scene(the_person, mc.location, the_object, round) #HERE IS WHERE THE SCENE SCRIPT IS CALLED
        $ mc.listener_system.fire_event("sex_event", the_person = the_person, the_position = the_position, the_object = the_object)

        $ change_amount = the_position.girl_arousal + (the_position.girl_arousal * mc.sex_skills[the_position.skill_tag] * 0.1) #How much we increase her arousal.
        if the_position.skill_tag == "Vaginal":
            $ the_person.discover_opinion("bareback sex")
            if mc.condom:
                $ change_amount += -2 * the_person.get_opinion_score("bareback sex")
            else:
                $ change_amount += 2 * the_person.get_opinion_score("bareback sex")

        if the_position.opinion_tags:
            python:
                for opinion_tag in the_position.opinion_tags:
                    change_amount += the_person.get_opinion_score(opinion_tag) #Add a bonus or penalty if she likes or dislikes the position.
                    the_person.discover_opinion(opinion_tag)

        if the_person.sluttiness + 1 > the_position.slut_cap:
            $ slut_report = "Position Max Reached."
        else:
            $ slut_report = the_person.change_slut_temp(1)

        if the_person.arousal > the_position.slut_cap: #She might be too turned on to be impressed by this position any more.
            if the_person.sluttiness > the_position.slut_cap: #She's too slutty to find this interesting.
                $ mc.log_event(the_person.title + ": Bored by position. Arousal gain halved.", "float_text_red")
                $ change_amount = change_amount/2 #Low sluttiness girls can be made to cum by kissing, higher sluttiness girls require more intense positions.
                #TODO: add a "sex_bored" dialogue option that can be called, asking for a more intense position.

        $ the_person.change_arousal(change_amount) #The girls arousal gain is the base gain + 10% per the characters skill in that category.
        $ mc.change_arousal(the_position.guy_arousal + (the_position.guy_arousal * the_person.sex_skills[the_position.skill_tag] * 0.1)) # The same calculation but for the guy

        ## POST ROUND CALCULATION AND DECISIONS PAST HERE ##
        if the_person.arousal >= 100:
            #She's climaxing.
            #$ the_person.call_dialogue("climax_responses") #We now use a position specific orgasm part of the scene.
            #$ the_position.redraw_scene(the_person,emotion="orgasm")
            $ mc.listener_system.fire_event("girl_climax", the_person = the_person, the_position = the_position, the_object = the_object)
            $ the_position.call_orgasm(the_person,mc.location, the_object, round)
            $ the_position.current_modifier = None
            if the_person.sluttiness > the_person.core_sluttiness and the_person.core_sluttiness < the_position.slut_cap:
                $ the_person.change_slut_core(1)
                $ the_person.change_slut_temp(-1)
            $the_person.change_happiness(2) #Orgasms are good, right?
        else:
            $the_person.call_dialogue("sex_responses")

        ## IF OTHER PEOPLE ARE AROUND SEE WHAT THEY THINK ##
        if not private:
            $ other_people = [person for person in mc.location.people if person is not the_person] #Build a list with all the _other_ people in the room other than the one we're fucking.
            $ watcher = get_random_from_list(other_people) #Get a random person from the people in the area, if there are any.
            if watcher:
                # NOTE: the dialogue here often draws the person talking with various emotions or positions, so we redraw the scene after we call them.
                $ watcher.call_dialogue("sex_watch", the_sex_person = the_person, the_position = the_position) #Get the watcher's reaction to the people having sex. This might include dialogue calls from other personalities as well!
                $ the_position.redraw_scene(the_person)
                $ the_person.call_dialogue("being_watched", the_watcher = watcher, the_position = the_position) #Call her response to the person watching her.
                $ the_person.change_arousal(the_person.get_opinion_score("public sex"))
                $ the_person.discover_opinion("public sex")

        $ strip_chance = the_person.effective_sluttiness() - the_person.outfit.slut_requirement
        $ the_clothing = the_person.outfit.remove_random_any(exclude_feet = True, do_not_remove = True)
        if renpy.random.randint(0,100) < strip_chance and the_clothing:
            $ ask_chance = renpy.random.randint(0,100)
            if ask_chance < the_person.obedience - the_person.arousal:
                $ the_position.call_strip_ask(the_person, the_clothing, mc.location, the_object, round)
            else:
                $ the_position.call_strip(the_person, the_clothing, mc.location, the_object, round) #If a girl's outfit is less slutty than she is currently feeling (with arousal factored in) she will want to strip stuff off.

    #TODO: This is where we check to see if a girl seizes initative during an encounter.
    #TODO: This is where a girl might request a different position (and be happy if you follow through)

    ##Ask how you want to keep fucking her or find out how she keeps fucking you##
    $ position_choice = "Keep Going" #Default value just to make sure scope is correct.
    python:
        if (mc.arousal >= 100):
            "You're past your limit, you have no choice but to cum!"
            position_choice = "Finish"
        else:
            if girl_in_charge:
                renpy.say("",the_person.title +  " is taking the lead. She keeps " + the_position.verb + "ing you.")
                position_choice = the_position
                #TODO: this is where we perform any changes for the girl.
                if not the_person.get_opinion_score("taking control") > 0:               
                    if renpy.random.randint(0, 100) > 70: # Give the player a chance to get back in charge without having to wait out the encounter.                  
                        renpy.say("", "[the_person.title] doesn't seem to mind not being completely in charge.")
                        tuple_list = []
                        tuple_list.append(["Keep going.",the_position])
                        tuple_list.append(["Change it up.","Pull Out"])
                        tuple_list.append(["Strip her down.","Strip"])
                        for position in the_position.connections:
                            if the_object.has_trait(position.requires_location):
                                appended_name = "Change to " + position.build_position_willingness_string(the_person) #Note: clothing check is now done in build_position_willingness_string() call and marks them as (disabled)
                                tuple_list.append([appended_name,position])
                        position_choice = renpy.display_menu(tuple_list,True,"Choice")
            else:
                tuple_list = []
                tuple_list.append(["Keep going.",the_position])
                tuple_list.append(["Back off and change positions.","Pull Out"])
                if (mc.arousal > 80): #Only let you finish if you've got a high enough arousal score. #TODO: Add stat that controls how much control you have over this.
                    tuple_list.append(["Cum!","Finish"])
                tuple_list.append(["Strip her down.","Strip"])
                for position in the_position.connections:
                    if the_object.has_trait(position.requires_location):
                        appended_name = "Change to " + position.build_position_willingness_string(the_person) #Note: clothing check is now done in build_position_willingness_string() call and marks them as (disabled)
                        tuple_list.append([appended_name,position])
                position_choice = renpy.display_menu(tuple_list,True,"Choice")

    if position_choice == "Finish":
        $ the_position.current_modifier = None
        $ the_position.call_outro(the_person, mc.location, the_object, round)
        $ mc.reset_arousal()
        # TODO: have you finishing bump her arousal up so you might both cum at once.

    elif position_choice == "Strip":
        call strip_menu(the_person) from _call_strip_menu_sex_description_enhanced_1
        $ the_position.redraw_scene(the_person)
        call sex_description_enhanced(the_person, the_position, the_object, round = 1, private = private, girl_in_charge = girl_in_charge) from _call_sex_description_enhanced_1

    elif position_choice == "Pull Out": #Also how you leave if you don't want to fuck till you cum.
        $ the_position.current_modifier = None
        $ mc.condom = False
        call fuck_person_enhanced(the_person, private, girl_in_charge = girl_in_charge) from _call_fuck_person_sex_description_enhanced_4

    else:
        if not position_choice == the_position: #We are changing to a new position.
            $ the_position.current_modifier = None
            if the_person.effective_sluttiness() >= position_choice.slut_requirement: #The person is slutty enough to want to have sex like this. Higher arousal can get you up to a +50 slutiness boost.
                $ the_person.call_dialogue("sex_accept")
                $ the_position.call_transition(position_choice, the_person, mc.location, the_object, round)
            else: #The person isn't slutty enough for this. First, try and use obedience. If you still fail, but by a little, she rebukes you but you keep seducing her. Otherwise, the entire thing ends.
                if the_person.effective_sluttiness() + (the_person.obedience-100) >= position_choice.slut_requirement:
                    #You can use obedience to do it.
                    $ change_amount = the_person.effective_sluttiness() - the_person.sluttiness
                    $ the_position.redraw_scene(the_person,emotion = "sad")
                    $ the_person.change_happiness(-change_amount) #She looses happiness equal to the difference between her sluttiness and the requirement. ie the amount obedience covered.
                    $ the_person.call_dialogue("sex_obedience_accept")
                    $ the_position.call_transition(position_choice, the_person, mc.location, the_object, round)
                else:
                    #No amount of obedience will help here. How badly did you screw up?
                    if (the_person.effective_sluttiness() < (position_choice.slut_requirement/2)): #Badly, not even half way to what you needed
                        $ the_person.change_happiness(-5) #She's pissed you would even try that
                        $ the_person.change_love(-1)
                        $ the_person.call_dialogue("sex_angry_reject")
                        return #Don't do anything else, just return.
                    else:
                        $ the_position.call_transition(position_choice, the_person, mc.location, the_object, round)
                        $ the_person.call_dialogue("sex_gentle_reject")
                        call sex_description_enhanced(the_person, the_position, the_object, round = 1, private = private, girl_in_charge = girl_in_charge) from _call_sex_description_enhanced_2
                        $ position_choice = the_position

        call sex_description_enhanced(the_person, position_choice, the_object, round+1, private = private, girl_in_charge = girl_in_charge) from _call_sex_description_enhanced_3
    return