init 5 python:
    doggy_anal.scenes.append("scene_SB_doggy_anal_1")
    doggy_anal.scenes.append("scene_SB_doggy_anal_2")

    config.label_overrides["transition_default_doggy_anal"] = "transition_default_doggy_anal_enhanced"

label scene_SB_doggy_anal_1(the_girl, the_location, the_object):
    "You give [the_girl.possessive_title]'s ass a good hard spank. She lets out a loud yelp."
    $ the_girl.call_dialogue("sex_responses_anal")
    if the_girl.sex_skills["Anal"] < 2: #Inexperienced
        "[the_girl.possessive_title] reflexively starts to pull away after you spank her. You grab her hips to keep her from pulling off completely."
        the_girl.char "Sorry, I just... I don't do this very often... please just be gentle with me!"
        "You pull her hips back toward you slowly. Her inexperienced ass yields to your penis and she sighs as you bottom out."
        "You decide to give her a little break in the intensity of your fucking. Leaving yourself deep inside her, you knead her ass cheeks with both hands."
        the_girl.char "mmm, that feels good [the_girl.mc_title]. Can I touch myself while you do that?"
        menu:
            "Masturbate for me":
                 "Encouraged by your response, [the_girl.possessive_title] reaches down with one hand and begins to rub her clit."
                 "You take it slow, and you revel in the delicious pleasure of each penetration as you thrust. [the_girl.possessive_title] struggles to hold herself up with one hand while the other works circles around her clit."
                 if the_girl.get_opinion_score("masturbating") > 0:
                     "[the_girl.possessive_title] moves her fingers masterfully across her pussy. You can tell she masturbates often."
                     $ the_girl.discover_opinion("masturbating")
                     $ the_girl.change_arousal(the_girl.get_opinion_score("masturbating" * 5))
                 if the_girl.sluttiness > 100:
                     the_girl.char "I'm sorry [the_girl.mc_title], I'll try to get better at this. Having you in my ass is so intense..."
                 else:
                     "[the_girl.possessive_title] seems to be enjoying the anal penetration a bit more now that she is touching herself."
            "Fuck me with your ass":
                 if the_girl.obedience > 130 or the_girl.get_opinion_score("being submissive") > 0:
                     the_girl.char "Yes sir. I'll do my best"
                 else:
                     the_girl.char "I'll give it my best, but this better be worth it..."
                 "[the_girl.possessive_title] slowly eases forward until just the tip remains inside, then slowly backs her ass back onto you. She is trying to obey but you can tell she is struggling to take you."
                 "The next she starts to ease forward, you put your hand on her hips for a second to stop her. You spit into your hand then rub it along your shaft a bit, hoping it will make the penetration easier."
                 the_girl.char "Mmm, that's a bit better..."
                 "With the extra lube, [the_girl.possessive_title] resumes fucking you. She still has a fairy slow pace, but is a bit quicker than before."

    else:
        "In response to your spanking, [the_girl.possessive_title] thrusts herself back against you. Your penis is completely consumed by her bowel and she moans lewdly."
        "When she starts to pull off you give her other ass check a hard swat. She buries her face in [the_object.name] and moans as she pushes herself back onto you again."
        the_girl.char "Oh fuck [the_girl.mc_title], I needed this so bad. Don't stop, it feels so good when you go deep!"
        "[the_girl.possessive_title]'s ass feels so tight you are tempted to let her continue setting the pace, but you worry she might get the wrong idea if you let this little slut take charge."
        menu:
            "Fuck me with your ass":
                 "You decide to see what [the_girl.possessive_title] can do if you let her take control of the pace. Encouraged by your words, she eagerly works your cock with her ass." ###FINISH
                 the_girl.char "Mmm, does it feel good when I work it like this?"
                 "[the_girl.possessive_title] begins to twerk up and down your shaft with quick, shallow movements."
                 if mc.arousal > 70:
                      mc.name "Damn that feels good. You're gonna make me cum if you keep that up. Where do you want my load?"
                      if mc.condom:
                           the_girl.char "Just shove it in deep and dump it right in my ass. You still have that condom on, right?"
                      elif SB_check_fetish(the_girl, cum_internal_role):
                          the_girl.char "Just shove it in deep and dump it right in my ass. You know I need your cum inside me, right where it belongs!"
                      elif SB_check_fetish(the_girl, cum_external_role):
                         the_girl.char "Anywhere on my skin! My ass, my face, I don't care, just spray me down with it! With you know I need it like that!"
                      elif the_girl.get_opinion_score("creampies") > 0:
                           the_girl.char "You should just shove it in as deep as you can and cum inside me."
                      elif the_girl.get_opinion_score("being covered in cum") > 0:
                           the_girl.char "You should pull out and cum all over my ass. That would be so hot..."
                      elif the_girl.get_opinion_score("cum facials") > 0:
                           the_girl.char "Tell me when you are about to cum and I'll let you cum all over my face..."
                      elif the_girl.obedience > 130:
                           the_girl.char "Cum wherever you want to... I just want to please you, sir."
                      else:
                           the_girl.char "I don't know... wherever you want I guess?"
                 else:
                      mc.name "Wow, your ass is amazing. Where'd you learn to work it like that girl? Have you been practicing?"
                      if SB_check_fetish(the_girl, anal_fetish_role):
                           "In response, she slams her ass all the way back on your dick. She grinds her hips left and right up against you."
                           the_girl.char "Practicing, dreaming, begging for your cock in my ass! Every moment my rear is empty I'm craving your dick deep inside it."
                           "You can feel her tense and relax her muscles in her ass rhythmically, messaging your shaft while you remain totally engulfed inside her."
                           mc.name "Fuck [the_girl.title], I dont't know how you do that, but its amazing."
                           "[the_girl.possessive_title] sighs. She is truly addicted to getting her tight back passage fucked"
                      elif the_girl.get_opinion_score("anal sex") > 0:
                           "In response, she slams her ass all the way back on your dick. She grinds her hips left and right up against you."
                           "You can feel her tense and relax her muscles in her ass rhythmically, messaging your shaft while you remain totally engulfed inside her."
                           mc.name "Wow, I guess so! That feels amazing. Feel free to practice anytime you want on me, [the_girl.title]!"
                           "[the_girl.possessive_title] sighs. You can tell having your dick in her ass is very fulfilling for her."
                      else:
                           "[the_girl.possessive_title] looks back at you."
                           the_girl.char "Honestly, I'm not usually into butt stuff... but I just want to make you feel so good..."
                 "[the_girl.possessive_title] continues to twerk her ass up and down on your penis. How does she make it look so easy?"
            "I'm in charge here":
                 "Sensing that your slut is getting out of hand, you quickly take charge. You grab her by the hair and pull her head back until her hands are no longer on the ground, taking away all her leverage."
                 $ the_girl.call_dialogue("suprised_exclaim")
                 "You lean forward and whisper into [the_girl.possessive_title]'s ear."
                 mc.name "I know you dream about my dick in your ass constantly and it feels good to finally have that dream come true, but don't forget who is in charge around here."
                 if the_girl.obedience > 130 or the_girl.get_opinion_score("being submissive") > 0:
                     $ the_girl.discover_opinion("being submissive")
                     if the_girl.get_opinion_score("being submissive") > 0:
                         $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive" * 5))
                         "For once, [the_girl.possessive_title] is speechless. She can only whimper softly in total submission to you."
                     else:
                         the_girl.char "I'm sorry [the_girl.mc_title], I couldn't help myself. Please use me however you want, I'll be good I promise!"
                     "You give her a couple slow, heavy thrusts before releasing her hair. She returns her hands to the ground and moans when you resume your slow, methodical fucking."
                 else :
                     the_girl.char "Okay! Geesh! Be careful with my hair, that hurts!"
                #TODO this option is kinda boring... expand some?

    return


label scene_SB_doggy_anal_2(the_girl, the_location, the_object):
    "[the_girl.possessive_title] lowers her shoulders against the [the_object.name] and groans as you fuck her from behind."
    the_girl.char "Ah... I feel so full!"
    "You reach forward and place your hands on [the_girl.possessive_title]'s shoulders. With each thrust you pull her back onto you forcefully, your hips smacking her ass cheeks loudly. She arches her back and lets out a series of satisfied yelps."
    $ the_girl.call_dialogue("sex_responses_anal")
    if the_girl.arousal > 80:
        "[the_girl.possessive_title]'s pussy is dripping wet. A damp spot has begun to accumulate below her pussy as a result of your rutting."
        the_girl.char "Ohhh, you feel so fucking good in my ass."
    else:
        "[the_girl.possessive_title] seems to be enjoying the fucking you are giving her. She yelps in response to one particularly eager thrust."
        the_girl.char "God dammit, you're so fucking big. You feel huge in my ass."
    if the_girl.get_opinion_score("giving handjobs") > 0:
        "[the_girl.possessive_title] reaches down and begins to stroke and rub your scrotum with one hand, while with the other hand she reaches back and pulls her ass cheeks apart."
        $ the_girl.change_arousal(the_girl.get_opinion_score("giving handjobs" * 2))
    elif the_girl.get_opinion_score("masturbating") > 0:
        "You notice that[the_girl.possessive_title] now has one hand on her pussy, rubbing her clit, and with the other hand she reaches back and pulls her ass cheeks apart."
        $ the_girl.change_arousal(the_girl.get_opinion_score("masturbating" * 3))
    else:
        "[the_girl.possessive_title] reaches back with both hands and spreads her ass cheeks apart."
    "With her ass cheeks spread, you consider for a moment, should you pull back and admire the view, or shove yourself down deep?"
    menu:
            "Admire her ass":
                "You pull yourself out of [the_girl.possessive_title]'s ass for moment and admire the soft, round cheeks of carnal pleasure in front of you."
                "Her asshole gapes a bit from your sudden pullout, and she quickly turns her head to see why she suddenly feels so empty."
                "[the_girl.possessive_title] realizes you are taking a moment to check out her backside."
                if the_girl.get_opinion_score("showing her ass"):
                    the_girl.char "Do you like my ass, [the_girl.mc_title]? I've caught you checking it out before. It gets me so hot when I feel your eyes checking out my backside..."
                    $ the_girl.change_arousal(the_girl.get_opinion_score("showing her ass" * 5))###
                    $ the_girl.discover_opinion("showing her ass")
                    "[the_girl.possessive_title] moves her ass side to side, gyrating her hips for you while keeping her ass cheeks spread wide."
                elif the_girl.get_opinion_score("being covered in cum"):
                    the_girl.char "Do you like what you see, [the_girl.mc_title]? I bet it is going to look even more amazing covered in your hot cum."
                    $mc.change_arousal(5)
                    "The thought of painting [the_girl.possessive_title]'s ass with your semen makes your cock twitch in anticipation."
                elif the_girl.sluttiness > 100:
                    the_girl.char "Hey, you can check my ass out later, right now you're supposed to be fucking it, [the_girl.mc_title]!"
                    "[the_girl.possessive_title] tries to push herself back on to you, but from her angle she is unable to get you to penetrate her again unless you help."
                    "She quickly gives up an resorts to rubbing her ass up and down along the length of your penis."
                elif the_girl.obedience > 130:
                    "[the_girl.possessive_title] blushes. The conflict of the dirtiness of the act of anal sex and her obedience to you are clear in her face."
                    the_girl.char "Sir... don't you find my ass pleasing? Why did you pull out?"
                    mc.name "Dont worry, [the_girl.title], I'll fuck your ass some more in a second, I just needed to take a moment and how loose your backdoor has gotten so far."
                    $ the_girl.change_slut_temp(2)
                    "[the_girl.possessive_title]'s cheeks turn even redder with your dirty talk. She puts her head down again, but leaves her cheeks spread, ready for you to resume fucking her whenever you are ready."
                else:
                    the_girl.char "Hey, why'd you pull out? I was just getting used to how thick you are..."
                "After taking a moment appraising [the_girl.possessive_title]'s buttocks, you decide to get back to the act."
                "With gentle pressure, you slowly fill her ass with your erection again. [the_girl.possessive_title] groans as you resume your thrusting."
            "Shove it in deep":
                "You decide with her cheeks spread wide to see how deep you can get yourself into [the_girl.possessive_title]. "
                "With her hands busy, she has no way of holding up your weight as you push yourself forward and then down on top of her, your full body weight pushing her prone down onto the [the_object.name]."
                "[the_girl.possessive_title] whimpers, her body now pinned between your body and [the_object.name]."
                if SB_check_fetish(the_girl, anal_fetish_role):
                    "Despite having no leverage, [the_girl.possessive_title] wriggles her ass against you as best as she can. Even with no room to move, her love for anal sex drives her to try to milk your cock."
                    "You enjoy her efforts before you speak clearly to her."
                    mc.name "Does this feel better than that plug? Is this what you're imagining everytime you push that plug up your ass?"
                    "[the_girl.possessive_title] is writhing in pleasure, having her fetish of anal sex fulfilled."
                    the_girl.char "Oh god it is. Everytime I play with my ass and all I can think about is your big meaty dick buried inside me."
                    "You grab her hair at the base of her scalp and pull her head back before whispering into her ear."
                    mc.name "Don't worry, slut. This won't be the last time I fill your ass with my cock."
                    "You can see goosebumps all over [the_girl.possessive_title]'s skin. She moans and then begs you to keep fucking her."
                elif the_girl.get_opinion_score("creampies") > 0:
                    the_girl.char "Holy hell that is deep... tell me... tell me you'll push it this deep again when you cum... that would be so hot!"
                    $mc.change_arousal(5)
                    "In your mind, you play out the fantasy of cumming so deep in [the_girl.possessive_title]'s ass, even when you pull out not a drop of your seed leaks out."
                    "You give the idea serious consideration. You can tell she would love it if you did."
                elif the_girl.get_opinion_score("anal sex") > 0:
                    "Despite having no leverage, [the_girl.possessive_title] wriggles her ass against you as best as she can. Even with no room to move, her love for anal sex drives her to milk your cock."
                    "You lower your face down behind her head and whisper into her ear."
                    mc.name "Mmm, so rear entry is how you like it, slut? Don't worry, this won't be the last time you feel my cock ravage your back door."
                    "You can see goosebumps all over [the_girl.possessive_title]'s skin. You wonder how many times you can make her cum before you blow your load."
                    $ the_girl.change_slut_temp(2)
                elif the_girl.sluttiness > 100:
                    the_girl.char "Oh fuck, bury it in me [the_girl.mc_title]! I don't think I've ever felt so full..."
                else:
                    "[the_girl.possessive_title] lets out a loud groan. You can tell she isn't used to being penetrated like this, but she is taking it as best as she can."
                    the_girl.char "God [the_girl.mc_title] that is so intense... please just try to be a little more gentle okay?"
                "You take a few seconds to enjoy being engulfed by her back passage, then give her a few slow, probing thrusts."
                "After a minute or two slow, deep thrusts you decide to move back to doggy. You push yourself up off of [the_girl.possessive_title]'s back, and she follows, getting on all fours again to resume your fucking."

    return

label transition_default_doggy_anal_enhanced(the_girl, the_location, the_object):
    if the_person.has_taboo("anal_sex"):
        if the_girl.effective_sluttiness(doggy_anal.associated_taboo) > doggy_anal.slut_cap or the_girl.get_opinion_score("showing her ass") > 0:
            $ the_girl.draw_person(position = "back_peek", the_animation = ass_bob)
            "She stands facing away from you and jiggles her butt playfully."
            mc.name "Get on your knees, I want to get a look at this ass."
            the_girl.char "This big fat ass? You finally want to take a closer look?"
            mc.name "I said on your knees."
            $ the_girl.draw_person(position = "doggy", the_animation = ass_bob, animation_effect_strength = 0.7)
            "She gets onto the [the_object.name] and points her butt in your direction. She lowers her shoulders and works her hips for you."

        else:
            $ the_girl.draw_person(position = "kneeling1")
            mc.name "Get on your knees."
            mc.name "Good girl, now spin around and show me that ass."
            "She nods and turns around."
            $ the_girl.draw_person(position = "doggy")
            mc.name "Nice. Now shake it for me."
            the_girl.char "Like... this?"
            $ the_girl.draw_person(position = "doggy", the_animation = ass_bob, animation_effect_strength = 0.4)
            "[the_girl.title] works her hips and jiggles her ass for you."
            mc.name "Getting there, a little faster now."
            $ the_girl.draw_person(position = "doggy", the_animation = ass_bob, animation_effect_strength = 0.7)
            "She speeds up."
        the_girl.char "Is that what you wanted?"
        "You slap your cock down on her ass and grab her tight cheeks, spreading them apart to get a look at her asshole."
        mc.name "It's a start. I think it's time we stretched you open."
        $ the_girl.call_dialogue(doggy_anal.associated_taboo+"_taboo_break")
        "You hold onto [the_girl.title]'s hips with one hand and your cock with the other, guiding it as you press it against her tight hole."
        if the_girl.sex_skills["Anal"] > 2:
            "She gasps as your tip starts to spread her open. She lowers her shoulders and pushes her hips against you, helping the process."
            the_girl.char "Oh god... Mfphhhh!"

        else:
            "She gasps as your tip tries to spread open her impossibly tight asshole. She tries to pull away, but you pull on her waist and bring her closer."
            mc.name "Come on, you'll get there."
            "You spit onto your cock and try again. This time making better progress, sliding the tip of your dick into [the_girl.title]'s ass."
            the_girl.char "Oh god... Fuck!"
        "Inch by inch you slide your entire length into [the_girl.possessive_title]. She grunts and gasps the whole way down."
        "When stop when you've bottomed out, to give your cock time to properly stretch her out."
        the_girl.char "I think... I'm ready for you to move some more..."
        "You pull back a little bit and give her a few testing strokes. When she can handle those you speed up, until you're thrusting your entire length."
        $ the_girl.break_taboo("anal_sex")
    else:
        "[the_girl.title] gets on her hands and knees as you kneel behind her. You bounce your hard shaft on her ass a couple of times before lining yourself up with tight asshole."
        mc.name "Ready?"
        the_girl.char "I... I think so."
        "You hold onto her hips and push forward, spreading her ass with your large cock. She gasps and balls her fists, until finally you've buried your shaft in her."
        "After giving her a second to acclimatize you start to thrust in and out, slowly at first but picking up speed."

    return
