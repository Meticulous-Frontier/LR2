init 5 python:
    doggy_anal.scenes.append("scene_SB_doggy_anal_1")
    doggy_anal.scenes.append("scene_SB_doggy_anal_2")

    doggy_anal.transition_default = "transition_default_doggy_anal_enhanced"

label scene_SB_doggy_anal_1(the_girl, the_location, the_object):
    "You give [the_girl.possessive_title!l]'s ass a good hard spank. She lets out a loud yelp."
    $ the_girl.call_dialogue("sex_responses_anal")
    if the_girl.sex_skills["Anal"] < 2: #Inexperienced
        "[the_girl.possessive_title] reflexively starts to pull away after you spank her. You grab her hips to keep her from pulling off completely."
        the_girl "Sorry, I just... I don't do this very often... please just be gentle with me!"
        "You pull her hips back toward you slowly. Her inexperienced ass yields to your penis and she sighs as you bottom out."
        "You decide to give her a little break in the intensity of your fucking. Leaving yourself deep inside her, you knead her ass cheeks with both hands."
        the_girl "Mmmm, that feels good [the_girl.mc_title]. Can I touch myself while you do that?"
        menu:
            "Masturbate for me":
                "Encouraged by your response, [the_girl.possessive_title!l] reaches down with one hand and begins to rub her clit."
                "You take it slow, and you revel in the delicious pleasure of each penetration as you thrust. [the_girl.possessive_title] struggles to hold herself up with one hand while the other works circles around her clit."
                if the_girl.get_opinion_score("masturbating") > 0:
                    "[the_girl.possessive_title] moves her fingers masterfully across her pussy. You can tell she masturbates often."
                    $ the_girl.discover_opinion("masturbating")
                    $ the_girl.change_arousal(the_girl.get_opinion_score("masturbating" * 5))
                if the_girl.sluttiness > 100:
                    the_girl "I'm sorry [the_girl.mc_title], I'll try to get better at this. Having you in my ass is so intense..."
                else:
                    "[the_girl.possessive_title] seems to be enjoying the anal penetration a bit more now that she is touching herself."
            "Fuck me with your ass":
                if the_girl.obedience > 130 or the_girl.get_opinion_score("being submissive") > 0:
                    the_girl "Yes sir. I'll do my best."
                else:
                    the_girl "I'll give it my best, but this better be worth it..."
                "[the_girl.possessive_title] slowly eases forward until just the tip remains inside, then slowly backs her ass back onto you. She is trying to obey but you can tell she is struggling to take you."
                "The next she starts to ease forward, you put your hand on her hips for a second to stop her. You spit into your hand then rub it along your shaft a bit, hoping it will make the penetration easier."
                the_girl "Mmm, that's a bit better..."
                "With the extra lube, [the_girl.possessive_title!l] resumes fucking you. She still has a fairy slow pace, but is a bit quicker than before."

    else:
        "In response to your spanking, [the_girl.possessive_title!l] thrusts herself back against you. Your penis is completely consumed by her bowel and she moans lewdly."
        "When she starts to pull off you give her other ass check a hard swat. She buries her face in [the_object.name] and moans as she pushes herself back onto you again."
        the_girl "Oh fuck [the_girl.mc_title], I needed this so bad. Don't stop, it feels so good when you go deep!"
        "[the_girl.possessive_title]'s ass feels so tight you are tempted to let her continue setting the pace, but you worry she might get the wrong idea if you let this little slut take charge."
        menu:
            "Fuck me with your ass":
                 "You decide to see what [the_girl.possessive_title!l] can do if you let her take control of the pace. Encouraged by your words, she eagerly works your cock with her ass." ###FINISH
                 the_girl "Mmm, does it feel good when I work it like this?"
                 "[the_girl.possessive_title] begins to twerk up and down your shaft with quick, shallow movements."
                 if mc.arousal > 70:
                      mc.name "Damn that feels good. You're gonna make me cum if you keep that up. Where do you want my load?"
                      if mc.condom:
                           the_girl "Just shove it in deep and dump it right in my ass. You still have that condom on, right?"
                      elif the_girl.has_cum_fetish():
                           the_girl "Anywhere on my skin! My ass, my face, I don't care, just spray me down with it! With you know I need it like that!"
                      elif the_girl.get_opinion_score("anal creampies") > 0:
                           the_girl "You should just shove it in as deep as you can and cum inside me."
                      elif the_girl.get_opinion_score("being covered in cum") > 0:
                           the_girl "You should pull out and cum all over my ass. That would be so hot..."
                      elif the_girl.get_opinion_score("cum facials") > 0:
                           the_girl "Tell me when you are about to cum and I'll let you cum all over my face..."
                      elif the_girl.obedience > 130:
                           the_girl "Cum wherever you want to... I just want to please you, sir."
                      else:
                           the_girl "I don't know... wherever you want I guess?"
                 else:
                      mc.name "Wow, your ass is amazing. Where'd you learn to work it like that girl? Have you been practicing?"
                      if the_girl.has_role(anal_fetish_role):
                           "In response, she slams her ass all the way back on your dick. She grinds her hips left and right up against you."
                           the_girl "Practicing, dreaming, begging for your cock in my ass! Every moment my rear is empty I'm craving your dick deep inside it."
                           "You can feel her tense and relax her muscles in her ass rhythmically, messaging your shaft while you remain totally engulfed inside her."
                           mc.name "Fuck [the_girl.title], I don't know how you do that, but it's amazing."
                           "[the_girl.possessive_title] sighs. She is truly addicted to getting her tight back passage fucked"
                      elif the_girl.get_opinion_score("anal sex") > 0:
                           "In response, she slams her ass all the way back on your dick. She grinds her hips left and right up against you."
                           "You can feel her tense and relax her muscles in her ass rhythmically, messaging your shaft while you remain totally engulfed inside her."
                           mc.name "Wow, I guess so! That feels amazing. Feel free to practice anytime you want on me, [the_girl.title]!"
                           "[the_girl.possessive_title] sighs. You can tell having your dick in her ass is very fulfilling for her."
                      else:
                           "[the_girl.possessive_title] looks back at you."
                           the_girl "Honestly, I'm not usually into butt stuff... but I just want to make you feel so good..."
                 "[the_girl.possessive_title] continues to twerk her ass up and down on your penis. How does she make it look so easy?"
            "I'm in charge here":
                 "Sensing that your slut is getting out of hand, you quickly take charge. You grab her by the hair and pull her head back until her hands are no longer on the ground, taking away all her leverage."
                 $ the_girl.call_dialogue("surprised_exclaim")
                 "You lean forward and whisper into [the_girl.possessive_title!l]'s ear."
                 mc.name "I know you dream about my dick in your ass constantly and it feels good to finally have that dream come true, but don't forget who is in charge around here."
                 if the_girl.obedience > 130 or the_girl.get_opinion_score("being submissive") > 0:
                     $ the_girl.discover_opinion("being submissive")
                     if the_girl.get_opinion_score("being submissive") > 0:
                         $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive" * 5))
                         "For once, [the_girl.possessive_title!l] is speechless. She can only whimper softly in total submission to you."
                     else:
                         the_girl "I'm sorry [the_girl.mc_title], I couldn't help myself. Please use me however you want, I'll be good I promise!"
                     "You give her a couple slow, heavy thrusts before releasing her hair. She returns her hands to the ground and moans when you resume your slow, methodical fucking."
                 else :
                     the_girl "Okay! Geesh! Be careful with my hair, that hurts!"
                #TODO this option is kinda boring... expand some?

    return


label scene_SB_doggy_anal_2(the_girl, the_location, the_object):
    "[the_girl.possessive_title] lowers her shoulders against the [the_object.name] and groans as you fuck her from behind."
    the_girl "Ah... I feel so full!"
    "You reach forward and place your hands on [the_girl.possessive_title!l]'s shoulders. With each thrust you pull her back onto you forcefully, your hips smacking her ass cheeks loudly. She arches her back and lets out a series of satisfied yelps."
    $ the_girl.call_dialogue("sex_responses_anal")
    if the_girl.arousal > 80:
        "[the_girl.possessive_title]'s pussy is dripping wet. A damp spot has begun to accumulate below her [the_girl.pubes_description] pussy as a result of your rutting."
        the_girl "Ohhh, you feel so fucking good in my ass."
    else:
        "[the_girl.possessive_title] seems to be enjoying the fucking you are giving her. She yelps in response to one particularly eager thrust."
        the_girl "God dammit, you're so fucking big. You feel huge in my ass."
    if the_girl.get_opinion_score("giving handjobs") > 0:
        "[the_girl.possessive_title] reaches down and begins to stroke and rub your scrotum with one hand, while with the other hand she reaches back and pulls her ass cheeks apart."
        $ the_girl.change_arousal(the_girl.get_opinion_score("giving handjobs" * 2))
    elif the_girl.get_opinion_score("masturbating") > 0:
        "You notice that [the_girl.possessive_title!l] now has one hand on her [the_girl.pubes_description] pussy, rubbing her clit, and with the other hand she reaches back and pulls her ass cheeks apart."
        $ the_girl.change_arousal(the_girl.get_opinion_score("masturbating" * 3))
    else:
        "[the_girl.possessive_title] reaches back with both hands and spreads her ass cheeks apart."
    "With her ass cheeks spread, you consider for a moment, should you pull back and admire the view, or shove yourself down deep?"
    menu:
        "Admire her ass":
            "You pull yourself out of [the_girl.possessive_title!l]'s ass for moment and admire the soft, round cheeks of carnal pleasure in front of you."
            "Her asshole gapes a bit from your sudden pullout, and she quickly turns her head to see why she suddenly feels so empty."
            "[the_girl.possessive_title] realizes you are taking a moment to check out her backside."
            if the_girl.get_opinion_score("showing her ass"):
                the_girl "Do you like my ass, [the_girl.mc_title]? I've caught you checking it out before. It gets me so hot when I feel your eyes checking out my backside..."
                $ the_girl.change_arousal(the_girl.get_opinion_score("showing her ass" * 5))###
                $ the_girl.discover_opinion("showing her ass")
                "[the_girl.possessive_title] moves her ass side to side, gyrating her hips for you while keeping her ass cheeks spread wide."
            elif the_girl.get_opinion_score("being covered in cum"):
                the_girl "Do you like what you see, [the_girl.mc_title]? I bet it is going to look even more amazing covered in your hot cum."
                $mc.change_arousal(5)
                "The thought of painting [the_girl.possessive_title!l]'s ass with your semen makes your cock twitch in anticipation."
            elif the_girl.sluttiness > 100:
                the_girl "Hey, you can check my ass out later, right now you're supposed to be fucking it, [the_girl.mc_title]!"
                "[the_girl.possessive_title] tries to push herself back on to you, but from her angle she is unable to get you to penetrate her again unless you help."
                "She quickly gives up an resorts to rubbing her ass up and down along the length of your penis."
            elif the_girl.obedience > 130:
                "[the_girl.possessive_title] blushes. The conflict of the dirtiness of the act of anal sex and her obedience to you are clear in her face."
                the_girl "Sir... don't you find my ass pleasing? Why did you pull out?"
                mc.name "Dont worry, [the_girl.title], I'll fuck your ass some more in a second, I just needed to take a moment and how loose your backdoor has gotten so far."
                $ the_girl.change_slut(2)
                "[the_girl.possessive_title]'s cheeks turn even redder with your dirty talk. She puts her head down again, but leaves her cheeks spread, ready for you to resume fucking her whenever you are ready."
            else:
                the_girl "Hey, why'd you pull out? I was just getting used to how thick you are..."
            "After taking a moment appraising [the_girl.possessive_title!l]'s buttocks, you decide to get back to the act."
            "With gentle pressure, you slowly fill her ass with your erection again. [the_girl.possessive_title] groans as you resume your thrusting."
        "Shove it in deep":
            "You decide with her cheeks spread wide to see how deep you can get yourself into [the_girl.possessive_title!l]. "
            "With her hands busy, she has no way of holding up your weight as you push yourself forward and then down on top of her, your full body weight pushing her prone down onto the [the_object.name]."
            "[the_girl.possessive_title] whimpers, her body now pinned between your body and [the_object.name]."
            if the_girl.has_role(anal_fetish_role):
                "Despite having no leverage, [the_girl.possessive_title!l] wriggles her ass against you as best she can. Even with no room to move, her love for anal sex drives her to try to milk your cock."
                "You enjoy her efforts before you speak clearly to her."
                mc.name "Does this feel better than that plug? Is this what you're imagining everytime you push that plug up your ass?"
                "[the_girl.possessive_title] is writhing in pleasure, having her fetish of anal sex fulfilled."
                the_girl "Oh god it is. Everytime I play with my ass and all I can think about is your big meaty dick buried inside me."
                "You grab her hair at the base of her scalp and pull her head back before whispering into her ear."
                mc.name "Don't worry, slut. This won't be the last time I fill your ass with my cock."
                "You can see goosebumps all over [the_girl.possessive_title!l]'s skin. She moans and then begs you to keep fucking her."
            elif the_girl.get_opinion_score("anal creampies") > 0:
                the_girl "Holy hell that is deep... tell me... tell me you'll push it this deep again when you cum... that would be so hot!"
                $mc.change_arousal(5)
                "In your mind, you play out the fantasy of cumming so deep in [the_girl.possessive_title!l]'s ass, even when you pull out not a drop of your seed leaks out."
                "You give the idea serious consideration. You can tell she would love it if you did."
            elif the_girl.get_opinion_score("anal sex") > 0:
                "Despite having no leverage, [the_girl.possessive_title!l] wriggles her ass against you as best she can. Even with no room to move, her love for anal sex drives her to milk your cock."
                "You lower your face down behind her head and whisper into her ear."
                mc.name "Mmm, so rear entry is how you like it, slut? Don't worry, this won't be the last time you feel my cock ravage your back door."
                "You can see goosebumps all over [the_girl.possessive_title!l]'s skin. You wonder how many times you can make her cum before you blow your load."
                $ the_girl.change_slut(2)
            elif the_girl.sluttiness > 100:
                the_girl "Oh fuck, bury it in me [the_girl.mc_title]! I don't think I've ever felt so full..."
            else:
                "[the_girl.possessive_title] lets out a loud groan. You can tell she isn't used to being penetrated like this, but she is taking it as best she can."
                the_girl "God [the_girl.mc_title] that is so intense... please just try to be a little more gentle okay?"
            "You take a few seconds to enjoy being engulfed by her back passage, then give her a few slow, probing thrusts."
            "After a minute or two slow, deep thrusts you decide to move back to doggy. You push yourself up off of [the_girl.possessive_title!l]'s back, and she follows, getting on all fours again to resume your fucking."

    return

label transition_default_doggy_anal_enhanced(the_girl, the_location, the_object):
    "[the_girl.title] gets on her hands and knees as you kneel behind her. You bounce your hard shaft on her ass a couple of times before lining yourself up with tight asshole."
    mc.name "Ready?"
    the_girl "I... I think so."
    "You hold onto her hips and push forward, spreading her ass with your large cock. She gasps and balls her fists, until finally you've buried your shaft in her."
    "After giving her a second to acclimatize you start to thrust in and out, slowly at first but picking up speed."
    return

# slightly modified dialog for when going the other way (she doesn't need to get on her hand and knees anymore)
label transition_anal_doggy_to_doggy_taboo_break_label(the_girl, the_location, the_object):
    the_girl "Are you enjoying pounding my tight asshole?"
    "You slide your cock out of her ass and drag it down between her legs, ending with your tip resting against her pussy."
    mc.name "No, this is what I really want."
    $ the_girl.call_dialogue(doggy.associated_taboo+"_taboo_break")
    "You hold onto [the_girl.title]'s hips with one hand and your cock with the other, guiding it as you push forward."
    "After a moment of resistance your cock spreads her [the_girl.pubes_description] pussy open and you slide smoothly inside of her."
    if the_girl.sex_skills["Vaginal"] > 2:
        the_girl "Oh god yes.... keep sliding that monster into me...."
        "You ram your whole length into her wet pussy and start pounding her."
    else:
        the_girl "Oh god... take it slow... "
        "You give her short thrusts, each time going a little bit deeper. Soon you're working your full length in and out of her wet hole."
    return
