## Cougar personality Mod by Tristimdorion
# All girls in town older than 45 get this personality trait
# See generic_personality_hook.rpy for more information

init 3 python:
    def cougar_personality_requirement():
        return True

    def change_cougar_personality_enabled(enabled):
        for person in all_people_in_the_game():
            update_cougar_personality(person)
        return

    cougar_personality_action = ActionMod("Cougar Personality", cougar_personality_requirement, "cougar_personality_dummy_label",
        menu_tooltip = "Enable or disable the cougar personality.", category="Personality", on_enabled_changed = change_cougar_personality_enabled)


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
        common_sexy_likes = ["doggy style sex", "giving blowjobs", "getting head", "anal sex", "public sex", "skimpy outfits", "anal creampies", "showing her tits", "showing her ass", "taking control", "not wearing underwear", "creampies", "drinking cum", "cum facials"],
        common_dislikes = ["Mondays", "the colour pink", "supply work", "conservative outfits", "work uniforms", "pants"],
        common_sexy_dislikes = ["being submissive", "being fingered", "missionary style sex", "bareback sex"],
        titles_function = cougar_titles, possessive_titles_function = cougar_possessive_titles, player_titles_function = cougar_player_titles)

    # don't add it to the default list of personalities, let the generic personality hook change it based on age

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

label cougar_introduction(the_person): # Copy paste from relaxed to fix crash
    mc.name "Excuse me, could I bother you for a moment?"
    "She turns around."
    $ the_person.set_title("???")
    the_person.char "I guess? What can I do for you?"
    mc.name "I know this is strange, but I saw you and I just needed to know your name."
    "She laughs with a twinkle in her eyes."
    the_person.char "Is that so? You're trying to impress me, aren't you."
    mc.name "Really, I really just wanted to talk to you."
    $ title_choice = get_random_title(the_person)
    $ formatted_title = the_person.create_formatted_title(title_choice)
    the_person.char "Well, if you insist, my name is [formatted_title]. It's nice to meet you..."
    $ the_person.set_title(title_choice)
    $ the_person.set_possessive_title(get_random_possessive_title(the_person))
    "With a commanding gaze she waits for you to introduce yourself."
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
        elif not the_person.relationship == "Single":
            $ so_title = SO_relationship_to_title(the_person.relationship)
            the_person.char "Oh my, what would my [so_title] say if he saw me here, like this....with you. Turn around, I need to cover myself!"
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
            if not the_person.relationship == "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "I... You just have to make sure my [so_title] never finds out about this. Nobody can know..."
            else:
                the_person.char "I... You just have to make sure your mom and sister never find out about this. Nobody can know..."
    return

label cougar_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        the_person.char "Not yet [the_person.mc_title], I need to get warmed up first. Let's start a little slower and enjoy ourselves."
    else:
        the_person.char "I... we can't do that [the_person.mc_title]. I could be your mother, there are lines we just shouldn't cross."
    return

label cougar_sex_angry_reject(the_person):
    if not the_person.relationship == "Single":
        $ so_title = SO_relationship_to_title(the_person.relationship)
        the_person.char "Wait, what? I have a [so_title], what did you think we were going to be doing?"
        "She glares at you and walks away."
    elif the_person.sluttiness < 20:
        the_person.char "Oh god, what did you just say [the_person.mc_title]?"
        the_person.char "I could be your mother, how could you even think about that!"
    else:
        the_person.char "What? Oh god, I... I'm too old for you [the_person.mc_title]! We can't do things like that, ever."
        "[the_person.possessive_title] turns away from you."
        the_person.char "You should go. This was a mistake. I should have known it was a mistake. I don't know what came over me."
    return


label cougar_climax_responses_foreplay(the_person):
    if the_person.sluttiness > 50:
        the_person.char "Oh my god! I'm going to... I'm going to..."
        the_person.char "{b}Cum!{/b} Ah!"
    else:
        the_person.char "Oh keep doing that [the_person.mc_title], I'm cumming!"
    return

label cougar_climax_responses_oral(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Oh fuck! Oh fuck, make me cum [the_person.mc_title]!"
        "She closes her eyes and squeals with pleasure."
    else:
        the_person.char "Oh my god, I'm going to cum. I'm going to cum!"
        "She closes her eyes and squeals with pleasure."
    return

label cougar_climax_responses_vaginal(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Ah! Yes [the_person.mc_title]! Right there on my...yesss...I'm cumming!"
        "She closes her eyes and goes into a frenzy of multiple orgasms."
    else:
        the_person.char "Oh god, that's it...keep going...yes [the_person.mc_title]..yes! Yes! YES!"
    return

label cougar_climax_responses_anal(the_person):
    if the_person.sluttiness > 80:
        the_person.char "I'm going to cum! Fuck my ass hard and make me cum!"
    else:
        the_person.char "Oh fuck, I think... I think I'm going to cum!"
    return

label cougar_seduction_response(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            the_person.char "Do you need the touch of an experienced woman, [the_person.mc_title]? I know how stressed you can get you."
        else:
            the_person.char "Oh sweety... What do you need help with [the_person.mc_title]?."
    else:
        if the_person.sluttiness > 50:
            the_person.char "Well, how about you let me take care of you for a change?"
        elif the_person.sluttiness > 20:
            the_person.char "What do you mean [the_person.mc_title]? Do you want to spend some time with me?"
        else:
            the_person.char "I'm not sure I understand. What do you need [the_person.mc_title]?"
    return

label cougar_seduction_accept_crowded(the_person):
    if the_person.relationship == "Single":
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
    else:
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (5*the_person.get_opinion_score("cheating on men")) > 60:
            the_person.char "No point wasting any time, right? I hope my [so_title] won't be too jealous."
        else:
            the_person.char "Okay, but we need to be careful. I don't want my [so_title] to find out what we're doing."
    return

label cougar_seduction_accept_alone(the_person):
    if the_person.relationship == "Single":
        if the_person.sluttiness < 35:
            the_person.char "I can't believe I'm saying this... I'll play along for now, but you better not disappoint me."
            mc.name "Of course [the_person.title], I promise."
        elif the_person.sluttiness < 70:
            the_person.char "Oh [the_person.mc_title], what kind woman would I be if I said no? Come on, let's enjoy ourselves."
        else:
            the_person.char "Oh [the_person.mc_title], I'm so glad I make you feel this way. Come on, let's get started!"
    else:
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (5*the_person.get_opinion_score("cheating on men")) > 60:
            the_person.char "Come on [the_person.mc_title], lets get going, screw my [so_title]!"
        else:
            the_person.char "I have a [so_title], I shouldn't be doing this..."
            "Her eyes tell quite a different story."
    return

label cougar_sex_responses_foreplay(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "Mmm, you know just what I like, don't you?"
        else:
            the_person.char "Oh my... that feels very good, [the_person.mc_title]!"

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            "[the_person.title] closes her eyes and lets out a loud, sensual moan."
        else:
            the_person.char "Keep doing that [the_person.mc_title]... Wow, you're good!"

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            the_person.char "Oh gods above that feels amazing!"
        else:
            the_person.char "Oh lord... I could get use to you touching me like this!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person.char "Touch me [the_person.mc_title], I want you to touch me!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "I should feel bad... but my egoistic [so_title] never touches me this way!"
                the_person.char "I need this, so badly!"
        else:
            the_person.char "I want you to keep touching me, I never guessed a young man could make me feel this way, but I want more of it!"
    return

label cougar_sex_responses_oral(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "Oh [the_person.mc_title], you're so good to me."
        else:
            the_person.char "Oh my... that feels..."
            "She sighs happily."
            the_person.char "Yes, right there!"

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            the_person.char "Yes, just like that! Mmm!"
        else:
            the_person.char "Keep doing that [the_person.mc_title], it's making me feel... very aroused."

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            the_person.char "Mmm, you really know how to put that tongue of yours to good use. That feels amazing!"
        else:
            the_person.char "Oh lord... your tongue is addictive, I just want more of it!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person.char "Oh I need this so badly [the_person.mc_title]! If you keep going you'll make me climax!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "I should feel bad, but you make me feel so good, my worthless [so_title] never does this for me!"
        else:
            the_person.char "Oh sweet lord in heaven... This feeling is intoxicating!"
    return

label cougar_sex_responses_vaginal(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "Mmm, I love feeling you inside of me!"
        else:
            the_person.char "Oh lord, you're so big... Whew!"

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            "[the_person.title] closes her eyes and lets out a loud, sensual moan."
        else:
            the_person.char "Oh that feels very good, keep doing that!"

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            the_person.char "Yes! Oh god yes, fuck me!"
        else:
            the_person.char "Oh lord your... cock feels so big!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person.char "Keep... keep going [the_person.mc_title]! I'm going to climax soon!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Keep going! My [so_title]'s tiny cock never makes me climax and I want it so badly!"
                the_person.char "I should feel bad, but all I want is your young cock in me right now!"
        else:
            "[the_person.title]'s face is flush as she pants and gasps."
    return

label cougar_sex_responses_anal(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "Mmm, you feel so big when you're inside me like this."
        else:
            the_person.char "Be gentle, it feels like you're going to tear me in half!"

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            the_person.char "Give it to me, [the_person.mc_title], give me every last inch!"
        else:
            the_person.char "Oh god! Oww! Move a little slower..."

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            the_person.char "I hope my ass isn't too tight for you, I don't want you to cum early."
        else:
            the_person.char "I don't think I will be able to walk straight after this!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person.char "You're young cock feels so stuffed inside me! Keep going, I might actually climax!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "My [so_title] always wanted to try anal, but I told him it would never happen. My rear entrance belongs to you, [the_person.mc_title]!"
        else:
            the_person.char "Oh lord, this is actually starting to feel good... If you keep this up, I'm going to cum!"
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
    elif not the_person.relationship == "Single":
        $so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (the_person.get_opinion_score("cheating on men")*5) > 60:
            the_person.char "Well thank you [the_person.mc_title]. Don't let my [so_title] hear you say that though, he might get jealous."
            "She smiles and winks mischievously."
        else:
            the_person.char "I have a [so_title], you really shouldn't be talking to me like that..."
            "She seems more worried about being caught than flirting with you."
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
            $ pronoun = person_body_shame_string(the_person, "little cum slut")
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
            the_person.char "It seems I did a good job, you have a wonderful taste [the_person.mc_title]."
        else:
            the_person.char "I'm not sure I'm really into this, I'll try to like it for you [the_person.mc_title]."
    else:
        if the_person.sluttiness > 70:
            the_person.char "Mmm, you taste great [the_person.mc_title], you can fill my mouth with your load anytime..."
        else:
            "She spits your cum on the floor..."
            the_person.char "Give me a little heads up next time, [the_person.mc_title]."
    return

label cougar_cum_vagina(the_person):
    if mc.condom:
        if the_person.sluttiness > 75 or the_person.get_opinion_score("creampies") > 0:
            the_person.char "Oh... your seed is so close to me. Just a thin, thin condom in the way..."
        else:
            the_person.char "I can feel your seed through the condom. Well done, there's a lot of it."

    else:
        if the_person.sluttiness > 75 or the_person.get_opinion_score("creampies") > 0:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Yes, give me your seed!"
                the_person.char "If I become pregnant I can say it's my [so_title]'s. I'm sure he would believe it."
            else:
                the_person.char "Mmm, your semen is so nice and warm. I wonder how potent it is. You might have gotten me pregnant, you know."
        else:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Oh no... You need to cum outside of me [the_person.mc_title]."
                the_person.char "What would I tell my [so_title] if I got pregnant? He might not believe it's his!"
            else:
                the_person.char "Oh no... You need to cum outside of me [the_person.mc_title]."
                the_person.char "I'm in no position to be getting pregnant."
                the_person.char "Well, I suppose you have me in the literal position to get pregnant, but you know what I mean."
    return

label cougar_cum_anal(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            $ pronoun = person_body_shame_string(the_person, "little anal slave")
            the_person.char "Ah...yes pump your seed into your [pronoun]?"
        else:
            the_person.char "Oh my, you filled up my bottom, remember [the_person.mc_title], I'm only doing this for you."
    else:
        if the_person.sluttiness > 75 or the_person.get_opinion_score("anal creampies") > 0:
            the_person.char "Cum inside me [the_person.mc_title], fill my ass with your cum!"
        else:
            the_person.char "Oh lord, I hope I'm ready for this!"
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
            the_person.char "I really need to take some more off."
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
        $ the_person.change_slut_temp(1)
        "[the_person.possessive_title] looks in another direction, but she keeps glancing at you and [the_sex_person.name]."

    elif the_person.sluttiness > the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person(emotion = "happy")
        the_person.char "Oh my, [the_person.mc_title]? You might want to teach me that someday..."
        $ the_person.change_slut_temp(2)
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
        the_person.char "[the_watcher.name], I'm glad you don't criticize me."
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
            "[the_person.possessive_title] does not acknowledge you when you enter."

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
    if the_person.relationship == "Single":
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
    else:
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person.char "You've been such a good boy tonight. My [so_title] went night fishing with some buddies, so..."
                the_person.char "Join me tonight and I think you can make me feel good..."
            else:
                the_person.char "You were a perfect gentleman tonight [the_person.mc_title]. It's been years since I had this much fun with my [so_title]."
                the_person.char "He has his poker night with some friends. Would you like to join me at my place and have glass of wine?"
        else:
            if the_person.love > 40:
                the_person.char "I don't want this night to end. My [so_title] is on a business trip this weekend."
                the_person.char "Do you want to come over to my place so we can spend more time together?"
            else:
                the_person.char "Tonight was fantastic. I think my [so_title] is out for the night."
                the_person.char "So do you want to come over to my place for a cup of coffee?"
    return

label cougar_sex_end_early(the_person):
    if the_person.sluttiness > 50:
        if the_person.love > 40:
            if the_person.arousal > 60:
                the_person.char "Is that it? You're going to drive me crazy [the_person.mc_title], I'm so horny..."
            else:
                the_person.char "All done? I hope you were having a good time."
        else:
            if the_person.arousal > 60:
                the_person.char "Already done? I don't know how you can stop, I'm so excited at the moment!"
            else:
                the_person.char "Leaving already? Well, that's disappointing."

    else:
        if the_person.love > 40:
            if the_person.arousal > 60:
                the_person.char "That's it? Well, you could at least make me cum too."
            else:
                the_person.char "All done? Maybe we can pick this up the next time when we're alone."
        else:
            if the_person.arousal > 60:
                the_person.char "I... I don't know what to say, did I exhaust you?"
            else:
                the_person.char "That's all you wanted? I guess we're finished then."
    return

label cougar_sex_take_control(the_person):
    if the_person.arousal > 60:
        the_person.char "I just can't let you go [the_person.mc_title], You are going to finish what you started!"
    else:
        the_person.char "Do you think you're going somewhere? You are not yet done [the_person.mc_title]."
    return

label cougar_sex_beg_finish(the_person):
    "Wait, you can't stop now? Please [the_person.mc_title], I'm almost there, I'll do anything!"
    return
