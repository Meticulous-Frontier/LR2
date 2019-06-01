## Cougar personality Mod by Tristimdorion
# All girls in town older than 40 get this personality trait
# See generic_personality_hook.rpy for more information

init 1400 python:
    def cougar_titles(person):
        valid_titles = [reserved_titles(person)]
        if person.love > 25:
            valid_titles.append("Cougar")
        if person.sluttiness > 70:
            valid_titles.append("Old Bitch")
        if person.sluttiness > 100 and the_person.get_opinion_score("anal sex") > 0 and person.sex_skills["Anal"] > 4:
            valid_titles.append("Anal Harlot")
        return valid_titles
    def cougar_possessive_titles(person):
        valid_possessive_titles = [relaxed_titles(person)]
        if person.sluttiness > 60:
            valid_possessive_titles.append("Your slutty cougar")
        if person.sluttiness > 100 and (the_person.get_opinion_score("drinking cum") > 0 or the_person.get_opinion_score("being covered in cum") > 0):
            valid_possessive_titles.append("Your cum-dump cougar")
        if person.sluttiness > 100 and the_person.get_opinion_score("anal sex") > 0 and person.sex_skills["Anal"] > 4:
            valid_possessive_titles.append("Your anal minx")
        return valid_possessive_titles
    def cougar_player_titles(person):
        valid_player_titles = [reserved_player_titles(person)]
        if person.happiness < 70:
            valid_player_titles.append("Litle Boy")
        if person.love > 25:
            valid_player_titles.append("Darling")
        if person.sluttiness > 60:
            valid_player_titles.append("Young Stud")
        return valid_player_titles

    cougar_personality = Personality("cougar", default_prefix = "cougar", #Cougar style personality
        common_likes = ["skirts", "small talk", "Mondays", "the weekend", "the colour red", "makeup", "sports", "flirting", "HR work"],
        common_sexy_likes = ["doggy style sex", "giving blowjobs", "getting head", "anal sex", "public sex", "skimpy outfits", "anal sex", "showing her tits", "showing her ass", "taking control", "not wearing underwear", "creampies", "drinking cum", "cum facials"],
        common_dislikes = ["Mondays", "the colour pink", "supply work", "conservative outfits", "work uniforms", "pants"],
        common_sexy_dislikes = ["being submissive", "being fingered", "missionary style sex", "risking getting pregnant"],
        titles_function = cougar_titles, possessive_titles_function = cougar_possessive_titles, player_titles_function = cougar_player_titles)

    # added to personalities prior to initalization of new games
    list_of_personalities.append(cougar_personality)

init 5 python:
    add_label_hijack("normal_start", "correct_personality_age_action")

# make the woman in the game the right age for their personality
# this used on the startup of the game (called ONCE)
label correct_personality_age_action(stack):
    python:
        for person in all_people_in_the_game(excluded_people = [mc, lily, mom, aunt, cousin, stephanie] + list_of_unique_characters):
            # make cougars personalities the right age
            if person.personality == cougar_personality:
                if person.age < 40: # split age for cougars
                    person.age = renpy.random.randint(40, 55)
                    # mc.log_event("Cougar " + person.name + " is " + str(person.age), "float_text_grey")
            # make sure other personalities are not older than 40
            if person.personality != cougar_personality:
                if person.age > 40: # split age for cougars
                    person.age = renpy.random.randint(18, 40)
                    # mc.log_event("Changed " + person.name + " is " + str(person.age), "float_text_grey")

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label cougar_greetings(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 60:
            the_person.char "Hello my boy. Is there anything I can take care of for you?"
        else:
            the_person.char "Hello young man. I hope everything is going well, if there's anything I can help with let me know."
    else:
        if the_person.sluttiness > 60:
            the_person.char "Hello [the_person.mc_title], how has your day been? I was... thinking about you, that's all."
        else:
            $ day_part = time_of_day_string()
            the_person.char "Good [day_part], [the_person.mc_title]!"
    return

label cougar_clothing_accept(the_person):
    if the_person.obedience > 140:
        the_person.char "Well, if you think I have got the body for it then I'm not going to argue."
        the_person.char "Thank you for the outfit, [the_person.mc_title]."
    else:
        the_person.char "Oh that's a nice combination! I'll show it to my friends later and see what they think."
    return

label cougar_clothing_reject(the_person):
    if the_person.obedience > 140:
        the_person.char "I know it would make your day if I wore this for you [the_person.mc_title], but what if my friends saw me in this?"
        the_person.char "I'm sorry, I know you are disappointed, but I will make it up to you."
    else:
        if the_person.sluttiness > 60:
            the_person.char "I... [the_person.mc_title], you don't think a woman of my... experience could get away with wearing this, do you?"
            "[the_person.possessive_title] laughs and shakes her head."
            the_person.char "No, these clothes are for young girls!"
        else:
            the_person.char "[the_person.mc_title]! I'm a lady, I can't show my face in public with something like that!"
            "[the_person.possessive_title] shakes her head and gives you a scowl."
    return

label cougar_clothing_review(the_person):
    if the_person.obedience > 130:
        the_person.char "Turn around [the_person.mc_title], I'm really not looking ladylike right now. Just give me a moment to get dressed..."
    else:
        if the_person.sluttiness > 50:
            the_person.char "Oh [the_person.mc_title], I shouldn't be seen like this... Just give me a moment and I'll get dressed."
        else:
            the_person.char "Oh [the_person.mc_title], I'm not decent! Turn around now, I need to cover myself!"
    return

label cougar_strip_reject(the_person):
    if the_person.obedience > 130:
        the_person.char "I know it would make your day [the_person.mc_title], but I don't think I should take anything else off. I'm a lady, after all."
    elif the_person.obedience < 70:
        the_person.char "Not yet sweety. You just need to relax and let [the_person.title] take care of you."
    else:
        the_person.char "Don't touch that [the_person.mc_title]. Could you imagine if it came off? I could be your mother, we shouldn't do this."
    return

label cougar_sex_accept(the_person):
    if the_person.sluttiness > 70:
        if the_person.obedience < 100:
            the_person.char "Such a nice body you have [the_person.mc_title] and I really want to do this... do you mind?"
        else:
            the_person.char "Whatever you want me to do [the_person.mc_title]. I just want to make sure you're happy."
    else:
        the_person.char "Okay, lets try it this, I hope you don't mind having sex with an older woman?"
    return

label cougar_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        the_person.char "I know I shouldn't do this, I know I should say no..."
        the_person.char "But you look so strong and beautiful, please..."
    else:
        if the_person.obedience > 130:
            the_person.char "I... We really shouldn't... But I know this makes you happy. Lets do it [the_person.mc_title]..."
        else:
            the_person.char "How does this keep happening [the_person.mc_title]? You know I love you but we shouldn't be doing this..."
            "[the_person.possessive_title] looks away, conflicted."
            the_person.char "I... You just have to make sure your mom and sister never find out about this. Nobody can know..."
    return

label cougar_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        the_person.char "Not yet [the_person.mc_title], I need to get warmed up first. Let's start a little slower and enjoy ourselves."
    else:
        the_person.char "I... we can't do that [the_person.mc_title]. I could be your mother, there are lines we just shouldn't cross."
    return

label cougar_sex_angry_reject(the_person):
    if the_person.sluttiness < 20:
        the_person.char "Oh god, what did you just say [the_person.mc_title]? I could be your mother, how could you even think about that!"
    else:
        the_person.char "What? Oh god, I... I'm too old for you [the_person.mc_title]! We can't do things like that, ever."
        "[the_person.possessive_title] turns away from you."
        the_person.char "You should go. This was a mistake. I should have known it was a mistake. I don't know what came over me."
    return

label cougar_climax_responses(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Ah! Yes [the_person.mc_title]! Right there on my...yesss...I'm cumming!"
        "She closes her eyes and goes into a frenzy of multiple orgasms."
    else:
        the_person.char "Oh god, that's it...keep going...yes [the_person.mc_title]..yes! Yes! YES!"
    return

label cougar_seduction_response(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            the_person.char "Do you need the touch of an experienced woman, [the_person.mc_title]? I know how stressed you can get you."
        else:
            the_person.char "Oh well... What do you need help with [the_person.mc_title]?."
    else:
        if the_person.sluttiness > 50:
            the_person.char "Well, how about you let me take care of you for a change?"
        elif the_person.sluttiness > 20:
            the_person.char "What do you mean [the_person.mc_title]? Do you want to spend some time with me?"
        else:
            the_person.char "I'm not sure I understand. What do you need [the_person.mc_title]?"
    return

label cougar_seduction_accept_crowded(the_person):
    if the_person.sluttiness < 35:
        "[the_person.possessive_title] pinches your ass cheek, whispering.."
        the_person.char "You can't say things like that in public [the_person.mc_title]! Think of my reputation."
        "She looks around quickly to see if anyone heard you, then takes your hand in hers."
        the_person.char "Come on, I'm sure we can find a quiet place were you can take care of me."

    elif the_person.sluttiness < 70:
        "[the_person.possessive_title] smiles and devours your body with her eyes, making sure nobody around you notices."
        the_person.char "Okay, but we need to be careful. I don't think people would understand our relationship. Let's find someplace quiet."

    else:
        the_person.char "Oh my [the_person.mc_title] ... why don't you take care of me right here!"
    return

label cougar_seduction_accept_alone(the_person):
    if the_person.sluttiness < 35:
        the_person.char "I can't believe I'm saying this... I'll play along for now, but you better not disappoint me."
        mc.name "Of course [the_person.title], I promise."
    elif the_person.sluttiness < 70:
        the_person.char "Oh [the_person.mc_title], what kind woman would I be if I said no? Come on, let's enjoy ourselves."
    else:
        the_person.char "Oh [the_person.mc_title], I'm so glad I make you feel this way. Come on, let's get started!"
    return

label cougar_sex_responses(the_person):
    if the_person.sluttiness > 50:
        if the_person.obedience > 130:
            the_person.char "Oh... Please [the_person.mc_title], keep doing that to me!"
        else:
            the_person.char "Ah yes, that's it [the_person.mc_title], give it to [the_person.possessive_title]!"
    else:
        "[the_person.possessive_title] closes her eyes."
        the_person.char "Yes [the_person.mc_title], just like that!"
    return

label cougar_seduction_refuse(the_person):
    if the_person.sluttiness < 30:
        the_person.char "Oh my god, what are you saying [the_person.mc_title]! Don't you think I'm a little too old for you? I'm sure you can't handle me..."
    elif the_person.sluttiness < 60:
        the_person.char "I'm sorry [the_person.mc_title], but we really shouldn't do this anymore. It's just... not going to happen."
    else:
        the_person.char "I'm sorry [the_person.mc_title], I know how much you like to spend time with me, but now isn't a good time for me. I'll make it up to you though, I promise."
    return

label cougar_flirt_response(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            the_person.char "Oh [the_person.mc_title] stop, you're making me horny again..."
        else:
            the_person.char "Oh stop [the_person.mc_title], it's not nice to make fun of me like that."
            "[the_person.possessive_title] blushes and looks away."
    else:
        if the_person.sluttiness > 50:
            the_person.char "Oh my...hmm... Thank you, [the_person.mc_title]."
            "[the_person.possessive_title] smiles at you and turns around slowly, giving you a full look at her body."
            the_person.char "Thank you for noticing me."
        else:
            the_person.char "Oh [the_person.mc_title], do you think I look good?"
    return

label cougar_cum_face(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            $ pronoun = person_body_shame_string(the_person, "litlle cum slut")
            the_person.char "Ah... do you like to see my face covered [the_person.mc_title]? Am I your good [pronoun]?"
        else:
            the_person.char "Oh, it's everywhere! Next time be more careful, I'm only doing this for you."
    else:
        if the_person.sluttiness > 70:
            the_person.char "Oh, yes [the_person.mc_title], I'm covered with your load!"
        else:
            the_person.char "[the_person.mc_title], next time don't mess up my makeup like this."
            "She pulls out a tissue and wipes her face quickly"
    return

label cougar_cum_mouth(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            the_person.char "It seems I did a good job, you have a wonderfull taste [the_person.mc_title]."
        else:
            the_person.char "I'm not sure I'm really into this, I'll try to like it for you [the_person.mc_title]."
    else:
        if the_person.sluttiness > 70:
            the_person.char "Mmm, you taste great [the_person.mc_title], you can fill my mouth with your load anytime..."
        else:
            "She spits your cum on the floor..."
            the_person.char "Give me a little heads up next time, [the_person.mc_title]."
    return

label cougar_sex_strip(the_person):
    if the_person.sluttiness < 20:
        if the_person.arousal < 50:
            the_person.char "I hope you don't mind if I slip this off..."
        else:
            the_person.char "I'm just going to take this off for you [the_person.mc_title]..."

    elif the_person.sluttiness < 60:
        if the_person.arousal < 50:
            the_person.char "How about I take this off for you."
        else:
            the_person.char "Oh [the_person.mc_title], you make me feel so young again!"
            the_person.char "I realy need to take some more off."
    else:
        if the_person.arousal < 50:
            the_person.char "I'm really horny, I bet you want to see some more of me."
        else:
            the_person.char "I need to get this off, I want to feel your young body against mine!"

    return

label cougar_suprised_exclaim(the_person):
    $rando = renpy.random.choice(["Oh my!","Oh, that's not good!", "Darn!", "Oh!", "My word!", "How about that!", "Shock and horror!", "I'll be jiggered!"])
    the_person.char "[rando]"
    return

label cougar_talk_busy(the_person):
    if the_person.obedience > 120:
        the_person.char "I'm sorry [the_person.mc_title], but I'm busy. Could we talk later?"
        the_person.char "Maybe you could take me somewhere nice."
    else:
        the_person.char "I'm sorry [the_person.mc_title], we will have to chit-chat later."
    return

label cougar_sex_watch(the_person, the_sex_person, the_position):
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry")
        the_person.char "[the_person.mc_title]! Why do you want me to watch that!"
        $ the_person.change_obedience(-2)
        $ the_person.change_happiness(-1)
        "[the_person.possessive_title] looks away while you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement - 10:
        $ the_person.draw_person(emotion = "sad")
        $ the_person.change_happiness(-1)
        the_person.char "[the_person.mc_title]! Could you at least try a more private place?"
        "[the_person.possessive_title] tries to avert her gaze while you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement:
        $ the_person.draw_person(emotion = "default")
        the_person.char "[the_person.mc_title], Why are you doing this here..."
        $ change_report = the_person.change_slut_temp(1)
        "[the_person.possessive_title] looks in another direction, but she keeps glancing at you and [the_sex_person.name]."

    elif the_person.sluttiness > the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person(emotion = "happy")
        the_person.char "Oh my, [the_person.mc_title]? You might want to teach me that someday..."
        $ change_report = the_person.change_slut_temp(2)
        "[the_person.possessive_title] studies [the_sex_person.name] while you [the_position.verb] her."

    else:
        $ the_person.draw_person(emotion = "happy")
        $ pronoun = person_body_shame_string(the_sex_person, "slut")
        the_person.char "You can do better [the_person.mc_title], give that little [pronoun] what she needs."
        "[the_person.possessive_title] watches you eagerly while [the_position.verb]ing [the_sex_person.name]."

    return

label cougar_being_watched(the_person, the_watcher, the_position):
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        the_person.char "Come on [the_person.mc_title], do me a little harder."
        $ the_person.change_arousal(1)
        "[the_person.possessive_title] seems turned on by [the_watcher.name] watching you and her [the_position.verb]."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        the_person.char "Don't listen to [the_watcher.name]. I'm just taking care of my young [the_person.mc_title]!"

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        $ the_person.change_arousal(1)
        the_person.char "[the_person.mc_title], I need you so much. I think [the_watcher.name] sees that."
        "[the_person.possessive_title] seems turned on by [the_watcher.name] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        the_person.char "Oh [the_person.mc_title], I know it's be wrong but being with you right here, just feels so right!"
        $ the_person.change_arousal(1)
        "The longer [the_watcher.name] keeps watching, the more turned on [the_person.possessive_title] gets."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        the_person.char "[the_person.mc_title], we shouldn't do this. Not here. What would people think of you with an older woman?"
        $ the_person.change_arousal(-1)
        $ the_person.change_slut_temp(-1)
        "[the_person.possessive_title] seems uneasy with [the_watcher.name] nearby."

    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        the_person.char "[the_watcher.name], I'm glad you don't critisize me."
        the_person.char "People say I shouldn't do this, but this young man makes me feel alive."
        $ the_person.change_arousal(1)
        $ the_person.change_slut_temp(1)
        "[the_person.possessive_title] seems more comfortable [the_position.verb]ing you with [the_watcher.name] around."

    return

label cougar_work_enter_greeting(the_person):
    if the_person.happiness < 80:
        if the_person.obedience > 120:
            "[the_person.possessive_title] gives you a nod and then turns back to her work."
        else:
            "[the_person.possessive_title] does not acknowlegde you when you enter."

    elif the_person.happiness > 120:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title] looks up from her work when you enter the room."
            the_person.char "Hello [the_person.mc_title]. Let me know if you need my help..."
            "Smiling at you while looking at your crotch, slowly turning back to her work."
        else:
            "[the_person.possessive_title] gives you warm smile."
            the_person.char "Hello [the_person.mc_title], good to see you!"
    else:
        if the_person.obedience < 90:
            "[the_person.possessive_title] glances up from her work."
            the_person.char "Hey, how's it going?"
        else:
            "[the_person.possessive_title] looks at you when you enter the room."
            the_person.char "Hello [the_person.mc_title], let me know if you need any help."
    return

label cougar_date_seduction(the_person): #TODO: Change this to be different.
    if the_person.sluttiness > the_person.love:
        if the_person.sluttiness > 40:
            the_person.char "You've been such a good boy tonight. Come with me tonight and I think you can make me feel good too..."
        else:
            the_person.char "You were a perfect gentleman tonight [the_person.mc_title], would you like to join me at my place?"
    else:
        if the_person.love > 40:
            the_person.char "I had such a wonderful time tonight. You make me feel so young and alive, want to take a nightcap at my place?"
        else:
            the_person.char "You've been a wonderful date. Would you like to share a bottle of wine at my place?"
    return
