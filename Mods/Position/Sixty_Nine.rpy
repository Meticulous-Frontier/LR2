#SB_Sixty_Nine.rpy

#This position is to help flesh out oral options in the game to prepare for the oral fetish.

init python:
    SB_sixty_nine = Position(name = "Sixty-Nine", slut_requirement = 45, slut_cap = 65, requires_hard = True, requires_large_tits = False,
        position_tag = "doggy", requires_location = "Lay", requires_clothing = "Vagina", skill_tag = "Oral",
        girl_arousal = 15, girl_energy = 10,
        guy_arousal = 15, guy_energy = 10,
        connections = [],
        intro = "intro_SB_sixty_nine",
        scenes = ["scene_SB_sixty_nine_1","scene_SB_sixty_nine_2"],
        outro = "outro_SB_sixty_nine",
        transition_default = "transition_default_SB_sixty_nine",
        strip_description = "strip_SB_sixty_nine", strip_ask_description = "strip_ask_SB_sixty_nine",
        orgasm_description = "orgasm_SB_sixty_nine",
        taboo_break_description = "taboo_break_SB_sixty_nine",
        verb = "sixty-nine",
        verbing = "sixty-nining",
        opinion_tags = ["giving blowjobs", "getting head"], record_class = "Cunnilingus",
        associated_taboo = "sucking_cock")

        # only one associated taboo is allowed in code ["sucking_cock", "licking_pussy", "touching_penis", "touching_vagina"]

    list_of_positions.append(SB_sixty_nine)

#init 1:
    #python:
        #SB_sixty_nine.link_positions(deepthroat,"transition_SB_sixty_nine_deepthroat")

label intro_SB_sixty_nine(the_girl, the_location, the_object):
    "You give her ass a good hard smack and then look at [the_girl.possessive_title]."
    mc.name "Hey, wanna sixty nine?"
    if the_girl.has_role(oral_fetish_role):
        "[the_girl.possessive_title] smiles wide and quickly responds."
        the_girl.char "That sounds amazing! Sixty nine has to be the absolute best position... I can't wait to taste you!"
    if the_girl.effective_sluttiness() > 45:
        "[the_girl.possessive_title] smiles and responds."
        the_girl.char "That sounds like fun! Let's do it!"
    else:
        "[the_girl.possessive_title] hesitates for a moment before responding."
        the_girl.char "I guess we could do that. But I'm on top!"
    "You lay down on the [the_object.name]. [the_girl.possessive_title] swings one leg over you, presenting her pussy to your face. You waste no time and start to flick your tongue around her slit."
    if the_girl.get_opinion_score("getting head") > 2 :
        the_girl.char "Oh! Yes that feels so good already! Oh [the_girl.mc_title] your tongue feels amazing."
    if the_girl.get_opinion_score("giving blowjobs") > 2:
        the_girl.char "Mmm, that feels good [the_girl.mc_title]... and your cock... it looks so good... I wanna swallow it whole!"
    if mc.condom:
        the_girl.char "Why are you wearing this thing? Lets take this off so I can take care of you better..."
        "[the_girl.possessive_title] pulls off your condom."
        $ mc.condom = False
    "[the_girl.possessive_title] begins to please you in return. Taking you into her mouth, she begins sucking you off."
    #$ SB_sixty_nine.redraw_scene(the_girl)
    return

label scene_SB_sixty_nine_1(the_girl, the_location, the_object):
    $ SB_sixty_nine.redraw_scene(the_girl)
    if the_girl.sex_skills["Oral"] < 2: #Inexperienced.
        "You rest your hands on [the_girl.possessive_title]'s ass as she bobs her head up and down. She struggles to take your very deep, so she focuses on licking and sucking your tip."
        "You circle her clit a few times with your tongue. You suck it into your mouth roughly a couple of times and then release it, you lips making a wet, lewd smackin noise"
        menu:
            "Focus on her" if mc.sex_skills["Oral"] > 2:
                "After a few teasing licks, you bury your face in her pussy. You make a few swiping licks across her clit and the lap up some of the juices flowing from her nethers."
                "[the_girl.possessive_title] is overwhelmed by the sensations and momentarily pulls off your dick."
                the_girl.char "Mmm! God [the_girl.mc_title] that feels so good..."
                $ the_girl.change_arousal(5)
                if the_girl.get_opinion_score("giving blowjobs") < 0:
                    $ the_girl.discover_opinion("giving blowjobs")
                    "[the_girl.possessive_title] looks down at your cock and hesitates."
                    the_girl.char "I'm sorry I don't... that I'm not as good at sucking you as you are at kissing me..."
                    mc.name "Give it time, you'll get use to it."
                else:
                    "[the_girl.possessive_title] slips you back into her soft mouth. She tries to take you a little deeper, but gags a bit and has to pull back off."
                    the_girl.char "I'm sorry that I'm not at good at sucking you as you are at kissing me..."
                    "You pause your licking to give her some encouragement."
                    mc.name "Don't worry, you just need more practice."
                "You knead her ass cheeks with your hands a few times, then spread her cheeks apart and continue to eat her out."
            "Focus on her\n{color=#ff0000}{size=18}Requires Oral Skill{/size}{/color} (disabled)" if mc.sex_skills["Oral"] < 3:
                    pass
            "Focus on you":
                "You pause your licking to give her some encouragement."
                mc.name "It's okay you can't go deep. Use your hands a little!"
                if the_girl.sex_skills["Foreplay"] < 2:
                    "[the_girl.possessive_title] wraps one hand around the base of your cock. She tries to stroke you in time with her mouth, but she is gripping you way too hard"
                    mc.name "Easy girl! Don't grip so hard!"
                    the_girl.char "Sorry! I'm just not very good at this I guess."
                    "[the_girl.possessive_title] keeps stroking you, this time you can barely feel it. You sigh and decide to just keep eating her out while she does her thing."
                else:
                    "[the_girl.possessive_title] wraps her right hand around the base of your cock and starts to slide it back and forth in time with her sucking. Her other hand begins to lightly cup and knead your balls."
                    if (the_girl.get_opinion_score("cum facials") > 0 or the_girl.get_opinion_score("being covered in cum") > 0 ) and the_girl.sluttiness > 40:
                        "After a moment she takes her lips off your dick and continues stroking you."
                        the_girl.char "Mmm, I can't wait to feel your hot cum all over my face..."
                        "She strokes you off faster and holds your cock right against her face."
                        the_girl.char "When I'm on top of you like this, I can point it wherever I want! Cover my face with it!"
                        $ the_girl.discover_opinion("cum facials")
                        $ the_girl.discover_opinion("being covered in cum")
                        $ the_girl.change_arousal(5)
                        "You give [the_girl.possessive_title]'s ass a hard smack and resume eating her pussy."
                        "[the_girl.possessive_title]'s cunt quivers as she slides your cock back into her mouth, sucking at it with renewed vigor."
                    elif the_girl.get_opinion_score("drinking cum") > 0 and the_girl.sluttiness > 40:
                        "After a moment she takes her lips off your dick and continues stroking you."
                        the_girl.char "Mmm, I can't wait to feel your cum sliding down my throat [the_girl.mc_title]."
                        "She latches back onto your cock, sucking at the tip eagerly before letting it slip out again."
                        the_girl.char "I want you to flood my mouth with your cum. Ugh, I want it so badly!"
                        $ the_girl.discover_opinion("drinking cum")
                        $ the_girl.change_arousal(5)
                        "[the_girl.possessive_title]'s cunt quivers as she slides your cock back into her mouth, sucking at it with renewed vigor."
                    else:
                        "You lap at [the_girl.possessive_title]'s pussy leisurely while she services your cock, stroking your shaft and sucking gently on your tip."



    elif the_girl.sex_skills["Oral"] < 6: #competent at oral
        "[the_girl.possessive_title] bobs her head up and down to slide your cock in and out. The feeling of her soft, warm mouth sends shivers up your spine."
        "You circle her clit a few times with your tongue. You suck it into your mouth roughly a couple of times and then release it, you lips making a wet, lewd smackin noise"
        menu:
            "Focus on her" if mc.sex_skills["Oral"] > 2:
                "After a few teasing licks, you bury your face in her pussy. You make a few swiping licks across her clit and the lap up some of the juices flowing from her nethers."
                "[the_girl.possessive_title] is overwhelmed by the sensations and momentarily pulls off your dick."
                the_girl.char "Mmm! God [the_girl.mc_title] that feels so good..."
                if the_girl.get_opinion_score("giving blowjobs") < 0:
                    $ the_girl.discover_opinion("giving blowjobs")
                    "[the_girl.possessive_title] looks down at your cock and hesitates. Then she slowly slides you back into her mouth and resumes stroking you with her pillowy soft lips."
                else:
                    $ the_girl.change_arousal(5)
                    "[the_girl.possessive_title] slips you back into her soft mouth. Her tongue swirls around you in large circles few a seconds and the resumes bobbing her head up and down."
                    "You pause your licking to give her some encouragement."
                    mc.name "That's it, [the_girl.title], suck my cock!"
                "You knead her ass cheeks with your hands a few times, then spread her cheeks apart and continue to eat her out."
            "Focus on her\n{color=#ff0000}{size=18}Requires Oral Skill{/size}{/color} (disabled)" if mc.sex_skills["Oral"] < 3:
                    pass
            "Focus on you":
                "You pause your licking to talk dirty to her."
                mc.name "Wow that feels good. Take it deep, slut!"
                if the_girl.get_opinion_score("taking control") > 0:
                    "[the_girl.possessive_title] pulls off you for a second and chuckles."
                    the_girl.char "[the_girl.mc_title]... I think you've forgotten who is on top!"
                    "[the_girl.possessive_title] pushes her pussy back up against your face and begins to grind herself on your face."
                    "You are caught unready. When you have a chance, you gasp a deep breath of air and begin to start licking her."
                    the_girl.char "Mmm, that's it [the_girl.mc_title]"
                    $ the_girl.change_arousal(5 * the_girl.get_opinion_score("taking control"))
                    "You eat her out for several seconds, as best as you can, while she grinds back against you. She moans lewdly and her pussy drips with excitement."
                    "Eventually she eases off your face, giving you a chance to catch your breath. She slowly lick you around the tip of your shaft a few times then resumes bobbing her head up and down on you."
                else:
                    "[the_girl.possessive_title] moans, the vibrations it causes around your shaft feels great."
                    "She tries to take your cock down her throat. She manages it comfortably for a second, but eventually she gags and starts to pull off."
                    if the_girl.get_opinion_score("being submissive"):
                        "SMACK"
                        "You give her ass a loud spank as she pulls off."
                        mc.name "Each time you gag I'm gonna spank you good, slut!"
                        "[the_girl.possessive_title] moans again at your rough treatment, and immediately starts to slide her mouth back down around your cock."
                        "After a moment she begins to gag again"
                        "SMACK"
                        "She retreats only a moment and goes deep again. Her gagging reflex kicks in almost immediately."
                        "SMACK"
                        "She moans loudly, the vibration feels amazing and she goes deep yet again. Her throat convulses around you."
                        "SMACK"
                        "She moans again, even louder, and you can see her pussy dripping with excitement."
                        "You begin to lap it up with your tongue and she goes deep on you again, her throat convulsing this time while she is still pushing down."
                        "It feels amazing, each time she goes deep on you and her throat spasms around you."
                        $ the_girl.change_arousal(5 * the_girl.get_opinion_score("being submissive"))
                        $ the_girl.discover_opinion("being submissive")
                        $ mc.change_arousal(5)

                    "[the_girl.possessive_title] wraps her right hand around the base of your cock and starts to slide it back and forth in time with her sucking. Her other hand begins to lightly cup and knead your balls."
                    if the_girl.has_role(cum_external_role):
                        "After a moment she takes her lips off your dick and continues stroking you."
                        the_girl.char "Mmm, I can't wait to feel your hot cum all over my face..."
                        "She strokes you off faster and holds your cock right against her face."
                        the_girl.char "When I'm on top of you like this, I can point it wherever I want! Cover my face with it!"
                        $ the_girl.discover_opinion("cum facials")
                        $ the_girl.discover_opinion("being covered in cum")
                        $ the_girl.change_arousal(5)
                        "You give [the_girl.possessive_title]'s ass a hard smack and resume eating her pussy."
                        "[the_girl.possessive_title]'s cunt quivers as she slides your cock back into her mouth, sucking at it with renewed vigor."
                    elif the_girl.has_role(cum_internal_role):
                        "After a moment she takes her lips off your dick and continues stroking you."
                        the_girl.char "Mmm, I can't wait to feel your cum sliding down my throat [the_girl.mc_title]."
                        "She latches back onto your cock, sucking at the tip eagerly before letting it slip out again."
                        the_girl.char "I want you to flood my mouth with your cum. Ugh, I want it so badly!"
                        $ the_girl.discover_opinion("drinking cum")
                        $ the_girl.change_arousal(5)
                        "[the_girl.possessive_title]'s cunt quivers as she slides your cock back into her mouth, sucking at it with renewed vigor."
                    elif (the_girl.get_opinion_score("cum facials") > 0 or the_girl.get_opinion_score("being covered in cum") > 0 ) and the_girl.sluttiness > 40:
                        "After a moment she takes her lips off your dick and continues stroking you."
                        the_girl.char "Mmm, I can't wait to feel your hot cum all over my face..."
                        "She strokes you off faster and holds your cock right against her face."
                        the_girl.char "When I'm on top of you like this, I can point it wherever I want! Cover my face with it!"
                        $ the_girl.discover_opinion("cum facials")
                        $ the_girl.discover_opinion("being covered in cum")
                        $ the_girl.change_arousal(5)
                        "You give [the_girl.possessive_title]'s ass a hard smack and resume eating her pussy."
                        "[the_girl.possessive_title]'s cunt quivers as she slides your cock back into her mouth, sucking at it with renewed vigor."
                    elif the_girl.get_opinion_score("drinking cum") > 0 and the_girl.sluttiness > 40:
                        "After a moment she takes her lips off your dick and continues stroking you."
                        the_girl.char "Mmm, I can't wait to feel your cum sliding down my throat [the_girl.mc_title]."
                        "She latches back onto your cock, sucking at the tip eagerly before letting it slip out again."
                        the_girl.char "I want you to flood my mouth with your cum. Ugh, I want it so badly!"
                        $ the_girl.discover_opinion("drinking cum")
                        $ the_girl.change_arousal(5)
                        "[the_girl.possessive_title]'s cunt quivers as she slides your cock back into her mouth, sucking at it with renewed vigor."
                    else:
                        "You lap at [the_girl.possessive_title]'s pussy leisurely while she services your cock, stroking your shaft and sucking gently on your tip."


    else: #Amazing at oral
        "[the_girl.possessive_title] slides your cock all the way down into her throat. She uses one hand to cup and lightly stroke your balls while she hungrily throat you."
        "You circle her clit a few times with your tongue. You suck it into your mouth roughly a couple of times and then release it, you lips making a wet, lewd smackin noise"
        "You can feel [the_girl.possessive_title]'s throat contracting around you as she uses a swallowing motion to pleasure you. The sensation is intensly pleasurable."
        "It feels so good it is making it hard for you to concentrate on pleasuring her."
        menu:
            "Focus on her" if mc.sex_skills["Oral"] > 5:
                "Not to be outdone, you double down on your efforts to please [the_girl.possessive_title] orally."
                "You aggressively lick her clit, while simultaneously kneading her ass cheeks with your hands. You pull her clit into your mouth and suck on it lightly."
                the_girl.char "mmmmmmmfff"
                "The vibrations in [the_girl.possessive_title]'s throat feel amazing around your cock. You lick up some of her fluids that are beginning to drip down then lick up an down the length of slit a few times."
                if the_girl.get_opinion_score("drinking cum") > 0 and (the_girl.get_opinion_score("drinking cum") >= the_girl.get_opinion_score("cum facials")):
                    "[the_girl.possessive_title] pulls off you for a moment."
                    the_girl.char "Oh god, [the_girl.mc_title], that feels so good. I can't wait to feel you blow your load straight down my throat!"
                    "[the_girl.possessive_title] licks up and down your shaft a few times, then slides your back into her mouth and slowly pushes herself down on to you, taking you all the way in."
                elif the_girl.get_opinion_score("cum facials") > 0:
                    "[the_girl.possessive_title] pulls off you for a moment."
                    the_girl.char "Oh god, [the_girl.mc_title], that feels so good. Make sure you warn me before you cum though... I want you to spray your cum all over my face!"
                "You can feel [the_girl.possessive_title]'s tongue slithering back and forth across the base of your dick, and her nose brushes up against your scrotum."
                "You and [the_girl.possessive_title] continue to please each other orally. You often you hear a muffled moan, accompanied by a pleasant vibration in your groin."

            "Focus on her\n{color=#ff0000}{size=18}Requires More Oral Skill{/size}{/color} (disabled)" if mc.sex_skills["Oral"] < 6:
                pass
            "Focus on you":
                "It feels so good, you don't even realize it but you stop licking her and close your eyes."
                mc.name "[the_girl.title]! Holy hell girl that feels so good."
                "You can feel [the_girl.possessive_title]'s tongue slithering back and forth across the base of your dick."
                $ mc.change_arousal(5)
                if the_girl.get_opinion_score("taking control") > 0:
                    "Suddenly, [the_girl.possessive_title] pulls you out of her throat."
                    the_girl.char "Hey now, don't forget about me!"
                    "You open your eyes just in time to see her back her pussy down onto your face as she begins to grind herself on you."
                    "You are caught unready. When you have a chance, you gasp a deep breath of air and begin to start licking her."
                    the_girl.char "Mmm, that's it [the_girl.mc_title]"
                    $ the_girl.change_arousal(5 * the_girl.get_opinion_score("taking control"))
                    "You eat her out for several seconds, as best as you can, while she grinds back against you. She strokes your shaft with her hand in time as she grinds on you."
                    "Eventually she eases off your face, giving you a chance to catch your breath. She slowly lick you around the tip of your shaft a few times then resumes bobbing her head up and down on you."
                else:
                    "Lost in the pleasure, [the_girl.possessive_title] suddenly pulls you out of her throat."
                    the_girl.char "Hey now, don't forget about me!"
                    "Your eyes snap open. You resume licking [the_girl.possessive_title]'s pussy with renewed vigor, hoping she will go back to what she was doing a moment ago."
                    "After a few moments, [the_girl.possessive_title] lowers her head back to your cock. She circles the tip with her tongue a few times, and then you feel the wonderful sensation as she slides you back into her mouth."


    return

label scene_SB_sixty_nine_2(the_girl, the_location, the_object):

    "[the_girl.possessive_title] pulls your cock out of her her mouth and starts to stroke you with her hand while her tongue circles around the tip."
    if the_girl.arousal > 50:
        "Her pussy glistens with moisture above you. You eagerly lap it up and the push your tongue into her moist, wet hole."
    else:
        "Her pristine pussy beckons your tongue. You eagerly push your tongue up into her moist, wet hole."

    menu:
        "Play with her ass":
            "You take a finger and push it into her pussy a few times and get it nice and lubed up."
            "[the_girl.possessive_title] moans as she working her tongue over your cock. She licks it bottom to top, then sucks on the tip, then licks it from the top back to the bottom."
            "You pull your finger out of her and start to slowly circle her asshole with it as your tongue moves around her clit."
            if the_girl.get_opinion_score("anal sex") > 0:
                "[the_girl.possessive_title] bucks her hips slightly as you start to push your finger into her tight back passage. Her back arches in pleasure."
                the_girl.char "Mmm! [the_girl.mc_title] don't stop, that feels so good."
                "She slips you back into her mouth. As you push your finger deeper into her rectum she takes you deeper in her mouth."
                $ the_girl.discover_opinion("anal sex")
                $ the_girl.change_arousal(the_girl.get_opinion_score("anal sex") + mc.sex_skills["Anal"])
                "[the_girl.possessive_title] mimics your motions with her mouth, bouncing her face up and down on your cock as you finger fuck her asshole."

            elif the_girl.get_opinion_score("anal sex") < 0:
                the_girl.char "Hey! Wrong hole! Don't touch me back there!"
                "It seems that [the_girl.possessive_title] doesn't like having her ass played with."
                $ the_girl.discover_opinion("anal sex")
                $ the_girl.change_arousal(the_girl.get_opinion_score("anal sex"))
            elif the_girl.sluttiness > 60:
                "[the_girl.possessive_title] tenses slightly as you start to push your finger into her back passage, but otherwise doesn't resist."
                mc.name "Relax [the_girl.title], let me take care of you."
                "You can feel her rectum physically unclench with your encouragement. You begin to slowly move your finger in and out of her."
                the_girl.char "That feels good [the_girl.mc_title]... just be careful with me back there!"
                "As you finger her, she delicately licks the tip of your dick for a bit, before parting her lips and resuming her suckling motions."
                $ the_girl.change_arousal(mc.sex_skills["Anal"])
            else:
                "[the_girl.possessive_title] tenses slightly as you start to push your finger into her back passage and begins to protest."
                mc.name "Hush [the_girl.title], let me take care of you."
                "[the_girl.possessive_title] stays pretty tense, so for now you just leave your finger where it is."
                "You decide to resume licking her pussy, your finger halfway inside her rectum."
                "[the_girl.possessive_title] delicately licks the tip of your dick for a bit, before parting her lips and resuming her suckling motions."
            "You decide that is enough ass play for now, so you resume eating [the_girl.possessive_title] out."


        "Finger Her":
            "You take a finger and push it into her pussy, while your tongue slithers back and forth across her slit."
            "[the_girl.possessive_title] moans as she working her tongue over your cock. She licks it bottom to top, then sucks on the tip, then licks it from the top back to the bottom."
            if mc.sex_skills["Foreplay"] > 2:   #MC is competent at foreplay
                "You push a second finger into her. [the_girl.possessive_title] moans around the base of your cock as she licks it up and down."
                "She stops stroking you with her hand, and you feel her welcoming lips around the tip of your cock as she resumes her sucking."
                "You push your fingers along the front of her steamy cunt, seeking out her G-spot. Her moan is muffled by your erection in her mouth."
                "[the_girl.possessive_title] shudders as your start to stroke her special spot. Your manhood pops out of her mouth suddenly as she moans, distracted by the pleasure."
                "With your other hand you give her ass a quick smack. She gasps and then quickly begins suckling your manhood again."
                $ the_girl.change_arousal(mc.sex_skills["Foreplay"])

            else:
                "You twirl you finger inside her for a bit, and then begin to push your finger in and out."
                "She stops stroking you with her hand, and you feel her welcoming lips around the tip of your cock as she resumes her sucking."
                "[the_girl.possessive_title]'s steamy cunt accepts your probing as you continue to lick and suck at her clit."
            if the_girl.arousal > 80:
                "[the_girl.possessive_title]'s drenched cunt pulsates around your finger."
            else:
                "[the_girl.possessive_title]'s creamy cunt melts around your finger."
            if the_girl.sex_skills["Oral"] < 6:
                "[the_girl.possessive_title] renews her vigor as she blows you. Her insistent mouth feels amazing around your shaft."
            else:
                "[the_girl.possessive_title] renews her vigor as she blows you. Her nose nestles into your balls as her easily swallows you into her greedy throat."
                "Her tongue feels amazing as she strokes you, her mouth nearly overloads your senses."
            "You continue to lick and tease [the_girl.possessive_title] as you slowly pull your finger out."


    return

label outro_SB_sixty_nine(the_girl, the_location, the_object):
    #$ SB_sixty_nine.current_modifier = "SB_sixty_nine"
    $ SB_sixty_nine.redraw_scene(the_girl)
    "Little by little the soft, warm mouth of [the_girl.possessive_title] brings you closer to orgasm. One last pass across her velvet tongue is enough to push you past the point of no return."
    mc.name "Ah, I'm going to cum!"
    if the_girl.get_opinion_score("cum facials") > 0: #She loves facials
        if the_girl.get_opinion_score("cum facials") == the_girl.get_opinion_score("drinking cum"):   #She likes them equally, so do one randomly
            if renpy.random.randint(0,100) < 50: #In her mouth
                if the_girl.has_role(oral_fetish_role):
                    "You feel [the_girl.possessive_title] take you all the way in her mouth as you start to orgasm."
                    "You grunt and twitch as you start to empty your balls right into her stomach."
                    "She tightens and relaxes her throat, swallowing your erection over and over as it spurts every last drop of cum straight down her throat."
                    $ the_girl.cum_in_mouth()
                    #$ SB_sixty_nine.redraw_scene(the_girl)
                    "When you're completely finished she pulls off slowly, kissing the tip before leaning back."
                    $ the_girl.call_dialogue("cum_mouth")
                elif the_girl.has_role(cum_internal_role):
                    "[the_girl.possessive_title] pulls off until just the tip of your cock is in her mouth and she begins to stroke you off eagerly."
                    "You erupt in orgasm into her greedy mouth. Her expert mouth milks you with every spurt."
                    "[the_girl.possessive_title] begins moaning uncontrollably around your twitching cock when her cum addicted brain registers her cum dosage."
                else:
                    "You feel [the_girl.possessive_title] leave just the tip of you in her mouth. She strokes you with her hand as you start to orgasm."
                    "She moans as you fill up her mouth with your sperm."
                    $ the_girl.cum_in_mouth()
                    #$ SB_sixty_nine.redraw_scene(the_girl)
                    "When you're completely finished, you can feel her swallow the contents of her mouth, before slowly pulling off."

                $ the_girl.call_dialogue("cum_mouth")
            else: #on her face
                "[the_girl.possessive_title] pulls you out of her mouth, and begins stroking you eagerly."
                the_girl.char "That's it, [the_girl.mc_title], cum all over me!"
                $ the_girl.cum_on_face()
                if the_girl.has_role(cum_external_role):
                    "[the_girl.possessive_title] begins moaning uncontrollably as she receives the cum her addicted brain has been begging her for."
                #$ SB_sixty_nine.redraw_scene(the_girl)
                "You let out a shudder moaning as you cum, pumping your sperm onto [the_girl.possessive_title]'s face. She sighs when you're completely finished."
                $ the_girl.call_dialogue("cum_face")
        else:
            "[the_girl.possessive_title] pulls you out of her mouth, and begins stroking you eagerly."
            the_girl.char "That's it, [the_girl.mc_title], cum all over me!"
            $ the_girl.cum_on_face()
            if the_girl.has_role(cum_external_role):
                "[the_girl.possessive_title] begins moaning uncontrollably as she receives the cum her addicted brain has been begging her for."
            #$ SB_sixty_nine.redraw_scene(the_girl)
            "You let out a shudder moaning as you cum, pumping your sperm onto [the_girl.possessive_title]'s face. She sighs when you're completely finished."
            $ the_girl.call_dialogue("cum_face")
        "You give [the_girl.possessive_title]'s slit a few more appreciative licks, and then you both start to get up."
    elif the_girl.get_opinion_score("drinking cum") > 0:
        if the_girl.has_role(cum_internal_role):
            "[the_girl.possessive_title] pulls off until just the  tip of your cock is in her mouth and she begins to stroke you off eagerly."
            "You erupt in orgasm into her greedy mouth. Her expert mouth milks you with every spurt."
            "[the_girl.possessive_title] begins moaning uncontrollably around your twitching cock when her cum addicted brain registers her cum dosage."
        elif the_girl.sex_skills["Oral"] > 5:
            "You feel [the_girl.possessive_title] take you all the way in her mouth as you start to orgasm."
            "You grunt and twitch as you start to empty your balls right into her stomach."
            "She tightens and relaxes her throat, swallowing your erection over and over as it spurts every last drop of cum straight down her throat."
            $ the_girl.cum_in_mouth()
            #$ SB_sixty_nine.redraw_scene(the_girl)
            "When you're completely finished she pulls off slowly, kissing the tip before leaning back."
        else:
            "You feel [the_girl.possessive_title] leave just the tip of you in her mouth. She strokes you with her hand as you start to orgasm."
            "She moans as you fill up her mouth with your sperm."
            $ the_girl.cum_in_mouth()
            #$ SB_sixty_nine.redraw_scene(the_girl)
            "When you're completely finished, you can feel her swallow the contents of her mouth, before slowly pulling off."

        $ the_girl.call_dialogue("cum_mouth")
        "You give [the_girl.possessive_title]'s slit a few more appreciative licks, and then you both start to get up."
    elif the_girl.sex_skills["Oral"] > 5: #She is amazing at oral
        "You feel [the_girl.possessive_title] take you all the way in her mouth as you start to orgasm."
        "You grunt and twitch as you start to empty your balls right into her stomach."
        "She tightens and relaxes her throat, swallowing your erection over and over as it spurts every last drop of cum straight down her throat."
        $ the_girl.cum_in_mouth()
        #$ SB_sixty_nine.redraw_scene(the_girl)
        "When you're completely finished she pulls off slowly, kissing the tip before leaning back."
        $ the_girl.call_dialogue("cum_mouth")
        "You give [the_girl.possessive_title]'s slit a few more appreciative licks, and then you both start to get up."
    elif the_girl.sluttiness < 40:
        "[the_girl.possessive_title] pulls you out of her mouth, and begins stroking you."
        $ the_girl.cum_on_face()
        #$ SB_sixty_nine.redraw_scene(the_girl)
        "You let out a shudder moaning as you cum, pumping your sperm onto [the_girl.possessive_title]'s face."
        $ the_girl.call_dialogue("cum_face")
    else:
        "You feel [the_girl.possessive_title] leave just the tip of you in her mouth. She strokes you with her hand as you start to orgasm."
        $ the_girl.cum_in_mouth()
        #1$ SB_sixty_nine.redraw_scene(the_girl)
        "When you're completely finished, you can feel her swallow the contents of her mouth, before slowly pulling off."
        "You give [the_girl.possessive_title]'s slit a few more appreciative licks, and then you both start to get up."

    return

label transition_SB_sixty_nine_deepthroat(the_girl, the_location, the_object):  #Delete this?
    mc.name "Fuck that feels great [the_girl.possessive_title]. Think you can take it any deeper?"
    #$ SB_sixty_nine.current_modifier = None
    $ SB_sixty_nine.redraw_scene(the_girl)
    "[the_girl.possessive_title] slides off your dick with a wet pop and takes a few breaths."
    the_girl.char "Well, I can try."
    #$ SB_sixty_nine.current_modifier = "SB_sixty_nine"
    $ SB_sixty_nine.redraw_scene(the_girl)
    "Once she's caught her breath she opens her mouth wide and slides you back down her throat. She doesn't stop until her nose taps your stomach and she has your entire cock in her mouth."
    return

label transition_default_SB_sixty_nine(the_girl, the_location, the_object):
    $ SB_sixty_nine.redraw_scene(the_girl)
    "You lay down on the [the_object.name]. [the_girl.possessive_title] swings one leg over your head and slowly moves her body into position on top of yours."
    if mc.condom:
        the_girl.char "Why are you wearing this thing? Lets take this off so I can take care of you better..."
        "[the_girl.possessive_title] pulls off your condom."
        $ mc.condom = False
    return

label strip_SB_sixty_nine(the_girl, the_clothing, the_location, the_object):
    "[the_girl.possessive_title] pops off your cock."
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing)
    "[the_girl.possessive_title] wiggles out of her [the_clothing.name]. She throws it to the side, then slides your cock inside her mouth."
    $ SB_sixty_nine.redraw_scene(the_girl)
    return

label strip_ask_SB_sixty_nine(the_girl, the_clothing, the_location, the_object):
    #$ SB_sixty_nine.current_modifier = None
    $ SB_sixty_nine.redraw_scene(the_girl)

    "[the_girl.possessive_title] pops off your cock."
    the_girl.char "Sir, I'd like to take off my [the_clothing.name], would you mind?"
    menu:
        "Let her strip":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = SB_sixty_nine.position_tag)
            "[the_girl.possessive_title] wiggles out of her [the_clothing.name]. She throws it to the side, then slides your cock all the way to the back of her mouth."
            $ SB_sixty_nine.redraw_scene(the_girl)

        "Leave it on":
            mc.name "No, don't interrupt this for that."
            the_girl.char "Okay... I just wanted to feel you up against me a little more..."
            "She slides you back into her mouth and presses you all the way to the back, rubbing your tip against the back of her throat for a second before she goes back to blowing you."
    return

label orgasm_SB_sixty_nine(the_girl, the_location, the_object):
    "Licking and probing all around [the_girl.possessive_title]'s clit, you can feel her start to quiver."
    "[the_girl.possessive_title] pauses suddenly. You hear her moaning, the sound muffled by your cock in her mouth."
    if the_girl.sex_skills["Oral"] < 4:
        "[the_girl.possessive_title] starts to pull back off until just the tip of your erection is left in her mouth."
    else:
        "[the_girl.possessive_title] pushes her face down on to your cock, burying it in her throat."
    the_girl.char "mmmmm....MMMMM....MMMMMMMFFFF"
    "She moans loudly as orgasmic waves wash over her. Once you think you hear her call your name, but the sound is muffled and mostly incomprehensible with your cock in her mouth."
    "After several seconds [the_girl.possessive_title] sighs and then begins to bob her head up and down on your again."
    return

label taboo_break_SB_sixty_nine(the_girl, the_location, the_object):
    # TODO: Add custom taboo break
    return
