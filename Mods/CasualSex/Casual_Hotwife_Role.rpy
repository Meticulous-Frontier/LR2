# ----Hotwife----
#   Married but in an open relationship.
#   Tends to hang out at the Sex Store(bar?)
#   First event: asks for you to take pictures of her blowing you to send to her husband
#   Second event: takes pictures while fucking
#   Third event: sex while husband is watching
#   Event Requirements: Advances require increasing sluttiness and charisma. Final event requires vaginal skill
#   Girl Requirements: age... 25+? Personality, not introverted?
#   Other notes: Can "buy her a drink", giving you the option to slip a serum into her drink. Loves cheating on men
#
#   Event States:
#   0 - Before first encounter
#   1 - Introduced to her
#   2 - She has blown you with pictures
#   3 - She has fucked you. (Get phone number and casual sex access)
#   4 - She has invited you over.
#   5 - You can fuck her in front of her husband (visit her at home access)
#
#   Required labels:
#     - Grab a drink - First action available.
#     - Sneak into the Bathroom - Sneak to the bathroom for blowjob
#     - Dance with her, then sex in the Bathroom
#     - She invites you over that night
#     - Sex at her place

init -2 python:
    def casual_hotwife_get_a_drink_requirement(person):  #For now this should always return true. May be other conditions not to in the future#
        if person.event_triggers_dict.get("hotwife_blowjob_text_enable", 0) == 1:
            return False
        if mc.location != downtown_bar:
            return "Not in Bar"
        return True

    def casual_hotwife_bathroom_blowjob_requirement(person):
        if person.event_triggers_dict.get("hotwife_progress", 0) < 1:
            return False
        if person.event_triggers_dict.get("hotwife_blowjob_text_enable", 0) == 1:
            return False
        if mc.location != downtown_bar:
            return "Not in Bar"
        elif mc.charisma < 4:
            return "Requires higher Charisma"
        elif person.effective_sluttiness() < 25:
            return "Requires higher sluttiness"
        elif person.event_triggers_dict.get("hotwife_blowjob_enable", 0) == 1:
            return True
        else:
            return "Grab a drink first"
        return False

    def casual_hotwife_blowjob_text_requirement(person):
        if person.event_triggers_dict.get("hotwife_blowjob_text_enable", 0) == 1:
            if day <= person.event_triggers_dict.get("hotwife_blowjob_ask_pictures", 0):
                return "Wait a few days"
            if time_of_day < 3:
                return True
            else:
                return "Ask her another time"
        return False

    def casual_hotwife_dancing_sex_requirement(person):
        if person.event_triggers_dict.get("hotwife_blowjob_text_enable", 0) == 1:
            return False
        if person.event_triggers_dict.get("hotwife_progress", 0) < 2:
            return False

        if mc.location != downtown_bar:
            return "Not in Bar"
        elif mc.charisma < 5:
            return "Requires higher Charisma"
        elif person.effective_sluttiness() < 40:
            return "Requires higher sluttiness"
        elif person.event_triggers_dict.get("hotwife_dancing_enable", 0) == 1:
            return True
        else:
            return "Grab a drink first"
        return False

    def casual_hotwife_sex_invite_requirement(person):
        if person.event_triggers_dict.get("hotwife_progress", 0) < 3:
            return False
        elif mc.charisma < 6:
            return "Requires higher Charisma"
        elif person.effective_sluttiness() < 50:
            return "Requires higher sluttiness"
        elif person.event_triggers_dict.get("hotwife_progress", 0) == 4:
            return "Already invited you over!"
        elif person.event_triggers_dict.get("hotwife_progress", 0) == 3:
            return True
        return False

    def casual_hotwife_her_place_requirement():
        if mc_asleep():
            return True
        return False

    def casual_hotwife_home_sex_requirement(person):
        if person.event_triggers_dict.get("hotwife_progress", 0) == 5:
            if mc.location == person.home:
                return True
            else:
                return "Only at her place"
        return False

    def casual_hotwife_ghost_requirement():
        if renpy.random.randint(0,100) < 20:
            return True
        return False

    def add_hotwife_ghost_action(person):
        remove_mandatory_crisis_list_action("casual_hotwife_ghost_label")
        casual_hotwife_ghost = Action("Casual hotwife Ghosts you", casual_hotwife_ghost_requirement, "casual_hotwife_ghost_label", args = person)
        mc.business.add_mandatory_crisis(casual_hotwife_ghost)
        return

    def get_hotwife_lingerie_set_white():
        outfit = Outfit("Lingerie Set Classic White")
        outfit.add_upper(teddy.get_copy(),colour_white)
        outfit.add_feet(garter_with_fishnets.get_copy(), colour_white)
        outfit.add_feet(high_heels.get_copy(), colour_white)
        return outfit

    def get_hotwife_lingerie_set_pink():
        outfit = Outfit("Pink Lingerie")
        outfit.add_upper(teddy.get_copy(),colour_pink)
        outfit.add_feet(garter_with_fishnets.get_copy(), colour_pink)
        outfit.add_feet(high_heels.get_copy(), colour_pink)
        return outfit

#*************Create Casual Hotwife Role***********#
init -1 python:
    casual_hotwife_get_a_drink = Action("Get a drink with her {image=gui/heart/Time_Advance.png}", casual_hotwife_get_a_drink_requirement, "casual_hotwife_get_a_drink_label",
        menu_tooltip = "Alcohol loosens lips!")
    casual_hotwife_bathroom_blowjob = Action("Sneak into the bathroom {image=gui/heart/Time_Advance.png}", casual_hotwife_bathroom_blowjob_requirement, "casual_hotwife_bathroom_blowjob_label",
        menu_tooltip = "She wants pics to send her husband...")
    casual_hotwife_blowjob_text = Action("Ask her about the blowjob pictures... {image=gui/heart/Time_Advance.png}", casual_hotwife_blowjob_text_requirement, "casual_hotwife_blowjob_text_label",
        menu_tooltip = "Make sure it went okay.")
    casual_hotwife_dancing_sex = Action("Dirty dancing {image=gui/heart/Time_Advance.png}", casual_hotwife_dancing_sex_requirement, "casual_hotwife_dancing_sex_label",
        menu_tooltip = "She wants to dance dirty with you!")
    casual_hotwife_sex_invite = Action("Your place or mine?", casual_hotwife_sex_invite_requirement, "casual_hotwife_sex_invite_label",
        menu_tooltip = "Ask if she wants to get out of here.")
    casual_hotwife_home_sex = Action("Put on a show {image=gui/heart/Time_Advance.png}", casual_hotwife_home_sex_requirement, "casual_hotwife_home_sex_label",
        menu_tooltip = "Let hubby watch.")
    casual_hotwife_role = Role(role_name ="Hot Wife", actions =[casual_hotwife_get_a_drink, casual_hotwife_bathroom_blowjob, casual_hotwife_blowjob_text, casual_hotwife_dancing_sex, casual_hotwife_sex_invite, casual_hotwife_home_sex], hidden = True)

#*************Mandatory Crisis******************#

init 1 python:
    def add_hotwife_sex_at_her_place_action(person):
        casual_hotwife_her_place.args = [person]    # set the current person as action argument
        mc.business.add_mandatory_crisis(casual_hotwife_her_place) # TODO Find out if this breaks if two girls hit this stage a the same point in gameplay
        return

    casual_hotwife_her_place = Action("Her Place", casual_hotwife_her_place_requirement, "casual_hotwife_her_place_label")


#************* Hotwife Action Labels *********#


#CSH00
label casual_hotwife_get_a_drink_label(the_person):
    mc.name "Care to get a drink, [the_person.title]?"
    if the_person.event_triggers_dict.get("hotwife_progress", 0) < 1:  #Do a charisma check to see if we continue...
        "[the_person.title] looks you over."
        if mc.charisma < 3:  #Fail charisma check
            "*Charisma Check Failed*"
            the_person "Hey, you're cute, but not really the kind of guy I'm looking for. Maybe another time."
            "You nod."
            mc.name "Another time then."
            "You should try raising your Charisma before you talk to her again!"
        else:               #Charisma Check Passed
            the_person "Hey... I'd love to grab a drink! Not often I find guys as cute as you!"
    else:
        the_person "Hey [the_person.mc_title]! A drink sounds great!"
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
    if the_person.event_triggers_dict.get("hotwife_progress", 0) < 1:  #This is your first time grabbing a drink Together
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
        $ the_person.event_triggers_dict["hotwife_progress"] = 1
        mc.name "Take care, I'm sure I'll see you here again sometime!"

    #***Event State 1 ####
    elif the_person.event_triggers_dict.get("hotwife_progress", 0) == 1:  #You are acquainted, but not yet done anything sexual
        mc.name "So, any luck going squirrel hunting?"
        if the_person.effective_sluttiness() > 25:
            "[the_person.possessive_title] laughs."
            the_person "No, not yet. I have a feeling though, the right opportunity may come a long soon..."
            "She lowers her voice a bit."
            the_person "To catch a squirrel, and take his nut... so to speak..."
            "Damn! Maybe she is finally ready to start the hotwife lifestyle."
            the_person "You wouldn't happen to know any squirrels would you?"
            mc.name "Oh, I think I know one... I bet he'd be more than happy to share his nuts with you..."
            "This analogy is starting to get a little weird though."
            mc.name "I bet your husband would be excited if you did manage to catch one."
            "[the_person.title] stutters for a second, but quickly smiles and regains her composure."
            the_person "Yeah, he keeps saying he will. I think its probably about time I put his eagerness to the test."
            if the_person.event_triggers_dict.get("hotwife_blowjob_enable", 0) == 1:
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
                $ the_person.event_triggers_dict["hotwife_blowjob_enable"] = 1
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
    elif the_person.event_triggers_dict.get("hotwife_progress", 0) == 2:  #She has blown you
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
            $ the_person.event_triggers_dict["hotwife_dancing_enable"] = 1
            mc.name "Indeed, that sounds like fun! I'll try to look for you next time I'm around."

    elif the_person.event_triggers_dict.get("hotwife_progress", 0) == 3:  #She's fucked you
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

    elif the_person.event_triggers_dict.get("hotwife_progress", 0) == 4:  #She's invited you over
        "You chat with [the_person.title] for a while, but you can definitely feel some tension in the air about your arrangement for tonight."
        mc.name "So... tonight at your place? I'll see you there?"
        the_person "Sounds good. See you then, [the_person.mc_title]."
    elif the_person.event_triggers_dict.get("hotwife_progress", 0) == 5:  #You've fucked in front of her husband
        the_person "Thanks for the drink, [the_person.mc_title]. This whole adventure has really supercharged my sex life, its nice to have a break from fucking and just enjoy a stiff drink."
        mc.name "Yeah, so is [the_person.SO_name] still enjoying your new lifestyle?"
        the_person "Oh god, we both are. I've started fucking around with a couple other guys too. Last time I came home, he tied me up and umm... reclaimed me in every hole he could fit it in..."
        mc.name "Damn! That sounds hot!"
        the_person "Yeah! I came so many times... you didn't forget my address did you? You should stop by sometime and we could fuck around again."
        mc.name "Don't worry, I haven't forgotten."
        "You and [the_person.title] finish your drinks and then you say goodbye."
    else:
        "DEBUG: How did you get here?"

    call advance_time from _call_advance_casual_hotwife_drink
    return

#CSH10
label casual_hotwife_bathroom_blowjob_label(the_person):
    if the_person.event_triggers_dict.get("hotwife_progress", 0) == 1: #This is our first time doing this
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
        "She starts to take you into her mouth. You snap a few more pictures of this beautiful hotwife, on her knees servicing you."
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
        $ the_person.event_triggers_dict["hotwife_blowjob_text_enable"] = 1
        $ the_person.event_triggers_dict["hotwife_progress"] = 2
        $ the_person.event_triggers_dict["hotwife_blowjob_ask_pictures"] = day + 1
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
        call advance_time from _call_advance_casual_hotwife_bathroom_blowjob
    return

label casual_hotwife_blowjob_text_label(the_person):
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
    $ the_person.event_triggers_dict["hotwife_blowjob_text_enable"] = 0
    call advance_time from _call_advance_casual_hotwife_sex_discussion
    return

#CSH20
label casual_hotwife_dancing_sex_label(the_person):
    if the_person.event_triggers_dict.get("hotwife_progress", 0) == 2:   #This is our first time doing this
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
        call fuck_person(the_person, start_position = SB_doggy_standing, start_object = make_counter(), skip_intro = True, asked_for_condom = True) from _call_sex_description_CSH020
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
        $ the_person.event_triggers_dict["hotwife_progress"] = 3
        "She takes her phone from you and starts going through the pictures you took."
        the_person "You'd better get going, [the_person.mc_title]. I'm going to send these to my husband..."

        $ the_person.event_triggers_dict["booty_call"] = True # unlock casual encounters
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
    call advance_time from _call_advance_casual_hotwife_dancing
    return

#CSH30
label casual_hotwife_sex_invite_label(the_person):
    mc.name "Hey so... I'm not doing anything later..."
    "You can see a smile start to form on [the_person.title]'s face."
    the_person "You want to come over tonight?"
    mc.name "That would be great."
    "[the_person.possessive_title] gives you her address."
    the_person "Come over tonight, around 10pm. You won't regret it! Is there anything else you want to do now?"
    $ add_hotwife_sex_at_her_place_action(the_person)
    $ the_person.learn_home()
    $ the_person.event_triggers_dict["hotwife_progress"] = 4

    #call advance_time from _call_advance_casual_hotwife_sex_invite
    return

#CSH40
label casual_hotwife_her_place_label(the_person):
    "You head over to [the_person.title]'s place. You can't believe you're gonna fuck her in front of her husband!"
    "You ring the doorbell. Soon [the_person.title] answers the door."

    $ the_person.change_to_hallway()
    $ the_person.apply_outfit(get_hotwife_lingerie_set_white(), update_taboo = True)
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
    call fuck_person(the_person, start_position = doggy, start_object = make_bed(), skip_intro = True, asked_for_condom = True) from _call_sex_description_CSH040
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
    $ perk_system.add_stat_perk(Stat_Perk(description = "Fucking a hotwife in front of her husband has made you feel more charismatic.", cha_bonus = 1, bonus_is_temp = False), "Hotwife Charisma Bonus")
    $ mc.change_location(bedroom)
    $ mc.location.show_background()
    $ the_person.event_triggers_dict["hotwife_progress"] = 5
    return

#CSH50
label casual_hotwife_home_sex_label(the_person):
    $ mc.change_location(the_person.home)
    $ mc.location.show_background()
    mc.name "So, want to have some fun tonight?"
    the_person "Sounds great! Just give me a minute to get ready..."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] walks into her bedroom and closes the door. You hang out in her living room for a few minutes while she gets ready."
    $ the_person.apply_outfit(get_hotwife_lingerie_set_pink(), update_taboo = True)
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

    call advance_time from _call_advance_casual_hotwife_home_sex
    return

label casual_hotwife_ghost_label(the_person):
    "You get a message on your phone. Looks like it is from [the_person.possessive_title]."
    the_person "Hey, I'm really sorry to have to do this, but we can't hookup anymore."
    the_person "I'm dedicated to my husband, but I find myself thinking about you constantly."
    the_person "This is beginning to turn into an emotional affair, and I can't do it anymore. I'm sorry."
    "Damn. Sounds like you pushed things with her a little too far..."
    $ the_person.remove_person_from_game()
    $ casual_sex_create_hotwife() #Create a new hotwife so MC can try again if they choose.
    return

#************* Personality****************#
#Override some of her personality functions so that her conversation options makes sense.

init 1301 python:              #Because Vren Init personality functionns at 1300



    def hotwife_titles(person):
        valid_titles = []
        valid_titles.append(person.name)
        if person.effective_sluttiness() > 40:
            valid_titles.append("Slutwife")
            valid_titles.append("Cuckold Wife")
        return valid_titles

    def hotwife_possessive_titles(person):
        valid_possessive_titles = [person.title]

        if person.effective_sluttiness() > 60:
            valid_possessive_titles.append("The Slutwife")
            valid_possessive_titles.append("Your Swinging Slut")

        if person.effective_sluttiness() > 100:
            valid_possessive_titles.append("The Bar Cumdump")
        return valid_possessive_titles
    def hotwife_player_titles(person):
        return mc.name

    hotwife_personality = Personality("hotwife", default_prefix = "wild",
    common_likes = ["skirts", "dresses", "the weekend", "the colour red", "makeup", "flirting", "high heels"],
    common_sexy_likes = ["casual sex", "doggy style sex", "giving blowjobs", "vaginal sex", "public sex", "lingerie", "skimpy outfits", "being submissive", "drinking cum", "cheating on men"],
    common_dislikes = ["polyamory", "pants", "working", "the colour yellow", "conservative outfits", "sports"],
    common_sexy_dislikes = ["taking control", "giving handjobs", "not wearing anything"],
    titles_function = hotwife_titles, possessive_titles_function = hotwife_possessive_titles, player_titles_function = hotwife_player_titles)


#************* Personality labels***************#


label hotwife_greetings(the_person):
    if mc.location == downtown_bar:
        if the_person.love > 50:  #She loves you too much and is going to or already has called things off
            the_person "Oh... hello, [the_person.mc_title]."
            $ add_hotwife_ghost_action(the_person)
            return
        if the_person.event_triggers_dict.get("hotwife_progress", 0) >= 2:
            the_person "Hey there [the_person.mc_title]."
            the_person "You want to umm, you know, meet me in the back? I'm sure that's why you're here..."
        else:
            the_person "Hey there!"

    elif the_person.effective_sluttiness() > 60:
        if the_person.obedience > 130:
            the_person "Hello, [the_person.mc_title], it's good to see you."
        else:
            the_person "Hey there handsome, feeling good?"
    else:
        if the_person.obedience > 130:
            the_person "Hello, [the_person.mc_title]."
        else:
            the_person "Hey there!"
    return

label hotwife_sex_responses(the_person):
    if the_person.effective_sluttiness() > 50:
        if the_person.obedience > 130:
            the_person "Oh my, keep doing that please!"
        else:
            the_person "Fuck it feels good when you do that. Keep going!"
    else:
        "[the_person.title] closes her eyes and moans quietly to herself."
    return

label hotwife_climax_responses_foreplay(the_person):
    if the_person.effective_sluttiness() > 50:
        the_person "Oh fuck yes, I'm going to cum! I'm cumming!"
    else:
        the_person "Oh fuck, you're going to make me cum! Fuck!"
        "She goes silent, then lets out a shuddering moan."
    return

label hotwife_climax_responses_oral(the_person):
    if the_person.effective_sluttiness() > 70:
        the_person "Fuck yes, I'm going to cum! Make me cum!"
    else:
        the_person "Oh my god, you're good at that! I'm going to... I'm going to cum!"
    return

label hotwife_climax_responses_vaginal(the_person):
    if the_person.effective_sluttiness() > 70:
        the_person "I'm going to cum! Ah! Make me cum [the_person.mc_title], I want to cum so badly! Ah!"
        "She closes her eyes and squeals with pleasure."
    else:
        the_person "Ah! I'm cumming! Oh fuck! Ah!"
    the_person "Fuck I hope daddy does this to me again later!"
    return

label hotwife_climax_responses_anal(the_person):
    if the_person.effective_sluttiness() > 70:
        the_person "Oh fuck, your cock feels so huge in my ass! It's going to make me cum!"
        the_person "Ah! Mmhmmm!"
    else:
        the_person "Oh fucking shit, I think you're going to make me..."
        "She barely finishes her sentence before her body is wracked with pleasure."
        the_person "Cum!"
    return

label hotwife_clothing_accept(the_person):
    if the_person.obedience > 130:
        the_person "It's for me? Thank you [the_person.mc_title], I'll add it to my wardrobe."
    else:
        the_person "Thanks [the_person.mc_title]! I wonder if daddy would like to see me in this too."
    return

#label hotwife_clothing_reject(the_person):
#    if the_person.obedience > 130:
#        the_person "Is that really for me [the_person.mc_title]? I want to... but I don't think I could wear that without getting in some sort of trouble."
#    else:
#        if the_person.effective_sluttiness() > 60:
#            the_person "Wow. I'm usually up for anything but I think that's going too far."
#        else:
#            the_person "Wow. It's a little... skimpy. I don't think I could wear that."
#    return

# label hotwife_clothing_review(the_person):
#     if mc.location == downtown_bar:
#         if the_person.effective_sluttiness() > 40:
#             the_person "I love when you look at me like that, but I don't think the downtown_bar staff would appreciate it as much. I'd better clean up a bit."
#         else:
#             the_person "I'd better clean up some before I go to leave the downtown_bar..."
#     elif the_person.obedience > 130:
#         the_person "I'm sorry [the_person.mc_title], you shouldn't have to see me like this. I'll go and get cleaned up so I'm presentable again."
#     else:
#         if the_person.effective_sluttiness() > 40:
#             the_person "Whew, I think we messed up my clothes a bit. Just give me a quick second to get dressed into something more decent."
#         else:
#             the_person "My clothes are a mess! I'll be back in a moment, I'm going to go get cleaned up."
#     return

#label hotwife_strip_reject(the_person, the_clothing, strip_type = "Full"):
#    if the_person.obedience > 130:
#        the_person "I'm sorry, but can we leave that where it is for now?"
#    elif the_person.obedience < 70:
#        the_person "Slow down there, I'll decide when that comes off."
#    else:
#        the_person "I think that should stay where it is for now."
#    return

# label hotwife_sex_accept(the_person):
#     if the_person.effective_sluttiness() > 70:
#         if the_person.obedience < 70:
#             the_person "I was just about to suggest the same thing."
#         else:
#             the_person "Mmm, you have a dirty mind [the_person.mc_title], I like it."
#     else:
#         the_person "Okay, we can give that a try."
#     return

label hotwife_sex_obedience_accept(the_person):
    if the_person.effective_sluttiness() > 70:
        the_person "Oh god [the_person.mc_title], I should really say no... but thinking about daddy doing this to me too gets me so hot!"
    else:
        if the_person.obedience > 130:
            the_person "Yes [the_person.mc_title], if that's what you want to do I'll give it a try."
        else:
            the_person "I... Okay, if you really want to, lets give it a try."
    return

# label hotwife_sex_gentle_reject(the_person):
#     if the_person.effective_sluttiness() > 50:
#         the_person "Wait, I don't think I'm warmed up enough for this [the_person.mc_title]. How about we do something else first?"
#     else:
#         the_person "Wait. I don't think I'm comfortable with this. Could we just do something else instead?"
#     return

label hotwife_sex_angry_reject(the_person):
    if the_person.effective_sluttiness() < 20:
        the_person "What the fuck! Do you think I'm just some whore who puts out for anyone who asks?"
        the_person "Not even daddy asks me to do that! Get the fuck away from me."
    else:
        the_person "What the fuck do you think you're doing, that's disgusting!"
        the_person "Not even daddy asks me to do that! Get the fuck away from me."
    return

label hotwife_seduction_response(the_person):
    if the_person.obedience > 130:
        if the_person.effective_sluttiness() > 50:
            the_person "Yes [the_person.mc_title]? Want to take some pics together?"
        else:
            the_person "Yes [the_person.mc_title]? Is there something I can help you with?"
    else:
        if the_person.effective_sluttiness() > 50:
            the_person "Mmm, I know that look. Do you want to fool around a little?"
        elif the_person.effective_sluttiness() > 10:
            the_person "Oh, do you see something you like?"
        else:
            the_person "Oh, I don't really know what to say [the_person.mc_title]..."
    return

# label hotwife_seduction_accept_crowded(the_person):
#     if mc.location == downtown_bar:
#         if the_person.effective_sluttiness() < 20:
#             the_person "I suppose we could sneak away into the locker room... There's nothing wrong with that, right?"
#         elif the_person.effective_sluttiness() < 70:
#             the_person "Come on, let's sneak into the locker room and do it!"
#         else:
#             the_person "Oh fuck that sounds nice. I'm not sure I can wait until we sneak into the locker room, maybe we should just do it right here!"
#         return
#
#     if the_person.effective_sluttiness() < 20:
#         the_person "I suppose we could sneak away for a few minutes. There's nothing wrong with that, right?"
#     elif the_person.effective_sluttiness() < 50:
#         the_person "Come on, let's go find someplace quiet where we won't be interrupted."
#     else:
#         the_person "No point waisting any time then, right? Let's get to it!"
#     return

# label hotwife_seduction_accept_alone(the_person):
#     if mc.location == downtown_bar:
#         if the_person.effective_sluttiness() < 20:
#             the_person "Well, there's nobody around to see us..."
#         elif the_person.effective_sluttiness() < 50:
#             the_person "I can't believe how empty the gym is right now. Let's do it right here!"
#         else:
#             the_person "Oh [the_person.mc_title], the gym is empty, fuck me now!"
#         return
#     if the_person.effective_sluttiness() < 20:
#         the_person "Well, there's nobody around to stop us..."
#     elif the_person.effective_sluttiness() < 50:
#         the_person "Mmm, that's a fun idea. Come on, let's get to it!"
#     else:
#         the_person "Oh [the_person.mc_title], don't make me wait!"
#     return

#label hotwife_seduction_refuse(the_person):
#    if the_person.effective_sluttiness() < 20:
#        "[the_person.title] blushes and looks away from you awkwardly."
#        the_person "I, uh... Sorry [the_person.mc_title], I just don't feel that way about you."
#
#    elif the_person.effective_sluttiness() < 50:
#        the_person "Oh, it's tempting, but I'm just not feeling like it right now. Maybe some other time?"
#        "[the_person.title] smiles and gives you a wink."
#
#    else:
#        the_person "It's so, so tempting, but I don't really feel up to it right now [the_person.mc_title]. Hold onto that thought though."
#    return

label hotwife_flirt_response(the_person):
    if mc.location == downtown_bar:
        if the_person.love > 50:  #She loves you too much and is going to or already has called things off
            the_person "Didn't your mother ever tell you its rude to hit on a married woman?"
            return
        if the_person.event_triggers_dict.get("hotwife_progress", 0) >= 2:
            the_person "Well why don't you meet me in the back in a bit and we'll see what happens?"
        else:
            the_person "Hey, maybe if you buy me a drink first."
            "[the_person.title] gives you a wink and smiles."
        return

    if the_person.obedience > 130:
        if the_person.effective_sluttiness() > 50:
            the_person "If that's what you want I'm sure I could help with that [the_person.mc_title]."
        else:
            the_person "Thank you for the compliment, [the_person.mc_title]."
    else:
        if the_person.effective_sluttiness() > 50:
            the_person "Mmm, if that's what you want I'm sure I could find a chance to give you a quick peak."
            "[the_person.title] smiles at you and spins around, giving you a full look at her body."
        else:
            the_person "Hey, maybe if you buy me dinner first."
            "[the_person.title] gives you a wink and smiles."
    return

label hotwife_flirt_response_low(the_person):
    #She's in her own outfit.
    the_person "Thanks! It's really cute, right? My husband helped me pick it out!"
    $ the_person.draw_person(position = "walking_away")
    "She smiles and gives you a quick spin, showing off her outfit from every angle."
    $ the_person.draw_person()
    return

label hotwife_flirt_response_mid(the_person):

    if the_person.effective_sluttiness() < 20 and mc.location.get_person_count() > 1:
        if the_person.outfit.tits_visible():
            the_person "Are you sure you don't mean my tits look good in this outfit?"
            "She winks and wiggles her shoulders, setting her boobs jiggling for you."
            mc.name "All of you looks good, tits included."
            the_person "Good answer. I knew you would like this look when I was picking it out this morning."
        else:
            the_person "Aw, thanks! I thought this was a pretty hot look when I was getting dressed this morning."

        the_person "Maybe hubby will let you come shopping with me one day, so you can tell me what else you want to see me in."
        mc.name "I think I would like that."

    else:
        the_person "Thanks, hubby thought I looked pretty hot in it too this morning when I picked it out."
        the_person "You want a better look, right? Here, how does it make my ass look?"
        $ the_person.draw_person(position = "back_peek")
        the_person "Good?"
        mc.name "Fantastic. I wish I could get an even better look at it."
        "[the_person.possessive_title] smiles and turns back to face you."
        $ the_person.draw_person()
        the_person "I'm sure you do. Buy me a drink and we'll see what happens."
    return

label hotwife_flirt_response_high(the_person):
    if the_person.love > 50: #She is going to ghost soon
        the_person "Didn't your mother ever tell you its rude to hit on a married woman?"
    else:
        "She looks at you and her eyes narrow."
        the_person "I appreciate the comment, I really do... but I'm worried you are taking things a little too far."
        the_person "Remember, we need to keep things CASUAL. Okay?"
    return


label hotwife_hookup_rejection(the_person):
    the_person "Your loss! Just thinking about you makes me want to get on my knees, and you could have had some of this..."
    return

label hotwife_hookup_accept(the_person):
    the_person "Meet me at the bar... you know where to go! ;)"
    "You put your phone in your pocket and head to the bar."

    $ mc.change_location(downtown_bar)
    $ mc.location.show_background()

    "A few minutes later, you walk into the bar. You start walking back toward the women's restroom. The bartender nods to you as you pass the bar."
    $ work_bathroom.show_background()
    $ the_person.draw_person(position = "stand4")
    $ the_person.arousal = 20
    "You discover [the_person.possessive_title] standing at one of the sinks, touching herself while waiting for you. Her pussy glistens with arousal."
    "You quickly lock the door behind you. She notices you walk in but doesn't say a word."
    $ the_person.draw_person(position = "kissing")
    "You walk over to her silently. She looks into your eyes as she wraps her arms around your shoulders. You bring your face to hers and begin to make out."
    "You waste no time and grab her hips with your hands. You pull her close and she begins to grind her hips against yours."
    the_person "Mmmm, my favorite bull is here to take care of me."
    $ the_person.change_arousal( 15 + (mc.sex_skills["Foreplay"] * 2)) #35 + 2
    "You run your hands along her stomach and back up a little bit, giving yourself some room to work."
    "You run your hand down [the_person.title]'s belly, across her mound and between her legs. She moans as your fingers run across her labia."
    the_person "I'm glad I called you, that feels good..."
    $ the_person.change_arousal( 15 + (mc.sex_skills["Foreplay"] * 2)) #50 + 4
    "[the_person.title] runs a hand through your hair, while you run your fingers along her slit."
    "You move two fingers across her clitoris gently in long strokes."
    "She grinds herself happily against your hand. She moans appreciatively at your skilled fingering."
    "You bring two fingers to her dripping hole and push them up inside of her. You find her G-spot and begin to stroke it firmly."
    the_person "Mmm, that's the spot..."
    "[the_person.title] gasps as you stroke her. Her body is reacting quickly to your fingers."
    $ the_person.change_arousal( 15 + (mc.sex_skills["Foreplay"] * 2)) #65 + 6
    if the_person.arousal > 100: #She is surprised how fast you make her cum
        "Suddenly, you feel her body go stiff and her moans ramp up quickly."
        the_person "Fuck! I'm gonna... you're gonna make me...!"
        "[the_person.title] convulses as she orgasms. She is caught completely off guard by how fast you made her cum."
        "The hand on the back of your head lets go but you continue to stroke her G-spot for several more seconds."
        $ the_person.change_slut_temp(1)
        $ the_person.change_happiness(2)
    else:
        the_person "Mmm, that's it. Your fingers feel so good."
        "[the_person.title]'s hand on the back of your head guides your face down to one of her breasts. You like and suck at her nipples as you continue to finger her."
        "Her body is responding. Her hips are starting to twitch back and forth on their own as she approaches an orgasm."
        $ the_person.change_arousal( 15 + (mc.sex_skills["Foreplay"] * 2)) #80 + 8
        if the_person.arousal > 100: #She orgasms
            the_person "Yes! That's it! I'm gonna cum!"
            "[the_person.title] convulses as she orgasms. She moans and runs her hands through your hair."
            "You continue to stroke her G-spot for several more seconds."
        else:   #Not skilled enough to make her orgasm.
            "You are feverishly working at her pussy, but for some reason you can seem to find the right spot."
            "Soon, your wrist starts to cramp up from the bad angle forcing you to slow. She is a little frustrated but still very aroused."
    $ the_person.change_arousal(-30) #50 + 8
    the_person "Mmm, that was a great warmup. Let me return the favor."
    "[the_person.possessive_title] quickly helps your undress, then gets down on her knees in front of you."

    $ the_person.draw_person(position = "blowjob")
    the_person "Here, don't forget this!"
    "She hands you her phone. You snap a couple picture of this bombshell on her knees with your cock in the foreground."
    "She gives your cock a few slow strokes before she begins to lick the tip. Her tongue feels like wet velvet as it circles around your glans."
    "[the_person.title] opens her mouth and then envelopes the end of your dick with her warm, wet mouth."
    "[the_person.title] keeps her mouth open wide and bobs her head back and forth to slide your cock in and out. The feeling of her soft, warm mouth sends shivers up your spine."
    "As she slides her tongue along your length you snap a few more pictures."
    "It feels amazing, you can tell if you let her keep going you will cum quickly."
    #TODO write blowjob finish scene#
    mc.name "That feels great, but I don't want to finish in your mouth. Why don't you stand up and turn around..."
    $ the_person.draw_person( position = "standing_doggy")
    if the_person.effective_sluttiness() > 40: #She asks if you want to use a condom
        the_person "Do you want to put on a condom first?"
        menu:
            "Put on a condom":
                mc.name "Yeah, I'd probably better. I may not be able to resist pulling out."
                if the_person.effective_sluttiness() > 60:
                    the_person "I mean... its okay with me if you wanted to stick it in for a little bit without one on, you know, just to get started..."
                    if the_person.effective_sluttiness() > 90:
                        the_person "...or even just finish inside me. I promise I wouldn't mind at all!"
                    mc.name "Maybe next time!"
                "You get a condom and put it on quickly."
                $ mc.condom = True
            "Fuck her raw":
                $ mc.condom = False
                mc.name "No way, I want to feel everything."
                if the_person.effective_sluttiness() > 60:
                    the_person "Mmmm, sounds good. I was hoping you would say that!"
                    if the_person.effective_sluttiness() > 80:
                        "She wiggles her ass back and forth a little bit."
                        the_person "You don't need to worry about pulling out. My husband goes crazy when another man cums inside me!"
                else:
                    the_person "Okay, just make sure to pull out before you finish, okay?"
    else:
        the_person "You have a condom right? Make sure you put one on..."
        mc.name "Right! I'd probably better. I may not be able to resist pulling out."
        "You get a condom and put it on quickly."
        $ mc.condom = True
    "You put your hands on her hips and put your dick at her entrance. She is still soaked from your fingering earlier, so you easily slide into her."
    "Her pussy feels amazing wrapped around your erection. Her legs shake a bit as she gets used to the depth of your penetration."
    $ the_person.change_arousal(20) #70 + 8
    the_person "Ohhh, [the_person.mc_title]... That is exactly what I was hoping for when I sent you that text earlier. That feels so good..."
    "You give her a few tentative thrusts, then quickly pick up the pace and begin fucking her in earnest."
    "You set her phone to video mode, and take a clip of her backside rippling as you thrust in and out of her."
    "Your hips slap against [the_person.possessive_title]'s ass as you fuck her vigorously."
    $ the_person.call_dialogue("sex_responses_vaginal")
    if mc.condom == True:
        "You grasp her ass with both hands and begin to grope her. You knead her cheeks as your hips slowly work your erection in and out of her."
        $ the_person.change_arousal(20) #90 + 8
        if the_person.arousal > 100:
            "You can feel [the_person.title]'s pussy begin to spasm as she cums. You can see in the mirror that her mouth is hanging open and her eyes are closed."
            $ the_person.change_slut_temp(1)
            $ the_person.change_happiness(2)
        "After the stimulation from hew blowjob earlier, you know you aren't going to last long. You give her ass a loud spank."
        mc.name "That's it, bitch. I'm about to cum!"
        if the_person.effective_sluttiness() > 100: #She is so slutty, she begs for your cum.
            the_person "The condom! Take it off! Please!?! Your cock is so good, I want to feel you dump your load inside me!"
            "Your brain is getting a little hazy with lust. Surely there's nothing wrong with that, right?"
            menu:
                "Take It Off":
                    "In one swift you pull out of [the_person.title], pull the condom off, then shove yourself deep back inside her."
                    "You wad up the condom then throw it on the counter. It lands with splat."
                    the_person "Yes! Cum for me! I want to feel it!"
                    $ the_person.change_arousal(20) #110 + 8
                    "Her excitement is too much. You bottom out and cum, dumping wave after wave of your semen deep inside of her."
                    the_person  "Yes! Fill me with your cum!"
                    "You feel her pussy convulsing around your dick as she also starts to orgasm."
                    $ the_person.change_slut_temp(1)
                    $ the_person.change_happiness(2)
                    $ the_person.cum_in_vagina()
                    "You wait until your orgasm has passed completely, then pull out and stand back. You cum leaks from her well used pussy."
                    "You use her phone and get several close up pictures of her well used snatch with your load dripping out of it."
                    "You take a moment to recover. Then you and [the_person.title] get cleaned up and dress. You quietly sneak out of the restroom."
                    return
                "Leave It On":
                    mc.name "I can't pull out, even for a second!"
        "You bottom out and cum, dumping your load into the condom."
        "You wait until your orgasm has passed completely, then pull out and stand back. Your condom is bulged on the end where it is filled with your seed."
        if the_person.arousal < 100:
            the_person "Wow, okay, I guess we are done?"
            $ the_person.change_happiness(-5)
            $ the_person.change_obedience(-5)
            "She is a bit disappointed she didn't finish."
        else:
            the_person "That was nice. I'll make sure next time I'm in the mood to hit you up again..."
        "You take your condom off and throw it in the trash can. You both get dressed before sneaking out of the bathroom."
        return
    else: #You went in raw
        "You push yourself in as deep as you can go. [the_person.possessive_title] moans as you fill her completely."
        "With every thrust, her ass ripples pleasantly. You give her cheek an open handed spank and watch as shockwaves expand from the epicenter."
        "[the_person.title] moans at your rough treatment."
        $ the_person.change_arousal(20) #70 + 8
        if the_person.arousal > 100:
            "You can feel [the_person.title]'s pussy begin to spasm as she cums. Her silky wetness contracting around you feels amazing."
            $ the_person.change_slut_temp(1)
            $ the_person.change_happiness(2)
    if the_person.effective_sluttiness() > 70:
        the_person "You should stick a finger in my other hole while you fuck me and take a picture. Then hubby will have to reclaim both holes!"
        "Wow, its not every day you have a beautiful married woman ask you to finger her ass while you bend her over and fuck her!"
        "You reach a hand forward and put your index finger in front of her face. She quickly gets the idea and opens her mouth with her tongue out, and begins slathering your finger with saliva."
        "When satisfied, you bring you fingers back to her tight back passage. You pull your cock almost completely out and stop you hip motion as you begin to press your finger against [the_person.title]'s puckered hole."
        "She forces her sphincter to relax and your finger begins to slip inside her."
        the_person "Ohh, yes. You can move your hips, that feels good..."
        "You give [the_person.possessive_title]'s cunt a few slow thrusts, while simultaneously fingering her other hole."
        $ the_person.change_arousal(20)#90 + 8
        if the_person.arousal > 120:
            the_person "OH! Its so good... fuck I'm gonna cum again!!!"
            "You get the now familiar feeling of [the_person.title] cumming around your cock, but this time you can also feel the waves around your finger."
            "You almost forgot to take some pictures! You grab her phone with your free hand and snap a few pics of her getting double penetration."
            "You wonder what it would feel like to make her cum again, but with your cock in her ass instead..."
            menu:
                "Stay Vaginal":
                    "As [the_person.title]'s pussy quivers around you, you decide to just keep doing what you are doing."
                "Fuck Her Ass" if the_person.effective_sluttiness() >= 80:
                    "You pull out of her pussy. Her juices leave a strand attached to you, connecting you to her cunt."
                    the_person "Mmm, [the_person.mc_title]? Why did you pull out... OH!"
                    "Her question is swiftly answered when she feels your manhood poking her puckered hole."
                    if the_person.effective_sluttiness() > 100:
                        the_person "Yes! Fuck my ass good!"
                    else:
                        the_person "Oh my... be careful!"
                    "With your hands firmly on her hips, you slowly push forward. It takes several seconds of steady pressure until you finally bottom out."
                    the_person "Oh god you make me feel so dirty... I love it!"
                    "You fuck her hard but at a steady, even pace."
                    "[the_person.possessive_title] moans, matching each hip movement of yours with movement of her own."
                    the_person "It feels so deep... I can't... my legs!"
                    "Her knees give out, but you are too close to stop fucking her. You grab her hips roughly and pick up the pace."
                    $ the_person.change_arousal(20)#110 + 8
                    "Her ass begins to spasm. Her buttery smooth back passage squeezes you over and over as her body is racked with yet another orgasm. It feels incredible."
                    $ the_person.change_slut_temp(2)
                    $ the_person.change_happiness(5)
                    mc.name "Get ready, I'm gonna cum!"
                    "[the_person.title] is incoherent, and doesn't process your words."
                    "You plunge deep into her ass and hold it there while you cum. She gasps in time with each new shot of hot semen inside of her."
                    $ the_person.cum_in_ass()
                    "You stand there for a minute, holding her hips in the air, you dick buried in her bowel as it softens. Eventually she speaks up."
                    the_person "Wow... okay... I think I can stand now..."
                    "You slowly let her down. Her legs buckle for a second, but she catches herself."
                    "You see a faint trace of your semen running down the back of her leg."
                    "You take several pics now. Her hole is gaping slightly and you can see the faint tint of your creamy deposit inside it."
                    the_person "That was SO good. You'll be hearing from me again, I'm sure. I can't wait to send hubby those pictures..."
                    "You and [the_person.title] get cleaned up and dressed, then sneak out of the restroom."
                    return
                "Fuck Her Ass\n{color=#ff0000}{size=18}Requires 80 sluttiness{/size}{/color} (disabled)" if the_person.effective_sluttiness() < 80:
                    pass
    "[the_person.possessive_title]'s creamy cunt draws you closer to your orgasm with each thrust. You finally pass the point of no return and speed up, fucking her as hard as you can manage."
    mc.name "Get ready, I'm gonna cum!"
    $ the_person.change_arousal(35)
    if the_person.effective_sluttiness() > 90:
        "To your surprise [the_person.title] reaches back with both hands and grabs your hips, pulling you deep inside of her."
        "Her grip is startlingly strong. You don't think you could pull out even if you wanted to!"
        the_person "That's it, cum with me!"
        "You cum erupts in a torrent. You seed spills deep inside [the_person.title]. Her entire body begins to spasm as she joins you in orgasm."
        $ the_person.change_happiness(5)
        $ the_person.change_slut_temp(1)
        $ the_person.cum_in_vagina()
        "You wait until your orgasm has passed completely, then pull out and stand back. You cum leaks from her well used pussy."
        "You use her phone and get several close up pictures of her well used snatch with your load dripping out of it."
        "You take a moment to recover. Then you and [the_person.title] get cleaned up and dress. You quietly sneak out of the restroom."
        return
    elif the_person.effective_sluttiness() > 60:
        the_person "Oh god... you should probably pull out but... it feels so good..."
        "You briefly consider pulling out."
        menu:
            "Pull Out":
                "You pull out of [the_person.possessive_title] at the last moment, stroking your shaft as you blow your load over her ass. She holds still for you as you cover her with your sperm."
                the_person "Oh! Its so hot on my skin!"
                $ the_person.cum_on_ass()
                $ the_person.draw_person(position = "standing_doggy")
                "You stand back and sigh contentedly, enjoying the sight of [the_person.possessive_title]'s ass covered in your semen."
                "You use her phone and get several close up pictures of her luscious ass with your load covering it."
                "You take a moment to recover. Then you and [the_person.title] get cleaned up and dressed. You quietly sneak out of the restroom."
                return
            "Creampie":
                "Her pussy feels too good. You bottom out and cum, dumping wave after wave of your semen deep inside of her."
                "You seed spills deep inside [the_person.title]. Her entire body begins to spasm as she joins you in orgasm."
                $ the_person.change_happiness(5)
                $ the_person.change_slut_temp(1)
                $ the_person.cum_in_vagina()
                "You wait until your orgasm has passed completely, then pull out and stand back. You cum leaks from her well used pussy."
                "You use her phone and get several close up pictures of her well used snatch with your load dripping out of it."
                "You take a moment to recover. Then you and [the_person.title] get cleaned up and dressed. You quietly sneak out of the restroom."
                return
    else:
        "[the_person.title] suddenly moves her hips forward, your cock slides out of her."
        the_person "Cum on my ass!"
        "You stroke your shaft as you blow your load over her ass. She holds still for you as you cover her with your sperm."
        $ the_person.cum_on_ass()
        $ the_person.draw_person(position = "standing_doggy")
        "You stand back and sigh contentedly, enjoying the sight of [the_person.possessive_title]'s ass covered in your semen."
        "You use her phone and get several close up pictures of her luscious ass with your load covering it."
        "You take a moment to recover. Then you and [the_person.title] get cleaned up and dressed. You quietly sneak out of the restroom."
    return

#label hotwife_cum_face(the_person):
#    if the_person.obedience > 130:
#        if the_person.effective_sluttiness() > 60:
#            the_person "Do I look cute covered in your cum, [the_person.mc_title]?"
#            "[the_person.title] licks her lips, cleaning up a few drops of your semen that had run down her face."
#        else:
#            the_person "I hope this means I did a good job."
#            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
#    else:
#        if the_person.effective_sluttiness() > 80:
#            the_person "Ah... I love a nice, hot load on my face. Don't you think I look cute like this?"
#        else:
#            the_person "Fuck me, you really pumped it out, didn't you?"
#            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
#    return

label hotwife_cum_mouth(the_person):
    if mc.location == downtown_bar or the_person.has_cum_fetish():
        if the_person.has_cum_fetish() or the_person.effective_sluttiness() > 80 or the_person.get_opinion_score("drinking cum") > 1:
            the_person "Your cum tastes great [the_person.mc_title]! I bet I get another tasty load later..."
            "[the_person.possessive_title] winks at you as she swallows your cum."
        elif the_person.effective_sluttiness() > 50 or the_person.get_opinion_score("drinking cum") > 0:
            the_person "Thanks [the_person.mc_title]. I hope daddy cums in my mouth later too!"
        else:
            "[the_person.title]'s face grimaces as she tastes your sperm in her mouth."
            the_person "Thank you [the_person.mc_title]. It doesn't taste the best, but I'm always a good little slut."
    elif the_person.obedience > 130:
        if the_person.effective_sluttiness() > 60 or the_person.get_opinion_score("drinking cum") > 0:
            the_person "That was very nice [the_person.mc_title], thank you."
        else:
            "[the_person.title]'s face grimaces as she tastes your sperm in her mouth."
            the_person "Thank you [the_person.mc_title], I hope you had a good time."
    else:
        if the_person.effective_sluttiness() > 80 or the_person.get_opinion_score("drinking cum") > 0:
            the_person "Your cum tastes great [the_person.mc_title], thanks for giving me so much of it."
            "[the_person.title] licks her lips and sighs happily."
        else:
            the_person "Bleh, I don't know if I'll ever get used to that."
    return

#label hotwife_suprised_exclaim(the_person):
#    $rando = renpy.random.choice(["Fuck!","Shit!","Oh fuck!","Fuck me!","Ah! Oh fuck!", "Ah!", "Fucking tits!", "Holy shit!", "Fucking shit!"])
#    the_person "[rando]"
#    return

# label hotwife_talk_busy(the_person):
#     if mc.location == downtown_bar:
#         the_person "Hey, I'm really sorry but I need to keep on the lookout. Maybe another time?"
#     if the_person.obedience > 120:
#         the_person "Hey, I'm really sorry but I've got some stuff I need to take care of. Could we catch up some other time?"
#     else:
#         the_person "Hey, sorry [the_person.mc_title] but I've got some stuff to take care of. It was great talking though!"
#     return

#label hotwife_sex_strip(the_person):
#    if the_person.effective_sluttiness() < 20:
#        if the_person.arousal < 50:
#            the_person "Let me get this out of the way..."
#        else:
#            the_person "Let me get this out of the way for you..."
#
#    elif the_person.effective_sluttiness() < 60:
#        if the_person.arousal < 50:
#            the_person "This is just getting in the way..."
#        else:
#            the_person "Ah... I need to get this off."
#
#    else:
#        if the_person.arousal < 50:
#            the_person "Let me get this worthless thing off..."
#        else:
#            the_person "Oh god, I need all of this off so badly!"

#    return

# label hotwife_sex_watch(the_person, the_sex_person, the_position):
#     if the_person.effective_sluttiness() < the_position.slut_requirement - 20:
#         $ the_person.draw_person(emotion = "angry")
#         the_person "Holy shit, are you really doing this in front of everyone?"
#         $ the_person.change_obedience(-2)
#         $ the_person.change_happiness(-1)
#         "[the_person.title] looks away while you and [the_sex_person.name] [the_position.verb]."
#
#     elif the_person.effective_sluttiness() < the_position.slut_requirement - 10:
#         $ the_person.draw_person()
#         $ the_person.change_happiness(-1)
#         "[the_person.title] tries to avert her gaze while you and [the_sex_person.name] [the_position.verb]."
#
#     elif the_person.effective_sluttiness() < the_position.slut_requirement:
#         $ the_person.draw_person()
#         the_person "Oh my god, you two are just... Wow..."
#         $ change_report = the_person.change_slut_temp(1)
#         "[the_person.title] averts her gaze, but keeps glancing over while you and [the_sex_person.name] [the_position.verb]."
#
#     elif the_person.effective_sluttiness() > the_position.slut_requirement and the_person.effective_sluttiness() < the_position.slut_cap:
#         $ the_person.draw_person()
#         the_person "Oh my god that's... Wow that looks...Hot."
#         $ change_report = the_person.change_slut_temp(2)
#         "[the_person.title] watches you and [the_sex_person.name] [the_position.verb]."
#
#     else:
#         $ the_person.draw_person(emotion = "happy")
#         the_person "Come on [the_person.mc_title], you can give her a little more than that. I'm sure she can handle it."
#         "[the_person.title] watches eagerly while you and [the_sex_person.name] [the_position.verb]."
#
#     return

# label hotwife_being_watched(the_person, the_watcher, the_position):
#     if the_person.effective_sluttiness() >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
#         #They agree you should give it to her harder
#         the_person "I can handle it [the_person.mc_title], you can be rough with me."
#         $ the_person.change_arousal(1)
#         "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."
#
#     elif the_person.effective_sluttiness() >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
#         #She's super slutty and doesn't care what people think.
#         the_person "Don't listen to [the_watcher.title], I'm having a great time. Look, she can't stop peeking over."
#
#     elif the_person.effective_sluttiness() >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
#         #She's super slutty and encourages the watcher to be slutty.
#         $ the_person.change_arousal(1)
#         "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."
#
#     elif the_person.effective_sluttiness() < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
#         #She's into it and encouraged by the slut watching her.
#         the_person "Oh god, having you watch us like this..."
#         $ the_person.change_arousal(1)
#         "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."
#
#     elif the_person.effective_sluttiness() < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
#         #She's into it but shamed by the prude watching her.
#         the_person "[the_person.mc_title], maybe we shouldn't be doing this here..."
#         $ the_person.change_arousal(-1)
#         $ the_person.change_slut_temp(-1)
#         "[the_person.title] seems uncomfortable with [the_watcher.title] nearby."
#
#     else: #the_person.effective_sluttiness() < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
#         #They're both into it but not fanatical about it.
#         the_person "Oh my god, having you watch us do this feels so dirty. I think I like it!"
#         $ the_person.change_arousal(1)
#         $ the_person.change_slut_temp(1)
#         "[the_person.title] seems more comfortable [the_position.verbing] you with [the_watcher.title] around."
#
#     return

# label hotwife_work_enter_greeting(the_person):
#     if the_person.happiness < 80:
#         if the_person.obedience > 120:
#             "[the_person.title] gives you a curt nod and then turns back to what she was doing."
#         else:
#             "[the_person.title] glances at you when you enters the room then looks away quickly to avoid starting a conversation."
#
#     elif the_person.happiness > 120:
#         if the_person.effective_sluttiness() > 50:
#             "[the_person.title] looks up from her work when you enter the room."
#             the_person "Hey [the_person.mc_title]. Let me know if you need any help with anything. Anything at all."
#             "She smiles and winks, then turns back to what she was doing."
#         else:
#             "[the_person.title] turns to you when you enter the room and shoots you a smile."
#             the_person "Hey, good to see you!"
#
#     else:
#         if the_person.obedience < 90:
#             "[the_person.title] glances up from her work."
#             the_person "Hey, how's it going?"
#         else:
#             "[the_person.title] waves at you as you enter the room."
#             the_person "Hey, let me know if you need anything [the_person.mc_title]."
#     return

# label hotwife_date_seduction(the_person):
#     if the_person.effective_sluttiness() > the_person.love:
#         if the_person.effective_sluttiness() > 40:
#             the_person "I had a great time [the_person.mc_title], but I can think of a few more things we could do together. Want to come back to my place?"
#             # the_person "I had a great night [the_person.mc_title], would you like to come back to my place and let me repay the favour?"
#         else:
#             the_person "I had a really good time tonight [the_person.mc_title]. I don't normally do this but... would you like to come back to my place?"
#             #the_person "I had a great night [the_person.mc_title], but I don't see why it should end here. If you want to come back to my place I can think of a few things we could do."
#     else:
#         if the_person.love > 40:
#             the_person "You're such great company [the_person.mc_title]. Would you like to come back to my place and spend some more time together?"
#         else:
#             the_person "I had a great night [the_person.mc_title]. Would you like to come back to my place for a quick drink?"
#     return

## Role Specific Section ##
# label hotwife_improved_serum_unlock(the_person):
#     mc.name "[the_person.title], now that you've had some time in the lab there's something I wanted to talk to you about."
#     the_person "Okay, how can I help?"
#     mc.name "All of our research and development up until this point has been based on the limited notes I have from my university days. I'm sure there's more we could learn, and I want you to look into it for me."
#     "[the_person.title] smiles mischievously."
#     the_person "I've got an idea that you might want to hear then. It's not the most... orthodox testing procedure but I think it is necessary if we want to see rapid results."
#     mc.name "Go on, I'm interested."
#     the_person "Our testing procedures focus on human safety, which I'll admit is important, but it doesn't leave us with much information about the subjective effects of our creations."
#     the_person "What I want to do is take a dose of our serum myself, then have you record me while you run me through some questions."
#     return

#</editor-fold>
