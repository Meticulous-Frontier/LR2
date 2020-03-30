init 1 python:
    def SB_fetish_cum_requirement():
        if time_of_day == 1 and mc.energy > 30:
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

    def SB_stephanie_cum_fetish_requirement():
        if mc.business.is_open_for_business():
            if renpy.random.randint(0,100) < 15:
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

    def add_sb_fetish_mom_cum_event():
        SB_fetish_mom_cum_event = Action("Mom Cum Fetish", SB_fetish_mom_cum_requirement, "SB_fetish_mom_cum_label")
        mc.business.mandatory_crises_list.append(SB_fetish_mom_cum_event)
    
    def add_sb_fetish_lily_cum_event():
        SB_fetish_lily_cum_event = Action("Sister Cum Fetish", SB_fetish_lily_cum_requirement, "SB_fetish_lily_cum_label")
        mc.business.mandatory_crises_list.append(SB_fetish_lily_cum_event)
        return

    def add_sb_fetish_cum_crisis(person):
        SB_fetish_cum_crisis = Action("Loves Cum.", SB_fetish_cum_requirement, "SB_fetish_cum_label", args = person)
        mc.business.mandatory_crises_list.append(SB_fetish_cum_crisis)
        return

    def add_sb_fetish_stephanie_cum_event():
        SB_fetish_stephanie_cum_action = Action("Stephanie Cum Fetish", SB_stephanie_cum_fetish_requirement, "SB_fetish_stephanie_cum_label")
        mc.business.mandatory_crises_list.append(SB_fetish_stephanie_cum_action)
        return

#SBC1
label SB_fetish_cum_label(the_person):
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
                $ the_clothing = None
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
                if the_person.outfit.has_mouth_cum():
                    #You came in her mouth! She now fetishes getting cum inside
                    #"Note, cum in mouth detected. Comment this later"
                    the_person.sexy_opinions["drinking cum"] = [FETISH_OPINION_VALUE, True]
                    the_person.sexy_opinions["creampies"] = [FETISH_OPINION_VALUE, True]
                    if not cum_internal_role in the_person.special_role:
                        the_person.special_role.append(cum_internal_role)
                        add_cum_slut_collar_to_base_outfit(the_person)
                if the_person.outfit.has_face_cum():
                    #You came on her face! Now she fetishes facials and getting cum on her.
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
        "Refuse":
            the_person.char "I'm sorry to hear that..." #TODO finish this

    $ the_person.review_outfit(dialogue = False) #Make sure to reset her outfit so she is dressed properly.
    $ mc.location.show_background()
    $ renpy.scene("Active")
    return

init 2 python:
    def SB_fetish_cum_dosage_requirement():
        if time_of_day > 0 and time_of_day < 4:
            if mc.business.is_open_for_business() and mc.is_at_work():
                return not get_fetish_cum_dosage_employee() is None
        return False

    def SB_fetish_shower_cum_requirement():
        if mc_at_home() and time_of_day==0:
            if SB_check_fetish(mom, cum_internal_role) or SB_check_fetish(mom, cum_external_role):
                return True
            if SB_check_fetish(lily, cum_internal_role) or SB_check_fetish(lily, cum_external_role):
                return True
        return False

    def get_fetish_cum_dosage_employee():
        meets_fetish_list = []
        for person in mc.business.get_employee_list():
            if SB_check_fetish(person, cum_internal_role) or SB_check_fetish(person, cum_external_role):
                meets_fetish_list.append(person)

        return get_random_from_list(meets_fetish_list)

    def get_fetish_shower_cum_girl():
        meets_fetish_list = []
        if SB_check_fetish(mom, cum_internal_role) or SB_check_fetish(mom, cum_external_role):
            meets_fetish_list.append(mom)
        if SB_check_fetish(lily, cum_internal_role) or SB_check_fetish(lily, cum_external_role):
            meets_fetish_list.append(lily)

        return get_random_from_list(meets_fetish_list)

    SB_fetish_cum_dosage_crisis = Action("Cum Fetish Dosage Crisis",SB_fetish_cum_dosage_requirement,"SB_fetish_cum_dosage_label")
    crisis_list.append([SB_fetish_cum_dosage_crisis, 5])

    SB_fetish_shower_cum = Action("Shower Surprise", SB_fetish_shower_cum_requirement, "SB_fetish_shower_cum_label")
    morning_crisis_list.append([SB_fetish_shower_cum, 5])


#SBC2
label SB_fetish_cum_dosage_label():
    $ the_person = get_fetish_cum_dosage_employee()
    if the_person is None:
        return
        
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
            call fuck_person(the_person, start_position = SB_cum_fetish_blowjob, start_object = make_floor(), girl_in_charge = False, position_locked = True) from _call_fuck_person_SBC20
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
    $ mc.change_location(bedroom)
    $ mc.location.show_background()
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
    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_SBC030
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
    call fuck_person(the_person, start_position = SB_sixty_nine, start_object = make_bed(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_fuck_person_SBC31
    $ the_report = _return
    if the_report.get("girl orgasms", 0) > 0:
        "[the_person.possessive_title] lays on top of you for a little longer, recovering. She idly licks your rapidly softening cock and nuzzles it for a bit."
    $ the_person.draw_person(position = "stand5")
    "[the_person.possessive_title] stands up."
    the_person.char "Okay... I think I'm good for now. It's time to get up! Why don't you hop in the shower while I go make some breakfast?"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] leave your room. Wow! What a night!"
    "You grab some clothes and head for the shower."

    python:
        the_person.review_outfit(dialogue = False) #Make sure to reset her outfit so she is dressed properly.
        mc.location.show_background()
        renpy.scene("Active")
    return "Advance Time"


#SBC4
label SB_fetish_lily_cum_label():
    $ the_person = lily
    $ mc.change_location(bedroom)
    $ mc.location.show_background()
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
        if the_person.outfit.has_mouth_cum():
            #You came in her mouth! She now fetishes getting cum inside
            #"Note, cum in mouth detected. Comment this later"
            the_person.sexy_opinions["drinking cum"] = [FETISH_OPINION_VALUE, True]
            the_person.sexy_opinions["creampies"] = [FETISH_OPINION_VALUE, True]
            if not cum_internal_role in the_person.special_role:
                the_person.special_role.append(cum_internal_role)
                add_cum_slut_collar_to_base_outfit(the_person)
        if the_person.outfit.has_face_cum():
            #You came on her face! Now she fetishes facials and getting cum on her.
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

    python:
        the_person.review_outfit(dialogue = False) #Make sure to reset her outfit so she is dressed properly.
        bedroom.show_background()
        renpy.scene("Active")
    return

#SBC5
label SB_fetish_shower_cum_label():
    $ the_person = get_fetish_shower_cum_girl()
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


#SBC060
label SB_fetish_stephanie_cum_label():
    $ the_person = stephanie
    if mc.location == mc.business.r_div: #Already in research
        "Suddenly, [the_person.possessive_title] looks up from her work and and speaks up."
        the_person.char "Hey [the_person.mc_title], I need to talk to you about something. Can we go somewhere private?"
    else:
        "You get a text message from [the_person.possessive_title]."
        the_person.char "Hey [the_person.mc_title], I need to talk to you about something. Can we meet somewhere private?"
        "You text her back."
    mc.name "Sure, meet me in my office."
    $ mc.change_location(office)
    $ mc.location.show_background()
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person)
    "[the_person.title] meets you there. You sit down and notice she closes the office door... and then locks it."
    mc.name "Have a seat. Is there something I can do for you?"
    "She sits down and immediately starts to talk to you."
    $ scene_manager.update_actor(the_person, position = "sitting")
    if the_person.love < 40 and the_person.obedience < 140:
        the_person.char "Look... I've been doing this for a while now. I know the real purpose of the serums you have me researching, and the effects they have on people..."
        the_person.char "I went along with things for a while because... well I don't know why. I guess I was just really into the science of things."
        "She shifts uncomfortably in her seat."
        $ scene_manager.update_actor(the_person, character_placement = character_right_flipped)
        the_person.char "Some of the things we've developed here are incredible. They can give people happiness, and expand their skills."
        the_person.char "The serums you've been giving out... I thought maybe you were just trying to make all the girls' lives here better."
        the_person.char "But... lately, I've found myself slipping further and further into these fantasies. It's making it hard to concentrate on my work!"
        the_person.char "I think you and I both know that this is a direct result of one of the serums we've been investigating lately... to give girls specific cravings. Fetishes even!"
        "She takes a second, she looks like she is on the verge of getting emotional. Then she straightens up and looks you straight in the eye"
        the_person.char "For god's sake, last night I had a dream that I was getting gangbanged and twelve guys came on, or in me, at the same time!"
        the_person.char "I'm sorry, but I can't do it anymore. You and I both know there isn't any real way to counter these effects. So, if I'm going to be a cum slut... I might as well enjoy it, right?"
        mc.name "I suppose so."
        $ scene_manager.update_actor(the_person, position = "stand4")
        "[the_person.possessive_title] pulls a serum out of her pocket."
        the_person.char "I don't have an antidote for this. It's the bimbo serum. I mixed it with a couple other things..."
        "This is some dangerous territory. If you let her go through with this, you are sure her sister will be pissed! Do you try to talk her down? Or let her do it?"
        menu:
            "Try to talk her down" if mc.charisma > 6:
                mc.name "Stop. You don't have to do that?"
                "She looks at the serum in her hand. Then back at you."
                the_person.char "Ummm, I don't know... I'm pretty sure I do."
                mc.name "Don't you want to know more... about the long term effects? Of the serums I mean?"
                the_person.char "You hardly need me to test something like that."
                mc.name "Who better to do it though? [the_person.title], you've been with me since the beginning. I'll help meet your needs. I know the cravings will be intense, but I promise I'll help!"
                "Her resolve is failing. She looks down at the serum again."
                mc.name "The science behind these chemicals is incredible. You KNOW you want to keep studying it together. With me!"
                the_person.char "[the_person.mc_title]... I want to. I really do. But I'm so scared right now."
                "You get up and walk around the desk."
                mc.name "It's okay. Sometimes science is a risky business. We can do this. Together. Let me have the serum."
                "She hesitates another moment. Then hands you the serum."
                the_person.char "Oh god... you better be right about this!"
                $ scene_manager.update_actor(the_person, position = "kissing")
                "She throws her arms around you, holding you close."
                the_person.char "The serums really are incredible. I do want to study them more. But first... I need your cum so bad! I can't think about anything else right now!"
                $ scene_manager.update_actor(the_person, position = "blowjob")
                "[the_person.possessive_title] gets on her knees and starts to pull down your trousers. It isn't long until she has your dick out and is stroking it eagerly."
                the_person.char "Come on [the_person.mc_title], you know what I need!"
                "She enthusiastically opens her mouth and sucks your hard cock into her mouth. She is desperate for your seed!"
                "You should consider carefully where you cum, it might change where she prefers to take cum from now on."
                call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_fuck_person_SBC060
                #Try and figure out where you came
                python:
                    if the_person.outfit.has_mouth_cum():
                        #You came in her mouth! She now fetishes getting cum inside
                        #"Note, cum in mouth detected. Comment this later"
                        the_person.sexy_opinions["drinking cum"] = [FETISH_OPINION_VALUE, True]
                        the_person.sexy_opinions["creampies"] = [FETISH_OPINION_VALUE, True]
                        if not cum_internal_role in the_person.special_role:
                            the_person.special_role.append(cum_internal_role)
                            add_cum_slut_collar_to_base_outfit(the_person)
                    if the_person.outfit.has_face_cum():
                        #You came on her face! Now she fetishes facials and getting cum on her.
                        #"Note, cum on face detected. Comment this later"
                        the_person.sexy_opinions["cum facials"] = [FETISH_OPINION_VALUE, True]
                        the_person.sexy_opinions["being covered in cum"] = [FETISH_OPINION_VALUE, True]
                        if not cum_external_role in the_person.special_role:
                            the_person.special_role.append(cum_external_role)
                            add_cum_slut_collar_to_base_outfit(the_person)
                the_person.char "Oh god... It's even better than I dreamed about last night."
                "[the_person.possessive_title] takes a minute to recover before standing up."
                $ scene_manager.update_actor(the_person, position = "stand2")
                the_person.char "Okay. We can do this. Together! I hope you realize the serums also greatly increase libido."
                mc.name "Don't worry."
                the_person.char "Well, I'll get back to work for now then. But I might swing by your office again later... you know... if I get hungry!"
                $ scene_manager.update_actor(the_person, position = "walking_away")
                "You say goodbye, and [the_person.possessive_title] turns and walks out of your office."
                "Looks like [the_person.title] has a cum fetish now!"
            "Let her take it":
                mc.name "I'm sorry, [the_person.title]. I didn't want it to be this way."
                "She looks at you. Her resolve stumbles, but only for a moment."
                the_person.char "Don't worry, I'll be the bimbo cum slut you've always wanted!"
                "She brings the serum to her mouth and drinks it down. She closes her eyes as it begins to take effect."
                $ the_person.change_happiness(15)
                if the_person.int > 1:
                    $ the_person.int = 1
                    $ mc.log_event(the_person.title + ": Intelligence reduced to 1", "float_text_blue")
                $ the_person.change_slut_core(20)
                $ slut_report = the_person.change_slut_temp(20)
                $ the_person.personality = bimbo_personality
                $ mc.log_event(the_person.title + ": Personality changed. Now: Bimbo", "float_text_pink")
                "It probably only takes a minute, but it feels like an eternity. Finally she opens her eyes."
                "She looks around a bit, seeming a bit confused about where she is."
                the_person.char "That's... we were talking about something... right?"
                "She looks at you. Her pupils are dilated and her breathing is calm."
                mc.name "We were just about done... with the talking anyway."
                the_person.char "That's right! We were going to do something else after though... right? I remember hoping that."
                "She begins to walk around the desk toward you."
                mc.name "That's right. You were going to get on your knees. And if everything goes well, I have a present for you."
                the_person.char "Oh! A present! I do love presents! Especially the ones I tend to get when I'm on my knees. I wonder what it could be!"
                $ scene_manager.update_actor(the_person, position = "blowjob")
                "[the_person.possessive_title] gets on her knees and skillfully removes your pants and underwear."
                "She gives your hardon a few eager strokes.."
                the_person.char "Mmm [the_person.mc_title]! You look so yummy!"
                "She enthusiastically opens her mouth and sucks your hard cock into her mouth. She is desperate for your seed!"
                "You should consider carefully where you cum, it might change where she prefers to take cum from now on."
                call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_fuck_person_SBC061
                #Try and figure out where you came
                python:
                    if the_person.outfit.has_mouth_cum():
                        #You came in her mouth! She now fetishes getting cum inside
                        #"Note, cum in mouth detected. Comment this later"
                        the_person.sexy_opinions["drinking cum"] = [FETISH_OPINION_VALUE, True]
                        the_person.sexy_opinions["creampies"] = [FETISH_OPINION_VALUE, True]
                        if not cum_internal_role in the_person.special_role:
                            the_person.special_role.append(cum_internal_role)
                            add_cum_slut_collar_to_base_outfit(the_person)
                    if the_person.outfit.has_face_cum():
                        #You came on her face! Now she fetishes facials and getting cum on her.
                        #"Note, cum on face detected. Comment this later"
                        the_person.sexy_opinions["cum facials"] = [FETISH_OPINION_VALUE, True]
                        the_person.sexy_opinions["being covered in cum"] = [FETISH_OPINION_VALUE, True]
                        if not cum_external_role in the_person.special_role:
                            the_person.special_role.append(cum_external_role)
                            add_cum_slut_collar_to_base_outfit(the_person)
                the_person.char "Your cum is amazing!"
                $ scene_manager.update_actor(the_person, position = "stand2")
                the_person.char "Mmm, thanks for that mister! I know this is kinda crazy but... I'm totally getting the urge for another load. Is there any more in those lonely looking balls for me?"
                mc.name "I'm sorry, but I have to get going."
                the_person.char "Awww! Okay. I hope you're around later though. I have a feeling I'm going to get hungry."
                $ scene_manager.update_actor(the_person, position = "stand4")
                the_person.char "I'll just go back to... whatever it was I was doing. What do I do here again?"
                mc.name "It doesn't matter, you can take the rest of the day off."
                the_person.char "Oh? Guess I'll just go find someone else to play with for a while. Your loss mister!"
                $ scene_manager.update_actor(the_person, position = "walking_away")
                "You say goodbye, and [the_person.possessive_title] turns and walks out of your office."
                "Looks like [the_person.title] has a  cum fetish now! But she is also a bimbo."
                "You are guessing she is probably not particularly fit for her job in research. Maybe you can move her somewhere else in the company?"

            "Try to talk her down \n{size=22}Requires High Charisma{/size}(disabled)" if mc.charisma <= 6:
                pass

    elif the_person.love < 70 and not girlfriend_role in the_person.special_role:   #She kinda trusts / loves you, but isn't fully committed and needs some convincing.
        the_person.char "Look... I've been doing this for a while now. I know the real purpose of the serums you have me researching, and the effects they have on people..."
        the_person.char "I went along with things for a while because I trust you. You've always impressed me with the way you do things."
        "She shifts uncomfortably in her seat."
        $ scene_manager.update_actor(the_person, character_placement = character_right_flipped)
        the_person.char "Some of the things we've developed here are incredible. They can give people happiness, and expand their skills."
        the_person.char "The serums you've been giving out... I thought maybe you were just trying to make all the girls' lives here better."
        the_person.char "But... lately, I've found myself slipping further and further into these fantasies. It's making it hard to concentrate on my work!"
        the_person.char "I think you and I both know that this is a direct result of one of the serums we've been investigating lately... to give girls specific cravings. Fetishes even!"
        "She takes a second, she looks like she is on the verge of getting emotional. Then she straightens up and looks you straight in the eye"
        the_person.char "For god's sake, last night I went to the bar and sucked off three different guys! In one night! That isn't normal!"
        the_person.char "I'm going to be honest here. I trust you, I'm sure you are just doing this for research or business purposes. But I'm at a tipping point here. I need you to answer this question honestly."
        mc.name "Okay, go ahead."
        the_person.char "Are you going to... you know... take responsibility for this? The urges are SO intense! You're the only guy here, I need your word that you'll help me take of these urges!"
        "From a pocket, she pulls out a serum that it looks like she has concocted."
        the_person.char "If you can't, I understand. But I don't think I can take it, knowing the serums gave me these urges... I need something to forget the research, and just move on with my life."
        the_person.char "I don't have an antidote for this. It's the bimbo serum. I mixed it with a couple other things... Maybe it's time for me to start a new life. I'm sure you could use me over in marketing or something, right?"
        "This is some dangerous territory. It sounds like she is looking to you to tell her what to do."
        "Become a bimbo, for real? Or, if you want her to stay the sexy, intelligent research lead, you'll have to help her with her newfound libido?"
        "If you have her take the serum, her sister will probably get very upset!"
        menu:
            "Help her":
                pass
            "Take the Serum":
                mc.name "I'm sorry, [the_person.title]. I didn't want it to be this way. I don't think I have the time to commit to something like that."
                $ scene_manager.update_actor(the_person, emotion = "sad")
                "She looks at you. You think you see a tear coming down from her eye."
                the_person.char "It's okay. The science is amazing. And I'm sure I'll enjoy life as... a bimbo butt slut."
                "She brings the serum to her mouth and drinks it down. She closes her eyes as it begins to take effect."
                $ the_person.change_happiness(-15)
                if the_person.int > 1:
                    $ the_person.int = 1
                    $ mc.log_event(the_person.title + ": Intelligence reduced to 1", "float_text_blue")
                $ the_person.change_slut_core(20)
                $ slut_report = the_person.change_slut_temp(20)
                $ the_person.personality = bimbo_personality
                $ mc.log_event(the_person.title + ": Personality changed. Now: Bimbo", "float_text_pink")
                "It probably only takes a minute, but it feels like an eternity. Finally she opens her eyes."
                "She looks around a bit, seeming a bit confused about where she is."
                the_person.char "That's... we were talking about something... right?"
                "She looks at you. Her pupils are dilated and her breathing is calm."
                mc.name "We were just about done... with the talking anyway."
                the_person.char "That's right! We were going to do something else after though... right? I remember hoping that."
                $ scene_manager.update_actor(the_person, position = "stand2")
                "She begins to walk around the desk toward you."
                mc.name "That's right. You were going to get on your knees. And if everything goes well, I have a present for you."
                the_person.char "Oh! A present! I do love presents! Especially the ones I tend to get when I'm on my knees. I wonder what it could be!"
                $ scene_manager.update_actor(the_person, position = "blowjob")
                "[the_person.possessive_title] gets on her knees and skillfully removes your pants and underwear."
                "She gives your hardon a few eager strokes.."
                the_person.char "Mmm [the_person.mc_title]! You look so yummy!"
                "She enthusiastically opens her mouth and sucks your hard cock into her mouth. She is desperate for your seed!"
                "You should consider carefully where you cum, it might change where she prefers to take cum from now on."
                call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_fuck_person_SBC062
                #Try and figure out where you came
                python:
                    if the_person.outfit.has_mouth_cum():
                        #You came in her mouth! She now fetishes getting cum inside
                        #"Note, cum in mouth detected. Comment this later"
                        the_person.sexy_opinions["drinking cum"] = [FETISH_OPINION_VALUE, True]
                        the_person.sexy_opinions["creampies"] = [FETISH_OPINION_VALUE, True]
                        if not cum_internal_role in the_person.special_role:
                            the_person.special_role.append(cum_internal_role)
                            add_cum_slut_collar_to_base_outfit(the_person)
                    if the_person.outfit.has_face_cum():
                        #You came on her face! Now she fetishes facials and getting cum on her.
                        #"Note, cum on face detected. Comment this later"
                        the_person.sexy_opinions["cum facials"] = [FETISH_OPINION_VALUE, True]
                        the_person.sexy_opinions["being covered in cum"] = [FETISH_OPINION_VALUE, True]
                        if not cum_external_role in the_person.special_role:
                            the_person.special_role.append(cum_external_role)
                            add_cum_slut_collar_to_base_outfit(the_person)
                the_person.char "Your cum is amazing!"
                $ scene_manager.update_actor(the_person, position = "stand2")
                the_person.char "Mmm, thanks for that mister! I know this is kinda crazy but... I'm totally getting the urge for another load. Is there any more in those lonely looking balls for me?"
                mc.name "I'm sorry, but I have to get going."
                the_person.char "Awww! Okay. I hope you're around later though. I have a feeling I'm going to get hungry."
                $ scene_manager.update_actor(the_person, position = "stand4")
                the_person.char "I'll just go back to... whatever it was I was doing. What do I do here again?"
                mc.name "It doesn't matter, you can take the rest of the day off."
                the_person.char "Oh? Guess I'll just go find someone else to play with for a while. Your loss mister!"
                $ scene_manager.update_actor(the_person, position = "walking_away")
                "You say goodbye, and [the_person.possessive_title] turns and walks out of your office."
                "Looks like [the_person.title] has a  cum fetish now! But she is also a bimbo."
                "You are guessing she is probably not particularly fit for her job in research. Maybe you can move her somewhere else in the company?"
                $ the_person.review_outfit(dialogue = False)
                $ renpy.scene("Active")
                return
        "She gives a deep sigh of relief."
        the_person.char "You have NO idea how glad I am to hear that."
        $ scene_manager.update_actor(the_person, position = "blowjob")
        "She comes around the desk then gets on her knees next to your chair. She looks up at you expectantly."
        the_person.char "Well? Why isn't your cock out? You said you would help!"
        mc.name "Oh. Right!"
        "You quickly pull down your zipper. She reaches in your trousers and pulls out your erection."
        "She enthusiastically opens her mouth and sucks your hard cock into her mouth. She is desperate for your seed!"
        "You should consider carefully where you cum, it might change where she prefers to take cum from now on."
        call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_fuck_person_SBC063
        #Try and figure out where you came
        python:
            if the_person.outfit.has_mouth_cum():
                #You came in her mouth! She now fetishes getting cum inside
                #"Note, cum in mouth detected. Comment this later"
                the_person.sexy_opinions["drinking cum"] = [FETISH_OPINION_VALUE, True]
                the_person.sexy_opinions["creampies"] = [FETISH_OPINION_VALUE, True]
                if not cum_internal_role in the_person.special_role:
                    the_person.special_role.append(cum_internal_role)
                    add_cum_slut_collar_to_base_outfit(the_person)
            if the_person.outfit.has_face_cum():
                #You came on her face! Now she fetishes facials and getting cum on her.
                #"Note, cum on face detected. Comment this later"
                the_person.sexy_opinions["cum facials"] = [FETISH_OPINION_VALUE, True]
                the_person.sexy_opinions["being covered in cum"] = [FETISH_OPINION_VALUE, True]
                if not cum_external_role in the_person.special_role:
                    the_person.special_role.append(cum_external_role)
                    add_cum_slut_collar_to_base_outfit(the_person)
        the_person.char "Oh god... Every load just feels so good!"
        "[the_person.possessive_title] takes a minute to recover before standing up."
        $ scene_manager.update_actor(the_person, position = "stand2")
        the_person.char "Okay. We can do this. Together! I hope you realize the serums also greatly increase libido."
        mc.name "Don't worry. I'm definitely aware."
        the_person.char "Well, I'll get back to work for now then. But I might swing by your office again later... you know... if I get hungry!"
        $ scene_manager.update_actor(the_person, position = "walking_away")
        "You say goodbye, and [the_person.possessive_title] turns and walks out of your office."
        "Looks like [the_person.title] has a cum fetish now!"
    else:
        the_person.char "Before I get started, I just want to make sure you understand. I support you completely. I'm not mad or anything, just a little concerned."
        the_person.char "I've been doing this for a while now. I know the real purpose of the serums you have me researching, and the effects they have on people..."
        the_person.char "I went along with things for a while because I trust you. Maybe even love you. You've always impressed me with the way you do things."
        the_person.char "Some of the things we've developed here are incredible. They can give people happiness, and expand their skills."
        the_person.char "The serums you've been giving out... I thought maybe you were just trying to make all the girls' lives here better."
        the_person.char "But... lately, I've found myself slipping further and further into these fantasies. It's making it hard to concentrate on my work!"
        the_person.char "I think you and I both know that this is a direct result of one of the serums we've been investigating lately... to give girls specific cravings. Fetishes even!"
        "She takes a second, she looks like she is on the verge of getting emotional. Then she straightens up and looks you straight in the eye"
        the_person.char "For god's sake, all I can think about is your cock blowing load after load all over me, in me, anywhere you want!"
        the_person.char "I trust you. It took me a while to realize what is going on, but I understand it now."
        the_person.char "This is the next step in our relationship. The urges are SO intense! You're the only guy here, I need you to help me take care of these urges!"
        the_person.char "I'm sure that relying on you for this can only bring us closer together."
        if the_person.relationship != "Single":
            $ SO_title = SO_relationship_to_title(the_person.relationship)
            mc.name "Wait, don't you have a [SO_title]?"
            the_person.char "So? He isn't here at work with me all day is he? He can cum for me when I get home, but I need you to do it while I'm here!"
        "Sounds like she thinks the whole reason you gave her the serums is because... you want to take things to the next level? For now, it is probably better if you just go along with it."
        mc.name "You're right. I probably should have been more honest about it, but I thought this would help bring us closer together."
        "She gives a deep sigh of relief."
        the_person.char "You have NO idea how glad I am to hear that."
        "[the_person.possessive_title] walks around your desk then gets on her knees."
        $ scene_manager.update_actor(the_person, position = "blowjob")

        the_person.char "Well? Why isn't your cock out? You said you would help!"
        mc.name "Oh. Right!"
        "You quickly pull down your zipper. She reaches in your trousers and pulls out your erection."
        "She enthusiastically opens her mouth and sucks your hard cock into her mouth. She is desperate for your seed!"
        "You should consider carefully where you cum, it might change where she prefers to take cum from now on."
        call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_fuck_person_SBC064
        #Try and figure out where you came
        python:
            if the_person.outfit.has_mouth_cum():
                #You came in her mouth! She now fetishes getting cum inside
                #"Note, cum in mouth detected. Comment this later"
                the_person.sexy_opinions["drinking cum"] = [FETISH_OPINION_VALUE, True]
                the_person.sexy_opinions["creampies"] = [FETISH_OPINION_VALUE, True]
                if not cum_internal_role in the_person.special_role:
                    the_person.special_role.append(cum_internal_role)
                    add_cum_slut_collar_to_base_outfit(the_person)
            if the_person.outfit.has_face_cum():
                #You came on her face! Now she fetishes facials and getting cum on her.
                #"Note, cum on face detected. Comment this later"
                the_person.sexy_opinions["cum facials"] = [FETISH_OPINION_VALUE, True]
                the_person.sexy_opinions["being covered in cum"] = [FETISH_OPINION_VALUE, True]
                if not cum_external_role in the_person.special_role:
                    the_person.special_role.append(cum_external_role)
                    add_cum_slut_collar_to_base_outfit(the_person)
        the_person.char "Oh god... I can't get enough of your cock! It tastes so good."
        "[the_person.possessive_title] takes a minute to recover before standing up."
        $ scene_manager.update_actor(the_person, position = "stand2")
        the_person.char "Okay. I can already feel the urge to get another load from you, but I know you are a busy guy."
        the_person.char "I'll be back later, okay? I have a feeling I'm going to be hungry for more!"
        $ scene_manager.update_actor(the_person, position = "walking_away")
        "You say goodbye, and [the_person.possessive_title] turns and walks out of your office."
        "Looks like [the_person.title] has a cum fetish now!"

    $ scene_manager.clear_scene()
    $ the_person.review_outfit(dialogue = False)
    $ renpy.scene("Active")
    return
