init 5 python:
    against_wall.double_orgasm = "against_wall_double_orgasm"

label against_wall_double_orgasm(the_girl, the_location, the_object):
    "[the_girl.title]'s tight cunt draws you closer to your orgasm with each thrust. Her breathing is getting ragged as she nears her orgasm also."
    the_girl "[the_girl.mc_title], your cock is so good! Pin me to the wall and make me cum all over it!"
    "You speed up with her words of encouragement, passing the point of no return. You push her up against the [the_object.name] and lay into her."
    $ the_girl.call_dialogue("sex_responses_vaginal")
    mc.name "Fuck, I'm going to cum!"
    $ the_girl.call_dialogue("cum_pullout")

    $ climax_controller = ClimaxController(["Cum inside of her","pussy"], ["Cum on her stomach", "body"])
    $ the_choice = climax_controller.show_climax_menu()

    if the_choice == "Cum inside of her":
        if the_girl.wants_creampie():
            the_girl "Oh god yes, cum with me [the_girl.mc_title]!"
        if mc.condom:
            "You push forward as you climax, thrusting your cock as deep inside of [the_girl.possessive_title!l] as you can manage. She wraps her legs around you as she cums in unison."
            $ the_girl.call_dialogue("cum_condom")
            $ climax_controller.do_clarity_release(the_girl)
            "Once your climax has passed you keep [the_girl.title] pinned to the [the_object.name] for a little longer. When her aftershocks wind down, she slowly unwraps her legs."
            "You step back and pull out of [the_girl.possessive_title!l]. Your condom is ballooned out, filled with your seed."
            if the_girl.has_cum_fetish():
                if renpy.random.randint(0, 1) == 1: # random choice of cum fetish dialog
                    $ the_girl.discover_opinion("drinking cum")
                    "[the_girl.possessive_title] reaches over for your cock. With delicate fingers she slides the condom off of you, pinching it off so your cum doesn't spill out."
                    the_girl "It would be a shame to waste all of this, right?"
                    "She smiles and brings the condom to her mouth. She tips the bottom up and drains it into her mouth."
                    $ the_girl.change_slut(the_girl.get_opinion_score("drinking cum"))
                    "[the_girl.possessive_title] moans as she pours your cum into her mouth."
                    $ the_girl.cum_in_mouth()
                    $ against_wall.redraw_scene(the_girl)
                    "She shudders at the sensation. It is apparent to you, if it was not before, that [the_girl.possessive_title!l] is literally addicted to your cum."
                else:
                    $ the_girl.discover_opinion("cum facials")
                    "[the_girl.possessive_title] reaches over for your cock. With delicate fingers she slides the condom off of you, pinching it off so your cum doesn't spill out."
                    the_girl "It would be a shame to waste all of this, right?"
                    $ the_girl.cum_on_face()
                    $ against_wall.redraw_scene(the_girl)
                    "She smiles and tips the contents of the condom out onto one of her hands. She tosses the condom aside and rubs her palms together."
                    "She takes a deep breath and closes her eyes. She reaches to her cheeks and starts to smear your cum over her face."
                    the_girl "Mmmmm. So good."
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
                "[the_girl.possessive_title] moans in ecstasy as the first wave of your cum floods her [the_girl.pubes_description] pussy."
                "Her body goes rigid as your cum pumps into her. Goosebumps erupt all over her body and her pupils dilate as her brain registers her creampie."
                "Having your cum inside of her heightens her orgasm as her fetish for your cum is fulfilled."
            else:
                "You push forward as you finally climax, thrusting your cock as deep inside of [the_girl.possessive_title!l] as you can manage."
                "She clings to you helplessly as she cums with you in unison."
            $ the_girl.call_dialogue("cum_vagina")
            $ the_girl.cum_in_vagina()
            $ climax_controller.do_clarity_release(the_girl)
            $ against_wall.redraw_scene(the_girl)
            "You wait until your orgasm has passed, then step back and sigh happily. [the_girl.title] stays leaning against the [the_object.name] for a few seconds as your semen drips down her leg."

    elif the_choice == "Cum on her stomach":
        if mc.condom == False and the_girl.wants_creampie() and the_girl.obedience <200 :
            "Before you get the chance to pull back and out, [the_girl.title] lifts both her feet up and wraps her legs around you, locking her ankles together."
            $ wordchoice = renpy.random.choice(["Oh God", "Oh yes", "Oh.. OH! Yes"])
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
                "[the_girl.possessive_title] pulls your body close to hers. She cries out as she orgasms, her slick cunt rippling all around you."
                "[the_girl.possessive_title]'s quivering hole feels too good, you can't hold it back anymore."
            else:
                "She humps against you a few times to make sure that you cum deep inside her. She cries out as she orgasms, her slick cunt rippling all around you."
            $ the_girl.call_dialogue("cum_vagina")
            $ the_girl.cum_in_vagina()
            $ climax_controller.do_clarity_release(the_girl)
            $ against_wall.redraw_scene(the_girl)
            if the_girl.has_cum_fetish():
                "[the_girl.possessive_title] moans in ecstasy as the first wave of your cum floods her [the_girl.pubes_description] pussy."
                "Her body goes rigid as your cum pumps into her. Goosebumps erupt all over her body and her pupils dilate as her brain registers her creampie."
                "Having your cum inside of her heightens her orgasm as her fetish for you cum is fulfilled."
                the_girl "Oh.. OH! Yes [the_girl.mc_title]! Pump it deep! You were meant to cum inside me!"
            "When you finish, [the_girl.title] leaves her legs wrapped around you as she has a couple aftershocks. Her pussy twitches with each one."
            "She slowly opens her eyes and looks at you."
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
                    the_girl "I'm sorry... I don't know what came over me... I just couldn't let you pull out!"
                else:
                    the_girl "I hope you enjoy paying child support, [the_girl.mc_title]."

            $ del wordchoice
            $ del wordchoice2
        else:
            $ the_girl.cum_on_stomach()
            $ climax_controller.do_clarity_release(the_girl)
            $ against_wall.redraw_scene(the_girl)
            if mc.condom:
                "You pull out of [the_girl.possessive_title!l] at the last moment and step back. You whip your condom off and blow your load over her stomach while she watches."
            else:
                "You pull out of [the_girl.possessive_title!l] at the last moment and step back. You stroke yourself off and blow your load over her stomach while she watches."
            "As your cum erupts, she reaches down with her hand and rapidly strokes her clit. She throws her head back and begins to orgasm together with you."
            the_girl "Ohhhh yes! Shower me with your hot cum!"
            "You sigh contentedly and relax for a moment, enjoying the sight of [the_girl.title] covered in your semen."
            if the_girl.has_cum_fetish():
                "[the_girl.possessive_title]'s body goes rigid and goosebumps erupt all over her body as her brain registers your cum on her."
                "[the_girl.possessive_title] revels in bliss as she mindlessly rubs in your cum and licks of her fingers to heighten her orgasm."
                "She truly is addicted to your cum."
            elif the_girl.effective_sluttiness() > 120:
                the_girl "What a waste, that would have felt so much better inside of me..."
                "She reaches down and runs a finger through the puddles of cum you've put on her, then licks her finger clean and winks at you."
            else:
                the_girl "Oh wow, there's so much of it. It feels so warm..."

    $ post_double_orgasm(the_girl)
    return
