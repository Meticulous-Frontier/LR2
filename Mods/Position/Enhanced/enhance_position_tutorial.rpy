# This file is designed to walk a user through enhancing existing Vren sex positions
# This file will offer the MC the opportunity to stealth off a condom that may be in use, as well as give unique orgasm text if you choose to cum inside her

init 2:     #This init must be a later number than the original position declaration.
            #Most positions are declared in init 0:
    python:
        doggy.scenes.append("doggy_stealth_attempt")    #Adding to doggy.scenes gives a new scene that could be randomly selected
        stealth_orgasm = False                          #Create a new variable to find out if orgasm was stealthed
        doggy.outro = "outro_stealth_doggy"             #Completely replace the orgasm scene
        doggy.intro = "intro_stealth_doggy"             #Rewrite intro to make sure stealth_orgasm = False so we don't have weird dialogue in follow up sessions


        doggy_anal.transitions.remove([doggy,"transition_doggy_anal_doggy"])

        doggy_anal.transitions.append([doggy,"transition_stealth_doggy_anal_doggy"])
        #Other variables we could change to enhance the position

        # doggy.strip_description = "strip_doggy"         #Make her notice the condom is off when she strips
        # doggy.strip_ask_description = "strip_ask_doggy" #Same as above
        # doggy.orgasm_description = "orgasm_doggy"       #change her orgasm in some way
        # doggy.girl_energy = 14                          #Change energy requirements
        # doggy.guy_energy = 20                           #Change energy requirements

#We redefine intro because stealth_orgasm could be set to true from a previous sex encounter if we swapped positions before finishing
label intro_stealth_doggy(the_girl, the_location, the_object):
    $ stealth_orgasm = False   #This is the only change made from the existing intro.
    mc.name "[the_girl.title], I want you to get on your hands and knees for me."
    if the_girl.effective_sluttiness() > 100:
        the_girl.char "I want you inside of me so badly..."
    elif the_girl.effective_sluttiness() > 80:
        the_girl.char "Mmm, you know just what I like [the_girl.mc_title]."
    else:
        the_girl.char "Like this?"
    "[the_girl.title] gets onto all fours in front of you on the [the_object.name]. She wiggles her ass impatiently at you as you get your hard cock lined up."
    if the_girl.arousal > 60:
        "You rub the tip of your penis against [the_girl.title]'s cunt, feeling how nice and wet she is already. She moans softly when you slide the head of your dick over her clit."
    else:
        "You rub the tip of your penis against [the_girl.title]'s cunt, getting ready to slide yourself inside."
    "When you're ready you push forward, slipping your shaft deep inside of [the_girl.possessive_title]. She gasps and quivers ever so slightly as you start to pump in and out."
    return


label doggy_stealth_attempt(the_girl, the_location, the_object):  #Write the new scene here
    "[the_girl.possessive_title] moans, clearly enjoying herself as your cock hits all the right places."
    "She lowers her face to the [the_object.name] and arches her back. Her ass jiggles pleasantly with each stroke."
    if mc.condom:
        "You look down and watch as her pussy takes your condom covered cock over and over. You wonder how good it would feel have her pussy stroke you raw."
        "[the_girl.title] is face down, if you are quick you could probably sneak the condom off without her even noticing."
        "If you take it off you should probably pull out when you finish though... or should you?"
        menu:
            "Attempt to remove condom":
                "You bring one hand down to your cock and get it ready. With one out stroke, you pretend to accidentally pull back to far, pulling out of her."
                "You quickly strip off the condom as quietly as possible, then line yourself up and plunge into [the_girl.title]'s heavenly slick cunt."
                $ stealth_orgasm = True
                $ mc.condom = False
                #TODO add a check against focus where she realizes what you are doing
                "You begin to pound her with renewed vigor, enjoying the steamy sensation of her raw pussy."
                the_girl.char "Oh god it feels so good. I can feel you so deep!"
                "You smirk and shove yourself in deep. It feels like her cunt is swallowing you whole. You enjoy the sensation for a few moments then resume fucking."
                return
            "Leave condom on":
                pass
    "You put one hand on her ass and give it a hard squeeze. [the_girl.possessive_title] responds by pushing herself back against you and swivels her hips around you."
    "You stay still and enjoy the sensations while [the_girl.title] uses your cock to stir her cunt. Eventually you grab her hips and resume fucking her."

    return

label outro_stealth_doggy(the_girl, the_location, the_object):
    "[the_girl.title]'s tight cunt draws you closer to your orgasm with each thrust. You finally pass the point of no return and speed up, fucking her as hard as you can manage."
    $the_girl.call_dialogue("sex_responses_vaginal")
    mc.name "Ah, I'm going to cum!"
    menu:
        "Cum inside of her.":
            if stealth_orgasm:  #You sly dog
                "You know you should probably pull out after stealthing the condom off, but you can't. You pull back on [the_girl.possessive_title]'s hips and drive your cock deep inside of her as you cum."
                the_girl.char "Oh god, you are cumming so hard, I swear I can almost feel it splashing inside of me!"
                $ the_girl.cum_in_vagina()
                $ doggy.redraw_scene(the_girl)
                "After you finish, you leave your cock deep inside her. A few drops of your cum start to drip out of her."
                "[the_girl.title] reaches between her legs and feels it, realizing you just finished inside of her."
                if the_girl.get_opinion_score("creampies") > 0:         #She likes creampies...
                    the_girl.char "Wait... that's... you took the condom off, didn't you? Oh fuck that's why it felt so good!"
                    $ the_girl.discover_opinion("creampies")
                    the_girl.char "Oh god that's so hot. You could knock me up you know? Next time at least warn me, so I can enjoy it too!"
                    $ the_girl.change_happiness(2)
                    $ the_girl.change_obedience(3)
                elif the_girl.sluttiness > 80:                          #She is slutty enough she doesn't mind the cream filling
                    the_girl.char "Oh my god you took the condom off? You know you can cum inside me anytime you want, no need to be stealthy about it!"
                    $ the_girl.change_obedience(3)
                else:                                                   #She gets pissed
                    the_girl.char "What the FUCK? You took the condom off? And then came inside me!?! I could get pregnant asshole!"
                    $ the_girl.change_happiness(-5)
                    $ the_girl.change_obedience(3)
                    $ the_girl.change_love(-5)          #She loses trust
                    "You planted your seed inside of [the_girl.possessive_title], but it is clear she isn't happy about it."
                "You slowly pull out of [the_girl.title]. Your cum is dripping down her leg as you sit back."
                $ stealth_orgasm = False                #MAke sure we set this to false so next sex session doesn't get confused
            elif mc.condom:
                "You pull back on [the_girl.possessive_title]'s hips and drive your cock deep inside of her as you cum. She gasps as you dump your load into her, barely contained by your condom."
                $ the_girl.call_dialogue("cum_vagina")
                "You wait until your orgasm has passed completely, then pull out and sit back. The condom is ballooned and sagging with the weight of your seed."
                if the_girl.get_opinion_score("drinking cum") > 0 and the_girl.sluttiness > 50:
                    $ the_girl.discover_opinion("drinking cum")
                    "[the_girl.possessive_title] turns around and reaches for your cock. With delicate fingers she slides the condom off of you."
                    the_girl.char "It would be a shame to waste all of this, right?"
                    "She winks and brings the condom to her mouth. She tips the bottom up and drains it into her mouth."
                    $ the_girl.change_slut_temp(the_girl.get_opinion_score("drinking cum"))
                else:
                    "[the_girl.possessive_title] turns around and reaches for your cock. She removes the condom and ties the end in a knot."
                    the_girl.char "Look at all that cum. Well done."
                "You sigh contentedly and enjoy the post-orgasm feeling of relaxation."
            else:
                $ stealth_orgasm = False
                "You pull back on [the_girl.possessive_title]'s hips and drive your cock deep inside of her as you cum. She gasps softly in time with each new shot of hot semen inside of her."
                $ the_girl.call_dialogue("cum_vagina")
                $ the_girl.cum_in_vagina()
                $ doggy.redraw_scene(the_girl)
                if the_girl.sluttiness > 80:
                    the_girl.char "Oh wow, there's so much of it..."
                else:
                    the_girl.char "Oh fuck, what if I get pregnant? Ah..."

                "You wait until your orgasm has passed completely, then pull out and sit back. Your cum starts to drip out of [the_girl.title]'s slit almost immediately."

        "Cum on her ass.":
            $ stealth_orgasm = False
            if mc.condom:
                "You pull out of [the_girl.title] at the last moment. You whip your condom off and stroke your cock as you blow your load over her ass."
                "She holds still for you as you cover her with your warm sperm."
            else:
                "You pull out of [the_girl.title] at the last moment, stroking your shaft as you blow your load over her ass. She holds still for you as you cover her with your sperm."
            $ the_girl.cum_on_ass()
            $ doggy.redraw_scene(the_girl)
            if the_girl.sluttiness > 120:
                the_girl.char "What a waste, you should have put that inside of me."
                "She reaches back and runs a finger through the puddles of cum you've put on her, then licks her finger clean."
            else:
                the_girl.char "Oh wow, there's so much of it..."
            "You sit back and sigh contentedly, enjoying the sight of [the_girl.title] covered in your semen."
    $ stealth_orgasm = False
    return

label transition_stealth_doggy_anal_doggy(the_girl, the_location, the_object):
    #transition from anal to normal doggy style.
    $ stealth_orgasm = False

    if the_girl.arousal >= 70 or report_log.get("girl orgasms", 0) > 0:
        "You pull out of [the_girl.title]'s wet pussy, leaving it dripping fluids on the floor."

    "You line your cock up with her asshole, the tip just barely pressing against it."
    call transition_default_anal_penetration_dialog(the_girl, the_location, the_object) from _call_transition_default_anal_penetration_dialog_3
    return

label transition_doggy_to_anal_doggy_taboo_break_label(the_girl, the_location, the_object):
    "You pull out of [the_girl.title]'s pussy and lean back to admire her ass."
    "You grab it and give it a squeeze, then a hard slap."
    if the_girl.effective_sluttiness(doggy_anal.associated_taboo) > doggy_anal.slut_cap or the_girl.get_opinion_score("showing her ass") > 0:
        the_girl.char "Mmmm."
        $ the_girl.draw_person(position = "doggy", the_animation = ass_bob, animation_effect_strength = 0.7)
        "[the_girl.possessive_title] points her butt in your direction. She lowers her shoulders and works her hips for you."
    else:
        mc.name "Nice. Now shake it for me."
        the_girl.char "Like... this?"
        $ the_girl.draw_person(position = "doggy", the_animation = ass_bob, animation_effect_strength = 0.4)
        "[the_girl.title] works her hips and jiggles her ass for you."
        mc.name "Getting there, a little faster now."
        $ the_girl.draw_person(position = "doggy", the_animation = ass_bob, animation_effect_strength = 0.7)
        "She speeds up."
    the_girl.char "Is that what you wanted?"
    "You slap your cock down on her ass and grab her tight cheeks, spreading them apart to get a look at her asshole."
    mc.name "It's a start. I think it's time we stretched you open."
    $ the_girl.call_dialogue(doggy_anal.associated_taboo+"_taboo_break")
    "You hold onto [the_girl.title]'s hips with one hand and your cock with the other, guiding it as you press it against her tight hole."
    if the_girl.sex_skills["Anal"] > 2:
        "She gasps as your tip starts to spread her open. She lowers her shoulders and pushes her hips against you, helping the process."
        the_girl.char "Oh god... Mfphhhh!"

    else:
        "She gasps as your tip tries to spread open her impossibly tight asshole. She tries to pull away, but you pull on her waist and bring her closer."
        mc.name "Come on, you'll get there."
        if the_girl.arousal >= 70 or report_log.get("girl orgasms", 0) > 0:
            "Your cock is still wet from [the_girl.title]'s pussy. You push steadily as you slide the tip into [the_girl.title]'s ass."
        else:
            "You pull back slightly, spit onto your cock and try again. This time making better progress, sliding the tip of your dick into [the_girl.title]'s ass."
        the_girl.char "Oh god... Fuck!"
    "Inch by inch you slide your entire length into [the_girl.possessive_title]. She grunts and gasps the whole way down."
    "You stop when you've bottomed out, to give your cock time to properly stretch her out."
    the_girl.char "I think... I'm ready for you to move some more..."
    "You pull back a little bit and give her a few testing strokes. When she can handle those you speed up, until you're thrusting your entire length."
    return
