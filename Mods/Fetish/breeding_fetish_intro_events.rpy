init -1 python:
    def breeding_fetish_employee_intro_requirement():
        if time_of_day == 3:
            if mc.business.is_open_for_business():
                if mc.is_at_work():
                    return True
        return False

    def breeding_fetish_generic_intro_requirement(the_person):
        if the_person.location != the_person.home:
            return True
        return False

    def breeding_fetish_family_intro_requirement(the_person):
        if the_person.location == the_person.home:
            if the_person.location.get_person_count() == 1: #She is alone in her bedroom
                return True
        return False

    def breeding_fetish_mom_intro_requirement(): #TODO this should be a morning mandatory crisis event.
        return True #??? Is this right?

    def breeding_fetish_lily_intro_requirement(the_person):
        if lily.location == lily.home:
            if lily_bedroom.get_person_count() == 1:
                return True
        return False

    def breeding_fetish_rebecca_intro_requirement():
        return False

    def breeding_fetish_gabrielle_intro_requirement():
        return False

    def breeding_fetish_stephanie_intro_requirement():
        if mc.business.is_open_for_business():
            if stephanie.location == stephanie.work:
                if renpy.random.randint(0,100) < 25:
                    return True
        return False

    def breeding_fetish_emily_intro_requirement():
        return False

    def breeding_fetish_christina_intro_requirement():
        return False

    def breeding_fetish_starbuck_intro_requirement():
        if starbuck.shop_progress_stage > 0:
            if time_of_day == 3:
                return True
        return False

    def breeding_fetish_sarah_intro_requirement():
        if not day%7 == 5 and mc_asleep() and sarah.event_triggers_dict.get("threesome_unlock", 0) >= 1:
            return True
        return False

    def breeding_fetish_ophelia_intro_requirement():
        return False

    def breeding_fetish_erica_intro_requirement():
        return False

    def breeding_fetish_candace_intro_requirement(the_person):
        if candace.location == candace.work:
            return True
        return False

    def breeding_fetish_ashley_intro_requirement():
        return False


init 2 python:
    # breeding_fetish_employee_intro = Action("Employee breeding fetish intro", breeding_fetish_employee_intro_requirement, "breeding_fetish_employee_intro_label")
    breeding_fetish_non_employee_intro = Action("Non Employee breeding fetish intro", breeding_fetish_generic_intro_requirement, "breeding_fetish_generic_intro_label")
    breeding_fetish_family_intro = Action("Family Member breeding fetish intro", breeding_fetish_family_intro_requirement, "breeding_fetish_family_intro_label")
    breeding_fetish_mom_intro = Action("Mom breeding fetish intro", breeding_fetish_mom_intro_requirement, "breeding_fetish_mom_intro_label")
    breeding_fetish_lily_intro = Action("Lily breeding fetish intro", breeding_fetish_lily_intro_requirement, "breeding_fetish_lily_intro_label")
    breeding_fetish_rebecca_intro = Action("Rebecca breeding fetish intro", breeding_fetish_rebecca_intro_requirement, "breeding_fetish_rebecca_intro_label")
    breeding_fetish_gabrielle_intro = Action("Gabrielle breeding fetish intro", breeding_fetish_gabrielle_intro_requirement, "breeding_fetish_gabrielle_intro_label")
    breeding_fetish_stephanie_intro = Action("Stephanie breeding fetish intro", breeding_fetish_stephanie_intro_requirement, "breeding_fetish_stephanie_intro_label")
    breeding_fetish_emily_intro = Action("Emily breeding fetish intro", breeding_fetish_emily_intro_requirement, "breeding_fetish_emily_intro_label")
    breeding_fetish_christina_intro = Action("Christina breeding fetish intro", breeding_fetish_christina_intro_requirement, "breeding_fetish_christina_intro_label")
    breeding_fetish_starbuck_intro = Action("Starbuck breeding fetish intro", breeding_fetish_starbuck_intro_requirement, "breeding_fetish_starbuck_intro_label")
    breeding_fetish_sarah_intro = Action("Sarah breeding fetish intro", breeding_fetish_sarah_intro_requirement, "breeding_fetish_sarah_intro_label")
    breeding_fetish_ophelia_intro = Action("Ophelia breeding fetish intro", breeding_fetish_ophelia_intro_requirement, "breeding_fetish_ophelia_intro_label")
    breeding_fetish_erica_intro = Action("Erica breeding fetish intro", breeding_fetish_erica_intro_requirement, "breeding_fetish_erica_intro_label")
    breeding_fetish_candace_intro = Action("Candace breeding fetish intro", breeding_fetish_candace_intro_requirement, "breeding_fetish_candace_intro_label")
    breeding_fetish_ashley_intro = Action("Ashley breeding fetish intro", breeding_fetish_ashley_intro_requirement, "breeding_fetish_ashley_intro_label")

init 3 python:
    def add_breed_me_collar_to_base_outfit(person):
        person.base_outfit.remove_all_collars()

        bm_collar = breed_collar.get_copy()
        bm_collar.colour = [1,.41,.71,.9]
        bm_collar.pattern = "Pattern_1"
        bm_collar.colour_pattern = [.1,.1,.1,.9]
        person.base_outfit.add_accessory(bm_collar)
        return

    def add_breeding_fetish(person):
        person.add_role(breeding_fetish_role)
        person.update_sex_skill("Vaginal", 6)
        person.event_triggers_dict["LastBreedingFetish"] = day
        add_breed_me_collar_to_base_outfit(person)
        return

init 50 python:
    def debug_set_stats_for_breeding_fetish_mins(the_person):
        the_person.situational_sluttiness = {} #A dict that stores a "situation" string and the corresponding amount it is contributing to the girls sluttiness.
        the_person.situational_obedience = {}
        the_person.arousal = 0
        the_person.energy = the_person.max_energy
        the_person.max_opinion_score("bareback sex")
        the_person.core_sluttiness = 70
        the_person.sluttiness = 70
        the_person.obedience = 0
        the_person.happiness = 100
        the_person.love = 0
        the_person.on_birth_control = False
        return

    def abort_breeding_fetish_intro(the_person): #Use this function to exit a anal fetish scene for whatever reason (something fails, MC choice, etc.)
        the_person.event_triggers_dict["breeding_fetish_start"] = False
        the_person.remove_role(breeding_fetish_role)

#Fetish Intro Labels
label breeding_fetish_employee_intro_label(the_person):
    $ fetish_after_hours_unlock()
    "You are finishing up the last of your work today and closing up. All your employees should be gone for the day."
    "However, you are surprised when you are interrupted by someone."
    $ the_person.draw_person()
    the_person "Ah! [the_person.mc_title]... I was hoping to catch you alone. I need to talk to you about something."
    mc.name "Good evening [the_person.title]. What can I do for you?"
    the_person "Ah... more like... what can you do to me..."
    "Did you hear that right?"
    mc.name "Oh?"
    the_person "I umm... I mean... sorry."
    "She looks a bit flustered for a second, but quickly gathers her thoughts and starts to talk to you."
    if the_person.age < 35:
        the_person "Well, you know sir, I'm still pretty young, and lately I've been dealing with some pretty intense biological... urges..."
    else:
        the_person "Well, you know sire, I'm starting to get a bit older, and as my biological clock is ticking I've been getting some pretty intense... urges..."
    the_person "I'm not sure why, but lately I've been having these fantasies about having sex, raw, over and over, and getting filled with cum!"
    "That's not surprising. Recently, you've been giving your employee serums that greatly increase her urges to reproduce..."
    if the_person.knows_pregnant():
        the_person "Obviously I'm already pregnant, but umm, I've really been craving your cock inside me, twitching and pulsing your loads deep, over and over..."
    else:
        the_person "I don't know how to say this but, I've been craving you, and your cock, twitching and pulsing load after load deep inside me! Knocking me up!"
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
    $ the_person.draw_person(position = "missionary")
    "You force her down onto her back."
    the_person "Oh my god..."
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
    the_person "Oh god! Yes do it! Oh fuck!"
    "Still holding her hands down, you start to thrust rapidly. It's time to give this horny slut a creampie!"
    call fuck_person(the_person, start_position = breeding_missionary , private = True, skip_intro = True, position_locked = True, asked_for_condom = True) from _employee_gets_breeding_fetish_01
    if the_person.has_creampie_cum():
        the_person "Oh god! Its so deep! Oh thank you so much [the_person.mc_title]!"
    else:
        #TODO what to put here?
        pass
    $ add_breeding_fetish(the_person)
    if the_person.knows_pregnant():
        the_person "I don't care if I am already pregnant... Please do that again! My body was made to take your cum like that!"
    else:
        the_person "I hope that did it, but you'd better cum inside me again and again anyway!"
    "You slowly back away from [the_person.title], allowing her to get up."
    $ the_person.draw_person()
    "[the_person.possessive_title] slowly stands up, her legs are a little unsteady."
    mc.name "I need to get a few more things done before I close up the office. From now on, you are my breeding stock. Be ready to take my cum whenever I tell you to!"
    the_person "Yes! Yes sir! I'll be ready, don't worry!"
    $ the_person.draw_person()
    "You say goodbye to [the_person.title]."
    "[the_person.possessive_title] now has a fetish to get bred by you!"
    return #Needs testing

label breeding_fetish_family_intro_label(the_person):
    $ the_person.draw_person(position = "back_peek")
    "You walk into [the_person.possessive_title]'s bedroom. She is looking at herself in the mirror, but turns to when she hears you walk in."
    the_person "Oh hey [the_person.mc_title]. I was just getting ready to head for bed."
    "She takes one last look at herself in the mirror, then turns around."
    $ the_person.draw_person(position = the_person.idle_pose)
    the_person "Do you want to cuddle with me for a little bit?"
    mc.name "Sounds nice."
    $ the_person.draw_person(position = "missionary")
    "You lay down next to [the_person.possessive_title] as she lays down on her back. You rest your head on her chest and put your arm across her."
    "For a while you simply enjoy the heat of each other's bodies. She is the first to break the silence."
    if the_person.knows_pregnant():
        the_person "Do you think its weird, if I told you I love this feeling? Being pregnant, making babies. It's like my body was made to do this, over and over again."
        the_person "I'm already looking forward to making another one, and this one isn't even here yet!"

    elif the_person.age < 35:
        the_person "Do you think I'm too old to have a baby? My hormones are in overdrive lately..."
        mc.name "No way. With modern medical science, women are having babies older and older, into their late forties even."
    else:
        the_person "My hormones are being crazy lately... would it be weird if I told you I... want to get knocked up?"
        mc.name "I'd imagine that's a pretty normal thing. We don't survive as a species if we don't have a drive to reproduce, right?"
    the_person "I suppose so."
    "You move your hand to her belly and begin to rub it. You've been giving her doses of your reproduction proclivity serums recently."
    "You wonder if she is on the verge of developing a fetish. Do you want to try and push her over the edge?"
    if the_person in unique_character_list:
        "Warning, this character is unique, and may have unique fetish dialogue. If you continue, you may miss this dialogue!"
    menu:
        "Attempt to train her breeding fetish" if mc.energy > 40:
            pass
        "Too tired" if mc.energy <= 40:
            pass
            #TODO re add the event for this person for the next day.
            return
        "Too risky, leave her alone":
            pass
            return
    "You decide it's time to train [the_person.possessive_title] to be your own personal breeding stock."
    "You push yourself up and on top of [the_person.title]. She puts her arms around you as your body begins to press against hers."
    mc.name "Honestly, I think its pretty normal to have desires like that."
    the_person "Yeah..."
    "You start to kiss her along her neck and then whisper in her ear."
    mc.name "To have a man pin you down, fuck you senseless, then dump his risky load deep inside you, over and over."
    $ the_person.change_arousal(20)
    the_person "Ah, that does sound nice..."
    mc.name "It sounds more than nice though, doesn't it? It's what you NEED. A bull, who fucks you and knocks you up, over and over. Like some kind of livestock."
    the_person "Ahhh, yeah! Oh god..."
    $ the_person.change_arousal(20)
    "You reach down and start to pull your cock out."
    the_person "but... we're... you know... family..."
    mc.name "Shhh, its okay. You can trust me, right? We're both consenting adults, who just happen to be related."
    "She bites her lip. It's clear from the look in her eyes that she wants it badly, but is afraid to take the leap."
    mc.name "Tell you what, let's go a little farther, and if it feels wrong we can stop."
    $ the_person.add_situational_slut("situation",20, "I can stop if I want to...")
    "She nods her head in agreement."
    if the_person.outfit.vagina_available():
        "You finish pulling your cock out and begin to rub it along her slit."
    else:
        "As you finish pulling your cock out, [the_person.possessive_title] reaches down and starts pulling her bottoms off."
        $ the_person.strip_outfit(exclude_upper = True, position = "missionary")
    $ the_person.change_arousal(10)
    if the_person.love < 0:
        the_person "I can't believe I'm saying this, and with you of all people..."
        the_person "But I'm ready! Just... just put it in me! Raw!"
    else:
        the_person "My brain says this is wrong, but my body keeps saying its so right!"
        the_person "Fuck me [the_person.mc_title], I want you to fill me with your cum!"
    "You run you cock along her slit a couple more times, then start to push it inside. She moans as you bottom out inside of her and start to fuck."
    call fuck_person(the_person, start_position = breeding_missionary , private = True, skip_intro = True, position_locked = True, asked_for_condom = True) from _family_gets_breeding_fetish_01
    $ add_breeding_fetish(the_person)
    $ the_person.draw_person(position = "missionary")
    if the_person.knows_pregnant():
        the_person "I know I'm already pregnant... but that was so good. Even after this one comes, I want to keep doing this!"
    else:
        the_person "Oh god, you're right. It feels so right getting seeded by you."
    "You slowly roll off of [the_person.title] and lay beside her."
    mc.name "Make sure you lay like this for a while. Keep those swimmers as deep as you can."
    "You get up and start to get dressed."
    the_person "Do you... want to stay with me tonight?"
    mc.name "I can't stay tonight, but from now on, you are my breeding stock. Be ready to take my cum whenever I tell you to."
    the_person "Yes! Yes sir! I'll be ready, don't worry!"
    "You say goodbye to [the_person.title]."
    "[the_person.possessive_title] now has a fetish to get bred by you!"
    $ the_person.clear_situational_slut("situation")
    return #Needs testing

label breeding_fetish_generic_intro_label(the_person): #This function to be used for generic non employee, non unique girls
    $ the_person.arousal = 40
    "As you walk into [mc.location.name], you notice [the_person.title]. She notices you also and approaches."
    $ the_person.draw_person()
    the_person "Hello [the_person.mc_title]! It's good to see you!"
    "You take a moment to look at her. Her cheeks seem flushed... Her nipples are poking against the fabric of her shirt. Is she... Aroused?"
    mc.name "It's good to see you also."
    the_person "Hey, I was just thinking about texting you. Are you busy right now?"
    mc.name "Probably not."
    "She leans forward and talks quietly in your ear."
    the_person "My place is right around the corner... want a tour of my bedroom?"
    "Wow, she is being very forward. It's not surprising though. Recently, you've dosed her with your reproduction proclivity serums."
    "It's possible she might be on the verge of developing a fetish. If you go back to her place, you can push her over the edge into having a breeding fetish!"
    if the_person in unique_character_list:
        "Warning, this character is unique, and may have unique fetish dialogue. If you continue, you may miss this dialogue!"
    menu:
        "Go to her place" if mc.energy > 40:
            mc.name "A tour would be nice. Lead the way."
        "Too tired" if mc.energy <= 40:
            pass
            #TODO re add the event for this person for the next day.
            return
        "Not now":
            mc.name "I'm sorry [the_person.title], I've got errands to accomplish. Maybe another time."
            $ the_person.change_love(-2)
            $ the_person.change_happiness(-5)
            the_person "Ah, okay. I see."
            return False

    "[the_person.title] takes your hand and you step away with her. After a few minutes of walking, you find yourself at her place."
    "She quickly unlocks the front door and pulls you inside."
    if the_person.home not in mc.known_home_locations:
        $ mc.known_home_locations.append(the_person.home)
    $ mc.change_location(the_person.home)
    $ mc.location.show_background()
    $ the_person.draw_person(position = "kissing")
    "She throws her arms around you and you start to make out. You hands drop to her ass and you start to grope her aggressively."
    the_person "Oh god, I'm not sure I can make it to the bedroom."
    $ the_person.draw_person(position = "against_wall")
    $ the_person.change_arousal(10) #50
    "You pick her up and carry her to her bedroom. She is grinding against you the whole way."
    "Knowing the reason she is so aroused, you start to talk dirty with her."
    mc.name "Are you on birth control, [the_person.title]?"
    the_person "You know I'm not..."
    mc.name "Good. When we get to your bed, I'm going to throw you down on it, pin you down, and fuck you until until I cum deep inside you."
    if the_person.knows_pregnant():
        the_person "Do it! I'm already pregnant, but I want to feel your seed deep inside me!"
    else:
        the_person "Oh fuck, but I could... I could get..."
        mc.name "Pregnant? You're right."
    $ the_person.draw_person(position = "missionary")
    mc.name "That's what you want, isn't it? For me to pin you down and breed you, over and over, like the little slut you are."
    the_person "Oh [the_person.mc_title], I really do!"
    if the_person.outfit.vagina_available():
        "You pullyour cock out and begin to rub it along her inviting slit."
    else:
        "As you pull your cock out, [the_person.possessive_title] pulls her bottoms off."
        $ the_person.strip_outfit(exclude_upper = True)
        "When she finishes you run your cock all along her inviting slit."

    $ the_person.change_arousal(10) #60
    the_person "Just shove it in! I'm ready!"
    "You decide to give her what she wants, for now. You grab her hips and then push yourself inside of her sopping wet cunt."
    call fuck_person(the_person, start_position = breeding_missionary , private = True, skip_intro = True, position_locked = True, asked_for_condom = True) from _generic_anyone_gets_breeding_fetish_01
    $ add_breeding_fetish(the_person)
    $ the_person.draw_person(position = "missionary")
    "When you finish, she lays back, just rubbing her hand along her belly."
    if the_person.knows_pregnant():
        the_person "I know I'm already pregnant... but that was so good. Even after this one comes, I want to keep doing this!"
    else:
        the_person "Oh god, that was amazing. I hope... I hope that did it!"
    "You slowly roll off of [the_person.title] and lay beside her."
    mc.name "Make sure you lay like this for a while. Keep my semen as deep as you can."
    "You get up and start to get dressed."
    the_person "Can we do this again soon?"
    mc.name "I plan to. Keep your cunt ready for me, anytime I want to dump my load inside you."
    the_person "Yes! Don't worry, I'll be ready!"
    "You say goodbye to [the_person.title]."
    "[the_person.possessive_title] now has a fetish to get bred by you!"


    return

label breeding_fetish_mom_intro_label(): # Needs testing
    $ the_person = mom
    $ the_person.on_birth_control = False
    $ the_person.event_triggers_dict["Mom_forced_off_bc"] = False   #Atleast set it up so that she doesn't want to get on BC without MC asking.
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
    the_person "Ohhh... good morning honey! Mommy needs your seed inside her this morning... and I'm not taking no for an answer!"
    "You are a little surprised by her forcefulness. Lately you've been giving her serums that should make her a bit more submissive..."
    the_person "I had such vivid dreams last night... you were fucking me and kept cumming inside me over and over and over!"
    the_person "My belly started bigger and my tits started to leak milk and I loved it so much..."
    "Ahh, you've been giving her serums that increase her drive to reproduce. Looks like they've finally driven her over the urge and given her a breeding fetish!"
    $ the_person.change_arousal (30)
    $ mc.change_arousal(20)
    "She starts to rock her hips back and forth. You reach up and start to fondle her tits as they sway back and forth."
    mc.name "Mmmm, I can't wait to drink milk from your tits again, [the_person.title]."
    if the_person.knows_pregnant(): #She already knows she's pregnant
        the_person "Oh god I know I'm already pregnant, but I just want you to fuck your cum into me over and over!"
    else:
        the_person "Oh god, can we really do this? Will you fuck your cum into me over and over until I'm pregnant? I want that so bad!"
    mc.name "Of course I'll give you my cum. From now on, you'll be my own personal mare. I'll breed you every chance I get."
    $ the_person.change_arousal(15)
    the_person "Oh [the_person.mc_title], that's so hot... I want it now! I'm going the ride the cum out of you now!"
    call get_fucked(the_person, the_goal = "vaginal creampie", start_position = cowgirl, private = True, skip_intro = True, allow_continue = False) from _mom_breeding_fetish_intro_01
    if the_person.has_creampie_cum():
        the_person "Oh god... I need to keep it all in..."
        "[the_person.title] reaches her hand down, trying to keep your cum inside of her, but failing, as your cum drips down the inside of her thighs."
    else:
        #TODO what to put here?
        pass
    mc.name "Don't worry, I'll give you more soon."
    "She chuckles, then smiles at you."
    the_person "You better... Every day! Even if I am pregnant..."
    $ add_breeding_fetish(the_person)
    the_person "It's good for the baby, I think! It knows when mommy is getting taken care of... How happy you make her..."
    $ the_person.draw_person(position = "missionary")
    "[the_person.title] lays down beside you for a while. Soon though, it is time to get up and ready for the day."
    the_person "Have a good day. Don't forget, try to be home for dinner tonight! You need to keep your energy up!"
    "You can hardly believe it. Your own mother now has a fetish to get bred by you!"

    return #Needs testing

label breeding_fetish_lily_intro_label(the_person): #NEeds testing, evening room entry event
    $ the_person = lily
    "Note: This scene was written assuming that eventually you fuck [the_person.title] on a live stream, but so far Vren has not written this step."
    "You step into [the_person.possessive_title]'s room. She is standing next to her mirror playing with her hair, but looks over at you and smiles when she hears the door."
    $ the_person.draw_person()
    the_person "Oh hey [the_person.mc_title]! I was wondering if you were going to be around tonight. Want to stream with me tonight?"
    "Your sister's job, over the last few months, has slowly evolved. From taking sexy snaps, to streaming sex live with you live. Having sex with your sister, AND getting paid for it? Its amazing."
    "You think about it. Do you want to do another stream tonight?"
    menu:
        "Hell yeah!" if mc.energy > 60:
            pass
        "Hell yeah! (disabled) " if mc.energy <= 60:
            pass
        "Not tonight":
            pass
            #TODO add this event back into lily's list, and politely decline.
    the_person "Great! I'll get it setup..."
    "You notice she hesitates a bit. She bites her lower lip before continuing."
    the_person "So umm, I've been getting some requests recently..."
    mc.name "Oh? What are the thirsty anonymous internet guys wanting?"
    "She chuckles a second, but you sense a nervous tone."
    the_person "Well... they've been asking to see us take things one step farther... For you to finish inside me!"
    if the_person.knows_pregnant():
        "[the_person.title] is already pregnant, so it doesn't necessarily make the act risky."
        mc.name "You're already pregnant... but is that what they want? To act like you could get pregnant?"
    else:
        "You knew [the_person.title] wasn't on birth control."
        mc.name "That could be risky. What if you got pregnant? Or is that the point?"
    "Recently, you've been feeding her with serums that greatly heighten her urge to reproduce... you wonder if there's even been any requests, or if she is just using that as an excuse."
    mc.name "Maybe I should message them. Find out more about what they want to see..."
    "She quickly interrupts you."
    the_person "No! You don't need to do that... I'm sure that's what it is! To watch as I pretend to get knocked up!"
    "She gives a telltale sign. As she says that, she looks away from you and to the side. She is lying to you."
    mc.name "That's what they want? Are you sure? Or is that what YOU want?"
    "[the_person.possessive_title] begins to blush heavily."
    the_person "Oh me? Want to get knocked up? By my brother? That's... I mean thats CRAZY!... right?"
    "She is struggling to give a reasonable explanation. It is pretty clear now that she is just fishing for an excuse to fuck you raw, and to get filled with your potent seed."
    mc.name "Yeah, I mean, wouldn't that be crazy? For a woman to want to get fucked? To have a man dominate her and do what he wants with her, then fill her up with his seed, consequences be damned?"
    $ the_person.change_arousal(10)
    the_person "Well yeah I mean obviously that sounds hot but your my brother..."
    mc.name "Right, who happens to be a man? Someone you know and trust."
    "She sighs. She resigns herself and opens up."
    the_person "I can't explain it... The way things between us have progressed... But I just can't stop thinking about it!"
    the_person "My body wants it so bad, for you to pin me down and fuck me anywhere you want and cumming inside me over and over..."
    "She pauses for a second..."
    if the_person.knows_pregnant():
        the_person "I know this is crazy... I'm already pregnant!.. but I don't want to stop now! I want to you to breed me over and over, like your personal breeding slave!"
    else:
        the_person "I know this is crazy... I want you to knock me up! And not just once! I want you to breed me over and over, like your personal breeding slave!"
    "The serums must have really done their job! She seems to have acquired a breeding fetish!"
    mc.name "Ok... from now on, you are my personal cum dumpster. I'll use you like you want!"
    the_person "Oh god... this is amazing! Let's do it!"
    "Suddenly she remembers."
    the_person "Can we... can we do it on stream? No one on there believes we are actually siblings. They think its all just for show!"
    mc.name "Go ahead, set it up."
    $ the_person.draw_person(position = "sitting")
    "[the_person.possessive_title] walks over to her laptop. You give her a few minutes to get everything setup."
    the_person "Okay... I promised all the viewers a crazy show! Oh god I can't believe it..."
    "She stands up."
    $ the_person.draw_person()
    the_person "Just one more thing to do..."
    $ the_person.strip_outfit()
    "[the_person.title] gets naked, and you quickly follow suit."
    mc.name "How do you think we should do this?"
    the_person "I was thinking... you could just lay back and hold the camera. I'll ride you reverse cowgirl, then when you finish you'll be to uhhh, you know, see it."
    mc.name "Mmm... that sounds amazing... for the viewers too!"
    "She punches your arm half heartily and laughs."
    "You walk over to her bed and lay down on it. After a minute she brings you the camera."
    "She goes back over to a the computer, and after a moment, she gives a countdown."
    the_person "Okay, we are streaming in 5, 4, 3..."
    "As she goes past three stops counting and instead starts to walk over to you. She starts to talk into the camera."
    the_person "Hey everyone... just as promised, I have a naughty stream setup tonight!"
    the_person "Tonight is the night. I'm going to fuck my brother and let him cum in my pussy!"
    "You can hear a few replies go through on the computer, but from where you are you can't see them. [the_person.title] also hears them."
    the_person "I'm sorry, tonight I won't be able to take requests during. Just sit back and enjoy the show!"
    $ the_person.draw_person(position = "doggy")
    "With that, she turns her back to you and swings one leg over your body, her ass now pointed back at you."
    "She reaches down and gives your bare cock a few strokes, then points it up at her cunt."
    "Her pussy is moist and she easily starts to slide down on it, your bare cock enveloped by her steamy flesh."
    the_person "Oh fuck bro, you fill me up so good..."
    "She's playing it up for the stream, but you know she is also having fun, fucking her brother."
    $ the_person.change_arousal(20)
    $ mc.change_arousal(20)
    "You lay back on the bed while [the_person.possessive_title] works your cock in and out of her. You make sure to keep her ass in the frame of the camera."
    "[the_person.possessive_title] gives you a few quick, shallow dips then pull off you almost completely, leaving just your tip inside her."
    "She swirls her hips a couple times then impales herself on your again. [the_person.title] works her hips relentlessly on top of you as she pleases herself on your erection."
    $ the_person.change_arousal(30)
    $ mc.change_arousal(30)
    "She is putting on an incredible show for the camera! Her skill at working dick is extraordinary."
    the_person "Oh god bro, I'm so full! I want you to cum inside me!"
    "Her dirty words are matched by her actions as she works your cock aggressively. Her sexual expertise is incredibly pleasing for both of you."
    mc.name "Do it sis, your ass is amazing!"
    "You play along for the stream, and while no one online actually believes it, you legitimately fuck your sister."
    $ the_person.change_arousal(30)
    $ mc.change_arousal(30)
    "[the_person.possessive_title] wiggles back and forth a few more times, then looks back at you and smiles."
    the_person "Do you like that, bro? Ah! That is so good..."
    "[the_person.possessive_title] reaches back between her legs and cups your balls."
    the_person "Mmm you feel so full... I want you to fill me up! I can't wait to milk all that cum out of you!"
    $ the_person.change_arousal(30)
    $ mc.change_arousal(30)
    "Her dirty talking it having it's desired effect, and the taboo of doing this while anyone in the world can watch is just too much."
    "[the_person.possessive_title]'s sweet cunt milks your cock, the wet friction pushes you past the point of no return."
    mc.name "Ah, I'm going to cum!"
    the_person "Oh god me too! Oh fuck bro I'm cumming! Fill me up I need your cum too!"
    "She slams her hips down. As deep as your cock can go, you start to cum, filling [the_person.possessive_title]."
    "Her hole is quivering as she cums at the same time, milking your cock for every last drop of seed."
    $ the_person.cum_in_vagina()
    $ the_person.change_stats(happiness = 5,  slut_temp = 5, slut_core = 5)
    $ the_person.draw_person(position = "doggy")
    "Eventually the twitching stops, for both of you. You did it. You dumped your seed into your sister's unprotected, fertile snatch."
    "When she slowly pulls off you, your seed immediately begins to leak out of her and down her legs. You make sure to get the whole thing in frame."
    $ mc.reset_arousal()
    $ the_person.reset_arousal()
    the_person "Oh god... I wonder if I got pregnant..."
    "[the_person.possessive_title] slowly recovers and gets up. She turns around and sits on the side of the bed, facing you."
    $ the_person.draw_person(position = "sitting")
    the_person "Well... I hope everyone enjoyed watching my brother try and knock me up... I know I enjoyed it."
    the_person "Time for the stream to end! Goodbye everyone!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.title] walks over to the computer, ending the live stream. Your seed still running down the inside of her legs."
    $ the_person.draw_person()
    the_person "Well... I think that went well!"
    mc.name "Me too... want to have another round?"
    the_person "Oh god... my body says yes... but I think I need to rest."
    "She bites her lip as she looks down at you."
    the_person "I meant it earlier though... I want you to breed me. Anytime, anywhere!"
    mc.name "Don't worry, I'll give you more soon."
    "She chuckles, then smiles at you."
    the_person "You better... Every day! Even if I am pregnant..."
    $ add_breeding_fetish(the_person)
    "You quietly get up and get dressed. You sneak out of her room, being carefully so your mother doesn't hear you."
    "You can hardly believe it. Your own sister now has a fetish to get bred by you!"
    return

label breeding_fetish_rebecca_intro_label():
    "Rebecca doesn't have a breeding fetish written yet"
    return

label breeding_fetish_gabrielle_intro_label():
    "Gabrielle doesn't have a breeding fetish written yet"
    return

label breeding_fetish_stephanie_intro_label():  #Needs Testing
    $ the_person = stephanie
    $ the_person.event_triggers_dict["LastBreedingFetish"] = day
    if mc.location == mc.business.r_div: #Already in research
        "Suddenly, [the_person.possessive_title] looks up from her work and and speaks up."
        the_person "Hey [the_person.mc_title], I need to talk to you about something. Can we go somewhere private?"
    else:
        "You get a text message from [the_person.possessive_title]."
        the_person "Hey [the_person.mc_title], I need to talk to you about something. Can we meet somewhere private?"
        "You text her back."
    mc.name "Sure, meet me in my office."
    $ mc.change_location(office)
    $ ceo_office.show_background()
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person)
    "[the_person.title] meets you there. You sit down and notice she closes the office door... and then locks it."
    mc.name "Have a seat. Is there something I can do for you?"
    "She sits down and immediately starts to talk to you."
    $ scene_manager.update_actor(the_person, position = "sitting")
    if the_person.love < 40 and the_person.obedience < 140:
        the_person "Look... I've been doing this for a while now. I know the real purpose of the serums you have me researching, and the effects they have on people..."
        the_person "I went along with things for a while because... well I don't know why. I guess I was just really into the science of things."
        "She shifts uncomfortably in her seat."
        $ scene_manager.update_actor(the_person, display_transform = character_right)
        the_person "Some of the things we've developed here are incredible. They can give people happiness, and expand their skills."
        the_person "The serums you've been giving out... I thought maybe you were just trying to make all the girls' lives here better."
        the_person "But... lately, I've found myself slipping further and further into these fantasies. It's making it hard to concentrate on my work!"
        the_person "I think you and I both know that this is a direct result of one of the serums we've been investigating lately... to give girls specific cravings. Fetishes even!"
        "She takes a second, she looks like she is on the verge of getting emotional. Then she straightens up and looks you straight in the eye."
        the_person "For god's sake, all I can think about is you cumming inside me over and over! Until my belly swells and my tits leak milk!"
        the_person "I'm sorry, but I can't do it anymore. You and I both know there isn't any real way to counter these effects. So, if I'm going to be get bred like a slut... I might as well enjoy it, right?"
        mc.name "I suppose so."
        $ scene_manager.update_actor(the_person, position = "stand4")
        "[the_person.possessive_title] pulls a serum out of her pocket."
        the_person "I don't have an antidote for this. It's the bimbo serum. I mixed it with a couple other things... might as well enjoy my new life!"
        "This is some dangerous territory. If you let her go through with this, you are sure her sister will be pissed! Do you try to talk her down? Or let her do it?"
        menu:
            "Try to talk her down" if mc.charisma > 6:
                mc.name "Stop. You don't have to do that?"
                "She looks at the serum in her hand. Then back at you."
                the_person "Ummm, I don't know... I'm pretty sure I do."
                mc.name "Don't you want to know more... about the long term effects? Of the serums I mean?"
                the_person "You hardly need me to test something like that."
                mc.name "Who better to do it though? [the_person.title], you've been with me since the beginning. I'll help meet your needs. I know the cravings will be intense, but I promise I'll help!"
                "Her resolve is failing. She looks down at the serum again."
                mc.name "The science behind these chemicals is incredible. You KNOW you want to keep studying it together. With me!"
                the_person "[the_person.mc_title]... I want to. I really do. But I'm so scared right now."
                "You get up and walk around the desk."
                mc.name "It's okay. Sometimes science is a risky business. We can do this. Together. Let me have the serum."
                "She hesitates another moment. Then hands you the serum."
                the_person "Oh god... you better be right about this!"
                $ scene_manager.update_actor(the_person, position = "kissing")
                "She throws her arms around you, holding you close."
                the_person "The serums really are incredible. I do want to study them more. But first... I need you to breed me! I can't think about anything else right now!"
                $ scene_manager.update_actor(the_person, position = "standing_doggy")
                "[the_person.possessive_title] turns around and bends over. Your hands immediately get to work."
                $ scene_manager.strip_actor_outfit(the_person, exclude_lower = False)
                "She wiggles her ass back and forth in front of you as you pull your dick out of your pants."
                the_person "Come on [the_person.mc_title], you know what I need!"
                "Without any hesitation you slide your cock into her cunt."
                $ the_person.break_taboo("vaginal_sex")
                call fuck_person(the_person, start_position = bent_over_breeding, skip_intro = True, position_locked = True, asked_for_condom = True) from _call_steph_breeding_fetish_intro_01
                $ add_breeding_fetish(the_person)
                the_person "Oh god... It's even better than I dreamed about last night."
                "[the_person.possessive_title] takes a minute to recover before standing up. She's rubbing her belly."
                $ scene_manager.update_actor(the_person, position = "stand2")
                the_person "Okay... I'm in. I hope you realize the serums also greatly increase libido."
                mc.name "Don't worry. If the urges ever get too strong, just come find me, anywhere I am I'll bend you over, even here in the lab."
                the_person "Ah... that sounds... acceptable. Okay, let's give this a shot I guess."
                $ scene_manager.update_actor(the_person, position = "walking_away")
                "You say goodbye, and [the_person.possessive_title] turns and walks out of your office, your cum running down the inside of her legs."
                "Looks like [the_person.title] has a breeding fetish now!"
            "Let her take it":
                mc.name "I'm sorry, [the_person.title]. I didn't want it to be this way."
                "She looks at you. Her resolve stumbles, but only for a moment."
                the_person "Don't worry, I'll be a REAL ideal employee for you soon."
                "She brings the serum to her mouth and drinks it down. She closes her eyes as it begins to take effect."
                $ enhanced_permanent_bimbo_on_apply(the_person, add_to_log = True)
                "It probably only takes a minute, but it feels like an eternity. Finally she opens her eyes."
                "She looks around a bit, seeming a bit confused about where she is."
                the_person "That's... we were talking about something... right?"
                "She looks at you. Her pupils are dilated and her breathing is calm."
                mc.name "We were just about done... with the talking anyway."
                the_person "That's right! We were going to do something else after though... right? I remember hoping that."
                "You being to walk towards her."
                mc.name "That's right. You were going to bend over my desk for a minute. And if everything goes well, I have a present for you."
                the_person "Oh! A present! I do love presents! Especially the ones I tend to get when I'm bent over. I wonder what it could be!"
                $ scene_manager.update_actor(the_person, position = "standing_doggy")
                "[the_person.possessive_title] turns around and bends over. Your hands immediately get to work."
                $ scene_manager.strip_actor_outfit(the_person, exclude_lower = False)
                "She wiggles her ass back and forth in front of you as you pull your dick out."
                the_person "Stick it in [the_person.mc_title]! I want to earn my special present!"
                "Without any hesitation you slide your cock into her cunt."
                $ the_person.break_taboo("vaginal_sex")
                call fuck_person(the_person, start_position = bent_over_breeding, start_object = make_desk(), skip_intro = True, position_locked = True, asked_for_condom = True) from _call_steph_bimbo_breeding_fetish_01
                $ add_breeding_fetish(the_person)
                the_person "That's it! That's just what I was hoping for."
                $ scene_manager.update_actor(the_person, position = "stand2")
                the_person "Mmm, thanks for that mister! I know this is kinda crazy but... I'm totally getting the urge for another round. Normally one time is enough but..."
                mc.name "I'm sorry, you'll have to be patient if you want another round."
                the_person "Ah... I see."
                the_person "Fine! I'll just go back to... whatever it was I was doing. What do I do here again?"
                mc.name "It doesn't matter, you can take the rest of the day off."
                the_person "Oh? That eager to get rid of me? Guess I'll just go find someone else to play with for a while. Your loss mister!"
                $ scene_manager.update_actor(the_person, position = "walking_away")
                "You say goodbye, and [the_person.possessive_title] turns and walks out of your office. Your seed is dribbling down her leg."
                "Looks like [the_person.title] has a breeding fetish now! But she is also a bimbo."
                "You are guessing she is probably not particularly fit for her job in research. Maybe you can move her somewhere else in the company?"

            "Try to talk her down\n{color=#ff0000}{size=18}Requires High Charisma{/size}{/color} (disabled)" if mc.charisma <= 6:
                pass

    elif the_person.love < 70 and not the_person.has_role(girlfriend_role):   #She kinda trusts / loves you, but isn't fully committed and needs some convincing.
        the_person "Look... I've been doing this for a while now. I know the real purpose of the serums you have me researching, and the effects they have on people..."
        the_person "I went along with things for a while because I trust you. You've always impressed me with the way you do things."
        "She shifts uncomfortably in her seat."
        $ scene_manager.update_actor(the_person, display_transform = character_right)
        the_person "Some of the things we've developed here are incredible. They can give people happiness, and expand their skills."
        the_person "The serums you've been giving out... I thought maybe you were just trying to make all the girls' lives here better."
        the_person "But... lately, I've found myself slipping further and further into these fantasies. It's making it hard to concentrate on my work!"
        the_person "I think you and I both know that this is a direct result of one of the serums we've been investigating lately... to give girls specific cravings. Fetishes even!"
        "She takes a second, she looks like she is on the verge of getting emotional. Then she straightens up and looks you straight in the eye."
        the_person "For god's sake, all I can think about is you cumming inside me over and over! Until my belly swells and my tits leak milk!"
        the_person "I'm going to be honest here. I trust you, I'm sure you are just doing this for research or business purposes. But I'm at a tipping point here. I need you to answer this question honestly."
        mc.name "Okay, go ahead."
        the_person "Are you going to... you know... take responsibility for this? The urges are SO intense! You're the only guy here, I need your word that you'll help me take of these urges!"
        "From a pocket, she pulls out a serum that it looks like she has concocted."
        the_person "If you can't, I guess I understand. But I don't think I can take it, knowing the serums gave me these urges... I need something to forget, and just move on with my life."
        the_person "I don't have an antidote for this. It's the bimbo serum. I mixed it with a couple other things... Maybe it's time for me to start a new life. I'm sure you could use me over in marketing or something, right?"
        "This is some dangerous territory. It sounds like she is looking to you to tell her what to do."
        "Become a bimbo, for real? Or, if you want her to stay the sexy, intelligent research lead, you'll have to help her with her newfound fetish?"
        "If you have her take the serum, her sister will probably get very upset!"
        menu:
            "Help her":
                pass
            "Take the Serum":
                mc.name "I'm sorry, [the_person.title]. I didn't want it to be this way. I don't think I have the time to commit to something like that."
                $ scene_manager.update_actor(the_person, emotion = "sad")
                "She looks at you. You think you see a tear coming down from her eye."
                the_person "It's okay. The science is amazing. And I'm sure I'll enjoy life as a mother."
                "She brings the serum to her mouth and drinks it down. She closes her eyes as it begins to take effect."
                $ enhanced_permanent_bimbo_on_apply(the_person, add_to_log = True)
                "It probably only takes a minute, but it feels like an eternity. Finally she opens her eyes."
                "She looks around a bit, seeming a bit confused about where she is."
                the_person "That's... we were talking about something... right?"
                "She looks at you. Her pupils are dilated and her breathing is calm."
                mc.name "We were just about done... with the talking anyway."
                the_person "That's right! We were going to do something else after though... right? I remember hoping that."
                "You being to walk towards her."
                mc.name "That's right. You were going to bend over my desk for a minute. And if everything goes well, I have a present for you."
                the_person "Oh! A present! I do love presents! Especially the ones I tend to get when I'm bent over. I wonder what it could be!"
                $ scene_manager.update_actor(the_person, position = "standing_doggy")
                "[the_person.possessive_title] turns around and bends over. Your hands immediately get to work."
                $ scene_manager.strip_actor_outfit(the_person, exclude_lower = False)
                "She wiggles her ass back and forth in front of you as you pull your dick out."
                the_person "Stick it in [the_person.mc_title]! I want to earn my special present!"
                "Without any hesitation you slide your cock into her cunt."
                $ the_person.break_taboo("vaginal_sex")
                call fuck_person(the_person, start_position = bent_over_breeding, start_object = make_desk(), skip_intro = True, position_locked = True, asked_for_condom = True) from _call_steph_bimbo_breeding_fetish_03
                $ add_breeding_fetish(the_person)
                the_person "That's it! That's just what I was hoping for."
                $ scene_manager.update_actor(the_person, position = "stand2")
                the_person "Mmm, thanks for that mister! I know this is kinda crazy but... I'm totally getting the urge for another round. Normally one time is enough but..."
                mc.name "I'm sorry, you'll have to be patient if you want another round."
                the_person "Ah... I see."
                the_person "Fine! I'll just go back to... whatever it was I was doing. What do I do here again?"
                mc.name "It doesn't matter, you can take the rest of the day off."
                the_person "Oh? That eager to get rid of me? Guess I'll just go find someone else to play with for a while. Your loss mister!"
                $ scene_manager.update_actor(the_person, position = "walking_away")
                "You say goodbye, and [the_person.possessive_title] turns and walks out of your office. Your seed is dribbling down her leg."
                "Looks like [the_person.title] has a breeding fetish now! But she is also a bimbo."
                "You are guessing she is probably not particularly fit for her job in research. Maybe you can move her somewhere else in the company?"
                $ clear_scene()
                return
        "She gives a deep sigh of relief."
        the_person "You have NO idea how glad I am to hear that."
        "[the_person.possessive_title] stands up."
        $ scene_manager.update_actor(the_person, position = "stand4")
        if the_person.outfit.tits_available() and the_person.outfit.vagina_available():
            pass
        else:
            "She starts to strip down."
            $ scene_manager.strip_actor_outfit(the_person, exclude_lower = False)
        "She looks at you expectantly."
        the_person "Well? Why are you still wearing clothes? You said you would help!"
        # call fuck_person(the_person, start_position = SB_anal_cowgirl, start_object = make_desk(), girl_in_charge = True, position_locked = True) from _call_sex_description_SBA093
        call get_fucked(the_person, the_goal = "vaginal creampie", start_position = cowgirl, start_object = make_desk(), allow_continue = False, asked_for_condom = True) from _call_steph_breeding_fetish_cowgirl_01
        $ add_breeding_fetish(the_person)
        the_person "Oh god... It's even better than I dreamed about last night."
        "[the_person.possessive_title] takes a minute to recover before standing up. She rubs her belly."
        $ scene_manager.update_actor(the_person, position = "stand2")
        the_person "Okay. I hope you realize the serums also greatly increase libido."
        mc.name "Don't worry. If the urges ever get too strong, just come find me, anywhere I am I'll bend you over, even here in the lab."
        the_person "Ah... that sounds... acceptable. Okay, let's give this a shot I guess."
        $ scene_manager.update_actor(the_person, position = "walking_away")
        "You say goodbye, and [the_person.possessive_title] turns and walks out of your office, your cum running down the inside of her legs."
        "Looks like [the_person.title] has a breeding fetish now!"
    else:
        the_person "Before I get started, I just want to make sure you understand. I support you completely. I'm not mad or anything, just a little concerned."
        the_person "I've been doing this for a while now. I know the real purpose of the serums you have me researching, and the effects they have on people..."
        the_person "I went along with things for a while because I trust you. Maybe even love you. You've always impressed me with the way you do things."
        the_person "Some of the things we've developed here are incredible. They can give people happiness, and expand their skills."
        the_person "The serums you've been giving out... I thought maybe you were just trying to make all the girls' lives here better."
        the_person "But... lately, I've found myself slipping further and further into these fantasies. It's making it hard to concentrate on my work!"
        the_person "I think you and I both know that this is a direct result of one of the serums we've been investigating lately... to give girls specific cravings. Fetishes even!"
        "She takes a second, she looks like she is on the verge of getting emotional. Then she straightens up and looks you straight in the eye."
        the_person "For god's sake, all I can think about is you cumming inside me over and over! Knocking me up and collaring me and called me your breeding stock!"
        the_person "I trust you. It took me a while to realize what is going on, but I understand it now."
        the_person "This is the next step in our relationship. The urges are SO intense! You're the only guy here, I need you to help me take of these urges!"
        the_person "I'm sure that relying on you for this can only bring us closer together."
        if the_person.relationship != "Single":
            $ SO_title = SO_relationship_to_title(the_person.relationship)
            mc.name "Wait, don't you have a [SO_title]?"
            the_person "So? He isn't here at work with me all day is he? He can fuck me when I get home, but I need you to do it while I'm here!"
        "Sounds like she thinks the whole reason you gave her the serums is because... you want to take things to the next level? For now, it is probably better if you just go along with it."
        mc.name "You're right. I probably should have been more honest about it, but I thought this would help bring us closer together."
        "She gives a deep sigh of relief."
        the_person "You have NO idea how glad I am to hear that."
        "[the_person.possessive_title] stands up."
        $ scene_manager.update_actor(the_person, position = "stand4")
        if the_person.outfit.tits_available() and the_person.outfit.vagina_available():
            pass
        else:
            "She starts to strip down."
            $ scene_manager.strip_actor_outfit(the_person, exclude_lower = False)
        "She looks at you expectantly."
        the_person "Well? Why are you still wearing clothes? You said you would help!"
        # call fuck_person(the_person, start_position = SB_anal_cowgirl, start_object = make_desk(), skip_intro = False, girl_in_charge = True, position_locked = True) from _call_sex_description_SBA094
        call get_fucked(the_person, the_goal = "vaginal creampie", start_position = cowgirl, start_object = make_desk(), skip_intro = False, allow_continue = False, asked_for_condom = True) from _call_breeding_fetish_steph_intro_02
        $ add_breeding_fetish(the_person)
        the_person "Oh god... It's even better than I dreamed about last night."
        "[the_person.possessive_title] takes a minute to recover before standing up. She rubs her belly."
        $ scene_manager.update_actor(the_person, position = "stand2")
        the_person "Okay. I hope you realize the serums also greatly increase libido."
        mc.name "Don't worry. If the urges ever get too strong, just come find me, anywhere I am I'll bend you over, even here in the lab."
        the_person "Ah... that sounds... acceptable. Okay, let's give this a shot I guess."
        $ scene_manager.update_actor(the_person, position = "walking_away")
        "You say goodbye, and [the_person.possessive_title] turns and walks out of your office, your cum running down the inside of her legs."
        "Looks like [the_person.title] has a breeding fetish now!"
    $ scene_manager.clear_scene()
    $ the_person.apply_planned_outfit()
    $ clear_scene()
    return #Needs testing

label breeding_fetish_emily_intro_label():
    "Emily doesn't have a breeding fetish written yet"
    return

label breeding_fetish_christina_intro_label():
    "Christina doesn't have a breeding fetish written yet"
    return

label breeding_fetish_alex_intro_label():
    "Alexia doesn't have a breeding fetish written yet"
    return

label breeding_fetish_nora_intro_label():
    "Nora doesn't have a breeding fetish written yet"
    return

label breeding_fetish_starbuck_intro_label():  #Needs TEsting
    $ the_person = starbuck
    "You get a text message from [the_person.possessive_title]."
    the_person "Hey, do you think you could help me close up the shop tonight? I have a few things I need help with."
    "You consider it. You don't have much else going on right now, so you decide to agree."
    mc.name "Sure, I'll be over shortly."
    "You make your way over to the sex shop."
    #TODO change background
    $ the_person.draw_person()
    "When you get to the store, you look around. It seems like the store is already pretty clean."
    mc.name "Good evening [the_person.title]. Still need help? Things look pretty good around here to me..."
    the_person "Hey [the_person.mc_title]! Thanks for coming. I'm almost done, but thought maybe you could we could just hang out for a bit."
    "Hmm, so she has ulterior motives for asking you here."
    mc.name "Certainly."
    "[the_person.possessive_title] locks the front door. She gets you a beer from her fridge and she grabs one for herself."
    "You make small talk for a bit. Finally, [the_person.title] starts to talk to you about why she asked you over."
    the_person "So... you are probably wondering why you are here. Today, something happened to me while I was working."
    the_person "This young couple came in, looking for some new lingerie. They needed new because the woman had umm... grown out of her clothing."
    the_person "She was... shall we say VERY pregnant. I think she was ready to pop any day!"
    if the_person.knows_pregnant():
        the_person "I know I'm already pregnant but... it was so hot! It made me realize how amazing it is to get bred."
    else:
        the_person "There was something about them though. They were practically glowing! And the way they looked at each other. I... I can't believe this, but it made me so jealous!"
        the_person "I've never had it quite this bad before... but it gave me this ITCH. I can't explain it, but I've been day dreaming all day about.. you know... being like that."
    if the_person.is_girlfriend():
        the_person "I know our relationship is kind of... unique... with how much older I am. But I don't think I've ever been so sure of something."
    else:
        the_person "I know its kind of weird, with how much older I am. But I don't think I've ever been more sure of something."
    the_person "Would you be my bull? Cum inside me... over and over... breed me like its your job!"
    the_person "I want to feel your seed inside me, every second of every day!"
    "Your cock is already hard, listening to [the_person.possessive_title] talk like this. You've been slipping her serums, and it looks like they've finally given her a breeding fetish."
    "It's time to seal the deal. If you give her what she wants now, she'll be begging you for creampies every chance she gets."
    mc.name "Okay. I'll give you my cum. Now turn around, I want to take you over the counter."
    $ the_person.change_arousal(8)
    the_person "Oh god, yes!"
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
    the_person "Stick it in [the_person.mc_title]! Fuck me hard and cum as deep as you can!"
    "You grab her hips to stop the wiggling. You line yourself up with her thirsty cunt and push into her. She gasps when you bottom out."
    the_person "Oh yes! Give it to me good!"
    call fuck_person(the_person, start_position = bent_over_breeding , private = True, skip_intro = True, position_locked = True, asked_for_condom = True) from _starbuck_gets_breeding_fetish_01
    if the_person.has_creampie_cum():
        the_person "Oh god! Baby making sex is so hot, I can't believe it..."
        "[the_person.title] reaches her hand back, trying to keep your cum inside of her, but failing, as your cum drips down the inside of her thighs."
    else:
        #TODO what to put here?
        pass
    $ add_breeding_fetish(the_person)
    if the_person.knows_pregnant():
        the_person "I don't care if I am already pregnant... Please do that again! My body was made to take your cum like that!"
    else:
        the_person "I hope that did it, but you'd better cum inside me again and again anyway!"
    $ the_person.draw_person()
    "[the_person.possessive_title] slowly stands up and turns to you."
    the_person "Wow... I'm glad I finished closing up before you got here..."
    $ the_person.draw_person(position = "kissing")
    "She draws you into a hug, then whispers in your ear."
    the_person "You can bend me over like that anytime... I don't even care if there are customers here when you do it..."
    $ the_person.draw_person()
    the_person "You go ahead, I have a couple more things to do before I go."
    "You say goodbye to [the_person.title]."
    "You can hardly believe it. The sex store owner [the_person.title] now has a fetish to get bred by you!"
    return #Needs testing

label breeding_fetish_sarah_intro_label():   #Needs Testing
    $ the_person = sarah
    $ mc.change_location(bedroom)
    $ mc.location.show_background()
    $ scene_manager = Scene()
    "As you are getting ready for bed, you get a text on your phone. It's from [the_person.possessive_title]"
    the_person "Hey, can I come over tonight? I had something I wanted to talk to you about."
    "You quickly text her back."
    mc.name "Sure. Want to spend the night?"
    the_person "Hell yeah! I'll bring some stuff over."
    "About 20 minutes later she texts you."
    the_person "Hey, I'm here! Come let me in!"
    "You head to your front door and open it."
    "For once, you managed to get her back to your room while avoiding [mom.possessive_title] and [lily.title]."
    $ scene_manager.add_actor(the_person, position = "sitting")
    "She walks over and sits on your bed."
    mc.name "So... what did you want to talk about?"
    "She clears her throat. You can tell she is a little nervous."
    if the_person.knows_pregnant():
        the_person "I know I'm already pregnant... and it is amazing really."
        the_person "But even after you got me pregnant, every time you finish inside me, I find myself craving it, more and more."
        the_person "The itch is getting so bad! I just want you to fill me up, over and over!"
        the_person "Even after the baby comes... I want my your seed planted deep in me as much as possible!"
        "This is quite a twist! You know you had started giving her pregnancy serums, and it sounds like they are starting to really have an effect."
        mc.name "I'll do it. From now on, you are my personal mare! I'll breed over and over, just like you want."
    else:
        the_person "Well, this is kind of hard to talk about. But... we've been having a lot of unprotected sex lately..."
        mc.name "Oh my god, are you pregnant?"
        the_person "No! No, not yet... that I know of anyway..."
        mc.name "Not... yet?"
        the_person "Well, [the_person.mc_title], it's been like a dream, having you back in my life like this. Things are amazing, being with you."
        the_person "I've been, well, tracking my cycles recently and, well, basically, I'm fertile right now."
        "You can feel your cock twitch in your pants. You imagine [the_person.possessive_title], knocked up, her tits swelling with milk and her belly growing..."
        the_person "Every time you finish inside me, I find myself thinking about it, more and more, what it would be like to get pregnant and have a baby with you."
        the_person "Look, you don't have to answer me right now, but, I thought maybe we could try and have a baby. Together?"
        the_person "I know this is crazy... but lately I've just had this almost overwhelming itch! I want you to knock me up and fill me over and over!"
        "This is quite a twist! You weren't expecting this so soon, but it seems the pregnancy serums you've been giving her are really working."
        mc.name "Honestly, I didn't realize this was something you were thinking about. But I would love to make a baby with you!"
    $ the_person.change_stats(happiness = 15, obedience = 10)
    the_person "Oh! Wow, I honestly... I thought you we're gonna say no! This is... I can't believe it."
    "She looks up at you, and you can see the changes in her facial expression. She goes from surprised, to happy, to sultry."
    the_person "So umm, what are you doing right now?"
    mc.name "I think we should get naked."
    the_person "Yes sir!"
    $ scene_manager.strip_actor_outfit(the_person, exclude_lower = False)
    "You get naked with [the_person.possessive_title]. She rolls on her back and spreads her legs."
    the_person "Come fill me up, [the_person.mc_title]!"
    call fuck_person(the_person, start_position = breeding_missionary, start_object = bedroom.get_object_with_name("bed"), skip_intro = False, girl_in_charge = False, position_locked = True, asked_for_condom = True) from _sarah_ask_for_baby_05
    if the_person.has_creampie_cum():
        the_person "Oh my god... we actually did it..."
        "She grabs an extra pillow and puts it under her butt so her hips are elevated."
        the_person "I'm just going to lay her like this for a bit, you know. Keep that seed nice and deep."
    else:
        mc.name "I'm sorry, I really want to, I'm just really tired."
        "You can tell she is a little disappointed."
        the_person "That's okay. Maybe in the morning?"
    "You snuggle up with [the_person.possessive_title]. Your serums have turned her into your personal breeding mare."
    $ add_breeding_fetish(the_person)
    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_sarah_breeding_request_5
    call Sarah_spend_the_night() from sarah_ask_for_baby_overnight_15

    return #Needs testing

label breeding_fetish_ophelia_intro_label():
    "Ophelia doesn't have a breeding fetish written yet"
    return

label breeding_fetish_erica_intro_label():
    "Erica doesn't have a breeding fetish written yet"
    return

label breeding_fetish_candace_intro_label(the_person): #This is going to be two intros, depending on if candace is still a bimbo or not NEeds Testing
    $ the_person = candace
    "As you step into the office, you see [the_person.possessive_title] looking over at you. She stands up and waves you over to her desk."
    $ the_person.draw_person()
    "You walk over to her."
    if candace_is_bimbo(): #She is a bimbo.
        mc.name "Hello [the_person.title]. Something I can help you with?"
        the_person "Yeah boss! I'm having trouble concentrating on my work this morning. Could you help me?"
        mc.name "Possibly, what seems to be distracting you?"
        the_person "Last night, I was like, totally watching porn, but I couldn't get off to the usual stuff. I was starting to get frustrated, until I finially found something that worked!"
        the_person "I found this video where like, the first half of it is this hottie getting railed and the guy cums in her, and then the second half she's like 8 months pregnant!"
        the_person "You could totally tell it was her too because like, she had the same tattoo and everything!"
        the_person "I went back and watched the first half again and came so hard, thinking about how that was how she got knocked up!"
        mc.name "That... sounds like a great a video, but I'm not sure what I can help you with."
        if the_person.knows_pregnant():
            the_person "I know that like, I'm already knocked up, OBVIOUSLY. But like, maybe we could make a video like that too?"
            the_person "You could just like, keep fucking babies into me non stop and every time you cum inside me, its like, this could be the time!"
            mc.name "You want me to keep getting you pregnant?"
            the_person "Like, over and over! That sound so hot!"
        else:
            the_person "I was thinking like, maybe we could do that! Take a video of you cumming inside me and knocking me up!"
            mc.name "You want me to get you pregnant?"
            the_person "Fuck yeah! That's like, so hot! And can you imagine having that on video? Holy fuck!"
        "Lately, you've been slipping her serums to increase her drive to reproduce. Unsurprisingly, it sounds like she has developed a breeding fetish."
        mc.name "Okay. I'll give you my cum. Now turn around, I'm going to take you over your desk."
        $ camera_person = get_random_from_list(known_people_at_location(mc.location, excluded_people = [the_person]))
        if not camera_person:
            "You look around the room, but no one else is around to record it, so you set up your phone to record and prop it up on a nearby desk as best you can."
        else:
            "You look around the room. You notice that another employee has overheard the conversation and is looking at you with some interest."
            mc.name "[camera_person.title], come here."
            $ camera_person.draw_person()
            camera_person "Yes?"
            mc.name "Take this, I need you to take a video for me."
            camera_person "Oh wow... you're really going to...? Right here?"
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
        the_person "Just, like, put it in me already!"
        mc.name "I want to hear you beg."
        the_person "PUT IT IN AND FUCK ME AND BREED ME AND CUM OVER AND OVER DEEP MAKE ME YOUR CUM DUMPSTER PLEASE PLEASE PLEASE!!!"
        "Wow, that didn't take much encouragement. You grab her hips, line yourself up and push yourself in deep."
        the_person "Yes!!!"
        call fuck_person(the_person, start_position = bent_over_breeding , private = False, skip_intro = True, position_locked = True, asked_for_condom = True) from _bimbo_candace_gets_breeding_fetish_01
        if the_person.has_creampie_cum():
            "[the_person.title] reaches her hand back, rubbing the cum that has started to drip out of her all around her slit, playing with it."
        else:
            #TODO what to put here?
            pass
        if camera_person == None:
            "You grab your phone off the desk and stop the video. You quickly put it in an email to [the_person.title] so she can have a copy of it."
        else:
            camera_person "Wow..."
            "You grab your phone from [camera_person.title] and thank her for her help. You quickly put the video in an email to [the_person.title] so she can have a copy of it."

        $ del camera_person

        if the_person.knows_pregnant():
            the_person "I don't care if I am already pregnant... Please do that again! My body was made to take your cum like that!"
        else:
            the_person "I hope that did it, but you'd better cum inside me again and again anyway!"
        $ the_person.draw_person()
        "[the_person.possessive_title] slowly stands up and turns to you."
        the_person "Did you, like... get the video?"
        mc.name "A copy should be in your email shortly."
        if the_person.knows_pregnant():
            the_person "We'll have to like, make more! You know, when you are ACTUALLY knocking me up, not just practicing!"
        else:
            the_person "Don't forget, I want another like, when my belly is all big and my titties are spraying milk everywhere!"
        mc.name "I'll make sure it happens. Do you think you can concentrate on your work now?"
        the_person "Yes sir! I'll get back to work!"
        $ add_breeding_fetish(the_person)
        "You step away from her desk, letting her get back to her work. You notice her humming a happy tune as you walk away."
        "You can hardly believe it. [the_person.possessive_title] now has a fetish to get bred by you!"
        return
    else:
        the_person "[the_person.mc_title], I've been thinking about something, and I needed to make you aware of it."
        mc.name "Okay, what would that be?"
        the_person "Well, as you know, you and I both have very good... shall we say, genetics?"
        the_person "We are both very talented, go getters, with good genes."
        the_person "We owe it to the world to make offspring. As many, and as often as we can."
        if the_person.knows_pregnant():
            mc.name "We've been doing pretty good at that so far."
            "[the_person.title] rubs her pregnant belly."
            the_person "I agree."
        the_person "It's important that you cum inside me on a regular basis... As often as possible, really."
        "Lately, you've been slipping her serums to increase her drive to reproduce. Unsurprisingly, it sounds like she has developed a breeding fetish."
        mc.name "Are you saying you want to be my personal breeding mare?"
        the_person "The comparison to livestock is crude... but fitting. Yes, [the_person.mc_title], I want you to breed me over and over as much and as often as possible!"
        $ the_person.draw_person(position = "standing_doggy")
        "[the_person.title] stands up and bends over her desk."
        the_person "You should start right now. It's okay, I'll count it as my 5 minute break."
        if the_person.outfit.vagina_available():
            "With her pussy already out and ready to be used, you waste no time getting your pants off. When you cock springs free, you use it smack her ass a couple times."
        else:
            "As you start to pull your cock out, [the_person.possessive_title] reaches back and starts to pull off the clothing covering her ass."
            $ the_person.strip_outfit(exclude_upper = True)
            "You give her ass a couple smacks with your cock."
        $ the_person.change_arousal(10)
        $ mc.change_arousal(10)
        mc.name "Are you ready to get bred, bitch?"
        "[the_person.title] keeps trying to back herself up onto you, but you move your dick around, frustrating her."
        the_person "[the_person.mc_title], its not appropriate to tease a lady like this."
        mc.name "I want to hear you beg."
        the_person "PUT IT IN AND FUCK ME AND BREED ME AND CUM OVER AND OVER DEEP MAKE ME YOUR CUM DUMPSTER PLEASE PLEASE PLEASE!!!"
        "Wow, that didn't take much encouragement. You grab her hips, line yourself up and push yourself in deep."
        the_person "Yes!!!"

        call fuck_person(the_person, start_position = bent_over_breeding , private = False, skip_intro = True, position_locked = True, asked_for_condom = True) from _bimbo_candace_gets_breeding_fetish_02
        if the_person.has_creampie_cum():
            "[the_person.title] reaches her hand back, rubbing the cum that has started to drip out of her all around her slit, playing with it."
            if the_person.knows_pregnant():
                the_person "Mmm... I think I felt the baby kick when you came inside me!"
            else:
                the_person "The odds aren't great from just one creampie. Make sure you cum inside me again soon!"
        else:
            the_person "You're.... you're done already?"
            mc.name "Sorry... I'll have to cum inside you another time."

        $ the_person.draw_person(position = "stand2")
        "[the_person.possessive_title] slowly stands up and turns to you."
        the_person "Thank you [the_person.mc_title]. Please cum inside me anytime you need a little relief from now on."
        $ add_breeding_fetish(the_person)
        "You step away from her desk, letting her get back to her work. You notice her humming a happy tune as you walk away."
        "You can hardly believe it. [the_person.possessive_title] now has a fetish to get bred by you!"
    return #Needs testing #Needs testing

label breeding_fetish_ashley_intro_label():
    "Ashley doesn't have a breeding fetish written yet"
    return

label breeding_fetish_dawn_intro_label():
    "Dawn doesn't have a breeding fetish written yet"
    return

label unit_test_breeding_fetish_intro():

    "Generic intros"
    $ debug_set_stats_for_breeding_fetish_mins(mom)
    "Method: breeding_fetish_family_intro_label"
    call breeding_fetish_family_intro_label(mom) from _unit_test_breeding_fetish_intro_01
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_breeding_fetish_mins(starbuck)
    "Method: breeding_fetish_generic_intro_label"
    call breeding_fetish_generic_intro_label(starbuck) from _unit_test_breeding_fetish_intro_02
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_breeding_fetish_mins(stephanie)
    "Method: breeding_fetish_employee_intro_label"
    call  breeding_fetish_employee_intro_label(stephanie) from _unit_test_breeding_fetish_intro_03
    $ mc.energy = mc.max_energy

    $ stephanie.remove_role(breeding_fetish_role)
    $ mom.remove_role(breeding_fetish_role)
    $ starbuck.remove_role(breeding_fetish_role)

    "Unique intros"
    $ debug_set_stats_for_breeding_fetish_mins(mom)
    "Method: breeding_fetish_mom_intro_label"
    call breeding_fetish_mom_intro_label() from _unit_test_breeding_fetish_intro_04
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_breeding_fetish_mins(lily)
    "Method: breeding_fetish_lily_intro_label"
    call breeding_fetish_lily_intro_label(lily) from _unit_test_breeding_fetish_intro_05
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_breeding_fetish_mins(aunt)
    "Method: breeding_fetish_rebecca_intro_label"
    call breeding_fetish_rebecca_intro_label() from _unit_test_breeding_fetish_intro_06
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_breeding_fetish_mins(cousin)
    "Method: breeding_fetish_gabrielle_intro_label"
    call breeding_fetish_gabrielle_intro_label() from _unit_test_breeding_fetish_intro_07
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_breeding_fetish_mins(stephanie)
    "Method: breeding_fetish_stephanie_intro_label"
    call breeding_fetish_stephanie_intro_label() from _unit_test_breeding_fetish_intro_08
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_breeding_fetish_mins(alexia)
    "Method: breeding_fetish_alex_intro_label"
    call breeding_fetish_alex_intro_label() from _unit_test_breeding_fetish_intro_09
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_breeding_fetish_mins(nora)
    "Method: breeding_fetish_nora_intro_label"
    call breeding_fetish_nora_intro_label() from _unit_test_breeding_fetish_intro_10
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_breeding_fetish_mins(emily)
    "Method: breeding_fetish_emily_intro_label"
    call breeding_fetish_emily_intro_label() from _unit_test_breeding_fetish_intro_11
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_breeding_fetish_mins(christina)
    "Method: breeding_fetish_christina_intro_label"
    call breeding_fetish_christina_intro_label() from _unit_test_breeding_fetish_intro_12
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_breeding_fetish_mins(starbuck)
    "Method: breeding_fetish_starbuck_intro_label"
    call breeding_fetish_starbuck_intro_label() from _unit_test_breeding_fetish_intro_13
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_breeding_fetish_mins(sarah)
    "Method: breeding_fetish_sarah_intro_label"
    call breeding_fetish_sarah_intro_label() from _unit_test_breeding_fetish_intro_14
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_breeding_fetish_mins(salon_manager)
    "Method: breeding_fetish_ophelia_intro_label"
    call breeding_fetish_ophelia_intro_label() from _unit_test_breeding_fetish_intro_15
    $ mc.energy = mc.max_energy

    $ create_debug_candace()
    $ debug_set_stats_for_breeding_fetish_mins(candace)
    "Method: breeding_fetish_candace_intro_label"
    call breeding_fetish_candace_intro_label(candace) from _unit_test_breeding_fetish_intro_16
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_breeding_fetish_mins(dawn)
    "Method: breeding_fetish_dawn_intro_label"
    call breeding_fetish_dawn_intro_label() from _unit_test_breeding_fetish_intro_17
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_breeding_fetish_mins(erica)
    "Method: breeding_fetish_erica_intro_label"
    call breeding_fetish_erica_intro_label() from _unit_test_breeding_fetish_intro_18
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_breeding_fetish_mins(ashley)
    "Method: breeding_fetish_ashley_intro_label"
    call breeding_fetish_ashley_intro_label() from _unit_test_breeding_fetish_intro_19
    $ mc.energy = mc.max_energy

    return
