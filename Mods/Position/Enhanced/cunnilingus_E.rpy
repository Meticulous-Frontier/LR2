# Added Rimming (Original idea by BadRabbit)

init 2:   #Initial declaration made in init 0
    python:
        cunnilingus.scenes.append("scene_SB_Oral_Laying_1")
        cunnilingus.scenes.append("scene_SB_Oral_Laying_2")


label scene_SB_Oral_Laying_1(the_girl, the_location, the_object):
    # CHOICE CONCEPT: Finger Fuck // Tongue Fuck her
    # Intro concept. Short difference depending on if she's wet or not.
    if the_girl.outfit.has_creampie_cum():
        "You lap at the juices flowing down from [the_girl.possessive_title]'s slit. It's an arousing mix of her juices and semen."
    elif the_girl.arousal > 70:
        "[the_girl.possessive_title]'s juices are beginning to flow freely from her slit. You lap them up before circling your tongue aroud her clit a few times."
    else:
        "[the_girl.possessive_title]'s pussy is still getting wet. You lick it slow, giving her time to warm up."

    menu:
        "Finger Her":
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

        "Push Your Tongue Deep":
            ##Based on player oral skill. High oral skill gives good arousal return, low skill falters
            "After licking at her clit, you move your tongue down to her entrance. You push your tongue up inside her as far as it will go."
            if mc.sex_skills["Oral"] > 3:
                "You push your tongue deep and twirl it all around her juicy canal. Your nose is pressing up against her clit, making her gasp."
                if the_girl.outfit.has_creampie_cum():
                    "Your tongue is deep. The salty cum deposited there flows out and begins to run down your chin."
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
                "You push your tongue deep and twirl it all around inside her. You poke it around all the soft, slick crevices that it can reach."
                "[the_girl.possessive_title] puts her hand on the back of your head. She starts to pull your head back a bit, guiding you back to her clit."
                the_girl.char "That feels good [the_girl.mc_title], but it feels even better when you kiss me here..."
                "You accept her guidance and begin to lick and suck at her clit again."
        "Finger Her Ass" if the_girl.get_opinion_score("anal sex") > 0:
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
        "Finger Her Ass\n{color=#ff0000}{size=18}Must like anal sex{/size}{/color} (disabled)" if the_girl.get_opinion_score("anal sex") <= 0:
            pass

        "Rim Her Ass" if the_girl.get_opinion_score("anal sex") > 0:
            "As you continue to lick around [the_girl.possessive_title]'s cunt, you slowly work your way towards her ass."
            if the_girl.has_role(anal_fetish_role):
                if the_girl is mom or the_girl is lily:
                    the_girl.char "Oh!!!"
                else:
                    "You reach out and gently pull out the buttplug that is in her ass."
            "You part her butt cheeks as you lick around her puckered hole, slowly moving to the center."
            $ the_girl.call_dialogue("suprised_exclaim")
            if the_girl.outfit.has_ass_cum():
                "As you lick her you notice that [the_girl.title] still has cum in her ass."
                menu:
                    "Ignore it":
                        "You decide to focus on her ass."
                    "Suck it up":
                        "You start to gently lick around her asshole and then start to suck the cum out of her ass, gently at first but with increasing pressure."
                        $ the_girl.change_arousal(2 + the_girl.get_opinion_score("anal sex"))
                        "You go back to rimming [the_girl.possessive_title]."

            if the_girl.has_role(anal_fetish_role):
                the_girl.char "Oh..my.. god! That feels sooo good...you have to keep doing that."
                "[the_girl.possessive_title] reached behind your head to hold your head in place. Her breathing is heavy but erratic."
                menu:
                    "Keep licking":
                        "You continue to lick [the_girl.possessive_title]'s asshole at a slow and steady pace."
                        the_girl.char "Oh!!! [the_girl.mc_title]!"
                        $ the_girl.call_dialogue("suprised_exclaim")

                    "Tongue fuck her ass.":
                        "You roll the sides of your tongue up and start to push the tip in and out of [the_girl.possessive_title]'s asshole."
                        the_girl.char "Oh!!! [the_girl.mc_title]!"
                        $ the_girl.call_dialogue("suprised_exclaim")
                        "You start to pick up the pace of your tongue action."

                "You continue for a while. [the_girl.title] clearly enjoys the feel of your tongue."
                $ the_girl.change_arousal((the_girl.get_opinion_score("anal sex") * 5) + (the_girl.get_opinion_score("taking control") * 2) + (the_girl.get_opinion_score("getting head")))
            elif the_girl.get_opinion_score("anal sex") > 0:
                "[the_girl.title] reaches down and grabs her own butt cheeks to hold them apart giving you free access to her asshole."
                "You can feel her body relax, as you push your tongue into her ass."
                $ the_girl.call_dialogue("suprised_exclaim")
                if the_girl.get_opinion_score("being fingered") > 0:
                    "As you continue to lick [the_girl.possessive_title]'s ass, you use your hands to play with her cunt."
                    if mc.sex_skills["Foreplay"] > 4:
                        "You spend a few seconds slowly stirring her vagina, then curl your finger up, rubbing her G-spot"
                        if the_girl.get_opinion_score("being fingered") > 0:
                            $ the_girl.discover_opinion("being fingered")
                            $ the_girl.change_arousal(the_girl.get_opinion_score("being fingered") + mc.sex_skills["Foreplay"])
                        the_girl.char "[the_girl.mc_title]! Oh [the_girl.mc_title] that feels so good."
                    else:
                        "You do your best to split your focus between rimming [the_girl.possessive_title] and fingering her pussy, but you find yourself struggling to do both."
                        "You take a break from using your fingers and focus on rimming her."
                the_girl.char "That's right. Lick my ass you dirty boy."
                "[the_girl.title]'s thighs begin to twitch."
                the_girl.char "Oh!!! [the_girl.mc_title] yes!"
                "You continue for a while. [the_girl.title] clearly enjoys the anal stimulation."
                $ the_girl.change_arousal((the_girl.get_opinion_score("anal sex") * 5) + the_girl.get_opinion_score("taking control") + (the_girl.get_opinion_score("getting head")))
            else:
                "[the_girl.title] slowly relaxes as you lick at her asshole."
                $ the_girl.call_dialogue("suprised_exclaim")
                if the_girl.get_opinion_score("being fingered") > 0:
                    "As you continue to lick [the_girl.possessive_title]'s ass, you use your hands to play with her cunt."
                    if mc.sex_skills["Foreplay"] > 4:
                        "You spend a few seconds slowly stirring her vagina, then curl your finger up, rubbing her G-spot"
                        $ the_girl.change_arousal(the_girl.get_opinion_score("being fingered") + mc.sex_skills["Foreplay"])
                        the_girl.char "[the_girl.mc_title]! Oh [the_girl.mc_title] that feels so good."
                    else:
                        "You do your best to split your focus between rimming [the_girl.possessive_title] and fingering her pussy, but you find yourself struggling to do both."
                        "You take a break from using your fingers and focus on rimming her."
                else:
                    "You continue to lick gently at [the_girl.possessive_title]'s ass."
                "[the_girl.title]'s moans in appreciation."
                "You continue for a while. [the_girl.title] enjoying the anal stimulation."
                $ the_girl.change_arousal(2)

            "You continue to use your tongue on her ass. As you do, [the_girl.title] gets more and more excited."
            $ the_girl.change_arousal(2)
            if (the_girl.get_opinion_score("masturbating")) > 0:
                "As you use your tongue [the_girl.possessive_title] reaches to her pussy with one of her hands."
                if (the_girl.get_opinion_score("vaginal sex")) > (the_girl.get_opinion_score("gettting head")):
                    "[the_girl.title] starts thrusting her fingers in and out of her pussy."
                else:
                    "[the_girl.title] starts rubbing her clit."
                $ the_girl.change_arousal((the_girl.get_opinion_score("masturbating") * 2))
            else:
                "[the_girl.possessive_title] rubs her breasts as you continue to use your tongue on her ass."
                the_girl.char "You make me feel so good..."
            "Eventually you finish rimming her and resume eating her out normally."
            if the_girl.get_opinion_score("anal sex") > 1:
                the_girl.char "Fuck that was intense..."

        "Rim Her Ass\n{color=#ff0000}{size=18}Must like anal sex{/size}{/color} (disabled)" if the_girl.get_opinion_score("anal sex") <= 0:
            pass

    if mc.arousal > 70:
        "[the_girl.possessive_title]'s constant moans and gasps are incredibly arousing. You can't help but stroke yourself as you eat her out."
        "You should probably fuck her soon before you cum in your pants!"
    elif mc.arousal > 40:
        "[the_girl.possessive_title]'s moaning and heavy breathing are arousing. You give yourself a couple strokes through your clothes while you eat her."
    else:
        "While you aren't being stimulated, [the_girl.possessive_title]'s gasps and breathing are starting to turn you on."
    return

label scene_SB_Oral_Laying_2(the_girl, the_location, the_object):
    # CHOICE CONCEPT: Submit // Control her
    "[the_girl.possessive_title]'s hips are beginning to rock side to side, grinding against you as you lick her."
    "You feel her legs cross behind your back while she runs her hands through your hair. She starts to grind against you more aggresively."
    "It feels like [the_girl.possessive_title] is trying to take control!"
    menu:
        "Let Her Take Control":
            "You take her enthusiasm as a sign that you must be doing well. You double down on her clit, sucking and licking at it."
            if the_girl.get_opinion_score("taking control") > 0:
                "[the_girl.possessive_title] uses the leverage her legs give her, wrapped around your back, to force your face down into her cunt roughly."
                if the_girl.outfit.has_creampie_cum():
                    "She starts to rock her hips. Your face is getting slick from the combination of juices around her pussy."
                else:
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
