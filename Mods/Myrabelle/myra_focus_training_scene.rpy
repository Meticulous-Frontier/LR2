# This file contains the details of Myra's focus training scenes.
# This scene will be callable on demand via Myra's role.
# Starts off with basic back massage while she is playing games. Progression:
# Back rub > Grope > Sit on lap with fingering > Assjob > Anal
# Each scene progresses based on sluttiness AND on Myra's focus level.
# Focus has increased chance of increasing based on suggestability.
# If Myra is in trance, give MC a chance to raise Focus at the end of the scene if it is below MC's value for free.



init 1 python:
    def myra_focus_progression_scene_0_req(the_group):    #Requirements for the basic scene. Should almost always be true.
        return True

    def myra_focus_progression_scene_1_req(the_group):    #Requirements for grope scene
        if the_group[0].sluttiness > 20:
            return True
        return False

    def myra_focus_progression_scene_2_req(the_group):    #Requirements for fingering
        if the_group[0].sluttiness > 40:
            return True
        return False

    def myra_focus_progression_scene_3_req(the_group):    #Requirements for assjob scene
        if the_group[0].sluttiness > 60:
            return True
        return False

    def myra_focus_progression_scene_4_req(the_group):    #Requirements for anal
        if the_group[0].sluttiness > 80:
            return True
        return False


    def myra_focus_progression_scene_action_req(the_person):  #Use this function to determine the requirement for when to actually run the scene itself.
        return True
        if the_person.location == gaming_cafe and myra_last_focus_train_day() < day:
            return True
        return False

    def myra_focus_unit_test_func(the_group):
        for person in the_group:
            person.change_slut(10)
            person.change_energy(200)
        mc.change_energy(200)
        return

init 2 python:
    def myra_focus_progression_scene_compile_scenes(the_progression_scene):
        #WARNING: The order of the following lists is critical! They are referenced based on their indexes!!!
        the_progression_scene.start_scene_list = ["myra_focus_progression_scene_intro_0", "myra_focus_progression_scene_intro_1", "myra_focus_progression_scene_intro_2", "myra_focus_progression_scene_intro_3", "myra_focus_progression_scene_intro_4"]
        the_progression_scene.req_list = [myra_focus_progression_scene_0_req, myra_focus_progression_scene_1_req, myra_focus_progression_scene_2_req, myra_focus_progression_scene_3_req, myra_focus_progression_scene_4_req]
        the_progression_scene.trans_list = ["myra_focus_trans_scene_0", "myra_focus_trans_scene_1", "myra_focus_trans_scene_2", "myra_focus_trans_scene_3", "myra_focus_trans_scene_4"]
        the_progression_scene.final_scene_list = ["myra_focus_progression_scene_0", "myra_focus_progression_scene_1", "myra_focus_progression_scene_2", "myra_focus_progression_scene_3", "myra_focus_progression_scene_4"]
        # the_progression_scene.regress_scene_list = []   #Add labels for regression here if desired.
        return

    myra_focus_progression_scene_action = Action("Train her Focus", myra_focus_progression_scene_action_req, "myra_focus_progression_scene_action_label")

    def myra_focus_progression_scene_init():  #Run this during init only
        global myra_focus_progression_scene
        myra_focus_progression_scene = Progression_Scene(
            compile_scenes = myra_focus_progression_scene_compile_scenes,
            start_scene_list = [],  #Set via the compile action
            req_list = [],  #Set via the compile action
            trans_list = [],    #Set via the compile action
            final_scene_list = [],  #Set via the compile action
            intro_scene = "myra_focus_progression_scene_intro_scene", #Scene that plays the first time this scene is run
            exit_scene = "myra_focus_progression_scene_exit_scene",   #Scene for if the player chooses to exit the scene
            progression_scene_action = myra_focus_progression_scene_action,      #The action used to call for this progression scene.
            choice_scene = "myra_focus_progression_scene_study_choice",   #The action used to let player decide if they want to continue the scene or leave
            stage = -1,     #-1 will play the intro
            person_action = False,   #If this progression scene should run when encountering a person
            business_action = False,    #If this progression scene is a mandatory business event
            is_random = False,  #If this progression scene is a randomly occuring crisis event
            unit_test_func = myra_focus_unit_test_func,  #Set a custom unit test function to test this progression event. Runs between every cycle
            advance_time = True,    #Currently this is broke. Advance time in the scenes themselves for now...
            is_multiple_choice = False, #If MC can choose what final scene he wants
            multiple_choice_scene = None,   #The scene that lets MC choose which final scene he wants.
            regress_scene_list = [])    #If the scene can regress, fill this with appropriate regression scenes to play between intro and final scenes.
        myra_focus_progression_scene.compile_scenes(myra_focus_progression_scene)   #This will populate the scenes that are blank above.



label myra_focus_progression_scene_action_label(the_person):  #Use (the_person) if this event is attached to a person, otherwise leave params blank, EG: myra_focus_progression_scene_action_label():

    call progression_scene_label(myra_focus_progression_scene, [the_person]) from _myra_focus_progression_scene_call_test_01  #[the_person] parameter should be a list of people in the scene itself, IE [mom], [mom,lily], [sarah,erica,mom], etc
    return

label myra_focus_progression_scene_intro_scene(the_group):
    $ the_person = the_group[0]
    $ the_person.draw_person(emotion = "sad")
    $ myra.event_triggers_dict["can_train_focus"] = True
    the_person "Hey [the_person.mc_title]."
    mc.name "Hey. How are you doing?"
    "[the_person.possessive_title] sighs."
    the_person "Oh, not so good. I just can't get that tournament out of my head."
    the_person "I can't believe I choked! It was just the whole atmosphere of it. There was so much pressure... I felt like I couldn't focus!"
    mc.name "That is understandable. It was your first public tournament, right?"
    the_person "I know, I just feel like I let my whole team down."
    "You shrug your shoulders."
    mc.name "I'm sure that as you gain more experience, you'll learn to ignore the noise and focus on the game better."
    the_person "I know, I just wish there was some way to fast track that, you know?"
    the_person "I've tried putting on loud music or youtube, but it just isn't the same as having real human interaction."
    mc.name "Hmmm..."
    "You think about it for a minute."
    mc.name "What if I helped distract you?"
    the_person "Huh? What do you mean?"
    mc.name "I mean, I have nothing going on right now. You play some, and I'll sit beside you and watch and talk to you. Ask you questions. That sort of thing."
    mc.name "You'll have to divide your attention between the two. It will be good focus training for you."
    the_person "I don't know... I guess we could try and see though?"
    the_person "Let me just grab an energy drink. I'll meet you at the PC's over there."
    "[the_person.title] points to a group of PCs."
    $ clear_scene()
    "You head over and sit down."
    "Your job now is to distract [the_person.possessive_title] as she plays the game. You wonder if you can make conversation enough to distract her?"
    "You wonder if there is anythign else you could do to distract her also."
    the_person "Alright, let's get this started."
    $ the_person.draw_person(position = "sitting")
    "[the_person.title] sits down at the desk, logs in and loads up the game."
    "Soon she is in a solo queue for some capture the point style pvp matches."
    "It's a 5v5 format with 3 king of the hill style points. Holding points and scoring kills grants your team points, and the first to 500 wins."
    "She starts playing and you watch as she starts out. She joins a team fight at the center point, fighting 4 on 4. She's doing great!"
    the_person "Hey, aren't you supposed to like... distract me or something?"
    mc.name "Right! So... umm.... did you hear about the new pirate movie?"
    the_person "I... are you telling me shitty jokes..."
    mc.name "Yes, it IS rated R!"
    "You drag out the letter, and she just rolls her eyes and keeps playing."
    "She easily pushes her team to control the center point, wiping the four enemy players in the process."
    the_person "This isn't working. Is that the best you can do?"
    "You desperately try to come up with something to talk about."
    mc.name "So, where do you and [alexia.name] know each other from?"
    the_person "Ah, we used to live in the same neighborhood growing up. Our mom's were friends and we use to hang out a lot, even though I was older than her."
    the_person "Sometimes I would even babysit... SHIT."
    "[the_person.title] pushed for the far point, but her team held back, and she now finds herself in a 2v1 on the far point."
    "Now is the time to push for answers and distract her."
    mc.name "That's neat. Do you two still hang out?"
    the_person "Hang out? I... I don't..."
    "[the_person.possessive_title] is trying to focus on the fight, but you keep pushing."
    mc.name "I mean, I know I see her around here on weekends, but do you two still get together?"
    the_person "Not really... I mean... we kinda went separate ways... I... YES!"
    "[the_person.possessive_title] manages to score a kill, then promptly disengages from the remaining enemy. They wasted valuable time defending their close point from her."
    mc.name "Why not? I mean, games are better played together, and if you got together to play I'm sure you would enjoy it."
    "[the_person.title] appears to be thoughtful about it as she moves to her next fight."
    the_person "You know, that's not a bad idea. She's a sweet girl, and it's not like having friends is such a bad thing."
    "[the_person.possessive_title] moves in to another group fight at the center point. Her team is getting beaten there badly, it looks like it is down to 3v2, and the two on her side are low on health."
    "[the_person.title] moves in to attack, when you notice her shoulders scrunching and she gets tense."
    mc.name "You get really tense when you play this game. Maybe it would be distracting if I tried helping you relax. May I?"
    the_person "I... I don't know what you have in mind, but go ahead..."
    "You stand up and move behind [the_person.possessive_title]. You put your hands on her shoulders and start to rub her back."
    the_person "Hey that's... ahhhh that feels nice..."
    "Her shoulders start to relax as your strong hands explore her shoulder blades. They seem very tense, so you use strong pressure to try and relax some of it away."
    mc.name "Damn, you are tense, girl! Let me try to work on some of this."
    the_person "That's... That is kind of distracting... wow..."
    "[the_person.title] tries to attack an enemy, but doesn't notice when another enemy joins the fight, making it 4v3."
    "Suddenly, the group stun locks her and easily spikes her down."
    the_person "Fuck! I can't play when you do that... its so..."
    mc.name "Distracting? Sounds like you just need to focus."
    the_person "Hmm... yeah you're right..."
    "You get to work on the tension in [the_person.possessive_title]'s neck and shoulders. A couple times when you find particularly tense muscles you hear a gasp as your massage them."
    $ the_person.change_slut(1, 40)
    $ the_person.change_happiness(2)
    $ the_person.change_love(1, 40)
    $ the_person.change_obedience(2)
    "You continue as [the_person.title] plays through a series of matches. Sometimes during particularly difficult fights, you feel her tense up, and you fight the tension away with your hands."
    "Overall, she does pretty good, but definitely not as dominating as she normally is. You feel like at the end of it she might have actually made some progress."
    "At the end of her last match, she logs off the game and stands up."
    $ the_person.draw_person()
    mc.name "So... have you thought about it?"
    the_person "You know, I think that might actually have worked..."
    mc.name "Yeah, but I mean about the other thing we talked about."
    the_person "What other thing?"
    mc.name "Why don't you invite [alexia.name] to hang out sometime?"
    the_person "You know what? I'm going to. I'm going to call her right now."
    "[the_person.possessive_title] pulls out her phone. She dials her friend from her contacts."
    the_person "Hey girl! Yeah it's me. Hey, I was just wondering something..."
    the_person "Do you have any time free soon? I was thinking maybe we could get together. Maybe you could come out to the cafe and just hang out after I close up?"
    if day%7 == 4:
        the_person "Oh!... tonight? Yeah! That would be great! Yeah we could stay up late and play anything, that would be fun!"
        "Wow, so tonight [the_person.title] and [alexia.title] are going to get together..."
    else:
        the_person "Oh! Yeah I could do Friday night! We could stay up late and play anything! That would be fun!"
        "Hmm, so friday [the_person.title] and [alexia.title] are going to get together..."
    "Maybe you should swing by? Just to say hello?"
    the_person "Okay girl. Yeah I'll text you. Sounds good! Bye!"
    "[the_person] hangs up the phone then looks at you."
    the_person "You know what? I'm glad you swung by. Do you think, if you ever have some spare time, we could do more focus training?"
    the_person "I could pay you, if you need, I don't expect you to do it for free."
    the_person "You could be like my coach! Even though you don't play much yourself, you still have an idea of how it works and seem to have a knack for helping me improve."
    mc.name "I don't want to make any promises, but I think I can do that."
    the_person "Okay! Just swing by and let me know whenever you have time."
    "You say goodbye to [the_person.title] and head out."
    $ clear_scene()
    "Training [the_person.possessive_title]'s focus will be beneficial to her career in esports. You wonder if any of your serums could help out."
    "You bet that you could probably offer to get her an energy drink when you train her and dose it..."
    "Would increasing her suggestability make it easier to train her focus? You imagine so."
    "You can now train [the_person.title]'s focus once per day."
    "[the_person.title] and [alexia.title] are getting together on Friday night. You make a note to swing by see what they are up to..."
    call advance_time from _call_advance_myra_focus_progression_scene_adv_01
    return

label myra_focus_progression_scene_intro_0(the_group):
    $ the_person = the_group[0]
    $ the_person.draw_person()
    the_person "Hey, want to help me with my training today?"
    the_person "I really feel like we are making progress with my focus, but I know it takes up a big chunk of your time."
    return

label myra_focus_progression_scene_intro_1(the_group):
    $ the_person = the_group[0]
    the_person "Hey, want to help me with my training?"
    "[the_person.title] looks around the cafe. She spots an area near the back that is dark with no one around. She nods towards it."
    the_person "There's no one in the back corner... It felt really nice last time..."
    $ mc.change_locked_clarity(10)
    if the_person.tits_available():
        the_person "Plus I think you'll find that you'll have easy access to the girls..."
    return

label myra_focus_progression_scene_intro_2(the_group):
    $ the_person = the_group[0]
    the_person "Hey, want to help me with my training?"
    "[the_person.title] looks around the cafe. She spots an area near the back that is dark with no one around. She nods towards it."
    the_person "There's no one in the back corner... I'll sit on your lap again and... you know..."
    $ mc.change_locked_clarity(20)
    if the_person.vagina_available():
        "She lowers her voice to a whisper."
        the_person "Plus, I'm not wearing any panties..."
    return

label myra_focus_progression_scene_intro_3(the_group):
    $ the_person = the_group[0]
    the_person "Hey, want to help me with my *training*?"
    "The inflection in her voice shifts when she says training, making it clear she is really more interested in just having your cock against her bare ass..."
    "[the_person.title] looks towards the back of the cafe and nods towards it."
    the_person "I've started closing that section when I think you might swing by. We won't be disturbed if you want to..."
    $ mc.change_locked_clarity(30)
    return

label myra_focus_progression_scene_intro_4(the_group):
    $ the_person = the_group[0]
    the_person "Hey, is it time to fuck my ass again?"
    mc.name "Don't you mean focus training?"
    the_person "Of course! I mean, if I can win a game while your big dick is in my ass, nothing could possibly get in my way!"
    "[the_person.title] looks towards the back of the cafe and nods towards it."
    the_person "The VIP section in the back is closed. Come on... you know you want to!"
    $ mc.change_locked_clarity(50)
    "[the_person.possessive_title] is eager to drag you to the back of the gaming cafe and stuff her ass with your cock while she plays a game."
    return

#For more progression, add more scenes.

label myra_focus_progression_scene_0(the_group, scene_transition = False):  #Innocent back massage
    $ the_person = the_group[0]
    "You walk over to the PC where [the_person.title] is sitting."
    $ the_person.draw_person(position = "sitting")
    "You set her energy drink down next to her keyboard. She is just getting logged in."



    $ clear_scene()
    call advance_time from _call_advance_myra_focus_progression_scene_adv_02
    return

label myra_focus_progression_scene_1(the_group, scene_transition = False):  #groping
    $ the_person = the_group[0]
    #If we've done this before, we need to set it up manually, otherwise transition covers this.
    if myra.event_triggers_dict.get("focus_train_grope", False):
        pass
    $ clear_scene()
    call advance_time from _call_advance_myra_focus_progression_scene_adv_03
    return

label myra_focus_progression_scene_2(the_group, scene_transition = False):  #sit on lap and fingering
    $ the_person = the_group[0]

    if myra.event_triggers_dict.get("focus_train_finger", False):
        pass
    $ clear_scene()
    call advance_time from _call_advance_myra_focus_progression_scene_adv_04
    return

label myra_focus_progression_scene_3(the_group, scene_transition = False):  #assjob / lapdance
    $ the_person = the_group[0]
    if myra.event_triggers_dict.get("focus_train_assjob", False):
        pass
    $ clear_scene()
    call advance_time from _call_advance_myra_focus_progression_scene_adv_05
    return

label myra_focus_progression_scene_4(the_group, scene_transition = False):  #anal
    $ the_person = the_group[0]
    if myra.event_triggers_dict.get("focus_train_anal", False):
        pass
    $ clear_scene()
    call advance_time from _call_advance_myra_focus_progression_scene_adv_06
    return



label myra_focus_trans_scene_0(the_group):
    pass
    #This label should probably never be called.
    return

label myra_focus_trans_scene_1(the_group):  #Use event triggers to determine if this is from a transition or normal.

    $ the_person = the_group[0]
    "This is the transition to the second scene."
    the_person "I have another idea though... what if you fucked... my other hole?"
    mc.name "That's a good idea."
    return

label myra_focus_trans_scene_2(the_group):
    $ the_person = the_group[0]

    return

label myra_focus_trans_scene_3(the_group):
    $ the_person = the_group[0]

    return

label myra_focus_trans_scene_4(the_group):
    $ the_person = the_group[0]

    return



label myra_focus_progression_scene_study_choice(the_group):
    $ the_person = the_group[0]
    $ the_person.draw_person()
    "Do you want to stick around and help [the_person.title] traing her focus?"
    menu:
        "Training" if mc.energy >= 60:
            pass
        "Training\n{color=#ff0000}{size=18}Not enough Energy{/size}{/color} (disabled)" if mc.energy < 60:
            pass
        "Not right now":
            return False
    mc.name "Sure, I have time to do that. How about you go get logged in and I'll grab you an energy drink?"
    the_person "Okay! That sounds perfect. I'll see you over there."
    $ clear_scene()
    call myra_focus_train_get_energy_drink(the_person) from _myra_energy_drink_focus_scene_01
    return True

label myra_focus_progression_scene_exit_scene(the_group):
    $ the_person = the_group[0]
    mc.name "Unfortunately, I don't have time to do that right now."
    the_person "Ah, that is too bad."
    if myra_focus_progress_scene.get_stage() >= 2:
        the_person "The sessions have been so... productive... I've been looking forward to them more and more!"
    the_person "But anyway, was there something else you needed?"
    $ clear_scene()
    return


#Progression scene specific labels

label myra_focus_train_get_energy_drink(the_person):
    if myra_has_exclusive_energy_drink():   #This should be false for now. Revisit this once we figure out how to assign a signature serum as her energy drink
        "You head to the fountain drinks and find the blue raspberry energy drink. You grab a large cup with some ice and top it off with the serum."
        "You look around... you could easily slip and additional serum into this drink... but that would also be two serums at once to [the_person.title]..."
    else:
        "You head to the refreshments and find an energy drink for [the_person.title]."
        "You look around... you could easily slip a serum into the drink before taking it back to her."
    call give_serum(the_person) from _call_give_myra_serum_focus_train_01
    if _return:
        "You slip the serum into her drink."
    else:
        "You decide not to add a serum to it."
    return

label myra_focus_training_encounter(the_person):
    $ encounter_num = renpy.random.randint(0,9) #In approximate degree of difficulty
    if encounter_num == 0:
        "[the_person.title] is pushing the middle. The other team seem distracted, presenting her team with a 2v4."
        "This should be an easy encounter for someone as skilled as [the_person.possessive_title]."
    elif encounter_num == 1:
        "[the_person.title] defends her home point with two teamates. The other team has sent 2 attackers, for a 2v3."
        "The two enemies are already injured, [the_person.possessive_title] should be able to handle this encounter, under normal circumstances anyway..."
    elif encounter_num == 2:
        "A 3v3 battle is occuring on the center point, which [the_person.title] quickly joins."
        "Her allies were struggling, but with [the_person.possessive_title] they should be able to turn the tide."
    elif encounter_num == 3:
        pass
    elif encounter_num == 4:
        "[the_person.title] finds herself in a team battle at the center point. This appears to be an even 3v3 battle."
        "This should be a moderatly challenging scenario for someone as skill as [the_person.possessive_title]."
    elif encounter_num == 5:
        pass
    elif encounter_num == 6:
        pass
    elif encounter_num == 7:
        pass
    elif encounter_num == 8:
        pass
    elif encounter_num == 9:
        pass




    return

init 4 python:
    #Encounter difficulty should be up to 100, depending on the scenario, with dif_modifier up to 100 also, for hardcore anal sex or impending orgasm.
    #Planned max stats of 8 focus and 6 foreplay should give about 80% success rate at full difficulty, and about 50% for easy encounters with zero stats.
    def myra_calc_encounter_outcome(the_person, difficulty, dif_modifier = 0):
        if the_person.arousal >= 100:   #Almost impossible to focus during impending orgasm.
            dif_modifier = 100
        encounter_dif = difficulty + dif_modifier
        skill_stat = (the_person.focus + the_person.sex_skills["Foreplay"]) * 10 #Max 140, min 20
        if encounter_dif < (skill_stat + 20):
            encounter_dif = skill_stat + 20
        if skill_stat > renpy.random.randint(0,encounter_dif):
            return True
        return False

    #Return odds for the purpose of creating a menu string
    def myra_calc_encounter_odds(the_person, the_difficulty, dif_modifier = 0):
        if the_person.arousal >= 100:   #Almost impossible to focus during impending orgasm.
            dif_modifier = 100
        encounter_dif = difficulty + dif_modifier
        skill_stat = (the_person.focus + the_person.sex_skills["Foreplay"]) * 10 #Max 140, min 20
        if encounter_dif < (skill_stat + 20):
            encounter_dif = skill_stat + 20
        chance = int((skill_stat / encounter_dif) * 100)
        return chance
