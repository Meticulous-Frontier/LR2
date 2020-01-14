init 1 python:
    def SB_fetish_cum_requirement():
        if time_of_day == 1:
            if mc.energy > 30:
                if mc.business.is_open_for_business():
                    if mc.is_at_work():
                        return True
        return False

    def SB_fetish_mom_cum_requirement():
        if mc_asleep() and day % 7 is not 4: # not on Friday nights
            if mc.energy > 30:  #Must have the energy to handle a long sexy night
                return True
        return False

    def SB_fetish_lily_cum_requirement():
        if mc_at_home() and time_of_day==0:
            return True
        return False

    def SB_get_cum_score(the_person):
        cum_score = 0
        for cumListEntry in FETISH_CUM_OPINION_LIST:
            cum_score += the_person.get_opinion_score(cumListEntry)

        return cum_score

    def add_cum_slut_collar_to_base_outfit(person):
        person.base_outfit.remove_all_collars()

        cs_collar = cum_slut_collar.get_copy()
        cs_collar.colour = [.1,.1,.1,.9]
        cs_collar.pattern = "Pattern_1"
        cs_collar.colour_pattern = [.95,.95,.95,.9]
        person.base_outfit.add_accessory(cs_collar)
        return

    SB_cum_outfit = Outfit("A Special Night")
    SB_cum_outfit.add_upper(lace_bra.get_copy(),colour_pink)
    SB_cum_outfit.add_feet(garter_with_fishnets.get_copy(), colour_pink)
    SB_cum_outfit.add_feet(high_heels.get_copy(), colour_pink)

    SB_cum_nude_outfit = Outfit("Nude")

    SB_fetish_mom_cum = Action("Mom Cum Fetish", SB_fetish_mom_cum_requirement, "SB_fetish_mom_cum_label")
    SB_fetish_lily_cum = Action("Sister Cum Fetish", SB_fetish_lily_cum_requirement, "SB_fetish_lily_cum_label")
    SB_fetish_cum_crisis = Action("Loves Cum.", SB_fetish_cum_requirement, "SB_fetish_cum_label")

#SBC1
label SB_fetish_cum_label(the_person):
    #$ the_person = FETISH_cum_EVENT_TARGET
    "You are just finishing up with with some work before you get ready for lunch. You hear a friendly voice greet you as you pull your packed lunch from the desk."
    the_person.char "Hey [the_person.mc_title]! That sure looks good!"
    $ the_person.draw_person()
    ###Draw the girl###
    "You give her a quick wave as she walks up to you. You assumed she was talking about your lunch, but quickly notice she is looking at your crotch."
    the_person.char "So, I forgot to pack a lunch today, and I'm pretty hungry, so I was wondering if, you know..."
    "Her hand travels down to your crotch. She begins to stroke you as she continues..."
    the_person.char "... if maybe while you were eating your lunch, I could bother you for a salty snack."
    "[the_person.possessive_title] looks at you with hopeful eyes."
    the_person.char "I could get down under your desk! If anyone walks by they won't even know!"
    menu:
        "Help yourself":  #This begins the sex scene
            mc.name "I suppose I could help you out with that. Are you sure you don't want to share any of my lunch?"
            the_person.char "Oh! That's okay, [the_person.mc_title]."
            "[the_person.possessive_title] lowers her voice and whispers huskily in your ear."
            the_person.char "I'm not sure what is going on with me but... lately... I've just been craving your cum so bad..."
            "You aren't surprised, it's been a while since you started giving her the serum for increased cum enjoyment."
            the_person.char "I feel like I'm going crazy..."
            if the_person.outfit.tits_available():
                "You check out [the_person.possessive_title]. Her delicious looking tits are on full display."
            else:
                "You check out [the_person.possessive_title]. You decide it might be easier to get off if you have a little more skin to look at while she sucks you."
                mc.name "Hey, before you get under the desk, why don't you get your tits out? It'd be great to have something to look at..."
                "[the_person.possessive_title] smiles wide"
                the_person.char "Of course! Let me get this off for you..."
                while not the_person.outfit.tits_available():
                    $ the_clothing = the_person.outfit.get_upper_ordered()[-1]
                    "[the_person.possessive_title] takes off her [the_clothing.name]"
                    $ the_person.draw_animated_removal(the_clothing)
            "[the_person.possessive_title] gropes her breasts with both hands, looking for your approval."
            mc.name "Mmm, that looks great. I think I'll eat my lunch now..."
            "[the_person.possessive_title] giggles."
            the_person.char "Mmm... me too!"
            "[the_person.possessive_title] quickly gets down underneath your desk, before you sit down."
            $ the_person.draw_person(position = "blowjob")
            "She immediately gets to work, pulling your dick out of your pants. You quickly feel the soft, velvet mouth wrapped around you."
            "[the_person.possessive_title] begins bobbing her head up and down eagerly, hungry for your delicious cum."
            "You should be careful where you cum. It is likely her fetish may develop based on where you cum!"
            ###cum Scene, standing variant###
            call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = True, position_locked = True) from _call_fuck_person_SBC10
            #Try and figure out where you came
            python:
                for sb_access in the_person.outfit.accessories:
                    if sb_access.name == "Mouth Cum":    #You came in her mouth! She now fetishes getting cum inside
                        #"Note, cum in mouth detected. Comment this later"
                        the_person.sexy_opinions["drinking cum"] = [FETISH_OPINION_VALUE, True]
                        the_person.sexy_opinions["creampies"] = [FETISH_OPINION_VALUE, True]
                        if not cum_internal_role in the_person.special_role:
                            the_person.special_role.append(cum_internal_role)
                            add_cum_slut_collar_to_base_outfit(the_person)
                    if sb_access.name == "Face Cum":     #You came on her face! Now she fetishes facials and getting cum on her.
                        #"Note, cum on face detected. Comment this later"
                        the_person.sexy_opinions["cum facials"] = [FETISH_OPINION_VALUE, True]
                        the_person.sexy_opinions["being covered in cum"] = [FETISH_OPINION_VALUE, True]
                        if not cum_external_role in the_person.special_role:
                            the_person.special_role.append(cum_external_role)
                            add_cum_slut_collar_to_base_outfit(the_person)
            "[the_person.possessive_title] is moaning ecstatically below your desk."
            if SB_check_fetish(the_person, cum_external_role):
                "Glancing down, you see [the_person.possessive_title] running her hands along her face, then down to her chest. She is rubbing your cum into her skin."
                the_person.char "Mmm... it feels so good! That first splash is always the best..."
            elif SB_check_fetish(the_person, cum_internal_role):
                "Glancing down, you see [the_person.possessive_title] licking her fingers. There isn't a trace of your cum anywhere, she has swallowed every drop."
                the_person.char "Mmm... it's all inside me now... right where it belongs!"
            "[the_person.possessive_title] stands up."
            $ the_person.draw_person()
            the_person.char "Wow, that was amazing, [the_person.mc_title]. I don't know what has been coming over me lately..."
            "[the_person.possessive_title] blushes and pauses..."
            mc.name "Did you get what you were hoping for?"
            "You tease her."
            the_person.char "Oh, I think I'm good for today... but I'm sure it won't be long until I get hungry again..."
            "She's been under the influence of your serums for a while now... you wonder if she's developed a cum fetish..."
            "[the_person.possessive_title] runs her hand through her hair. She licks her lips and smiles at you."
            the_person.char "Thanks again, [the_person.mc_title]. We should do this again... and soon."
            "You wave goodbye to [the_person.possessive_title] and finish eating your lunch."
            $ SB_CALCULATE_RANDOM_EVENT_RATE()
        "Refuse":
            the_person.char "I'm sorry to hear that..." #TODO finish this
            $ SB_CALCULATE_RANDOM_EVENT_RATE()

    $ SB_CALCULATE_RANDOM_EVENT_RATE()
    $ FETISH_CUM_EVENT_INUSE = False
    $ the_person.reset_arousal()
    $ the_person.review_outfit(dialogue = False) #Make sure to reset her outfit so she is dressed properly.
    $ mc.location.show_background()
    $ renpy.scene("Active")
    return

init 2 python:
    def SB_fetish_cum_dosage_requirement():
        if time_of_day < 4:
            if mc.is_at_work():
                if SB_check_fetish(person, cum_internal_role) or SB_check_fetish(person, cum_external_role):
                    return True
        return False

    def SB_fetish_shower_cum_requirement():
        if mc_at_home() and time_of_day==0:
            if SB_check_fetish(mom, cum_internal_role) or SB_check_fetish(mom, cum_external_role):
                return True
            if SB_check_fetish(lily, cum_internal_role) or SB_check_fetish(lily, cum_external_role):
                return True
        return False

    SB_fetish_cum_dosage_crisis = Action("Cum Fetish Dosage Crisis",SB_fetish_cum_dosage_requirement,"SB_fetish_cum_dosage_label")
    crisis_list.append([SB_fetish_cum_dosage_crisis, 5])

    SB_fetish_shower_cum = Action("Shower Surprise", SB_fetish_shower_cum_requirement, "SB_fetish_shower_cum_label")
    morning_crisis_list.append([SB_fetish_shower_cum, 5])


#SBC2
label SB_fetish_cum_dosage_label():
    $ meets_fetish_list = []
    python:
        for person in mc.business.get_employee_list():
            if SB_check_fetish(person, cum_internal_role) or SB_check_fetish(person, cum_external_role):
                meets_fetish_list.append(person)

        the_person = get_random_from_list(meets_fetish_list)
        del meets_fetish_list
    "As you finish up with one of your work tasks, you decide to take a quick break."
    "You step into your office and sit down for a minute. You hop on your laptop and start browsing the internet."
    "*KNOCK KNOCK*"
    $ the_person.draw_person()
    "You look up and see [the_person.possessive_title] at your door."
    if mc.business.is_open_for_business():
        mc.name "Hello [the_person.title], come in."
        "[the_person.possessive_title] walks into your office."
        the_person.char "Hey [the_person.mc_title]. So... I saw you walk into your office a minute ago and I was just thinking that its been a while..."
        mc.name "A while since what?"
        "[the_person.possessive_title] stutters for a second."
        the_person.char "...A while since you let me have your cum, so I thought..."
        "[the_person.possessive_title] voice trails off. It seems she is craving it again."
    else:
        "You are surprised to see her, considering the business is closed for the day."
        mc.name "Hello [the_person.title], come in."
        "[the_person.possessive_title] walks into your office."
        the_person.char "Oh [the_person.mc_title]! Thank goodness you are here, you are just the man I wanted to see."
        the_person.char "You know how much I need your cum... so I was wondering... want to take a five minute break? I promise I won't be a bother!"
    menu:
        "Suck me off":
            the_person.char "Yes! Oh thank you [the_person.mc_title]!"
            "[the_person.possessive_title] walks over to you and immediately drops down on her knees. You consider asking her to strip down a bit, but she is already too busy stroking your cock."
            $ the_person.draw_person(position = "blowjob")
            ###cum Scene, standing variant###
            call fuck_person(the_person, start_position = SB_cum_fetish_blowjob, start_object = make_floor(), girl_in_charge = True, position_locked = True) from _call_fuck_person_SBC20
            the_person.char "Oh my god, thank you [the_person.mc_title]... I wish I had time make you cum again... but I know you're a busy a man..."
            "[the_person.possessive_title] starts to get up. Her hunger for cum satisfied for now."
            the_person.char "Thanks again, [the_person.mc_title]. Don't hesitate to ask if you ever need to be... you know... serviced."
            "You wave goodbye to [the_person.possessive_title] as she leaves your office. Damn that was good!"
        "No Thanks":
            "[the_person.possessive_title] is caught completely off guard by your refusal."
            $ the_person.change_obedience(-10)
            $ the_person.change_happiness(-10)
            the_person.char "Oh!... Okay... Well... hey I understand... Maybe some other time yeah?"
            "[the_person.possessive_title] quickly sulks off. Maybe you should've?"
        "Too Tired" if mc.energy < 30:
            "[the_person.possessive_title] is surprised by your answer."
            $ the_person.change_obedience(-5)
            $ the_person.change_happiness(-5)
            the_person.char "Oh! I'm sorry... I know you work so hard around here. Maybe tomorrow then?"
            "[the_person.possessive_title] quickly sulks off."
    python:
        the_person.review_outfit(dialogue = False)
        renpy.scene("Active")
    return

#SBC3
label SB_fetish_mom_cum_label():
    $ the_person = mom
    "Tired from a long day, you quickly fall asleep."
    "You are having some very pleasant dreams. [the_person.possessive_title] is posing for you in some sexy lingerie, then gets down on her knees..."
    "Her velvet soft mouth wraps around your cock, and she begins to bob her head eagerly up and down your erection."
    "[the_person.possessive_title]'s skilled tongue teases and strokes you. The pleasure is so intense you slowly start to awaken from your naughty dream."
    "However, as you awaken, the pleasure you are experiencing continues."
    $ the_person.draw_person(position = "blowjob")
    "You look down and discover that [the_person.possessive_title] is between your legs. She has pulled your underwear down and is sucking you off."
    mc.name "[the_person.title]? What are you..."
    "[the_person.possessive_title] interrupts you."
    the_person.char "Shhh, just lay back. I need your cum right now. I couldn't sleep, I was craving you so bad."
    "You lay back, [the_person.possessive_title] continues to suck you off."
    "Your mind is racing. You've been giving her your serums for a while now. Maybe she has developed a fetish for your cum?"
    "[the_person.possessive_title] keeps her mouth open wide and bobs her head back and forth to slide your cock in and out. The feeling of her soft, warm mouth sends shivers up your spine."
    "She moans slightly as she strokes you with her soft, velvet lips. She pulls off for a second and looks at you."
    the_person.char "[the_person.mc_title]... I want you to cum wherever you want, okay? Just do it in me or on me somewhere..."
    "She opens her mouth and goes back to work. Her skilled mouth is quickly bringing you to an orgasm!"
    "You carefully consider where to cum. This may have an effect on how her cum fetish develops!"
    menu:
        "Cum in her mouth" if not SB_check_fetish(the_person, cum_internal_role):
            "You rest your hand on her head, guiding her as she sucks you off."
            "With a little encouragement, you pull [the_person.possessive_title]'s head down a little further with each stroke."
            mc.name "That's it [the_person.title]. I'm going to cum in your mouth and I want you to swallow every drop."
            "[the_person.possessive_title] moans. She is ready for her prize."
            mc.name "Fuck, here I come!"
            "[the_person.possessive_title] moans and looks you in the eyes. She pulls off until just the tip of your cock is in her mouth and she begins to stroke you off eagerly."
            "You erupt in orgasm into her greedy mouth. [the_person.possessive_title] is swallowing rapidly as you fill her mouth with your cum."
            "[the_person.possessive_title] is moaning uncontrollably around your spasming cock."
            $ the_person.cum_in_mouth()
            $ the_person.draw_person(position = "blowjob")
            $ the_person.sexy_opinions["drinking cum"] = [FETISH_OPINION_VALUE, True]
            $ the_person.sexy_opinions["creampies"] = [FETISH_OPINION_VALUE, True]
            $ the_person.special_role.append(cum_internal_role)
            $ add_cum_slut_collar_to_base_outfit(the_person)
            "You look down and see [the_person.possessive_title]. She uses her finger to wipe up a bit of cum that leaked out of her mouth and licks it clean."

        "Cum on her face" if not SB_check_fetish(the_person, cum_external_role):
            "You rest your hand on her head, slowly gathering her hair up."
            mc.name "That's it [the_person.title]. I'm going to cum all over that pretty little face of yours."
            "[the_person.possessive_title] moans. She is ready for her prize."
            mc.name "Fuck, here I come!"
            "[the_person.possessive_title] moans and looks you in the eyes. She pulls off your cock and strokes you eagerly, waiting for the first splash across her face."
            "You erupt in orgasm and shoot your load across her glowing face. Her pupils dilate as her cum addicted brain registers the presence of your cum on her skin."
            "[the_person.possessive_title] moans uncontrollably with every spurt"
            $ the_person.cum_on_face()
            $ the_person.draw_person(position = "blowjob")
            $ the_person.sexy_opinions["cum facials"] = [FETISH_OPINION_VALUE, True]
            $ the_person.sexy_opinions["being covered in cum"] = [FETISH_OPINION_VALUE, True]
            $ the_person.special_role.append(cum_external_role)
            $ add_cum_slut_collar_to_base_outfit(the_person)
            "Slowly recovering, you look at [the_person.possessive_title]'s cum covered face. Her eyes are closed and she is absentmindedly playing with some of the cum that is starting to run down her neck."

    the_person.char "Oh... I needed that so bad... you have no idea."
    $ the_person.reset_arousal()
    "[the_person.possessive_title] slowly crawls up the bed and lays down next to you. You put your arm around her."
    "Completely satisfied, she quickly falls asleep."
    "Wow! [the_person.possessive_title] just woke you up, in the middle of the night, with an amazing blowjob, took your load, then cuddled up and fell asleep with you."
    "You have a feeling that this is only the beginning of things between you and her."
    "You slowly fall asleep, enjoying the warmth of her body."
    call SB_process_overnight_no_events() from _SB_overnight_SBC030
    "When morning comes, you feel a stirring in your loins again as you start to slowly wake up. The now familiar feeling of [the_person.possessive_title]'s mouth feels amazing."
    $ the_person.apply_outfit(SB_cum_nude_outfit)
    $ the_person.draw_person( position = "blowjob")
    "She senses that you are beginning to awake."
    the_person.char "Good morning, [the_person.mc_title]. It's a new day... and I need another load of your cum..."
    "Last night she sucked you off. Maybe this morning you should repay the favor?"
    mc.name "Good morning. Why don't you get on top of me? I wanna eat your pussy for breakfast."
    the_person.char "Oh! That sounds good. As long as you promise to cum for me..."
    mc.name "Don't worry, I promise."
    "[the_person.possessive_title] repositions and swings a leg over your body, presenting her pussy right in front of your face. You waste no time and start to flick your tongue around her slit."
    the_person.char "Mmm, that feels good [the_person.mc_title]... and your cock... it looks so good... I wanna swallow it whole!"
    "[the_person.possessive_title] begins to please you in return. Taking you into her mouth, she begins sucking you off."
    call fuck_person(the_person, start_position = SB_sixty_nine, start_object = make_bed(), skip_intro = True, girl_in_charge = True, position_locked = True) from _call_fuck_person_SBC31
    $ the_report = _return
    if the_report.get("girl orgasms", 0) > 0:
        "[the_person.possessive_title] lays on top of you for a little longer, recovering. She idly licks your rapidly softening cock and nuzzles it for a bit."
    $ the_person.draw_person(position = "stand5")
    "[the_person.possessive_title] stands up."
    the_person.char "Okay... I think I'm good for now. It's time to get up! Why don't you hop in the shower while I go make some breakfast?"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] leave your room. Wow! What a night!"
    "You grab some clothes and head for the shower."

    $ SB_CALCULATE_RANDOM_EVENT_RATE()
    $ FETISH_CUM_EVENT_INUSE = False
    python:
        the_person.review_outfit(dialogue = False) #Make sure to reset her outfit so she is dressed properly.
        mc.location.show_background()
        renpy.scene("Active")
    return


#SBC4
label SB_fetish_lily_cum_label():
    $ the_person = lily
    "You wake up a little groggy. Your head kinda hurts, so you grab some clothes and head towards the bathroom to take a hot shower. Hopefully the steam will help you feel better."
    $ home_shower.show_background()
    "You stand in the shower, enjoying the hot water for several minutes. The steam is beginning to cloud up the bathroom."
    "You are surprised when the shower door opens. You see [the_person.possessive_title] getting in the shower with you."
    $ the_person.apply_outfit(SB_cum_nude_outfit)
    $ the_person.draw_person()
    the_person.char "Good morning [the_person.mc_title]. Mind if I join you?"
    "You are surprised. She hasn't been this direct with you before. You quickly invite her in."
    the_person.char "Thanks! You were taking forever, and I got tired of waiting. This will be more fun than showering by myself, anyway."
    "[the_person.possessive_title] grabs some soap and begins soaping up her body. You watch her as she works the soap into her skin."
    the_person.char "Hey, can you get my back?"
    mc.name "Sure."
    $ the_person.draw_person(position = "back_peek")
    "[the_person.possessive_title] hands you her bath sponge. You give her back a good scrubbing."
    "When you finish you hand her the bath sponge back, but she doesn't turn around. Instead, she slowly leans back until she is up against you."
    "Her body now completely up against yours, your cock is rapidly hardening, resting in the crack of her ass. She starts to slowly move her hips back and forth, grinding against you."
    "[the_person.possessive_title] moans as she grinds against you. She turns around and wraps her arms around you."
    $ the_person.draw_person(position = "kissing")
    the_person.char "[the_person.mc_title]... it feels so good against me. I want to taste it!"
    "You are a little bit surprised."
    mc.name "Are you sure you want that? Or do you want me to fuck you?"
    "[the_person.possessive_title] shakes her head."
    the_person.char "No... I'm not sure what is going on with me lately, but I've just been craving your cum so bad..."
    $ the_person.draw_person(position = "blowjob")
    "[the_person.possessive_title] gets down on her knees in front of you."
    the_person.char "I feel like I'm going crazy... but I can't stop thinking about you. About swallowing your cum, or you cumming all over my face, or my body..."
    "You see [the_person.possessive_title] reach down with one hand and start to touch herself. She runs her tongue up and down your shaft a few times."
    the_person.char "It's like I'm thirsty... but no amount of water I drink makes my thirst go away... Only when I think about drinking your sweet cum do I feel any better..."
    "[the_person.possessive_title] opens her mouth and starts to suck you off. You feel her soft, velvet mouth wrapped around you."
    "[the_person.possessive_title] begins bobbing her head up and down eagerly, hungry for your delicious cum."
    "You should be careful where you cum. It is likely her fetish may develop based on where you cum!"
    call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = True, position_locked = True) from _call_fuck_person_SBC40
    #Try and figure out where you came
    python:
        for sb_access in the_person.outfit.accessories:
            if sb_access.name == "Mouth Cum":    #You came in her mouth! She now fetishes getting cum inside
                #"Note, cum in mouth detected. Comment this later"
                the_person.sexy_opinions["drinking cum"] = [FETISH_OPINION_VALUE, True]
                the_person.sexy_opinions["creampies"] = [FETISH_OPINION_VALUE, True]
                if not cum_internal_role in the_person.special_role:
                    the_person.special_role.append(cum_internal_role)
                    add_cum_slut_collar_to_base_outfit(the_person)
            if sb_access.name == "Face Cum":     #You came on her face! Now she fetishes facials and getting cum on her.
                #"Note, cum on face detected. Comment this later"
                the_person.sexy_opinions["cum facials"] = [FETISH_OPINION_VALUE, True]
                the_person.sexy_opinions["being covered in cum"] = [FETISH_OPINION_VALUE, True]
                if not cum_external_role in the_person.special_role:
                    the_person.special_role.append(cum_external_role)
                    add_cum_slut_collar_to_base_outfit(the_person)

    "[the_person.possessive_title] is moaning ecstatically. You start to worry that [mom.possessive_title] might hear."
    if SB_check_fetish(the_person, cum_external_role):
        "Glancing down, you see [the_person.possessive_title] running her hands along her face, then down to her chest. She is rubbing your cum into her skin."
        the_person.char "Mmm... it feels so good! That first splash is always the best..."
    elif SB_check_fetish(the_person, cum_internal_role):
        "Glancing down, you see [the_person.possessive_title] licking her fingers. There isn't a trace of your cum anywhere, she has swallowed every drop."
        the_person.char "Mmm... it's all inside me now... right where it belongs!"
    $ the_person.draw_person(position = "kissing")
    "[the_person.possessive_title] stands up and hugs you."
    the_person.char "Wow, that was amazing, [the_person.mc_title]. I don't know what has been coming over me lately..."
    "You hold her close."
    the_person.char "That was exactly what I've been craving."
    "She sighs happily."
    the_person.char "But... I can already feel the thirst. It's going to come back isn't it?"
    "Her body shivers slightly."
    the_person.char "I guess maybe its those serums I've been testing for you. You'll help me, right? I'm going to need your cum again... and soon I think!"
    mc.name "Of course, [the_person.title]. I'll always be here for you."
    "[the_person.possessive_title]'s body melts into yours as she hears your words."
    the_person.char "Okay... I'm going to hop out of the shower now."
    "[the_person.possessive_title] gets out. You finish up with your shower, balls empty and ready for the day!"


    $ SB_CALCULATE_RANDOM_EVENT_RATE()
    $ FETISH_CUM_EVENT_INUSE = False

    python:
        the_person.review_outfit(dialogue = False) #Make sure to reset her outfit so she is dressed properly.
        bedroom.show_background()
        renpy.scene("Active")

        for morn_event in morning_crisis_list:
            if morn_event[0].name == "Sister Cum Fetish":
                #renpy.say("","DEBUG: Successfully located shower, attempting removal and replacement.")
                morning_crisis_list.remove(morn_event)
    return "True"

#SBC5
label SB_fetish_shower_cum_label():
    $ meets_fetish_list = []
    python:
        if SB_check_fetish(mom, cum_internal_role):
            meets_fetish_list.append(mom)
        elif SB_check_fetish(mom, cum_external_role):
            meets_fetish_list.append(mom)
        if SB_check_fetish(lily, cum_internal_role):
            meets_fetish_list.append(lily)
        elif SB_check_fetish(lily, cum_external_role):
            meets_fetish_list.append(lily)

        the_person = get_random_from_list(meets_fetish_list)
        del meets_fetish_list
    "You wake up a little groggy. Your head kinda hurts, so you grab some clothes and head towards the bathroom to take a hot shower. Hopefully the steam will help you feel better."
    $ home_shower.show_background()
    "You stand in the shower, enjoying the hot water for several minutes. The steam is beginning to cloud up the bathroom."
    "You hear the shower door open and see [the_person.possessive_title] getting in the shower with you."
    $ the_person.apply_outfit(SB_cum_nude_outfit)
    $ the_person.draw_person()
    the_person.char "Good morning [the_person.mc_title]. Mind if I join you?"
    mc.name "Of course! Come on in."
    the_person.char "Thanks! I saw you get in the shower this morning... I was feeling thirsty, so I decided to hop in."
    "[the_person.possessive_title] reaches down and begins to stroke your cock."
    the_person.char "I had so many crazy dreams last night, all about you... cumming really hard!"
    the_person.char "It was amazing! You just kept cumming and cumming... all over me, and I was swallowing as much as a could and I was covered in it..."
    $ the_person.draw_person(position = "blowjob")
    "[the_person.possessive_title] gets down on her knees."
    the_person.char "I'm sorry, I know I shouldn't approach you like this... but I can't help myself this morning! Give me your cum please!"
    "[the_person.possessive_title] looks up at your from her knees. She looks you right in the eyes as she leans forward and slides her lips over the tip of your dick."
    call fuck_person(the_person, start_position = SB_cum_fetish_blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = True, position_locked = True) from _call_fuck_person_SBC50
    the_person.char "Oh my god, thank you [the_person.mc_title]. I needed that so bad."
    "[the_person.possessive_title] stands up. Her hunger for cum satisfied for now."
    $ the_person.draw_person(position = "stand4")
    the_person.char "Okay... I'm going to hop out and let your finish showering now. Please give me more cum soon!"
    "[the_person.possessive_title] gets out. You finish up with your shower, balls empty and ready for the day!"

    python:
        the_person.review_outfit(dialogue = False) #Make sure to reset her outfit so she is dressed properly.
        mc.location.show_background()
        renpy.scene("Active")

    return
