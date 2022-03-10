init 5 python:
    piledriver.double_orgasm = "piledriver_double_orgasm"

label piledriver_double_orgasm(the_girl, the_location, the_object):
    "[the_girl.title] is moaning with every thrust into her cunt. Her breathing is getting ragged and more desperate."
    the_girl "It's so good... I'm gonna cum!"
    "Pinning [the_girl.title] down to the [the_object.name] as you fuck her is really turning you on. You feel yourself approaching the point of no return."
    mc.name "Me too!"
    $ the_girl.call_dialogue("cum_pullout")
    if the_girl.wants_creampie():
        the_girl "Do it! I want you to cum with me!"

    $ climax_controller = ClimaxController(["Cum inside of her","pussy"], ["Cum on her face", "face"])
    $ the_choice = climax_controller.show_climax_menu()

    if the_choice == "Cum inside of her":
        "You use your full weight to push your cock deep inside of [the_girl.possessive_title]'s cunt as you climax. She is moaning loudly as she cums together with you at the same time."
        $ climax_controller.do_clarity_release(the_girl)
        if mc.condom:
            $ the_girl.call_dialogue("cum_condom")
            "When you finish, you leave yourself deep inside her for a few moments while she has a few aftershocks."
            "You pull off of [the_girl.possessive_title]."
            "Your condom is ballooned with your seed, hanging off your cock to one side."
            if the_girl.has_cum_fetish():
                if renpy.random.randint(0, 1) == 1: # random choice of cum fetish dialog
                    "[the_girl.possessive_title] reaches up for your cock. With delicate fingers she slides the condom off of you, pinching it off so your cum doesn't spill out."
                    the_girl "It would be a shame to waste all of this, right?"
                    "She smiles and brings the condom to her mouth. She tips the bottom up and drains it into her mouth."
                    $ the_girl.change_slut(the_girl.get_opinion_score("drinking cum"))
                    "[the_girl.possessive_title] moans as she pours your cum into her mouth."
                    $ the_girl.cum_in_mouth()
                    "She shudders at the sensation. It is apparent to you, if it was not before, that [the_girl.possessive_title] is literally addicted to your cum."
                else:
                    "[the_girl.possessive_title] reaches up for your cock. With delicate fingers she slides the condom off of you, pinching it off so your cum doesn't spill out."
                    the_girl "It would be a shame to waste all of this, right?"
                    "She smiles and tips the contents of the condom out onto one of her hands. She tosses the condom aside and rubs her palms together."
                    "She takes a deep breath and closes her eyes. She reaches to her cheeks and starts to smear your cum over her face."
                    the_girl "Mmmmm. So good."
                    $ the_girl.cum_on_face()
            elif the_girl.get_opinion_score("drinking cum") > 0 and the_girl.effective_sluttiness() > 50:
                $ the_girl.discover_opinion("drinking cum")
                "[the_girl.possessive_title] reaches up for your cock. With delicate fingers she slides the condom off of you, pinching it off so your cum doesn't spill out."
                the_girl "It would be a shame to waste all of this, right?"
                "She smiles and brings the condom to her mouth. She tips the bottom up and drains it into her mouth."
                $ the_girl.change_slut(the_girl.get_opinion_score("drinking cum"))
            else:
                "[the_girl.possessive_title] reaches up for your cock, removes the condom, and ties the end in a knot for you."
                the_girl "Look at all that cum. Well done."
        else:
            $ the_girl.call_dialogue("cum_vagina")
            $ the_girl.cum_in_vagina()
            $ missionary.redraw_scene(the_girl)
            if the_girl.has_cum_fetish():
                "[the_girl.possessive_title] moans as the first wave of your cum floods her [the_girl.pubes_description] pussy."
                the_girl "Oh fuck oh yes!!!"
                "Her body convulses as she begins to cum at the same time. She wraps her legs around you and clings to you as orgasm hits her as you cum inside of her."
                "[the_girl.possessive_title] revels in having her cum fetish fulfilled."
            "When you finish, you wait a few minutes while [the_girl.title] has a few aftershocks. Her pussy grasps your cock with each one."
            "You slowly pull out of [the_girl.possessive_title]."

    elif the_choice == "Cum on her face":
        $ the_girl.cum_on_face()
        $ missionary.redraw_scene(the_girl)
        $ climax_controller.do_clarity_release(the_girl)
        if mc.condom:
            "You pull out at the last moment and grab your cock. You whip off your condom and stroke yourself off, blowing your load over [the_girl.title]'s face."
        else:
            "You pull out at the last moment and grab your cock. You stroke yourself off, blowing your load over [the_girl.title]'s face."
        "[the_girl.title] reaches down and starts rubbing circles around her clit as you start to blow your load. She is cumming at the same time."
        the_girl "Ohhhh yes! Shower me with your hot cum!"
        if the_girl.has_cum_fetish():
            "[the_girl.possessive_title]'s body goes rigid as your cum splashes onto her skin. Goosebumps erupt all over her body as her brain registers your cum on her."
            "[the_girl.possessive_title] revels in bliss as your dick sprays jet after jet of seed across her. Your cum on her skin heightens her orgasm."
            "She truly is addicted to your cum."
        else:
            the_girl "Ah... Good job... Ah..."
            "You sit back and sigh contentedly, enjoying the sight of [the_girl.possessive_title]'s body covered in your semen."

    $ post_double_orgasm(the_girl) #We have to put this at the end of each double orgasm scene because return doesn't return to where you think it will.
    return
