init 1 python:
    #Requirement functions

    def anal_fetish_employee_intro_requirement():
        if time_of_day == 3:
            if mc.business.is_open_for_business():
                if mc.is_at_work():
                    return True
        return False


    def anal_fetish_family_intro_requirement():
        if the_person.location == the_person.home:
            if the_person.location.get_person_count() == 1: #She is alone in her bedroom
                return True
        return False

    def anal_fetish_generic_intro_requirement():
        return False

    def anal_fetish_mom_intro_requirement():
        return False

    def anal_fetish_lily_intro_requirement():
        if time_of_day == 3 and mc.business.is_open_for_business() and mc.is_at_work():
            return True
        return False

    def anal_fetish_rebecca_intro_requirement():
        return False

    def anal_fetish_gabrielle_intro_requirement():
        return False

    def anal_fetish_stephanie_intro_requirement():
        return False

    def anal_fetish_alex_intro_requirement():
        return False

    def anal_fetish_nora_intro_requirement():
        return False

    def anal_fetish_emily_intro_requirement():
        return False

    def anal_fetish_christina_intro_requirement():
        return False

    def anal_fetish_starbuck_intro_requirement():
        return False

    def anal_fetish_sarah_intro_requirement():
        return False

    def anal_fetish_ophelia_intro_requirement():
        return False

    def anal_fetish_candace_intro_requirement():
        return False

    def anal_fetish_dawn_intro_requirement():
        return False

    def anal_fetish_erica_intro_requirement():
        return False

    def anal_fetish_ashley_intro_requirement():
        return False

    def add_fuck_doll_collar_to_base_outfit(person):
        person.base_outfit.remove_all_collars()

        fd_collar = fuck_doll_collar.get_copy()
        fd_collar.colour = [.41,.16,.38,.9]
        fd_collar.pattern = "Pattern_1"
        fd_collar.colour_pattern = [.95,.95,.95,.9]
        person.base_outfit.add_accessory(fd_collar)
        return

init 2 python: #Other anal fetish related python code
    anal_fetish_employee_intro = Action("Employee Anal Fetish Intro", anal_fetish_employee_intro_requirement, "anal_fetish_employee_intro_label")
    anal_fetish_generic_intro = Action("Generic Anal Fetish Intro", anal_fetish_generic_intro_requirement, "anal_fetish_generic_intro_label")
    anal_fetish_family_intro = Action("Family Anal Fetish Intro", anal_fetish_family_intro_requirement, "anal_fetish_family_intro_label")
    anal_fetish_lily_intro = Action("Lily Anal Fetish Intro", anal_fetish_lily_intro_requirement, "anal_fetish_lily_intro_label")

    def add_anal_fetish(person):
        person.add_role(anal_fetish_role)
        person.update_sex_skill("Anal", 6)
        person.event_triggers_dict["LastAnalFetish"] = day
        add_fuck_doll_collar_to_base_outfit(person)
        return




### Function labels

label anal_fetish_employee_intro_label():
    $ fetish_after_hours_unlock()
    "You are just finishing up with business for the day. As you are closing up your workstation, something is bothering you."
    "You couldn't help but notice one of your employees, [the_person.title], has been acting a little bit... different."
    "She seems to be using her ass to try and get attention."
    "Even now, as you walk around he business in your closing rounds, [the_person.possessive_title] bends over her desk when she notices you are nearby."

    $ the_person.draw_person(position = "standing_doggy")
    "She tries to pretend like she doesn't notice you, but you notice subtle shifts in her hips, wiggling a bit as you walk by her."
    "[the_person.possessive_title] has been doses recently with some of your anal enhancing serums. You wonder if she is ready to awaken a new love of anal sex."
    if the_person in unique_character_list:
        "Warning, this character is unique, and may have unique fetish dialogue. If you continue, you may miss this dialogue!"
    menu:
        "Attempt to train her anal fetish" if mc.energy > 40:
            pass
        "Too tired" if mc.energy <= 40:
            pass
            #TODO re add the event for this person for the next day.
        "Too risky, leave her alone":
            "You decide to leave her alone for now. You might revisit this decision at a later date."
            $ fetish_after_hours_unlock()
            $ clear_scene()
            return
    mc.name "Hello [the_person.title]."
    the_person "Hey [the_person.mc_title]! Its good to see you!"
    $ the_person.draw_person(position = the_person.idle_pose)
    "She quickly stands up and turns to you. You take a deep breath. Its time to take the plunge."
    mc.name "[the_person.title], are busy today? I have something I could use your help with after we close up."
    the_person "Oh! I suppose I could stay for a bit. Let me just finish this up. Want to meet in your office?"
    "It's clear from the tone of her voice she's hoping for some personal attention."
    mc.name "That sounds perfect. See you there."
    $ clear_scene()
    $ ceo_office.show_background()
    "You head to your office and wait a few minutes. Shortly after you hear a knock at the door."
    $ the_person.draw_person()
    ###Draw the girl###
    mc.name "Come in. Please have a seat."
    $ the_person.draw_person(position = "sitting")
    "As she sits down, she starts to fidgit a bit."
    mc.name "First off, I want you to know that you aren't in trouble. That isn't why I asked you here."
    the_person "Okay..."
    mc.name "I've noticed you've been acting a bit different lately whenever I am around. Bending over, wiggling your hips at me."
    the_person "I... sir its not..."
    if the_person.has_taboo("anal_sex"):
        mc.name "I was wondering if you've ever tried anal before. It's clear that it is something that is on your mind."
    else:
        mc.name "I was wondering if you want a round of anal. It is clear to me that your ass needs some attention."
    "[the_person.title] laughs a little."
    the_person "Oh! I umm... I suppose I would be up for something like that."
    "You stand up and start to walk around the desk toward [the_person.possessive_title]."
    mc.name "You aren't fooling anyone [the_person.title]. Your body langage is practically begging for it."
    mc.name "Now get up and bend over the desk so I can get a good look."
    the_person "Oh my god..."
    $ the_person.draw_person(position = "standing_doggy")
    if the_person.vagina_available():
        "You give her ass a smack, admiring the way her cheeks wobble."
    else:
        mc.name "Let's get this out of the way first."
        $ the_person.strip_outfit(exclude_upper = True)
        "Once you've got her clothing out of the way, you give her ass a smack, admiring the way her cheeks wobble."
    $ the_person.change_arousal(15)
    the_person "Mmm... like the view?"
    mc.name "I love it."
    "[the_person.title] moans as you firmly knead her ass for a bit."
    $ the_person.change_arousal(15)
    "You slide your fingers down betwee her cheeks and find her cunt just starting to leak a bit of moisture."
    mc.name "Wow, you really like this kind of attention don't you."
    "[the_perosn.possessive_title] can only moan as you slide two fingers inside her cunt. With your other hand you give her another spank."
    $ the_person.change_arousal(10)
    mc.name "There, that should be good."
    "You remove yor fingers briefly, then bring them up slightly. She sighs as you wiggle them around her puckered hole."
    "You push against her. Your fingers easily begin to slip into [the_person.possessive_title]'s back door."
    $ the_person.change_arousal(20)
    the_person "Oh fuck..."
    "[the_person.title]'s knees buckle a bit as you begin to work your fingers in and out of her."
    mc.name "Do you like it?"
    the_person "God yes... keep going!"
    $ the_person.change_arousal(15)
    "[the_person.possessive_title]'s breathing is getting erratic as you finger fuck her asshole for a minute or two."
    the_person "I didn't know... I didn't know it could be this good!"
    $ the_person.change_arousal(15)
    "[the_person.title]'s arousal is beginning to run down the inside of her thighs. She is REALLY getting off on this!"
    "You double your efforts in an attempt to get her to cum from just your fingers."
    the_person "Oh... OH! Don't stop!"
    $ the_person.change_arousal(20)
    "[the_person.possessive_title]'s whole body quivers as she orgasms. You push your fingers as deep as you can get them, feeling her body clench them rhythmically."
    $ the_person.have_orgasm(half_arousal = True)
    mc.name "Damn, that was hot. I could feel you cumming, gripping my fingers. I can't wait to feel you do that around my cock."
    "You start to pull your cock out. Still recovering, [the_person.title] takes a moment to register your words."
    the_person "Ah... yeah... on your... what?"
    "Once you pull it out, you smack her ass cheeks back and forth with it a couple times."
    the_person "Oh! Yeah but... [the_person.mc_title] its so big... I'm not sure..."
    mc.name "Shhh. Don't worry, I'll give you some time to adjust before I fuck your backdoor raw."
    "[the_person.title] submissively whimpers, but doesn't protest any further. Instead, she leans forward a little farther, preparing herself to get fucked."
    "When you're ready you push forward. Her back passage slowly accepts your erection, eliciting a satisfied sigh from [the_person.possessive_title]."
    $ the_person.break_taboo("anal_sex")
    ###Anal Scene, standing variant###
    call fuck_person(the_person, start_position = SB_anal_standing, start_object = make_desk(), skip_intro = True) from _call_fuck_person_anal_fetish_intro_employee_01
    #$ the_person.SB_fetish = "anal sex"
    $ the_person.max_opinion_score("anal sex")
    $ the_person.max_opinion_score("anal creampies")
    "[the_person.possessive_title] takes a few minutes to recover, then turns to you."
    $ the_person.draw_person(position = the_person.idle_pose)
    the_person "Wow, that was amazing, [the_person.mc_title]. I don't know what has been coming over me lately... I just can't stop thinking about you bending me over..."
    "[the_person.possessive_title] blushes and pauses..."
    mc.name "...And doing what, [the_person.title]?"
    "You tease her."
    the_person "I can't stop thinking about how full it feels... it feels so right when you push into my ass. It gets me so hot imagining it..."
    $ add_anal_fetish(the_person)
    mc.name "Here, I have something that might help."
    "You reach into your desk. Inside is a pink glass anal plug that you would normally use for discipline. Her eyes light up a bit when she see it."
    mc.name "Take this. Anytime you start getting the urge and its distracting you from work, play with it a bit. I'm sure it will help."
    "[the_person.possessive_title] takes her butt plug. She slowly pushes it into her ass."
    the_person "Thank you so much [the_person.mc_title]. We should do this again... and soon."
    $ the_person.draw_person(position = "walking_away")
    "You wave goodbye to [the_person.possessive_title] and get ready to head home for the night."


    $ the_person.apply_planned_outfit()
    $ clear_scene()
    return True

label anal_fetish_family_intro_label(the_person):
    $ the_person.aroual = 30
    $ the_person.draw_person(position = "standing_doggy")
    "As you walk into the room, you notice [the_person.possessive_title]. She is bent over and appears to be reading something on her phone."
    mc.name "Hey [the_person.title]"
    $ the_person.draw_person(position = "back_peek")
    "She quickly looks back at you."
    the_person "Oh hey [the_person.mc_title]."
    $ the_person.draw_person(position = "standing_doggy")
    "She turns back to her phone. As you start to walk over to her, you notice she appears to be moving her hips back and forth a bit..."
    mc.name "Looking at something interesting?"
    the_person "You could say that."
    "As you walk closer to her, you being to hear some of the audio her phone is playing. You hear some moaning and the sounds of skin against skin."
    "When you are right behind her, you can hear enough. She is watching some kind of porn."
    "You put your hands on her hips. With gentle force, you push your hips against hers. She starts to wiggle her ass up against you."
    mc.name "Watching something good I take it. Anything you'd like to try?"
    if the_person.has_taboo("anal_sex"):
        the_person "Actually yeah... something we haven't really tried before."
    else:
        the_person "Ah, well, we've tried it before, but I've been thinking about it a lot lately."
    "You keep rubbing yourself up against her as she watches her video. She moans as your cock gets hard and presses against her."
    $ the_person.change_arousal (10) # 40
    $ mc.change_arousal (10)
    if the_person.has_breeding_fetish(): #She likes getting pregnant
        the_person "You know I love it when we fuck and you cum deep inside me... but I was thinking maybe we could have a change of pace."
    elif the_person.has_taboo("condomless_sex") and not the_person.has_taboo("vaginal_sex"): #you'be fucked but not bare
        the_person "You know... what if we had sex... bare... and you could cum inside me. Without having to worry about getting me pregnant!"
        the_person "I know we are related, but I think I know how we could get around that."
    elif the_person.has_taboo("vaginal_sex") and not the_person.has_taboo("anal_sex"): #You've taken her ass before but not her pussy
        the_person "I know we've done it this way before, but I think I've really started to enjoy it this way."
    elif the_eprson.has_taboo("anal_sex") and the_person.has_taboo("vaginal_sex"): # You haven't fucked at all
        the_person "I umm... I'm not ready to go all the way with you... but I think I have an idea for something that would COULD do..."
    else:
        the_person "What can I say, the video reminded me of you a little bit..."
    "She holds her phone up. On the screen is a woman, bent over with her panties pulled down, getting fucked in the ass."
    "[the_person.possessive_title] has been dosed recently with some of your anal enhancing serums. You wonder if she is ready to awaken a new love of anal sex."
    if the_person in unique_character_list:
        "Warning, this character is unique, and may have unique fetish dialogue. If you continue, you may miss this dialogue!"
    menu:
        "Attempt to train her anal fetish" if mc.energy > 40:
            pass
            return False
        "Too tired" if mc.energy <= 40:
            pass
            #TODO re add the event for this person for the next day.
        "Not right now":
            "You decide to leave her alone for now. You might revisit this decision at a later date."
            $ clear_scene()
            return
    mc.name "God you are so naughty. You want me to fuck you in your ass right here, don't you?"
    the_person "Of course not. It doesn't have to be right here."
    mc.name "You'd like that though, wouldn't you? My cute litte [the_person.title], getting her ass taken anytime I feel like it. Anytime, anywhere."
    $ the_person.change_arousal(15) #55
    the_person "You make it sound bad..."
    mc.name "It sounds to me like you are being awfully naughty. I think you need a good spanking."
    if the_person.vagina_available():
        "You give her ass a smack, admiring the way her cheeks wobble."
    else:
        mc.name "Let's get this out of the way first."
        $ the_person.strip_outfit(exclude_upper = True)
        "Once you've got her clothing out of the way, you give her ass a smack, admiring the way her cheeks wobble."
    $ the_person.change_arousal(10) #65
    "You give her another spank. Her cheeks are starting to redden a bit, but its obvious from her arousal that she loves it."
    if the_person.has_taboo("anal_sex"):
        mc.name "I can't believe you want me to stick it in your ass. You are such a naughty little slut."
        "She stays quiet for now, but her ass wiggles a bit, making an enticing target."
        "You give her another spank."
        the_person "Ah! Oh fuck..."
        $ the_person.change_arousal(5) # 70
    else:
        mc.name "It's clear to me you've got a little bit of an obsession going. Can't get enough dick in your ass, even if its a family member?"
        "She stays quiet for now, but her ass wiggles a bit, making an enticing target."
        "You give her another spank."
        $ the_person.change_arousal(5) # 70
    mc.name "Fine, it's clear what you really want. Don't worry, I'll give it to you."
    "You pull out your cock. You grab her hand and bring it to your mouth where you spit a big glob of saliva, then make her stroke you a couple times, getting you lubricated."
    $ mc.change_arousal(5)
    "When you're ready, you point it at her puckered hole and begin to push. It takes several seconds, but you feel her sphincter give way and part for you."
    "With sweet, delicious pressure, your erection slowly buries itself in [the_person.possessive_title]'s bowel."
    $ the_person.change_arousal(15) #85
    $ mc.change_arousal(15)
    the_person "Oh god... why does it... feel so good!!!"
    "[the_person.possessive_title]'s ass feels amazing as you start to fuck it. It's time to show her just how good you can make her feel this way."
    call fuck_person(the_person, start_position = SB_anal_standing, skip_intro = True) from _call_fuck_person_anal_fetish_intro_family_01
    $ the_person.max_opinion_score("anal sex")
    $ the_person.max_opinion_score("anal creampies")
    "[the_person.possessive_title] slowly stands up."
    $ the_person.draw_person(position = the_person.idle_pose)
    the_person "That was amazing, [the_person.mc_title]."
    the_person "I... I think I need to get some new toys... something a little more purposefully made for anal use..."
    "You think about it for a minute."
    if starbuck_is_business_partner():
        mc.name "I have a friend who runs a sex shop over at the mall. Head over there sometime and tell her I sent you."
        mc.name "I'll text her to let her know you are coming. She can set you up with some special toys."
    else:
        mc.name "Hey, maybe you should go to the mall. I heard they have a sex shop there."
        mc.name "Maybe they have something there that would be good for you if I'm not around to fuck that ass."
    the_person "You know, I think I'll do that. Thank you [the_person.mc_title]. My ass is yours if you want to do this again sometime..."
    mc.name "A tempting offer to be sure."
    "You part ways with [the_person.title], confident that her new found anal fetish will bring you a lot of pleasure in the future."
    $ add_anal_fetish(the_person)
    $ clear_scene() #TODO does this leave you talking to the girl? If so figure out how to part ways cleanly here.
    return True

label anal_fetish_generic_intro_label(the_person):
    # Concept, spank her while fingering her ass so she can discover her new submissive, anal loving side.
    $ the_person.arousal = 40
    $ the_person.draw_person()
    "You walk up to [the_person.title] to say hello. However, something about her demeanor seems a little off."
    mc.name "Hello [the_person.title]. How are you doing today?"
    the_person "Hello [the_person.mc_title]! It's good to see you..."
    "You take a moment to look at her. Her cheeks seem flushed... Her nipples are poking against the fabric of her shirt. Is she... Aroused?"
    the_person "... Actually... I do have something you could help me with."
    "She leans forward and talks quietly in your ear."
    the_person "I woke up super horny this morning, but none of my usually masturbation techniques seemed to work... Can you help me out?"
    "Hmm, very interesting. Recently, you've been dosing her with your anal proclivity serums. Maybe that's why she's having trouble getting off?"
    "Helping her might develop her anal interest into a fetish!"
    if the_person in unique_character_list:
        "Warning, this character is unique, and may have unique fetish dialogue. If you continue, you may miss it!"
    menu:
        "Help her":
            mc.name "Let's find somewhere private first."
        "Too busy":
            mc.name "I'm sorry [the_person.title], but I just wanted to talk about something."
            $ the_person.change_love(-2)
            $ the_person.change_happiness(-5)
            the_person "Ah, okay. I see."
            return False

    "[the_person.title] takes your hand. You take a few minutes to find somewhere private where you won't be interrupted."
    $ the_person.draw_person(position = "kissing")
    "She throws her arms around you and you start to make out. You hands drop to her ass and you start to grope her aggressively."
    the_person "Mmm... that feels nice..."
    "You give her ass a rough spank."
    $ the_person.change_arousal(5) #45
    the_person "Oh! Mmm I've been bad haven't I..."
    "You give her a couple more spanks. She moans appreciatively."
    $ the_person.change_arousal(5) # 50
    mc.name "You really have been bad. Turn around, I need to punish you more appropriately."
    "[the_person.possessive_title] doesn't say a word, but submissively turns around and bends over for you."
    $ the_person.draw_person(position = "standing_doggy")
    if the_person.vagina_available():
        "You give her ass a smack, admiring the way her cheeks wobble."
    else:
        mc.name "Let's get this out of the way first."
        $ the_person.strip_outfit(exclude_upper = True)
        "Once you've got her clothing out of the way, you give her ass a smack, admiring the way her cheeks wobble."
    $ the_person.change_arousal (15) # 65
    mc.name "You've got an amazing ass [the_person.title]..."
    "You give her another spank. Her cheeks are starting to redden a bit, but its obvious from her arousal that she loves it."
    if the_person.has_taboo("anal_sex"):
        mc.name "Have you ever tried taking it in your ass? I think its clear that your ass needs some attention."
        the_person "Oh? I umm... not exactly... I not that kind of girl..."
        "You give her another spank."
        the_person "Ah! Oh fuck..."
        $ the_person.change_arousal(5) # 70
    else:
        mc.name "It is clear to me that your ass needs some attention. I'm going to spank you until its red and then fuck it."
        the_person "I... I'm not like... usually that kind of girl..."
        "You give her another spank."
        $ the_person.change_arousal(5) # 70
    mc.name "Are you sure? You certainly seem to be enjoying this so far."
    "Another spank. You notice goosebumps growing all down her body."
    $ the_person.change_arousal(10) # 80
    the_person "I... I can't believe I'm saying this but... my body is telling me to!"
    mc.name "I'm sorry, what exactly is your body telling you?"
    "*SPANK*"
    the_person "Ah! Its telling me it wants you to fuck my ass! Push it in and fuck me raw! Oh god it sounds so good!"
    "You give her ass two more final spanks."
    $ the_person.change_arousal(10) # 90
    mc.name "Alright. First, get on your knees. I want my cock nice and lubed up so it goes in easy."
    $ the_person.draw_person(position = "blowjob")
    "[the_person.possessive_title] immediately drops to her knees without a word. You quickly pull your cock out."
    "She wastes no time and begins slobbering all over your erection. Her tongue runs up and down your full length, multiple times."
    $ mc.change_arousal(10)
    mc.name "Good girl. Now get ready for me, I'm going to fuck your ass, just the way you want it."
    the_person "Oh god..."
    $ the_person.draw_person(position = "standing_doggy")
    "[the_person.possessive_title] turns and points her ass at you, bending over. You grab her hip in one hand and your cock in the other."
    "You run the tip of your saliva soaked meat all around her puckered hole, then start to push. She mewls as you start to push it in."
    "Slow and steady, you push yourself in until you are completely bottomed out in her bottom."
    $ the_person.change_arousal (15) #105
    the_person "Oh my god... its so big! Oh [the_person.mc_title] its so good!"
    $ the_person.have_orgasm(half_arousal = True)
    "[the_person.possessive_title]'s ass is twitching wildly all around you as she orgasms. You hold her hips tight and in place with both hands as her body quivers."
    "It feels amazing to have her body gripping you as she cums."
    $ mc.change_arousal(10)
    mc.name "See? You just needed something in your ass so you could cum."
    the_person "I... I think you might be right... I..."
    "She stops mid sentence as you give her a quick thrust."
    mc.name "Its okay to admit you are a buttslut. Now, lets just make sure you needs are sated before we part ways."
    "[the_person.possessive_title] is unable to reply as you begin to fuck her ass. It's time to show her just how good you can make her feel that way."
    call fuck_person(the_person, start_position = SB_anal_standing, skip_intro = True) from _call_fuck_person_anal_fetish_intro_generic_01
    #$ the_person.SB_fetish = "anal sex"
    $ the_person.max_opinion_score("anal sex")
    $ the_person.max_opinion_score("anal creampies")
    $ the_person.draw_person(position = "doggy")
    "After you finish with her, [the_person.possessive_title] drops to her knees as she tries to recover."
    $ the_person.draw_person(position = the_person.idle_pose)
    the_person "That was amazing, [the_person.mc_title]."
    the_person "I can't stop thinking about how full it felt, when your cock pushed into my ass..."
    if starbuck_is_business_partner():
        mc.name "Hey, I have a friend who runs a sex shop over at the mall. Head over there sometime and tell her I sent you."
        mc.name "I'll text her to let her know you are coming. She can set you up with some masturbation toys that can help you if you find yourself in this position again."
    else:
        mc.name "Hey, maybe you should go to the mall. I heard they have a sex shop there."
        mc.name "Maybe they have something that would help you out, with masturbating, if you find yourself in this position again."
    the_person "You know, I think I'll do that. Thank you [the_person.mc_title]. My ass is yours if you want to do this again sometime..."
    mc.name "A tempting offer to be sure."
    "You part ways with [the_person.title], confident that her new found anal fetish will bring you a lot of pleasure in the future."
    $ add_anal_fetish(the_person)
    $ clear_scene() #TODO does this leave you talking to the girl? If so figure out how to part ways cleanly here.
    return True

label anal_fetish_mom_intro_label():
    return False

label anal_fetish_lily_intro_label():
    $ the_person = lily # make sure we use lily for the event
    $ the_person.event_triggers_dict["LastAnalFetish"] = day
    $ fetish_after_hours_unlock()
    "As you are finishing up with work for the day, you get a text on your phone. It is from Lily, [the_person.possessive_title]."
    the_person "Hey [the_person.mc_title]! Can you do me a favor? Meet me at the mall when you get off work. I need your help with something..."
    "You let her know you'll be there. You quickly finish up with your work and head over to the mall."
    $ mall.show_background()
    "When you get to the mall, you look around for a minute, then spot [the_person.title]. She waves to you then comes running over to you, giving you a big hug."
    $ the_person.draw_person(position = "stand4")
    the_person "Hey! Thanks for coming with me! I need your help with something!"
    "You are a little hesitant. She wants you to go shopping with her?"
    mc.name "Are you sure you need me for this?"
    "She gives you a mischievous smile."
    the_person "Definitely! Don't worry, you'll be glad you came when you see where we are going."
    the_person "I have had some special requests on my insta pic channel. I need you because I don't want to go by myself and get creeped on!"
    "[the_person.title] grabs you by the hand and leads you into the mall. It seems any inhibition she might have previously had being seen with her [the_person.mc_title] has vanished after being corrupted by your serums."
    "You are almost surprised when she leads you into the sex shop. The owner greets you as you walk in."
    $ sex_store.show_background()
    if starbuck.sluttiness > 50 or starbuck.love > 30 or starbuck_is_business_partner()::
        $ starbuck.draw_person(emotion = "happy")
        starbuck "Hello! Welcome to... Oh hey [the_person.mc_title]! Good to see you! Oh and you brought a partner! Hi I'm [starbuck.title]!"
    else:
        $ starbuck.draw_person(emotion = "happy")
        starbuck "Hello! Welcome to Starbuck's Sex Shop! It's so great to see a couple come in."
    starbuck "Is there anything I can help you find?"
    $ the_person.draw_person(position = "stand4")
    "[the_person.possesive_title] takes the lead."
    the_person "Yeah so, I was wondering, do you sell a special type of strap on that came be used to... umm... strap on to a guy so he can fuck your pussy and ass at the same time?"
    "You can barely believe your ears. You knew that the serums you had been giving [the_person.title] were starting to really corrupt her, but you had no idea she was ready for something like this."
    "And for her instapic channel? It's almost too good to be true."
    $ starbuck.draw_person(emotion = "happy")
    starbuck "Oh! I've got just the thing! Follow me!"
    $ starbuck.draw_person(position = "walking_away")
    if perk_system.has_item_perk("Male Strapon"):
        "As you are following, remembering you already have something similar, you show [the_person.title] what you have in your backpack."
        mc.name "Hey... I already kinda have something like that..."
        "She looks at what you've got and her eyes get bright."
        the_person "Ah! Bro! Why didn't you tell me you had one of these?"
        "[starbuck.possessive_title] turns to you as you reach a selection of dildos."
        the_person "Just pretend like we are looking then, that will totally work!"
    else:
        "[starbuck.possessive_title] leads you over to a selection of dildos. They have special straps that go around the man so that they are secured, just below penis, and can be used for double penetration."

    $ the_person.draw_person(position = "stand4")
    the_person "Hmm... I don't know, what do you think about this one?"
    "[the_person.title] picks up one. It has an extra little vibrating unit."
    mc.name "That looks pretty good, actually."
    "[the_person.title] takes it up to the counter."
    $ starbuck.draw_person(emotion = "happy", position = "stand2")
    starbuck "Great! This one is actually on sale, but I hadn't gotten around to marking it yet. Its only $200!"
    "You decide to offer to pay for it."
    mc.name "Here, let me just put this on the company card..."
    $ mc.business.change_funds(-200)
    if perk_system.has_item_perk("Male Strapon"):
        "Well, now you have an extra, in case anything ever happens to your other one..."
    starbuck "Okay! You're all set! Do you two want to try it out? I have a special room in the back, sometimes people just can't WAIT to get home before trying out a purchase!"
    $ the_person.draw_person(position = "stand4")
    "[the_person.title] hesitates and looks at you."
    mc.name "I think that would be a good idea, don't you [the_person.title]?"
    the_person "Oh yeah, of course!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] grabs your hand and you follow her to the backroom. It has a familiar smell of body fluids and sweat."
    $ the_person.draw_person(position = "stand4")
    "Come on [the_person.mc_title], I can't wait to feel you fuck me with this thing on..."
    "[the_person.possessive_title] quickly strips, eager to get started."
    $ the_person.apply_outfit(SB_anal_nude_outfit)
    $ the_person.draw_person(position = "stand4")
    "You get yourself naked as well. On a nearby shelf you spot a bulk size bottle of intimate lube."
    "[the_person.possessive_title] gets down on her knees and starts to secure the toy to your cock."
    $ the_person.draw_person(position = "blowjob")
    mc.name "Mmm, you look amazing on your knees [the_person.title]."
    "[the_person.possessive_title] looks up at you."
    the_person "Yeah, you like it anytime I'm near your dick. Trust me, I'd love to blow you, but I've got something else in mind..."
    $ the_person.draw_person(position = "doggy")
    "[the_person.possessive_title] turns over and gets on her hands and knees in front of you on the floor. She lifts her hips and starts waving her ass in the air."
    "You grab a few squirts of the lube and get your cock and the dildo all lubed up. You grab another squirt and start working it in her rear entry."
    the_person "Mmm... that is so good... I don't know why, lately I just haven't been to stop thinking about your cock fucking me back there..."
    "You've been having her test some of your anal enhancing serums. It sounds like she might be developing an anal fetish!"
    "You push two fingers into her tight rump. They grip and squeeze at your fingers."
    $ the_person.change_arousal(10)
    the_person "Oh! That feels good... but I'm ready for you. Let me have it [the_person.mc_title]!"
    "You use your hand to line yourself cock up with her puckered hole. She reaches down and grabs the dildo and lines it up with her pussy."
    "With one slow, smooth motion, you push your cock past her well lubed sphincter. It goes in with a small pop, and then you continue with a slow thrust until your cock is buried in her ass."
    $ the_person.break_taboo("anal_sex")
    the_person "Fuck! Holy hell... [the_person.mc_title] that is intense! I've never felt... I'm so full!!!"
    "Going tantalizingly slow, you pull yourself mostly out, then back into her buttery smooth back door."
    the_person "Okay... Go slow... but I'm ready!"
    call fuck_person(the_person, start_position = SB_doggy_anal_dildo_dp, start_object = make_floor(), skip_intro = True) from _lily_anal_fetish_intro_01
    $ the_report = _return
    if the_report.get("girl orgasms", 0) > 1:
        "[the_person.possessive_title] is a sweaty, heaving mess. You know she had multiple orgasms from the intense sensations of the double penetration."
        "She looks back at you in awe."
    elif the_report.get("girl orgasms", 0) > 0:
        "[the_person.possessive_title] is laying on the floor, exhausted from the intensity of the double penetration."
        "She looks back at you and smiles"
    the_person "[the_person.mc_title]... That felt amazing. I'm not sure though... are we going to able to keep this from mom? I don't think I can stay quiet enough when I'm getting fucked in both holes like that..."
    "You give her a reassuring smile."
    mc.name "Don't worry [the_person.title], we'll be careful."
    the_person "Good... because lately I've just been craving you so bad. We don't have to always use the strap on. But just thinking about you fucking my ass makes me so horny."
    $ add_anal_fetish(the_person)

    "It is pretty clear from the way she got off while you were fucking her and the way she was talking afterwards, you're convinced [the_person.possessive_title] has developed an anal fetish!"
    $ mc.change_location(sex_store)
    "After you both clean up, you leave the back room of the sex shop."
    $ starbuck.draw_person(emotion = "happy")
    starbuck "Have a good day! Thank you for shopping at Starbuck's sex shop!"
    if starbuck.sluttiness > 50:
        "You wave goodbye to [the_person.possessive_title]. You note some telltale signs of arousal, flushed cheeks, and you can see her nipples are erect."
        "Was she watching you somehow? Oh well, you decide to head out."
    else:
        "You wave goodbye to [the_person.possessive_title] and head out."
    $ male_strapon_unlock()  #TODO test this
    $ the_person.apply_planned_outfit()
    $ clear_scene()
    return

label anal_fetish_rebecca_intro_label():
    return False

label anal_fetish_gabrielle_intro_label():
    return False

label anal_fetish_stephanie_intro_label():
    return False

label anal_fetish_alex_intro_label():
    return False

label anal_fetish_nora_intro_label():
    return False

label anal_fetish_emily_intro_label():
    return False

label anal_fetish_christina_intro_label():
    return False

label anal_fetish_starbuck_intro_label():
    return False

label anal_fetish_sarah_intro_label():
    return False

label anal_fetish_ophelia_intro_label():
    return False

label anal_fetish_candace_intro_label():
    return False

label anal_fetish_dawn_intro_label():
    return False

label anal_fetish_erica_intro_label():
    return False

label anal_fetish_ashley_intro_label():
    return False
