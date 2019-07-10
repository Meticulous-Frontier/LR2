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
    def casual_hotwife_get_a_drink_requirement(the_person):  #For now this should always return true. May be other conditions not to in the future#
        if the_person.event_triggers_dict.get("hotwife_blowjob_text_enable", 0) == 1:
            return False
        return True

    def casual_hotwife_bathroom_blowjob_requirement(the_person):
        if the_person.event_triggers_dict.get("hotwife_progress", 0) < 1:
            return False
        if the_person.event_triggers_dict.get("hotwife_blowjob_text_enable", 0) == 1:
            return False
        if the_person.event_triggers_dict.get("hotwife_blowjob_enable", 0) == 1:
            #TODO Check to see if you are at the bar!!!
            return True
        elif mc.charisma < 4:
            return "Requires higher Charisma"
        elif the_person.sluttiness < 25:
            return "Requires higher sluttiness"
        else:
            return "Grab a drink with her first"
        return False

    def casual_hotwife_blowjob_text_requirement(the_person):
        if the_person.event_triggers_dict.get("hotwife_blowjob_text_enable", 0) == 1:
            if time_of_day < 3:
                return True
            else:
                return "You should ask her another time"
        return False

    def casual_hotwife_dancing_sex_requirement(the_person):

        return False

    def casual_hotwife_sex_invite_requirement(the_person):

        return False

    def casual_hotwife_her_place_requirement():

        return False

    def casual_hotwife_home_sex_requirement(the_person):

        return False


#*************Create Casual Hotwife Role***********#
init -1 python:
    casual_hotwife_get_a_drink = Action("Get a drink with her", casual_hotwife_get_a_drink_requirement, "casual_hotwife_get_a_drink_label",
        menu_tooltip = "Alcohol loosens lips!")
    casual_hotwife_bathroom_blowjob = Action("Sneak into the bathroom", casual_hotwife_bathroom_blowjob_requirement, "casual_hotwife_bathroom_blowjob_label",
        menu_tooltip = "She wants pics to send her husband...")
    casual_hotwife_blowjob_text = Action("Ask her about the blowjob pictures...", casual_hotwife_blowjob_text_requirement, "casual_hotwife_blowjob_text_label",
        menu_tooltip = "Make sure it went okay.")
    casual_hotwife_dancing_sex = Action("Dirty dancing", casual_hotwife_dancing_sex_requirement, "casual_hotwife_dancing_sex_label",
        menu_tooltip = "She wants to dance dirty with you!")
    casual_hotwife_sex_invite = Action("Your place or mine?", casual_hotwife_sex_invite_requirement, "casual_hotwife_sex_invite_label",
        menu_tooltip = "Ask if she wants to get out of here.")
    casual_hotwife_home_sex = Action("Put on a show.", casual_hotwife_home_sex_requirement, "casual_hotwife_home_sex_label",
        menu_tooltip = "Let hubby watch.")
    casual_hotwife_role = Role(role_name ="?????", actions =[casual_hotwife_get_a_drink, casual_hotwife_bathroom_blowjob, casual_hotwife_blowjob_text, casual_hotwife_dancing_sex, casual_hotwife_sex_invite, casual_hotwife_home_sex])

#*************Mandatory Crisis******************#

init 1 python:
    casual_hotwife_her_place = Action("Her Place", casual_hotwife_her_place_requirement, "casual_hotwife_her_place_label")


#************* Hotwife Action Labels *********#

#label (the_person):
#CSH00
label casual_hotwife_get_a_drink_label(the_person):
    mc.name "Care to get a drink, [the_person.title]?"
    if the_person.event_triggers_dict.get("hotwife_progress", 0) < 1:  #Do a charisma check to see if we continue...
        "[the_person.title] looks you over."
        if mc.charisma < 3:  #Fail charisma check
            "*Charisma Check Failed*"
            the_person.char "Hey, you're cute, but not really the kind of guy I'm looking for. Maybe another time."
            "You nod."
            mc.name "Another time then."
            "You should try raising your Charisma before you talk to her again!"
        else:               #Charisma Check Passed
            the_person.char "Hey... I'd love to grab a drink! Not often I find guys as cute as you!"
    else:
        the_person.char "Hey [the_person.mc_title]! A drink sounds great!"
    "You consider for a moment. If you offer to buy her a drink, you'll have a chance to slip a serum into it."
    $ offer_drink_chance = ((mc.charisma + (the_person.sluttiness / 10) + 2) * 10)  #More willing to let you buy a drink for her as she gets sluttier
    $ rand_chance = renpy.random.randint(0,100)
    $ bartender_name = get_random_male_name()
    menu:
        "Offer to Buy\n{size=22}Success Chance: [offer_drink_chance]%%{/size}":
            mc.name "Hey, let me buy you a drink."
            if rand_chance < offer_drink_chance:  #Success
                the_person.char "Hmm... Okay! That sounds great! I'll go find us a table!"
                "You head over to the bar and order yourself a beer, and a cocktail for [the_person.title]."
                "The place is busy, so its easy to slip some serum into her drink."
                call give_serum(the_person) from _call_give_serum_CSH000
            else:                                 #Fail

                the_person.char "That's okay! I prefer to go dutch anyway."
                "You head over to the bar and order yourself a beer, [the_person.title] orders herself a fruity sounding cocktail."
                the_person.char "Hey there, [bartender_name]! I'll have a flora dora tonight. You know how I like it!"
                "It sounds like she knows the bartender. She must be in here pretty often!"
        "Grab Drinks Seperately":
            the_person.char "That's okay! I prefer to go dutch anyway."
            "You head over to the bar and order yourself a beer, [the_person.title] orders herself a fruity sounding cocktail."
            the_person.char "Hey there, [bartender_name]! I'll have a flora dora tonight. You know how I like it!"
            "It sounds like she knows the bartender. She must be in here pretty often!"
    $ the_person.draw_person(position = "sitting")
    "You sit down at a table with [the_person.title]."

    #***Event State 0 ####
    if the_person.event_triggers_dict.get("hotwife_progress", 0) < 1:  #This is your first time grabbing a drink Together
        mc.name "So, you come here often?"
        the_person.char "Oh! Yeah, I'm here all the time. I'm on a first name basis with the bartender at this point, haha!"
        mc.name "That great! This place is pretty nice. I can see why you come here. You said earlier you don't find guys like me very often. It's hard to believe a beautiful girl like you is single!"
        "You see her cheeks blush a little bit."
        the_person.char "Yeah, well, I'm not exactly single. I'm more in, what you might call an open relationship..."
        "Her responses catches you a little bit by surprise."
        the_person.char "It's pretty crazy. To be honest I never thought I would do something like this, but recently my husband has started asking me to go out and meet other guys and then tell him how it goes..."
        "Ahhh, her husband is some kind of cuckold?"
        mc.name "Ah, I see. That's interesting! Managed to snag any guys yet?"
        the_person.char "Well... to be honest... no. I haven't. I've gone out by myself a few times now... but I'm still too nervous. Something about you though, it puts me at ease to be around you..."
        "You chat with [the_person.title] for a bit longer, but soon it is time to leave."
        $ the_person.event_triggers_dict["hotwife_progress"] = 1
        python:
            for role in the_person.special_role:
                if role.role_name == "?????":
                    role.role_name = "Hotwife"
        mc.name "Take care, I'm sure I'll see you here again sometime!"


    #***Event State 1 ####
    elif the_person.event_triggers_dict.get("hotwife_progress", 0) == 1:  #You are acquainted, but not yet done anything sexual
        mc.name "So, any luck going squirrel hunting?"
        if the_person.sluttiness > 25:
            "[the_person.possessive_title] laughs."
            the_person.char "No, not yet. I have a feeling though, the right opportunity may come a long soon..."
            "She lowers her voice a bit."
            the_person.char "To catch a squirrel, and take his nut... so to speak..."
            "Damn! Maybe she is finally ready to start the hotwife lifestyle."
            the_person.char "You wouldn't happen to know any squirrels would you?"
            mc.name "Oh, I think I know one... I bet he'd be more than happy to share his nuts with you..."
            "This analogy is starting to get a little weird though."
            mc.name "I bet your husband would be excited if you did manage to catch one."
            "[the_person.title] stutters for a second, but quickly smiles and regains her composure."
            the_person.char "Yeah, he keeps saying he will. I think its probably about time I put his eagerness to the test."
            if the_person.event_triggers_dict.get("hotwife_blowjob_enable", 0) == 1:
                the_person.char "Just let me know when you have the time... I think we would both really enjoy our time."
                "[the_person.title] licks her lips, then gets up."
                $ the_person.draw_person (position = "stand4")
                the_person.char "See ya later [the_person.mc_title]"
            elif mc.charisma > 3:
                the_person.char "Tell you what... I have to get going for now... but next time you see me here..."
                "She gives you a wink."
                the_person.char "I'm good friends with the bartender... I'm sure if I asked he'd give us some private time back in the bathroom..."
                mc.name "Damn. Sounds good. I'll be sure to look for your soon."
                "[the_person.title] licks her lips, then gets up."
                $ the_person.draw_person (position = "stand4")
                the_person.char "See ya later [the_person.mc_title]"
                $ the_person.event_triggers_dict["hotwife_blowjob_enable"] = 1
                "Sounds like you might get lucky next time you meet up with [the_person.possessive_title]"
            else:
                "Failed Charisma Check."
                "She looks at you for a second, then hesitates."
                the_person.char "Soon... anyway..."
                $ the_person.draw_person (position = "stand4")
                "[the_person.title] stands up abruptly."
                the_person.char "Sorry, I gotta get going. See ya later [the_person.mc_title]!"
                "You wave goodbye as she walks off. You should work on your Charisma more and talk to her again sometime..."
        else:
            "[the_person.possessive_title] sighs."
            the_person.char "No, not yet. I'm just having a hard time getting myself to open up to that kind of thing."
            mc.name "Well, it is definitely not something you want to rush into."
            the_person.char "Yeah... he keeps telling me... he wants me to seduce a guy, and get pictures, to send him you know?"
            "Yep! He definitely sounds like a cuckold."
            the_person.char "But I don't know, I think maybe I just need a little more time."
            "Sounds like she might benefit from a few more doses of your serum, too..."
    elif the_person.event_triggers_dict.get("hotwife_progress", 0) == 2:  #She has blown you
        "This scene is not yet written!"

    elif the_person.event_triggers_dict.get("hotwife_progress", 0) == 3:  #She's fucked you
        "This scene is not yet written!"

    elif the_person.event_triggers_dict.get("hotwife_progress", 0) == 4:  #She's invied you over
        "You chat with [the_person.title] for a while, but you can definitely feel some tension in the air about your arrangement for tonight."
        mc.name "So... tonight at your place? I'll see you there?"
        the_person.char "Sounds good. See you then, [the_person.mc_title]."
    elif the_person.event_triggers_dict.get("hotwife_progress", 0) == 5:  #You've fucked in front of her hustband
        "This scene is not yet written!"
    else:
        "DEBUG: How did you get here?"
    return

#CSH10
label casual_hotwife_bathroom_blowjob_label(the_person):
    if the_person.event_triggers_dict.get("hotwife_progress", 0) == 1: #This is our first time doing this
        mc.name "Hey, so uhh... wanna sneak into the bathroom for a bit?"
        "You see a bright red flush in her cheeks, but she quickly nods."
        the_person.char "I would like that...a lot!"
        "She takes a quick look around."
        the_person.char "Let me just go talk to the bartender... head to the lady's room and wait outside... I'll be over in a second."
        $ the_person.draw_person(position = "walking_away")
        "[the_person.possessive_title] walk away to talk to the bartender. You make your way over to the lady's room."
        $ the_person.draw_person(position = "stand4")
        "Soon, [the_person.title] comes over, holding a sign that says 'Bathroom closed for renovations: Please use men's room"
        "You both take a quick look around, and when the coast is clear, you both walk into the bathroom and lock the door behind you."
        "You waste no time, you quickly wrap your arms around [the_person.title] and start making out with her."
        $ the_person.draw_person(position = "kissing")
        the_person.char "Mm... mmm.... mmmmmmmmmff..."
        "She is moaning in your mouth. You can tell the naughtiness of getting intimate with someone other than her husband is really turning her on."
        $ the_person.change_arousal(10)
        the_person.char "Ok... wow this is hot. This is my first time ever doing something like this... so... I want you to just let me do my thing, ok?"
        "You quickly agree."
        the_person.char "Also, could you take my phone? And like, you know, take some pictures for me? Daddy asked me to..."
        "She is very awkwardly asking. You quickly answer like this is a completely normal request to put her at ease."
        mc.name "Of course! How else is daddy gonna know what his slutty girl has been up to?"
        "She smiles."
        the_person.char "Exactly!"
        "She hands you her phone with the camera app up."
        $ the_person.draw_person(position = "stand3")
        if not the_person.outfit.tits_available():    #If covered up, have her take her top off
            the_person.char "Here I go... don't forget to take pictures!"
            $ the_clothing = the_person.outfit.get_upper_ordered()[-1]
            "[the_person.possessive_title] takes off her [the_clothing.name]"
            $ the_person.draw_animated_removal(the_clothing)
        else:
            "[the_person.possessive_title] strikes a pose, her tits on display."
            the_person.char "Don't forget to take pictures!"
        "With her phone in hand, you snap a few pictures as she slowly walks over to you."
        "She runs her hands across your chest. She slowly gets down on her knees in front of you."
        $ the_person.draw_person(position = "blowjob")
        "[the_person.possessive_title] tugs at your belt, then slowly lowers your pants."
        "One more tug on your underwear, and your erection springs free."
        the_person.char "Wow! I haven't seen anything other than hubby for... years..."
        "She begins to stroke you softly with her hand."
        the_person.char "Mmmmm.... its so hard... and hot!"
        "You moan as she strokes you. You make sure to snap a couple pictures."
        the_person.char "Does that feel good? I bet it does... I just wanna make you feel good..."
        "She closes her eyes, then opens her mouth. She slowly rubs the tip back and forth along her slithery tongue."
        the_person.char "Mmm, you taste good too."
        "She starts to take you into her mouth. You snap a few more pictures of this beautiful hotwife, on her knees servicing you."
        "[the_person.possessive_title]'s head is now bouncing up and down on your cock. Her pouty lips feel amazing sliding up and down your length."
        "You forget you are supposed to take pictures and begin to just enjoy the wonderful sensations."
        call sex_description(the_person, blowjob, make_floor(), 1, private= True, girl_in_charge = True) from _call_sex_description_CSH010
        if the_person.arousal > 100:
            "Wow... I can't believe I came... while I was blowing you! That was fucking hot!"
        else:
            "Wow... that was hot!"
        $ cum_face = False
        $ cum_mouth = False
        python:
            for cs_access in the_person.outfit.accessories:
                if cs_access.name == "Mouth Cum":    #You came in her mouth!
                    cum_mouth = True
                if cs_access.name == "Face Cum":     #You came on her face!
                    cum_face = True
        if cum_mouth:
            "[the_person.possessive_title] looks up at you. She couldn't quiet swallow all your cum, some of it is slowly dripping down the sides of her mouth."
            the_person.char "Hey! Don't forget to take pictures!"
            "You suddenly remember the phone. You snap a couple pictures of her face with your traces of cum on it."
        else:
            "[the_person.possessive_title] looks up at you. Her face is plastered with your sticky seed."
            the_person.char "Hey! Don't forget to take pictures!"
            "You suddenly remember the phone. You snap a couple pictures of her face with your cum covering it."
        $ the_person.draw_person (position = "stand2")
        "[the_person.title] stands up. You hand her back her phone."
        the_person.char "Wow... well... I guess theres no going back now? I guess I'll go ahead and send him some of these..."
        "The gets close to you."
        the_person.char "Well, no matter what happens tonight, thanks for your help! If all goes well... maybe we can do this again."
        mc.name "Yeah I mean... if it makes your hubby happy for you to give me blowjobs... I GUESS I can help out..."
        "She laughs and punches you in the arm."
        the_person.char "Alright, I'm going to clean up. I'll see you."
        "You sneak your way out of the bathroom while [the_person.possessive_title] cleans herself up. You hope everything goes well with her tonight!"
        $ the_person.event_triggers_dict["hotwife_blowjob_text_enable"] = 1
        $ the_person.event_triggers_dict["hotwife_progress"] = 2
        $ the_person.reset_arousal()
        $ the_person.review_outfit(show_review_message = False)
    else:   #This is not our first time getting blown#
        mc.name "Hey, you wanna sneak off for a bit?"
        "[the_person.possessive_title] flashes you her beautiful smile."
        the_person.char "You bet! You know what to do!"
        "You head to the lady's room. [the_person.title] soon follows behind you. She locks the door as she closes it."
        $ the_person.draw_person (position = "kissing")
        "You waste no time. She throws her arms around you and you begin to make out."
        if the_person.sluttiness > 30 and not the_person.outfit.tits_available():
            "[the_person.possessive_title] steps back suddenly."
            the_person.char "Let me just get this off... daddy loves it when I have my tits out for this..."
            "She hands you her phone with the camera app out. You snap some pictures as she starts to strip."
            while not the_person.outfit.tits_available():
                $ the_clothing = the_person.outfit.get_upper_ordered()[-1]
                "[the_person.possessive_title] takes off her [the_clothing.name]"
                $ the_person.draw_animated_removal(the_clothing)
            "With her tits completely exposed, she saunters back over to you then starts to get down on her knees."
        else:
            "[the_person.possessive_title] slowly starts to get down on her knees in front of you."
        $ the_person.draw_person(position = "blowjob")
        "You can tell that [the_person.title] is hungry. She wastes no time pulling your pants off, followed quickly by your underwear."
        "Your hardened cock springs out. Her agile hands grasp it and begin to stroke."
        if the_person.sluttiness > 50:
            the_person.char "Mmm, I've been working on a new skill lately... since we started doing this. Mind if I practice on you?"
            mc.name "Sure I guess, but what is..."
            "She doesn't wait for you to finish your response. In one, smooth motion, she opens her mouth and swallows your cock whole."
            "Past her lips, to the back of her tongue, and down her throat the tip of your dick goes."
            mc.name "Oh fuck!"
            "You make sure to snap more pictures of her. She's getting good at this!"
            "You decide to just enjoy her skilled mouth going down on you."
            call sex_description(the_person, deepthroat, make_floor(), 1, private= True, girl_in_charge = True) from _call_sex_description_CSH011
        else:
            the_person.char "Mmmm, I can't wait any longer... I have to taste it!"
            "She opens up her mouth and wraps her lips around your meat."
            "You snap some pictures as she pulls of and begin to run her tongue up and down along the sides of your cock."
            mc.name "Mmm, that feels great [the_person.title]."
            "You decide to just enjoy her skilled mouth going down on you."
            call sex_description(the_person, blowjob, make_floor(), 1, private= True, girl_in_charge = True) from _call_sex_description_CSH012

        $ cum_face = False
        $ cum_mouth = False
        python:
            for cs_access in the_person.outfit.accessories:
                if cs_access.name == "Mouth Cum":    #You came in her mouth!
                    cum_mouth = True
                if cs_access.name == "Face Cum":     #You came on her face!
                    cum_face = True
        if cum_mouth:
            "[the_person.possessive_title] looks up at you. She couldn't quiet swallow all your cum, some of it is slowly dripping down the sides of her mouth."
            the_person.char "Hey! Don't forget to take pictures!"
            "You suddenly remember the phone. You snap a couple pictures of her face with your traces of cum on it."
        else:
            "[the_person.possessive_title] looks up at you. Her face is plastered with your sticky seed."
            the_person.char "Hey! Don't forget to take pictures!"
            "You suddenly remember the phone. You snap a couple pictures of her face with your cum covering it."
        the_person.char "Mmm, that was great [the_person.mc_title]! I can't wait until I get home tonight... I hope daddy gets the handcuffs out again..."
        "You say goodbye and excuse yourself while she gets herself cleaned up. This arrangement is working out to be very beneficial!"
        $ the_person.reset_arousal()
        $ the_person.review_outfit(show_review_message = False)
    return

label casual_hotwife_blowjob_text_label(the_person):
    mc.name "So... how did it go with the pictures?"
    "[the_person.possessive_title] gives you a quick smile."
    the_person.char "Well, I sent them off to him before I left the bar the other night, and I got an almost immediate response. 'Come home now'. No explanation or anything..."
    the_person.char "At first I got really scared. Did I just completely fuck up? So I went straight home..."
    the_person.char "When I got home, he was waiting for me... He umm... he handcuffed with my hands behind my back... I didn't even know he had handcuffs!"
    "Her voice is starting to get excited as she recounts some of the details."
    the_person.char "He forced me down on my knees and then said... he said that I was a dirty little slut, and that after using my mouth on another man he would have to... reclaim it."
    the_person.char "So I opened up and I let him use my mouth... god I never could have imagined my husband doing that to me could be so hot."
    the_person.char "Now... I'm a good wife... I've always, you know, swallowed for him. But this time..."
    "Her voice trails off a bit as she recalls the details. A smile on her face."
    the_person.char "I've never, ever had so swallow soooooo much. It was so hot, like a firehose it just kept cumming..."
    "You shift uncomfortably. This story is starting to turn you on!"
    $ mc.change_arousal (20)
    the_person.char "Haaa... sorry! I probably should have just said that it went well."
    mc.name "No it is quite alright. I was a little concerned with how things would go for you, but I'm glad that it turned out well!"
    $ the_person.draw_person(position = "stand4", emotion = "happy")
    the_person.char "It really did! So uhh, wanna go again, just ask. I'd be happy to be. BUT, we need to set some ground rules first!"
    mc.name "Okay, I'm down for that."
    the_person.char "Okay, well, like I said. I'm a good wife! I love my husband. If things between us ever start to get... you know... serious? I'm going to have to break it off."
    "You nod in understanding."
    the_person.char "If you try to make me choose between you two, I'll choose him, everytime. So lets just keep this casual, okay?"
    mc.name "Sounds good. Purely physical. I'm completely okay with that."
    the_person.char "Right... here, let's exchange numbers. I'll text you and if we're both free, we can screw around, no strings attached!"
    "You agree. You and [the_person.title] exchange numbers."
    the_person.char "Okay, well, I need to get going. I'm sure I'll see you around soon..."
    "You say goodbye and head out. Hot damn! You are now friends with benefits with a hot wife. You bet the sex is going to be amazing..."
    $ the_person.event_triggers_dict["hotwife_blowjob_text_enable"] = 0
    if casual_sex_add_person_to_list(the_person):
        "You now have [the_person.title]'s phone number. She may call you from time to time to hookup!"
    else:
        "DEBUG: Did not suc cessfully get phone number. Whoops!"

    return

#CSH20
label casual_hotwife_dancing_sex_label(the_person):
    "This scene is not yet written!"

    return

#CSH30
label casual_hotwife_sex_invite_label(the_person):
    "This scene is not yet written!"

    return

#CSH40
label casual_hotwife_her_place_label(the_person):
    "This scene is not yet written!"


    return

#CSH50
label casual_hotwife_home_sex_label(the_person):
    "This scene is not yet written!"


    return

#************* Personality****************#
#Override some of her personality functions so that her conversation options makes sense.

init 1301 python:              #Because Vren Init personality functionns at 1300



    def hotwife_titles(the_person):
        valid_titles = []
        valid_titles.append(the_person.name)
        if the_person.sluttiness > 40:
            valid_titles.append("Slutwife")
        return valid_titles

    def hotwife_possessive_titles(the_person):
        valid_possessive_titles = [the_person.title]

        if the_person.sluttiness > 60:
            valid_possessive_titles.append("The Slutwife")
            valid_possessive_titles.append("Your Swinging Slut")

        if the_person.sluttiness > 100:
            valid_possessive_titles.append("The Bar Cumdump")
        return valid_possessive_titles
    def hotwife_player_titles(the_person):
        return mc.name
    hotwife_personality = Personality("hotwife", default_prefix = "wild",
    common_likes = [],
    common_sexy_likes = ["casual sex"],
    common_dislikes = ["relationships"],
    common_sexy_dislikes = [],
    titles_function = hotwife_titles, possessive_titles_function = hotwife_possessive_titles, player_titles_function = hotwife_player_titles)




#************* Personality labels***************#


label hotwife_greetings(the_person):
    if mc.location == downtown_bar:
        if the_person.love > 50:  #She loves you too much and is going to or already has called things off
            the_person.char "Oh... hello [the_person.mc_title]"
            return
        if the_person.event_triggers_dict.get("hotwife_progress", 0) >= 2:
            the_person.char "Hey there [the_person.mc_title]"
            the_person.char "You want to umm, you know, meet me in the back? I'm sure that's why you're here..."
        else:
            the_person.char "Hey there!"

    elif the_person.sluttiness > 60:
        if the_person.obedience > 130:
            the_person.char "Hello [the_person.mc_title], it's good to see you."
        else:
            the_person.char "Hey there handsome, feeling good?"
    else:
        if the_person.obedience > 130:
            the_person.char "Hello [the_person.mc_title]."
        else:
            the_person.char "Hey there!"
    return

label hotwife_sex_responses(the_person):
    if the_person.sluttiness > 50:
        if the_person.obedience > 130:
            the_person.char "Oh my, keep doing that please!"
        else:
            the_person.char "Fuck it feels good when you do that. Keep going!"
    else:
        "[the_person.title] closes her eyes and moans quietly to herself."
    return

label hotwife_climax_responses(the_person):
    if the_person.sluttiness > 70:
        the_person.char "I'm going to cum! Ah! Make me cum [the_person.mc_title], I want to cum so badly! Ah!"
        "She closes her eyes and squeals with pleasure."
    else:
        the_person.char "Ah! I'm cumming! Oh fuck! Ah!"
    the_person.char "Fuck I hope daddy does this to me again later!"
    return

label hotwife_clothing_accept(the_person):
    if the_person.obedience > 130:
        the_person.char "It's for me? Thank you [the_person.mc_title], I'll add it to my wardrobe."
    else:
        the_person.char "Thanks [the_person.mc_title]! I wonder if daddy would like to see me in this too."
    return

#label hotwife_clothing_reject(the_person):
#    if the_person.obedience > 130:
#        the_person.char "Is that really for me [the_person.mc_title]? I want to... but I don't think I could wear that without getting in some sort of trouble."
#    else:
#        if the_person.sluttiness > 60:
#            the_person.char "Wow. I'm usually up for anything but I think that's going too far."
#        else:
#            the_person.char "Wow. It's a little... skimpy. I don't think I could wear that."
#    return

# label hotwife_clothing_review(the_person):
#     if mc.location == downtown_bar:
#         if the_person.sluttiness > 40:
#             the_person.char "I love when you look at me like that, but I don't think the downtown_bar staff would appreciate it as much. I'd better clean up a bit."
#         else:
#             the_person.char "I'd better clean up some before I go to leave the downtown_bar..."
#     elif the_person.obedience > 130:
#         the_person.char "I'm sorry [the_person.mc_title], you shouldn't have to see me like this. I'll go and get cleaned up so I'm presentable again."
#     else:
#         if the_person.sluttiness > 40:
#             the_person.char "Whew, I think we messed up my clothes a bit. Just give me a quick second to get dressed into something more decent."
#         else:
#             the_person.char "My clothes are a mess! I'll be back in a moment, I'm going to go get cleaned up."
#     return

#label hotwife_strip_reject(the_person):
#    if the_person.obedience > 130:
#        the_person.char "I'm sorry, but can we leave that where it is for now?"
#    elif the_person.obedience < 70:
#        the_person.char "Slow down there, I'll decide when that comes off."
#    else:
#        the_person.char "I think that should stay where it is for now."
#    return

# label hotwife_sex_accept(the_person):
#     if the_person.sluttiness > 70:
#         if the_person.obedience < 70:
#             the_person.char "I was just about to suggest the same thing."
#         else:
#             the_person.char "Mmm, you have a dirty mind [the_person.mc_title], I like it."
#     else:
#         the_person.char "Okay, we can give that a try."
#     return

label hotwife_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Oh god [the_person.mc_title], I should really say no... but thinking about daddy doing this to me too gets me so hot!"
    else:
        if the_person.obedience > 130:
            the_person.char "Yes [the_person.mc_title], if that's what you want to do I'll give it a try."
        else:
            the_person.char "I... Okay, if you really want to, lets give it a try."
    return

# label hotwife_sex_gentle_reject(the_person):
#     if the_person.sluttiness > 50:
#         the_person.char "Wait, I don't think I'm warmed up enough for this [the_person.mc_title]. How about we do something else first?"
#     else:
#         the_person.char "Wait. I don't think I'm comfortable with this. Could we just do something else instead?"
#     return

label hotwife_sex_angry_reject(the_person):
    if the_person.sluttiness < 20:
        the_person.char "What the fuck! Do you think I'm just some whore who puts out for anyone who asks?"
        the_person.char "Not even daddy asks me to do that! Get the fuck away from me."
    else:
        the_person.char "What the fuck do you think you're doing, that's disgusting!"
        the_person.char "Not even daddy asks me to do that! Get the fuck away from me."
    return

label hotwife_seduction_response(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            the_person.char "Yes [the_person.mc_title]? Want to take some pics together?"
        else:
            the_person.char "Yes [the_person.mc_title]? Is there something I can help you with?"
    else:
        if the_person.sluttiness > 50:
            the_person.char "Mmm, I know that look. Do you want to fool around a little?"
        elif the_person.sluttiness > 10:
            the_person.char "Oh, do you see something you like?"
        else:
            the_person.char "Oh, I don't really know what to say [the_person.mc_title]..."
    return

# label hotwife_seduction_accept_crowded(the_person):
#     if mc.location == downtown_bar:
#         if the_person.sluttiness < 20:
#             the_person.char "I suppose we could sneak away into the locker room... There's nothing wrong with that, right?"
#         elif the_person.sluttiness < 70:
#             the_person.char "Come on, let's sneak into the locker room and do it!"
#         else:
#             the_person.char "Oh fuck that sounds nice. I'm not sure I can wait until we sneak into the locker room, maybe we should just do it right here!"
#         return
#
#     if the_person.sluttiness < 20:
#         the_person.char "I suppose we could sneak away for a few minutes. There's nothing wrong with that, right?"
#     elif the_person.sluttiness < 50:
#         the_person.char "Come on, let's go find someplace quiet where we won't be interupted."
#     else:
#         the_person.char "No point waisting any time then, right? Let's get to it!"
#     return

# label hotwife_seduction_accept_alone(the_person):
#     if mc.location == downtown_bar:
#         if the_person.sluttiness < 20:
#             the_person.char "Well, there's nobody around to see us..."
#         elif the_person.sluttiness < 50:
#             the_person.char "I can't believe how empty the gym is right now. Let's do it right here!"
#         else:
#             the_person.char "Oh [the_person.mc_title], the gym is empty, fuck me now!"
#         return
#     if the_person.sluttiness < 20:
#         the_person.char "Well, there's nobody around to stop us..."
#     elif the_person.sluttiness < 50:
#         the_person.char "Mmm, that's a fun idea. Come on, let's get to it!"
#     else:
#         the_person.char "Oh [the_person.mc_title], don't make me wait!"
#     return

#label hotwife_seduction_refuse(the_person):
#    if the_person.sluttiness < 20:
#        "[the_person.title] blushes and looks away from you awkwardly."
#        the_person.char "I, uh... Sorry [the_person.mc_title], I just don't feel that way about you."
#
#    elif the_person.sluttiness < 50:
#        the_person.char "Oh, it's tempting, but I'm just not feeling like it right now. Maybe some other time?"
#        "[the_person.title] smiles and gives you a wink."
#
#    else:
#        the_person.char "It's so, so tempting, but I don't really feel up to it right now [the_person.mc_title]. Hold onto that thought though."
#    return

label hotwife_flirt_response(the_person):
    if mc.location == downtown_bar:
        if the_person.love > 50:  #She loves you too much and is going to or already has called things off
            the_person.char "Didn't your mother ever tell you its rude to hit on a married woman?"
            return
        if the_person.event_triggers_dict.get("hotwife_progress", 0) >= 2:
            the_person.char "Well why don't you meet me in the back in a bit and we'll see what happens?"
        else:
            the_person.char "Hey, maybe if you buy me a drink first."
            "[the_person.title] gives you a wink and smiles."
        return

    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            the_person.char "If that's what you want I'm sure I could help with that [the_person.mc_title]."
        else:
            the_person.char "Thank you for the compliment, [the_person.mc_title]."
    else:
        if the_person.sluttiness > 50:
            the_person.char "Mmm, if that's what you want I'm sure I could find a chance to give you a quick peak."
            "[the_person.title] smiles at you and spins around, giving you a full look at her body."
        else:
            the_person.char "Hey, maybe if you buy me dinner first."
            "[the_person.title] gives you a wink and smiles."
    return

label hotwife_hookup_rejection(the_person):
    the_person.char "Your loss! Just thinking about you makes me want to get on my knees, and you could have had some of this..."
    return

#label hotwife_cum_face(the_person):
#    if the_person.obedience > 130:
#        if the_person.sluttiness > 60:
#            the_person.char "Do I look cute covered in your cum, [the_person.mc_title]?"
#            "[the_person.title] licks her lips, cleaning up a few drops of your semen that had run down her face."
#        else:
#            the_person.char "I hope this means I did a good job."
#            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
#    else:
#        if the_person.sluttiness > 80:
#            the_person.char "Ah... I love a nice, hot load on my face. Don't you think I look cute like this?"
#        else:
#            the_person.char "Fuck me, you really pumped it out, didn't you?"
#            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
#    return

label hotwife_cum_mouth(the_person):
    if mc.location == downtown_bar:
        if the_person.sluttiness > 80:
            the_person.char "Your cum tastes great [the_person.mc_title]! I bet I get another tasty load later..."
            "[the_person.possessive_title] winks at you as she swallows your cum."
        elif the_person.sluttiness > 50:
            the_person.char "Thanks [the_person.mc_title]. I hope daddy cums in my mouth later too!"
        else:
            "[the_person.title]'s face grimaces as she tastes your sperm in her mouth."
            the_person.char "Thank you [the_person.mc_title]. It doesn't taste the best, but I'm always a good little slut."
    elif the_person.obedience > 130:
        if the_person.sluttiness > 60:
            the_person.char "That was very nice [the_person.mc_title], thank you."
        else:
            "[the_person.title]'s face grimaces as she tastes your sperm in her mouth."
            the_person.char "Thank you [the_person.mc_title], I hope you had a good time."
    else:
        if the_person.sluttiness > 80:
            the_person.char "Your cum tastes great [the_person.mc_title], thanks for giving me so much of it."
            "[the_person.title] licks her lips and sighs happily."
        else:
            the_person.char "Bleh, I don't know if I'll ever get use to that."
    return

#label hotwife_suprised_exclaim(the_person):
#    $rando = renpy.random.choice(["Fuck!","Shit!","Oh fuck!","Fuck me!","Ah! Oh fuck!", "Ah!", "Fucking tits!", "Holy shit!", "Fucking shit!"])
#    the_person.char "[rando]"
#    return

# label hotwife_talk_busy(the_person):
#     if mc.location == downtown_bar:
#         the_person.char "Hey, I'm really sorry but I need to keep on the lookout. Maybe another time?"
#     if the_person.obedience > 120:
#         the_person.char "Hey, I'm really sorry but I've got some stuff I need to take care of. Could we catch up some other time?"
#     else:
#         the_person.char "Hey, sorry [the_person.mc_title] but I've got some stuff to take care of. It was great talking though!"
#     return

#label hotwife_sex_strip(the_person):
#    if the_person.sluttiness < 20:
#        if the_person.arousal < 50:
#            the_person.char "Let me get this out of the way..."
#        else:
#            the_person.char "Let me get this out of the way for you..."
#
#    elif the_person.sluttiness < 60:
#        if the_person.arousal < 50:
#            the_person.char "This is just getting in the way..."
#        else:
#            the_person.char "Ah... I need to get this off."
#
#    else:
#        if the_person.arousal < 50:
#            the_person.char "Let me get this worthless thing off..."
#        else:
#            the_person.char "Oh god, I need all of this off so badly!"

#    return

# label hotwife_sex_watch(the_person, the_sex_person, the_position):
#     if the_person.sluttiness < the_position.slut_requirement - 20:
#         $ the_person.draw_person(emotion = "angry")
#         the_person.char "Holy shit, are you really doing this in front of everyone?"
#         $ the_person.change_obedience(-2)
#         $ the_person.change_happiness(-1)
#         "[the_person.title] looks away while you and [the_sex_person.name] [the_position.verb]."
#
#     elif the_person.sluttiness < the_position.slut_requirement - 10:
#         $ the_person.draw_person()
#         $ the_person.change_happiness(-1)
#         "[the_person.title] tries to avert her gaze while you and [the_sex_person.name] [the_position.verb]."
#
#     elif the_person.sluttiness < the_position.slut_requirement:
#         $ the_person.draw_person()
#         the_person.char "Oh my god, you two are just... Wow..."
#         $ change_report = the_person.change_slut_temp(1)
#         "[the_person.title] averts her gaze, but keeps glancing over while you and [the_sex_person.name] [the_position.verb]."
#
#     elif the_person.sluttiness > the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
#         $ the_person.draw_person()
#         the_person.char "Oh my god that's... Wow that looks...Hot."
#         $ change_report = the_person.change_slut_temp(2)
#         "[the_person.title] watches you and [the_sex_person.name] [the_position.verb]."
#
#     else:
#         $ the_person.draw_person(emotion = "happy")
#         the_person.char "Come on [the_person.mc_title], you can give her a little more than that. I'm sure she can handle it."
#         "[the_person.title] watches eagerly while you and [the_sex_person.name] [the_position.verb]."
#
#     return

# label hotwife_being_watched(the_person, the_watcher, the_position):
#     if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
#         #They agree you should give it to her harder
#         the_person.char "I can handle it [the_person.mc_title], you can be rough with me."
#         $ the_person.change_arousal(1)
#         "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."
#
#     elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
#         #She's super slutty and doesn't care what people think.
#         the_person.char "Don't listen to [the_watcher.title], I'm having a great time. Look, she can't stop peeking over."
#
#     elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
#         #She's super slutty and encourages the watcher to be slutty.
#         $ the_person.change_arousal(1)
#         "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."
#
#     elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
#         #She's into it and encouraged by the slut watching her.
#         the_person.char "Oh god, having you watch us like this..."
#         $ the_person.change_arousal(1)
#         "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."
#
#     elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
#         #She's into it but shamed by the prude watching her.
#         the_person.char "[the_person.mc_title], maybe we shouldn't be doing this here..."
#         $ the_person.change_arousal(-1)
#         $ the_person.change_slut_temp(-1)
#         "[the_person.title] seems uncomfortable with [the_watcher.title] nearby."
#
#     else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
#         #They're both into it but not fanatical about it.
#         the_person.char "Oh my god, having you watch us do this feels so dirty. I think I like it!"
#         $ the_person.change_arousal(1)
#         $ the_person.change_slut_temp(1)
#         "[the_person.title] seems more comfortable [the_position.verb]ing you with [the_watcher.title] around."
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
#         if the_person.sluttiness > 50:
#             "[the_person.title] looks up from her work when you enter the room."
#             the_person.char "Hey [the_person.mc_title]. Let me know if you need any help with anything. Anything at all."
#             "She smiles and winks, then turns back to what she was doing."
#         else:
#             "[the_person.title] turns to you when you enter the room and shoots you a smile."
#             the_person.char "Hey, good to see you!"
#
#     else:
#         if the_person.obedience < 90:
#             "[the_person.title] glances up from her work."
#             the_person.char "Hey, how's it going?"
#         else:
#             "[the_person.title] waves at you as you enter the room."
#             the_person.char "Hey, let me know if you need anything [the_person.mc_title]."
#     return

# label hotwife_date_seduction(the_person):
#     if the_person.sluttiness > the_person.love:
#         if the_person.sluttiness > 40:
#             the_person.char "I had a great time [the_person.mc_title], but I can think of a few more things we could do together. Want to come back to my place?"
#             # the_person.char "I had a great night [the_person.mc_title], would you like to come back to my place and let me repay the favour?"
#         else:
#             the_person.char "I had a really good time tonight [the_person.mc_title]. I don't normally do this but... would you like to come back to my place?"
#             #the_person.char "I had a great night [the_person.mc_title], but I don't see why it should end here. If you want to come back to my place I can think of a few things we could do."
#     else:
#         if the_person.love > 40:
#             the_person.char "You're such great company [the_person.mc_title]. Would you like to come back to my place and spend some more time together?"
#         else:
#             the_person.char "I had a great night [the_person.mc_title]. Would you like to come back to my place for a quick drink?"
#     return

## Role Specific Section ##
# label hotwife_improved_serum_unlock(the_person):
#     mc.name "[the_person.title], now that you've had some time in the lab there's something I wanted to talk to you about."
#     the_person.char "Okay, how can I help?"
#     mc.name "All of our research and development up until this point has been based on the limited notes I have from my university days. I'm sure there's more we could learn, and I want you to look into it for me."
#     "[the_person.title] smiles mischievously."
#     the_person.char "I've got an idea that you might want to hear then. It's not the most... orthodox testing procedure but I think it is nessesary if we want to see rapid results."
#     mc.name "Go on, I'm interested."
#     the_person.char "Our testing procedures focus on human safety, which I'll admit is important, but it doesn't leave us with much information about the subjective effects of our creations."
#     the_person.char "What I want to do is take a dose of our serum myself, then have you record me while you run me through some questions."
#     return

#</editor-fold>
