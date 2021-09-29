# enhancements for blowjob
# Original code by BadRabbit

init 5 python:
    blowjob.intro = "intro_blowjob_enhanced"
    blowjob.outro = "outro_blowjob_enhanced"
    blowjob.transition_default = "transition_default_blowjob_enhanced"
    deepthroat.outro = "outro_deepthroat_enhanced"
    deepthroat.transition_default = "transition_default_deepthroat_enhanced"
    skull_fuck.outro = "outro_skull_fuck_enhanced"

    blowjob.transitions.remove([deepthroat, "transition_blowjob_deepthroat"])
    blowjob.transitions.append([deepthroat, "transition_blowjob_deepthroat_enhanced"])

label intro_blowjob_enhanced(the_girl, the_location, the_object):
    "You unzip your pants and pull your underwear down far enough to let your hard cock out."
    mc.name "How about you take care of this for me?"
    if the_girl.has_cum_fetish() or the_girl.get_opinion_score("giving blowjobs") > 1:
        $ blowjob.redraw_scene(the_girl)
        "Without hesitation, [the_girl.possessive_title] drops to her knees in front of you. She runs her hands along your hips, then leans forward and slides her lips over the tip of your dick."
    else:
        "[the_girl.possessive_title] grabs your cock with one hand."
        the_girl "Sure thing but what do you want?"
        mc.name "How about a blowjob?"
        if the_girl.effective_sluttiness() > 35 or the_girl.get_opinion_score("giving blowjobs") > 0:
            "[the_girl.possessive_title] looks down at your shaft, thinks about it for a moment, then drops to her knees in front of you. She leans forward and slides her lips over the tip of your dick."
        else:
            "[the_girl.possessive_title] looks down at your shaft for a moment, thinks about it for a moment, then drops to her knees in front of you. She leans forward and kisses the tip of your dick gingerly."
        $ blowjob.redraw_scene(the_girl)

    $ blowjob.current_modifier = "blowjob"
    $ blowjob.redraw_scene(the_girl)
    return

label outro_blowjob_enhanced(the_girl, the_location, the_object):
    $ blowjob.current_modifier = "blowjob"
    $ blowjob.redraw_scene(the_girl)
    "Little by little the soft, warm mouth of [the_girl.title] brings you closer to orgasm. One last pass across her velvet tongue is enough to push you past the point of no return."
    $ climax_controller = ClimaxController(["Cum on her face","face"],["Cum in her mouth","mouth"])
    $ the_choice = climax_controller.show_climax_menu()
    if the_choice == "Cum on her face":
        mc.name "Fuck, here I come!"
        call blowjob_enhanced_kneel_face_cum(the_girl) from _call_blowjob_enhanced_kneel_face_cum_outro_blowjob
    elif the_choice == "Cum in her mouth":
        $ blowjob.current_modifier = "blowjob"
        $ blowjob.redraw_scene(the_girl)
        mc.name "Fuck, I'm about to cum!"
        "You keep a hand on the back of [the_girl.title]'s head to make it clear you want her to keep sucking."
        call blowjob_enhanced_kneel_mouth_cum(the_girl) from _call_blowjob_enhanced_kneel_mouth_cum_outro_blowjob
    return

label outro_deepthroat_enhanced(the_girl, the_location, the_object):
    $ deepthroat.current_modifier = "blowjob"
    $ deepthroat.redraw_scene(the_girl)
    "The warm, tight feeling of [the_girl.title]'s throat wrapped around your shaft pulls you closer and closer to orgasm. You feel yourself pass the point of no return and let out a soft moan."

    $ climax_controller = ClimaxController(["Cum on her face", "face"],["Cum in her mouth", "mouth"],["Cum down her throat", "throat"])
    $ the_choice = climax_controller.show_climax_menu()

    if the_choice == "Cum on her face":
        mc.name "Fuck, here I come!"
        $ deepthroat.current_modifier = None
        $ deepthroat.redraw_scene(the_girl)
        call blowjob_enhanced_kneel_face_cum(the_girl) from _call_blowjob_enhanced_kneel_face_cum_outro_deepthroat
    elif the_choice == "Cum in her mouth":
        $ blowjob.current_modifier = "blowjob"
        $ blowjob.redraw_scene(the_girl)
        mc.name "Fuck, I'm about to cum! I'm going to fill that cute mouth of yours up!"
        "You keep your hand on the back of [the_girl.title]'s head to make it clear you want her to keep sucking."
        call blowjob_enhanced_kneel_mouth_cum(the_girl) from _call_blowjob_enhanced_kneel_mouth_cum_outro_deepthroat
    elif the_choice == "Cum down her throat":
        mc.name "Fuck, here I come!"
        $ blowjob.current_modifier = "blowjob"
        $ blowjob.redraw_scene(the_girl)
        call blowjob_enhanced_kneel_throat_cum(the_girl) from _call_blowjob_enhanced_kneel_throat_cum_outro_deepthroat
    return

label outro_skull_fuck_enhanced(the_girl, the_location, the_object):
    "[the_girl.title]'s warm, wet throat wrapped around your cock sends shivers up your spine and the sound of her gagging on your dick pushes you past your limits."
    "You have a brief moment to consider how you want to finish as you jackhammer yourself in and out of her mouth."

    $ climax_controller = ClimaxController(["Cum on her face", "face"],["Cum down her throat", "throat"])
    $ the_choice = climax_controller.show_climax_menu()

    if the_choice == "Cum on her face":
        mc.name "Fuck, here I come!"
        $ deepthroat.current_modifier = None
        $ deepthroat.redraw_scene(the_girl)
        call blowjob_enhanced_kneel_face_cum(the_girl) from _call_blowjob_enhanced_kneel_face_cum_outro_skull_fuck
    elif the_choice == "Cum down her throat":
        mc.name "Fuck, here I come!"
        $ blowjob.current_modifier = "blowjob"
        $ blowjob.redraw_scene(the_girl)
        call blowjob_enhanced_kneel_throat_cum(the_girl) from _call_blowjob_enhanced_kneel_throat_cum_outro_skull_fuck
    return

label transition_default_blowjob_enhanced(the_girl, the_location, the_object):
    if mc.condom:
        the_girl "I don't think we need this anymore."
        "[the_girl.possessive_title] pulls the condom off your dick."
        $ mc.condom = False

    $ blowjob.current_modifier = "blowjob"
    $ blowjob.redraw_scene(the_girl)
    if the_girl.has_cum_fetish() or the_girl.get_opinion_score("giving blowjobs") > 1:
        "Without hesitation, [the_girl.possessive_title] drops to her knees in front of you. She runs her hands along your hips, then leans forward and slides her lips over the tip of your dick."
    else:
        if the_girl.effective_sluttiness() > 35 or the_girl.get_opinion_score("giving blowjobs") > 0:
            "[the_girl.possessive_title] looks at your shaft then drops to her knees in front of you. She leans forward and slides her lips over the tip of your dick."
        else:
            "[the_girl.possessive_title] looks at your shaft for a moment then drops to her knees in front of you. She leans forward and kisses the tip of your dick gingerly."
    mc.name "That's it, that's a good girl."
    return

label transition_blowjob_deepthroat_enhanced(the_girl, the_location, the_object):
    mc.name "Fuck that feels great [the_girl.title]. Think you can take it any deeper?"
    $ blowjob.current_modifier = None
    $ blowjob.redraw_scene(the_girl)
    "[the_girl.possessive_title] slides off your dick with a wet pop and takes a few breaths."
    if the_girl.body_type == "curvy_body" and the_girl.get_opinion_score("giving blowjobs") > 0 and the_girl.sex_skills["Oral"] > 3 and renpy.random.randint(0,2) == 0:
        the_girl "Well you know what they say."
        mc.name "What?"
        the_girl "Big girls give better head."
        "With that she opens her mouth wide and slides you back down her throat. She doesn't stop until her nose taps your stomach and she has your entire cock in her mouth. [the_girl.possessive_title] look up at you and winks as she starts to very slightly bob her head."
    else:
        if the_girl.effective_sluttiness() > 60 or the_girl.sex_skills["Oral"] > 3 :
            if the_girl.get_opinion_score("giving blowjobs") < 0:
                the_girl "Okay [the_girl.mc_title], I'll see what I can do."
            else:
                the_girl "Okay [the_girl.mc_title], I'll see what I can do, but I'm not very good at it."
        else:
            the_girl "I'll... I'll do my best."

        if the_girl.sex_skills["Oral"] < 3:
            "She kisses the tip of your cock, then slides it into her mouth. Gets your length half way down, then gags softly on it and pauses."
            $ deepthroat.current_modifier = "blowjob"
            $ deepthroat.redraw_scene(the_girl)
            "[the_girl.possessive_title] collects herself then keeps going, fighting her gag reflex until she manages to fit three quarters of your shaft down her throat."
        else:
            $ deepthroat.current_modifier = "blowjob"
            $ deepthroat.redraw_scene(the_girl)
            "She kisses the tip of your cock, then slides it into her mouth. Bit by bit she takes it deeper, until you have your entire shaft down her throat."
            "She pauses there for a moment, then starts to bob her head up and down slowly."
    return

label transition_blowjob_to_deepthroat_taboo_break_label(the_girl, the_location, the_object):
    mc.name "Fuck that feels great [the_girl.title]. Could you do something for me?"
    $ blowjob.current_modifier = None
    $ blowjob.redraw_scene(the_girl)
    "[the_girl.possessive_title] slides off your dick with a wet pop and takes a few breaths."
    the_girl "Alright, what dirty thought crossed your mind?"
    mc.name "Could you slide my dick as deep as possible down your throat?"
    the_girl "Oh, you want me to deepthroat this monster..."
    if the_girl.effective_sluttiness() > 60 or the_girl.sex_skills["Oral"] > 3 :
        if the_girl.get_opinion_score("giving blowjobs") < 0:
            the_girl "Okay [the_girl.mc_title], I'll see what I can do."
        else:
            the_girl "Okay [the_girl.mc_title], I'll see what I can do, but I'm not very good at it."
    else:
        the_girl "I'll... I'll give it a try..."

    if the_girl.sex_skills["Oral"] < 3:
        "She kisses the tip of your cock, then slides it into her mouth. Gets your length half way down, then gags softly on it and pauses."
        $ deepthroat.current_modifier = "blowjob"
        $ deepthroat.redraw_scene(the_girl)
        "[the_girl.possessive_title] collects herself then keeps going, fighting her gag reflex until she manages to fit three quarters of your shaft down her throat."
    else:
        $ deepthroat.current_modifier = "blowjob"
        $ deepthroat.redraw_scene(the_girl)
        "She kisses the tip of your cock, then slides it into her mouth. Bit by bit she takes it deeper, until you have your entire shaft down her throat."
        "She pauses there for a moment, then starts to bob her head up and down slowly."
    return

label transition_default_deepthroat_enhanced(the_girl, the_location, the_object):
    if mc.condom:
        "You pull the condom off your dick as [the_girl.title] gets ready in front of you, on her knees with her mouth open."
        $ mc.condom = False
    else:
        "[the_girl.title] gets ready in front of you, on her knees with her mouth open."
    $ blowjob.redraw_scene(the_girl)

    menu:
        "Ask for deepthroat":
            mc.name "Why don't you take it nice and deep?"
            if the_girl.has_cum_fetish() or the_girl.get_opinion_score("giving blowjobs") > 1:
                "Without hesitation, [the_girl.possessive_title] leans forward and slides your dick down her throat."
            else:
                "She gives a nod and slowly slides your cock half way down, until she starts gagging and pulls back."
                the_girl "Erm, I still need to get used to your size."

        "Guide her":
            "You place a hand on the back of her head and slowly pull her towards you, sliding your cock down her throat."
            if the_girl.has_cum_fetish() or the_girl.get_opinion_score("being submissive") > 0:
                "She doesn't resist and lets you push her all the way down, while looking lovingly into your eyes."
            elif the_girl.get_opinion_score("taking control") > 0:
                if the_girl.sex_skills["Oral"] >= 3:
                    "She pushes away your hand, smiles, and pushes your cock all the way down, squeezing your balls just a little too hard."
                else:
                    "She slaps your hand away, and continues to suck your dick, albeit a little deeper than before."
                    $ the_girl.change_stats(arousal = -10)
            else:
                if the_girl.sex_skills["Oral"] >= 3:
                    "Slowly she takes your hand away, but slides your cock all the way down her throat."
                else:
                    "She shifts her position so you can no longer guide her, but she slides your cock down a little further."
                    $ the_girl.change_stats(arousal = -5)

        "Push her down":
            "You place a hand on the back of her head and you push your cock down her throat."
            if the_girl.has_cum_fetish() or the_girl.get_opinion_score("being submissive") > 0:
                "She doesn't resist and lets you push her all the way down, while looking lovingly into your eyes."
            elif the_girl.get_opinion_score("taking control") > 0:
                if the_girl.sex_skills["Oral"] >= 4:
                    "She is resisting your push, slowly sliding your cock all the way down, squeezing your balls just a little too hard."
                else:
                    "She resists your push, spitting out your cock."
                    the_girl "Hey, I'm not your fleshlight! Let me do this on my own."
                    $ the_girl.change_stats(arousal = -10, happiness = -2)
            else:
                if the_girl.sex_skills["Oral"] >= 4:
                    "She doesn't resist and lets you push her down, while looking into your eyes."
                else:
                    "She resists your push, coming back up."
                    the_girl "Don't be so rough, let us enjoy this."
                    $ the_girl.change_stats(arousal = -5, happiness = -1)

    "After taking a few seconds to get used to your size she starts to move back and forth, with each thrust forward, burying your cock nice and deep in her throat."
    return

label blowjob_enhanced_kneel_throat_cum(the_girl):
    if the_girl.obedience >= 130 or the_girl.get_opinion_score("drinking cum") > 0: #She takes it like a champ
        "With both hands firmly on [the_girl.possessive_title]'s head you pull her as far down your cock as she'll go."
        "You grunt and release your load, firing pulse after pulse of hot cum down her throat and directly into her stomach."
        $ skull_fuck.current_modifier = None
        $ skull_fuck.redraw_scene(the_girl)
        "[the_girl.title] struggles to drink it all down, but doesn't try and pull off."
        $ ClimaxController.manual_clarity_release(climax_type = "throat", the_person = the_girl)
        $ the_girl.cum_in_mouth()
        $ skull_fuck.redraw_scene(the_girl)
        "When the last moments of your climax have passed you pull back, cock trailing spit and cum as you leave her mouth."
        if the_girl.get_opinion_score("drinking cum") > 0:
            the_girl "I thought you were going to drown me with your cum for a moment... Mmmm."
            $ the_girl.change_slut(1)
            $ the_girl.change_happiness(1)
            "She shivers with pleasure at the thought."
        else:
            "She runs the back of her hand along her lips, removing the cum trails and sits back to catch her breath."
            $ the_girl.call_dialogue("cum_mouth")

    elif the_girl.effective_sluttiness() > 90 or (the_girl.get_opinion_score("giving blowjobs") > 0 and the_girl.sex_skills["Oral"] > 0) or the_girl.sex_skills["Oral"] > 3:
        "[the_girl.possessive_title] looks up at you and stares into your eyes as you climax."
        if the_girl.sex_skills["Oral"] > 3:
            "She tightens and relaxes her throat, as if to draw out every last drop of semen from you."
        "She gently licks your balls with her tongue."
        $ ClimaxController.manual_clarity_release(climax_type = "throat", the_person = the_girl)
        $ the_girl.cum_in_mouth()
        $ deepthroat.redraw_scene(the_girl)
        "When you're completely finished she pulls off slowly, kissing the tip before leaning back."
        $ the_girl.call_dialogue("cum_mouth")
    elif the_girl.effective_sluttiness() > 60 or the_girl.get_opinion_score("giving blowjobs") > -1 or the_girl.sex_skills["Oral"] > 1:
        "[the_girl.possessive_title] closes her eyes and holds still as you climax. You feel her throat spasm a few times as she struggles to keep your cock in place."
        $ ClimaxController.manual_clarity_release(climax_type = "throat", the_person = the_girl)
        $ the_girl.cum_in_mouth()
        $ deepthroat.redraw_scene(the_girl)
        "When you're finished she pulls off quickly, gasping for air. It takes a few seconds for her to regain her composure."
        $ the_girl.call_dialogue("cum_mouth")
    else:
        "[the_girl.possessive_title] closes her eyes and tries to hold still as you climax. Her throat spasms as soon as the first blast of sperm splashes across the back, and she goes to pull back."
        menu:
            "Let her pull back":
                "With no other choice, you stroke yourself off onto her face as she coughs and gasps for breath."
                $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_girl)
                $ the_girl.cum_on_face()
                $ deepthroat.redraw_scene(the_girl)
                $ the_girl.call_dialogue("cum_face")
            "Stop her":
                "You grab [the_girl.possessive_title]'s head with both hands and pull her as far down your cock as she'll go."
                "[the_girl.title]'s eyes go wide as she realizes you don't intend to let her off your cock as you cum."
                "She tries to pull her head back, but you hold it in place as you begin to unload your hot, sticky load directly into her throat."
                "For a brief second she manages to keep up with the torrent of cum, then it overwhelms her."
                "She spasms and gags. A mix of her spit and your semen bubble around the base of your cock, collecting in drops that roll down her chin and onto her tits."
                "She gags and coughs again, this time blowing little cum bubbles out of her nose as her body struggles to find somewhere to put more and more of your sperm."
                $ ClimaxController.manual_clarity_release(climax_type = "throat", the_person = the_girl)
                $ the_girl.cum_in_mouth()
                $ skull_fuck.redraw_scene(the_girl)
                "Finally you're spent and you finally let [the_girl.title] pull off of your cock."
                the_girl "Guahh... Guahh... Ah.... Ah...."
                mc.name "Fuck that felt good."
                the_girl "There was so much... Ah... I thought I was going to drown in it..."
                "Still gasping for air, she wipes your sperm away from her nose and chin, then swallows loudly to get rid of the rest of it."
                $ the_girl.call_dialogue("cum_mouth")
                $ the_girl.change_arousal(the_girl.get_opinion_score("drinking cum") + the_girl.get_opinion_score("being submissive"))
    return

label blowjob_enhanced_kneel_mouth_cum(the_girl):
    if the_girl.get_opinion_score("drinking cum") < 0:
       "[the_girl.title] clearly has other ideas as she brings one hand up to your cock and goes to pull her mouth off of your cock."
       menu:
           "Let her off":
                "You let her pull back."
                $ the_girl.change_stats(love = -the_girl.get_opinion_score("drinking cum"), happiness = -the_girl.get_opinion_score("drinking cum"))
                if the_girl.has_cum_fetish():
                    "[the_girl.title] takes a hold of your cock with one hand and starts to pump it."
                    "She sticks out her tongue for you and holds still, eager to take your hot load."
                    $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_girl)
                    $ the_girl.cum_on_face()
                    $ blowjob.redraw_scene(the_girl)
                    "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face and into her open mouth. She shivers herself as your cum splashes over her."
                    $ the_girl.change_arousal(10)
                elif the_girl.get_opinion_score("cum facials") < 0:
                    "[the_girl.title] moves her head so that your cum will miss her face."
                    if the_girl.get_opinion_score("being covered in cum") > 0):
                        "[the_girl.possessive_title] moves your cock to point at her chest."
                        $ ClimaxController.manual_clarity_release(climax_type = "body", the_person = the_girl)
                        $ the_girl.cum_on_tits()
                        $ blowjob.redraw_scene(the_girl)
                        $ the_girl.change_stats(love = the_girl.get_opinion_score("being covered in cum"), happiness = the_girl.get_opinion_score("being covered in cum"))
                        if the_girl.outfit.tits_available():
                            "You let out a shuddering moan as you cum, pumping your sperm over [the_girl.possessive_title]'s bare tits. She shivers herself as your cum splashes over her."
                        else:
                            "You let out a shuddering moan as you cum, pumping your sperm over [the_girl.possessive_title]'s chest. She smiles as your cum splashes over her."
                    else:
                        "You cum onto the floor, missing [the_girl.possessive_title] completely."
                        $ the_girl.change_stats(love = -the_girl.get_opinion_score("cum facials"), happiness = -the_girl.get_opinion_score("cum facials"))
                elif (the_girl.effective_sluttiness() > 80 or the_girl.get_opinion_score("cum facials") > 0):
                    "[the_girl.title] sticks out her tongue for you, holds still and looks you in the eye, eager to take your hot load."
                    $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_girl)
                    $ the_girl.cum_on_face()
                    $ blowjob.redraw_scene(the_girl)
                    "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face and into her open mouth. She makes sure to wait until you're completely finished as she maintains eye contact."
                elif the_girl.effective_sluttiness() > 60:
                    "[the_girl.title] closes her eyes and waits patiently for you to cum."
                    $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_girl)
                    $ the_girl.cum_on_face()
                    $ blowjob.redraw_scene(the_girl)
                    "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face. She waits until she's sure you're finished, then opens one eye and looks up at you."
                else:
                    "[the_girl.title] closes her eyes and turns away, presenting her cheek to you as you finally climax."
                    $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_girl)
                    $ the_girl.cum_on_face()
                    $ blowjob.redraw_scene(the_girl)
                    "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face. She flinches as the first splash of warm liquid lands on her cheek, but doesn't pull away entirely."

                if the_girl.has_face_cum():
                    "You take a deep breath to steady yourself once you've finished cumming. [the_girl.title] looks up at you from her knees, face covered in your semen."
                    $ the_girl.call_dialogue("cum_face")
                    if the_girl.has_cum_fetish():
                        "She closes her eyes and starts to gently massage your cum all over her face."

           "Hold her in place":
                "You grab her head with both your hands and thrust roughly into her mouth as you cum."
                $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = the_girl)
                $ the_girl.cum_in_mouth()
                $ blowjob.redraw_scene(the_girl)
                $ the_girl.call_dialogue("cum_mouth")
                if the_girl.get_opinion_score("being submissive") > 0:
                    $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive"))
                else:
                    $ the_girl.change_stats(arousal = the_girl.get_opinion_score("being submissive"), love = the_girl.get_opinion_score("drinking cum"), happiness = the_girl.get_opinion_score("drinking cum"))
    else:
        if the_girl.has_cum_fetish():
            if renpy.random.randint(0, 1) == 1: # random choice of cum fetish dialog
                "[the_girl.possessive_title] goes as deep as she can on your dick, trying to get as much of it in her mouth as possible."
                "You feel [the_girl.possessive_title] take you all the way in her mouth as you start to orgasm."
                "You grunt and twitch as you start to empty your balls right into her throat."
                "She tightens and relaxes her throat, swallowing your erection over and over as it spurts every last drop of cum straight down her throat."
                $ ClimaxController.manual_clarity_release(climax_type = "throat", the_person = the_girl)
                $ the_girl.cum_in_mouth()
                $ blowjob.redraw_scene(the_girl)
                "When you're completely finished she pulls back slightly so that she can breathe more easily."
                $ the_girl.call_dialogue("cum_mouth")
            else:
                "She keeps blowing you until you tense up and start to pump your load out into her mouth."
                "[the_girl.possessive_title] pulls her head back until just the tip of your cock is in her mouth and she begins to stroke you."
                "You erupt in orgasm into her greedy mouth. Her expert mouth milks you with every spurt."
                $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = the_girl)
                $ the_girl.cum_in_mouth()
                $ blowjob.redraw_scene(the_girl)
                $ the_girl.change_arousal(10)
                $ the_girl.call_dialogue("cum_mouth")
                "[the_girl.possessive_title] begins moaning uncontrollably around your twitching cock when her cum addicted brain registers her cum dosage."
        elif the_girl.effective_sluttiness() > 70 or the_girl.get_opinion_score("giving blowjobs") > 0:
            "[the_girl.possessive_title] doesn't even flinch as you shoot your hot cum across the back of her throat."
            $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = the_girl)
            $ the_girl.cum_in_mouth()
            $ blowjob.redraw_scene(the_girl)
            "She keeps bobbing her head up and down until you've let out every last drop, then slides back carefully. She looks up at you and opens her mouth to shows it full of sperm."
        else:
            "[the_girl.possessive_title] stops when you shoot your first blast of hot cum across the back of her throat."
            $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = the_girl)
            $ the_girl.cum_in_mouth()
            $ blowjob.redraw_scene(the_girl)
            "She pulls back, leaving just the tip of your cock in her mouth as you fill it up with semen. Once you've finished she slides off, looks up at you and opens her mouth to shows it full of sperm."


        if not the_girl.has_cum_fetish():
            if the_girl.get_opinion_score("being covered in cum") > 0 and the_girl.outfit.tits_available():
                "[the_girl.possessive_title] tilts her head forward and let your cum dribble out of her mouth onto her bare tits."
                $ the_girl.call_dialogue("cum_mouth")
                $ the_girl.cum_on_tits()
                $ blowjob.redraw_scene(the_girl)
                "She starts to rub your cum on her breasts."
            elif the_girl.effective_sluttiness() > 80 or the_girl.get_opinion_score("drinking cum") > 0:
                "Once you've had a good long look at your work [the_girl.title] closes her mouth and swallows loudly."
                "It takes a few big gulps to get every last drop of your cum down, but when she opens up again it's all gone."
                $ blowjob.current_modifier = None
                $ blowjob.redraw_scene(the_girl)
                $ the_girl.call_dialogue("cum_mouth")
            else:
                "Once you've had a good long look at your work [the_girl.title] leans over to the side and lets your cum dribble out slowly onto the ground."
                "She straightens up and wipes her lips with the back of her hand."
                $ blowjob.current_modifier = None
                $ blowjob.redraw_scene(the_girl)
                $ the_girl.call_dialogue("cum_mouth")
    return

label blowjob_enhanced_kneel_face_cum(the_girl):
    if the_girl.has_cum_fetish():
        if renpy.random.randint(0, 1) == 1: # random choice of cum fetish dialog
            "You go to step back but [the_girl.possessive_title]'s grabs your butt-cheeks with her hands, holding you in place and pushing her face forward."
            "You feel [the_girl.possessive_title] take you all the way in her mouth as you start to orgasm."
            "You grunt and twitch as you start to empty your balls right into her throat."
            "She tightens and relaxes her throat, swallowing your erection over and over as it spurts every last drop of cum straight down her throat."
            $ ClimaxController.manual_clarity_release(climax_type = "throat", the_person = the_girl)
            $ the_girl.cum_in_mouth()
            $ blowjob.redraw_scene(the_girl)
            "When you're completely finished she pulls back slightly so that she can breathe more easily."
        else:
            "You go to step back but [the_girl.possessive_title]'s grabs you by the cock with her hand."
            "[the_girl.possessive_title] lets you pull back until just the tip of your cock is in her mouth and she begins to stroke you."
            "You erupt in orgasm into her greedy mouth. Her expert mouth milks you with every spurt."
            $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = the_girl)
            $ the_girl.cum_in_mouth()
            $ blowjob.redraw_scene(the_girl)
            "[the_girl.possessive_title] begins moaning uncontrollably around your twitching cock when her cum addicted brain registers her cum dosage."
        $ the_girl.change_arousal(10)
        $ the_girl.call_dialogue("cum_mouth")
    else:
        "You take a step back, pulling your cock out of [the_girl.possessive_title]'s mouth with a satisfyingly wet pop, and take aim at her face."
        if (the_girl.get_opinion_score("drinking cum")) > (the_girl.get_opinion_score("cum facials")):
            "[the_girl.possessive_title] looks slightly disappointed."
        $ blowjob.current_modifier = None
        $ the_girl.draw_person(position = "kneeling1")
        if the_girl.has_cum_fetish():
            "[the_girl.title] takes a hold of your cock with one hand and starts to pump it."
            "She sticks out her tongue for you and holds still, eager to take your hot load."
            $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_girl)
            $ the_girl.cum_on_face()
            $ the_girl.draw_person(position = "kneeling1")
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face and into her open mouth. She shivers herself as your cum splashes over her."
            $ the_girl.change_arousal(10)

        elif the_girl.get_opinion_score("cum facials") < 0:
            "[the_girl.title] moves her head to the side so that your cum will miss her."
            menu:
                "Let her off":
                    $ ClimaxController.manual_clarity_release(climax_type = "air", the_person = the_girl)
                    "You cum onto the floor, missing [the_girl.possessive_title]."
                    $ the_girl.change_stats(love = -the_girl.get_opinion_score("cum facials"), happiness = -the_girl.get_opinion_score("cum facials"))
                "Pull her back":
                    $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_girl)
                    $ the_girl.cum_on_face()
                    $ the_girl.draw_person(position = "kneeling1")
                    $ the_girl.change_stats(love = the_girl.get_opinion_score("cum facials"), happiness = the_girl.get_opinion_score("cum facials"))
                    "You grab your cock with one hand and her head with the other. You hold her head in place as you use your other hand to pump your cum over [the_girl.possessive_title]'s face."
        elif (the_girl.effective_sluttiness() > 80 or the_girl.get_opinion_score("cum facials") > 0):
            "[the_girl.title] sticks out her tongue for you, holds still and looks you in the eye, eager to take your hot load."
            $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_girl)
            $ the_girl.cum_on_face()
            $ the_girl.draw_person(position = "kneeling1")
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face and into her open mouth. She makes sure to wait until you're completely finished as she maintains eye contact."
        elif the_girl.effective_sluttiness() > 60:
            "[the_girl.title] closes her eyes and waits patiently for you to cum."
            $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_girl)
            $ the_girl.cum_on_face()
            $ the_girl.draw_person(position = "kneeling1")
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face. She waits until she's sure you're finished, then opens one eye and looks up at you."
        else:
            "[the_girl.title] closes her eyes and turns away, presenting her cheek to you as you finally climax."
            $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_girl)
            $ the_girl.cum_on_face()
            $ the_girl.draw_person(position = "kneeling1")
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face. She flinches as the first splash of warm liquid lands on her cheek, but doesn't pull away entirely."
        if the_girl.has_face_cum():
            "You take a deep breath to steady yourself once you've finished cumming. [the_girl.title] looks up at you from her knees, face covered in your semen."
            $ the_girl.call_dialogue("cum_face")
            if the_girl.has_cum_fetish():
                "She closes her eyes and starts to gently massage your cum all over her face."
    return
