#Testing Comments


init 1301 python:

    def Sarah_titles(the_person):
        return the_person.name
    def Sarah_possessive_titles(the_person):
        valid_possessive_titles = [Sarah_titles(the_person)]
        valid_possessive_titles.append("Your childhood friend")
        if the_person.event_triggers_dict.get("try_for_baby", 0) >= 1:
            valid_possessive_titles.append("Your breeding mare")
        return valid_possessive_titles
    def Sarah_player_titles(the_person):
        return mc.name
    Sarah_personality = Personality("Sarah", default_prefix = "relaxed",
    common_likes = ["skirts", "small talk", "Fridays", "the weekend", "the colour purple", "makeup", "flirting", "heavy metal","punk"],
    common_sexy_likes = ["doggy style sex", "giving blowjobs", "getting head", "anal sex", "public sex", "skimpy outfits", "showing her ass", "threesomes", "not wearing underwear", "creampies", "bareback sex"],
    common_dislikes = ["the colour pink", "supply work", "conservative outfits", "work uniforms"],
    common_sexy_dislikes = ["being submissive", "being fingered", "missionary style sex"],
    titles_function = Sarah_titles, possessive_titles_function = Sarah_possessive_titles, player_titles_function = Sarah_player_titles)





############################
##### Sarah Personality#####
############################
# <editor-fold
label Sarah_introduction(the_person):  #This shouldn't proc... ever?
    mc.name "Excuse me, could I bother you for a moment?"
    "She turns around and looks you up and down."

    $ the_person.set_title("???")
    the_person.char "Uh, sure? What do you want?"
    mc.name "I know this sounds crazy, but I saw you and just wanted to say hi and get your name."
    "She laughs and crosses her arms."
    $ title_choice = get_random_title(the_person)
    $ formatted_title = the_person.create_formatted_title(title_choice)
    the_person.char "Yeah? Well I like the confidence, I'll say that. My name's [formatted_title]."
    $ the_person.set_title(title_choice)
    $ the_person.set_possessive_title(get_random_possessive_title(the_person))
    the_person.char "And what about you, random stranger? What's your name?"
    return

label Sarah_greetings(the_person):
    if the_person.love < 0:
        the_person.char "Ugh, what do you want?"
    elif the_person.happiness < 90:
        the_person.char "Hey. Did you need something? I'm sorry I'm having a bit of a rough day."
    else:
        if the_person.sluttiness > 60:
            if Sarah_is_fertile():
                the_person.char "Hello. Need something? I hope so, I know I really need something soon..."
                "She lowers her voice and whispers in your ear."
                the_person.char "I'm fertile right now."
            elif the_person.event_triggers_dict.get("dating_path", False) == True:
                the_person.char "Hello babe! I hope you aren't here just to talk."
            elif the_person.obedience > 130:
                the_person.char "Hello there [the_person.mc_title]. It's good to see you, is there anything I can help you with?"
            else:
                the_person.char "Hey there [the_person.mc_title]. I was just thinking about some fun things we could do together..."
        else:
            if the_person.obedience > 130:
                the_person.char "Hello [the_person.mc_title]"
            else:
                the_person.char "Hey, how's it going?"
    return

label Sarah_sex_responses(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "Oh fuck, I love that rush when you first get started."
        else:
            the_person.char "Oh... [the_person.mc_title] that feels really good..."

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            the_person.char "Mmm, keep going [the_person.mc_title]. You are getting me so hot."
        else:
            the_person.char "That... That feels great [the_person.mc_title]!"

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            if the_person.event_triggers_dict.get("dating_path", False) == True:
                the_person.char "Oh god, I'm your dirty little slut [the_person.mc_title]! It feels so good!"
            else:
                the_person.char "The things you do to me, it feel so good [the_person.mc_title]!"
        else:
            the_person.char "Does it feel as good for you as it does for me? Mmm, it feels so good!"
    else:
        if the_person.sluttiness > 50:
            if the_person.event_triggers_dict.get("dating_path", False) == True:
                the_person.char "You fuck me so good, I can't imagine being with anyone else. Make me cum baby!"
            elif the_person.relationship == "Single":
                the_person.char "Fuck! I'm... You're going to make me cum! I want you to make me cum!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Oh god, why am I even with my [so_title]? He doesn't drive me crazy like you do [the_person.mc_title]!"
                the_person.char "Make me cum my brains out! Screw my [so_title], he's not half the man you are!"
        else:
            if the_person.event_triggers_dict.get("dating_path", False) == True and the_person.love > 80:
                the_person.char "Oh my god, [the_person.mc_title], I love you so much, you're gonna make me explode! Don't stop!"
            the_person.char "Don't stop! You're going to make me cum, don't you dare stop!"

    return

label Sarah_climax_responses_foreplay(the_person):
    if the_person.sluttiness > 50:
        if the_person.event_triggers_dict.get("dating_path", False) == True:
            the_person.char "Oh god, even like this, you still make me cum! I'm cumming [the_person.mc_title]!"
        else:
            the_person.char "Oh fuck yes, I'm going to cum! I'm cumming!"
    else:
        the_person.char "Oh fuck, you're going to make me cum! Fuck!"
        "She goes silent, then lets out a shuddering moan."
    return

label Sarah_climax_responses_oral(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Fuck yes, I'm going to cum! Make me cum!"
    else:
        the_person.char "Oh my god, you're good at that! I'm going to... I'm going to cum!"
    return

label Sarah_climax_responses_vaginal(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Ah! More! I'm going to... Ah! Cum! Fuck!"
        "She closes her eyes and squeals with pleasure."
    else:
        the_person.char "Oh god, I'm going to... Oh fuck me! Ah!"
    return

label Sarah_climax_responses_anal(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Oh fuck, your cock feels so huge in my ass! It's going to make me cum!"
        the_person.char "Ah! Mmhmmm!"
    else:
        the_person.char "Oh fucking shit, I think you're going to make me..."
        "She barely finishes her sentence before her body is wracked with pleasure."
        the_person.char "Cum!"
    return

label Sarah_clothing_accept(the_person):
    if the_person.obedience > 130:
        the_person.char "You picked this out for me? That's all I need to hear. Thanks!"
    else:
        the_person.char "Hey, thanks. That's a good look, I like it."
    return

label Sarah_clothing_reject(the_person):
    if the_person.obedience > 130:
        the_person.char "I don't... I'm sorry, but I really don't think I could get away with wearing something like this. I appreciate the thought though."
    else:
        if the_person.sluttiness > 60:
            the_person.char "Jesus, you didn't leave much to the imagination, did you? I don't think I can wear this."
        else:
            the_person.char "There's not much of an outfit to this outfit. Thanks for the thought, but there's no way I could wear this."
    return

label Sarah_clothing_review(the_person):
    if the_person.obedience > 130:
        the_person.char "Oh man, I'm a mess. I'll be back in a moment, I'm just going to get cleaned up for you."
    else:
        if the_person.sluttiness > 40:
            the_person.char "I don't think everyone else would appreciate me going around dressed like this as much as you would. I'll be back in a second, I just want to get cleaned up."
        else:
            the_person.char "Damn, everything's out of place after that. Wait here a moment, I'm just going to find a mirror and try and look presentable."
    return

label Sarah_strip_reject(the_person):
    if the_person.obedience > 130:
        the_person.char "Could we leave that where it is for now, please?"
    elif the_person.obedience < 70:
        the_person.char "No, no, no, I'll decide what comes off and when, okay?"
    else:
        the_person.char "Not yet... get me a little warmed up first, okay?"
    return

label Sarah_sex_accept(the_person):
    if the_person.sluttiness > 70:
        if Sarah_is_fertile():
            the_person.char "My body is yours to use, [the_person.mc_title]. Just try to cum inside me... it's a good time of the month for that!"
        elif the_person.event_triggers_dict.get("dating_path", False) == True:
            the_person.char "Yes! Let's go! I'm glad I'm not the only one feeling needy."
        elif the_person.obedience < 70:
            the_person.char "Let's do it. Once you've had your fill I have a few ideas we could try out."
        else:
            the_person.char "I was hoping you would suggest that, just thinking about it gets me excited."
    else:
        the_person.char "You want to give it a try? Okay, let's try it."
    return

label Sarah_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        if the_person.event_triggers_dict.get("dating_path", False) == True:
            the_person.char "I can't say no to you, can I? I want you feel good, use me however you want, [the_person.mc_title]!"
        else:
            the_person.char "God, what have you done to me? I should say no, but... I just want you to use me however you want, [the_person.mc_title]."
    else:
        if the_person.obedience > 130:
            the_person.char "If that's what you want to do then I'll what you tell me to do."
        else:
            the_person.char "I shouldn't... but if you want to try it out I'm game. Try everything once, right?"
    return

label Sarah_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        the_person.char "Not yet [the_person.mc_title], get me warmed up first."
    else:
        the_person.char "Wait, I just... I don't think I'm ready for this. I want to fool around, but let's keep it casual."
    return

label Sarah_sex_angry_reject(the_person):
    if not the_person.relationship == "Single":
        $ so_title = SO_relationship_to_title(the_person.relationship)
        the_person.char "What? I have a [so_title], so you can forget about doing anything like that. Ever."
        "She glares at you, then walks away."
    elif the_person.sluttiness < 20:
        the_person.char "I'm sorry, what!? No, you've massively misread the situation, get the fuck away from me!"
        "[the_person.title] glares at you and steps back."
    else:
        the_person.char "What? That's fucking disgusting, I can't believe you'd even suggest that to me!"
        "[the_person.title] glares at you and steps back."
    return

label Sarah_seduction_response(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            the_person.char "Oh, I think I know what you need right now. Let me take care of you."
        else:
            the_person.char "Right now? Okay, lead the way I guess."
    else:
        if the_person.sluttiness > 50:
            the_person.char "Mmm, you're feeling as horny as me then? Come on, let's go."
            "[the_person.title] takes your hand and leads you off to find some place out of the way."
        elif the_person.sluttiness > 10:
            the_person.char "I know that look you're giving me, I think I know what you want."
        else:
            the_person.char "[mc.name], I know what you mean... Okay, I can spare a few minutes."
    return

label Sarah_seduction_accept_crowded(the_person):
    if the_person.relationship == "Single":
        if the_person.sluttiness < 20:
            the_person.char "Alright, let's slip away for a few minutes and you can convince me a little more."
        elif the_person.sluttiness < 50:
            the_person.char "Come on, I know someplace nearby where we can get a few minutes privacy."
        else:
            the_person.char "Oh my god. I hope you aren't planning on making me wait [the_person.mc_title], because I don't know if I can!"
    else:
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (5*the_person.get_opinion_score("cheating on men")) > 50:
            the_person.char "Fuck, let's get this party started!"
            the_person.char "I hope you don't mind that I've got a [so_title], because I sure as hell don't right now!"
        else:
            the_person.char "God damn it, you're bad for me [the_person.mc_title]... Come on, we need to go somewhere quiet so my [so_title] doesn't find out about this."
    return

label Sarah_seduction_accept_alone(the_person):
    if the_person.relationship == "Single":
        if the_person.sluttiness < 20:
            the_person.char "Well, I think you deserve a chance to impress me."
        elif the_person.sluttiness < 50:
            the_person.char "Mmm, well let's get this party started and see where it goes."
        else:
            the_person.char "Fuck, I'm glad you're as horny as I am right now. Come on, I can't wait any more!"
    else:
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (5*the_person.get_opinion_score("cheating on men")) > 50:
            the_person.char "Fuck, you know how to turn me on in ways my [so_title] never can. Come here!"
        else:
            the_person.char "You're such bad news [the_person.mc_title]... I have a [so_title], but all I can ever think of is you!"
    return

label Sarah_seduction_refuse(the_person):
    if the_person.sluttiness < 20:
        the_person.char "Sorry [the_person.mc_title], I'm not really in the mood to flirt or fool around."
        "[the_person.title] shrugs unapologetically."

    elif the_person.sluttiness < 50:
        the_person.char "I'll admit it, you're tempting me, but I'm not in the mood to fool around right now. Maybe some other time though, I think we could have a lot of fun together."

    else:
        the_person.char "Shit, that sounds like a lot of fun [the_person.mc_title], but I'm not feeling it right now. Hang onto that thought and we can fool around some other time."
    return

label Sarah_flirt_response(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            the_person.char "You know that all you have to do is ask and it's all yours."
        else:
            the_person.char "Thank you [the_person.mc_title], I'm glad you're enjoying the view."

    elif not the_person.relationship == "Single":
        $so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (the_person.get_opinion_score("cheating on men")*5) > 50:
            the_person.char "Then why don't you do something about it? Come on, we don't have to tell my [so_title] anything at all, right?"
            "[the_person.title] winks and spins around, giving you a full look at her body."
        else:
            the_person.char "You're playing with fire [the_person.mc_title]. I've got a [so_title], and I don't think he'd appreciate you flirting with me."
            mc.name "What about you, do you appreciate it?"
            "She gives a coy smiles and shrugs."
            the_person.char "Maybe I do."

    else:
        if the_person.sluttiness > 50:
            the_person.char "Then why don't you do something about it? Come on, all you have to do is ask."
            "[the_person.title] smiles at you and spins around, giving you a full look at her body."
        else:
            the_person.char "Well thank you, play your cards right and maybe you'll get to see a little bit more."
            the_person.char "You'll have to really impress me though, I have high standards."
    return

label Sarah_flirt_response_low(the_person):
    if sarah.event_triggers_dict.get("epic_tits_progress", 0)>= 2:  #She has gone through bigger tits story
        the_person.char "Oh? You like how I look, now that I'm the total package?"
        $ the_person.draw_person(position = "walking_away")
        "[the_person.possessive_title] gives you a quick spin, showing off her body at the same time as her outfit."
        $ the_person.draw_person()
    else:
        the_person.char "Oh? Thank you [the_person.mc_title]! I'm glad to hear you like the way I look."
        the_person.char "I'm not sure why you feel that way though, I'm not wearing anything special."
    mc.name "Your body is fantastic, and the outfit is the icing on the cake."
    "She smiles and laughs."
    the_person.char "Ah, so you are resorting to flattery then? You kind words are noted, [the_person.mc_title]!"
    return

label Sarah_flirt_response_mid(the_person):
    if  the_person.relationship != "Single": # She is taken
        the_person.char "Thank you [the_person.mc_title], but you know you shouldn't be saying that."
        mc.name "Why not? You're hot and I'm just trying to give you a compliment."
        the_person.char "Thank you, but I have a boyfriend. You know this."
        "She sighs and looks away from you for a moment."
        the_person.char "I... guess it's still nice to hear though. It's been a while since my boyfriend said I was hot."
        mc.name "Well I'm happy to tell you that you are very, very hot [the_person.title]."
        "[the_person.possessive_title] smiles and shrugs."
        the_person.char "Thanks. It means a lot to hear that from my childhood friend."
    elif the_person.effective_sluttiness("underwear_nudity") < 20:
        the_person.char "I know we are childhood friends, and obviously I want you to be honest with me, but I'm not sure it's right for you to say stuff like that."
        mc.name "Like what? That you're hot?"
        the_person.char "I guess I'm just not used to hearing the guy I used to play hide and seek with when I was little call me \"hot\"."
        mc.name "Well I suppose you'd better get used to, since its true and I'm not going to stop reminding you anytime soon."
        "[the_person.title] rolls her eyes at you, but you also notice the corner of her mouth turn up in a slight smile."
        the_person.char "Thank Romeo, though I will admit it is nice to hear."

    else:
        the_person.char "Buttering me up again, are you?"
        the_person.char "You know, with that way you talk about me, a girl could get the wrong idea about what your intentions might be..."
        "[the_person.possessive_title] smiles and runs her hands down her hips. She hesitates for a moment, then turns around and pats her ass."
        $ the_person.draw_person(position = "back_peek")
        the_person.char "What exactly are your intentions, [the_person.mc_title]? You seem to have a hard time taking your eyes off of me..."
        "You zone out for a second, checking out [the_person.title]'s shapely hind end."
        $ the_person.draw_person()
        "She turns back and giggles."
        if sarah.event_triggers_dict.get("epic_tits_progress", 0)>= 2:
            the_person.char "Tongue tied?. That's okay, I've been having that effect on a lot of guys lately."
        mc.name "What can I say? Your body is hypnotizing."
    return

label Sarah_flirt_response_high(the_person):
    if mc.location.get_person_count() == 1: #If you are alone she'll flirt with you
        if the_person.effective_sluttiness() > 25: # High sluttiness flirt
            if the_person.has_taboo("underwear_nudity"):
                the_person.char "Oh [the_person.mc_title], you're so bad! Do you really want to... see me naked?"
            else:
                the_person.char "Oh [the_person.mc_title]. You're always trying to get me naked."

            mc.name "You're so beautiful, I always want to see more."
            "She sighs and smiles."
            the_person.char "Don't worry, I want to get naked for you."

            menu:
                "Kiss her.":
                    "You put an arm around [the_person.possessive_title]'s waist and pull her close."

                    if the_person.has_taboo("kissing"):
                        $ the_person.call_dialogue("kissing_taboo_break")
                        $ the_person.break_taboo("kissing")
                        "You lean in and kiss her. She hesitates for a moment before gently pressing herself against your body."
                    else:
                        "Before you can take the initiative, she pushes herself on her toes and kisses you. You open your mouth and she devours your tongue eagerly."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_sarah_flirt_01

                "Just flirt.":
                    mc.name "Believe me, I want to get naked for you too. Hopefully soon I'll have the time."
                    "[the_person.possessive_title] gives you a little pout."
                    the_person.char "We make time for what's important. But I understand, running a business is a lot of work."
                    the_person.char "Hopefully you have time soon!"

        else:
            the_person.char "Oh [the_person.mc_title]... I don't know if I could go that far."
            mc.name "Relax, we're just joking around. Unless you want to get naked for me?"
            "She laughs and shakes her head in disbelief. You see a glint of mischief in her eye when she asks you."
            the_person.char "Why don't you get naked first and we'll see what happens?"
            mc.name "You'll pull your phone out and start taking blackmail pictures. Theres no way I'm doing that."
            the_person.char "Me? Blackmail you? [the_person.mc_title] why I would never!"
            if the_person.has_taboo("touching_penis"):
                mc.name "Do you what would actually be really helpful? I've gotten all worked up, why don't you just touch me with your hand for a bit."
                the_person.char "You want me... to give you a handjob?"
                mc.name "You would be doing me a big favor..."
                $ the_person.call_dialogue("touching_penis_taboo_break")
                $ the_person.break_taboo("touching_penis")
            else:
                the_person.char "Ok fine, I've got a better idea. What if I put my hand in your pants and umm, you know, like we did the other day..."
                mc.name "Mmm, I suppose I would be up for that."
            "[the_person.possessive_title] places a hand on your chest and strokes it tenderly."
            "She looks into your eyes as her hand moves lower, running over your abs, down to your waist."
            "Her fingers slide into your pubic hair, then to the side of your cock and between your legs."
            "She runs a finger along the bottom of your shaft, ending at the sensitive spot under your tip."
            "Then she wraps her full hand around it and slides it back down to the base."
            "[the_person.possessive_title] begins to stroke you off with long, deliberate motions."
            call fuck_person(the_person, private = True, start_position = handjob, skip_intro = True) from _call_fuck_sarah_flirt_02

    else: #She shushes you and rushes you off somewhere private.
        if the_person.effective_sluttiness() > 25: #She's slutty, but you need to find somewhere private so people don't find out.
            the_person.char "[the_person.mc_title]..."
            "[the_person.possessive_title] glances around nervously."
            the_person.char "Take me somewhere private and say something like that again and it might actually happen..."
            menu:
                "Find someplace quiet.":
                    mc.name "Then let's find somewhere private. Come on."
                    "You take her hand and start to lead her away. She follows you eagerly."
                    the_person.char "Wow, I wasn't expecting you to actually do it! This is gonna be fun!"
                    "When you find a quiet spot you pull [the_person.possessive_title] close to you."
                    if the_person.has_taboo("kissing"):
                        $ the_person.call_dialogue("kissing_taboo_break")
                        $ the_person.break_taboo("kissing")
                        "You lean in and kiss her. She hesitates for a moment before gently pressing herself against your body."
                    else:
                        the_person.char "Oh god... come here [the_person.mc_title]..."
                        "She pushes herself up on her toes to meet your lips as you bring your head down to kiss her."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_sarah_flirt_03

                "Just flirt.":
                    mc.name "I know, I just like to tease you."
                    the_person.char "Oh, is that so? Well two can play at that game."
                    if sarah.event_triggers_dict.get("epic_tits_progress", 0)>= 2:
                        $ the_person.draw_person(the_animation = blowjob_bob)
                        "She checks that nobody else is looking, then grabs her tits and jiggles them for you."
                        the_person.char "Teasing a lady like me. You should be ashamed of yourself, [the_person.mc_title]"
                        $ the_person.draw_person()
                    else:
                        "She checks that nobody else is looking, the reaches down and grabs your package. You harden rapidly as she gives it a couple of strokes."
                        the_person.char "Teasing a lady like me. You should be ashamed of yourself, [the_person.mc_title]"
                    mc.name "Jesus woman, you win!"
                    the_person.char "I'm glad you understand."

        else: #She's not slutty, so she's embarrassed about what you're doing.
            "[the_person.possessive_title] gasps softly and glances around, checking to see if anyone else was listening."
            the_person.char "[the_person.mc_title], stop joking around! If other people overhear they might get the wrong idea!"
            mc.name "It's fine, nobody heard anything. Besides, who cares if other people know I want to see you naked?"
            "[the_person.possessive_title] gives you a very convincing frown, but she eventually breaks and cracks a smile."
            the_person.char "I guess, I just wish you would be a little more discrete."
            "She places a gentle hand on your shoulder and kisses you on the cheek."
    return

label Sarah_cum_face(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 60:
            the_person.char "What do you think? Is this a good look [the_person.mc_title]?"
            "[the_person.title] licks her lips, cleaning up a few drops of your semen that had run down her face."
        else:
            the_person.char "I hope you had a good time [the_person.mc_title]. It certainly seems like you did."
            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
    else:
        if the_person.sluttiness > 80:
            the_person.char "Mmm that's such a good feeling. Do you think I look cute like this?."
            "[the_person.title] runs her tongue along her lips, then smiles and laughs."
        else:
            the_person.char "Whew, glad you got that over with. Take a good look while it lasts."
    return

label Sarah_cum_mouth(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 60:
            the_person.char "Mmm, thank you [the_person.mc_title]."
        else:
            "[the_person.title]'s face grimaces as she tastes your cum in her mouth."
            the_person.char "Ugh. There, all taken care of [the_person.mc_title]."
    else:
        if the_person.sluttiness > 80:
            the_person.char "Mmm, you taste great [the_person.mc_title]. Was it nice to watch me take your load in my mouth?"
        else:
            the_person.char "Ugh, that's such a... unique taste."
    return

label Sarah_cum_vagina(the_person):
    #TODO
    return

label Sarah_cum_anal(the_person):
    #TODO
    return

label Sarah_suprised_exclaim(the_person):
    $rando = renpy.random.choice(["Fuck!","Shit!","Oh fuck!","Fuck me!","Ah! Oh fuck!", "Ah!", "Fucking tits!", "Holy shit!", "Fucking shit!", "God fucking dammit!", "Son of a bitch!", "Mother fucker!", "Whoah!"])
    the_person.char "[rando]"
    return

label Sarah_talk_busy(the_person):
    if the_person.obedience > 120:
        the_person.char "I've got a ton of things I need to get to, could we talk some other time [the_person.mc_title]?"
    else:
        the_person.char "Hey, I'd love to chat but I have a million things to get done right now. Maybe later?"
    return

label Sarah_sex_strip(the_person):
    if the_person.sluttiness < 20:
        if the_person.arousal < 50:
            the_person.char "One sec, I want to take something off."
        else:
            the_person.char "Ah, I'm wearing way too much right now. One sec!"

    elif the_person.sluttiness < 60:
        if the_person.arousal < 50:
            the_person.char "Why do I bother wearing all this?"
        else:
            the_person.char "Wait, I want to get a little more naked for you."

    else:
        if the_person.arousal < 50:
            the_person.char "Give me a second, I'm going to strip something off just. For. You."
        else:
            the_person.char "Ugh let me get this off. I want to feel your pressed against every inch!"
    return

label Sarah_sex_watch(the_person, the_sex_person, the_position):
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry")
        the_person.char "Ugh, jesus you two. Get a room or something, nobody wants to see this."
        $ the_person.change_obedience(-2)
        $ the_person.change_happiness(-1)
        "[the_person.title] looks away while you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement - 10:
        $ the_person.draw_person()
        the_person.char "Could you two at least keep it down? This is fucking ridiculous."
        $ the_person.change_happiness(-1)
        "[the_person.title] tries to avert her gaze and ignore you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement:
        $ the_person.draw_person()
        the_person.char "You're certainly feeling bold today [the_sex_person.name]. At least it looks like you're having a good time..."
        $ change_report = the_person.change_slut_temp(1)
        "[the_person.title] watches for a moment, then turns away while you and [the_sex_person.name] keep [the_position.verb]."

    elif the_person.sluttiness > the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person()
        the_person.char "Oh wow that's hot. You don't mind if I watch, do you?"
        $ change_report = the_person.change_slut_temp(2)
        "[the_person.title] watches you and [the_sex_person.name] [the_position.verb]."

    else:
        $ the_person.draw_person(emotion = "happy")
        the_person.char "Come on [the_person.mc_title], [the_sex_person.name] is going to fall asleep at this rate! You're going to have to give her a little more than that."
        "[the_person.title] watches eagerly while you and [the_sex_person.name] [the_position.verb]."
    return

label Sarah_being_watched(the_person, the_watcher, the_position):
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        the_person.char "Come on [the_person.mc_title], be rough with me. I can handle it!"
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        the_person.char "I bet she just wishes she was the one being [the_position.verb]ed by you."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        the_person.char "Oh god, you need to get a little of this yourself, [the_watcher.title]!"
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        the_person.char "[the_watcher.title], I'm giving him all I can right now. Any more and he's going to break me!"
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        the_person.char "Fuck, maybe we should go somewhere a little quieter..."
        $ the_person.change_arousal(-1)
        $ the_person.change_slut_temp(-1)
        "[the_person.title] seems uncomfortable with [the_watcher.title] nearby."

    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        the_person.char "Ah, now this is a party! Maybe when he's done you can tap in and take a turn [the_watcher.title]!"
        $ the_person.change_arousal(1)
        $ the_person.change_slut_temp(1)
        "[the_person.title] seems more comfortable [the_position.verb]ing you with [the_watcher.title] around."

    return

label Sarah_work_enter_greeting(the_person):
    if the_person.happiness < 80:
        "[the_person.title] glances at you when you enter the room. She scoffs and turns back to her work."

    elif the_person.happiness > 130:
        if the_person.sluttiness > 40:
            the_person.char "Hey [the_person.mc_title], down here for business or pleasure?"
            "The smile she gives you tells you which one she's hoping for."
        else:
            "[the_person.title] looks up from her work and smiles at you when you enter the room."
            the_person.char "Hey [the_person.mc_title], it's nice to have you stop by. Let me know if you need anything!"

    else:
        if the_person.sluttiness > 60:
            "[the_person.title] walks over to you when you come into the room."
            the_person.char "Just the person I was hoping would stop by. I'm here if you need anything."
            "She winks and slides a hand down your chest, stomach, and finally your crotch."
            the_person.char "Anything at all."
        else:
            the_person.char "Hey [the_person.mc_title]. Need anything?"
    return

label Sarah_date_seduction(the_person):
    if the_person.relationship == "Single":
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person.char "I've had a blast [the_person.mc_title], but there are a few more things I'd like to do with you. Want to come back to my place and find out what they are?"
            else:
                the_person.char "You've been a blast [the_person.mc_title]. Want to come back to my place, have a few drinks, and see where things lead?"
        else:
            if the_person.love > 40:
                the_person.char "Tonight's been amazing [the_person.mc_title], I just don't want to say goodbye. Do you want to come back to my place and have a few drinks?"
            else:
                the_person.char "This might be crazy, but I had a great time tonight and you make me a little crazy. Do you want to come back to my place and see where things go?"
    else:
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person.char "I've had a blast [the_person.mc_title], but I'm not done with you yet. Want to come back to my place?"
                the_person.char "My [so_title] won't be home until morning, so we would have plenty of time."
            else:
                the_person.char "This might be crazy, but do you want to come back to have another drink with me?"
                the_person.char "My [so_title] is stuck at work and I don't want to be left all alone."
        else:
            if the_person.love > 40:
                the_person.char "You're making me feel crazy [the_person.mc_title]. Do you want to come have a drink at my place?"
                the_person.char "My [so_title] won't be home until morning, and we have a big bed you could help me warm up."
            else:
                the_person.char "This is crazy, but would you want to have one last drink at my place? My [so_title] won't be home until morning..."
    return

label Sarah_sex_end_early(the_person):
    if the_person.sluttiness > 50:
        if the_person.love > 40:
            if the_person.arousal > 60:
                the_person.char "You're really done? Fuck [the_person.mc_title], I'm still so horny..."
            else:
                the_person.char "That's all you wanted? I was prepared to do so much more to you..."
        else:
            if the_person.arousal > 60:
                the_person.char "Fuck, I'm so horny... you're sure you're finished?"
            else:
                the_person.char "That was a little bit of fun, I suppose."

    else:
        if the_person.love > 40:
            if the_person.arousal > 60:
                the_person.char "[the_person.mc_title], you got me so turned on..."
            else:
                the_person.char "I hope you had a good time."
        else:
            if the_person.arousal > 60:
                the_person.char "Oh god, that was intense..."
            else:
                the_person.char "Done? Good, nice and quick."
    return


label Sarah_sex_take_control (the_person):
    if the_person.arousal > 60:
        the_person.char "Ha! That's funny. Get back here, I'm almost done!"
    else:
        the_person.char "You wish! I'm not done with you yet."
    return

label Sarah_sex_beg_finish(the_person):
    "Wait [the_person.mc_title], I'm going to cum soon and I just really need this... I'll do anything for you, just let me cum!"
    return

## Role Specific Section ##
label Sarah_improved_serum_unlock(the_person):
    mc.name "[the_person.title], now that you've had some time in the lab there's something I wanted to talk to you about."
    the_person.char "Okay, how can I help?"
    mc.name "All of our research and development up until this point has been based on the limited notes I have from my university days. I'm sure there's more we could learn, and I want you to look into it for me."
    "[the_person.title] smiles mischievously."
    the_person.char "Well, I've got an idea in mind. It's risky, but I think it could really push our research to a new level."
    mc.name "Go on, I'm interested."
    the_person.char "Our testing procedures focus on human safety, which I'll admit is important, but it doesn't leave us with much information about the subjective effects of our creations."
    the_person.char "What I want to do is take a dose of our serum myself, then have you record me while you run me through some questions."
    return

label Sarah_get_drunk_dialogue(the_person, intoxication_level):
    if intoxication_level < 3: # mostly sober
        if the_person.sluttiness > 60:
            "[the_person.title] is carrying on, talking about a time that she was trying to hookup with a random guy on Tinder but it didn't go well."
            the_person.char "...So anyway, that's when I decided to start making sure to keep my pubic hair trimmed."
            mc.name "Yeah I bet. To be honest though, I probably would have eaten you out anyway."
            the_person.char "Yeah right, and risk getting hair in your mouth? Hey, that reminds me of a joke I heard. What do you call a roman with a hair stuck in his teeth?"
            mc.name "I don't know, what?"
            the_person.char "A gladiator!"
            "You share a laugh together and continue having your drinks."
        else:
            "[the_person.title] is carrying on, talking about her time at her internship, before you hired her."
            the_person.char "...So anyway, I still can't believe I didn't realize what was going on. That man can go fuck himself!"
            mc.name "Well, I for one am glad that they let you go, or it is likely we never would have reconnected."
            the_person.char "I mean... that's true! I guess everything happens for a reason?"

    elif intoxication_level < 5: # drunk
        if the_person.sluttiness > 60:
            "[the_person.title] is carrying on. She's had a few drinks and is starting to get pretty obvious, flirting with you."
            the_person.char "...So anyway, that's why I'm banned from the weekly wine tasting. They keep saying to spit it out, but I always swallow."
            mc.name "Always?"
            the_person.char "Don't believe me?"
            "[the_person.possessive_title] takes a deep sip of her drink, then makes a show, tiling her head back and swallowing it all with a loud gulp."
            the_person.char "The defense declares this evidence to be called exhibit A... maybe later I can show you exhibit D."
        else:
            "[the_person.title] is carrying on, talking about her time at her internship, before you hired her."
            the_person.char "...So anyway, I still can't believe I didn't realize what was going on. That man can go fuck himself!"
            mc.name "Well, I for one am glad that they let you go, or it is likely we never would have reconnected."
            the_person.char "I mean... that's true! I guess everything happens for a reason?"

    else:   #Absolutely wasted
        if the_person.sluttiness > 60:
            "[the_person.title] is wasted. She's trying to flirt with you, but can hardly get through her pick up lines."
            mc.name "You doing okay over there?"
            the_person.char "Me? Ummm... OF COURSE. Heyyyy, are you a candle?"
            mc.name "Not exactly..."
            the_person.char "BECAUSE I WOULD TOTALLY SUCK YOU OFF."
            mc.name "You mean... blow me?"
            the_person.char "Thatsh what I said!"
            "You make a mental note that it's probably better to get her a water next instead of another drink."
        else:
            "[the_person.title] is carrying on, talking about her time at her internship, before you hired her."
            the_person.char "I mean, there were a couple cute dudesh there... and girlsh too if I'm honest..."
            the_person.char "But what ish going on now... I mean wow there issh sum incredible ass in your company!"
            mc.name "Yeah, I really enjoy the company and the employees."
            the_person.char "No kidding! Ugh my head hurtsss."
            "You make a mental note that it's probably better to get her a water next instead of another drink."

    return
