init 2:   #Initial declaration made in init 0
    python:
        cunnilingus.scenes.append("scene_SB_Oral_Laying_1")
        cunnilingus.scenes.append("scene_SB_Oral_Laying_2")


label scene_SB_Oral_Laying_1(the_girl, the_location, the_object, the_round):
    # CHOICE CONCEPT: Finger Fuck // Tongue Fuck her
    # Intro concept. Short difference depending on if she's wet or not.
    if the_girl.arousal > 70:
        "[the_girl.possessive_title]'s juices are beginning to flow freely from her slit. You lap them up before circling your tongue aroud her clit a few times."
    else:
        "[the_girl.possessive_title]'s pussy is still getting wet. You lick it slow, giving her time to warm up."

    menu:
        "Finger Her.":
            #Generic choice with bonus based on girl opinion and MC foreplay skill
            "As you continue to lick all around [the_girl.possessive_title]'s cunt, you slowly push a finger up inside of her."
            if mc.sex_skills["Foreplay"] > 2:
                "You spend a few seconds slowly stirring her vagina, then curl your finger up, rubbing her G-spot"
                if the_girl.get_opinion_score("being fingered") > 0:
                    $ the_girl.discover_opinion("being fingered")
                    $ the_girl.change_arousal(the_girl.get_opinion_score("being fingered") + mc.sex_skills["Foreplay"])
                the_girl.char "[the_girl.mc_title]! Oh [the_girl.mc_title] that feels so good."
                "She moans and runs her hands through your hair."
                "You lightly suck on her clit as you finger her, caressing her most sensitive places."
            else:
                "You do your best to split your focus between kissing [the_girl.possessive_title]'s pussy and fingering her, but you find yourself struggling to do both."
                "You take a break from licking her and focus pleasing her with your finger for a bit."
                if the_girl.get_opinion_score("being fingered") > 0:
                    $ the_girl.discover_opinion("being fingered")
                    $ the_girl.change_arousal(the_girl.get_opinion_score("being fingered"))
                    the_girl.char "Mmmm, I love it when you stick your fingers inside me..."
                else:
                    "[the_girl.possessive_title] enjoys your fingering, but soon you feel her hands running through your hair. She's lightly pulling your head down, trying to get you to resume licking her."
                "You slowly pull your finger out, then focus on pleasing her orally."

        "Push Your Tongue Deep.":
            ##Based on player oral skill. High oral skill gives good arousal return, low skill falters
            "After licking at her clit, you move your tongue down to her entrance. You push your tongue up inside her as far as it will go."
            if mc.sex_skills["Oral"] > 3:
                "You push your tongue deep and twirl it all around her juicy canal. Your nose is pressing up against her clit, making her gasp."
                if the_girl.get_opinion_score("taking control") > 0:
                    "[the_girl.possessive_title] puts her hand on the back of your head, urging your tongue deeper and your nose more firmly against her clit."
                    "She starts to rock her hips, grinding herself against your face."
                    the_girl.char "Mmm, that's it [the_girl.mc_title]! Fuck that feels good!"
                    $ the_girl.discover_opinion("taking control")
                    $ the_girl.change_arousal(the_girl.get_opinion_score("taking control") * 3)
                else:
                    the_girl.char "Oh [the_girl.mc_title]! That feels so good..."
                    $ the_girl.change_arousal(2)

                "[the_girl.possessive_title] moans and trembles as you please her."
            else:
                "You push your tongue deep and twirl it all around insdie her. You poke it around all the soft, slick crevices that it can reach."
                "[the_girl.possessive_title] puts her hand on the back of your head. She starts to pull your head back a bit, guiding you back to her clit."
                the_girl.char "That feels good [the_girl.mc_title], but it feels even better when you kiss me here..."
                "You accept her guidance and begin to lick and suck at her clit again."
        "Finger Her Ass." if (the_girl.get_opinion_score("anal sex") > 0 and the_girl.get_opinion_status("anal sex")):
            "As you continue to lick all around [the_girl.possessive_title]'s cunt, you slowly push a finger up inside of her pussy."
            if the_girl.arousal > 50:
                "It isn't long until your finger is well lubricated from her sopping wet cunt."
            else:
                "It takes a bit, but soon your finger is lubricated by her natural juices."
            "You bring your finger down to her puckered hole and give he a little bit of pressure up against it. She sighs and you can feel her body relax, allowing you to push your finger into her ass."
            the_girl.char "Oh god I love it when you do this..."
            "[the_girl.possessive_title] is running her hands through your hair, her breathing heavy. You push your finger deep into her bowel."
            "You attack her clit with your tongue and lips. She bucks her hips against your face, pulling off your finger a bit. She rocks her hips back down, your finger pushing deep into her again."
            "[the_girl.title]'s hips begin to grind forward and back. With each peak she grinds her clit against your face, and with each trough your finger is fully embedded in her backdoor."
            the_girl.char "Oh!!! [the_girl.mc_title] yes!"
            "You continue for a while. [the_girl.title] clearly enjoys the anal penetration. Eventually you pull your finger out and resume eating her out normally."
            $ the_girl.change_arousal(the_girl.get_opinion_score("anal sex") * 10)
            the_girl.char "Fuck that was intense..."
        "Finger Her Ass.\n{size=22}Must like anal sex{/size} (disabled)" if (the_girl.get_opinion_score("anal sex") <= 0 or not the_girl.get_opinion_status("anal sex")):
            pass


    if mc.arousal > 70:
        "[the_girl.possessive_title]'s constant moans and gasps are incredibly arousing. You can't help but stroke yourself as you eat her out."
        "You should probably fuck her soon before you cum in your pants!"
    elif mc.arousal > 40:
        "[the_girl.possessive_title]'s moaning and heavy breathing are arousing. You give yourself a couple strokes through your clothes while you eat her."
    else:
        "While you aren't being stimulated, [the_girl.possessive_title]'s gasps and breathing are starting to turn you on."
    return

label scene_SB_Oral_Laying_2(the_girl, the_location, the_object, the_round):
    # CHOICE CONCEPT: Submit // Control her
    "[the_girl.possessive_title]'s hips are beginng to rock side to side, grinding against you as you lick her."
    "You feel her legs cross behind your back while she runs her hands through your hair. She starts to grind against you more aggresively."
    "It feels like [the_girl.possessive_title] is trying to take control!"
    menu:
        "Let Her Take Control":
            "You take her enthusiasm as a sign that you must be doing well. You double down on her clit, sucking and licking at it."
            if the_girl.get_opinion_score("taking control") > 0:
                "[the_girl.possessive_title] uses the leverage her legs give her, wrapped around your back, to force your face down into her cunt roughly."
                "She starts to rock her hips, grinding herself against your face."
                the_girl.char "Mmm, that's it [the_girl.mc_title]! Fuck that feels good!"
                $ the_girl.discover_opinion("taking control")
                $ the_girl.change_arousal(the_girl.get_opinion_score("taking control") * 3)
            else:
                "She starts to rock her hips, grinding herself against your face."
                the_girl.char "Oh [the_girl.mc_title]! That feels so good..."
                $ the_girl.change_arousal(2)
            "She grinds against you hard, but your are quickly running out of air. When it gets to be too intense you break her hold on you by pushing yourself up on your hands."
            the_girl.char "Mmmm, sorry [the_girl.mc_title], it feels so good when you lick me like this!"
        "Subdue Her":
            "You grab her hand off the back of your head. You arch your back to take away the leverage her legs give."
            mc.name "If you can't behave yourself, I'll have to spank that naughtiness out of you."
            if the_girl.get_opinion_score("being submissive") > 0:
                the_girl.char "Sorry! But maybe you should spank me... I've been a pretty bad girl lately."
                "You give her pussy a moderate spank."
                mc.name "I wasn't talking about your ass."
                "[the_girl.possessive_title] quivers at your rough touch and words. She pretends she doesn't like it."
                the_girl.char "Sorry sir! It won't happen again, I promise!"
            else:
                the_girl.char "Sorry! It won't happen again!"
            "You don't believe her, but you quickly dive into her pussy again, wary of her trying to take control again."




    if mc.arousal > 70:
        "[the_girl.possessive_title]'s constant moans and gasps are incredibly arousing. You can't help but stroke yourself as you eat her out."
        "You should probably fuck her soon before you cum in your pants!"
    elif mc.arousal > 40:
        "[the_girl.possessive_title]'s moaning and heavy breathing are arousing. You give yourself a couple strokes through your clothes while you eat her."
    else:
        "While you aren't being stimulated, [the_girl.possessive_title]'s gasps and breathing are starting to turn you on."
    return
