init 1 python:
    #Requirement functions

    def cum_fetish_employee_intro_requirement():
        return False

    def cum_fetish_family_intro_requirement():
        return False

    def cum_fetish_generic_intro_requirement():
        return False

    def cum_fetish_mom_intro_requirement():
        return False

    def cum_fetish_lily_intro_requirement():
        return False

    def cum_fetish_rebecca_intro_requirement():
        return False

    def cum_fetish_gabrielle_intro_requirement():
        return False

    def cum_fetish_stephanie_intro_requirement():
        return False

    def cum_fetish_alex_intro_requirement():
        return False

    def cum_fetish_nora_intro_requirement():
        return False

    def cum_fetish_emily_intro_requirement():
        return False

    def cum_fetish_christina_intro_requirement():
        return False

    def cum_fetish_starbuck_intro_requirement():
        return False

    def cum_fetish_sarah_intro_requirement():
        return False

    def cum_fetish_ophelia_intro_requirement():
        return False

    def cum_fetish_candace_intro_requirement():
        return False

    def cum_fetish_dawn_intro_requirement():
        return False

    def cum_fetish_erica_intro_requirement():
        return False

    def cum_fetish_ashley_intro_requirement():
        return False

    def add_cum_slut_collar_to_base_outfit(person):
        person.base_outfit.remove_all_collars()

        cs_collar = cum_slut_collar.get_copy()
        cs_collar.colour = [.1,.1,.1,.9]
        cs_collar.pattern = "Pattern_1"
        cs_collar.colour_pattern = [.95,.95,.95,.9]
        person.base_outfit.add_accessory(cs_collar)
        return

init 2 python:
    def add_cum_fetish(person):
        person.max_opinion_score("drinking cum")
        person.max_opinion_score("being covered in cum")
        person.add_role(cum_fetish_role)
        person.update_sex_skill("Oral", 6)
        person.event_triggers_dict["LastCumFetish"] = day
        add_cum_slut_collar_to_base_outfit(person)
        return



### Function labels

label cum_fetish_employee_intro_label(the_person):
    $ the_person.arousal = 40
    $ the_person.event_triggers_dict["LastCumFetish"] = day
    $ fetish_after_hours_unlock()
    "It's the end of the day, and you and your employees are packing up to head out. However, one of your employees is acting a little suspicious and milling around."
    "The rest of the girls in her department pack up and head out, while she clearly is wasting time. You decide to ask her if she's okay."
    $ the_person.draw_person()
    "You walk up to her."
    mc.name "Hey [the_person.title]. You doing okay? Everyone else has left for the day."
    the_person "Oh! Hi [the_person.mc_title]."
    "She looks around the room, noting that its empty."
    the_person "I know its... time to leave but..."
    "As you step closer to you, she suddenly rushes at you and wraps her arms around you."
    $ the_person.draw_person(position = "kissing")
    the_person "I'm sorry! I'm not ready to go home yet! I wanted to get your attention but I just couldn't do it with everyone around..."
    "She starts to kiss your neck. Her hand reaches down and starts to stroke your cock through your clothes."
    the_person "I know this is really forward, but can I ask you for a favor?"
    mc.name "I'd say you are in a good position to do that."
    the_person "I just wanted to know if I could suck you off. I'm not sure why, but lately everytime I think about your cock, my mouth starts to water and it sounds so good..."
    "Wow, sounds like [the_person.title] is really hungry for your dick. You wonder if she might be developing a fetish from your cum proclivity serums."
    "Do you want to try and train her into a cumslut?"
    if the_person in unique_character_list:
        "Warning, this character is unique, and may have unique fetish dialogue. If you continue, you may miss this dialogue!"
    menu:
        "Train her to be a cumslut" if mc.energy > 40:
            pass
        "Too tired" if mc.energy <= 40:
            pass
            #TODO re add the event for this person for the next day.
            return
        "Refuse":
            "You decide to leave her alone for now. You might revisit this decision at a later date."
            $ fetish_after_hours_unlock()
            $ clear_scene()
            return
    mc.name "I'll let you do that, but only if you do as I say when I finish."
    the_person "Oh? That sounds fun..."
    $ the_person.draw_person(position = "blowjob")
    "[the_person.possesive_title] drops to her knees and unzips your pants, then pulls your cock out."
    the_person "Mmm, it looks so tasty."
    "She opens her mouth and slowly licks some of your precum from the tip. You watch as she works her tongue around her mouth, savoring the taste."
    $ mc.arousal = 15
    if the_person.tits_available():
        "As she takes you in her mouth, she runs her fingers along her breasts, pinching and pulling at her nipples."
    else:
        mc.name "Get your tits out. I want something nice to look at."
        the_person "Mmm, okay."
        $ the_person.strip_outfit(exclude_upper = False, exclude_lower = True)
        "When she finishes, she takes you back in her mouth, she runs her fingers along her breasts, pinching and pulling at her nipples."
    call fuck_person(the_person, start_position = cum_fetish_blowjob, skip_intro = True, position_locked = True) from _call_fuck_cum_fetish_employee_intro_01
    mc.name "Damn that was good. You really got off on that, didn't you?"
    the_person "Mmm... yeah..."
    mc.name "I want you to wipe some cum on your fingers, and rub it into your tits."
    the_person "Oh? That's... oh god that sounds hot..."
    "She takes her hand and wipes a bit of your cum off her face, then brings them down to her breasts..."
    $ the_person.cum_on_tits()
    $ the_person.change_arousal(20)
    mc.name "That's it. Feels good, doesn't it?"
    the_person "Your cum feels so good on my skin... its electric!"
    mc.name "Good girl. Keeping going, rub some on your stomach..."
    the_person "Oh my god..."
    $ the_person.cum_on_stomach()
    "Taking what she can, [the_person.possesive_title] goes further, rubbing your cum onto her belly."
    $ the_person.change_arousal(20)
    "[the_person.title] is breathing rapidly now. When she looks up at you, her pupils are actually a little dialated. She is REALLY getting off on this!"
    mc.name "That's a good cumslut. You know whats coming next, right?"
    the_person "Oh god, probably me soon!"
    mc.name "Do it. Rub some cum around your cunt and get yourself off for me."
    the_person "Oh fuck yes!"
    $ the_person.draw_person(position = "kneeling1")
    $ the_person.change_arousal (25)
    "[the_person.possesive_title] immediately begins to finger herself rapidly. Once in a while she will wipe a bit of cum off her face, rub it in circles around her slit, then keep going."
    the_person "Oh god! [the_person.mc_title] I'm cumming!"
    $ the_person.have_orgasm()
    "[the_person.title] cries out as she cums. Her body convulses in waves as a strong orgasm overtakes her."
    "It takes several seconds for her to catch her breath."
    $ add_cum_fetish(the_person)
    the_person "That... was amazing..."
    "You put your cock back in your pants and grab your stuff."
    mc.name "You are such a good cum slut. I'll make sure to make use of your mouth again soon. Have a goodnight [the_person.title]."
    the_person "Good night [the_person.mc_title]!"
    "You leave the office, setting the doors to lock automatically after [the_person.title] leaves. She definitely seems to have developed a fetish for your cum!"
    return False

label cum_fetish_family_intro_label():
    return False

label cum_fetish_generic_intro_label():
    return False

label cum_fetish_mom_intro_label():
    $ the_person = mom
    $ the_person.event_triggers_dict["LastCumFetish"] = day
    $ mc.change_location(bedroom)
    $ mc.location.show_background()
    "Tired from a long day, you quickly fall asleep."
    "You are having some very pleasant dreams. [the_person.possessive_title] is posing for you in some sexy lingerie, then gets down on her knees..."
    "Her velvet soft mouth wraps around your cock, and she begins to bob her head eagerly up and down your erection."
    "[the_person.possessive_title]'s skilled tongue teases and strokes you. The pleasure is so intense you slowly start to awaken from your naughty dream."
    "However, as you awaken, the pleasure you are experiencing continues."
    $ the_person.draw_person(position = "blowjob")
    "You look down and discover that [the_person.possessive_title] is between your legs. She has pulled your underwear down and is sucking you off."
    $ the_person.break_taboo("sucking_cock")
    mc.name "[the_person.title]? What are you..."
    "[the_person.possessive_title] interrupts you."
    the_person.char "Shhh, just lay back. I need your cum right now. I couldn't sleep, I was craving you so bad."
    "You lay back, [the_person.possessive_title] continues to suck you off."
    "Your mind is racing. You've been giving her your serums for a while now. Maybe she has developed a fetish for your cum?"
    "[the_person.possessive_title] keeps her mouth open wide and bobs her head back and forth to slide your cock in and out. The feeling of her soft, warm mouth sends shivers up your spine."
    "She moans slightly as she strokes you with her soft, velvet lips. She pulls off for a second and looks at you."
    the_person.char "[the_person.mc_title]... I want you to cum wherever you want, okay? Just do it in me or on me somewhere..."
    "She opens her mouth and goes back to work. Her skilled mouth is quickly bringing you to an orgasm!"
    menu:
        "Cum in her mouth":
            "You rest your hand on her head, guiding her as she sucks you off."
            "With a little encouragement, you pull [the_person.possessive_title]'s head down a little further with each stroke."
            mc.name "That's it [the_person.title]. I'm going to cum in your mouth and I want you to swallow every drop."
            "[the_person.possessive_title] moans. She is ready for her prize."
            mc.name "Fuck, here I come!"
            "[the_person.possessive_title] moans and looks you in the eyes. She pulls off until just the tip of your cock is in her mouth and she begins to stroke you off eagerly."
            "You erupt in orgasm into her greedy mouth. [the_person.possessive_title] is swallowing rapidly as you fill her mouth with your cum."
            "[the_person.possessive_title] is moaning uncontrollably around your twitching cock."
            $ the_person.cum_in_mouth()
            $ the_person.draw_person(position = "blowjob")
            $ add_cum_fetish(the_person)
            "You look down and see [the_person.possessive_title]. She uses her finger to wipe up a bit of cum that leaked out of her mouth and licks it clean."

        "Cum on her face":
            "You rest your hand on her head, slowly gathering her hair up."
            mc.name "That's it [the_person.title]. I'm going to cum all over that pretty little face of yours."
            "[the_person.possessive_title] moans. She is ready for her prize."
            mc.name "Fuck, here I come!"
            "[the_person.possessive_title] moans and looks you in the eyes. She pulls off your cock and strokes you eagerly, waiting for the first splash across her face."
            "You erupt in orgasm and shoot your load across her glowing face. Her pupils dilate as her cum addicted brain registers the presence of your cum on her skin."
            "[the_person.possessive_title] moans uncontrollably with every spurt"
            $ the_person.cum_on_face()
            $ the_person.draw_person(position = "blowjob")
            $ add_cum_fetish(the_person)
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
    $ the_person.apply_outfit(special_fetish_nude_outfit)
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
    "[the_person.possessive_title] leave your room. Wow! What a night! She definitely has a fetish for your cum now."
    "You grab some clothes and head for the shower."

    python:
        the_person.apply_planned_outfit()
        mc.location.show_background()
        clear_scene()
    return "Advance Time"

label cum_fetish_lily_intro_label():
    $ the_person = lily
    $ the_person.event_triggers_dict["LastCumFetish"] = day
    $ mc.change_location(bedroom)
    $ mc.location.show_background()
    "You wake up a little groggy. Your head kinda hurts, so you grab some clothes and head towards the bathroom to take a hot shower. Hopefully the steam will help you feel better."
    $ home_shower.show_background()
    "You stand in the shower, enjoying the hot water for several minutes. The steam is beginning to cloud up the bathroom."
    "You are surprised when the shower door opens. You see [the_person.possessive_title] getting in the shower with you."
    $ the_person.apply_outfit(special_fetish_nude_outfit)
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
    "You see [the_person.possessive_title] reaches down with one hand and start to touch herself. She runs her tongue up and down your shaft a few times."
    the_person.char "It's like I'm thirsty... but no amount of water I drink makes my thirst go away... Only when I think about drinking your sweet cum do I feel any better..."
    "[the_person.possessive_title] opens her mouth and starts to suck you off. You feel her soft, velvet mouth wrapped around you."
    $ the_person.break_taboo("sucking_cock")
    "[the_person.possessive_title] begins bobbing her head up and down eagerly, hungry for your delicious cum."
    # call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = True, position_locked = True) from _call_fuck_person_SBC40
    call get_fucked(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, allow_continue = False) from _call_fuck_person_SBC40
    $ add_cum_fetish(the_person)
    "[the_person.possessive_title] is moaning ecstatically. You start to worry that [mom.possessive_title] might hear."
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
    "She definitely seems to have developed a fetish for your cum."

    python:
        the_person.apply_planned_outfit()
        mc.location.show_background()
        clear_scene()
    return

label cum_fetish_rebecca_intro_label():
    return False

label cum_fetish_gabrielle_intro_label():
    return False

label cum_fetish_stephanie_intro_label():
    return False

label cum_fetish_alex_intro_label():
    return False

label cum_fetish_nora_intro_label():
    return False

label cum_fetish_emily_intro_label():
    return False

label cum_fetish_christina_intro_label():
    return False

label cum_fetish_starbuck_intro_label():
    return False

label cum_fetish_sarah_intro_label():
    return False

label cum_fetish_ophelia_intro_label():
    return False

label cum_fetish_candace_intro_label():
    return False

label cum_fetish_dawn_intro_label():
    return False

label cum_fetish_erica_intro_label():
    return False

label cum_fetish_ashley_intro_label():
    return False
