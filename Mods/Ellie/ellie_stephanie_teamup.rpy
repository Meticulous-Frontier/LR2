init 1: #Use these transforms for having the two girls observe your research.
    transform character_researcher_1(xoffset = 0, yoffset = 0, zoom = 0.7):
        yalign (0.85 + yoffset)
        yanchor 1.0
        xalign (0.5 + xoffset)
        xanchor 1.0
        xzoom -(zoom)
        zoom zoom

    transform character_researcher_2(xoffset = 0, yoffset = 0, zoom = 0.7):
        yalign (0.85 + yoffset)
        yanchor 1.0
        xalign (0.4 + xoffset)
        xanchor 1.0
        yzoom zoom


init 5 python:
    add_label_hijack("normal_start", "activate_ellie_stephanie_teamup_mod_core")
    add_label_hijack("after_load", "update_ellie_stephanie_teamup_mod_core")

    def ellie_stephanie_teamup_scene_mod_initialization():
        ellie_stephanie_teamup_progression_scene_init()
        return

label activate_ellie_stephanie_teamup_mod_core(stack):
    python:
        ellie_stephanie_teamup_scene_mod_initialization()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_ellie_stephanie_teamup_mod_core(stack):
    python:
        if "ellie_stephanie_teamup_progression_scene" not in globals():
            ellie_stephanie_teamup_progression_scene_init()
        else:
            ellie_stephanie_teamup_progression_scene.compile_scenes(ellie_stephanie_teamup_progression_scene)
        execute_hijack_call(stack)
    return



init 1 python:
    def ellie_stephanie_teamup_progression_scene_0_req(the_group):    #Requirements for the basic scene. Should almost always be true.
        return True

    def ellie_stephanie_teamup_progression_scene_1_req(the_group):    #Requirements for the second stage.
        if the_group[0].sluttiness > 20:
            return True
        return False


    def ellie_stephanie_teamup_progression_scene_action_req(the_person):  #Use this function to determine the requirement for when to actually run the scene itself.
        if time_of_day == 1 and day%7 == 2:
            if mc.business.head_researcher != None:
                return True
        return False

    def ellie_stephanie_teamup_unit_test_func(the_group):
        for person in the_group:
            person.change_slut(30)
            person.change_energy(200)
        mc.change_energy(200)
        return

init 2 python:
    def ellie_stephanie_teamup_progression_scene_compile_scenes(the_progression_scene):
        #WARNING: The order of the following lists is critical! They are referenced based on their indexes!!!
        the_progression_scene.start_scene_list = ["ellie_stephanie_teamup_progression_scene_intro_0", "ellie_stephanie_teamup_progression_scene_intro_1"]
        the_progression_scene.req_list = [ellie_stephanie_teamup_progression_scene_0_req, ellie_stephanie_teamup_progression_scene_1_req]
        the_progression_scene.trans_list = ["ellie_stephanie_teamup_trans_scene_0", "ellie_stephanie_teamup_trans_scene_1"]
        the_progression_scene.final_scene_list = ["ellie_stephanie_teamup_progression_scene_scene_0", "ellie_stephanie_teamup_progression_scene_scene_1"]
        return

    ellie_stephanie_teamup_progression_scene_action = Action("ellie_stephanie_teamup Fuck session", ellie_stephanie_teamup_progression_scene_action_req, "ellie_stephanie_teamup_progression_scene_action_label")

    def ellie_stephanie_teamup_progression_scene_init():  #Run this during init only
        global ellie_stephanie_teamup_progression_scene
        ellie_stephanie_teamup_progression_scene = Progression_Scene(
            compile_scenes = ellie_stephanie_teamup_progression_scene_compile_scenes,
            start_scene_list = [],  #Set via the compile action
            req_list = [],  #Set via the compile action
            trans_list = [],    #Set via the compile action
            final_scene_list = [],  #Set via the compile action
            intro_scene = "ellie_stephanie_teamup_progression_scene_intro_scene", #Scene that plays the first time this scene is run
            exit_scene = "ellie_stephanie_teamup_progression_scene_exit_scene",   #Scene for if the player chooses to exit the scene
            progression_scene_action = ellie_stephanie_teamup_progression_scene_action,      #The action used to call for this progression scene.
            choice_scene = "ellie_stephanie_teamup_progression_scene_choice",   #The action used to let player decide if they want to continue the scene or leave
            stage = -1,     #-1 will play the intro
            person_action = True,   #If this progression scene should run when encountering a person
            business_action = False,    #If this progression scene is a mandatory business event
            is_random = False,  #If this progression scene is a randomly occuring crisis event
            unit_test_func = ellie_stephanie_teamup_unit_test_func,  #Set a custom unit test function to test this progression event. Runs between every cycle
            advance_time = True,    #Currently this is broke. Advance time in the scenes themselves for now...
            is_multiple_choice = False, #If MC can choose what final scene he wants
            multiple_choice_scene = None,   #The scene that lets MC choose which final scene he wants.
            regress_scene_list = [])    #If the scene can regress, fill this with appropriate regression scenes to play between intro and final scenes.
        ellie_stephanie_teamup_progression_scene.compile_scenes(ellie_stephanie_teamup_progression_scene)   #This will populate the scenes that are blank above.


label ellie_stephanie_teamup_progression_scene_action_label(the_person):  #Use (the_person) if this event is attached to a person, otherwise leave params blank, EG: ellie_stephanie_teamup_progression_scene_action_label():
    pass
    call progression_scene_scene_label(ellie_stephanie_teamup_progression_scene, [the_person, mc.business.head_researcher]) from _ellie_stephanie_teamup_progression_scene_call_test_01  #[the_person] parameter should be a list of people in the scene itself, IE [mom], [mom,lily], [sarah,erica,mom], etc
    return

label ellie_stephanie_teamup_progression_scene_intro_scene(the_group):
    $ the_person = the_group[0]
    $ the_researcher = the_group[1]
    $ scene_manager = Scene()
    if mc.location == mc.business.r_div:
        "[the_person.title] walks in the door of the lab. She is excited to see you."
    else:
        $ mc.start_text_convo(the_person)
        the_person "Hey! Can you meet me down in the lab?"
        mc.name "On my way!"
        $ mc.end_text_convo()
        "You walk down to the lab."
        $ mc.change_location(mc.business.r_div)
        $ mc.location.show_background()

    $ scene_manager.add_actor(the_person)
    the_person "Hey [the_person.mc_title]. I've run into a bit of a situation with the nanobots."
    mc.name "Oh? What's wrong?"
    the_person "I recently ran a tweak to some of the code... but the time it takes to get feedback on code revisions takes ages."
    $ scene_manager.add_actor(the_researcher, display_transform = character_center_flipped, position = "walking_away")
    "[the_researcher.possessive_title] walks by as you chat with [the_person.title]."
    the_person "I wish there was some way we could get more immediate test results... the waiting is really hampering my productivity."
    $ scene_manager.update_actor(the_researcher, position = "stand3")
    "[the_researcher.title] suddenly turns to you and [the_person.possessive_title]."
    the_researcher "Wait... did I hear you would like immediate test results?"
    the_person "Errr, I think so?"
    the_researcher "I've got a great idea! We recently put a serum testing clause in place. Let's draft someone and run it!"
    the_person "You want to give them to an employee? I mean, I guess that could work..."
    the_researcher "Of course it would work. Let me just pull up the list here..."
    "[the_researcher.possessive_title] turns and logs in to a nearby computer terminal."
    $ scene_manager.add_actor(the_researcher, display_transform = character_left, position = "standing_doggy")
    $ mc.change_locked_clarity(10)
    "Her ass sways a bit as she logs in and pulls up an employee list."
    the_researcher "Alright... here's my short list of employees to call in. Who do you think we should test [the_researcher.mc_title]?"
    $ scene_manager.update_actor(the_researcher, position = "stand3")
    "[the_researcher.title] stands up and to the side. You look at the computer terminal..."
    $ possible_picks = mc.business.get_requirement_employee_list(obedience_required = 110, exclude_list = [the_person, the_researcher])
    call screen employee_overview(white_list = possible_picks, person_select = True)
    $ pick_1 = _return
    if pick_1 == None:
        mc.name "Sorry, I don't think any of these girls will work..."
        the_researcher "Bullshit. Hang on, I'll pick one..."
        $ pick_1 = get_random_from_list(mc.business.get_requirement_employee_list(obedience_required = 110, exclude_list = [the_person, the_researcher]))
        the_researcher "Ah, here we go."
    the_researcher "I'll go get her."
    $ scene_manager.remove_actor(the_researcher)
    "[the_researcher.title] hurries off, leaving you with [the_person.possessive_title]."
    the_person "Stars, this is happening so fast... I'm not sure I even have any ready!"
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "She quickly turns to one of the research stations. You see her quickly prepare a small tab of nanobots."
    $ scene_manager.update_actor(the_person, position = the_person.idle_pose)
    the_person "There... that should do it. I made up a quick tab of basic bots to test."
    "You talk with [the_person.title] for a bit about her coding optimizations until [the_researcher.possessive_title] returns."
    $ scene_manager.update_actor(the_researcher, display_transform = character_left)
    $ scene_manager.update_actor(pick_1, display_transform = character_center_flipped)
    "She returns with [pick_1.possessive_title]."
    the_researcher "Yes, it is in the employee manual. Don't worry, we'll be observing you the entire time, okay?"
    pick_1 "Okay I guess... Oh, [pick_1.mc_title]? You didn't tell me he was going to be here too."
    mc.name "Yes, I will also be observing."
    pick_1 "I see. I guess that's okay then."
    the_researcher "Alright. Let's get started!"
    "In the corner of the research department, you have a small room designed for private testing. You walk into the room with the three girls."
    $ scene_manager.update_actor(the_person, display_transform = character_researcher_1)
    $ scene_manager.update_actor(the_researcher, display_transform = character_researcher_2)
    $ scene_manager.update_actor(pick_1, display_transform = character_right, position = "sitting")
    "The two researchers stand to one side, while your test subject sits on the exam table."
    "You take the tablet from [the_person.possessive_title]."
    mc.name "Alright, here you go [pick_1.title]. The effects should happen fairly quickly, so I want you to try and be mindful of what you are feeling."
    "You hand the tablet to [pick_1.possessive_title]. She swallows it with a glass of water."
    the_researcher "Alright, while we are waiting, let's go over a quick questionaire. We can compare them between the before and after."
    pick_1 "Okay..."
    "You listen as [the_researcher.possessive_title] starts to ask some standard survey questions... It goes on for a while..."
    $ fetish_serum_increase_opinion(FETISH_BASIC_OPINION_LIST, 2, pick_1)
    $ pick_1.change_arousal(15)
    "However, as you watch [pick_1.title]..."
    $ fetish_serum_increase_opinion(FETISH_BASIC_OPINION_LIST, 2, pick_1)
    $ pick_1.change_arousal(15)
    "She seems to be getting aroused... some of her answers are starting to take longer than they should..."
    if pick_1.opinion_score_masturbating() < 2:
        $ pick_1.max_opinion_score("masturbating", add_to_log = True)
    else:
        $ fetish_serum_increase_opinion(FETISH_BASIC_OPINION_LIST, 2, pick_1)
    $ pick_1.change_arousal(15)
    "[the_researcher.title] seems to be picking up on it also."
    the_researcher "Are you doing okay, [pick_1.name]?"
    pick_1 "I'm sorry... I'm just having a really hard time concentrating... I just... I'm feeling really hot..."
    the_researcher "Ah, can you describe what you are feeling?"
    pick_1 "To be honest, I really feel the need to... touch myself."
    "You hear a small gasp from [the_person.title], but you notice [the_researcher.possessive_title] give a slight smile."
    the_researcher "Would you say that you feel a strong urge to masturbate?"
    pick_1 "Uhhh... yeah... incredibly strong actually..."
    "You can see [the_researcher.title] and [the_person.possessive_title] chatting for a few moments, but can't really tell what they are saying..."
    "Then, you see [the_researcher.possessive_title] look over at you and give a quick wink."
    the_researcher "Alright, remember this is for science. Go ahead and masturbate, and let is know if anything feels different than usual."
    pick_1 "Ahh, umm... okay..."
    the_researcher "If it makes you feel uncomfortable we can have [the_researcher.mc_title] leave the room."
    "You shoot her a quick glare. Thankfully [pick_1.title] doesn't seem to notice."
    pick_1 "No, that's alright. I don't mind..."
    $ scene_manager.update_actor(pick_1, position = "kneeling1")
    if pick_1.vagina_available():
        "[pick_1.possessive_title] repositions herself and slowly runs a hand down between her legs."
        "You watch as she dips a finger into her exposed pussy while using her palm to press down on her clit."
        $ mc.change_locked_clarity(30)
    else:
        "[pick_1.possessive_title] repositions herself and slowly runs a hand down between her legs."
        "Her hand disappears under her clothes as she starts to touch herself."
        $ mc.change_locked_clarity(10)
    pick_1 "Ahh.... mmm..."
    $ pick_1.change_arousal(30)
    "[pick_1.possessive_title] doesn't waste any time. She moans as she touches herself."
    pick_1 "Oh god... it feels so good... I feel like my whole body is on fire..."
    "[pick_1.title] bites her lip and looks you straight in the eyes as she continues to touch herself."
    "Her eyes flicker down to your crotch a couple of times. You can tell she wants you to step in, but you stick to observing."
    $ pick_1.change_arousal(50)
    "You can see [pick_1.possessive_title] has really picked up the pace and eyes are starting to glaze over a bit. She's almost finished."
    pick_1 "Oh fuck... oh!"
    $ pick_1.have_orgasm(half_arousal = False)
    $ mc.change_locked_clarity(50)
    $ pick_1.change_obedience(5)
    $ pick_1.change_slut(2, 50)
    "[pick_1.title]'s legs shake a bit as she starts to orgasm. Her moans echo through the small test room as you watch."
    "Eventually she finishes, slowly moving her hand away from her crotch."
    the_researcher "How do you feel now? Was that helpful?"
    "[pick_1.title] startles at the sudden question."
    pick_1 "Oh! Uhhh... yeah... but I think I need to lay down for a bit..."
    the_researcher "That's fine. We will leave you the room to recover."
    "You step out of the room with [the_researcher.title] and [the_person.possessive_title], leaving the test subject to recover."
    $ scene_manager.remove_actor(pick_1)
    $ scene_manager.update_actor(the_researcher, display_transform = character_center_flipped)
    $ scene_manager.update_actor(the_person, display_transform = character_right)
    mc.name "Well that was insightful. Were you able to make any helpful observations?"
    the_researcher "Yeah, I think so."
    the_person "Yeah... hey umm... did you give her the entire tablet?"
    mc.name "I... yes?"
    the_person "I didn't think about it... that was the amount we usually put in a whole batch of serum..."
    the_researcher "Ahhh, that is why the effects were so immediate. That was actually incredibly insightful then!"
    the_person "Yeah... I think the tweaks I made for efficiency this past week worked..."
    "The two girls talk for a bit about the test. They seem to have learned quite a bit."
    $ get_fetish_basic_serum().add_mastery(2)
    $ mc.log_event("Mastery of " + get_fetish_basic_serum().name + " increased by 2.", "float_text_blue")
    the_researcher "So next time maybe we..."
    the_person "Next time?"
    the_researcher "Yeah? I mean, seems like it would be really helpful to optimize these if we study them more in depth in the future."
    the_person "Yeah, that's true... what do you think, [the_person.mc_title]?"
    mc.name "It makes sense. What kind of basis would be useful?"
    the_person "Well, sometimes I like to look at the code and make optimizations over the weekend... maybe once a week?"
    the_person "I'll finish up optimizations early in the week... maybe we could do this every Wednesday?"
    the_person "That would give me a chance to finalize changes, then have a couple days to analyze results."
    mc.name "Sounds good. [the_researcher.title], can you meet with her every Wednesday morning for these tests? I may not always be able to be here."
    the_researcher "Certainly. Especially if they all turn out as hot as this one!"
    the_person "Ahh, yeah considering the programs, they probably will..."
    mc.name "Perfect. Good work girls."
    "You say goodbye to the girls then step away. You can hear them chatting about the test."
    $ scene_manager.clear_scene()
    "You can now visit the research department every Wednesday morning to join [ellie.title] and [the_researcher.possessive_title] studying the nanobots."
    "As you return to your work, you try to adjust yourself. The scene has left you really turned on. Hopefully in the future you can take more a 'active' role in the research..."
    $ del the_researcher
    return

label ellie_stephanie_teamup_progression_scene_intro_0(the_group):
    $ the_person = the_group[0]
    "This is the most basic intro scene. It should run after you have experienced the intro."
    $ the_person.draw_person()
    the_person "Hey, down to fuck?"
    return

label ellie_stephanie_teamup_progression_scene_intro_1(the_group):
    $ the_person = the_group[0]
    "This is the second intro scene, played after you unlocked it."
    the_person "Hey, I had fun last time when you fucked my ass!"
    return

#For more progression, add more scenes.

label ellie_stephanie_teamup_trans_scene_0(the_group):
    pass
    #This label should probably never be called.
    return

label ellie_stephanie_teamup_trans_scene_1(the_group):
    $ the_person = the_group[0]
    "This is the transition to the second scene."
    the_person "I have another idea though... what if you fucked... my other hole?"
    mc.name "That's a good idea."
    return

label ellie_stephanie_teamup_progression_scene_scene_0(the_group):
    $ the_person = the_group[0]
    "This is the most basic final scene.."
    $ the_person.draw_person()
    the_person "Alright, let's do it!"
    call fuck_person(the_person) from _call_sex_description_ellie_stephanie_teamup_scene_01

    the_person "Whew! that was great!"
    #You probably want to to advance time after this
    # call advance_time from _call_advance_ellie_stephanie_teamup_progression_scene_adv_02
    return

label ellie_stephanie_teamup_progression_scene_scene_1(the_group):
    $ the_person = the_group[0]
    "This is the second scene. I'm not coding it, but you could code it that she gets naked and bends over, preseting her ass here."
    $ the_person.draw_person(position = "standing_doggy")
    the_person "Don't worry, my ass is always ready for you!"
    call fuck_person(the_person) from _call_sex_description_ellie_stephanie_teamup_scene_02

    the_person "Oh my god I hope I can walk tomorrow!"
    #You probably want to to advance time after this
    #call advance_time from _call_advance_ellie_stephanie_teamup_progression_scene_adv_03
    return


label ellie_stephanie_teamup_progression_scene_choice(the_group):
    $ the_person = the_group[0]
    "Use this scene to give MC a chance to bail out."
    "Are you going to fuck her?"
    menu:
        "Fuck her":
            return True
        "Leave":
            return False
    return True

label ellie_stephanie_teamup_progression_scene_exit_scene(the_group):
    $ the_person = the_group[0]
    "Use this scene to show MC bailing out."
    mc.name "Unfortunately, I don't have time to fuck you. Goodbye."
    the_person "Bye!"
    "You stand up and leave the room, leaving the girls to their study session."
    $ clear_scene()
    return






#This is for reusable scenes and functions required for the scene.
#If there are any special functions or scenes you want to add, do it here.
#For example, for the above scene, you could write a script where the girl strips her bottoms and presents her ass to MC.
