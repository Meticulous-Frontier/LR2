
init 2 python:
    def camilla_mod_initialization():
        camilla_wardrobe = wardrobe_from_xml("ashley_Wardrobe")
        camilla_base_outfit = Outfit("camilla's base accessories")
        the_eye_shadow = heavy_eye_shadow.get_copy()
        the_eye_shadow.colour = [.18, .54, .34, 0.95]
        the_rings = copper_ring_set.get_copy()   #Change this
        copper_ring_set.colour = [.1,.36,.19,1.0]
        camilla_base_outfit.add_accessory(the_eye_shadow)
        camilla_base_outfit.add_accessory(the_rings)

        # init camilla role
        camilla_role = Role(role_name ="camilla", actions =[], hidden = True)

        #global camilla_role
        global camilla
        camilla = make_person(name = "Camilla", last_name ="Rojas", age = 22, body_type = "thin_body", face_style = "Face_3",  tits="B", height = 0.92, hair_colour="brown", hair_style = ponytail, skin="tan" , \
            eyes = "brown", personality = introvert_personality, name_color = "#228b22", dial_color = "228b22" , starting_wardrobe = camilla_wardrobe, \
            stat_array = [1,4,4], skill_array = [1,1,3,5,1], sex_array = [4,2,2,2], start_sluttiness = 7, start_obedience = -18, start_happiness = 119, start_love = 0, \
            title = "camilla", possessive_title = "Your intern", mc_title = mc.name, relationship = "Married", kids = 0, force_random = True, base_outfit = camilla_base_outfit,
            forced_opinions = [["production work", 2, True], ["work uniforms", -1, False], ["flirting", 1, False], ["working", 1, False], ["the colour green", 2, False], ["pants", 1, False], ["the colour blue", -2, False], ["classical", 1, False]],
            forced_sexy_opinions = [["taking control", 2, False], ["getting head", 2, False], ["drinking cum", -2, False], ["giving blowjobs", -2, False], ["public sex", 2, False]])

        camilla.generate_home()
        camilla.set_schedule(stephanie.home, times = [0,1,4])
        camilla.set_schedule(downtown_bar, times = [2,3])
        camilla.home.add_person(camilla)

        camilla.event_triggers_dict["intro_complete"] = False    # True after first talk
        camilla.event_triggers_dict["excitement_overhear"] = False   #
        camilla.event_triggers_dict["attitude_discussed"] = False   #
        camilla.event_triggers_dict["porn_discovered"] = False       #
        camilla.event_triggers_dict["porn_discussed"] = False    #
        camilla.event_triggers_dict["concert_overheard"] = False    #True after overhearing
        camilla.event_triggers_dict["concert_date"] = 0   #0 = not started, 1 = date arranged, 2 = date complete
        camilla.event_triggers_dict["porn_convo_day"] = 9999
        camilla.event_triggers_dict["porn_convo_avail"] = False
        camilla.event_triggers_dict["story_path"] = None

        # add appoint
        #office.add_action(HR_director_appointment_action)

        # camilla_intro = Action("camilla_intro",camilla_intro_requirement,"camilla_intro_label") #Set the trigger day for the next monday. Monday is day%7 == 0
        # mc.business.add_mandatory_crisis(camilla_intro) #Add the event here so that it pops when the requirements are met.

        # set relationships
        # town_relationships.update_relationship(camilla, stephanie, "Sister")
        # town_relationships.update_relationship(nora, camilla, "Friend")
        # town_relationships.update_relationship(lily, camilla, "Rival")

        camilla.add_role(camilla_role)
        return

label camilla_get_a_drink_label(the_person):
    mc.name "Care to get a drink, [the_person.title]?"

    "You consider for a moment. If you offer to buy her a drink, you'll have a chance to slip a serum into it."
    $ ran_num = (mc.charisma + (the_person.effective_sluttiness() / 10)) * 10  #More willing to let you buy a drink for her as she gets sluttier
    #$ bartender_name = get_random_male_name()
    menu:
        "Offer to Buy\n{color=#ff0000}{size=18}Success Chance: [ran_num]%%{/size}{/color}":
            mc.name "Hey, let me buy you a drink."
            if renpy.random.randint(0,100) < ran_num:  #Success
                the_person "Hmm... Okay! That sounds great! I'll go find us a table!"
                "You head over to the bar and order yourself a beer, and a cocktail for [the_person.title]."
                the_person.SO_name "Here you go, one beer, and a cocktail for the beautiful [the_person.name]."
                "Sounds like the bartender knows [the_person.title] pretty well. She must be in here often!"
                "The place is busy, so its easy to slip some serum into her drink."
                call give_serum(the_person) from _call_give_serum_CSH000
            else:                                 #Fail

                the_person "That's okay! I prefer to go dutch anyway."
                "You head over to the bar and order yourself a beer, [the_person.title] orders herself a fruity sounding cocktail."
                the_person "Hey there, [the_person.SO_name]! I'll have a flora dora tonight. You know how I like it!"
                "It sounds like she knows the bartender. She must be in here pretty often!"
        "Grab Drinks Separately":
            the_person "That's okay! I prefer to go dutch anyway."
            "You head over to the bar and order yourself a beer, [the_person.title] orders herself a fruity sounding cocktail."
            the_person "Hey there, [the_person.SO_name]! I'll have a flora dora tonight. You know how I like it!"
            "It sounds like she knows the bartender. She must be in here pretty often!"
    $ the_person.draw_person(position = "sitting")
    "You sit down at a table with [the_person.title]."

    #***Event State 0 ####
    if the_person.event_triggers_dict.get("camilla_progress", 0) < 1:  #This is your first time grabbing a drink Together
        mc.name "So, you come here often?"
        the_person "Oh! Yeah, I'm here all the time. I'm on a first name basis with the bartender at this point, haha!"
        mc.name "That great! This place is pretty nice. I can see why you come here. You said earlier you don't find guys like me very often. It's hard to believe a beautiful girl like you is single!"
        "You see her cheeks blush a little bit."
        the_person "Yeah, well, I'm not exactly single. I'm more in, what you might call an open relationship..."
        "Her responses catches you a little bit by surprise."
        the_person "It's pretty crazy. To be honest I never thought I would do something like this, but recently my husband has started asking me to go out and meet other guys and then tell him how it goes..."
        "Ahhh, her husband is some kind of cuckold?"
        mc.name "Ah, I see. That's interesting! Managed to snag any guys yet?"
        the_person "Well... to be honest... no. I haven't. I've gone out by myself a few times now... but I'm still too nervous. Something about you though, it puts me at ease to be around you..."
        "You chat with [the_person.title] for a bit longer, but soon it is time to leave."
        $ the_person.event_triggers_dict["camilla_progress"] = 1
        mc.name "Take care, I'm sure I'll see you here again sometime!"

    #***Event State 1 ####
    elif the_person.event_triggers_dict.get("camilla_progress", 0) == 1:  #You are acquainted, but not yet done anything sexual
        mc.name "So, any luck going squirrel hunting?"
        if the_person.effective_sluttiness() > 25:
            "[the_person.possessive_title] laughs."
            the_person "No, not yet. I have a feeling though, the right opportunity may come a long soon..."
            "She lowers her voice a bit."
            the_person "To catch a squirrel, and take his nut... so to speak..."
            "Damn! Maybe she is finally ready to start the camilla lifestyle."
            the_person "You wouldn't happen to know any squirrels would you?"
            mc.name "Oh, I think I know one... I bet he'd be more than happy to share his nuts with you..."
            "This analogy is starting to get a little weird though."
            mc.name "I bet your husband would be excited if you did manage to catch one."
            "[the_person.title] stutters for a second, but quickly smiles and regains her composure."
            the_person "Yeah, he keeps saying he will. I think its probably about time I put his eagerness to the test."
            if the_person.event_triggers_dict.get("camilla_blowjob_enable", 0) == 1:
                the_person "Just let me know when you have the time... I think we would both really enjoy our time."
                "[the_person.title] licks her lips, then gets up."
                $ the_person.draw_person (position = "stand4")
                the_person "See ya later, [the_person.mc_title]."
            elif mc.charisma > 3:
                the_person "Tell you what... I have to get going for now... but next time you see me here..."
                "She gives you a wink."
                the_person "I'm good friends with the bartender... I'm sure if I asked he'd give us some private time back in the bathroom..."
                mc.name "Damn. Sounds good. I'll be sure to look for your soon."
                "[the_person.title] licks her lips, then gets up."
                $ the_person.draw_person (position = "stand4")
                the_person "See ya later, [the_person.mc_title]."
                $ the_person.event_triggers_dict["camilla_blowjob_enable"] = 1
                "Sounds like you might get lucky next time you meet up with [the_person.title]."
            else:
                "Failed Charisma Check."
                "She looks at you for a second, then hesitates."
                the_person "Soon... anyway..."
                $ the_person.draw_person (position = "stand4")
                "[the_person.title] stands up abruptly."
                the_person "Sorry, I gotta get going. See ya later, [the_person.mc_title]!"
                "You wave goodbye as she walks off. You should work on your Charisma more and talk to her again sometime..."
        else:
            "[the_person.possessive_title] sighs."
            the_person "No, not yet. I'm just having a hard time getting myself to open up to that kind of thing."
            mc.name "Well, it is definitely not something you want to rush into."
            the_person "Yeah... he keeps telling me... he wants me to seduce a guy, and get pictures, to send him you know?"
            "Yep! He definitely sounds like a cuckold."
            the_person "But I don't know, I think maybe I just need a little more time."
            "Sounds like she might benefit from a few more doses of your serum, too..."


    #***Event State 2 ####
    elif the_person.event_triggers_dict.get("camilla_progress", 0) == 2:  #She has blown you
        mc.name "How are things going? Still going well with the husband?"
        the_person "Oh yes... I haven't had the guts to do anything with any other guys yet, but, those blowjob pictures definitely changed our sex life."
        mc.name "Good, glad to hear its working out for you."
        the_person "Yeah... he umm... he's started asking me if, you know, I'm almost ready to take things to the next level..."
        mc.name "Oh yeah? Meaning what?"
        the_person "Well, you know, not just blowing a guy but, letting him fuck me..." #TODO Finish this
        "You just about choke on your drink."
        mc.name "Hey, I'd be glad to help out. But obviously, don't rush into it if you aren't ready yet."
        "[the_person.title] takes a long sip from her cocktail."
        if mc.charisma < 5 or the_person.effective_sluttiness() < 40:
            if mc.charisma < 5:
                "Charisma check failed! Raise your charisma and try this conversation again."
            if the_person.effective_sluttiness() < 40:
                "Sluttiness check failed! Raise her sluttiness and try this conversation again."
            the_person "I'm sorry, [the_person.mc_title], I just don't think I'm ready to try that yet."
            "You nod in understanding."
            the_person "But umm.... I'd be glad to, you know, get you off in the usual way..."
            mc.name "Sounds good. I'll try to look for you next time I'm around."
        else:
            "She slowly puts her drink down."
            the_person "You know what? How about next time you see me here, how about we dance for a while?"
            mc.name "Oh?"
            the_person "Yeah, I mean, I love dancing... and a little bit of dirty dancing is a great way to get things started..."
            $ the_person.event_triggers_dict["camilla_dancing_enable"] = 1
            mc.name "Indeed, that sounds like fun! I'll try to look for you next time I'm around."

    elif the_person.event_triggers_dict.get("camilla_progress", 0) == 3:  #She's fucked you
        mc.name "So, how are things going at home?"
        the_person "Oh well... the hubby, he loves the photos he's been getting lately... and more importantly, I love what he does to me after he gets them."
        mc.name "Hah, that's good! I'm glad, it sounds like it has really spiced things up for you two."
        "[the_person.possessive_title] takes a long sip of her drink."
        the_person "So umm... he's started asking, when am I gonna bring you back to our place..."
        mc.name "Oh? He wants pictures of us in his own house huh?"
        the_person "Well, not exactly."
        mc.name "What do you mean?"
        the_person "Well, he wants to be there. He wants to watch."
        "Wow, her husband is really getting into the cuckolding thing!"
        mc.name "And how do you feel about it? Do you feel like you're ready for that?"
        if mc.charisma < 6 or the_person.effective_sluttiness() < 50:  #Checks Fail
            the_person "Honestly? I'm still adapting to how things are now."
            mc.name "That's understandable. There's no reason to take things too fast."
            "[the_person.title] takes another long sip from her beverage."
            the_person "For now... let's just keep things how they are. But hey, you never know, maybe we can take that step soon!"
            "You and [the_person.title] finish your drinks and then you say goodbye."
        else:
            the_person "Honestly? I'm getting a little turned on just thinking about it."
            mc.name "I'll admit, I'm' a little hesitant to do something like that in front of your husband... but if you're sure about it."
            the_person "Yeah... I'm certain! Let me know when would be a good time to come over, and I'll get the details sorted."
            "Wow, she wants you to come to her house and fuck her in front of her husband! You should probably get on that before the opportunity passes!"
            "You and [the_person.title] finish your drinks and then you say goodbye."

    elif the_person.event_triggers_dict.get("camilla_progress", 0) == 4:  #She's invited you over
        "You chat with [the_person.title] for a while, but you can definitely feel some tension in the air about your arrangement for tonight."
        mc.name "So... tonight at your place? I'll see you there?"
        the_person "Sounds good. See you then, [the_person.mc_title]."
    elif the_person.event_triggers_dict.get("camilla_progress", 0) == 5:  #You've fucked in front of her husband
        the_person "Thanks for the drink, [the_person.mc_title]. This whole adventure has really supercharged my sex life, its nice to have a break from fucking and just enjoy a stiff drink."
        mc.name "Yeah, so is [the_person.SO_name] still enjoying your new lifestyle?"
        the_person "Oh god, we both are. I've started fucking around with a couple other guys too. Last time I came home, he tied me up and umm... reclaimed me in every hole he could fit it in..."
        mc.name "Damn! That sounds hot!"
        the_person "Yeah! I came so many times... you didn't forget my address did you? You should stop by sometime and we could fuck around again."
        mc.name "Don't worry, I haven't forgotten."
        "You and [the_person.title] finish your drinks and then you say goodbye."
    else:
        "DEBUG: How did you get here?"

    call advance_time from _call_advance_camilla_drink
    return

#CSH10
label camilla_bathroom_blowjob_label(the_person):
    if the_person.event_triggers_dict.get("camilla_progress", 0) == 1: #This is our first time doing this
        mc.name "Hey, so uhh... wanna sneak into the bathroom for a bit?"
        "You see a bright red flush in her cheeks, but she quickly nods."
        the_person "I would like that...a lot!"
        "She takes a quick look around."
        the_person "Let me just go talk to the bartender... head to the lady's room and wait outside... I'll be over in a second."
        $ the_person.draw_person(position = "walking_away")
        "[the_person.possessive_title] walk away to talk to the bartender. You make your way over to the lady's room."
        $ the_person.draw_person(position = "stand4")
        "Soon, [the_person.title] comes over, holding a sign that says 'Bathroom closed for renovations: Please use men's room"
        $ mc.change_location(work_bathroom)
        $ mc.location.show_background()
        "You both take a quick look around, and when the coast is clear, you both walk into the bathroom and lock the door behind you."
        "You waste no time, you quickly wrap your arms around [the_person.title] and start making out with her."
        $ the_person.draw_person(position = "kissing")
        $ mc.change_arousal(10)
        the_person "Mm... mmm.... mmmmmmmmmff..."
        "She is moaning in your mouth. You can tell the naughtiness of getting intimate with someone other than her husband is really turning her on."
        $ the_person.change_arousal(10)
        the_person "Ok... wow this is hot. This is my first time ever doing something like this... so... I want you to just let me do my thing, ok?"
        "You quickly agree."
        the_person "Also, could you take my phone? And like, you know, take some pictures for me? Daddy asked me to..."
        "She is very awkwardly asking. You quickly answer like this is a completely normal request to put her at ease."
        mc.name "Of course! How else is daddy gonna know what his slutty girl has been up to?"
        "She smiles."
        the_person "Exactly!"
        "She hands you her phone with the camera app up."
        $ the_person.draw_person(position = "stand3")
        if not the_person.outfit.tits_available():    #If covered up, have her take her top off
            the_person "Here I go... don't forget to take pictures!"
            $ the_clothing = the_person.outfit.get_upper_top_layer()
            "[the_person.possessive_title] takes off her [the_clothing.name]."
            $ the_person.draw_animated_removal(the_clothing)
            $ the_clothing = None
        else:
            "[the_person.possessive_title] strikes a pose, her tits on display."
            the_person "Don't forget to take pictures!"
        "With her phone in hand, you snap a few pictures as she slowly walks over to you."
        "She runs her hands across your chest. She slowly gets down on her knees in front of you."
        $ the_person.change_arousal(20)
        $ the_person.draw_person(position = "blowjob")
        "[the_person.possessive_title] tugs at your belt, then slowly lowers your pants."
        "One more tug on your underwear, and your erection springs free."
        the_person "Wow! I haven't seen anything other than hubby for... years..."
        "She begins to stroke you softly with her hand."
        the_person "Mmmmm.... its so hard... and hot!"
        "You moan as she strokes you. You make sure to snap a couple pictures."
        $ mc.change_arousal(10)
        $ the_person.change_arousal(10)
        the_person "Does that feel good? I bet it does... I just wanna make you feel good..."
        "She closes her eyes, then opens her mouth. She slowly rubs the tip back and forth along her slithery tongue."
        the_person "Mmm, you taste good too."
        "She starts to take you into her mouth. You snap a few more pictures of this beautiful camilla, on her knees servicing you."
        "[the_person.possessive_title]'s head is now bouncing up and down on your cock. Her pouty lips feel amazing sliding up and down your length."
        $ the_person.change_arousal(20)
        $ mc.change_arousal(20)
        "You forget you are supposed to take pictures and begin to just enjoy the wonderful sensations."
        # call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = True, position_locked = True) from _call_sex_description_CSH010
        call get_fucked(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, allow_continue = False) from _call_sex_description_CSH010
        $ the_report = _return
        if the_report.get("girl orgasms", 0) > 0:
            "Wow... I can't believe I came... while I was blowing you! That was fucking hot!"
        else:
            "Wow... that was hot!"

        if the_person.has_mouth_cum():
            "[the_person.possessive_title] looks up at you. She couldn't quite swallow all your cum, some of it is slowly dripping down the sides of her mouth."
            the_person "Hey! Don't forget to take pictures!"
            "You suddenly remember the phone. You snap a couple pictures of her face with your traces of cum on it."
        elif the_person.has_face_cum():
            "[the_person.possessive_title] looks up at you. Her face is plastered with your sticky seed."
            the_person "Hey! Don't forget to take pictures!"
            "You suddenly remember the phone. You snap a couple pictures of her face with your cum covering it."
        $ the_person.draw_person (position = "stand2")
        "[the_person.title] stands up. You hand her back her phone."
        the_person "Wow... well... I guess there's no going back now? I guess I'll go ahead and send him some of these..."
        "She gets closer to you."
        the_person "Well, no matter what happens tonight, thanks for your help! If all goes well... maybe we can do this again."
        mc.name "Yeah I mean... if it makes your hubby happy for you to give me blowjobs... I GUESS I can help out..."
        "She laughs and punches you in the arm."
        the_person "Alright, I'm going to clean up. I'll see you."
        $ clear_scene()
        $ mc.change_location(downtown_bar)
        $ mc.location.show_background()
        "You sneak your way out of the bathroom while [the_person.possessive_title] cleans herself up. You hope everything goes well with her tonight!"
        $ the_person.event_triggers_dict["camilla_blowjob_text_enable"] = 1
        $ the_person.event_triggers_dict["camilla_progress"] = 2
        $ the_person.event_triggers_dict["camilla_blowjob_ask_pictures"] = day + 1
        $ the_person.apply_planned_outfit()
    else:   #This is not our first time getting blown#
        mc.name "Hey, you wanna sneak off for a bit?"
        "[the_person.possessive_title] flashes you her beautiful smile."
        the_person "You bet! You know what to do!"
        $ mc.change_location(work_bathroom)
        $ mc.location.show_background()
        "You head to the lady's room. [the_person.title] soon follows behind you. She locks the door as she closes it."
        $ the_person.draw_person (position = "kissing")
        "You waste no time. She throws her arms around you and you begin to make out."
        if the_person.effective_sluttiness() > 30 and not the_person.outfit.tits_available():
            "[the_person.possessive_title] steps back suddenly."
            the_person "Let me just get this off... daddy loves it when I have my tits out for this..."
            "She hands you her phone with the camera app out. You snap some pictures as she starts to strip."
            while not the_person.outfit.tits_available():
                $ the_clothing = the_person.outfit.get_upper_top_layer()
                "[the_person.possessive_title] takes off her [the_clothing.name]."
                $ the_person.draw_animated_removal(the_clothing)
                $ the_clothing = None
            "With her tits completely exposed, she saunters back over to you then starts to get down on her knees."
        else:
            "[the_person.possessive_title] slowly starts to get down on her knees in front of you."
        $ the_person.draw_person(position = "blowjob")
        "You can tell that [the_person.title] is hungry. She wastes no time pulling your pants off, followed quickly by your underwear."
        "Your hardened cock springs out. Her agile hands grasp it and begin to stroke."
        if the_person.effective_sluttiness() > 50:
            the_person "Mmm, I've been working on a new skill lately... since we started doing this. Mind if I practice on you?"
            mc.name "Sure I guess, but what is..."
            "She doesn't wait for you to finish your response. In one, smooth motion, she opens her mouth and swallows your cock whole."
            $ the_person.break_taboo("sucking_cock")
            "Past her lips, to the back of her tongue, and down her throat the tip of your dick goes."
            mc.name "Oh fuck!"
            "You make sure to snap more pictures of her. She's getting good at this!"
            "You decide to just enjoy her skilled mouth going down on you."
            # call fuck_person(the_person, start_position = deepthroat, start_object = make_floor(), skip_intro = True, girl_in_charge = True, position_locked = True) from _call_sex_description_CSH011
            call get_fucked(the_person, start_position = deepthroat, start_object = make_floor(), skip_intro = True, allow_continue = False) from _call_sex_description_CSH011
        else:
            the_person "Mmmm, I can't wait any longer... I have to taste it!"
            $ the_person.break_taboo("sucking_cock")
            "She opens up her mouth and wraps her lips around your meat."
            "You snap some pictures as she pulls of and begin to run her tongue up and down along the sides of your cock."
            mc.name "Mmm, that feels great [the_person.title]."
            "You decide to just enjoy her skilled mouth going down on you."
            # call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = True, position_locked = True) from _call_sex_description_CSH012
            call get_fucked(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, allow_continue = False) from _call_sex_description_CSH012

        if the_person.has_mouth_cum():
            "[the_person.possessive_title] looks up at you. She couldn't quite swallow all your cum, some of it is slowly dripping down the sides of her mouth."
            the_person "Hey! Don't forget to take pictures!"
            "You suddenly remember the phone. You snap a couple pictures of her face with your traces of cum on it."
        elif the_person.has_face_cum():
            "[the_person.possessive_title] looks up at you. Her face is plastered with your sticky seed."
            the_person "Hey! Don't forget to take pictures!"
            "You suddenly remember the phone. You snap a couple pictures of her face with your cum covering it."
        $ the_person.draw_person (position = "stand2")
        the_person "Mmm, that was great [the_person.mc_title]! I can't wait until I get home tonight... I hope daddy gets the handcuffs out again..."
        $ clear_scene()
        $ mc.change_location(downtown_bar)
        $ mc.location.show_background()
        "You say goodbye and excuse yourself while she gets herself cleaned up. This arrangement is working out to be very beneficial!"
        $ the_person.apply_planned_outfit()
        call advance_time from _call_advance_camilla_bathroom_blowjob
    return

label camilla_blowjob_text_label(the_person):
    mc.name "So... how did it go with the pictures?"
    "[the_person.possessive_title] gives you a quick smile."
    the_person "Well, I sent them off to him before I left the bar the other night, and I got an almost immediate response. 'Come home now'. No explanation or anything..."
    the_person "At first I got really scared. Did I just completely fuck up? So I went straight home..."
    the_person "When I got home, he was waiting for me... He umm... he handcuffed me with my hands behind my back... I didn't even know he had handcuffs!"
    "Her voice is starting to get excited as she recounts some of the details."
    the_person "He forced me down on my knees and then said... he said that I was a dirty little slut, and that after using my mouth on another man he would have to... reclaim it."
    the_person "So I opened up and I let him use my mouth... god I never could have imagined my husband doing that to me could be so hot."
    the_person "Now... I'm a good wife... I've always, you know, swallowed for him. But this time..."
    "Her voice trails off a bit as she recalls the details. A smile on her face."
    the_person "I've never, ever had to swallow soooooo much. It was so hot, like a firehose it just kept cumming..."
    "You shift uncomfortably. This story is starting to turn you on!"
    $ mc.change_arousal (20)
    the_person "Haaa... sorry! I probably should have just said that it went well."
    mc.name "No it is quite alright. I was a little concerned with how things would go for you, but I'm glad that it turned out well!"
    $ the_person.draw_person(position = "stand4", emotion = "happy")
    the_person "It really did! So uhh, if you wanna go again, just ask. I'd be happy to be of service, BUT, we need to set some ground rules first!"
    mc.name "Okay, I'm down for that."
    the_person "Okay, well, like I said. I'm a good wife! I love my husband. If things between us ever start to get... you know... serious? I'm going to have to break it off."
    "You nod in understanding."
    the_person "If you try to make me choose between you two, I'll choose him, every time. So lets just keep this casual, okay?"
    mc.name "Sounds good. Purely physical. I'm completely okay with that."
    the_person "Right... here, let's exchange numbers. I'll text you and if we're both free, we can screw around, no strings attached!"
    "You agree. You and [the_person.title] exchange numbers."
    the_person "Okay, well, I need to get going. I'm sure I'll see you around soon..."
    "You say goodbye and head out. Hot damn! You are now friends with benefits with a hot wife. You bet the sex is going to be amazing..."
    $ the_person.event_triggers_dict["camilla_blowjob_text_enable"] = 0
    call advance_time from _call_advance_camilla_sex_discussion
    return

#CSH20
label camilla_dancing_sex_label(the_person):
    if the_person.event_triggers_dict.get("camilla_progress", 0) == 2:   #This is our first time doing this
        mc.name "Hey, [the_person.title]. You up for some dancing?"
        "[the_person.possessive_title] smiles."
        the_person "You know, I am. Let's go!"
        "You follow [the_person.title] out on to the dance floor. The bar is playing some pretty upbeat, fun music."
        "You waste no time and grab [the_person.possessive_title]. You sync your movements to the beat and begin to move your bodies to the beat."
        $ the_person.draw_person (position = "back_peek")
        "At some point, [the_person.title] turns away from you. You put your hand on her hips and bring her close to you."
        "You can feel her grinding her ass back against you as you keep moving to the beat. Her ass feels great moving back and forth against your rapidly rising erection."
        mc.name "Mmm, that feels good. I can't wait to get you alone..."
        $ the_person.change_arousal(20)
        $ mc.arousal += 10
        "She gives a sigh and melts back into you. You let your hands roam all along the sides of her body, once in a while moving across the sides of her breasts."
        "The song ends and a slower song begins to play."
        $ the_person.draw_person (position = "kissing")
        "[the_person.possessive_title] turns back to you and puts her arms around your shoulders. You hands start on her hips, but soon drift down to her ass."
        the_person "I love this song. Let's dance to this and then head to the back..."
        "You notice her glance over to the bar. You follow her eyes and notice the bartender, [the_person.SO_name] is watching you dance."
        "You look back at [the_person.title]. You squeeze her supple ass and grind up against her slightly."
        the_person "Mmm... fuck that feels good."
        "[the_person.title] begins moving her hips against yours. Your cock, constrained in your clothing, is nestled against her crotch, aching to be let free."
        $ the_person.change_arousal(20)
        $ mc.arousal += 10
        "The song ends, and [the_person.title] looks at you."
        the_person "Ok... you know what to do... I'll meet you in the Lady's room in just a minute..."
        $ clear_scene()
        $ mc.change_location(work_bathroom)
        $ mc.location.show_background()
        "You head to women's restroom and [the_person.title] soon meets you there."
        $ the_person.draw_person (position = "against_wall")
        "You grab her and pick her up. Her legs wrap around you."
        the_person "Oh god... I can't believe I'm doing this... but I need it so bad!"
        "You take her over to the counter and set her on the edge of it. You start to strip her clothes off."
        if the_person.outfit.vagina_available() and the_person.outfit.tits_available():
            "You stop for a second and admire [the_person.title], her body on display in front of you."
        else:
            "Piece by piece, you take [the_person.title]'s clothes off."

            $ the_person.strip_outfit(position = "against_wall")
            $ the_person.change_arousal(20)

            "Once finished, You stop for a second and admire [the_person.title], her body on display in front of you."
        the_person "Oh! Shit I almost forgot!"
        "[the_person.possessive_title] grabs her purse. She rummages through it for a moment then pulls out her phone."
        the_person "Can't forget this!"
        "She hands you her phone and you quickly pull up her camera app. While you are doing that [the_person.possessive_title] turns around and leans over the counter."
        $ the_person.draw_person (position = "standing_doggy")
        "You snap a couple pictures of her amazing ass while she is bent over."
        the_person "Okay, you better get your pants off, we don't have much time!"
        "You quickly drop your pants, letting your aching hard on spring free. You step behind [the_person.title], letting your cock nestle between her pliant ass cheeks."
        "You snap a few more pictures as you dry hump her ass crack a bit. Then you pull back a bit and get yourself pointed at her juicy slit."
        "You change the camera app to take a video. You figure since this is her first time getting fucked by a man other than her husband it might come in handy..."
        "With one hand firmly on [the_person.possessive_title]'s hip, you steadily push yourself into her. She moans loudly and you capture the whole thing on glorious video."
        $ the_person.break_taboo("vaginal_sex")
        $ the_person.break_taboo("condomless_sex")
        the_person "Oh fuck that feels good. Fuck me good [the_person.mc_title]!"
        "You stop the video, you figure this is as good of a place as any to stop it. You take a few nice and slow strokes, snapping pictures of your cock penetrating her at various depths."
        "You look up and get one last picture of [the_person.title] in the mirror. Her mouth is open and she has one hand groping one of her own tits while her other hand is reaching back and grabbing your hip."
        "You set the phone down and begin to fuck her."
        $ mc.condom = False
        call fuck_person(the_person, start_position = SB_doggy_standing, start_object = make_counter(), skip_intro = True, skip_condom = True) from _call_sex_description_CSH020
        $ the_report = _return
        if the_report.get("guy orgasms", 0) > 0:
            #TODO description for all possible cum locations
            if the_person.has_mouth_cum():
                "[the_person.possessive_title] looks up at you. She couldn't quite swallow all your cum, some of it is slowly dripping down the sides of her mouth."
                "You grab her phone and snap a couple pictures of her face with your traces of cum on it."
            elif the_person.has_face_cum():
                "[the_person.possessive_title] looks up at you. Her face is plastered with your sticky seed."
                "You grab her phone and snap a couple pictures of her face with your cum covering it."
            elif the_person.has_tits_cum():
                "[the_person.possessive_title] looks up at you. Her tits are plastered with your sticky seed."
                "You grab her phone and snap a couple pictures of her tits with your cum covering it."
            elif the_person.has_ass_cum():
                "[the_person.possessive_title] looks back at you. Her ass is plastered with your sticky seed."
                "You grab her phone and snap a couple pictures of her ass with your cum covering it."
            else:       #We assume we finished inside her#
                "[the_person.possessive_title]'s pussy is dripping cum from your creampie."
                "You grab her phone and snap a couple pictures of her well used pussy with your cum dripping out of it."
        if the_report.get("girl orgasms", 0) > 0:
            the_person "Oh my god... that was amazing. That felt so good."
        $ the_person.draw_person("stand3")
        the_person "Wow, I never knew cheating could feel so good. God, I can't wait until my husband reclaims me later... oh fuck."
        "[the_person.possessive_title] starts to touch herself a bit, getting herself excited thinking about what is in store for her later tonight. She quickly realizes she needs to stop though."
        $ the_person.event_triggers_dict["camilla_progress"] = 3
        "She takes her phone from you and starts going through the pictures you took."
        the_person "You'd better get going, [the_person.mc_title]. I'm going to send these to my husband..."

        $ the_person.event_triggers_dict["booty_call"] = True # unlock casual encounters
        $ mc.phone.register_number(the_person)

        "You now have [the_person.title]'s phone number. She may call you from time to time to hookup!"

        $ clear_scene()
        $ the_person.apply_planned_outfit()

    else:   #We've done this before
        mc.name "Hey, [the_person.title]. You up for some dancing?"
        "[the_person.possessive_title] smiles."
        the_person "You know it! Let's go!"
        "You follow [the_person.title] out on to the dance floor. The bar is playing some pretty upbeat, fun music."
        "You waste no time and grab [the_person.possessive_title]. You sync your movements to the beat and begin to move your bodies to the beat."
        $ the_person.draw_person (position = "back_peek")
        "At some point, [the_person.title] turns away from you. You put your hand on her hips and bring her close to you."
        "You can feel her grinding her ass back against you as you keep moving to the beat. Her ass feels great moving back and forth against your rapidly rising erection."
        mc.name "Mmm, that feels good. I can't wait to fuck you again."
        $ the_person.change_arousal(20)
        $ mc.arousal += 10
        "She gives a sigh and melts back into you. You let your hands roam all along the sides of her body, once in a while moving across the sides of her breasts."
        "The song ends and a slower song begins to play."
        $ the_person.draw_person (position = "kissing")
        "[the_person.possessive_title] turns back to you and puts her arms around your shoulders. You hands start on her hips, but soon drift down to her ass."
        the_person "I love this song. Let's dance to this! Then we can head to the back and you can have your way with me..."
        "You squeeze her supple ass and grind up against her slightly."
        the_person "Mmm... fuck that feels good. You better make sure I cum all over that amazing cock of yours."
        "[the_person.title] begins moving her hips against yours. Your cock, constrained in your clothing, is nestled against her crotch, aching to be let free."
        $ the_person.change_arousal(20)
        $ mc.arousal += 10
        "The song ends, and [the_person.title] looks at you."
        the_person "Ok! I didn't think that song was ever going to end. I'll meet you in the Lady's room in just a minute."
        $ clear_scene()
        $ mc.change_location(work_bathroom)
        $ mc.location.show_background()
        "You head to women's restroom and [the_person.title] soon meets you there."
        $ the_person.draw_person (position = "stand4")
        the_person "Okay, I want you to sit on the counter. I'm gonna get naked for you."
        "She hands you her phone."
        the_person "Here we go! Get lots of good pics!"
        call free_strip_scene(the_person) from _CS_free_strip_scene_CSH021
        "You got lots of pics of her strip tease. You take a few more as she saunters over to you."
        the_person "Come on, lets fuck!"
        call fuck_person(the_person) from _call_casual_sex_mod_CSH022
        "As you finish up, you make sure to take some pictures of the aftermath. You notice [the_person.possessive_title] is touching herself."
        the_person "Oh god, daddy is fuck me so rough tonight when he reclaims me tonight... I'm gonna be so sore. I can't wait!"
        "You almost think she is going to make herself cum again until she stops."
        $ the_person.draw_person("stand3")
        the_person "Thanks again [the_person.mc_title]. You know where to look for me next time you need some... action."
        "She takes her phone from you and starts going through the pictures you took."
        the_person "You'd better get going. I'm going to send these to my husband..."
        $ the_person.apply_planned_outfit()
        $ clear_scene()

    $ mc.change_location(downtown_bar)
    $ mc.location.show_background()
    "You grab your clothes and quickly get yourself presentable, before sneaking your way out of the lady's room."
    call advance_time from _call_advance_camilla_dancing
    return

#CSH30
label camilla_sex_invite_label(the_person):
    mc.name "Hey so... I'm not doing anything later..."
    "You can see a smile start to form on [the_person.title]'s face."
    the_person "You want to come over tonight?"
    mc.name "That would be great."
    "[the_person.possessive_title] gives you her address."
    the_person "Come over tonight, around 10pm. You won't regret it! Is there anything else you want to do now?"
    $ add_camilla_sex_at_her_place_action(the_person)
    $ the_person.learn_home()
    $ the_person.event_triggers_dict["camilla_progress"] = 4

    #call advance_time from _call_advance_camilla_sex_invite
    return

#CSH40
label camilla_her_place_label(the_person):
    "You head over to [the_person.title]'s place. You can't believe you're gonna fuck her in front of her husband!"
    "You ring the doorbell. Soon [the_person.title] answers the door."

    $ the_person.change_to_hallway()
    $ the_person.apply_outfit(get_camilla_lingerie_set_white(), update_taboo = True)
    $ the_person.draw_person(position = "stand4")
    the_person "You made it! I wasn't sure you would actually come!"
    mc.name "Of course!"
    $ mc.change_location(the_person.home)
    $ mc.location.show_background()
    "You check her out. She definitely looks ready for some action! She takes your hand and slowly walks you back to the bedroom."
    the_person "[the_person.SO_name] and I were just getting started... you came at the perfect time..."
    "[the_person.SO_name]? Why does that sound so familiar?"
    $ the_person.change_to_bedroom()
    "As you walk into the bedroom, you see [the_person.SO_name], the bartender sitting in a chair, completely naked."
    "Holy shit! Its the bartender! He had a front row ticket every time you fucked [the_person.title] at the bar! No wonder he went along with all of it!"
    "He nods to you, but you are shocked at the revelation."
    the_person "Don't worry about him, get over here and fuck me [the_person.mc_title]!"
    $ the_person.draw_person(position = "doggy")
    "You watch as [the_person.possessive_title] crawls on to the bed, pointing her ass back at you. She wiggles it back and forth, enticingly."
    "You walk up behind her and run your hands over her pliant cheeks. [the_person.SO_name]'s chair is at the end of the bed, so he will have an excellent profile view while you fuck his wife."
    "With one hand you start to undo your trousers. With your other hand, you run you fingers along her slit. She is wet and ready for you."
    "Your cock now free, you line yourself up with [the_person.possessive_title]'s pussy. You put her husband out of your mind as you slowly push into her."
    "[the_person.possessive_title] gasps as you begin to slide in and out of her."
    call fuck_person(the_person, start_position = doggy, start_object = make_bed(), skip_intro = True, skip_condom = True) from _call_sex_description_CSH040
    $ the_report = _return

    #Finishing dialogue based on sexual performance
    if the_report.get("girl orgasms", 0) > 1:   #She had more than one orgasm
        the_person "Oh my god... I came so many times..."
        "[the_person.possessive_title] collapses onto the bed after your performance. You get up and start to get dressed."
        "You nod at [the_person.SO_name], and he nods back. He goes over to a bedside table and gets out a set of handcuffs."
        "After you fucked her brains out, [the_person.title] lays helpless on the bed as he starts to cuff her hands behind her back."
        "You finished getting dressed and decide to leave them to it, so you quietly excuse yourself from the bedroom."
    elif the_report.get("girl orgasms", 0) > 0: #She had one orgasm
        the_person "Oh god, I came so hard... That was good [the_person.mc_title]."
        $ the_person.draw_person (position = "missionary")
        "[the_person.possessive_title] rolls over on her back and spreads her legs wide."
        the_person "[the_person.SO_name]... I've been a bad girl..."
        "[the_person.SO_name] gets up from his chair and gets some handcuffs from a bedside table. You get yourself dressed."
        "[the_person.SO_name] begins cuffing [the_person.title]'s hands to the bedpost. You finish getting dress and quietly excuse yourself from the bedroom."
    else:                           #You left her hanging
        "Surprised you are finished so soon, [the_person.title] gets up and sits at the edge of the bed."
        $ the_person.draw_person( position = "sitting")
        the_person "Thanks for getting me warmed up..."
        "[the_person.SO_name] gets up from his chair and gets some handcuffs from a bedside table. You get yourself dressed."
        the_person "Oh... [the_person.SO_name], I've been a bad girl... what are you gonna do with those handcuffs?"
        "[the_person.SO_name] begins cuffing [the_person.title]'s behind her back. You finish getting dress and quietly excuse yourself from the bedroom."
    "You make your way back home. You can hardly believe your luck, fucking [the_person.title] in her house, in front of her husband, who is also the bartender!"
    $ perk_system.add_stat_perk(Stat_Perk(description = "Fucking a camilla in front of her husband has made you feel more charismatic.", cha_bonus = 1, bonus_is_temp = False), "camilla Charisma Bonus")
    $ mc.change_location(bedroom)
    $ mc.location.show_background()
    $ the_person.event_triggers_dict["camilla_progress"] = 5
    return

#CSH50
label camilla_home_sex_label(the_person):
    $ mc.change_location(the_person.home)
    $ mc.location.show_background()
    mc.name "So, want to have some fun tonight?"
    the_person "Sounds great! Just give me a minute to get ready..."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] walks into her bedroom and closes the door. You hang out in her living room for a few minutes while she gets ready."
    $ the_person.apply_outfit(get_camilla_lingerie_set_pink(), update_taboo = True)
    $ the_person.draw_person(position = "stand4")
    "She opens up the bedroom door and motions for you to follow her. As you step into her bedroom you see [the_person.SO_name] sitting at the edge of the bed again."
    $ the_person.change_to_bedroom()
    "You nod at him, and he gives a brief nod back. You turn your attention back to [the_person.title]."
    the_person "Mmm, I can't wait. Let's go!"
    call fuck_person(the_person) from _call_casual_sex_mod_CSH050
    $ the_report = _return
    if the_report.get("girl orgasms", 0) > 1:
        the_person "Oh my god... I came so many times..."
        "[the_person.possessive_title] collapses onto the bed after your performance. You get up and start to get dressed."
        "You nod at [the_person.SO_name], and he nods back. He goes over to a bedside table and gets out a set of handcuffs."
        "After you fucked her brains out, [the_person.title] lays helpless on the bed as he starts to cuff her hands behind her back."
        "You finished getting dressed and decide to leave them to it, so you quietly excuse yourself from the bedroom."
    elif the_report.get("girl orgasms", 0) > 0:
        the_person "Oh god, I came so hard... That was good [the_person.mc_title]."
        $ the_person.draw_person (position = "missionary")
        "[the_person.possessive_title] rolls over on her back and spreads her legs wide."
        the_person "[the_person.SO_name]... I've been a bad girl..."
        "[the_person.SO_name] gets up from his chair and gets some handcuffs from a bedside table. You get yourself dressed."
        "[the_person.SO_name] begins cuffing [the_person.title]'s hands to the bedpost. You finish getting dress and quietly excuse yourself from the bedroom."
    else:                           #You left her hanging
        "Surprised you are finished so soon, [the_person.title] gets up and sits at the edge of the bed."
        $ the_person.draw_person( position = "sitting")
        the_person "Thanks for getting me warmed up..."
        "[the_person.SO_name] gets up from his chair and gets some handcuffs from a bedside table. You get yourself dressed."
        the_person "Oh... [the_person.SO_name], I've been a bad girl... what are you gonna do with those handcuffs?"
        "[the_person.SO_name] begins cuffing [the_person.title]'s behind her back. You finish getting dress and quietly excuse yourself from the bedroom."

    $ mc.change_location(bedroom)
    $ mc.location.show_background()
    "You make your way back home after a sexy evening with [the_person.possessive_title]."

    call advance_time from _call_advance_camilla_home_sex
    return

label camilla_ghost_label(the_person):
    "You get a message on your phone. Looks like it is from [the_person.possessive_title]."
    the_person "Hey, I'm really sorry to have to do this, but we can't hookup anymore."
    the_person "I'm dedicated to my husband, but I find myself thinking about you constantly."
    the_person "This is beginning to turn into an emotional affair, and I can't do it anymore. I'm sorry."
    "Damn. Sounds like you pushed things with her a little too far..."
    $ the_person.remove_person_from_game()
    $ casual_sex_create_camilla() #Create a new camilla so MC can try again if they choose.
    return
