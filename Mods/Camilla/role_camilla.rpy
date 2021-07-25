
init 2 python:

    camilla_spot_at_bar = Action("Camilla at the bar", camilla_spot_at_bar_requirement, "camilla_spot_at_bar_label")
    camilla_get_a_drink = Action("Get a drink", camilla_get_a_drink_requirement, "camilla_get_a_drink_label")
    camilla_go_dancing = Action("Salsa Dancing", camilla_go_dancing_requirement, "camilla_go_dancing_label")
    camilla_take_pics = Action("Take Sexy Pics", camilla_take_pics_requirement, "camilla_take_pics_label")
    camilla_dance_lessons = Action("Dancing Lessons", camilla_dance_lessons_requirement, "camilla_dance_lessons_label")
    camilla_blowjob_text = Action("Blowjob Discussion", camilla_blowjob_text_requirement, "camilla_blowjob_text_label")

    def camilla_mod_initialization():
        camilla_wardrobe = wardrobe_from_xml("ashley_Wardrobe")
        camilla_base_outfit = Outfit("camilla's base accessories")
        the_makeup = blush.get_copy()
        the_makeup.colour = [.65, .23, .17, 0.75]
        the_lipstick = lipstick.get_copy()
        the_lipstick.colour = [.26, .21, .14, 0.33]
        the_rings = copper_ring_set.get_copy()   #Change this
        copper_ring_set.colour = [.95,.95,.78,1.0]
        camilla_base_outfit.add_accessory(the_makeup)
        camilla_base_outfit.add_accessory(the_lipstick)
        camilla_base_outfit.add_accessory(the_rings)

        # init camilla role
        camilla_role = Role(role_name ="camilla", actions =[camilla_get_a_drink, camilla_go_dancing, camilla_take_pics], hidden = True)

        #global camilla_role
        global camilla
        camilla = make_person(name = "Camilla", last_name ="Rojas", age = 34, body_type = "standard_body", face_style = "Face_2",  tits="D", height = 0.98, hair_colour="golden blonde", hair_style = braided_bun, skin="tan" , \
            eyes = "brown", personality = introvert_personality, name_color = "#228b22", dial_color = "228b22" , \
            #starting_wardrobe = camilla_wardrobe, \
            stat_array = [1,4,4], skill_array = [1,1,3,5,1], sex_array = [4,2,2,2], start_sluttiness = 7, start_obedience = -18, start_happiness = 119, start_love = 0, \
            relationship = "Married", kids = 0, force_random = True, base_outfit = camilla_base_outfit,
            forced_opinions = [["production work", 2, True], ["work uniforms", -1, False], ["flirting", 1, False], ["working", 1, False], ["the colour green", 2, False], ["pants", 1, False], ["the colour blue", -2, False], ["classical", 1, False]],
            forced_sexy_opinions = [["taking control", 2, False], ["getting head", 2, False], ["drinking cum", -2, False], ["giving blowjobs", -2, False], ["public sex", 2, False]])

        camilla.generate_home()
        camilla.set_schedule(camilla.home, times = [0,4])
        #camilla.set_schedule(downtown_bar, times = [2,3])  #Disabled for now
        camilla.set_schedule(downtown_bar, times = [3])
        camilla.set_schedule(mall, times = [1,2], days = [0, 1, 2, 3, 4])
        camilla.home.add_person(camilla)

        camilla.event_triggers_dict["intro_complete"] = False    # True after first talk
        camilla.event_triggers_dict["get_drinks"] = False
        camilla.event_triggers_dict["go_dancing"] = False
        camilla.event_triggers_dict["take_pics"] = False

        # add appoint
        #office.add_action(HR_director_appointment_action)

        # camilla_intro = Action("camilla_intro",camilla_intro_requirement,"camilla_intro_label") #Set the trigger day for the next monday. Monday is day%7 == 0
        # mc.business.add_mandatory_crisis(camilla_intro) #Add the event here so that it pops when the requirements are met.

        # set relationships
        # town_relationships.update_relationship(camilla, stephanie, "Sister")
        # town_relationships.update_relationship(nora, camilla, "Friend")
        # town_relationships.update_relationship(lily, camilla, "Rival")

        camilla.add_role(camilla_role)
        camilla.add_role(lifestyle_coach_role)
        camilla.add_unique_on_room_enter_event(lifestyle_coach_intro)
        return



init -1 python:
    def camilla_spot_at_bar_requirement(the_person):
        if the_person.location == downtown_bar:
            return True
        return False

    def camilla_get_a_drink_requirement(the_person):
        if the_person.location == downtown_bar and the_person.event_triggers_dict.get("get_drinks", False):
            if mc.business.change_funds > 20:
                return True
            else:
                return "Not enough money!"
        return False

    def camilla_dance_lessons_requirement():
        if day%7 == 2 and time_of_day == 3:
            return True
        return False

    def camilla_go_dancing_requirement(the_person):
        return "Disabled for now"
        if the_person.location == downtown_bar and camilla_can_go_dancing():
            return True
        return False

    def camilla_take_pics_requirement(the_person):
        if the_person.location == downtown_bar and camilla_will_take_pics() and the_person.effective_sluttiness > 40:
            return True
        return False

    def camilla_blowjob_text_requirement():
        if day >= camilla.event_triggers_dict.get("camilla_blowjob_pic_day", 9999):
            return True
        return False


label camilla_spot_at_bar_label(the_person):
    "As you walk into the bar, you take a look around."
    $ the_person.draw_person(position = "sitting")
    "Sitting at the bar by herself, you notice [the_person.title], the lifestyle coach from the mall."
    "You are surprised a woman as pretty as her is sitting by herself at the bar, so you decide to go say hi."
    "She notices you as you walk up to her."
    mc.name "Hello [the_person.title]. Out for a drink this evening?"
    the_person "Hello... [the_person.mc_title] was it?"
    mc.name "Excellent memory. Yes I worked with you some at the mall the other day."
    the_person "Yes, I remember. The small business owner."
    mc.name "I noticed you at the bar by yourself. Mind if I sit with you for a while?"
    the_person "That's fine."
    "You sit down in a bar stool next to [the_person.possessive_title]"
    mc.name "So how long have you been working as a lifestyle coach?"
    the_person "Honestly, not too long. I mainly just do it as an extra source of income to suppliment what my hubby brings in."
    "Ah, so she is married. You should probably keep things low key for now."
    mc.name "That's admirable. How long have you been married?"
    the_person "Almost 15 years now."
    mc.name "Wow, you don't look like someone who has been married 15 years!"
    the_person "Ah, we got married young."
    mc.name "Kids?"
    "[the_person.title] hesitates. You might have hit a sore subject with her..."
    the_person "No, no niños..."
    mc.name "I'm sorry... I'm probably getting a little personal."
    the_person "It's okay, that's a perfectly normal question to ask."
    "You feel bad. You notice that her glass is almost empty. You wave down the bartender. When he walks over, he smiles wide at [the_person.title]"
    "?????" "Something I can get for you?"
    mc.name "Can I get a beer and another for my friend?"
    "?????" "Sure. A beer and another paloma for the lovely miss [the_person.last_name]."
    "The bartender walks off. He seems to know [the_person.title]. She must be a regular here?"
    mc.name "Ah, you come here often then?"
    the_person "I do. I'm here most evenings. I like have a drink before I head home each night. My husband works late."
    mc.name "I see. I'm here somewhat often as well. Maybe we could have a drink together once in a whlie?"
    the_person "I... I suppose that would be alright."
    "You sit back in the chair and chat with [the_person.possessive_title] for a while. You both enjoy the time together, getting to know one another as friends."
    $ the_person.change_love(3)
    $ mc.business.change_funds(-20)
    "Eventually you settle up with the bartender. You notice him gesture at [the_person.title] when she isn't looking, and gives you a little wink."
    "You aren't sure... is he trying to say she's... available? Maybe since her husband works late she picks up guys at the bar..."
    "You file it away in your brain. Maybe you could come back and have drinks with her again. A bar would be an ideal place to dose her with a few serums too..."
    "You get up and say goodbye to [the_person.possessive_title]."
    mc.name "Thank you for the conversation. I'll see you around [the_person.title]"
    the_person "Take care [the_person.mc_title]."
    "You can now have drinks with [the_person.title] at the bar in the evenings."
    $ camilla.event_triggers_dict["get_drinks"] = True
    #TODO advance time
    return


label camilla_get_a_drink_label(the_person):
    mc.name "Care to get a drink, [the_person.title]?"
    "You consider for a moment. If you offer to buy her a drink, you'll have a chance to slip a serum into it."
    $ ran_num = (mc.charisma + (the_person.effective_sluttiness() / 10)) * 10  #More willing to let you buy a drink for her as she gets sluttier
    #$ bartender_name = get_random_male_name()
    if camilla_can_go_dancing():
        $ ran_num = 100
    menu:
        "Offer to Buy\n{color=#ff0000}{size=18}Success Chance: [ran_num]%%{/size}{/color}":
            mc.name "Hey, let me buy you a drink."
            if renpy.random.randint(0,100) < ran_num:  #Success
                the_person "Hmm... Okay! That sounds great! I'll go find us a table!"
                "You head over to the bar and order yourself a beer, and a cocktail for [the_person.title]."
                the_person.SO_name "Here you go, one beer, and a cocktail for the beautiful [the_person.name]."
                "Sounds like the bartender knows [the_person.title] pretty well. She must be in here often!"
                "The place is busy, so its easy to slip some serum into her drink."
                call give_serum(the_person) from _call_give_serum_camilla_01
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
    if not camilla_is_open():
        mc.name "Glad to see you here again. How have you been?"
        the_person "Pretty good. You?"
        mc.name "I'm doing well. Especially now that I have a chance to have a drink with a beautiful woman such as yourself."
        "She looks a little embarassed, but doesn't respond negatively to your comment."
        mc.name "So, your hubby is okay with you going out to the bar all by yourself?"
        the_person "Si, he doesn't mind. In fact, he kind of encourages it."
        mc.name "Really? That's interesting."
        "[the_person.possessive_title] takes a sip of her drink and takes a moment."
        the_person "Truth me told, hubby has been encouraging me recently to umm... get out and meet new people... men specifically."
        "Her statement catches you a little bit by surprise."
        the_person "To be honest... I'm not sure I'm going to... but hubby has this fantasy thing where I... get with other guys..."
        "Ah her husband is some kind of cuckold."
        mc.name "That's interesting. Manage to snag any yet?"
        the_person "No. I'm... I just want to be a good wife... and honestly I never thought my hubby would ask me to do something like this."
        the_person "I'm still too nervous, but I like to come to the bar and have a couple drinks. Maybe someday I'll actually go through with it."
        "[the_person.possessive_title] takes another long sip of her drink."
        the_person "I don't know why but, its nice being able to talk to you. Something about you puts me at ease."
        mc.name "Ah, I understand what you mean."
        "You chat with [the_person.title] for a bit longer, but soon it is time to leave."
        $ the_person.event_triggers_dict["is_open"] = True
        mc.name "Take care, I'm sure I'll see you here again sometime!"
    elif not camilla_can_go_dancing():
        mc.name "So, how's it going? Any luck with picking up guys?"
        if the_person.effective_sluttiness() > 15:
            "[the_person.possessive_title] ignores your question and looks at you."
            the_person "Do you like salsa dancing?"
            mc.name "Ah, I'll admit, I've never really tried it."
            "[the_person.title] takes a sip of her drink."
            the_person "Did you know they do salsa dancing here sometimes? Even if you are new at it, it would be fun to try it sometime."
            the_person "On Wednesday nights they have a salsa dancing for beginners class. You should come and I'll go with you."
            "That sounds suspiciously like a date. With this smoking hot seniorita in an open relationship, the implications are impossible to ignore."
            mc.name "Sure, I'll do it next Wednesday."
            the_person "Great!"
            "You chat with [the_person.title] for a bit longer, but soon it is time to leave."
            $ mc.business.add_mandatory_crisis(camilla_dance_lessons)
            mc.name "Take care, I'm sure I'll see you here again sometime!"
        else:
            "[the_person.possessive_title] sighs."
            the_person "No, not yet. I'm just having a hard time getting myself to open up to that kind of thing."
            mc.name "Well, it is definitely not something you want to rush into."
            the_person "Yeah... he keeps telling me... he wants me to seduce a guy, and get pictures, to send him you know?"
            "Yep! He definitely sounds like a cuckold."
            the_person "But I don't know, I think maybe I just need a little more time."
            "Sounds like she might benefit from a few more doses of your serum, too..."
            "You chat with [the_person.title] for a bit longer, but soon it is time to leave."
            mc.name "Take care, I'm sure I'll see you here again sometime!"

    elif not camilla_will_take_pics():
        if the_person.effective_sluttiness() > 40:
            mc.name "So, any progress with the husband?"
            the_person "Not yet... but I think I'm ready to. I'm just waiting for the right opportunity to come along."
            mc.name "Oh? What kind of opportunity are you waiting for?"
            the_person "I guess... I'm just waiting on the right guy to offer to umm... take some pics with me."
            "She lowers her voice to a whisper."
            the_person "You know I'm on a first name basis with the bartender? I'm pretty sure he would help cover for me with... whoever that guy happens to be."
            call camilla_bathroom_blowjob_label(the_person) from _camilla_first_blowjob_pics_01
        else:
            the_person "No dancing tonight?"
            mc.name "No, sometimes it is nice to just relax and have drink."
            the_person "Yeah, I agree."
            "You chat with [the_person.possessive_title] for a bit."
            "There is definitely some sexual tension in the air between you two, but she knows she can talk to you about it when she is ready."
            $ mc.change_locked_clarity(10)

    elif not camilla_can_go_to_her_place():
        if the_person.effective_sluttiness() > 60:
            pass
        else:
            pass
    # else:
    #     pass
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

label camilla_dance_lessons_label():
    $ the_person = camilla
    $ scene_manager = Scene()
    "It's Wednesday night, and you have a date with [the_person.possessive_title] at the bar to learn salsa dancing."
    $ mc.change_location(downtown_bar)
    $ mc.location.show_background()
    "When you get there, you step inside. You see [the_person.title] at the bar, in a very nice dress."
    $ scene_manager.add_actor(the_person)
    "You walk over to her. When she sees you she smiles."
    the_person "Ah, señor! I wasn't sure that you would actually come!"
    mc.name "Of course. Sometimes we need to be adventurous and get out of our comfort zone to try something new."
    "When you finish your statement, you give her a wink. She immediately realizes you are commenting about her situation with her husband..."
    $ the_person.change_slut_temp(3)
    the_person "You are right about that, but tonight, it is all about you!"
    "You make some idle chatter at the bar as you wait for the lessons to begin. You admit you are pretty nervous, but as people filter in, you see a lot of people around who also look new at this."
    "?????" "Alright, everyone here for salsa lessons, we are forming up over here! Come with your partner!"
    "You and [the_person.possessive_title] head over."
    "?????" "Alright, my name is Alvero, and I'll be your instructor tonight! First let's start off with a litte..."
    "You listen intently as the instructor begins initial warm up instructions."
    "Finally, its time to start dancing."
    $ scene_manager.update_actor(the_person, position = "kissing")
    "You get close to [the_person.title] as the music starts. You listen as the instructor begins to issue commands."
    "Alvero" "Alright fellas, remember, your sole purpose while salsa dancing is to display the beautiful flower you are partners with."
    $ scene_manager.update_actor(the_person, position = "kissing", display_transform = character_left_flipped)
    "You try one of the moves as instructed, moving [the_person.possessive_title] away from you a bit and allowing her make a graceful spin back to you."
    $ scene_manager.update_actor(the_person, position = "back_peek", display_transform = character_right)
    "She spins beautifully and stops with her back to you. She looks back and gives you a sly smile."
    if mc_dancing_skill() < 4:
        "Unfortunately you fumble a bit as she spins back out. You don't trip but you definitely feel awkward compared to the grace your partner is exhibiting."
        $ scene_manager.update_actor(the_person, position = "kissing")
        "[the_person.title] whispers in your ear."
        the_person "Don't worry, we were all new at one time. You are doing great."
        $ the_person.change_happiness(2)
        $ the_person.change_love(2)
    elif mc_dancing_skill() < 10:
        "You spin her back out the other side. She gracefully finishes her spin before returning to you."
        $ scene_manager.update_actor(the_person, position = "kissing")
        "[the_person.title] whispers in your ear."
        the_person "You're doing great! I think you are a natural."
        $ the_person.change_happiness(2)
        $ the_person.change_love(2)
        $ the_person.change_obedience(2)
    else:
        "You easily lead her into a reverse spin out the other side the way the instructor led. Her skirt flares up as she spins gracefully and then returns to your side."
        $ mc.change_locked_clarity(10)
        $ scene_manager.update_actor(the_person, position = "kissing")
        "[the_person.title] whispers in your ear."
        the_person "Are you sure this is your first time doing this? You have the manner of someone experienced sir..."
        $ the_person.change_obedience(5)
        $ the_person.change_love(5)
    "As you continue your first salsa dancing lesson, that trend continues."
    if mc_dancing_skill() < 4:
        "You are bumbling and awkward, but you enjoy the chance to get close with this sexy señora."
        $ mc.change_locked_clarity(10)

    elif mc_dancing_skill() < 10:
        "While you don't have nearly the skill of your partner, you feel like you are learning fairly quick."
        "By the end of the night, you are spinning and dancing with [the_person.possessive_title]. While you still make a few mistakes, you are getting better."
        "It is nice to get so close and personal with this señora."
        $ mc.change_locked_clarity(20)
    else:
        "You take to salsa dancing like a natural. Throughout the night you have her spinning and moving to the music."
        "After a short time, you stop listening to the instructor and start doing things your own way. You lead [the_person.possessive_title] around the dance floor with authority."
        "At the end of the lesson, she is close to you again, breathless. A light sheen of sweat makes her skin shine."
        "You hands on her body throughout the dancing has definitely put sexual tension in the air."
        $ mc.change_locked_clarity(30)
        $ the_person.change_slut_temp(5)
    $ scene_manager.update_actor(the_person, position = the_person.idle_pose)
    "Tired from your evening, you chat with [the_person.possessive_title] before you leave."
    the_person "So, they do this most evenings here. If you ever want a dance partner, I love to dance!"
    mc.name "I'll remember that. It might be a good way to unwind a bit after a long day at work."
    "You can now take [the_person.title] dancing any evening she is at the bar."
    $ camilla.event_triggers_dict["go_dancing"] = True
    $ scene_manager.clear_scene()
    call advance_time from _call_advance_camilla_post_dance_lesson_01

    return

label camilla_go_dancing_label(the_person):
    pass
    return

label camilla_take_pics_label(the_person):  #Not the first time.
    mc.name "Hey, you wanna sneak off for a bit and take some pictures?"
    "[the_person.possessive_title] flashes you her beautiful smile."
    the_person "Si! You know what to do!"
    $ mc.change_location(work_bathroom)
    $ mc.location.show_background()
    "You head to the lady's room. [the_person.title] soon follows behind you. She locks the door as she closes it."
    $ the_person.draw_person (position = "kissing")
    "You waste no time. She throws her arms around you and you begin to make out."
    if the_person.effective_sluttiness() > 30 and not the_person.outfit.tits_available():
        "[the_person.possessive_title] steps back suddenly."
        the_person "Let me just get this off... Papi loves it when I have my tits out for this..."
        "She hands you her phone with the camera app out. You snap some pictures as she starts to strip."
        while not the_person.outfit.tits_available():   #TODO change this to use more recent strip code
            $ the_clothing = the_person.outfit.get_upper_top_layer()
            "[the_person.possessive_title] takes off her [the_clothing.name]."
            $ the_person.draw_animated_removal(the_clothing)
            $ the_clothing = None
        "With her tits completely exposed, she saunters back over to you then starts to get down on her knees."
    else:
        "[the_person.possessive_title] slowly starts to get down on her knees in front of you."
    $ the_person.draw_person(position = "blowjob")
    "You can tell that [the_person.title] is hungry. She wastes no time pulling your pants down, followed quickly by your underwear."
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
        # call fuck_person(the_person, start_position = deepthroat, start_object = make_floor(), skip_intro = True, girl_in_charge = True, position_locked = True) from _call_camilla_sex_description_CSH011
        call get_fucked(the_person, start_position = deepthroat, start_object = make_floor(), skip_intro = True, allow_continue = False) from _call_camilla_sex_description_CSH011
    else:
        the_person "Mmmm, I can't wait any longer... I have to taste it!"
        $ the_person.break_taboo("sucking_cock")
        "She opens up her mouth and wraps her lips around your meat."
        "You snap some pictures as she pulls of and begin to run her tongue up and down along the sides of your cock."
        mc.name "Mmm, that feels great [the_person.title]."
        "You decide to just enjoy her skilled mouth going down on you."
        # call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = True, position_locked = True) from _call_camilla_sex_description_CSH012
        call get_fucked(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, allow_continue = False) from _call_camilla_sex_description_CSH012

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

#CSH10
label camilla_bathroom_blowjob_label(the_person):
    $ camilla.event_triggers_dict["take_pics"] = True
    mc.name "Hey, so uhh... want me to take some pictures for you?"
    "You see a bright red flush in her cheeks, but she quickly nods."
    the_person "Si! I would like that...a lot!"
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
    $ mc.change_locked_clarity(20)
    the_person "Mm... mmm.... mmmmmmmmmff..."
    "She is moaning in your mouth. You can tell the naughtiness of finally getting intimate with someone other than her husband is really turning her on."
    $ the_person.change_arousal(10)
    the_person "Ok... wow this is hot. This is my first time ever doing something like this... so... I want you to just let me do my thing, ok?"
    "You quickly agree."
    the_person "Also, could you take my phone? And take some pictures for me? Papi asked me to..."
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
    $ mc.change_locked_clarity(40)
    $ the_person.draw_person(position = "blowjob")
    "[the_person.possessive_title] tugs at your belt, then slowly lowers your pants."
    "One more tug on your underwear, and your erection springs free."
    the_person "Wow! I haven't seen anything other than hubby for... years..."
    "She begins to stroke you softly with her hand."
    the_person "Mmmmm.... its so hard... and hot!"
    "You moan as she strokes you. You make sure to snap a couple pictures."
    $ mc.change_arousal(10)
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(40)
    the_person "Does that feel good? I bet it does... I just wanna make you feel good..."
    "She closes her eyes, then opens her mouth. She slowly rubs the tip back and forth along her slithery tongue."
    the_person "Mmm, you taste good too."
    "She starts to take you into her mouth. You snap a few more pictures of this beautiful senora, on her knees servicing you."
    "[the_person.possessive_title]'s head is now bouncing up and down on your cock. Her pouty lips feel amazing sliding up and down your length."
    $ the_person.change_arousal(20)
    $ mc.change_arousal(20)
    $ mc.change_locked_clarity(40)
    "You forget you are supposed to take pictures and begin to just enjoy the wonderful sensations."
    # call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = True, position_locked = True) from _call_camilla_sex_description_CSH010
    call get_fucked(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, allow_continue = False) from _call_camilla_sex_description_CSH010
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
    $ the_person.event_triggers_dict["camilla_blowjob_pic_day"] = day + 1
    $ the_person.apply_planned_outfit()
    $ the_person.add_unique_on_room_enter_event(camilla_blowjob_text)
    return

label camilla_blowjob_text_label(the_person):
    mc.name "So... how did it go with the pictures?"
    "[the_person.possessive_title] gives you a quick smile."
    the_person "Well, I sent them off to him as he was getting off work, and I got an almost immediate response. 'Come home now'. No explanation or anything..."
    the_person "At first I got really scared. Did I just completely fuck up? So I went straight home..."
    the_person "When I got home, he was waiting for me... He umm... he handcuffed me with my hands behind my back... I didn't even know he had handcuffs!"
    "Her voice is starting to get excited as she recounts some of the details."
    the_person "He forced me down on my knees and then said... he said that I was a dirty little slut, and that after using my mouth on another man he would have to... reclaim it."
    the_person "So I opened up and I let him use my mouth... god I never could have imagined my husband doing that to me could be so hot!"
    the_person "Now... I'm a good wife... I've always, you know, swallowed for him. But this time..."
    "Her voice trails off a bit as she recalls the details. A smile on her face."
    the_person "I've never, ever had to swallow soooooo much. It was so hot, like a firehose it just kept cumming..."
    "You shift uncomfortably. This story is starting to turn you on!"
    $ mc.change_arousal (20)
    $ mc.change_locked_clarity(20)
    the_person "Haaa... sorry! I probably should have just said that it went well."
    mc.name "No it is quite alright. I was a little concerned with how things would go for you, but I'm glad that it turned out well!"
    $ the_person.draw_person(position = "stand4", emotion = "happy")
    the_person "It really did! So uhh, if you wanna go again, just ask. I'd be happy to be of service, BUT, we need to set some ground rules first!"
    mc.name "Okay, I'm down for that."
    the_person "Okay, well, like I said. I'm a good wife! I love my husband. He always comes first."
    "You nod in understanding."
    the_person "If you try to make me choose between you two, I'll choose him, every time. So lets just keep this casual, okay?"
    mc.name "Sounds good. Purely physical. I'm completely okay with that."
    the_person "Right... here, let's exchange numbers. I'll text you and if we're both free, we can screw around, no strings attached!"
    "You agree. You and [the_person.title] exchange numbers."
    the_person "Okay, well, I need to get going. I'm sure I'll see you around soon..."
    "You say goodbye and head out. Hot damn! You are now friends with benefits with a hot wife. You bet the sex is going to be amazing..."
    call advance_time from _call_advance_camilla_sex_discussion
    #TODO figure out how to add phone numbers to MC's phone
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
        call fuck_person(the_person, start_position = SB_doggy_standing, start_object = make_counter(), skip_intro = True, skip_condom = True) from _call_camilla_sex_description_CSH020
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
        call free_strip_scene(the_person) from _CS_free_strip_scene_camilla_021
        "You got lots of pics of her strip tease. You take a few more as she saunters over to you."
        the_person "Come on, lets fuck!"
        call fuck_person(the_person) from _call_casual_sex_mod_camilla_022
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
    call fuck_person(the_person, start_position = doggy, start_object = make_bed(), skip_intro = True, skip_condom = True) from _call_camilla_sex_description_CSH040
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
    call fuck_person(the_person) from _call_casual_sex_mod_camilla_505
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


init -1 python:
    def camilla_can_get_drinks():
        return camilla.event_triggers_dict.get("get_drinks", False)

    def camilla_is_open():
        return camilla.event_triggers_dict.get("is_open", False)

    def camilla_can_go_dancing():
        return camilla.event_triggers_dict.get("go_dancing", False)

    def camilla_will_take_pics():
        return camilla.event_triggers_dict.get("take_pics", False)

    def camilla_can_go_to_her_place():
        return camilla.event_triggers_dict.get("her_place", False)

    def mc_dancing_skill(): #Wrapper for measuring MC's progress learning to salsa dance.
        return mc.charisma + round((mc.max_energy - 100) / 20)
