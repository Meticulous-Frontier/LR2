init 5 python:
    SB_doggy_standing.double_orgasm = "SB_doggy_standing_double_orgasm"

label SB_doggy_standing_double_orgasm(the_girl, the_location, the_object):
    "[the_girl.title]'s back is arched and she is moaning non stop. Her ass quakes with every rapid thrust."
    the_girl "Oh god its so good! Oh [the_girl.mc_title] I'm gonna cum!"
    "Hearing her call out your name is pushing you over the edge. You are about to cum too."
    mc.name "I'm cumming too!"
    $ the_girl.call_dialogue("cum_pullout")
    menu:
        "Cum inside of her":
            "[the_girl.possessive_title]'s drenched cunt is just too good. You decide to cum inside it."
            if mc.condom:
                "You pull back on [the_girl.possessive_title]'s hips and drive your cock deep inside of her as you cum. She moans when she feels you filling the condom deep inside of her."
                $ the_girl.call_dialogue("cum_condom")
                "Her cunt quivers as she joins you in orgasm. Her body goes rigid but you can feel the delicious pulsing as it feels like her body is trying to suck the condom off."
                "You wait until her orgasm has passed completely, then pull out and sit back. Your condom is bulged on the end where it is filled with your seed."
                if (the_girl.get_opinion_score("drinking cum") > 0 and the_girl.sluttiness > 50) or the_girl.has_cum_fetish():
                    $ the_girl.discover_opinion("drinking cum")
                    "[the_girl.possessive_title] turns around and reaches for your cock. With delicate fingers she slides the condom off of you."
                    the_girl.char "It would be a shame to waste all of this, right?"
                    "She winks and brings the condom to her mouth. Squeezing all your cum right into her mouth."
                    $ the_girl.change_slut_temp(the_girl.get_opinion_score("drinking cum"))
                else:
                    "[the_girl.possessive_title] turns around and reaches for your cock. She removes the condom and ties the end in a knot, before throwing it away."
                "You sigh contentedly and enjoy the post-orgasm feeling of relaxation."
            else:
                "You pull back on [the_girl.possessive_title]'s hips and drive your cock as deep inside of her as you cum. She moans in time with each new shot of hot semen inside of her."

                if the_girl.get_opinion_score("creampies") > 0 or the_girl.wants_creampie():
                    the_girl.char  "Yes! Fill me with your cum!"
                "You feel her pussy convulsing around your dick as she also starts to orgasm."
                $ the_girl.cum_in_vagina()
                $ SB_doggy_standing.redraw_scene(the_girl)
                if the_girl.has_cum_fetish() or the_girl.has_breeding_fetish():
                    "[the_girl.possessive_title]'s body goes rigid as your cum pours into her pussy. Goosebumps erupt all over her body as her brain registers her creampie."
                    the_girl.char "Oh.. OH! Yes [the_girl.mc_title]! Pump it deep! I was made to take your cum inside me!"
                    "[the_girl.possessive_title] revels in having her fetish fulfilled."
                if the_girl.get_opinion_score("bareback sex") > 0:
                    the_girl.char "Oh god... I can feel it so deep. I mean... it could... hopefully..."
                    "[the_girl.possessive_title]'s voice starts to trail off."
                elif the_girl.wants_creampie():
                    the_girl.char "Oh god it's so deep."
                elif the_girl.on_birth_control:
                    the_girl.char "Oh fuck...  Good thing I'm on the pill..."
                else:
                    the_girl.char "Oh fuck... I could get pregnant you know..."
                "When you finish, you wait for a bit, reveling in the sensations as [the_girl.title]'s slick cunt has aftershocks."

                "You wait until her orgasm has passed completely, then pull out and stand back."

                if the_girl.has_breeding_fetish():
                    "As your cum starts to leak out, [the_girl.possessive_title] reaches back and tries to keep it inside with her hand."
                else:
                    "You cum leaks out of her dripping wet pussy."

        "Cum on her ass":
            if mc.condom:
                "You pull out of [the_girl.possessive_title] at the last moment, pulling your condom off as your blow your load all over her ass."
                "She holds still for you as you cover her with your sperm."
            else:
                "You pull out of [the_girl.possessive_title] at the last moment, stroking your shaft as you blow your load over her ass. She holds still for you as you cover her with your sperm."
            "She reaches down and you see she is rapidly rubbing her clit as she begins to orgasm at the same time."
            if the_girl.get_opinion_score("being covered in cum") > 0:
                 the_girl.char "Yes! Paint me with your sticky cum!"
            $ the_girl.cum_on_ass()
            $ SB_doggy_standing.redraw_scene(the_girl)
            if the_girl.has_cum_fetish():
                "[the_girl.possessive_title]'s body goes rigid as your cum coats her ass. Goosebumps erupt all over her body as her brain registers your cum on her skin."
                "[the_girl.possessive_title] revels in bliss as your dick sprays jet after jet of seed across her ass. She moans lewdly as her orgasm is enhanced by your bodyshot."
                "She truly is addicted to your cum."
            "After you finish, you watch as she slowly stops rubbing herself. Her body twitches once in a while from an aftershock."
            if the_girl.sluttiness > 120 or the_girl.get_opinion_score("being covered in cum") > 0:
                the_girl.char "Oh god your seed is so hot! Does it look sexy, having it plastered all over my ass?"
                "She reaches back and runs a finger through the puddles of cum you've put on her, then licks her finger clean."
            else:
                the_girl.char "Oh! Its so warm..."
            "You sit back and sigh contentedly, enjoying the sight of [the_girl.possessive_title]'s ass covered in your semen."
        "Cum on her face":
            mc.name "Fuck, get ready [the_girl.title], I wanna cum on your face!"
            if mc.condom:
                "You pull your cock out of [the_girl.possessive_title] with a satisfying pop. You pull your condom off as she turns around on gets on her knees in front of you."
            else:
                "You pull your cock out of [the_girl.possessive_title]. She immediately turns around on gets on her knees in front of you."
            $ the_girl.draw_person(position = "kneeling1")
            if the_girl.get_opinion_score("being covered in cum") > 0 or the_girl.get_opinion_score("cum facials") > 0:
                "[the_girl.possessive_title] reaches up with one handing, stroking you to finish. She reaches down with her other hand and begins to aggressively touch herself."
                "Your orgasm hits hard. Your first jet sprays across her face. Her face is orgasmic bliss as she finishes at the same time."
                $ the_girl.cum_on_face()
                $ the_girl.draw_person(position = "kneeling1")
                if the_girl.has_cum_fetish():
                    "You can see [the_girl.possessive_title]'s pupils dilate as you fulfil her cum fetish."
                    "[the_girl.possessive_title] revels in bliss as your dick sprays jet after jet of seed across her face. She moans lewdly."
                    "She truly is addicted to your cum."
                else:
                    "[the_girl.possessive_title] moans as your dick sprays jet after jet of seed across her face."
            elif the_girl.sluttiness > 80:
                "[the_girl.possessive_title] sticks out her tongue for you and holds still, eager to take your hot load."
                "She reaches down and begins to touch herself, bringing herself to orgasm at the same time as you."
                $ the_girl.cum_on_face()
                $ the_girl.draw_person(position = "kneeling1")
                "You let out a shudder moaning as you cum, pumping your sperm onto [the_girl.possessive_title]'s face and into her open mouth. She makes sure to wait until you're completely finished."
                the_girl.char "Oh god... it feels so good on my skin..."
            elif the_girl.sluttiness > 60:
                "[the_girl.possessive_title] closes her eyes and waits patiently for you to cum."
                "She reaches down and begins to touch herself, bringing herself to orgasm at the same time as you."
                $ the_girl.cum_on_face()
                $ the_girl.draw_person(position = "kneeling1")
                "You let out a shudder moaning as you cum, pumping your sperm onto [the_girl.possessive_title]'s face. She waits until she's sure you're finished, then opens one eye and looks up at you."
            else:
                "[the_girl.possessive_title] closes her eyes and turns away, presenting her cheek to you as you finally climax."
                "She reaches down and begins to touch herself, bringing herself to orgasm at the same time as you."
                $ the_girl.cum_on_face()
                $ the_girl.draw_person(position = "kneeling1")
                "You let out a shudder moaning as you cum, pumping your sperm onto [the_girl.possessive_title]'s face. She flinches as the first splash of warm liquid lands on her cheek, but doesn't pull away entirely."
            "You take a deep breath to steady yourself once you've finished orgasming. [the_girl.possessive_title] looks up at you from her knees, face covered in your semen."
            $ the_girl.call_dialogue("cum_face")
    $ post_double_orgasm(the_girl)
    return
