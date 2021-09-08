init 5 python:
    missionary.outro = "outro_missionary_enhanced"
    against_wall.outro = "outro_against_wall_enhanced"

label outro_missionary_enhanced(the_girl, the_location, the_object):
    "You get to hear every little gasp and moan from [the_girl.title] as you're pressed up against her. Combined with the feeling of fucking her pussy it's not long before you're pushed past the point of no return."
    mc.name "I'm going to cum!"
    $ the_girl.call_dialogue("cum_pullout")

    $ climax_controller = ClimaxController(["Cum inside of her","pussy"], ["Cum outside", "body"])
    $ the_choice = climax_controller.show_climax_menu()

    if the_choice == "Cum inside of her":
        "You use your full weight to push your cock deep inside of [the_girl.possessive_title]'s cunt as you climax. She gasps and claws lightly at your back as you pump your seed into her."

        if mc.condom:
            $ the_girl.call_dialogue("cum_condom")
            $ climax_controller.do_clarity_release(the_girl)
            "You take a moment to catch your breath, then roll off of [the_girl.possessive_title] and lie beside her."
            "Your condom is ballooned with your seed, hanging off your cock to one side."
            if the_girl.has_cum_fetish():
                if renpy.random.randint(0, 1) == 1: # random choice of cum fetish dialog
                    $ the_girl.discover_opinion("drinking cum")
                    "[the_girl.possessive_title] reaches over for your cock. With delicate fingers she slides the condom off of you, pinching it off so your cum doesn't spill out."
                    the_girl "It would be a shame to waste all of this, right?"
                    "She smiles and brings the condom to her mouth. She tips the bottom up and drains it into her mouth."
                    $ the_girl.change_slut(the_girl.get_opinion_score("drinking cum"))
                    "[the_girl.possessive_title] moans as she pours your cum into her mouth."
                    $ the_girl.cum_in_mouth()
                    "She shudders at the sensation. It is apparent to you, if it was not before, that [the_girl.possessive_title] is literally addicted to your cum."
                else:
                    $ the_girl.discover_opinion("cum facials")
                    "[the_girl.possessive_title] reaches over for your cock. With delicate fingers she slides the condom off of you, pinching it off so your cum doesn't spill out."
                    the_girl "It would be a shame to waste all of this, right?"
                    "She smiles and tips the contents of the condom out onto one of her hands. She tosses the condom aside and rubs her palms together."
                    $ the_girl.cum_on_face()
                    "She takes a deep breath and closes her eyes. She reaches to her cheeks and starts to smear your cum over her face."
                    the_girl "Mmmmm. So good."
            elif the_girl.get_opinion_score("drinking cum") > 0 and the_girl.effective_sluttiness() > 50:
                $ the_girl.discover_opinion("drinking cum")
                "[the_girl.possessive_title] reaches over for your cock. With delicate fingers she slides the condom off of you, pinching it off so your cum doesn't spill out."
                the_girl "It would be a shame to waste all of this, right?"
                "She smiles and brings the condom to her mouth. She tips the bottom up and drains it into her mouth."
                $ the_girl.change_slut(the_girl.get_opinion_score("drinking cum"))
            else:
                "[the_girl.possessive_title] reaches over for your cock, removes the condom, and ties the end in a knot for you."
                the_girl "Look at all that cum. Well done."
        else:
            $ the_girl.call_dialogue("cum_vagina")
            $ the_girl.cum_in_vagina()
            $ climax_controller.do_clarity_release(the_girl)
            $ missionary.redraw_scene(the_girl)
            if the_girl.has_cum_fetish():
                "[the_girl.possessive_title] moans as the first wave of your cum floods her [the_girl.pubes_description] pussy."
                "Her body goes rigid as your cum pumps into her. Goosebumps erupt all over her body and her pupils dilate as her brain registers her creampie."
                the_girl "Oh.. OH! Yes [the_girl.mc_title]! Pump it deep! You were meant to cum inside me!"
                "[the_girl.possessive_title] revels in having her cum fetish fulfilled."
            "You take a moment to catch your breath, then roll off of [the_girl.possessive_title] and lie beside her."

    elif the_choice == "Cum outside":
        if mc.condom == False and (the_girl.has_cum_fetish() or (the_girl.wants_creampie() and the_girl.obedience <150 and the_girl.get_opinion_score("taking control") > -1 and the_girl.get_opinion_score("creampies") > 0)):
            "Before you get the chance to pull back and out, [the_girl.title] lifts both her feet up and wraps her legs around you, locking her ankles together."
            $ wordchoice = renpy.random.choice(["Oh God,", "Oh yes", "Oh.. OH! Yes "])
            $ wordchoice2 = renpy.random.choice(["Cum for me!", "Cum inside!", "Cum for me!", "Cum in me!", "Pump it deep!", ""])
            if the_girl.love < 0:
                "Where do think you're going, [the_girl.mc_title]?"
            else:
                the_girl "[wordchoice], [the_girl.mc_title]! [wordchoice2]"
            "The strength of her legs prevents you from pulling out."
            $ ran_num = renpy.random.randint(0,1)
            if ran_num == 0:
                mc.name "What the fuck!"
            if the_girl.sex_skills["Vaginal"] > 3:
                "[the_girl.possessive_title] pulls your body close to hers, burying your cock as deep as she can and milks it with the muscles inside her pussy."
                "[the_girl.possessive_title]'s quivering hole feels too good, you can't hold it back anymore."
            else:
                "She humps against you a few times to make sure that you cum deep inside her."
            $ the_girl.call_dialogue("cum_vagina")
            $ the_girl.cum_in_vagina()
            $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_girl)
            $ missionary.redraw_scene(the_girl)
            if the_girl.has_cum_fetish():
                "[the_girl.possessive_title] moans as the first wave of your cum floods her [the_girl.pubes_description] pussy."
                "Her body goes rigid as your cum pumps into her. Goosebumps erupt all over her body and her pupils dilate as her brain registers her creampie."
                the_girl "Oh.. OH! Yes [the_girl.mc_title]! Pump it deep! You were meant to cum inside me!"
                "[the_girl.possessive_title] revels in having her cum fetish fulfilled."
            $ wordchoice = renpy.random.choice(['Relax', "Don't panic", 'Stay calm', 'Chill', "It's okay"])
            $ wordchoice2 = renpy.random.choice(['the pill', 'birth control'])
            if the_girl.knows_pregnant():# The personality reactions but should it not be True instead of False?
                the_girl "[wordchoice], [the_girl.mc_title]. I'm already pregnant remember?"
            elif the_girl.on_birth_control:
                the_girl "[wordchoice], [the_girl.mc_title]. I'm on [wordchoice2]."
            elif the_girl.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_girl.relationship)
                the_girl "[wordchoice], [the_girl.mc_title]. If anything happens I'll tell my [so_title] it's his."
            else:
                if the_girl.love >59:
                    the_girl "I love you, [the_girl.mc_title]. We should make a baby together."
                elif the_girl.love >0:
                    pass
                else:
                    the_girl "I hope you enjoy paying child support, [the_girl.mc_title]."
        else:
            $ the_girl.cum_on_stomach()
            $ missionary.redraw_scene(the_girl)
            $ climax_controller.do_clarity_release(the_girl)
            if pregnant_role in the_girl.special_role and the_girl.event_triggers_dict.get("preg_transform_day",day) < day:
                if mc.condom:
                    "You pull out at the last moment and grab your cock. You whip off your condom and stroke yourself off, blowing your load over [the_girl.title]'s pregnancy bump."
                else:
                    "You pull out at the last moment and grab your cock. You kneel and stroke yourself off, blowing your load over [the_girl.title]'s pregnancy bump."
            else:
                if mc.condom:
                    "You pull out at the last moment and grab your cock. You whip off your condom and stroke yourself off, blowing your load over [the_girl.title]'s stomach."
                else:
                    "You pull out at the last moment and grab your cock. You kneel and stroke yourself off, blowing your load over [the_girl.title]'s stomach."
            if the_girl.has_cum_fetish():
                "[the_girl.possessive_title]'s body goes rigid as your cum splashes onto her skin. Goosebumps erupt all over her body as her brain registers your cum on her."
                "[the_girl.possessive_title] revels in bliss as your dick sprays jet after jet of seed across her. She moans lewdly."
                "She truly is addicted to your cum."
            else:
                the_girl "Ah... Good job... Ah..."
                "You sit back and sigh contentedly, enjoying the sight of [the_girl.possessive_title]'s body covered in your semen."
    return

label outro_against_wall_enhanced(the_girl, the_location, the_object):
    "[the_girl.title]'s tight cunt draws you closer to your orgasm with each thrust. You speed up as you pass the point of no return, pushing her up against the [the_object.name] and laying into her."
    $ the_girl.call_dialogue("sex_responses_vaginal")
    mc.name "Fuck, I'm going to cum!"
    $ the_girl.call_dialogue("cum_pullout")

    $ climax_controller = ClimaxController(["Cum inside of her","pussy"], ["Cum on her stomach", "body"])
    $ the_choice = climax_controller.show_climax_menu()

    if the_choice == "Cum inside of her":
        if mc.condom:
            "You push forward as you climax, thrusting your cock as deep inside of [the_girl.possessive_title] as you can manage. She pants quietly as you pulse your hot cum into the condom you're wearing."
            $ the_girl.call_dialogue("cum_condom")
            $ climax_controller.do_clarity_release(the_girl)
            "Once your climax has passed you step back and pull your cock out from [the_girl.title]. Your condom is ballooned out, filled with your seed."
            if the_girl.has_cum_fetish():
                if renpy.random.randint(0, 1) == 1: # random choice of cum fetish dialog
                    $ the_girl.discover_opinion("drinking cum")
                    "[the_girl.possessive_title] reaches over for your cock. With delicate fingers she slides the condom off of you, pinching it off so your cum doesn't spill out."
                    the_girl "It would be a shame to waste all of this, right?"
                    "She smiles and brings the condom to her mouth. She tips the bottom up and drains it into her mouth."
                    $ the_girl.change_slut(the_girl.get_opinion_score("drinking cum"))
                    "[the_girl.possessive_title] moans as she pours your cum into her mouth."
                    $ the_girl.cum_in_mouth()
                    "She shudders at the sensation. It is apparent to you, if it was not before, that [the_girl.possessive_title] is literally addicted to your cum."
                else:
                    $ the_girl.discover_opinion("cum facials")
                    "[the_girl.possessive_title] reaches over for your cock. With delicate fingers she slides the condom off of you, pinching it off so your cum doesn't spill out."
                    the_girl "It would be a shame to waste all of this, right?"
                    "She smiles and tips the contents of the condom out onto one of her hands. She tosses the condom aside and rubs her palms together."
                    "She takes a deep breath and closes her eyes. She reaches to her cheeks and starts to smear your cum over her face."
                    the_girl "Mmmmm. So good."
                    $ the_girl.cum_on_face()
            elif the_girl.get_opinion_score("drinking cum") > 0 and the_girl.effective_sluttiness() > 50:
                $ the_girl.discover_opinion("drinking cum")
                "[the_girl.possessive_title] reaches for your cock. With delicate fingers she slides the condom off of you."
                the_girl "It would be a shame to waste all of this, right?"
                "She smiles and brings the condom to her mouth. She tips the bottom up and drains it into her mouth."
                $ the_girl.change_slut(the_girl.get_opinion_score("drinking cum"))
            else:
                "[the_girl.possessive_title] reaches for your cock, removes the condom, and ties the end in a knot."
                the_girl "Look at all that cum. Well done."
        else:
            if the_girl.has_cum_fetish():
                "[the_girl.possessive_title] moans as the first wave of your cum floods her [the_girl.pubes_description] pussy."
                "Her body goes rigid as your cum pumps into her. Goosebumps erupt all over her body and her pupils dilate as her brain registers her creampie."
                "[the_girl.possessive_title] revels in having her cum fetish fulfilled."
            else:
                "You push forward as you finally climax, thrusting your cock as deep inside of [the_girl.possessive_title] as you can manage. She gasps softly each time your dick pulses and shoots hot cum into her."
            $ the_girl.call_dialogue("cum_vagina")
            $ the_girl.cum_in_vagina()
            $ against_wall.redraw_scene(the_girl)
            $ climax_controller.do_clarity_release(the_girl)
            "You wait until your orgasm has passed, then step back and sigh happily. [the_girl.title] stays leaning against the [the_object.name] for a few seconds as your semen drips down her leg."

    elif the_choice == "Cum on her stomach":
        if mc.condom == False and (the_girl.has_cum_fetish() or (the_girl.wants_creampie() and the_girl.obedience <150 and the_girl.get_opinion_score("taking control") > -1 and the_girl.get_opinion_score("creampies") > 0)):
            "Before you get the chance to pull back and out, [the_girl.title] lifts both her feet up and wraps her legs around you, locking her ankles together."
            $ wordchoice = renpy.random.choice(["Oh God,", "Oh yes", "Oh.. OH! Yes "])
            $ wordchoice2 = renpy.random.choice(["Cum for me!", "Cum inside!", "Cum for me!", "Cum in me!", "Pump it deep!", ""])
            if the_girl.love < 0:
                "Where do think you're going, [the_girl.mc_title]?"
            else:
                the_girl "[wordchoice], [the_girl.mc_title]! [wordchoice2]"
            "The strength of her legs prevents you from pulling out."
            $ ran_num = renpy.random.randint(0,1)
            if ran_num == 0:
                mc.name "What the fuck!"
            if the_girl.sex_skills["Vaginal"] > 3:
                "[the_girl.possessive_title] pulls your body close to hers, burying your cock as deep as she can and milks it with the muscles inside her pussy."
                "[the_girl.possessive_title]'s quivering hole feels too good, you can't hold it back anymore."
            else:
                "She humps against you a few times to make sure that you cum deep inside her."
            $ the_girl.call_dialogue("cum_vagina")
            $ the_girl.cum_in_vagina()
            $ against_wall.redraw_scene(the_girl)
            $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_girl)
            if the_girl.has_cum_fetish():
                "[the_girl.possessive_title] moans as the first wave of your cum floods her [the_girl.pubes_description] pussy."
                "Her body goes rigid as your cum pumps into her. Goosebumps erupt all over her body and her pupils dilate as her brain registers her creampie."
                "She throws her head back in pleasure."
                the_girl "Oh.. OH! Yes [the_girl.mc_title]! Pump it deep! You were meant to cum inside me!"
                "[the_girl.possessive_title] revels in having her cum fetish fulfilled."
            $ wordchoice = renpy.random.choice(['Relax', "Don't panic", 'Stay calm', 'Chill', "It's okay"])
            $ wordchoice2 = renpy.random.choice(['the pill', 'birth control'])
            if the_girl.knows_pregnant():# The personality reactions but should it not be True instead of False?
                the_girl "[wordchoice], [the_girl.mc_title]. I'm already pregnant remember?"
            elif the_girl.on_birth_control:
                the_girl "[wordchoice], [the_girl.mc_title]. I'm on [wordchoice2]."
            elif the_girl.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_girl.relationship)
                the_girl "[wordchoice], [the_girl.mc_title]. If anything happens I'll tell my [so_title] it's his."
            else:
                if the_girl.love >59:
                    the_girl "I love you, [the_girl.mc_title]. We should make a baby together."
                elif the_girl.love >0:
                    pass
                else:
                    the_girl "I hope you enjoy paying child support, [the_girl.mc_title]."
        else:
            $ the_girl.cum_on_stomach()
            $ against_wall.redraw_scene(the_girl)
            $ climax_controller.do_clarity_release(the_girl)
            if mc.condom:
                "You pull out of [the_girl.possessive_title] at the last moment and step back. You whip your condom off and blow your load over her stomach while she watches."
            else:
                "You pull out of [the_girl.possessive_title] at the last moment and step back. You stroke yourself off and blow your load over her stomach while she watches."
            if the_girl.effective_sluttiness() > 120:
                the_girl "What a waste, that would have felt so much better inside of me..."
                "She reaches down and runs a finger through the puddles of cum you've put on her, then licks her finger clean and winks at you."
            else:
                the_girl "Oh wow, there's so much of it. It feels so warm..."
            "You sigh contentedly and relax for a moment, enjoying the sight of [the_girl.title] covered in your semen."
    return
