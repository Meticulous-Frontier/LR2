## Morning crisis
#Have breakfast with Jennifer. Designed as an opportunity to raise her obedience, and to give some variation to morning events
#You wake up and have breakfast with Jennifer. At minimal sluttiness, gives MC the option to giver her a motivational speech.
#At mid sluttiness, MC can tell Jennifer she should try going to work without underwear on, try and get attention from men that way.
#At high sluttiness, Jennifer asks MC to cum on/in her so she can feel it throughout the day.
#Fetish options: for Anal, Jennifer asks for anal, for cum fetish, you cum on/in her as appropriate, and for vaginal, she asks for creampie.

init -1 python:
    mom_breakfast_mod_weight = 5

init 2 python:
    def mom_breakfast_crisis_requirement():
        if mc_at_home() and time_of_day == 0:
            if day % 7 == 5 or day % 7 == 6: #Checks to see if it is saturday or sunday.
                return False
            return True
        return False

    def mom_commando_day_selfie_requirement():
        if time_of_day == 2: #It is the end of the day on friday
            return True
        return False

    def mom_breakfast_mod_initialization(self):
        pass #???? Do I need something here? TODO
        return

    shower_crisis_action = ActionMod("Breakfast with Mom", mom_breakfast_crisis_requirement,"mom_breakfast_action_label", initialization = mom_breakfast_mod_initialization,
        menu_tooltip = "You have breakfast with Mom before she goes to work..", category="Home", is_crisis = True, is_morning_crisis = True, crisis_weight = mom_breakfast_mod_weight)

    mom_commando_day_selfie_action = Action("Mom Commando Selfie", mom_commando_day_selfie_requirement, "mom_commando_day_selfie_label")

label mom_breakfast_action_label():
    "You wake up, shower, and get ready for the day. As you finish getting ready you notice the smell of bacon and coffee coming from the kitchen."

    python:
        mc.change_location(kitchen)
        mc.location.show_background()
        the_person = mom
        scene_manager = Scene()
        scene_manager.add_actor(the_person, position = "sitting")
    #"When you walk out to the kitchen, you see [the_person.title] just sitting down to some breakfast."
    #$ the_person.draw_person(position = "sitting")

    mc.name "Good morning, [the_person.title]. That smells great!"
    "She sees you walk into the kitchen and greets you warmly."
    the_person.char "Good morning! I made extra, grab some breakfast! I want you well fed going to work today."
    "You grab some coffee and some bacon and sit down next to [the_person.possessive_title]. She is shaking her head while she looks at her phone."
    #$ the_person.draw_person(position = "sitting",emotion="angry")
    $ scene_manager.update_actor(the_person, position = "sitting", emotion="angry")
    mc.name "Everything okay?"
    if the_person.sluttiness < 20:  #Low Sluttiness path
        call mom_breakfast_action_label_low() from _call_mom_breakfast_action_label_low
    elif the_person.sluttiness < 70: #mid sluttiness path
        call mom_breakfast_action_label_medium() from _call_mom_breakfast_action_label_medium
    else:
        call mom_breakfast_action_label_high() from _call_mom_breakfast_action_label_high


    $ scene_manager.clear_scene()
    return

label mom_breakfast_action_label_low():
    "She wrinkles her nose for a second and then looks up at you."
    the_person.char "What? Oh... sorry, I was just looking at this work email. Sometimes I just feel so burnt out."
    "You look down at your coffee. You should probably say something."
    menu:
        "Emphasize Family": #This will increase love value.
            mc.name "You work so hard, [the_person.title]. You are pretty amazing, sacrificing so much for your family."
            "Your kind words bring a smile to her face."
            $ scene_manager.update_actor(the_person, position = "sitting", emotion="happy")
            the_person.char "Thank you, [the_person.mc_title], for your kind words. You and your sister mean so much to me, its a good reminder why I do what I do sometimes."
            $ the_person.change_love(5)
            $ the_person.change_happiness(2)

        "Emphasize Happiness": #This will increase happiness (duh)
            mc.name "I'm sorry work is such a pain. Just think about the weekend coming up, maybe you and [lily.title] can go shopping or something?"
            "Your kind words bring a smile to her face."
            $ scene_manager.update_actor(the_person, position = "sitting", emotion="happy")
            the_person.char "Thank you, [the_person.mc_title], for your kind words. You and your sister mean so much to me, its a good reminder why I do what I do sometimes."
            $ the_person.change_love(2)
            $ the_person.change_happiness(5)
        "Emphasize Stability": #This will increase obedience
            mc.name "I'm sorry work is annoying. I know you do it just to keep us afloat, but I have a good feeling about this business I'm running now, I can start supporting the family more soon."
            "Your kind words bring a smile to her face."
            $ scene_manager.update_actor(the_person, position = "sitting", emotion="happy")
            the_person.char "Oh, thank you [the_person.mc_title], but you don't need to worry about supporting me. I'm just happy to see you making something of yourself."
            $ the_person.change_obedience(5)
            $ the_person.change_happiness(2)
    "You and [the_person.title] chat for a while longer, until you finish with your breakfast."
    mc.name "Thanks for the great breakfast! I'll see you tonight after work!"
    "You say goodbye to her and head out for the day."
    return

label mom_breakfast_action_label_medium():
    "She wrinkles her nose for a second and then looks up at you."
    the_person.char "What? Oh... sorry! I was supposed to meet with this guy after work today for a few drinks, but he cancelled on me!"
    "[the_person.title] mutters to herself for a moment."
    $ scene_manager.update_actor(the_person, position = "sitting", emotion="sad")
    the_person.char "I mean, what does a woman my age have to do to get some male attention? It feels like no one even notices me at work anymore."
    "You look down at your coffee. You should probably say something."
    menu:
        "Go Commando": #Tell her to go without underwear. Has a chance of causing an event later in the day where she sends you a selfie with cum somewhere on her.
            mc.name "There are a few girls at my company that come in to work sometimes without any underwear on when they are looking for attention. Maybe you should try that?"
            "[the_person.title] thinks for a moment."
            $ scene_manager.update_actor(the_person, position = "sitting", emotion="happy")
            the_person.char "You know what? Why not! I used to do that on dates when I was younger. If nothing else, it'll make me feel young!"
            "[the_person.title] gets up and gives you a quick peck on the cheek."
            $ scene_manager.update_actor(the_person, position = "stand4")
            the_person.char "You have a good day at work, I'm going to go umm, get changed!"
            $ the_person.draw_person(position = "walking_away")
            $ the_person.change_stats(slut_temp = 10, obedience = 5)
            if the_person.sluttiness > 50:
                $ mc.business.mandatory_crises_list.append(mom_commando_day_selfie_action)
            return
        "Give Her Some Attention":  #Sluttiness staircase event, take it farther the sluttier she is
            mc.name "I'm sorry [the_person.title], I didn't realize you were in need of some attention!"
            "You get up from your chair and walk around behind [the_person.possessive_title]"
            the_person.char "[the_person.mc_title]? What are you... oohhhh."
            "You put your hands on her shoulders and begin to massage them. She sighs as your hands begin to work on her tension."
            menu:
                "Grope her breasts" if the_person.sluttiness > 30:
                    "You work on her shoulders for a couple of minutes, then slowly run your hands down to her considerable chest."
                    the_person.char "Oh [the_person.mc_title]... I'm not sure..."
                    $ the_person.break_taboo("touching_body")
                    "You interrupt her and whisper in her ear."
                    mc.name "Sshhh, just relax. Close your eyes and relax."
                    $ the_person.change_arousal(15)
                    "You roll her nipples a couple of times between your fingers. She sighs at the sensations you are giving her."

                "Finish Massage":
                    "You work on her shoulders for a while. She sighs in relaxation. You finish up and go back to your breakfast."
                    return
            if the_person.outfit.tits_available():
                "This skin of [the_person.possessive_title]'s creamy tits feels hot and soft in your hands."
            else:
                menu:
                    "Pull Her Top Up" if the_person.sluttiness > 40:
                        while the_person.outfit.get_upper_top_layer():    #If covered up, have her take her top off
                            $ scene_manager.draw_animated_removal(the_person, the_person.outfit.get_upper_top_layer())
                        "You reach down and slowly remove her top, exposing her creamy tits."
                        $ the_person.break_taboo("bare_tits")
                        "Your hands return to her chest, her boobs feel hot and soft in your hands."

                    "Finish Massage":
                        "[the_person.possessive_title] feel great, but eventually you decide it is too risky to keep going."
                        "[the_person.title] shakes her head a bit as you sit back down, as if trying to clear some thoughts from her head."
                        return
            #Assume we are still going
            "She arches her back as the pleasurable feeling of having her tits played with begins to grow."
            $ the_person.change_arousal(20) #35
            the_person.char "Oh, that feels so good, but we should probably stop before your sister comes out..."
            menu:
                "Pet Her Pussy" if the_person.sluttiness > 50 and not the_person.outfit.vagina_available():
                    "You whisper in her ear."
                    mc.name "I've got a better idea."
                    "You let one hand slowly descend from her breast down to the mound between her legs."
                    the_person.char "Oh! Mmmm, okay..."
                    "[the_person.title] lets out a little yelp when you first make contact with her groin."
                    "She arches her back again as you begin to nibble at her ear."
                    $ the_person.change_arousal(30) #65
                    menu:
                        "Finger Her" if the_person.sluttiness > 60:
                            "You bring your hand up a bit, then slowly down again, this time beneath her clothing."
                            $ the_person.break_taboo("touching_vagina")
                            "This time, she doesn't put up a fight, she is too close to cumming."
                            "Your fingers are now sliding across the flesh of her moistened cunt."
                        "Finish Massage":
                            "You decide for now just to tease her. You pet her through her clothes for a minute longer then stop, kissing her on her neck."
                            "[the_person.title] looks at you as you sit down, arousal clear in her eyes."
                            mc.name "Don't want to go to far, [lily.name] could walk out at any moment..."
                            "She shakes her head for a moment, trying to clear her thoughts, but it is obvious her mind continues to dwell on how it could go if you had kept going..."
                            $ the_person.change_stats(obedience = 10, slut_temp = 3)
                            return
                    pass
                "Finish Massage":
                    "You pinch and pull at her nipples for a few more minutes, but eventually you decide just to tease her for now."
                    "[the_person.title] looks at you as you sit down, arousal clear in her eyes."
                    mc.name "Don't want to go to far, [lily.name] could walk out at any moment..."
                    $ the_person.change_stats(obedience = 5, slut_temp = 3)
                    return
                "Finger Her" if the_person.sluttiness > 60 and the_person.outfit.vagina_available():
                    "You whisper in her ear."
                    mc.name "I've got a better idea."
                    "You let one hand slowly descend from her breast down to her exposed cunt."
                    $ the_person.break_taboo("touching_vagina")
                    $ the_person.change_arousal(30) #65
            #We assume here we are fingering her to completion.
            "You dip two fingers into her honeypot. She moans as your begin to stir your fingers for a bit."
            the_person.char "Oh honey, that feels so good..."
            $ the_person.change_arousal(20) #85
            "Her hip are beginning to move on their own now, needily grinding against your hand."
            "Her breathing is getting ragged. You begin to circle her clit with your fingers, trying to finish her off."
            the_person.char "Oh! Thats it! Oh god I'm gonna..."
            "[the_person.title]'s body tenses, then convulses. She is able to muffle her noises to a whimper, trying not to alarm your sister."
            $ the_person.call_dialogue("climax_responses_foreplay")
            $ mc.listener_system.fire_event("girl_climax", the_person = the_person) #TODO check and make sure this works...
            $ the_person.change_stats(obedience = 5, happiness = 5)
            "When she has finished climaxing, you slowly withdraw your finger and sit back down at the table. You take a quick sip of your coffee."
            "[the_person.title] is just putting her clothing back in place when your sister comes out of her room."
            $ the_person.review_outfit(dialogue = False)
            $ scene_manager.draw_scene()
            "She grabs some cereal and sits at the table with you and [the_person.title]"
            $ scene_manager.add_actor(lily, position = "sitting", character_placement = character_left_flipped)
            lily.char "Good morning! Thanks for the coffee mom!"
            the_person.char "Good... Good morning dear..."
            "[lily.title] looks over at [the_person.title] with some concern."
            lily.char "Are you feeling okay mom? Your cheeks are all flushed and you look so... tired?"
            the_person.char "Of course dear, I was just getting ready to go get ready for work..."
            $ scene_manager.update_actor(mom, position = "stand2")
            "As [the_person.possessive_title] starts to get up, she looks at you. You make sure she notices as you lick some of her juices off your fingers."
            $ the_person.change_stats(slut_core = 2, slut_temp = 5)
            the_person.char "Oh my..."
            $ scene_manager.update_actor(mom, position = "walking_away")
            "[the_person.title] turns and leaves the kitchen in a hurry. You quickly finish breakfast and head out as well."
    return

label mom_breakfast_action_label_high():
    "She wrinkles her nose for a second and then looks up at you."
    the_person.char "What? Oh... sorry! I was just sending some dirty text messages with this guy at work, but he has to go because of his wife or something..."
    "[the_person.title] mutters to herself for a moment. Then she looks over at you."
    $ scene_manager.update_actor(mom, position = "sitting", emotion="happy")
    the_person.char "Say... you look awfully handsome this morning..."
    "She looks around, and notices the door to sister's room is still closed. She must be sleeping in."
    the_person.char "I had some really crazy dreams last night, it would be nice if I could release a little tension before work. Are you up for a quickie?"
    menu:
        "Have a Quickie":
            mc.name "That sounds pretty nice actually, what did you have in mind?"

        "Feed Her" if SB_check_fetish(the_person, cum_internal_role) or SB_check_fetish(the_person, cum_external_role):
            #fetish blowjob path
            the_person.char "Oh! I know! You just keep eating your breakfast, mommy will just help herself!"
            $ scene_manager.update_actor(mom, position = "blowjob")
            $ the_person.break_taboo("touching_penis")
            "[the_person.possessive_title] quickly gets down on her knees and under the table. You feel her expert hands removing your belt and trousers. She sighs when your cock springs free."
            the_person.char "Mmm, that's what I was dreaming about... I had a dream that I was blowing you, and you started cumming, and you just kept cumming and cumming and it was everywhere..."
            "She opens her mouth and runs her tongue along your length, breathing in your masculine musk."
            the_person.char "It was amazing... I want some of the real thing!"
            $ the_person.break_taboo("sucking_cock")
            "She opens her mouth and slides your penis in. She dances circles all around it while she suckles the tip. You look down and notice that she is touching herself."
            $ the_person.change_arousal(20)
            call fuck_person(the_person, start_position = SB_cum_fetish_blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = True, position_locked = True) from _call_fuck_person_workday_breakfast_01
            "Finished with her breakfast, [the_person.title] gets up from the table and excuses herself."
            $ scene_manager.update_actor(mom, position = "walking_away")
            the_person.char "Have a good day at work, I'm gonna go get ready for the day!"
            return
        
        "Long Day Ahead":
            mc.name "I'm sorry [the_person.title], but I have a long day scheduled today. I think I had better save my energy!"
            $ scene_manager.update_actor(mom, position = "sitting", emotion="sad")
            $ the_person.change_stats(happiness = -5, obedience = 5)
            the_person.char "That's okay, I understand. Well don't forget, dinner will be the usual time tonight. Maybe we can do something after that?"
            "You give her a non-committal shrug. The tension at the table is a little much, so you quickly finish your breakfast and head out."
            return

    $ scene_manager.update_actor(mom, position = "stand4")
    the_person.char "Oh! We'd better go quick, your sister could come out at any time..."

    if mc.business.event_triggers_dict.get("family_threesome", False) == True:
        mc.name "Why does it matter if [lily.name] comes out?"
        the_person.char "Well, I mean its not that I mind, but your mommy has needs [the_person.mc_title]..."
        menu:
            "Insist [lily.title] join you" if willing_to_threesome(mom, lily):
                mc.name "Don't worry [the_person.title]. I'll make sure you have your needs met."
                the_person.char "I suppose that would be okay, just make sure I get to finish!"
                mc.name "Of course!"
                "[the_person.possessive_title] quickly starts to strip down while you knock on [lily.possessive_title]'s door."

                $ scene_manager.strip_actor_outfit(mom)
                "After no response, you knock again."
                lily.char "What!?! I'm tired!"
                mc.name "Me and mom are gonna have some fun, you should join us."
                lily.char "Huh? Really!?! I'll be right there!"
                "You walk back to the kitchen and [lily.title] quickly joins you."
                $ scene_manager.add_actor(lily, character_placement = character_center)
                if lily.outfit.full_access():
                    "Already basically ready to go, [lily.title] looks to you for direction."
                else:
                    "Seeing [the_person.possessive_title] already naked, [lily.title] strips down also."
                    $ scene_manager.strip_actor_outfit(lily)
                mc.name "Mom is feeling needy this morning sis, why don't we take care of her?"
                lily.char "Sounds great!"
                call start_threesome(the_person, lily, start_position = Threesome_doggy_deluxe) from _fuck_mom_for_breakfast_1
                $ the_report = _return
                if the_report["girl one orgasms"] > 0 and the_report["girl two orgasms"] > 0 and the_report["guy orgasms"] > 0: #Happy family
                    "The three of you remain together for a while, enjoying your orgasms."
                    $ the_person.change_stats(obedience = 5, happiness = 15)
                    the_person.char "You two... I get overwhelmed by all the love I feel for you two when we do things like this. I love you both so much!"
                elif the_report["girl one orgasms"] > 0:
                    "[the_person.possessive_title] recovers for a bit from her orgasm."
                    $ the_person.change_stats(obedience = 5, happiness = 5)
                    the_person.char "Thank you, [the_person.mc_title], for insisting on bringing your sister out. You were right, that felt so good."
                    lily.char "What? Mooooom! You were gonna fuck around without me?"
                "You get up and excuse yourself. Time to start the day!"
                return

            "Relent":
                mc.name "Ok... but I'm not going to keep it down just because she is home."
                the_person.char "Okay dear."

    "[the_person.possessive_title] quickly starts to strip down."

    $ scene_manager.strip_actor_outfit(mom)

    "You take a quick sip of coffee. [the_person.possessive_title] is naked in the kitchen!"
    if SB_check_fetish(the_person, anal_fetish_role): #The anal role
        "She opens one of the drawers and pulls out a bottle of lube..."
        mc.name "You keep lube in the kitchen?"
        the_person.char "Hush, you never know when you might have need of something like that, especially with all the urges I've been having lately..."
        "You watch as she applies a generous amount to her hand, then she reaches back and starts applying it to her back end."
        the_person.char "Remember, this is a quickie! Sit back and enjoy, but don't hold back! I want your cum!"
        "[the_person.possessive_title] unzips your pants and pulls out your firm cock. She sits down on your lap, facing you."
        $ scene_manager.update_actor(mom, position = "cowgirl")
        "With one hand on your cock, she guides you to her tight anal pucker. In one smooth motion, she relaxes herself and lowers her body down on to you, impaling herself on your manhood."
        the_person.char "OH fuck, that is just what I needed... I was dreaming about this last night... I dreamed that you had me tied up and bent over and you pounded my ass over and over..."
        "She is whispering in your ear. [the_person.title] is truly desperate to have her ass stuffed with your cock."
        the_person.char "I remember you saying you were gonna cum... and I was so ready for it, I was begging you for it... and then suddenly I woke up!"
        "[the_person.possessive_title] hips are moving in wide circles. Her bowel feels amazing, like a buttery vice."
        the_person.char "I just need to feel it. To feel you cum inside my ass, to blow so deep and fill me up."
        "Her voice and her movements are desperate. You suddenly realize that she is racing you to the finish, and you aren't sure who is going to finish first."
        the_person.char "I need it [the_person.mc_title]! I want to feel you slowly oozing out of me as I walk around at work today. Then when I get home I want you to spank me and fuck my ass over the counter while I cook dinner!"
        "Your balls are beginning to tense, you are seconds away from ejaculating!"
        the_person.char "Claim my asshole! Mark your territory with your cum! Then spank me and do it again and again!"
        "You climax in a frenzy. She arches her back and moans involuntarily when she feels your cum flood her rectum. Her orgasm hits immediately after yours."
        "Finally speechless, [the_person.title]'s body stops rocking, but you feel the twitching of her sphincter as orgasmic waves hit her. You sigh happily, dumping the last of your cum insider her."

        $ the_person.cum_in_ass()
        $ mc.listener_system.fire_event("girl_climax", the_person = the_person) #TODO check and make sure this works...
        $ the_person.change_stats(happiness = 5, obedience = 5)

        "As her orgasm subsides, [the_person.possessive_title] suddenly returns to her senses."
        the_person.char "Oh god... [lily.name] could walk out any second!"
        $ scene_manager.update_actor(mom, position = "walking_away")
        "[the_person.title] quickly gets up and hurries away. She calls back before she gets to her room."
        the_person.char "I love you, have a good day at work!"
        $ scene_manager.remove_actor(mom)
        "You put your cock away and finish your breakfast before heading out for the day."
        return

    the_person.char "Remember, this is a quickie! Sit back and enjoy, but don't hold back! I want your cum!"
    "[the_person.possessive_title] unzips your pants and pulls out your firm cock. She sits down on your lap, facing you."
    $ scene_manager.update_actor(mom, position = "cowgirl")
    "With one hand on your cock, she guides you straight to her cunt. In one smooth motion, she relaxes herself and lowers her body down on to you, impaling herself on your manhood."
    the_person.char "OH fuck, that is just what I needed... I was dreaming about this last night..."
    "She is whispering in your ear. [the_person.title] is really turned on right now."
    the_person.char "I remember you saying you were gonna cum... and I was so ready for it, I begging you for it... and then suddenly I woke up!"
    "[the_person.possessive_title] hips are moving in wide circles. Her sopping wet cunt feels amazing surrounding your penis."
    the_person.char "I want to feel it. Not just when you cum now... but when I'm at work, I want to feel you slowly leak out of me..."
    "Her voice and her movements are desperate. You suddenly realize that she is racing you to the finish, and you aren't sure who is going to finish first."
    the_person.char "I need it [the_person.mc_title]! I want every drip to be a reminder of how good you make me feel!"
    "Your balls are beginning to tense, you are seconds away from ejaculating! She begins to make a short, fast humping motion, grinding her clit against your stomach."
    the_person.char "Claim mommy! Mark your territory with your cum! Fill me up!"
    "You climax in a frenzy. She arches her back and moans involuntarily when she feels your cum flood her womb. Her orgasm hits immediately after yours."
    "Finally speechless, [the_person.title]'s body stops rocking, but you feel the twitching of her pussy as orgasmic waves hit her. You sigh happily, dumping the last of your cum insider her."

    $ the_person.cum_in_vagina()
    $ mc.listener_system.fire_event("girl_climax", the_person = the_person) #TODO check and make sure this works...
    $ the_person.change_stats(happiness = 5, obedience = 5)

    "As her orgasm subsides, [the_person.possessive_title] suddenly returns to her senses."
    the_person.char "Oh god... [lily.name] could walk out any second!"
    $ scene_manager.update_actor(mom, position = "walking_away")
    "[the_person.title] quickly gets up and hurries away. She calls back before she gets to her room."
    the_person.char "I love you, have a good day at work!"
    $ scene_manager.clear_scene()
    "You put your cock away and finish your breakfast before heading out for the day."
    return


label mom_commando_day_selfie_label():
    $ the_person = mom
    $ the_person.strip_outfit(delay = 0, exclude_upper = True)
    $ the_person.cum_on_ass()
    "You get a notification on your phone from [the_person.title]."
    the_person.char "Hey, you were right! Going commando really payed off. I was making copies and when I bent over to pick them up from the tray, one of my colleagues noticed..."
    the_person.char "We snuck off to a janitor closet... he just barely pulled out in time!"
    $ the_person.draw_person(position = SB_get_random_ass_position())
    "She sends you a selfie of her ass covered in cum. You quickly text her back."
    mc.name "Nice! You should leave it right there and walk around the office like that!"
    "A moment later."
    the_person.char "Don't tempt me! See you at home tonight!"
    "You smile and resume your day."
    $ renpy.scene("Active")
    $ the_person.review_outfit(dialogue = False)
    return
