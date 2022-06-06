# Enhanced version of skull fuck orgasm by BadRabbit

init 5 python:
    config.label_overrides["orgasm_skull_fuck"] = "orgasm_skull_fuck_enhanced"
    skull_fuck.scenes.append("scene_skull_fuck_4_enhanced")

label scene_skull_fuck_4_enhanced(the_girl, the_location, the_object):
    if the_girl.sex_skills["Oral"] < 4:
        "[the_girl.title] is struggling to take the full length of your dick down her throat. She pulls off and pants for air."
        the_girl "Ah... I haven't got it quite right yet..."
        "Once she's caught her breath you slide your cock back into her mouth. Slowly sliding it deeper down her throat."
        "[the_girl.possessive_title] looks up to you, tears welling up in her eyes."
        if the_girl.sex_skills["Oral"] < 2:
            "She gags and gurgles as you bottom your cock out with each stroke, but manages to keep her arms down at her sides."
            mc.name "You're such a perfect flesh light, you know that? Fuck, this feels good."
            "Her inexperience stops her from making any progress. She lurches backwards, gagging and gasping for air."
            the_girl "Maybe I... Ah... Just need more practice..."
            "She shrugs, wipes some spit from her lips, and slips you back into her mouth."
        else:
            "She sputters as you throat her. Her spit bubbles around your shaft and drips down her chin, dropping onto her tits below."
            mc.name "That's it, gag on it you cock slut!"
            "You massage her throat with your hand and can feel the pressure on your own cock."
    else:
        "You stop fucking [the_girl.title]'s face for a second."
        mc.name "I wonder how long I could keep deep fucking your face, want to find out?"
        "She nods and you push your cock back into [the_girl.possessive_title]'s throat. Your balls tap against her chin."
        if the_girl.get_opinion_score("being submissive") > 0 and the_girl.get_opinion_score("giving blowjobs") > 0:
            "After a while, she pulls back, gagging and gasping for air."
            mc.name "That wasn't bad, but I think you could do better..."
            the_girl "I want to try again. [the_girl.mc_title], could you... hold me down so I can't pull off?"
            "You place a steady hand on the back of her head and pull her closer to you in response."
            mc.name "I'll help you do the best you could possibly do."
            $ the_girl.change_happiness(4+the_girl.get_opinion_score("giving blowjobs"))
            "She looks up to you, takes a few deep breaths through her nose and slides you all the way to the back of her throat."
            "[the_girl.possessive_title]'s throat spasms around your shaft as she starts to reach her limit. She closes her eyes and focuses hard on her task."
            menu:
                "Keep fucking her throat" if the_girl.obedience >= 110:
                    mc.name "Not yet, you can do better than that."
                    "You keep fucking [the_girl.title]'s throat deeply. She doesn't resist."
                    "After a few more seconds [the_girl.title] tries to pull off again, forcing you to pull her back in."
                    menu:
                        "Keep fucking her throat" if the_girl.obedience >= 120:
                            "A little more force and [the_girl.title] stays where she is. Her eyes are closed tight as she struggles to stay in control."
                            "More time passes. [the_girl.title] starts to squirm on her knees."
                            $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive"))
                            menu:
                                "Keep fucking her throat" if the_girl.obedience >= 130:
                                    mc.name "Don't give up now [the_girl.title], you're doing great."
                                    "You grab a handful of her hair to give you a better grip and don't let her go anywhere."
                                    "[the_girl.title]'s throat starts to rhythmically clench down on the shaft of your dick."
                                    $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive"))
                                    $ mc.change_arousal(1)
                                    "[the_girl.possessive_title]'s grabs at your legs, looking for support."
                                    menu:
                                        "Keep fucking her throat" if the_girl.obedience >= 150:
                                            mc.name "You're going to choke on this dick until I'm satisfied. Don't you dare pull off."
                                            "[the_girl.title] moans, her throat rumbling around your cock. Her eyes roll up as she tries to make eye contact with you."
                                            $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive"))
                                            "Several more long seconds pass. Pushed to her limit, [the_girl.title] pulls back harder and starts to tap on your leg."
                                            menu:
                                                "Choke her out" if the_girl.obedience >= 170:
                                                    mc.name "I said don't hold still. Not until I'm done with you."
                                                    "[the_girl.title] squirms and fidgets on her knees, but obeys your commands like a good girl."
                                                    "Little by little her movements slow down, her eyelids start to droop down over her rolled up eyes, and she slips into a half-conscious state."
                                                    $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive"))
                                                    "[the_girl.possessive_title]'s body doesn't stop reacting to you and your cock. Her throat rhythmically milking your shaft and she keeps moaning softly."
                                                    "Satisfied, you keep fucking [the_girl.title]'s face. She keeps sucking on you in her oxygen deprived stupor."
                                                    mc.name "That's enough [the_girl.title], you've done enough."
                                                    "You pull back entirely. She leaves your cock with a satisfying, wet pop followed by a huge gasp for air."
                                                    "It takes a few long moments until [the_girl.title] shakes her head and comes to her senses."
                                                    $ the_girl.increase_trance(show_dialogue = False)
                                                    the_girl "I... Oh my god... How long was I... Ah... Ah..."
                                                    $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive"))
                                                    "The thought of passing out on your cock seems to turn her on."
                                                    mc.name "Long enough, I think you've got a new personal best."
                                                    "[the_girl.possessive_title] bites her lip and moans to herself for a second."
                                                    the_girl "Thank you [the_girl.mc_title], you really pushed me there. Now... I can't make this all about me."
                                                    "She takes a deep breath, opens wide, waiting for you enter into her mouth. She holds her head still while you fuck her face and when you pull back, she takes a quick breath through her nose."
                                                    return #Don't do the rest of the scene because we have our special case here.

                                                "Choke her out\n{color=#ff0000}{size=18}Requires: 170 Obedience{/size}{/color} (disabled)" if the_girl.obedience < 170:
                                                    pass

                                                "Let her up":
                                                    pass
                                        "Keep fucking her throat\n{color=#ff0000}{size=18}Requires: 150 Obedience{/size}{/color} (disabled)" if the_girl.obedience < 150:
                                            pass

                                        "Let her up":
                                            pass
                                "Keep fucking her throat\n{color=#ff0000}{size=18}Requires: 130 Obedience{/size}{/color} (disabled)" if the_girl.obedience < 130:
                                    pass

                                "Let her up":
                                    pass

                        "Keep fucking her throat\n{color=#ff0000}{size=18}Requires: 120 Obedience{/size}{/color} (disabled)" if the_girl.obedience < 120:
                            pass

                        "Let her up":
                            pass

                "Keep fucking her throat\n{color=#ff0000}{size=18}Requires: 110 Obedience{/size}{/color} (disabled)" if the_girl.obedience < 110:
                    pass

                "Let her up":
                    pass

            "[the_girl.title] yanks her head back and off of your hard cock. She gasps for breath as soon as you're clear."
            the_girl "That... was... intense... Ah..."
            "It takes her a moment to catch her breath. You run your fingers through her hair while you let her recover."
            the_girl "That was a long time, but I think I could do better next time... Don't go so easy on me, okay?"
            "With that she leans forward and you start fucking her pretty face again."
        else:
            mc.name "Wow... that was pretty good, right?"
            $ the_girl.change_happiness(1+the_girl.get_opinion_score("giving blowjobs"))
            mc.name "Ah... Right, where was I..."
            "She only gurgles an answer while you push your cock back into her throat."
    return


label orgasm_skull_fuck_enhanced(the_girl, the_location, the_object):
    $ skull_fuck.current_modifier = "blowjob"
    $ skull_fuck.redraw_scene(the_girl)
    "You're happily fucking [the_girl.possessive_title]'s warm, wet throat when you notice her closing her eyes."
    "Her thighs quiver and her hands drop instinctively to her crotch. She begins to rub her pussy furiously, driving herself to orgasm."
    mc.name "Cum for me you dirty slut!"
    if the_girl.sex_skills["Oral"] > 3:
        "[the_girl.possessive_title] keeps her mouth wide open for you, even as she twitches and writhes through her climax."
        "You fuck her tight throat until she finishes twitching."
    else:
        "[the_girl.possessive_title] gags on your cock as you push her down onto it."
        "Her body tightens up as she climaxes, and you make sure to take advantage of her tight throat by fucking it hard."

    if the_girl.get_opinion_score("being submissive") > 0:
        if the_girl.sluttiness > the_girl.sluttiness and the_girl.sluttiness < skull_fuck.slut_cap:
            $ the_girl.change_slut(the_girl.get_opinion_score("being submissive")) #If she likes being submissive this makes her cum and become sluttier super hard.

        $ the_girl.change_obedience(2*the_girl.get_opinion_score("being submissive"))
        if the_girl.outfit.vagina_visible():
            "You can see that [the_girl.title]'s [the_girl.pubes_description] pussy is dripping wet as she cums."
        else:
            $ the_item = the_girl.outfit.get_lower_top_layer()
            if the_item.underwear:
                "[the_girl.title]'s dripping wet pussy has managed to soak through her underwear, leaving a wet mark on her [the_item.display_name]."
            else:
                "[the_girl.title] clenches her thighs together and rides out her orgasm."
            $ the_item = None
    else:
        $ the_girl.change_stats(happiness = -2, obedience = 1)

    $ skull_fuck.current_modifier = None
    $ skull_fuck.redraw_scene(the_girl)

    "Watching [the_girl.title]'s body writhe as she climaxes from your cock encourages you to go faster."
    "You clamp down on her head and slam yourself in and out of her throat."
    return
