init 5 python:
    doggy.double_orgasm = "doggy_double_orgasm"

label doggy_double_orgasm(the_girl, the_location, the_object):
    "[the_girl.title] lifts one leg off [the_object.name] as you fuck her hard, in the final stretch before your orgasm."
    the_girl "Oh god it's so good! Oh [the_girl.mc_title] I'm gonna cum!"
    "Hearing her call out your name is pushing you over the edge. You are about to cum too."
    mc.name "I'm cumming too!"
    $ the_girl.call_dialogue("cum_pullout")
    menu:
        "Cum inside of her":
            if stealth_orgasm:  #You sly dog
                "You know you should probably pull out after pulling the condom off, but you can't. You pull back on [the_girl.possessive_title]'s hips and drive your cock deep inside of her as you cum."
                the_girl "Oh god, you are cumming so hard, I swear I can feel it splashing inside of me!"
                "You cum in unison with [the_girl.title]."
                $ the_girl.cum_in_vagina()
                $ doggy.redraw_scene(the_girl)
                $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_girl)
                "After you finish, you leave your cock deep inside her, enjoying her hole quivering with each aftershock. A few drops of your cum start to drip out of her."
                "[the_girl.title] reaches between her legs and feels it, realizing you just finished inside of her."
                if the_girl.has_role(prostitute_role):
                    if the_girl.on_birth_control:
                        the_girl "What the FUCK? You took the condom off? And then came inside me!?! I know I'm just a working girl, but you can't treat me like this."
                    else:
                        the_girl "What? You took the condom off? And then came inside me!?! Fuck, I could get pregnant, not all working girls take birth control, you asshole!"
                    $ the_girl.change_happiness(-5)
                    $ the_girl.change_obedience(3)
                    $ the_girl.change_love(-5)          #She loses trust
                elif the_girl.wants_creampie():         #She likes creampies...
                    the_girl "Wait... that's... you took the condom off, didn't you? Oh fuck that's why it felt so good!"
                    $ the_girl.discover_opinion("creampies")
                    if the_girl.on_birth_control:
                        the_girl "Oh god that's so hot. I love feeling cum deep inside me."
                    else:
                        the_girl "Oh god that's so hot. You could knock me up you know? Next time be more careful!"
                    $ the_girl.change_happiness(2)
                    $ the_girl.change_obedience(3)
                elif the_girl.get_opinion_score("bareback sex") > 0:  #She is slutty enough she doesn't mind the cream filling
                    the_girl "Oh my god you took the condom off? You know you can cum inside me anytime you want, no need to be stealthy about it!"
                    $ the_girl.change_obedience(3)
                else:                                                   #She gets pissed
                    if the_girl.on_birth_control:
                        the_girl "What the FUCK? You took the condom off? And then came inside me!?! You asshole!"
                    else:
                        the_girl "What the FUCK? You took the condom off? And then came inside me!?! I could get pregnant asshole!"
                    $ the_girl.change_happiness(-5)
                    $ the_girl.change_obedience(3)
                    $ the_girl.change_love(-5)          #She loses trust
                    "You planted your seed inside of [the_girl.possessive_title], but it is clear she isn't happy about it."
                "You slowly pull out of [the_girl.title]. Your cum is dripping down her leg as you sit back."
            elif mc.condom:
                "You pull back on [the_girl.possessive_title]'s hips and drive your cock deep inside of her as you cum. She moans as you dump your load into her, barely contained by your condom."
                the_girl "Oh god cum with me!"
                "You can feel her pussy quivering all around you as you cum in unison. Her body is milking your cum, with only a thin layer of latex keeping it from spilling deep inside her."
                "After you finish, you leave your cock deep inside her, enjoying her hole quivering with each aftershock"
                "You pull out and sit back. The condom is ballooned and sagging with the weight of your seed."
                if the_girl.get_opinion_score("drinking cum") > 0 and the_girl.sluttiness > 50:
                    $ the_girl.discover_opinion("drinking cum")
                    "[the_girl.possessive_title] turns around and reaches for your cock. With delicate fingers she slides the condom off of you."
                    the_girl "It would be a shame to waste all of this, right?"
                    "She winks and brings the condom to her mouth. She tips the bottom up and drains it into her mouth."
                    $ the_girl.change_slut_temp(the_girl.get_opinion_score("drinking cum"))
                else:
                    "[the_girl.possessive_title] turns around and reaches for your cock. She removes the condom and ties the end in a knot."
                    the_girl "Look at all that cum. Well done."
                "You sigh contentedly and enjoy the post-orgasm feeling of relaxation."
            else:
                "You pull back on [the_girl.possessive_title]'s hips and drive your cock deep inside of her as you cum. She moans in time with each new shot of hot semen inside of her."
                the_girl "Oh god cum with me!"
                "You can feel her pussy quivering all around you as you cum in unison. Her body is milking your cum, you swear it feels like she's pulling it deep into her womb."
                "After you finish, you leave your cock deep inside her, enjoying her hole quivering with each aftershock"
                $ the_girl.call_dialogue("cum_vagina")
                $ the_girl.cum_in_vagina()
                $ doggy.redraw_scene(the_girl)
                $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_girl)
                "You slowly pull out of [the_girl.possessive_title]. Your cum is dripping down her leg as you sit back."

        "Cum on her ass":
            if mc.condom:
                "You pull out of [the_girl.title] at the last moment. You whip your condom off and stroke your cock as you blow your load over her ass."
            else:
                "You pull out of [the_girl.title] at the last moment, stroking your shaft as you blow your load over her ass."
            "She reaches down and starts to play with herself, bringing herself to orgasm in unison with you."
            the_girl "Oh god I'm cumming!"
            $ the_girl.cum_on_ass()
            $ doggy.redraw_scene(the_girl)
            $ ClimaxController.manual_clarity_release(climax_type = "body", the_person = the_girl)
            "You sit back and sigh contentedly, enjoying the sight of [the_girl.title] covered in your semen."
            if the_girl.sluttiness > 120:
                the_girl "What a waste, you should have put that inside of me."
                "She reaches back and runs a finger through the puddles of cum you've put on her, then licks her finger clean."
            else:
                the_girl "Oh wow, there's so much of it..."

    $ stealth_orgasm = False
    $ post_double_orgasm(the_girl)
    return
