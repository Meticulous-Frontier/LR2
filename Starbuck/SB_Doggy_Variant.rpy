init:
    python:
        SB_doggy_anal = Position("Doggy Anal",80,100,"doggy","Lay","Vagina","Anal",15,18,[],
        "intro_SB_doggy_anal",
        ["scene_SB_doggy_anal_1","scene_SB_doggy_anal_2"],
        "outro_SB_doggy_anal",
        "transition_default_SB_doggy_anal",
        "strip_SB_doggy_anal", "strip_ask_SB_doggy_anal",
        "orgasm_SB_doggy_anal",
        opinion_tags = ["doggy style sex" "anal sex"])
        #list_of_positions.append(SB_doggy_anal)

init 1:
    python:
        SB_doggy_anal.link_positions_two_way(doggy, "transition_SB_doggy_anal_doggy", "transition_doggy_SB_doggy_anal")

label intro_SB_doggy_anal(the_person, the_location, the_object, the_round):
    mc.name "[the_person.title], I want you to get on your hands and knees for me. I want to fuck your ass today."
    if the_person.effective_sluttiness() > 110:
        the_person.char "Oh god I love it when you do this to me..."
    elif the_person.effective_sluttiness() > 80:
        the_person.char "Ok, just be careful [the_person.mc_title]..."
    else:
        the_person.char "I don't know, are you sure that thing is gonna fit in me back there?"
    "[the_person.possessive_title] gets onto all fours in front of you on the [the_object.name]. She arches her back and presents her ass."
    if the_person.arousal > 60:
        "You rub the tip of your penis against [the_person.possessive_title]'s cunt, feeling how nice and wet she is already. You rub your lubricated penis against her ass to help prepare her for your initial penetration."
        "You rub your dick against her pussy again and gather more of her juices. She is already so wet you are soon slick with her secretions"
    else:
        "You line yourself up with her ass, but the lack of lubricant makes it impossible to push it in. You pull on her hair to bring her head back around to face you."
        "You put your other hand in front of her face and she quickly opens her mouth and sucks on them. [the_person.possessive_title] slobbers all over your fingers for a few a seconds before you pull them out with a loud pop"
        "You use your fingers to crudely work in and out of her ass a few times to help get it lubricated."
        "Deciding against making her suck on your fingers again after they've been in her ass, you spit a couple times down on her ass to get a bit more lubrication so you can penetrate her"
    "When you're ready you slowly push forward. It takes several seconds of steady pressure until you finally bottom out."
    if SB_get_fetish(the_person) == "Anal Fetish":
        the_person.char "Oh my god it's so dirty... but it is so good too..."
        $ the_person.discover_opinion("anal sex")
    return

label scene_SB_doggy_anal_1(the_person, the_location, the_object, the_round):
    "You give [the_person.possessive_title]'s ass a good hard spank. She lets out a loud yelp"
    $ the_person.call_dialogue("sex_responses")
    if the_person.sex_skills["Anal"] < 2: #Inexperienced
        "[the_person.possessive_title] reflexively starts to pull away after you spank her. You grab her hips to keep her from pulling off completely."
        the_person.char "Sorry, I just... I don't do this very often... please just be gentle with me!"
        "You pull her hips back toward you slowly. Her inexperienced ass yields to your penis and she sighs as you bottom out"
        "You decide to give her a little break in the intensity of your fucking. Leaving yourself deep inside her, you kneed her ass cheeks with both hands."
        the_person.char "mmm, that feels good [the_person.mc_title]. Can I touch myself while you do that?"
        menu:
            "Masturbate for me":
                 "Encouraged by your response, [the_person.possessive_title] reaches down with one hand and begins to rub her clit."
                 "You take it slow, and you revel in the delicious pleasure of each penetration as you thrust. [the_person.possessive_title] struggles to hold herself up with one hand while the other works circles around her clit"
                 if the_person.get_opinion_score("masturbating") > 0:
                     "[the_person.possessive_title] moves her fingers masterfully across her pussy. You can tell she masturbates often."
                     $ the_person.discover_opinion("masturbating")
                     $ the_person.change_arousal(the_person.get_opinion_score("masturbating" * 5))
                 if the_person.sluttiness > 100:
                     the_person.char "I'm sorry [the_person.mc_title], I'll try to get better at this. Having you in my ass is so intense..."
                 else:
                     "[the_person.possessive_title] seems to be enjoying the anal penetration a bit more now that she is touching herself"
            "Fuck me with your ass":
                 if the_person.obedience > 130 or the_person.get_opinion_score("being submissive") > 0:
                     the_person.char "Yes sir. I'll do my best"
                 else:
                     the_person.char "I'll give it my best, but this better be worth it..."
                 "[the_person.possessive_title] slowly eases forward until just the tip remains inside, then slowly backs her ass back onto you. She is trying to obey but you can tell she is struggling to take you"
                 "The next she starts to ease forward, you put your hand on her hips for a second to stop her. You spit into your hand then rub it along your shaft a bit, hoping it will make the penetration easier"
                 the_person.char "Mmm, that's a bit better..."
                 "With the extra lube, [the_person.possessive_title] resumes fucking you. She still has a fairy slow pace, but is a bit quicker than before."

    else:
        "In response to your spanking, [the_person.possessive_title] thrusts herself back against you. Your penis is completely consumed by her bowel and she moans lewdly."
        "When she starts to pull off you give her other ass check a hard swat. She buries her face in [the_object.name] and moans as she pushes herself back onto you again."
        the_person.char "Oh fuck [the_person.mc_title], I needed this so bad. Don't stop, it feels so good when you go deep!"
        "[the_person.possessive_title]'s ass feels so tight you are tempted to let her continue setting the pace, but you worry she might get the wrong idea if you let this little slut take charge."
        menu:
            "Fuck me with your ass":
                 "You decide to see what [the_person.possessive_title] can do if you let her take control of the pace. Encouraged by your words, she eagerly works your cock with her ass" ###FINISH
                 the_person.char "Mmm, does it feel good when I work it like this?"
                 "[the_person.possessive_title] begins to twerk up and down your shaft with quick, shallow movements."
                 if mc.arousal > 70:
                      mc.name "Damn that feels good. You're gonna make me cum if you keep that up. Where do you want my load?"
                      if SB_get_fetish(the_person) == "Internal Cum Fetish":
                          the_person.char "Just shove it in deep and dump it right in my ass. You know I need your cum inside me, right where it belonds!"
                      elif SB_get_fetish(the_person) == "External Cum Fetish":
                         the_person.char "Anywhere on my skin! My ass, my face, I don't care, just spray me down with it! With you know I need it like that!"
                      elif the_person.get_opinion_score("creampies") > 0:
                           the_person.char "You should just shove it in as deep as you can and cum inside me."
                      elif the_person.get_opinion_score("being covered in cum") > 0:
                           the_person.char "You should pull out and cum all over my ass. That would be so hot..."
                      elif the_person.get_opinion_score("cum facials") > 0:
                           the_person.char "Tell me when you are about to cum and I'll let you cum all over my face..."
                      elif the_person.obedience > 130:
                           the_person.char "Cum wherever you want to... I just want to please you sir"
                      else:
                           the_person.char "I don't know... wherever you want I guess?"
                 else:
                      mc.name "Wow, your ass is amazing. Where'd you learn to work it like that girl? Have you been practicing?"
                      if SB_get_fetish(the_person) == "Anal Fetish":
                           "In response, she slams her ass all the way back on your dick. She grinds her hips left and right up against you."
                           the_person.char "Practicing, dreaming, begging for your cock in my ass! Every moment my rear is empty I'm craving your dick deep inside it."
                           "You can feel her tense and relax her muscles in her ass rhythmically, messaging your shaft while you remain totally engulfed inside her."
                           mc.name "Fuck [the_person.title], I dont't know how you do that, but its amazing."
                           "[the_person.possessive_title] sighs. She is truly addicted to getting her tight back passage fucked"
                      elif the_person.get_opinion_score("anal sex") > 0:
                           "In response, she slams her ass all the way back on your dick. She grinds her hips left and right up against you."
                           "You can feel her tense and relax her muscles in her ass rhythmically, messaging your shaft while you remain totally engulfed inside her."
                           mc.name "Wow, I guess so! That feels amazing. Feel free to practice anytime you want on me, [the_person.title]!"
                           "[the_person.possessive_title] sighs. You can tell having your dick in her ass is very fulfilling for her."
                      else:
                           "[the_person.possessive_title] looks back at you."
                           the_person.char "Honestly, I'm not usually into butt stuff... but I just want to make you feel so good..."
                 "[the_person.possessive_title] continues to twerk her ass up and down on your penis. How does she make it look so easy?"
            "I'm in charge here":
                 "Sensing that your slut is getting out of hand, you quickly take charge. You grab her by the hair and pull her head back until her hands are no longer on the ground, taking away all her leverage."
                 $ the_person.call_dialogue("suprised_exclaim")
                 "You lean forward and whisper into [the_person.possessive_title]'s ear."
                 mc.name "I know you dream about my dick in your ass constantly and it feels good to finally have that dream come true, but don't forget who is in charge around here."
                 if the_person.obedience > 130 or the_person.get_opinion_score("being submissive") > 0:
                     $ the_person.discover_opinion("being submissive")
                     if the_person.get_opinion_score("being submissive") > 0:
                         $ the_person.change_arousal(the_person.get_opinion_score("being submissive" * 5))
                         "For once, [the_person.possessive_title] is speechless. She can only whimper softly in total submission to you."
                     else:
                         the_person.char "I'm sorry [the_person.mc_title], I couldn't help myself. Please use me however you want, I'll be good I promise!"
                     "You give her a couple slow, heavy thrusts before releasing her hair. She returns her hands to the ground and moans when you resume your slow, methodical fucking."
                 else :
                     the_person.char "Okay! Geesh! Be careful with my hair, that hurts!"
                #TODO this option is kinda boring... expand some?

    return


label scene_SB_doggy_anal_2(the_person, the_location, the_object, the_round):
    "[the_person.possessive_title] lowers her shoulders against the [the_object.name] and groans as you fuck her from behind."
    the_person.char "Ah... I feel so full!"
    "You reach forward and place your hands on [the_person.possessive_title]'s shoulders. With each thrust you pull her back onto you forcefully, your hips smacking her ass cheeks loudly. She arches her back and lets out a series of satisfied yelps."
    $the_person.call_dialogue("sex_responses")
    if the_person.arousal > 80:
        "[the_person.possessive_title]'s pussy is dripping wet. A damp spot has begun to accumulate below her pussy as a result of your rutting."
        the_person.char "Ohhh, you feel so fucking good in my ass."
    else:
        "[the_person.possessive_title] seems to be enjoying the fucking you are giving her. She yelps in response to one particularly eager thrust."
        the_person.char "God dammit, you're so fucking big. You feel huge in my ass."
    if the_person.get_opinion_score("giving handjobs") > 0:
        "[the_person.possessive_title] reaches down and begins to stroke and rub your scrotum with one hand, while with the other hand she reaches back and pulls her ass cheeks apart."
        $ the_person.change_arousal(the_person.get_opinion_score("giving handjobs" * 2))
    elif the_person.get_opinion_score("masturbating") > 0:
        "You notice that[the_person.possessive_title] now has one hand on her pussy, rubbing her clit, and with the other hand she reaches back and pulls her ass cheeks apart."
        $ the_person.change_arousal(the_person.get_opinion_score("masturbating" * 3))
    else:
        "[the_person.possessive_title] reaches back with both hands and spreads her ass cheeks apart."
    "With her ass cheeks spread, you consider for a moment, should you pull back and admire the view, or shove yourself down deep?"
    menu:
            "Admire her ass":
                "You pull yourself out of [the_person.possessive_title]'s ass for moment and admire the soft, round cheeks of carnal pleasure in front of you."
                "Her asshole gapes a bit from your sudden pullout, and she quickly turns her head to see why she suddenly feels so empty."
                "[the_person.possessive_title] realizes you are taking a moment to check out her backside."
                if the_person.get_opinion_score("showing her ass"):
                    the_person.char "Do you like my ass, [the_person.mc_title]? I've caught you checking it out before. It gets me so hot when I feel your eyes checking out my backside..."
                    $ the_person.change_arousal(the_person.get_opinion_score("showing her ass" * 5))###
                    $ the_person.discover_opinion("showing her ass")
                    "[the_person.possessive_title] moves her ass side to side, gyrating her hips for you while keeping her ass cheeks spread wide."
                elif the_person.get_opinion_score("being covered in cum"):
                    the_person.char "Do you like what you see, [the_person.mc_title]? I bet it is going to look even more amazing covered in your hot cum"
                    $mc.change_arousal(5)
                    "The thought of painting [the_person.possessive_title]'s ass with your semen makes your cock twitch in anticipation."
                elif the_person.sluttiness > 100:
                    the_person.char "Hey, you can check my ass out later, right now you're supposed to be fucking it, [the_person.mc_title]!"
                    "[the_person.possessive_title] tries to push herself back on to you, but from her angle she is unable to get you to penetrate her again unless you help."
                    "She quickly gives up an resorts to rubbing her ass up and down along the length of your penis."
                elif the_person.obedience > 130:
                    "[the_person.possessive_title] blushes. The conflict of the dirtiness of the act of anal sex and her obedience to you are clear in her face."
                    the_person.char "Sir... don't you find my ass pleasing? Why did you pull out?"
                    mc.name "Dont worry, [the_person.title], I'll fuck your ass some more in a second, I just needed to take a moment and how loose your backdoor has gotten so far."
                    $ the_person.change_slut_temp(2)
                    "[the_person.possessive_title]'s cheeks turn even redder with your dirty talk. She puts her head down again, but leaves her cheeks spread, ready for you to resume fucking her whenever you are ready."
                else:
                    the_person.char "Hey, why'd you pull out? I was just getting used to how thick you are..."
                "After taking a moment appraising [the_person.possessive_title]'s buttocks, you decide to get back to the act"
                "With gentle pressure, you slowly fill her ass with your erection again. [the_person.possessive_title] groans as you resume your thrusting"
            "Shove it in deep":
                "You decide with her cheeks spread wide to see how deep you can get yourself into [the_person.possessive_title]. "
                "With her hands busy, she has no way of holding up your weight as you push yourself forward and then down on top of her, your full body weight pushing her prone down onto the [the_object.name]"
                "[the_person.possessive_title] whimpers, her body now pinned between your body and [the_object.name]"
                if SB_get_fetish(the_person) == "Anal Fetish":
                    "Despite having no leverage, [the_person.possessive_title] wriggles her ass against you as best as she can. Even with no room to move, her love for anal sex drives her to try to milk your cock"
                    "You enjoy her efforts before you speak clearly to her."
                    mc.name "Does this feel better than that plug? Is this what you're imagining everytime you push that plug up your ass?"
                    "[the_person.possessive_title] is writhing in pleasure, having her fetish of anal sex fulfilled."
                    the_person.char "Oh god it is. Everytime I play with my ass and all I can think about is your big meaty dick buried inside me."
                    "You grab her hair at the base of her scalp and pull her head back before whispering into her ear."
                    mc.name "Don't worry, slut. This won't be the last time I fill your ass with my cock."
                    "You can see goosebumps all over [the_person.possessive_title]'s skin. She moans and then begs you to keep fucking her."
                elif the_person.get_opinion_score("creampies") > 0:
                    the_person.char "Holy hell that is deep... tell me... tell me you'll push it this deep again when you cum... that would be so hot!"
                    $mc.change_arousal(5)
                    "In your mind, you play out the fantasy of cumming so deep in [the_person.possessive_title]'s ass, even when you pull out not a drop of your seed leaks out."
                    "You give the idea serious consideration. You can tell she would love it if you did."
                elif the_person.get_opinion_score("anal sex") > 0:
                    "Despite having no leverage, [the_person.possessive_title] wriggles her ass against you as best as she can. Even with no room to move, her love for anal sex drives her to milk your cock"
                    "You lower your face down behind her head and whisper into her ear."
                    mc.name "Mmm, is rear entry is how you like it, slut? Don't worry, this won't be the last time you feel my cock ravage your back door."
                    "You can see goosebumps all over [the_person.possessive_title]'s skin. You wonder how many times you can make her cum before you blow your load."
                    $ the_person.change_slut_temp(2)
                elif the_person.sluttiness > 100:
                    the_person.char "Oh fuck, bury it in me [the_person.mc_title]! I don't think I've ever felt so full..."
                else:
                    "[the_person.possessive_title] lets out a loud groan. You can tell she isn't used to being penetrated like this, but she is taking it as best as she can."
                    the_person.char "God [the_person.mc_title] that is so intense... please just try to be a little more gentle okay?"
                "You take a few seconds to enjoy being engulfed by her back passage, then give her a few slow, probing thrusts."
                "After a minute or two slow, deep thrusts you decide to move back to doggy. You push yourself up off of [the_person.possessive_title]'s back, and she follows, getting on all fours again to resume your fucking."

    return


label scene_SB_doggy_anal_3(the_person, the_location, the_object, the_round):
    "third scene here"





    return

label outro_SB_doggy_anal(the_person, the_location, the_object, the_round):
    "[the_person.possessive_title]'s tight ass draws you closer to your orgasm with each thrust. You finally pass the point of no return and speed up, fucking her as hard as you can manage."
    $the_person.call_dialogue("sex_responses")
    mc.name "Ah, I'm going to cum!"
    menu:
        "Cum inside of her.":
            "You pull back on [the_person.possessive_title]'s hips and drive your cock deep inside of her as you cum. She gasps softly in time with each new shot of hot semen inside of her."
            if the_person.get_opinion_score("creampies") > 0:
                the_person.char "Yes! Fill my ass with your cum!"
            $ cum_in_ass(the_person)
            $ SB_doggy_anal.redraw_scene(the_person)
            if SB_get_fetish(the_person) == "Internal Cum Fetish":
                "[the_person.possessive_title]'s body goes rigid as your cum poors into her ass. Goosebumps erupt all over her body as her brain registers her creampie."
                the_person.char "Oh.. OH! Yes [the_person.mc_title]! Pump it deep! You were meant to cum inside me!"
                "[the_person.possessive_title] revels in having her cum fetish fulfilled."
            if the_person.sluttiness > 110:
                the_person.char "Oh god it's so good. It doesn't matter which hole you do it in, I love it when you cum inside me."
            else:
                the_person.char "Oh fuck, I can't believe I let you cum in my ass..."

            "You wait until your orgasm has passed completely, then pull out and sit back. Her asshole gapes slightly and you can see a hint of your cum start to dribble out, but most of it stays buried with her bowel"

        "Cum on her ass.":
            "You pull out of [the_person.possessive_title] at the last moment, stroking your shaft as you blow your load over her ass. She holds still for you as you cover her with your sperm."
            if the_person.get_opinion_score("being covered in cum") > 0:
                 the_person.char "Yes! Paint me with your sticky cum!"
            $ the_person.cum_on_ass()
            $ SB_doggy_anal.redraw_scene(the_person)
            if SB_get_fetish(the_person) == "External Cum Fetish":
                "[the_person.possessive_title]'s body goes rigid as your cum coats her ass. Goosebumps erupt all over her body as her brain registers your cum on her skin."
                "[the_person.possessive_title] revels in bliss as your dick sprays jet after jet of seed across her ass. She moans lewdly."
                "She truly is addicted to your cum."
            elif the_person.sluttiness > 120:
                the_person.char "Oh god your seed is so hot! Does it look sexy, having it plastered all over my ass?"
                "She reaches back and runs a finger through the puddles of cum you've put on her, then licks her finger clean."
            else:
                the_person.char "Oh! Its so warm..."
            "You sit back and sigh contentedly, enjoying the sight of [the_person.possessive_title]'s ass covered in your semen."
        "Cum on her face.":
            mc.name "Fuck, get ready [the_person.title], I wanna cum on your face!"
            "You pull your cock out of [the_person.possessive_title]'s ass with a satisfying pop. She immediately turns around on gets on her knees in front of you."
            $ the_person.draw_person(position = "blowjob")
            if SB_get_fetish(the_person) == "External Cum Fetish":
                "[the_person.possessive_title] reaches up and begins stroking you off for your final few seconds."
                "Your orgasm hits hard. Your first jet sprays across her face."
                "You can see [the_person.possessive_title]'s pupils dilate as you fulfil her cum fetish."
                "[the_person.possessive_title] revels in bliss as your dick sprays jet after jet of seed across her face. She moans lewdly."
                "She truly is addicted to your cum."
            if the_person.sluttiness > 80:
                "[the_person.possessive_title] sticks out her tongue for you and holds still, eager to take your hot load."
                $ the_person.cum_on_face()
                $ the_person.draw_person(position = "blowjob")
                "You let out a shudder moaning as you cum, pumping your sperm onto [the_person.possessive_title]'s face and into her open mouth. She makes sure to wait until you're completely finished."
                the_person.char "Oh god... it feels so good on my skin..."
            elif the_person.sluttiness > 60:
                "[the_person.possessive_title] closes her eyes and waits patiently for you to cum."
                $ the_person.cum_on_face()
                $ the_person.draw_person(position = "blowjob")
                "You let out a shudder moaning as you cum, pumping your sperm onto [the_person.possessive_title]'s face. She waits until she's sure you're finished, then opens one eye and looks up at you."
            else:
                "[the_person.possessive_title] closes her eyes and turns away, presenting her cheek to you as you finally climax."
                $ the_person.cum_on_face()
                $ the_person.draw_person(position = "blowjob")
                "You let out a shudder moaning as you cum, pumping your sperm onto [the_person.possessive_title]'s face. She flinches as the first splash of warm liquid lands on her cheek, but doesn't pull away entirely."
            "You take a deep breath to steady yourself once you've finised orgasming. [the_person.possessive_title] looks up at you from her knees, face covered in your semen."
            $ the_person.call_dialogue("cum_face")


    return

label transition_SB_doggy_anal_doggy(the_person, the_location, the_object, the_round):
    "You decide to give [the_person.possessive_title] a break. She murmurs a bit in disappointment when you slowly pull your dick out of her ass completely."
    "You bounce your hard shaft on her ass a couple of times before lining yourself up with her pussy."
    the_person.char "Wait, are you sure its okay to stick in there after its been in my ass?"
    "You ignore her question and push forward, slipping your shaft deep inside of [the_person.possessive_title]'s cunt. She gasps and quivers ever so slightly as you start to pump in and out."
    return

label transition_doggy_SB_doggy_anal(the_person, the_location, the_object, the_round):
    "You stop your thrusting for a moment and she looks back at you. You put two fingers in front of her mouth, and after a moment she takes them in her mouth and starts to suck on them"
    "[the_person.possessive_title] slobbers all over your fingers for a few a seconds before you pull them out with a loud pop"
    "You use your fingers to crudely work in and out of her ass a few times to help get it lubricated. [the_person.possessive_title] moans at the feeling of your penis in one hole and your fingers in another"
    mc.name "Are you ready for me, [the_person.title]? I'm going to stick it in your ass now"
    the_person.char "Take me however you want, [the_person.mc_title], just be careful with me!"
    "When you're ready you slowly push forward. It takes several seconds of steady pressure until you finally bottom out."
    if the_person.get_opinion_score("anal sex") > 0 :
        the_person.char "Oh my god it's so dirty... but it is so good too..."
        $ the_person.discover_opinion("anal sex")
    return

label transition_default_SB_doggy_anal(the_person, the_location, the_object, the_round):
    "[the_person.possessive_title] gets on her hands and knees as you kneel behind her. You bounce your hard shaft on her ass a couple of times before lining yourself up with her sphincter."
    "Once you're both ready you push yourself forward, slipping your hard shaft deep inside of her. She lets out a gasp under her breath."
    return

label strip_SB_doggy_anal(the_person, the_clothing, the_location, the_object, the_round):
    "[the_person.possessive_title] leans forward a little further and pops off your cock."
    $ the_person.call_dialogue("sex_strip")
    $ the_person.draw_animated_removal(the_clothing, position = doggy.position_tag)
    "[the_person.possessive_title] struggles out of her [the_clothing.name] and throws it to the side. Then she gets herself lined up in front of you again."
    "She groans happily when you push back inside of her."
    return

label strip_ask_SB_doggy_anal(the_person, the_clothing, the_location, the_object, the_round):
    the_person.char "Sir, I'd like to take off my [the_clothing.name], would you mind?"
    "[the_person.char] pants as you fuck her from behind."
    menu:
        "Let her strip.":
            mc.name "Take it off for me."
            $ the_person.draw_animated_removal(the_clothing, position = doggy.position_tag)
            "[the_person.possessive_title] struggles out of her [the_clothing.name] and throws it to the side. Then she gets herself lined up in front of you again."
            "She groans happily when you push back inside of her."

        "Leave it on.":
            mc.name "No, I like how you look with it on."
            if the_person.sluttiness < 80:
                the_person.char "Do you think I look sexy in it?"
                "You speed up, fucking her faster in response to her question."
            elif the_person.sluttiness < 100:
                the_person.char "Does it make me look like a good little slut? All I want to be is your good little slut sir."
                "She pushes her hips back into you and moans happily."
            else:
                the_person.char "Does it make me look like the cum hungry slut that I am? That's all I want to be for you sir, your dirty little cum dumpster!"
                "She grinds her hips back into you and moans ecstatically."
    return

label orgasm_SB_doggy_anal(the_person, the_location, the_object, the_round):
    "[the_person.possessive_title]'s tight back passage starts to quiver, and suddenly tenses up."
    $ the_person.call_dialogue("climax_responses")
    "You bury your cock in deep in [the_person.possessive_title]'s ass while she cums. Her bowel grips you tightly."
    "After a couple of seconds [the_person.possessive_title] sighs and the tension drains from her body."
    if the_person.get_opinion_score("anal sex") < 0:
        the_person.char "I can't believe that just happened... oh god now you're going to keep going, aren't you?"
    else:
        the_person.char "Don't stop... it still feels so good!"
    return
