init -1 python:
    def SB_get_breeding_score(the_person):
        breeding_score = 0
        for breedListEntry in FETISH_BREEDING_OPINION_LIST:
            breeding_score += the_person.get_opinion_score(breedListEntry)

        return breeding_score


#Requirement functions
    def breeding_fetish_employee_intro_requirement():
        return True


#Other breeding fetish calls
init 3 python:
    def add_breeding_fetish(person):
        person.add_role(breeding_fetish_role)
        person.update_sex_skill("Vaginal", 6)
        person.event_triggers_dict["LastBreedingFetish"] = day
        add_breed_me_collar_to_base_outfit(person)
        return


#Fetish Intro Labels
label breeding_fetish_employee_intro_label(the_person):
    "You are finishing up the last of your work today and closing up. All your employees should be gone for the day."
    "However, you are surprised when you are interrupted by someone."
    $ the_person.draw_person()
    the_person.char "Ah! [the_person.mc_title]... I was hoping to catch you alone. I need to talk to you about something."
    mc.name "Good evening [the_person.title]. What can I do for you?"
    the_person.char "Ah... more like... what can you do to me..."
    "Did you hear that right?"
    mc.name "Oh?"
    the_person.char "I umm... I mean... sorry."
    "She looks a bit flustered for a second, but quickly gathers her thoughts and starts to talk to you."
    if the_person.age < 35:
        the_person.char "Well, you know sir, I'm still pretty young, and lately I've been dealing with some pretty instense biological... urges..."
    else:
        the_person.char "Well, you know sire, I'm starting to get a bit older, and as my biological clock is ticking I've been getting some pretty intense... urges..."
    the_person.char "I'm not sure why, but lately I've been having these fantasies about having sex, raw, over and over, and getting filled with cum!"
    "That's not surprising. Recently, you've been giving your employee serums that greatly increase her urges to reproduce..."
    if the_person.knows_pregnant():
        the_person.char "Obviously I'm already pregnant, but umm, I've really been craving your cock inside me, twitching and pulsing your loads deep, over and over..."
    else:
        the_person.char "I don't know how to say this but, I've been craving you, and your cock, twitching and pulsing load aftet load deep inside me! Knocking me up!"
    "The serums must really be effecting her, for her to be this forward with you. You decide to take advantage of the situation... and of her."
    "You get close to her. She wraps her arms around you as you get close."
    $ the_person.draw_person(position = "kissing")
    mc.name "So what you are saying is..."
    "You grab her ass and grope it, pushing into her."
    mc.name "... You wouldn't mind it if..."
    $ the_person.draw_person(position = "against_wall")
    "You roughly pick her up and slowly move her backwards."
    mc.name "... I just pushed you back..."
    "You keep her backing up until her ass runs into the edge of someone's desk."
    mc.name "... Onto this desk..."
    $ the_person.draw_person(position = missionary)
    "You force her down onto her back."
    the_person.char "Oh my god..."
    mc.name "...and fucked you..."
    if the_person.outfit.vagina_available():
        "You reach down and pull your cock out from your pants."
    else:
        "As you start to pull your cock out, [the_person.possessive_title] reaches down and starts pulling her clothes off."
        $ the_person.strip_outfit(exclude_upper = True)
    $ the_person.change_arousal (15)
    mc.name "... and pinned you down..."
    "You grab her hands and force them down at her sides. She has a wild look in her eye as your raw cock nears her cunt."
    mc.name "...and fucked your brains out..."
    "As you finish those words, your push yourself inside of her. She moans as it goes in."
    $ the_person.change_arousal (20)
    $ mc.change_arousal(15)
    mc.name "...and didn't stop until I dump my cum deep?"
    the_person.char "Oh god! Yes do it! Oh fuck!"
    "Still holding her hands down, you start to thrust rapidly. It's time to give this horny slut a creampie!"
    call fuck_person(the_person, start_position = breeding_missionary , private = True, skip_intro = True, hide_leave = True, position_locked = True) from _employee_gets_breeding_fetish_01
    if the_person.has_creampie_cum():
        the_person.char "Oh god! Its so deep! Oh thank you so much [the_person.mc_title]!"
    else:
        #TODO what to put here?
        pass
    $ add_breeding_fetish(the_person)
    if the_person.knows_pregnant():
        the_person.char "I don't care if I am already pregnant... Please do that again! My body was made to take your cum like that!"
    else:
        the_person.char "I hope that did it, but you'd better cum inside me again and again anyway!"
    "You slowly back away from [the_person.title], allowing her to get up."
    $ the_person.draw_person()
    "[the_person.possessive_title] slowly stands up, her legs are a little unsteady."
    mc.name "I need to get a few more things done before I close up the office. From now on, you are my breeding stock. Be ready to take my cum whenever I tell you to!"
    the_person.char "Yes! Yes sir! I'll be ready, don't worry!"
    $ the_person.draw_person()
    "You say goodbye to [the_person.title]."
    "[the_person.possessive_title] now has a fetish to get bred by you!"
    return

label breeding_fetish_mom_intro_label():
    $ the_person = mom
    # We'll start this exactly like the crisis with mom waking you up, but with definitely more urgency in her.
    # First we need to take her and remove enough clothing that we can get to her vagina, otherwise none of this stuff makes sense.
    # We do that by getting her lowest level pieces of bottom clothing and removing it, then working our way up until we can use her vagina.
    # This makes sure skirts are kept on (because this is suppose to be a quicky).
    $ bottom_list = the_person.outfit.get_lower_ordered()
    $ removed_something = False
    $ the_index = 0
    while not the_person.outfit.vagina_available() and the_index < __builtin__.len(bottom_list):
        $ the_person.outfit.remove_clothing(bottom_list[the_index])
        $ removed_something = True
        $ the_index += 1

    "You're woken up by your bed shifting under you and a sudden weight around your waist."
    "You feel a tug on your clothing, and you are slowly opening your eyes when you feel your morning wood spring free."
    $ the_person.draw_person(position = "cowgirl", emotion = "happy")
    "You open you eyes to see [the_person.possessive_title] lining you up with her pussy, before slowly sliding down on top of you."
    mc.name "Ooohh... good morning [the_person.title]."
    the_person.char "Ohhh... good morning honey! Mommy needs your seed inside her this morning... and I'm not taking no for an answer!"
    "You are a little surprised by her forcefulness. Lately you've been giving her serums that should make her a bit more submissive..."
    the_person.char "I had such vivid dreams last night... you were fucking me and kept cumming inside me over and over and over!"
    the_person.char "My belly started bigger and my tits started to leak milk and I loved it so much..."
    "Ahh, you've been giving her serums that increase her drive to reproduce. Looks like they've finally driven her over the urge and given her a breeding fetish!"
    $ the_person.change_arousal (30)
    $ mc.change_arousal(20)
    "She starts to rock her hips back and forth. You reach up and start to fondle her tits as they sway back and forth."
    mc.name "Mmmm, I can't wait to drink milk for your tits again, [the_person.title]."
    if the_person.knows_pregnant(): #She already knows she's pregnant
        the_person.char "Oh god I know I'm already pregnant, but I just want you to fuck your cum into me over and over!"
    else:
        the_person.char "Oh god, can we really do this? Will you fuck your cum into me over and over until I'm pregnant? I want that so bad!"
    mc.name "Of course I'll give you my cum. From now on, you'll by my own personal mare. I'll breed you every chance I get."
    $ the_person.change_arousal(15)
    the_person.char "Oh [the_person.mc_title], that's so hot... I want it now! I'm going the ride the cum out of you now!"
    call get_fucked(the_person, the_goal = "vaginal creampie", start_position = cowgirl, private = True, skip_intro = True, allow_continue = False) from _mom_breeding_fetish_intro_01
    if the_person.has_creampie_cum():
        the_person.char "Oh god... I need to keep it all in..."
        "[the_person.title] reaches her hand down, trying to keep your cum inside of her, but failing, as your cum drips down the inside of her thighs."
    else:
        #TODO what to put here?
        pass
    mc.name "Don't worry, I'll give you more soon."
    "She chuckles, then smiles at you."
    the_person.char "You better... Every day! Even if I am pregnant..."
    $ the_person.add_role(breeding_fetish_role)
    $ the_person.update_sex_skill("Vaginal", 6)
    $ the_person.event_triggers_dict["LastBreedingFetish"] = day
    $ add_breed_me_collar_to_base_outfit(the_person)
    the_person.char "It's good for the baby, I think! It knows when mommy is getting taken care of... How happy you make her..."
    $ the_person.draw_person(position = "missionary")
    "[the_person.title] lays down beside you for a while. Soon though, it is time to get up and ready for the day."
    the_person.char "Have a good day. Don't forget, try to be home for dinner tonight! You need to keep your energy up!"
    "You can hardly believe it. Your own mother now has a fetish to get bred by you!"

    return

label breeding_fetish_lily_intro_label():

    return

label breeding_fetish_rebecca_intro_label():

    return

label breeding_fetish_gabrielle_intro_label():

    return

label breeding_fetish_stephanie_intro_label():

    return

label breeding_fetish_starbuck_intro_label():
    $ the_person = starbuck
    "You get a text message from [the_person.possessive_title]."
    the_person.char "Hey, do you think you could help me close up the shop tonight? I have a few things I need help with."
    "You consider it. You don't have much else going on right now, so you decide to agree."
    mc.name "Sure, I'll be over shortly."
    "You make your way over to the sex shop."
    #TODO change background
    $ the_person.draw_person()
    "When you get to the store, you look around. It seems like the store is already pretty clean."
    mc.name "Good evening [the_person.title]. Still need help? Things look pretty good around here to me..."
    the_person.char "Hey [the_person.mc_title]! Thanks for coming. I'm almost done, but thought maybe you could we could just hang out for a bit."
    "Hmm, so she has ulterior motives for asking you here."
    mc.name "Certainly."
    "[the_person.possessive_title] locks the front door. She gets you a beer from her fridge and she grabs one for herself."
    "You make small talk for a bit. Finally, [the_person.title] starts to talk to you about why she asked you over."
    the_person.char "So... you are probably wondering why you are here. Today, something happened to me while I was working."
    the_person.char "This young couple came in, looking for some new lingerie. They needed new because the woman had umm... grown out of her clothing."
    the_person.char "She was... shall we say VERY pregnant. I think she was ready to pop any day!"
    if the_person.knows_pregnant():
        the_person.char "I know I'm already pregnant but... it was so hot! It made me realize how amazing it is to get bred."
    else:
        the_person.char "There was something about them though. They were practically glowing! And the way they looked at each other. I... I can't believe this, but it made me so jealous!"
        the_person.char "I've never had it quite this bad before... but it gave me this ITCH. I can't explain it, but I've been day dreaming all day about.. you know... being like that."
    if the_person.is_girlfriend():
        the_person.char "I know our relationship is kind of... unique... with how much older I am. But I don't think I've ever been so sure of something."
    else:
        the_person.char "I know its kind of weird, with how much older I am. But I don't think I've ever been more sure of something."
    the_person.char "Would you be my bull? Cum inside me... over and over... breed me like its your job!"
    the_person.char "I want to feel your seed inside me, every second of every day!"
    "Your cock is already hard, listening to [the_person.possessive_title] talk like this. You've been slipping her serums, and it looks like they've finally given her a breeding fetish."
    "It's time to seal the deal. If you give her what she wants now, she'll be begging you for creampies every chance she gets."
    mc.name "Okay. I'll give you my cum. Now turn around, I want to take you over the counter."
    $ the_person.change_arousal(8)
    the_person.char "Oh god, yes!"
    $ the_person.draw_person(position = "standing_doggy")
    "She turns around and bends over the counter, as you asked her to. You step close behind her."
    if the_person.outfit.vagina_available():
        "With her pussy already out and ready to be used, you waste no time getting your pants off. When you cock springs free, you using it smack her ass a couple times."
    else:
        "As you start to pull your cock out, [the_person.possessive_title] reaches back and starts to pull off the clothing covering her ass."
        $ the_person.strip_outfit(exclude_upper = True)
        "You give her ass a couple smacks with your cock."
    $ the_person.change_arousal(10)
    $ mc.change_arousal(10)
    "She wiggles her hips back and forth a bit, teasing you."
    the_person.char "Stick it in [the_person.mc_title]! Fuck me hard and cum as deep as you can!"
    "You grab her hips to stop the wiggling. You line yourself up with her thirsty cunt and push into her. She gasps when you bottom out."
    the_person.char "Oh yes! Give it to me good!"
    call fuck_person(the_person, start_position = bent_over_breeding , private = True, skip_intro = True, hide_leave = True, position_locked = True) from _starbuck_gets_breeding_fetish_01
    if the_person.has_creampie_cum():
        the_person.char "Oh god! Babymaking sex is so hot, I can't believe it..."
        "[the_person.title] reaches her hand back, trying to keep your cum inside of her, but failing, as your cum drips down the inside of her thighs."
    else:
        #TODO what to put here?
        pass
    $ add_breeding_fetish(the_person)
    if the_person.knows_pregnant():
        the_person.char "I don't care if I am already pregnant... Please do that again! My body was made to take your cum like that!"
    else:
        the_person.char "I hope that did it, but you'd better cum inside me again and again anyway!"
    $ the_person.draw_person()
    "[the_person.possessive_title] slowly stands up and turns to you."
    the_person.char "Wow... I'm glad I finished closing up before you got here..."
    $ the_person.draw_person(position = "kissing")
    "She draws you into a hug, then whispers in your ear."
    the_person.char "You can bend me over like that anytime... I don't even care if there are customers here when you do it..."
    $ the_person.draw_person()
    the_person.char "You go ahead, I have a couple more things to do before I go."
    "You say goodbye to [the_person.title]."
    "You can hardly believe it. The sex store owner [the_person.title] now has a fetish to get bred by you!"
    return

label breeding_fetish_sarah_intro_label():
    $ the_person = sarah
    $ mc.change_location(bedroom)
    $ mc.location.show_background()
    $ scene_manager = Scene()
    "As you are getting ready for bed, you get a text on your phone. It's from [the_person.possessive_title]"
    the_person.char "Hey, can I come over tonight? I had something I wanted to talk to you about."
    "You quickly text her back."
    mc.name "Sure. Want to spend the night?"
    the_person.char "Hell yeah! I'll bring some stuff over."
    "About 20 minutes later she texts you."
    the_person.char "Hey, I'm here! Come let me in!"
    "You head to your front door and open it."
    "For once, you managed to get her back to your room while avoiding [mom.possessive_title] and [lily.title]."
    $ scene_manager.add_actor(the_person, position = "sitting")
    "She walks over and sits on your bed."
    mc.name "So... what did you want to talk about?"
    "She clears her throat. You can tell she is a little nervous."
    if the_person.knows_pregnant():
        the_person.char "I know I'm already pregnant... and it is amazing really."
        the_person.char "But even after you got me pregnant, every time you finish inside me, I find myself craving it, more and more."
        the_person.char "The itch is getting so bad! I just want you to fill me up, over and over!"
        the_person.char "Even after the baby comes... I want my your seed planted deep in me as much as possible!"
        "This is quite a twist! You know you had started giving her pregnancy serums, and it sounds like they are starting to really have an effect."
        mc.name "I'll do it. From now on, you are my personal mare! I'll breed over and over, just like you want."
    else:
        the_person.char "Well, this is kind of hard to talk about. But... we've been having a lot of unprotected sex lately..."
        mc.name "Oh my god, are you pregnant?"
        the_person.char "No! No, not yet... that I know of anyway..."
        mc.name "Not... yet?"
        the_person.char "Well, [the_person.mc_title], it's been like a dream, having you back in my life like this. Things are amazing, being with you."
        the_person.char "I've been, well, tracking my cycles recently and, well, basically, I'm fertile right now."
        "You can feel your cock twitch in your pants. You imagine [the_person.possessive_title], knocked up, her tits swelling with milk and her belly growing..."
        the_person.char "Every time you finish inside me, I find myself thinking about it, more and more, what it would be like to get pregnant and have a baby with you."
        the_person.char "Look, you don't have to answer me right now, but, I thought maybe we could try and have a baby. Together?"
        the_person.char "I know this is crazy... but lately I've just had this almost overwhelming itch! I want you to knock me up and fill me over and over!"
        "This is quite a twist! You weren't expecting this so soon, but it seems the pregnancy serums you've been giving her are really working."
        mc.name "Honestly, I didn't realize this was something you were thinking about. But I would love to make a baby with you!"
    $ the_person.change_stats(happiness = 15, obedience = 10)
    the_person.char "Oh! Wow, I honestly... I thought you we're gonna say no! This is... I can't believe it."
    "She looks up at you, and you can see the changes in her facial expression. She goes from surprised, to happy, to sultry."
    the_person.char "So umm, what are you doing right now?"
    mc.name "I think we should get naked."
    the_person.char "Yes sir!"
    $ scene_manager.strip_actor_outfit(the_person, exclude_lower = False)
    "You get naked with [the_person.possessive_title]. She rolls on her back and spreads her legs."
    the_person.char "Come fill me up, [the_person.mc_title]!"
    call fuck_person(the_person, start_position = breeding_missionary, start_object = bedroom.get_object_with_name("bed"), skip_intro = False, girl_in_charge = False, position_locked = True) from _sarah_ask_for_baby_05
    if the_person.has_creampie_cum():
        the_person.char "Oh my god... we actually did it..."
        "She grabs an extra pillow and puts it under her butt so her hips are elevated."
        the_person.char "I'm just going to lay her like this for a bit, you know. Keep that seed nice and deep."
    else:
        mc.name "I'm sorry, I really want to, I'm just really tired."
        "You can tell she is a little disappointed."
        the_person.char "That's okay. Maybe in the morning?"
    "You snuggle up with [the_person.possessive_title]. Your serums have turned her into your personal breeding mare."
    $ add_breeding_fetish(the_person)
    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_sarah_breeding_request_5
    call Sarah_spend_the_night() from sarah_ask_for_baby_overnight_15

    return

label breeding_fetish_ophelia_intro_label():

    return

label breeding_fetish_erica_intro_label():

    return

label breeding_fetish_candace_intro_label(): #This is going to be two intros, depending on if candace is still a bimbo or not
    $ the_person = candace
    $ camera_person = None
    $ room_list = []
    if candace_is_bimbo(): #She is a bimbo.
        "As you step into the office, you see [the_person.possessive_title] looking over at you. She stands up and waves you over to her desk."
        $ the_person.draw_person()
        "You walk over to her."
        mc.name "Hello [the_person.title]. Something I can help you with?"
        the_person.char "Yeah boss! I'm having trouble concentrating on my work this morning. Could you help me?"
        mc.name "Possibly, what seems to be distracting you?"
        the_person.char "Last night, I was like, totally watching porn, but I couldn't get off to the usual stuff. I was starting to get frustrated, until I finially found something that worked!"
        the_person.char "I found this video where like, the first half of it is this hottie getting railed and the guy cums in her, and then the second half she's like 8 months pregnant!"
        the_person.char "You could totally tell it was her too because like, she had the same tattoo and everything!"
        the_person.char "I went back and watched the first half again and came so hard, thinking about how that was how she got knocked up!"
        mc.name "That... sounds like a great a video, but I'm not sure what I can help you with."
        if the_person.knows_pregnant():
            the_person.char "I know that like, I'm already knocked up, OBVIOUSLY. But like, maybe we could make a video like that too?"
            the_person.char "You could just like, keep fucking babies into me non stop and every time you cum inside me, its like, this could be the time!"
            mc.name "You want me to keep getting you pregnant?"
            the_person.char "Like, over and over! That sound so hot!"
        else:
            the_person.char "I was thinking like, maybe we could do that! Take a video of you cumming inside me and knocking me up!"
            mc.name "You want me to get you pregnant?"
            the_person.char "Fuck yeah! That's like, so hot! And can you imagine having that on video? Holy fuck!"
        "Lately, you've been slipping her serums to increase her drive to reproduce. Unsurpisingly, it sounds like she has developed a breeding fetish."
        mc.name "Okay. I'll give you my cum. Now turn around, I'm going to take you over your desk."
        if len(mc.location.people) == 1:
            "You look around the room, but no one else is around to record it, so you set up your phone to record and prop it up on a nearby desk as best you can."
        else:
            python:
                room_list = mc.location.people.copy()
                room_list.remove(the_person)
                camera_person = get_random_from_list(room_list)
            "You look around the room. You notice that another employee has overheard the conversation and is looking at you with some interest."
            mc.name "[camera_person.title], come here."
            $ camera_person.draw_person()
            camera_person.char "Yes?"
            mc.name "Take this, I need you to take a video for me."
            camera_person.char "Oh wow... you're really going to...? Right here?"
            "You nod and hand her your phone, with it set to video mode."
        "You turn back to [the_person.possessive_title]."
        $ the_person.draw_person(position = "standing_doggy")
        if the_person.outfit.vagina_available():
            "With her pussy already out and ready to be used, you waste no time getting your pants off. When you cock springs free, you using it smack her ass a couple times."
        else:
            "As you start to pull your cock out, [the_person.possessive_title] reaches back and starts to pull off the clothing covering her ass."
            $ the_person.strip_outfit(exclude_upper = True)
            "You give her ass a couple smacks with your cock."
        $ the_person.change_arousal(10)
        $ mc.change_arousal(10)
        mc.name "Are you ready to get bred, bitch?"
        "[the_person.title] keeps trying to back herself up onto you, but you move your dick around, frustrating her."
        the_person.char "Just, like, put it in me already!"
        mc.name "I want to hear you beg."
        the_person.char "PUT IT IN AND FUCK ME AND BREED ME AND CUM OVER AND OVER DEEP MAKE ME YOUR CUM DUMPSTER PLEASE PLEASE PLEASE!!!"
        "Wow, that didn't take much encouragement. You grab her hips, line yourelf up and push yourself in deep."
        the_person.char "Yes!!!"
        call fuck_person(the_person, start_position = bent_over_breeding , private = False, skip_intro = True, hide_leave = True, position_locked = True) from _bimbo_candace_gets_breeding_fetish_01
        if the_person.has_creampie_cum():
            "[the_person.title] reaches her hand back, rubbing the cum that has started to drip out of her all around her slit, playing with it."
        else:
            #TODO what to put here?
            pass
        if camera_person == None:
            "You grab your phone off the desk and stop the video. You quickly put it in an email to [the_person.title] so she can have a copy of it."
        else:
            camera_person.char "Wow..."
            "You grab your phone from [camera_person.title] and thank her for her help. You quickly put the video in an email to [the_person.title] so she can have a copy of it."

        if the_person.knows_pregnant():
            the_person.char "I don't care if I am already pregnant... Please do that again! My body was made to take your cum like that!"
        else:
            the_person.char "I hope that did it, but you'd better cum inside me again and again anyway!"
        $ the_person.draw_person()
        "[the_person.possessive_title] slowly stands up and turns to you."
        the_person.char "Did you, like... get the video?"
        mc.name "A copy should be in your email shortly."
        if the_person.knows_pregnant():
            the_person.char "We'll have to like, make more! You know, when you are ACTUALLY knocking me up, not just practicing!"
        else:
            the_person.char "Don't forget, I want another like, when my belly is all big and my titties are spraying milk everywhere!"
        mc.name "I'll make sure it happens. Do you think you can concentrate on your work now?"
        the_person.char "Yes sir! I'll get back to work!"
        $ add_breeding_fetish(the_person)
        "You step away from her desk, letting her get back to her work. You notice her humming a happy tune as you walk away."
        "You can hardly believe it. [the_person.possessive_title] now has a fetish to get bred by you!"
        return
    else:
        "This story is not yet written." #TODO this branch
    return

label breeding_fetish_ashley_intro_label():

    return

label breeding_fetish_high_fertility_crisis_label():


    return
