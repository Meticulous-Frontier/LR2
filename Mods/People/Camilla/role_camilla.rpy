
#Init  functions
init 2 python:

    camilla_spot_at_bar = Action("Camilla at the bar", camilla_spot_at_bar_requirement, "camilla_spot_at_bar_label")
    camilla_get_a_drink = Action("Get a drink {image=gui/heart/Time_Advance.png}", camilla_get_a_drink_requirement, "camilla_get_a_drink_label", is_fast = False)
    camilla_go_dancing = Action("Salsa Dancing", camilla_go_dancing_requirement, "camilla_go_dancing_label")
    camilla_take_pics = Action("Take Sexy Pics {image=gui/heart/Time_Advance.png}", camilla_take_pics_requirement, "camilla_take_pics_label", is_fast = False)
    camilla_dance_lessons = Action("Dancing Lessons", camilla_dance_lessons_requirement, "camilla_dance_lessons_label")
    camilla_blowjob_text = Action("Blowjob Discussion", camilla_blowjob_text_requirement, "camilla_blowjob_text_label")
    camilla_her_place = Action("Cuckold Visit", camilla_her_place_requirement, "camilla_her_place_label")
    camilla_home_sex = Action("Cuckold Visit {image=gui/heart/Time_Advance.png}", camilla_home_sex_requirement, "camilla_home_sex_label", is_fast = False)
    camilla_outfit_help = Action("Shopping Trip", camilla_outfit_help_requirement, "camilla_outfit_help_label")
    camilla_lingerie_help = Action("Lingerie Shopping", camilla_lingerie_help_requirement, "camilla_lingerie_help_label")
    camilla_formal_date = Action("Camilla Comes Over", camilla_formal_date_requirement, "camilla_formal_date_label")
    camilla_gives_anal_virginity = Action("Camilla Tries Anal", camilla_gives_anal_virginity_requirement, "camilla_gives_anal_virginity_label")

    def camilla_mod_initialization():
        camilla_wardrobe = wardrobe_from_xml("Camilla_Wardrobe")
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
        camilla_role = Role(role_name ="camilla", actions =[camilla_get_a_drink, camilla_go_dancing, camilla_take_pics, camilla_home_sex], hidden = True)
        camilla_job = Job("Lifestyle Coach", camilla_role, mall, work_times = [1,2])

        #global camilla_role
        global camilla
        camilla = make_person(name = "Camilla", last_name ="Rojas", body_type = "thin_body", age = 34, face_style = "Face_2",  tits="D", height = 0.98, hair_colour="golden blonde", hair_style = braided_bun, skin="tan" , \
            personality = introvert_personality, name_color = "#228b22", dial_color = "228b22", starting_wardrobe = camilla_wardrobe, \
            stat_array = [1,4,4], skill_array = [1,1,3,5,1], sex_skill_array = [4,2,2,2], sluttiness = 7, obedience_range = [70, 85], happiness = 119, love = 0, \
            relationship = "Married", kids = 0, force_random = True, base_outfit = camilla_base_outfit, type = 'story',
            forced_opinions = [["dancing", 2, True], ["fashion", 2, False], ["flirting", 1, False], ["working", 1, False], ["the colour purple", 2, False], ["dresses", 2, False], ["the colour blue", -2, False], ["skirts", 1, False]],
            forced_sexy_opinions = [["being submissive", 2, False], ["getting head", 2, False], ["drinking cum", 1, False], ["giving blowjobs", 2, False], ["public sex", 1, False], ["showing her ass", 2, False], ["anal sex", -2, False], ["bareback sex", 2, False]])

        camilla.generate_home()
        camilla.change_job(camilla_job, job_known = True)
        camilla.set_schedule(downtown_bar, the_times = [3])
        camilla.home.add_person(camilla)

        camilla.event_triggers_dict["intro_complete"] = False    # True after first talk
        camilla.event_triggers_dict["get_drinks"] = False
        camilla.event_triggers_dict["go_dancing"] = False
        camilla.event_triggers_dict["take_pics"] = False
        camilla.event_triggers_dict["will_fuck"] = False
        camilla.event_triggers_dict["her_place"] = False
        camilla.event_triggers_dict["outfit_help"] = False
        camilla.event_triggers_dict["lingerie_help"] = False
        camilla.event_triggers_dict["formal_date"] = False
        camilla.event_triggers_dict["lost_anal_virginity"] = False
        camilla.event_triggers_dict["boudoir_stage"] = 0

        camilla.fertility_percent = -1000.0 #She's infertile


        # add appoint
        #office.add_action(HR_director_appointment_action)

        # camilla_intro = Action("camilla_intro",camilla_intro_requirement,"camilla_intro_label") #Set the trigger day for the next monday. Monday is day%7 == 0
        # mc.business.add_mandatory_crisis(camilla_intro) #Add the event here so that it pops when the requirements are met.

        # set relationships
        # town_relationships.update_relationship(camilla, stephanie, "Sister")
        # town_relationships.update_relationship(nora, camilla, "Friend")
        # town_relationships.update_relationship(lily, camilla, "Rival")

        camilla.add_role(lifestyle_coach_role)
        camilla.add_unique_on_room_enter_event(lifestyle_coach_intro)
        return


#Requirement Functions

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
        if the_person.location == downtown_bar and camilla_will_take_pics() and the_person.effective_sluttiness() > 40:
            return True
        return False

    def camilla_blowjob_text_requirement(the_person):
        if day >= camilla.event_triggers_dict.get("camilla_blowjob_pic_day", 9999):
            return True
        return False

    def camilla_her_place_requirement():
        if time_of_day == 4:
            return True
        return False

    def camilla_home_sex_requirement(the_person):
        if camilla_can_go_to_her_place() and time_of_day == 4:
            if the_person.is_home():
                return True
        return False

    def camilla_outfit_help_requirement(the_person):
        if the_person.location == mall and the_person.love >= 20:
            return True
        return False

    def camilla_lingerie_help_requirement(the_person):
        if the_person.location == mall and the_person.love >= 40 and camilla_will_take_pics():
            return True
        return False

    def camilla_formal_date_requirement():
        if time_of_day == 3 and camilla.love >= 60 and camilla_will_take_pics() and day%7 < 4:
            return True
        return False

    def camilla_gives_anal_virginity_requirement(the_person):
        return False

#Additional Camilla Functions
init 2 python:
    def camilla_wear_salsa_dress():
        salsa_dress = camilla.wardrobe.get_outfit_with_name("Camilla Sexy Salsa Outfit")
        if salsa_dress:
            camilla.apply_outfit(salsa_dress)
        return

    def get_camilla_lingerie_set_white():
        outfit = Outfit("Lingerie Set Classic White")
        outfit.add_upper(teddy.get_copy(),colour_white)
        outfit.add_feet(garter_with_fishnets.get_copy(), colour_white)
        outfit.add_feet(high_heels.get_copy(), colour_white)
        return outfit

    def get_camilla_lingerie_set_pink():
        outfit = Outfit("Pink Lingerie")
        outfit.add_upper(teddy.get_copy(),colour_pink)
        outfit.add_feet(garter_with_fishnets.get_copy(), colour_pink)
        outfit.add_feet(high_heels.get_copy(), colour_pink)
        return outfit

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
    "You sit down in a bar stool next to [the_person.possessive_title]."
    mc.name "So how long have you been working as a lifestyle coach?"
    the_person "Honestly, not too long. I mainly just do it as an extra source of income to supplement what my hubby brings in."
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
    "You feel bad. You notice that her glass is almost empty. You wave down the bartender. When he walks over, he smiles wide at [the_person.title]."
    "?????" "Something I can get for you?"
    mc.name "Can I get a beer and another for my friend?"
    "?????" "Sure. A beer and another paloma for the lovely miss [the_person.last_name]."
    "The bartender walks off. He seems to know [the_person.title]. She must be a regular here?"
    mc.name "Ah, you come here often then?"
    the_person "I do. I'm here most evenings. I like to have a drink before I head home each night. My husband works late."
    mc.name "I see. I'm here somewhat often as well. Maybe we could have a drink together once in a while?"
    the_person "I... I suppose that would be alright."
    "You sit back in the chair and chat with [the_person.possessive_title] for a while. You both enjoy the time together, getting to know one another as friends."
    $ the_person.change_love(3)
    $ mc.business.change_funds(-20)
    "Eventually you settle up with the bartender. You notice him gesture at [the_person.title] when she isn't looking, and gives you a little wink."
    "You aren't sure... is he trying to say she's... available? Maybe since her husband works late she picks up guys at the bar..."
    "You file it away in your brain. Maybe you could come back and have drinks with her again. A bar would be an ideal place to dose her with a few serums too..."
    "You get up and say goodbye to [the_person.possessive_title]."
    mc.name "Thank you for the conversation. I'll see you around [the_person.title]."
    the_person "Take care [the_person.mc_title]."
    "You can now have drinks with [the_person.title] at the bar in the evenings."
    $ camilla.event_triggers_dict["get_drinks"] = True
    $ camilla.add_unique_on_room_enter_event(camilla_outfit_help)
    #TODO advance time
    return


label camilla_get_a_drink_label(the_person):
    mc.name "Care to get a drink, [the_person.title]?"
    "You consider for a moment. If you offer to buy her a drink, you'll have a chance to slip a serum into it."
    $ ran_num = (mc.charisma + (the_person.effective_sluttiness() / 10)) * 10  #More willing to let you buy a drink for her as she gets sluttier
    #$ bartender_name = Person.get_random_male_name()
    if camilla_can_go_dancing():
        $ ran_num = 100
    menu:
        "Offer to Buy\n{color=#ff0000}{size=18}Success Chance: [ran_num]%%{/size}{/color}":
            mc.name "Hey, let me buy you a drink."
            if renpy.random.randint(0,100) < ran_num:  #Success
                the_person "Hmm... Okay! That sounds great! I'll go find us a table!"
                "You head over to the bar and order yourself a beer, and a cocktail for [the_person.title]."
                the_person.SO_name "Here you go, one beer, and a cocktail for the beautiful [the_person.fname]."
                "Sounds like the bartender knows [the_person.title] pretty well. She must be in here often!"
                "The place is busy, so it's easy to slip some serum into her drink."
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
        "She looks a little embarrassed, but doesn't respond negatively to your comment."
        mc.name "So, your hubby is okay with you going out to the bar all by yourself?"
        the_person "Si, he doesn't mind. In fact, he kind of encourages it."
        mc.name "Really? That's interesting."
        "[the_person.possessive_title] takes a sip of her drink and takes a moment."
        the_person "Truth be told, hubby has been encouraging me recently to umm... get out and meet new people... men specifically."
        "Her statement catches you a little bit by surprise."
        the_person "To be honest... I'm not sure I'm going to... but hubby has this fantasy thing where I... get with other guys..."
        "Ah her husband is some kind of cuckold."
        mc.name "That's interesting. Manage to snag any yet?"
        the_person "No. I'm... I just want to be a good wife... and honestly I never thought my hubby would ask me to do something like this."
        the_person "I'm still too nervous, but I like to come to the bar and have a couple drinks. Maybe someday I'll actually go through with it."
        "[the_person.possessive_title] takes another long sip of her drink."
        the_person "I don't know why but, it's nice being able to talk to you. Something about you puts me at ease."
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
            "That sounds suspiciously like a date. With this smoking hot señorita in an open relationship, the implications are impossible to ignore."
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
            mc.name "No, sometimes it is nice to just relax and have a drink."
            the_person "Yeah, I agree."
            "You chat with [the_person.possessive_title] for a bit."
            "There is definitely some sexual tension in the air between you two, but she knows she can talk to you about it when she is ready."
            $ mc.change_locked_clarity(10)

    elif not camilla_will_fuck():
        mc.name "How are things going? Still going well with the husband?"
        the_person "Oh yes... I haven't had the guts to do anything with any other guys yet, but, those blowjob pictures definitely changed our sex life."
        mc.name "Good, glad to hear it's working out for you."
        the_person "Yeah... he umm... he's started asking me if, you know, I'm almost ready to take things to the next level..."
        mc.name "Oh yeah? Meaning what?"
        the_person "Well, you know, not just blowing a guy but, letting him fuck me..." #TODO Finish this
        "You just about choke on your drink."
        mc.name "Hey, I'd be glad to help out. But obviously, don't rush into it if you aren't ready yet."
        "[the_person.title] takes a long sip from her cocktail."
        if the_person.effective_sluttiness() > 60 and the_person.is_willing(SB_doggy_standing):
            "In the background, you hear the music shift a bit as some salsa music begins to play."
            "[the_person.possessive_title] looks you up and down for moment, then downs the remainder of her drink."
            the_person "Nothing like a stiff drink. Would you like to dance, [the_person.mc_title]?"
            "Something about the way she asks you makes it clear that she might be up for more than just dancing."
            mc.name "Let's do it."
            call camilla_dancing_sex_label(the_person) from _camilla_dance_and_fuck_01
        else:
            the_person "Ay, caramba, [the_person.mc_title], I just don't think I'm ready."
            "You nod in understanding."
            the_person "But I'd be glad to, you know, get you off in the usual way..."
            mc.name "Sounds good. I'll try to look for you next time I'm around."
            $ mc.change_locked_clarity(20)

    elif not camilla_can_go_to_her_place():
        mc.name "How are things going? You husband happy with the pics we've been sending him?"
        the_person "Oh si... he loves the photos. And I love what he does to me after he gets them!"
        mc.name "Hah, that's good! I'm glad, it sounds like it has really spiced things up for you two."
        "[the_person.possessive_title] takes a long sip of her drink."
        if the_person.effective_sluttiness() > 80:
            the_person "So, he's started asking, when am I gonna bring you back to our place..."
            mc.name "Oh? He wants pictures of us in his own house huh?"
            the_person "Well, not exactly."
            mc.name "What do you mean?"
            the_person "Well, he wants to be there. He wants to watch."
            "Wow, her husband is really getting into the cuckolding thing!"
            mc.name "And how do you feel about it? Do you feel like you're ready for that?"
            the_person "Honestly? I'm getting a little turned on just thinking about it."
            mc.name "I'll admit, I'm' a little hesitant to do something like that in front of your husband... but if you're sure about it."
            the_person "Yeah... I'm certain! Let me know when would be a good time to come over, and I'll get the details sorted."
            "Wow, she wants you to come to her house and fuck her in front of her husband! You should probably get on that before the opportunity passes!"
            menu:
                "Tonight":
                    mc.name "What about tonight?"
                    the_person "I... you want to come over tonight?"
                    mc.name "Sure. I'm not doing anything."
                    "[the_person.possessive_title] gives you her address."
                    the_person "Come over tonight, around 10pm. You won't regret it! I'm going to go now and get... set up..."
                    $ mc.business.add_mandatory_crisis(camilla_her_place)
                    $ the_person.learn_home()
                "Soon":
                    pass
            "You and [the_person.title] finish your drinks and then you say goodbye."
        else:
            "[the_person.title] clearly has something on her mind, but she doesn't seem to have the courage to speak up."
            "As far as things have gone with her, is her husband pushing her to go even farther?"
            the_person "Yeah, it has certainly worked wonders..."
            "You make small talk with [the_person.possessive_title] for a while. Eventually you finish your drinks and part ways."

    else:
        the_person "Thanks for the drink, [the_person.mc_title]. This whole adventure has really supercharged my sex life, it's nice to have a break from fucking and just enjoy a stiff drink."
        mc.name "Yeah, so is [the_person.SO_name] still enjoying your new lifestyle?"
        the_person "Oh god, we both are. I've started fucking around with a couple other guys too. Last time I came home, he tied me up and umm... reclaimed me in every hole he could fit it in..."
        mc.name "Damn! That sounds hot!"
        the_person "Yeah! I came so many times... you didn't forget my address did you? You should stop by sometime and we could fuck around again."
        mc.name "Don't worry, I haven't forgotten."
        "You and [the_person.title] finish your drinks and then you say goodbye."

    call advance_time from _call_advance_camilla_drink
    return

label camilla_dance_lessons_label():
    $ the_person = camilla
    $ camilla_wear_salsa_dress()
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
    $ the_person.change_slut(2)
    the_person "You are right about that, but tonight, it is all about you!"
    "You make some idle chatter at the bar as you wait for the lessons to begin. You admit you are pretty nervous, but as people filter in, you see a lot of people around who also look new at this."
    "?????" "Alright, everyone here for salsa lessons, we are forming up over here! Come with your partner!"
    "You and [the_person.possessive_title] head over."
    "?????" "Alright, my name is Alvero, and I'll be your instructor tonight! First let's start off with a little..."
    "You listen intently as the instructor begins initial warm up instructions."
    "Finally, it's time to start dancing."
    $ scene_manager.update_actor(the_person, position = "kissing")
    "You get close to [the_person.title] as the music starts. You listen as the instructor begins to issue commands."
    "Alvero" "Alright fellas, remember, your sole purpose while salsa dancing is to display the beautiful flower you are partners with."
    $ scene_manager.update_actor(the_person, position = "kissing", display_transform = character_left_flipped)
    "You try one of the moves as instructed, moving [the_person.possessive_title] away from you a bit and allowing her to make a graceful spin back to you."
    $ scene_manager.update_actor(the_person, position = "back_peek", display_transform = character_right)
    "She spins beautifully and stops with her back to you. She looks back and gives you a sly smile."
    if mc_dancing_skill() < 4:
        "Unfortunately you fumble a bit as she spins back out. You don't trip but you definitely feel awkward compared to the grace your partner is exhibiting."
        $ scene_manager.update_actor(the_person, position = "kissing")
        "[the_person.title] whispers in your ear."
        the_person "Don't worry, we were all new at one time. You are doing great."
        $ the_person.change_stats(happiness = 2, love = 2)
    elif mc_dancing_skill() < 10:
        "You spin her back out the other side. She gracefully finishes her spin before returning to you."
        $ scene_manager.update_actor(the_person, position = "kissing")
        "[the_person.title] whispers in your ear."
        the_person "You're doing great! I think you are a natural."
        $ the_person.change_stats(happiness = 2, love = 2, obedience = 2)
    else:
        "You easily lead her into a reverse spin out the other side the way the instructor led. Her skirt flares up as she spins gracefully and then returns to your side."
        $ mc.change_locked_clarity(10)
        $ scene_manager.update_actor(the_person, position = "kissing")
        "[the_person.title] whispers in your ear."
        the_person "Are you sure this is your first time doing this? You have the manner of someone experienced sir..."
        $ the_person.change_stats(obedience = 5, love = 3)
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
        "Your hands on her body throughout the dancing has definitely put sexual tension in the air."
        $ mc.change_locked_clarity(30)
        $ the_person.change_slut(2, 50)
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
    if camilla_will_fuck(): #If we've had sex before, open up to that.
        "Knowing you don't have much time, you start getting her naked right away."
        "Piece by piece, you take [the_person.title]'s clothes off."

        $ the_person.strip_outfit(position = "kissing")
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(20)
        the_person "Here, take this. You know what to do!"
        "[the_person.possessive_title] hands you her phone. You pull up her photo app."
        $ the_person.draw_person(position = "missionary")
        "She hops up on the bathroom sink and spreads her legs, showing you everything."
        "Moisture glistens between her legs, her pussy looks great and ready for you to fuck. You snap several pictures."
        the_person "Here, let me see it now..."
        "She takes her phone back. You see her attach a couple to a text message and send it."
        the_person "Alright, I'm going to set this up to take a picture every few seconds... now get over here and fuck me!"
        call fuck_person(the_person, start_object = make_sink(), private = True) from _call_camilla_sex_photo_shoot_01
        $ the_report = _return
        if the_report.get("guy orgasms", 0) > 0:
            #description for all possible cum locations
            if the_person.has_mouth_cum():
                $ the_person.draw_person()
                "[the_person.possessive_title] stands up as you grab her phone."
                "She couldn't quite swallow all your cum, some of it is slowly dripping down the sides of her mouth. You snap a couple pictures."
            elif the_person.has_face_cum():
                $ the_person.draw_person()
                "[the_person.possessive_title] stands up as you grab her phone."
                "Her face is plastered with your sticky seed. You snap a couple pictures of her sperm covered smile."
            elif the_person.has_tits_cum():
                $ the_person.draw_person()
                "[the_person.possessive_title] stands up as you grab her phone."
                "Her tits are plastered with your sticky seed. You snap a couple pictures of her snow capped mountains."
            elif the_person.has_ass_cum():
                $ the_person.draw_person(position = "standing_doggy")
                "[the_person.possessive_title] bends over the bathroom sink. Her ass is plastered with your sticky seed."
                "You grab her phone and snap a couple pictures of her ass with your cum covering it."
            elif the_person.has_creampie_cum():       #We assume we finished inside her#
                $ the_person.draw_person(position = "missionary")
                "[the_person.possessive_title] sits on the edge of the bathroom sink, mirroring her pose before you started fucking."
                "This time though, her cunt is a little gaped and your seed is clearly leaking out and down her legs."
                "You grab her phone and snap a couple pictures of her well used pussy with your cum dripping out of it."
            else:   #We have no idea where the cum is. It got wasted?
                "You grab her phone and snap a couple pictures of her well used pussy."
        if the_report.get("girl orgasms", 0) > 0:
            the_person "Oh my god... that was amazing. You always make me feel so good."

    else:
        if the_person.effective_sluttiness() > 30 and not the_person.outfit.tits_available():
            "[the_person.possessive_title] steps back suddenly."
            the_person "Let me just get this off... Papi loves it when I have my tits out for this..."
            "She hands you her phone with the camera app out. You snap some pictures as she starts to strip."
            if the_person.outfit.can_half_off_to_tits():
                $ generalised_strip_description(the_person, the_person.outfit.get_half_off_to_tits_list(), half_off_instead = True)
            else:
                $ generalised_strip_description(the_person, the_person.outfit.get_tit_strip_list())

            "With her tits completely exposed, she saunters back over to you then starts to get down on her knees."
        else:
            "[the_person.possessive_title] slowly starts to get down on her knees in front of you."
        $ the_person.draw_person(position = "blowjob")
        "You can tell that [the_person.title] is hungry. She wastes no time pulling your pants down, followed quickly by your underwear."
        "Your hardened cock springs out. Her agile hands grasp it and begin to stroke."
        if the_person.is_willing(deepthroat):
            the_person "Mmm, I've been working on a new skill lately... since we started doing this. Mind if I practice on you?"
            mc.name "Sure I guess, but what is..."
            "She doesn't wait for you to finish your response. In one, smooth motion, she opens her mouth and swallows your cock whole."
            $ the_person.break_taboo("sucking_cock")
            "Past her lips, to the back of her tongue, and down her throat the tip of your dick goes."
            mc.name "Oh fuck!"
            "You make sure to snap more pictures of her. She's getting good at this!"
            "You decide to just enjoy her skilled mouth going down on you."
            # call fuck_person(the_person, start_position = deepthroat, start_object = make_floor(), skip_intro = True, girl_in_charge = True, position_locked = True) from _call_camilla_sex_description_CSH011
            call get_fucked(the_person, start_position = deepthroat, start_object = make_sink(), private = True, skip_intro = True, allow_continue = False) from _call_camilla_sex_description_CSH011
        else:
            the_person "Mmmm, I can't wait any longer... I have to taste it!"
            $ the_person.break_taboo("sucking_cock")
            "She opens up her mouth and wraps her lips around your meat."
            "You snap some pictures as she pulls off and begins to run her tongue up and down along the sides of your cock."
            mc.name "Mmm, that feels great [the_person.title]."
            "You decide to just enjoy her skilled mouth going down on you."
            # call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = True, position_locked = True) from _call_camilla_sex_description_CSH012
            call get_fucked(the_person, start_position = blowjob, start_object = make_sink(), private = True, skip_intro = True, allow_continue = False) from _call_camilla_sex_description_CSH012

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
    the_person "Si! I would like that... a lot!"
    "She takes a quick look around."
    the_person "Let me just go talk to the bartender... head to the lady's room and wait outside... I'll be over in a second."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] walks away to talk to the bartender. You make your way over to the lady's room."
    $ the_person.draw_person(position = "stand4")
    "Soon, [the_person.title] comes over, holding a sign that says 'Bathroom closed for renovations: Please use men's room"
    $ mc.change_location(work_bathroom)
    $ mc.location.show_background()
    "You both take a quick look around, and when the coast is clear, you both walk into the bathroom and lock the door behind you."
    "You waste no time, you quickly wrap your arms around [the_person.title] and start making out with her."
    $ the_person.draw_person(position = "kissing")
    $ mc.change_locked_clarity(20)
    the_person "Mm... mmm... mmmmmmmmmff..."
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
    the_person "Mmmmm... it's so hard... and hot!"
    "You moan as she strokes you. You make sure to snap a couple pictures."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(40)
    the_person "Does that feel good? I bet it does... I just wanna make you feel good..."
    "She closes her eyes, then opens her mouth. She slowly rubs the tip back and forth along her slithery tongue."
    the_person "Mmm, you taste good too."
    "She starts to take you into her mouth. You snap a few more pictures of this beautiful señora, on her knees servicing you."
    "[the_person.possessive_title]'s head is now bouncing up and down on your cock. Her pouty lips feel amazing sliding up and down your length."
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(40)
    "You forget you are supposed to take pictures and begin to just enjoy the wonderful sensations."
    # call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = True, position_locked = True) from _call_camilla_sex_description_CSH010
    call get_fucked(the_person, start_position = blowjob, start_object = make_sink(), private = True, skip_intro = True, ignore_taboo = True,  allow_continue = False) from _call_camilla_sex_description_CSH010
    $ the_report = _return
    if the_report.get("girl orgasms", 0) > 0:
        the_person "Wow... I can't believe I came... while I was blowing you! That was fucking hot!"
    else:
        the_person "Wow... that was hot!"

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
    $ the_person.draw_person()
    "You walk up to [the_person.possessive_title]."

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
    $ mc.change_locked_clarity(20)
    the_person "Haaa... sorry! I probably should have just said that it went well."
    mc.name "No it's alright. I was a little concerned with how things would go for you, but I'm glad that it turned out well."
    $ the_person.draw_person(position = "stand4", emotion = "happy")
    the_person "It really did! So uhh, if you wanna go again, just ask. I'd be happy to be of service, BUT, we need to set some ground rules first!"
    mc.name "Okay, I'm down for that."
    the_person "Okay, well, like I said. I'm a good wife! I love my husband. He always comes first."
    "You nod in understanding."
    the_person "If you try to make me choose between you two, I'll choose him, every time. So let's just keep this casual, okay?"
    mc.name "Sounds good. Purely physical. I'm okay with that."
    the_person "Right... here, let's exchange numbers. I'll text you and if we're both free, we can screw around, no strings attached!"
    "You agree. You and [the_person.title] exchange numbers."
    $ mc.phone.register_number(the_person)
    the_person "Okay, well, I need to get going. I'm sure I'll see you around soon..."
    "You say goodbye and head out. Hot damn! You are now friends with benefits with a hot wife. You bet the sex is going to be amazing..."
    call advance_time from _call_advance_camilla_sex_discussion
    return

#CSH20
label camilla_dancing_sex_label(the_person):
    if not camilla_will_fuck():   #We haven't gotten the good ending to this scene yet.
        $ scene_manager = Scene()
        $ scene_manager.add_actor(the_person, position = "walking_away")
        "You follow [the_person.title] out on to the dance floor."
        "You waste no time and grab [the_person.possessive_title]. You sync your movements to the beat and begin to move your bodies to the beat."
        $ scene_manager.update_actor(the_person, position = "kissing")
        "You bring her close, letting your body be close to hers. Heat begins to build as you get into the dance."
        $ scene_manager.update_actor(the_person, position = "kissing", display_transform = character_left_flipped)
        "When things start to get too heated, [the_person.possessive_title] moves away from you a bit."
        "You hold out your opposite hand, spinning her around gracefully back to you, finishing her spin with her back facing you."
        $ scene_manager.update_actor(the_person, position = "back_peek", display_transform = character_right)
        if mc_dancing_skill() >= 6: #Pass the dancing check
            "With [the_person.title] facing away from you, you put a hand on her hips and bring her close to you."
            "She slightly grinds her ass back against you as you keep moving to the beat. Her ass feels great moving back and forth against your rapidly rising erection."
            mc.name "Mmm, that feels good. I can't wait to get you alone..."
            $ the_person.change_arousal(20)
            $ mc.change_locked_clarity(20)
            "She gives a sigh and melts back into you. You let your hands roam all along the sides of her body, once in a while moving across the sides of her breasts."
            "Being careful not to push things too fast, you spin her out again, and then back to you."
        else:   #dancing check failed.
            "As you try to spin her back to you, clumsily you accidentally stick your foot out too far, and [the_person.title] trips over it."
            $ scene_manager.update_actor(the_person, position = "doggy", display_transform = character_right)
            the_person "Oof!"
            "You quickly help her up."
            $ scene_manager.update_actor(the_person, position = "stand3")
            mc.name "Sorry, I..."
            the_person "It's okay... let's just dance."
            "After your little mishap, it is clear that the energy between the two of you isn't as intense as it was. It takes all your concentration to keep from tripping her up again."
            "When you finish, [the_person.possessive_title] moves to the side of the dance floor."
            the_person "Thank you for the dance, [the_person.mc_title], but I need to get going..."
            $ clear_scene()
            "As [the_person.title] moves away from you, you can't help but feeling like you missed an opportunity tonight."
            "Note: Dancing skill is based on MC's Charisma and Energy levels. Try increasing Charisma and make sure energy is high before attempting this scene."
            return
        $ scene_manager.update_actor(the_person, position = "kissing")
        "[the_person.possessive_title] turns back to you and puts her arms around your shoulders. Your hands start on her hips, but soon drift down to her ass."
        the_person "I love this song. Let's dance to this and then..."
        "You notice her glance over to the bar. You follow her eyes and notice the bartender, [the_person.SO_name] is watching you dance."
        "You look back at [the_person.title]. You squeeze her supple ass and grind up against her slightly."
        the_person "Mmm... fuck that feels good."
        "[the_person.title] begins moving her hips against yours. Your cock, constrained in your clothing, is nestled against her crotch, aching to be let free."
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(30)
        "The song ends, and [the_person.title] looks at you."
        the_person "Ok... you know what to do... I'll meet you in the Lady's room in just a minute..."
        $ clear_scene()
        $ mc.change_location(work_bathroom)
        $ mc.location.show_background()
        "You head to the women's restroom and [the_person.title] soon meets you there."
        $ the_person.draw_person (position = "against_wall")
        "You grab her and pick her up. Her legs wrap around you."
        the_person "Oh god... I can't believe I'm doing this... but I need it so bad!"
        "You take her over to the bathroom sinks and set her on the edge of it. You start to strip her clothes off."
        if the_person.outfit.vagina_visible():
            "You stop for a second and admire [the_person.title]'s [the_person.pubes_description] little slit glistening in the florescent lights."
        else:
            "You quickly remove [the_person.title]'s clothes blocking the way to your prize."

            $ the_person.strip_to_vagina(position = "against_wall", prefer_half_off = True, visible_enough = True)
            $ the_person.change_arousal(20)

            "Once finished, You stop for a second and admire [the_person.title]'s [the_person.pubes_description] little slit glistening in the florescent lights."
        the_person "Oh! Shit I almost forgot!"
        $ the_person.draw_person(position = "walking_away")
        "[the_person.possessive_title] grabs her purse. She rummages through it for a moment then pulls out her phone."
        the_person "Can't forget this!"
        $ the_person.draw_person(position = "stand3")
        "She hands you her phone and you quickly pull up her camera app. While you are doing that [the_person.possessive_title] turns around and leans over the bathroom sink."
        $ the_person.draw_person (position = "standing_doggy")
        "You snap a couple pictures of her amazing ass while she is bent over."
        the_person "Okay, you better get your pants off, we don't have much time!"
        "You quickly drop your pants, letting your aching hard on spring free. You step behind [the_person.title], letting your cock nestle between her pliant ass cheeks."
        "You snap a few more pictures as you dry hump her ass crack a bit. Then you pull back a bit and get yourself pointed at her juicy slit."
        mc.name "Should I umm... wrap it up?"
        the_person "Don't bother, unless you REALLY want to. I'm actually infertile..."
        mc.name "Ah... I see..."
        "You change the camera app to take a video. You figure since this is her first time getting fucked by a man other than her husband it might come in handy..."
        "With one hand firmly on [the_person.possessive_title]'s hip, you steadily push yourself into her. She moans loudly and you capture the whole thing on glorious video."
        $ the_person.break_taboo("vaginal_sex")
        $ the_person.break_taboo("condomless_sex")
        the_person "Oh fuck that feels good. Fuck me good [the_person.mc_title]!"
        "You stop the video, you figure this is as good of a place as any to stop it. You take a few nice and slow strokes, snapping pictures of your cock penetrating her at various depths."
        "You look up and get one last picture of [the_person.title] in the mirror. Her mouth is open and she has one hand groping one of her own tits while her other hand is reaching back and grabbing your hip."
        "You set the phone down and begin to fuck her."
        $ mc.condom = False
        call fuck_person(the_person, start_position = SB_doggy_standing, start_object = make_sink(), private = True, skip_intro = True, skip_condom = True, ignore_taboo = True) from _call_camilla_sex_description_CSH020
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
            elif the_person.has_creampie_cum():       #We assume we finished inside her#
                "[the_person.possessive_title]'s pussy is dripping cum from your creampie."
                "You grab her phone and snap a couple pictures of her well used pussy with your cum dripping out of it."
            else:   #We have no idea where the cum is. It got wasted?
                "You grab her phone and snap a couple pictures of her well used pussy."
        if the_report.get("girl orgasms", 0) > 0:
            the_person "Oh my god... that was amazing. That felt so good."
        $ the_person.draw_person("stand3")
        the_person "Wow, I never knew cheating could feel so good. God, I can't wait until my husband reclaims me later... oh fuck."
        "[the_person.possessive_title] starts to touch herself a bit, getting herself excited thinking about what is in store for her later tonight. She quickly realizes she needs to stop though."
        $ the_person.event_triggers_dict["will_fuck"] = True
        "She takes her phone from you and starts going through the pictures you took."
        the_person "You'd better get going, [the_person.mc_title]. I'm going to send these to my husband..."

        $ the_person.event_triggers_dict["booty_call"] = True # unlock casual encounters. Am I still using this? I should probably get rid of this...

        $ clear_scene()
        $ the_person.apply_planned_outfit()
        $ mc.change_location(downtown_bar)
        $ mc.location.show_background()
        "After straightening up, you step out of the restroom and into the bar."
        "You just fucked [the_person.possessive_title], a married woman, in the bar bathroom! And you know this is probably not just going to be a one time thing."
        return


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
        "[the_person.possessive_title] turns back to you and puts her arms around your shoulders. Your hands start on her hips, but soon drift down to her ass."
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
        "You head to the women's restroom and [the_person.title] soon meets you there."
        $ the_person.draw_person (position = "stand4")
        the_person "Okay, I want you to sit on the bathroom sink. I'm gonna get naked for you."
        "She hands you her phone."
        the_person "Here we go! Get lots of good pics!"
        call strip_tease(the_person, for_pay = False, skip_intro = True) from _CS_free_strip_scene_camilla_021
        "You got lots of pics of her strip tease. You take a few more as she saunters over to you."
        the_person "Come on, let's fuck!"
        call fuck_person(the_person, start_object = make_sink(), private = True) from _call_casual_sex_mod_camilla_022
        "As you finish up, you make sure to take some pictures of the aftermath. You notice [the_person.possessive_title] is touching herself."
        the_person "Oh god, daddy is gonna fuck me so rough when he reclaims me tonight... I'm gonna be so sore. I can't wait!"
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
label camilla_her_place_label():
    $ the_person = camilla
    "You head over to [the_person.title]'s place. You can't believe you're gonna fuck her in front of her husband!"
    "You ring the doorbell. Soon [the_person.title] answers the door."

    $ the_person.change_to_hallway()
    $ the_person.apply_outfit(get_camilla_lingerie_set_white(), update_taboo = True)
    $ the_person.draw_person(position = "stand4")
    the_person "Señor! I wasn't sure you would actually come!"
    mc.name "Of course!"
    $ mc.change_location(the_person.home)
    $ mc.location.show_background()
    "You check her out. She definitely looks ready for some action! She takes your hand and slowly walks you back to the bedroom."
    the_person "[the_person.SO_name] and I were just getting started... you came at the perfect time..."
    "[the_person.SO_name]? Why does that sound so familiar?"
    $ the_person.change_to_bedroom()
    "As you walk into the bedroom, you see [the_person.SO_name], the bartender sitting in a chair, completely naked."
    "Holy shit! It's the bartender! He had a front row ticket every time you fucked [the_person.title] at the bar! No wonder he went along with all of it!"
    "He nods to you, but you are shocked at the revelation."
    the_person "Don't worry about him, get over here and fuck me [the_person.mc_title]!"
    $ the_person.draw_person(position = "doggy")
    "You watch as [the_person.possessive_title] crawls on to the bed, pointing her ass back at you. She wiggles it back and forth, enticingly."
    "You walk up behind her and run your hands over her pliant cheeks. [the_person.SO_name]'s chair is at the end of the bed, so he will have an excellent profile view while you fuck his wife."
    "With one hand you start to undo your trousers. With your other hand, you run you fingers along her slit. She is wet and ready for you."
    "Your cock now free, you line yourself up with [the_person.possessive_title]'s pussy. You put her husband out of your mind as you slowly push into her."
    "[the_person.possessive_title] gasps as you begin to slide in and out of her."
    call fuck_person(the_person, start_position = doggy, start_object = make_bed(), private = True, skip_intro = True, skip_condom = True) from _call_camilla_sex_description_CSH040
    $ the_report = _return

    #Finishing dialogue based on sexual performance
    if the_report.get("girl orgasms", 0) > 1:   #She had more than one orgasm
        the_person "Oh my god... I came so many times..."
        "[the_person.possessive_title] collapses onto the bed after your performance. You get up and start to get dressed."
        "You nod at [the_person.SO_name], and he nods back. He goes over to a bedside table and gets out a set of handcuffs."
        "After you fucked her brains out, [the_person.title] lays helpless on the bed as he starts to cuff her hands behind her back."
        "You've finished getting dressed and decide to leave them to it, so you quietly excuse yourself from the bedroom."
    elif the_report.get("girl orgasms", 0) > 0: #She had one orgasm
        the_person "Oh god, I came so hard... That was good [the_person.mc_title]."
        $ the_person.draw_person (position = "missionary")
        "[the_person.possessive_title] rolls over on her back and spreads her legs wide."
        the_person "[the_person.SO_name]... I've been a bad girl..."
        "[the_person.SO_name] gets up from his chair and gets some handcuffs from a bedside table. You get yourself dressed."
        "[the_person.SO_name] begins cuffing [the_person.title]'s hands to the bedpost. You finish getting dressed and quietly excuse yourself from the bedroom."
    else:                           #You left her hanging
        "Surprised you are finished so soon, [the_person.title] gets up and sits at the edge of the bed."
        $ the_person.draw_person( position = "sitting")
        the_person "Thanks for getting me warmed up..."
        "[the_person.SO_name] gets up from his chair and gets some handcuffs from a bedside table. You get yourself dressed."
        the_person "Oh... [the_person.SO_name], I've been a bad girl... what are you gonna do with those handcuffs?"
        "[the_person.SO_name] begins cuffing [the_person.title]'s behind her back. You finish getting dressed and quietly excuse yourself from the bedroom."
    $ clear_scene()
    $ mc.change_location(downtown)
    $ mc.location.show_background()
    "You make your way back home. You can hardly believe your luck, fucking [the_person.title] in her house, in front of her husband, who is also the bartender!"
    $ perk_system.add_stat_perk(Stat_Perk(description = "Fucking Camilla in front of her husband has made you feel more charismatic.", cha_bonus = 1, bonus_is_temp = False), "Camilla Charisma Bonus")
    $ mc.change_location(bedroom)
    $ mc.location.show_background()
    $ the_person.event_triggers_dict["her_place"] = True
    #$ the_person.event_triggers_dict["camilla_progress"] = 5
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
    call fuck_person(the_person, private = True) from _call_casual_sex_mod_camilla_505
    $ the_report = _return
    if the_report.get("girl orgasms", 0) > 1:
        the_person "Oh my god... I came so many times..."
        "[the_person.possessive_title] collapses onto the bed after your performance. You get up and start to get dressed."
        "You nod at [the_person.SO_name], and he nods back. He goes over to a bedside table and gets out a set of handcuffs."
        "After you fucked her brains out, [the_person.title] lays helpless on the bed as he starts to cuff her hands behind her back."
        "You've finished getting dressed and decide to leave them to it, so you quietly excuse yourself from the bedroom."
    elif the_report.get("girl orgasms", 0) > 0:
        the_person "Oh god, I came so hard... That was good [the_person.mc_title]."
        $ the_person.draw_person (position = "missionary")
        "[the_person.possessive_title] rolls over on her back and spreads her legs wide."
        the_person "[the_person.SO_name]... I've been a bad girl..."
        "[the_person.SO_name] gets up from his chair and gets some handcuffs from a bedside table. You get yourself dressed."
        "[the_person.SO_name] begins cuffing [the_person.title]'s hands to the bedpost. You finish getting dressed and quietly excuse yourself from the bedroom."
    else:                           #You left her hanging
        "Surprised you are finished so soon, [the_person.title] gets up and sits at the edge of the bed."
        $ the_person.draw_person( position = "sitting")
        the_person "Thanks for getting me warmed up..."
        "[the_person.SO_name] gets up from his chair and gets some handcuffs from a bedside table. You get yourself dressed."
        the_person "Oh... [the_person.SO_name], I've been a bad girl... what are you gonna do with those handcuffs?"
        "[the_person.SO_name] begins cuffing [the_person.title]'s behind her back. You finish getting dressed and quietly excuse yourself from the bedroom."
    $ clear_scene()
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


# Camilla's love story scenes

label camilla_outfit_help_label(the_person):    #20
    python:
        builder = WardrobeBuilder(the_person)
        outfit_slut_points = __builtin__.min(__builtin__.int(the_person.effective_sluttiness() / 8), 12)
        camilla_outfit_1 = builder.personalize_outfit(builder.build_outfit(None, outfit_slut_points))
        camilla_outfit_2 = builder.personalize_outfit(builder.build_outfit(None, outfit_slut_points))
        camilla_outfit_3 = None
    "You go for a walk around the mall. As you pass by the stall where [the_person.title] is working it, she notices you."
    $ the_person.draw_person()
    the_person "Oh [the_person.mc_title]!"
    mc.name "Hey [the_person.title]."
    the_person "You have awesome timing. I got a couple new outfits from Sak's, and I was hoping to get your opinion on them?"
    mc.name "Oh?"
    the_person "Yeah! I have a date with the hubby soon, and I want to look nice. It's been a while since he's taken me out somewhere."
    "Oof. Obviously you knew she was taken, but this could be a good opportunity to get to know her a little better, so you agree."
    mc.name "Sure, I can help out."
    the_person "Great! I'm about due for a break. Let me just put up a be right back sign and we can head over to the clothing store and I'll use the changing room there."
    $ mc.change_location(clothing_store)
    $ mc.location.show_background()
    "You walk with her to the clothing store and back towards the dressing rooms."
    mc.name "So, a hot date huh? Any idea what you are gonna do?"
    the_person "I have no idea! I just want to make sure I look nice for it!"
    the_person "Alright, give me just one moment and I'll be out!"
    $ clear_scene()
    "[the_person.possessive_title] steps into the dressing room. You wish you could have a look and see what is going on in there, but think better of it in this public setting."
    $ the_person.apply_outfit(camilla_outfit_1, update_taboo = True)
    $ the_person.draw_person(position = "stand2")
    "[the_person.title] steps out of the dressing room."
    the_person "Here! This is the front..."
    $ the_person.draw_person(position = "back_peek")
    the_person "And this is what it looks like from the back..."
    $ mc.change_locked_clarity(10)
    "She pauses for a few seconds to let you look her up and down."
    $ the_person.draw_person(position = "stand2")
    the_person "Alright. So this is the first one! Hang on before you say anything, let me show you the other one I am thinking of..."
    $ clear_scene()
    "[the_person.possessive_title] disappears back into the dressing room... damn you wish you could see her getting undressed..."
    $ the_person.apply_outfit(camilla_outfit_2, update_taboo = True)
    $ the_person.draw_person(position = "stand4")
    "[the_person.title] steps out of the dressing room in her second outfit."
    the_person "Here we go! And of course..."
    $ the_person.draw_person(position = "back_peek")
    "She turns around again, giving you a good look at her back side."
    $ mc.change_locked_clarity(10)
    the_person "The back of this one..."
    $ the_person.draw_person(position = "stand4")
    the_person "What do you think?"
    menu:
        "Suggest the first outfit":
            mc.name "I think your husband would appreciate the first outfit the most."
            "She smiles and nods."
            $ the_person.change_happiness(5)
            $ the_person.next_day_outfit = camilla_outfit_1
            $ the_person.add_outfit(camilla_outfit_1,"full")
            the_person "Thanks! It helps to have a man's opinion on this."

        "Suggest the second outfit":
            mc.name "I think your husband would appreciate the second outfit the most."
            "She smiles and nods."
            $ the_person.change_happiness(5)
            $ the_person.next_day_outfit = camilla_outfit_2
            $ the_person.add_outfit(camilla_outfit_2,"full")
            the_person "Thanks! It helps to have a man's opinion on this."

        "Suggest your own outfit":
            mc.name "They both look good, but I think I have another idea for something you could wear..."
            "[the_person.title] seems surprised, but goes along with it for now."
            the_person "Oh? I suppose I have time I could try on one more outfit... why don't you go pick something out for me while I change?"
            mc.name "Okay."
            $ clear_scene()
            call outfit_master_manager(slut_limit = the_person.sluttiness + 5, show_overwear = False, show_underwear = False) from _call_outfit_master_manager_camilla_hubby_impression_01
            $ camilla_outfit_3 = _return
            #$ the_person.draw_person()

            if camilla_outfit_3 == None:
                "You try a few different combinations, but you can't come up with anything. You head back to the changing room."
                $ the_person.apply_planned_outfit()
                $ the_person.draw_person()
                mc.name "Sorry, I thought I had an idea but I guess I was wrong."
                the_person "That's fine [the_person.mc_title]. I think I'm going to go with the first one."
                $ the_person.change_happiness(5)
                $ the_person.next_day_outfit = camilla_outfit_1
                $ the_person.add_outfit(camilla_outfit_1,"full")
            else:
                "You take the outfit for [the_person.possessive_title] back to the changing room and set it on top of the door."
                the_person "Okay, give me a minute to try it on!"

                $ the_person.apply_outfit(camilla_outfit_3, update_taboo = True)
                $ the_person.draw_person()
                $ the_person.change_stats(happiness = 5, obedience = 5, love = 1)
                the_person "This is... surprisingly fashionable!"
                $ the_person.draw_person(position = "back_peek")
                "[the_person.title] gives you a quick turn to show it off."
                $ mc.change_locked_clarity(10)
                $ the_person.add_outfit(camilla_outfit_3,"full")
                $ the_person.next_day_outfit = camilla_outfit_3
                the_person "What the hell. I'm going to get it. Give me a minute, I'm going to change back..."
                $ clear_scene()
                $ the_person.apply_planned_outfit()
                $ the_person.draw_person()

    the_person "Thank you so much for the help [the_person.mc_title]. This has been really helpful!"
    mc.name "Of course. Always glad to help."
    $ the_person.change_love(1, 40)
    the_person "I'd better get back to my stall. Take care!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.title] walks away, leaving you in the clothing store. You hope that her husband can appreciate her beauty as much as you do!"
    $ the_person.add_unique_on_room_enter_event(camilla_lingerie_help)
    python: #Cleanup time
        del builder
        del outfit_slut_points
        del camilla_outfit_1
        del camilla_outfit_2
        del camilla_outfit_3
    return

label camilla_lingerie_help_label(the_person):  #40
    python:
        builder = WardrobeBuilder(the_person)
        outfit_slut_points = __builtin__.min(__builtin__.int(the_person.effective_sluttiness() / 6), 12)
        camilla_lingerie_1 = builder.personalize_outfit(builder.build_outfit("UnderwearSets", outfit_slut_points))
        camilla_lingerie_2 = builder.personalize_outfit(builder.build_outfit("UnderwearSets", outfit_slut_points))
        #camilla_lingerie_3 = None

    "Walking around the mall, you happen to walk by [the_person.possessive_title]'s stall. You decide to stop in and see how she is doing."
    $ the_person.draw_person()
    mc.name "Hello [the_person.title]. How are you doing?"
    the_person "Oh hey [the_person.mc_title]. I'm doing good. Here to work on your goals again?"
    mc.name "Nah, I just stopped in to say hello and see how you are doing."
    the_person "Ah, thanks. It's always good to see you."
    "You chat with her for a few minutes about general small talk."
    the_person "Say... are you busy right now?"
    mc.name "Not really."
    the_person "I'm due for a lunch break... want to snap a few more umm... you know... pics for me?"
    "Damn. You can't forget taking pics with her in the bar restroom with your dick in her mouth. Surely this opportunity is worth taking too!"
    mc.name "Definitely. Have something in mind?"
    the_person "Well, I have a couple more outfits I kind of wanted to get your opinion on, but they are for a more intimate encounter than last time..."
    mc.name "Wow, sounds great! Lead the way!"
    $ mc.change_location(clothing_store)
    $ mc.location.show_background()
    "You walk with her to the clothing store and back towards the dressing rooms."
    the_person "So, I have a special night planned with the hubby... I was hoping you could give me your opinion on some lingerie sets..."
    the_person "And then snap a couple quick pictures that I can send to him as a tease!"
    mc.name "Alright, I think I'm down for that."
    "When you get to the dressing rooms, [the_person.possessive_title] takes a quick look around to make sure the coast is clear, then quickly drags you into the changing room with her."
    the_person "Shh, just be quiet. It'll be easier if you're in here with me while I try these on."
    $ the_person.strip_outfit(exclude_feet = False)
    $ mc.change_locked_clarity(20)
    "Quietly, [the_person.possessive_title] strips down in front of you. She gives you a sheepish smile when she is naked, before donning her underwear set."
    $ the_person.apply_outfit(camilla_lingerie_1, update_taboo = True)
    $ the_person.draw_person(position = "stand2")
    "[the_person.title] whispers to you."
    the_person "Okay. This is the first set..."
    $ the_person.draw_person(position = "standing_doggy")
    "[the_person.possessive_title] turns around and bends over, give you the opportunity to check out how the set hugs her curves."
    "You enjoy a good long look."
    $ mc.change_locked_clarity(20)
    $ the_person.draw_person(position = "stand2")
    the_person "Alright, one second..."
    $ the_person.strip_outfit(exclude_feet = False)
    $ mc.change_locked_clarity(20)
    "Quietly, [the_person.possessive_title] strips down in front of you again."
    $ the_person.apply_outfit(camilla_lingerie_2, update_taboo = True)
    $ the_person.draw_person(position = "stand4")
    "[the_person.title] whispers to you."
    the_person "Okay. This is the second set."
    $ the_person.draw_person(position = "standing_doggy")
    "[the_person.possessive_title] turns around and bends over again. The way she is showing off her body is really starting to turn you on."
    $ mc.change_locked_clarity(20)
    "You swear you see a little wiggle in her hips as you check her out."
    $ the_person.draw_person(position = "stand4")
    the_person "What do you think? Which set did you like better?"
    menu:
        "The first set":
            the_person "Ah, okay. One second..."
            $ the_person.strip_outfit(exclude_feet = False)
            $ mc.change_locked_clarity(20)
            "Quietly, [the_person.possessive_title] strips down and then changes back into the first outfit."

            $ the_person.apply_outfit(camilla_lingerie_1, update_taboo = True)
            $ the_person.draw_person(position = "stand2")
            $ the_person.add_outfit(camilla_lingerie_1,"full")
        "This set":
            the_person "Ah, I see..."
            $ the_person.add_outfit(camilla_lingerie_2,"full")

    the_person "Okay, can you snap some pics for me?"
    mc.name "Sure."
    "[the_person.title] hands you her phone with her camera app pulled up. She strikes a few poses for you."
    $ the_person.draw_person(position = "stand4")
    "[the_person.possessive_title] strikes a few poses for you. You make sure to snap pics showing off her incredible body as best you can."
    $ the_person.draw_person(position = "standing_doggy")
    if camilla_will_fuck():
        "Bending over, you get an awesome view of [the_person.title]'s ass."
        "For a second you get goosebumps thinking about the first time you bent her over the bathrooms sink at the bar and fucked her proper."
        $ mc.change_locked_clarity(50)
    else:
        "Bending over, you get a great view of [the_person.title]'s undefiled ass."
        "The way things are going, you think it is only a matter of time until you can bend her over and fuck her properly."
        $ mc.change_locked_clarity(30)
    $ the_person.draw_person(position = "sitting")
    "You snap a few more pictures of [the_person.possessive_title] as she sits on the bench, showcasing her long, sexy legs."
    "Suddenly, you are struck by just how picture perfect she really is. Long legs, nice tits, and her tanned skin gives her an exotic appearance."
    mc.name "[the_person.fname]... have you ever thought about shooting some professional pictures?"
    the_person "Umm... you mean like... modeling?"
    mc.name "Not necessarily modeling... but like, boudoir photos? You really do have the body for it."
    $ the_person.change_stats(slut = 1, max_slut = 60, love = 2, max_love = 80)
    the_person "Oh! You mean like... sexy photos?"
    mc.name "Yeah."
    the_person "Wow... I mean, I guess I've always kind of thought about it but... I don't think I really have the body for it?"
    "What the fuck, is she serious?"
    mc.name "I would argue aggressively against that statement. Your body would be perfect for boudoir."
    the_person "I don't know... what would I even do with them?"
    mc.name "You could sell them for advertisement purposes, or even keep them for you and your husband."
    mc.name "You should try it. Worst case scenario, you don't care for it, so you get rid of them and don't try it again."
    the_person "I guess... I could maybe try it sometime? Is that something you could do for me?"
    if mc_business_has_expensive_camera():
        "You think about it. You do have the expensive camera that you got for making ads at your business."
        if alexia == mc.business.company_model: #Alexia is the company model
            "Actually, the photo sessions you have been doing with [alexia.possessive_title] have been going well."
            "Maybe you could have her help you with it? That would probably make it an easier sell to [the_person.title] if a woman was helping."
            mc.name "Actually, at my business I have a nice camera and photographer we use for company ads. She would probably be willing to help if I asked her to."
            "[the_person.possessive_title] thinks about it for a bit, but finally agrees."
            the_person "Okay... I'll do it. Can you set it up for me and let me know when and where?"
            mc.name "Certainly, I'll get back to you about it."
        else:
            "Right now though, you don't really have anyone who you could count on to take the pictures."
            "Maybe in the future you will have something better in line to facilitate this sort of photo shoot."
            mc.name "I don't have the ability right now to do that, but I'll let you know in the future if that is something I can pull off."
            "She looks disappointed, but also relieved."
            the_person "Okay. I appreciate the thought."
    else:
        "Unfortunately, you have no idea how you could facilitate this. After thinking about it for a bit, you decide it isn't in your capabilities right now."
        mc.name "I don't have the ability right now to do that, but I'll let you know in the future if that is something I can pull off."
        "She looks disappointed, but also relieved."
        the_person "Okay. I appreciate the thought."
    $ camilla_alexia_boudoir_intro_setup()
    "You snap a couple more photos. Just when you think you are finishing up, [the_person.title] gets down on her knees and slides over to you."
    $ the_person.draw_person(position = "blowjob")
    "[the_person.possessive_title] grabs your zipper and starts to pull it down. A couple quick motions later, and your cock is out and inches from her face."
    the_person "Hey, keep taking pictures!"
    mc.name "Right!"
    "You snap more pictures as [the_person.title] opens up and slides her warm wet mouth down over the tip of your erection."
    $ mc.change_locked_clarity(50)
    "All the sexy wardrobe changes have you aching for release. You sigh as [the_person.possessive_title]'s mouth starts bobbing up and down."
    call get_fucked(the_person, start_position = blowjob, private = True, skip_intro = True, ignore_taboo = True,  allow_continue = False) from _call_camilla_lingerie_blowjob_01
    if the_person.has_mouth_cum():
        "[the_person.possessive_title] looks up at you. You frame the cum dribbling down the sides of her mouth in a final set of pictures."
        the_person "Mmm, another tasty snack. Glad I got a high protein lunch today!"
    elif the_person.has_face_cum():
        "[the_person.possessive_title] looks up at you. You frame her cum drenched face in a final set of pictures."
        the_person "God, it doesn't get old, does it? Sucking off another man?"
    $ the_person.draw_person (position = "stand2")
    "[the_person.title] stands up. You hand her back her phone."
    the_person "Go ahead and sneak out, I'm going to buy this and send a few messages..."
    mc.name "Sounds good... I'll see you next time."
    $ clear_scene()
    "With a quick wink, you excuse yourself from the changing room and go out into the clothing store."
    "[the_person.title] was so hot in that lingerie. You really hope you get the chance to take more photos of her like that."
    $ mc.business.add_mandatory_crisis(camilla_formal_date)
    python: #Cleanup time
        del builder
        del outfit_slut_points
        del camilla_lingerie_1
        del camilla_lingerie_2
    return

label camilla_formal_date_label():    #60
    $ the_person = camilla
    "As you are finishing up your day, your phone vibrates, and you see you have a message from [the_person.possessive_title]."
    $ mc.start_text_convo(the_person)
    the_person "Hey Señor! Sorry, I know this is last minute... are you busy tonight?"
    mc.name "I'm not now. Want to meet at the bar?"
    the_person "I was actually wondering if you wanted to grab dinner somewhere else tonight."
    "Dinner? That sounds a LOT like a date! You wonder why she suddenly wants to change things up. Could be interesting!"
    mc.name "Sounds great. I know a good place. I'll text you the address, my treat, okay?"
    the_person "Wow, you don't have to do that... but I'm not going to say no! See you there!"
    "You send her the address and set a time. It's a fairly upscale place that you think she will be fairly impressed by."
    $ mc.end_text_convo()
    "You double check and make sure you look okay for the occasion, then head over to the restaurant."
    $ mc.change_location(fancy_restaurant)
    $ mc.location.show_background()
    "When you arrive, you check in at the front counter. You wait a few minutes, but your date soon arrives."

    $ the_person.planned_outfit = the_person.wardrobe.get_outfit_with_name("Camilla Summer Dress") or the_person.get_random_appropriate_outfit(guarantee_output = True)
    $ the_person.apply_outfit(the_person.planned_outfit)
    $ the_person.draw_person()
    the_person "Buenas noches señor!"
    mc.name "Ah. [the_person.title], good to see you. You look great!"
    the_person "Gracias! I can't wait to try this place. I knew it was here, but despite living in this town for a decade, I've never been inside."
    mc.name "Yes, and I think the change of scenery will do us some good. The bar is nice and all but this is certainly a pleasant alternative."
    the_person "Yeah I suppose so."
    "You make some small talk with [the_person.possessive_title] until you are shown to your table."
    $ the_person.draw_person(position = "sitting")
    "The waiter seats you both and turns to you."
    "WAITER" "Can I get your started with anything? Our house red wine is delightful for a beautiful young couple such as yourselves."
    the_person "Ha!... ahhh..."
    "[the_person.title] lets out a snort. For a second, the waiter looks at you in distress, thinking he's embarrassed you by assuming you were a couple, but you just smile."
    mc.name "That sounds great. Start with two glasses?"
    "WAITER" "Yes sir. I'll have those right out."
    "As the waiter walks away, [the_person.possessive_title] looks at you and laughs."
    the_person "A young couple. That's the funniest thing I've heard in a while!"
    if camilla_will_fuck():
        mc.name "Is it funny though? We do other things that couples often do..."
    elif camilla_will_take_pics():
        mc.name "I mean, we've been intimate. Is it really that far off?"
    else:
        mc.name "I mean, I helped you shop for lingerie. Is it REALLY that far off?"
    the_person "I suppose that is a fair point."
    mc.name "I know it was for the benefit if your husband... but still."
    $ the_person.draw_person(position = "sitting", emotion = "angry")
    the_person "Ugh, can we PLEASE not bring him up tonight?"
    "Yikes... has something happened between them? Usually the time you spend with [the_person.title] is for mostly his benefit..."
    "The look on her face tells you that you should probably leave it alone though."
    mc.name "I'm fine with that. Let's talk more about *us* then."
    $ the_person.draw_person(position = "sitting", emotion = "happy")
    mc.name "I suppose I'll go first... What are you ordering?"
    the_person "I have no idea... the menu all looks so good. I was thinking maybe the salmon."
    mc.name "That does sound good..."
    the_person "Yeah. I had a friend tell me once it's a good aphrodisiac. Might be good for when it's time to get out of here."
    "The sultry tone in [the_person.possessive_title]'s voice makes it clear that she is hoping for there to be a part two to this date."
    "The waiter brings out the wine and takes your orders. Before long you've drank two glasses each. The waiter returns and sees your empty glasses."
    "WAITER" "Sir, you and your friend here seem to be enjoying the wine tonight. Might I bring a full bottle for you?"
    mc.name "That sounds great."
    "Soon the food and the wine arrive. You dig in to a plate of pesto shrimp linguini and [the_person.title] eats her salmon."
    "When you finish eating, you've both had several glasses of wine. [the_person.possessive_title] looks at you seriously."
    the_person "So, you are probably wondering why I suddenly want to go out for dinner with you."
    mc.name "Yeah I'm definitely wondering..."
    "[the_person.title] takes a long draught of wine and then continues."
    the_person "Well, at the bar a few nights ago, I got approached by a woman. She said hello, knew my name. Knew a lot about me actually."
    the_person "She explained that she was so happy that I was FINALLY coming around to the hotwife lifestyle."
    the_person "I... I asked how she knew about it? And she said... she said that her and her husband and... and my husband... had been fucking around too."
    the_person "Of course I just... you know... played it off cool. But I was so blindsided by it! I asked her... you know... how long had they been at it."
    the_person "And, well, they've been fucking around for a LOT longer than we have..."
    the_person "But that hey! It's okay right? We're all in the lifestyle together now right?"
    the_person "She pointed out her husband. Asked if I was interested. I said maybe, but honestly I just got sick to my stomach."
    mc.name "[the_person.fname]... I'm sorry..."
    $ the_person.change_stats(happiness = -5, love = 2, max_love = 80)
    the_person "It's ok. You didn't have anything to do with it. I just... I just don't understand, why he kept it all a secret from me... you know?"
    "[the_person.title] turns away for a second and wipes her eyes."
    mc.name "What... what are you going to do?"
    the_person "I have no idea, honestly. These last few weeks have been so crazy! I don't know if I even want this lifestyle."
    the_person "I honestly was just thinking that... maybe tonight we could go back to your place?"
    the_person "I don't want to go home tonight. Just let me come over, and tomorrow, or the next day, or sometime soon, I can really just think about it and figure it out."
    mc.name "Okay. Let's get out of here."
    $ mc.business.change_funds(-200)
    "You quickly grab the check, putting the dinner on the company card. A short walk later, you are walking into your house with [the_person.possessive_title]."
    $ mc.change_location(bedroom)
    $ mc.location.show_background()
    #TODO if MC has fixed up bedroom camilla is impressed, if not she says something of colour.
    $ the_person.draw_person()
    the_person "Wow... I've not been in a man's bedroom in... a long time."
    mc.name "You want to just... get some sleep? I'm sure it's been a long day."
    $ the_person.change_love(2, 90)
    the_person "That is very kind of you... but that isn't why I'm here."
    "You step close to [the_person.title] and pull her close to you."
    $ the_person.draw_person(position = "kissing")
    $ the_person.change_arousal(10)
    "You lips meet with an immediate spark. There is something different about her this time."
    "Before when you would kiss, she was a bit reserved, holding back a piece of herself."
    "This time though, she isn't kissing you out of a duty to her husband. She's doing it because she WANTS to."
    "Your hands drop to her ass. She moans into your mouth as you make out."
    $ the_person.change_arousal(15)
    the_person "Señor! I'm ready... let's do this!"
    $ the_person.draw_person()
    "With a shove, she pushes you onto your back on your bed. She stands in front of you as she strips down."
    $ the_person.strip_outfit()
    $ mc.change_locked_clarity(50)
    "[the_person.possessive_title] stands in front of you, completely naked, ready for a full night of fun. She slowly climbs on top of you."
    $ the_person.draw_person(position = "cowgirl")
    the_person "Like what you see, señor?"
    mc.name "Fuck yes. You are so sexy..."
    the_person "Mmm... I believe you... but I want to see proof..."
    "[the_person.title] grabs your pants and you lift your ass up a bit as she slides them off you."
    "She grabs your mostly erect cock and gives it a couple strokes."
    the_person "Ahh... not bad... but I think we can get it a little harder first..."
    "[the_person.possessive_title] opens her mouth and runs her tongue along the length of your cock."

    python: #Creation of custom sex path for this scene.
        first_node = dom_sex_path_node(cowgirl_blowjob, completion_requirement = dom_requirement_mc_aroused)    #Blowjob to arousal
        final_node = dom_sex_path_node(SB_reverse_cowgirl, completion_requirement = dom_requirement_creampie)   #Finish inside her
        sex_path = [first_node, final_node]
    call get_fucked(the_person, the_goal = "vaginal creampie", sex_path = sex_path, skip_intro = True, allow_continue = False, start_object = make_bed()) from _camilla_sleepover_fuck_01
    $ the_report = _return
    if the_report.get("girl orgasms", 0) > 0:
        the_person "Oh my god... that was amazing. You ALWAYS get me off... its incredible..."
    if the_report.get("guy orgasms", 0) > 0:
        if the_person.has_ass_cum():
            "[the_person.possessive_title] looks back at you. Her ass is plastered with your sticky seed."
            "For once, you can just lie back and enjoy it, without worrying about snapping pictures for her husband."
            "You have to admit, having her all to yourself feels great."
        elif the_person.has_creampie_cum():       #We assume we finished inside her#
            "[the_person.possessive_title]'s pussy is dripping cum from your creampie."
            "It's so hot, dumping your load inside a married woman."
            if camilla_is_fertile():
                "Especially since you cured her infertility."
                if the_person.knows_pregnant():
                    "You've already knocked her up, and now every load is another claim you are staking on her body."
                else:
                    "Every load you dump inside her could be the one that knocks her up."
            else:
                "But it is a little worrying to be doing so... is she even on birth control?"
                mc.name "Is it okay? To be having risky sex like this?"
                the_person "Oh yeah. I don't know if I've ever talked to you about this but... I'm actually infertile..."
                the_person "A hormonal issue going back since before puberty."
                mc.name "Ah, I see."
    python:
        del sex_path
        del first_node
        del final_node

    "[the_person.title] lays down in your bed next to you, on her side. You cuddle up behind her."
    $ the_person.draw_person(position = "walking_away")
    "Her body is flushed and hot, but her beautiful skin feels amazing against yours."
    "You put your arm around her. She takes your hand and puts it on her breast. You give it a good squeeze."
    the_person "Goodnight [the_person.mc_title]..."
    mc.name "Night..."

    python: # she stays the night so she will have to wear the same outfit again the next day
        the_person.next_day_outfit = the_person.planned_outfit

    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_camilla_spend_the_night
    python: # init morning
        the_person.apply_outfit(special_fetish_nude_outfit)
        the_person.change_energy(200)
        mc.location.lighting_conditions = dark_lighting

    $ the_person.draw_person(position = "walking_away")
    "In the middle of the night, you stir a bit. The warm body next to you continues sleeping."
    "It takes you a few moments to remember... [the_person.possessive_title] invited herself over last night, and she's naked, right next to you!"
    "Your hand is cupping her chest. You give her hefty tits a squeeze, enjoying their heat and weight."
    $ mc.change_locked_clarity(50)
    $ the_person.change_arousal(10)
    the_person "Mmm..."
    "God, thinking about the latina goddess next to you in bed is getting you hard. She's still sleeping... but surely she wouldn't mind if you slipped inside her for a bit?"
    "You are both already naked... maybe you could just slide it between her legs for a bit, up against her pussy... that could be nice..."
    "You carefully move your hips back and down, then slowly push forward, your cock sliding in between her thighs..."
    the_person "Ahhh... [the_person.SO_name]..."
    $ mc.change_locked_clarity(50)
    $ the_person.change_arousal(15)
    "[the_person.title] is so out of it, she thinks you are her husband!"
    "As you slide up against her, you can feel a bit of heat and humidity escaping her crotch. She's definitely getting turned on too."
    "You let go of her tits and reach down between her legs. You use your hand to push your cock against her slit as much as possible and then start to thrust a bit."
    $ mc.change_locked_clarity(50)
    $ the_person.change_arousal(25) #60
    the_person "[the_person.SO_name], que me cojan..."
    "You have no idea what she is saying, but she is definitely getting into it. You decide to go for it."
    "You take a couple more strokes, then use your hand to put your cock up. You slide into her wet cunt quite easily."
    $ mc.change_locked_clarity(50)
    $ the_person.change_arousal(25) #85
    the_person "Que me jodan más fuerte..."
    "God, fucking married women is amazing. She is pushing her ass back against you now. You aren't sure if she's woken up or not but you don't really care."
    "You grope her tits roughly and start to really pound her. She is moaning loudly."
    $ mc.change_locked_clarity(50)
    $ the_person.change_arousal(25) #110
    the_person "Papi! punto de correrse!"
    "Did she just call you daddy? Either way, the urgency in her voice makes it clear she is finishing."
    "[the_person.possessive_title] shoves her ass back against you as she cums. Her helpless body quivers in delight. Her moans drive you even harder."
    $ the_person.have_orgasm()
    "The quivering pussy enveloping your cock is too much. You are going to cum!"
    "You decide to keep playing the part. You shove your erection in deep and let yourself go."
    the_person "Dame esa leche!"
    $ the_person.cum_in_vagina()
    $ the_person.draw_person(position = "walking_away")
    $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_person)
    "You explode inside of [the_person.title]. You flood her cunt with wave after wave of cum. She moans and gasps."
    "When you finish, you collapse back in bed beside her. You put your arm around her, and feel her take your hand and move it to her breast again."
    "So... she definitely woke up at some point of that..."
    "You drift off to sleep again."
    $ mc.location.lighting_conditions = standard_outdoor_lighting
    $ the_person.apply_planned_outfit()
    $ the_person.draw_person(position = "back_peek")
    "You slowly wake up. When you stir, you see [the_person.possessive_title] looking at herself in your mirror on the wall, doing some makeup."
    "She hears you stir and turns her head to look at you."
    the_person "Good morning, señor..."
    mc.name "Good morning."
    the_person "I need to run some errands... Sorry, but I need to go."
    "You stand up and walk over to her. She turns as your approach her and you embrace."
    $ the_person.draw_person(position = "kissing")
    the_person "Thank you for last night... it was magical."
    mc.name "It was. Can we do it again soon?"
    "[the_person.title] falters for a moment."
    the_person "I'm not sure... Things are really confusing right now."
    $ the_person.draw_person()
    "[the_person.possessive_title] slowly pulls away from you."
    the_person "I need to go. Goodbye."
    mc.name "Bye."
    $ clear_scene()
    "[the_person.title] leaves your room. It was so hot, sleeping with such a sexy married woman."
    "It is nagging at you a little bit though. She's married to someone else. Are you really okay with this?"
    "You feel some pangs of jealousy. Maybe you could make her yours? Convincing her to leave her husband seems like a tall task."
    "Is that really what you want? To wreck someone's marriage? The guy doesn't seem that great though. Maybe you would be doing her a favor."
    "Either way, you can't help but feel like the time is coming soon that you are going to have to decide what you really want from your relationship with [the_person.title]."
    $ the_person.add_unique_on_room_enter_event(camilla_gives_anal_virginity)
    return

label camilla_gives_anal_virginity_label(the_person): #80
    "In this scene, camilla gives MC her anal virginity."
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

    def camilla_will_fuck():
        return camilla.event_triggers_dict.get("will_fuck", False)

    def camilla_can_go_to_her_place():
        return camilla.event_triggers_dict.get("her_place", False)

    def camilla_outfit_help_complete():
        return camilla.event_triggers_dict.get("outfit_help", False)

    def camilla_lingerie_help_complete():
        return camilla.event_triggers_dict.get("lingerie_help", False)

    def camilla_formal_date_complete():
        return camilla.event_triggers_dict.get("formal_date", False)

    def camilla_has_lost_anal_virginity():
        return camilla.event_triggers_dict.get("lost_anal_virginity", False)

    def mc_dancing_skill(): #Wrapper for measuring MC's progress learning to salsa dance.
        return mc.charisma + __builtin__.round((mc.max_energy - 100) / 20)

    def camilla_is_fertile():   #Just make this a function name. Can come back and make the method once we decide triggers for making her fertile.
        return False
