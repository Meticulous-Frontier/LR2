init python:
    SB_anal_standing = Position("Standing Anal",70,95,"standing_doggy","Low","Vagina","Anal",18,18,[],
        "intro_SB_anal_standing",
        ["scene_SB_anal_standing_1","scene_SB_anal_standing_2"],
        "outro_SB_anal_standing",
        "transition_default_SB_anal_standing",
        "strip_SB_anal_standing", "strip_ask_SB_anal_standing",
        "orgasm_SB_anal_standing",
        opinion_tags = ["doggy style sex", "anal sex", "sex standing up"])
    list_of_positions.append(SB_anal_standing)

init 1 python:
    SB_anal_standing.link_positions(SB_doggy_standing, "transition_SB_anal_standing_SB_doggy_standing")
    SB_anal_standing.link_positions(doggy_anal, "transition_SB_anal_standing_doggy_anal")

label intro_SB_anal_standing(the_girl, the_location, the_object, the_round):
    "With you arms wrapped around [the_girl.possessive_title], you make out for a bit with her back to the [the_object.name]"
    "You turn her around, and she leans over [the_object.name], presenting her ass to you."
    mc.name "That's it, [the_girl.title], I'm going to fuck your ass today."
    if SB_check_fetish(the_girl, anal_fetish_role):
        the_girl.char "Oh thank god, I've been day dreaming about this all day long."
    elif the_girl.get_opinion_score("anal sex") > 0 :
        the_girl.char "I can't wait! It's so intense when you fuck me back there..."
    elif the_girl.effective_sluttiness() > 110:
        the_girl.char "Oh god I love it when you do this to me..."
    elif the_girl.effective_sluttiness() > 80:
        the_girl.char "Ok, just be careful [the_girl.mc_title]..."
    else:
        the_girl.char "I don't know, are you sure that thing is gonna fit in me back there?"

    if SB_check_fetish(the_girl, anal_fetish_role):
        if the_girl == mom:
            "You work your cock up and down [the_girl.possessive_title]'s slit a few times, her wetness lubricating it."
            "You lean forward and whisper into her ear."
            mc.name "[the_girl.title]... your [the_girl.mc_title] is about to fuck your ass now, just the way you like."
            "Her body shudders from your dirty talk. She wiggles her ass back up against you."
            the_girl.char "Do it honey. [the_girl.title] is ready for you!"
        elif the_girl == lily:
            "You work your cock up and down [the_girl.possessive_title]'s slit a few times, her wetness lubricating it."
            "You lean forward and whisper into her ear."
            mc.name "Hey [the_girl.title], your [the_girl.mc_title] is about to fuck your ass now, just the way you like."
            "Her body shudders from your dirty talk. She wiggles her ass back up against you."
            the_girl.char "Do it! Stick it in me, you know I can take it!"
        else:
            "You slowly pull out the pink jewelled butt plug from [the_girl.possessive_title]'s rectum. She quivers in anticipation of what you are about to do to her."
            $ the_girl.change_arousal(the_girl.get_opinion_score("anal sex"))
            "You work a couple fingers into her bottom. It is clear she loves anal sex so much, she keeps herself lubed up with the plug in throughout the day hoping for you to come fuck it."
            "You decide to tease her before you put it in."
            mc.name "You're such a buttslut, [the_girl.title]. Are you sure you want it back there? Your pussy looks like it could use a proper fucking too..."
            "[the_girl.possessive_title] tries to push back against you and begins to beg."
            the_girl.char "No! I need you in my ass right now... I need the heat and intensity of you fucking my ass right now!"
            "When you're ready you push forward. Her back passage greedily accepts your erection, eliciting a satisfied sigh from [the_girl.possessive_title]"
    elif the_girl.arousal > 60:
        "You rub the tip of your penis against [the_girl.possessive_title]'s cunt, feeling how nice and wet she is already. You rub your lubricated penis against her ass to help prepare her for your initial penetration."
        "You rub your dick against her pussy again and gather more of her juices. She is already so wet you are soon slick with her secretions"
    else:
        "You line yourself up with her ass, but the lack of lubricant makes it impossible to push it in. You pull on her hair to bring her head back around to face you."
        "You put your other hand in front of her face and she quickly opens her mouth and sucks on them. [the_girl.possessive_title] slobbers all over your fingers for a few a seconds before you pull them out with a loud pop"
        "You use your fingers to crudely work in and out of her ass a few times to help get it lubricated."
        "Deciding against making her suck on your fingers again after they've been in her ass, you spit a couple times down on her ass to get a bit more lubrication so you can penetrate her"
    "When you're ready you slowly push forward. It takes several seconds of steady pressure until you finally bottom out."
    if the_girl.get_opinion_score("anal sex") > 0 :
        the_girl.char "Oh my god it's so dirty... but it is so good too..."
        $ the_girl.discover_opinion("anal sex")
    return

label scene_SB_anal_standing_1(the_girl, the_location, the_object, the_round):
    "Your hips slap against [the_girl.possessive_title]'s as you plunder her rectum."
    $ the_girl.call_dialogue("sex_responses_anal")
    if the_girl.sex_skills["Anal"] < 2: #Inexperienced
        "After a particularly hard thrust, [the_girl.possessive_title] reflexively starts to pull away. You grab her hips to keep her from pulling off completely."
        the_girl.char "I'm sorry [the_girl.mc_title], it hurts. Can you go a little slower?"
        "You pull her hips back toward you slowly. Her inexperienced ass yields to your penis and she sighs as you bottom out"
        "You pull yourself out a bit, then spit on her asshole and work it around a bit to provide a bit of extra lubrication."
        "Next time you push yourself in it goes in a bit easier, but you can tell she is having a hard time taking you in her back passage."
    elif SB_check_fetish(the_girl, anal_fetish_role):           #Anal fetish
        "After a particularly hard thrust, [the_girl.possessive_title] moans lewdly."
        if the_girl == mom:
            the_girl.char "That's it honey, fuck me harder! God I wish I could walk around with you inside me all day..."
        elif the_girl == lily:
            the_girl.char "That's it [the_girl.mc_title]! Fuck me harder! God I wish I could walk around with you inside me all day..."
        else:
            the_girl.char "That's it, fuck me harder! This is so much better than that plug, I wish I could walk around with you inside me all day..."
        "With one hand on her hip to control the pace, you grope and worship her ass cheeks with the other hand."
        "[the_girl.possessive_title] clenches each time you pull back, and relaxes each time your push forward. The sensation is exquisite."
        "You use both hands to grab her hips and slam yourself into her."
        "Buried deep inside, you stir your hips in a circular motion. Her rectum quivers and caresses you in response."
    else:
        "Fucking her hard, [the_girl.possessive_title] moans, matching each hip movement of yours with movement of her own."
        the_girl.char "Oh god, you fuck me so good, I can barely keep up!"
        "[the_girl.possessive_title] reaches back with one hand and pulls her ass cheek back, giving you a great view of her booty hole stretched wide to accomodate you."
        "Buried deep inside, you stir your hips in a circular motion. Her rectum quivers in response."
    menu:
        "knead her ass":
            "With your erection buried deep in her rump, you take both hands and knead her ass cheeks."
            mc.name "[the_girl.title], your ass is so tight, I can't believe you let me sodomize you like this."
            if the_girl.get_opinion_score("being submissive") > 0 or the_girl.obedience > 130:
                "[the_girl.possessive_title] trembles at your words and touch. "
                "You pull her ass cheeks apart and revel in her ultimate submission, your cock in her forbidden hole."
                the_girl.char "I couldn't stop you from fucking me... any way you want... even if I wanted to..."
                "You reach forward and run a hand through her hair. You knead her scalp for a few seconds, then grasp her hair and pull it towards you."
                mc.name "That's right bitch, you're here to pleasure me, when, how, and wherever I want."
                $ the_girl.discover_opinion("being submissive")
                $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive") * 3)
            elif the_girl.get_opinion_score("taking control") > 0 or the_girl.obedience < 80:
                "[the_girl.possessive_title] looks back at you and smiles."
                the_girl.char "It's definitely a... unique feeling [the_girl.mc_title]. Maybe you should let me peg you sometime?"
                "You give [the_girl.possessive_title] a good, hard thrust in response."
                $ the_girl.discover_opinion("taking control")
            else:
                the_girl.char "I don't know what is about you, [the_girl.mc_title]... I just want to make you feel good!"
                "You pull her ass cheeks apart. You give her a couple long, slow thrusts and enjoy the sight of your erection disappearing inside her bowel."
                if mc.arousal > 70:
                    "You moan at the sensations."
                    mc.name "You feel amazing. You're gonna make me cum soon."
                    if the_girl.get_opinion_score("creampies") > 0:
                        "[the_girl.possessive_title] looks back at you and smiles."
                        the_girl.char "Oh [the_girl.mc_title], I can't wait to feel you fill me up. I hope you finish deep!"
                        "[the_girl.possessive_title]'s ass quivers a bit, as she imagines you cumming deep inside her."
                        $ the_girl.discover_opinion("creampies")
                        $ the_girl.change_arousal(the_girl.get_opinion_score("creampies") * 3)
                        if the_girl.get_opinion_score("being covered in cum") > 0:
                            the_girl.char "You could always pull out too... your cum feels so good when is splashes all over my skin..."
                            $ the_girl.discover_opinion("being covered in cum")
                            $ the_girl.change_arousal(the_girl.get_opinion_score("being covered in cum") * 3)
                            if the_girl.get_opinion_score("cum facials") > 0:
                                the_girl.char "Or my face! You haven't cum on my face in a while either..."
                                $ the_girl.discover_opinion("cum facials")
                                $ the_girl.change_arousal(the_girl.get_opinion_score("cum facials") * 3)
                                "[the_girl.possessive_title] starts muttering to herself, fantasizing about all the different ways you could cum on, or in her."
            "You put your hands on her hips and resume your anal coupling."



        "Play with her clit":
            "You lean forward a bit and reach down with one hand and begin to move it in circles around her clit."
            if the_girl.get_opinion_score("being fingered"):
                "[the_girl.possessive_title] moans loudly in response."
                the_girl.char "Oh [the_girl.mc_title], I love your hands on me... especially down there..."
                "You slide your middle finger along her slit a few times and then push up inside her pussy."
                "You give your hips a few long, slow strokes and you move your finger in time, penetrating both her holes at once."
                $ the_girl.discover_opinion("being fingered")
                $ the_girl.change_arousal(the_girl.get_opinion_score("being fingered") * 3 + mc.sex_skills["Foreplay"])
                "She really enjoys the extra stimulation."
            else:
                "[the_girl.possessive_title] moans in response."
                "After a few moments of stimulation, she starts to move her hips back and forth, stirring your dick inside her bowel."
                $ the_girl.change_arousal(mc.sex_skills["Foreplay"])
                if the_girl.arousal > 80:
                    "You can feel her juices dripping down from her slit in response to your touch."
                    if the_girl.arousal > 130:
                        "She moans loudly. She grinds herself up against your fingers while your cock is buried deep inside her ass. The stirring motion feels great."
                        the_girl.char "Oh fuck, here I go again!"
                        "[the_girl.possessive_title]'s legs start to give out as she cums yet again. You hold her body in place as she cums, your hips in the back and your hand in her crotch."
                        $the_girl.change_happiness(5)
                        the_girl.char "Oh jesus... you made me cum again... I... god keep going, I'm going to cum again!"
                        return
            "After a bit longer of touching her, you straighten your back and begin to rock your hips again, continuing to fuck her ass."
    return


label scene_SB_anal_standing_2(the_girl, the_location, the_object, the_round):
    "[the_girl.possessive_title] quivers as you slow up the pace a bit. The sensation of burying yourself in her tight chute over and over is amazing."
    if the_girl.outfit.tits_available():
        "You reach around her body with one hand and grasp her tit. You pinch and pull at her nipple roughly as you plow her behind."
    else:
        "You run your hands along her hips. You grab her hips and smack her ass roughly as you plow her behind."

    if the_girl.arousal > 130:
        the_girl.char "Ohhh my god, its so good... I can't believe I came already..."
        "[the_girl.possessive_title]'s legs are shaking. She is thoroughly enjoying her anal plundering."
        if SB_check_fetish(the_girl, anal_fetish_role):
            the_girl.char "This is it, this is why I love anal so much... I just can't stop cumming! It feels so good."
    elif the_girl.arousal > 80:
        the_girl.char "Ohhh, it feels so good. You're gonna make me cum like this... aren't you?"
        "You can feel a slight quiver in [the_girl.possessive_title]'s body as you fuck her. She's probably going to cum soon!"
    else:
        "[the_girl.possessive_title] groans in response to one particularly deep thrust."
        the_girl.char "It's so big... How does it even fit back there?"
    "You push yourself in as deep as you can go. [the_girl.possessive_title] moans as you fill her completely."
    menu:
        "Admire her":
            "You moan in appreciation."
            mc.name "[the_girl.title], your ass is so good. Your booty feels amazing."
            if SB_check_fetish(the_girl, anal_fetish_role):
                the_girl.char "I love being your anal slut. Fuck me good [the_girl.mc_title]!"
            elif the_girl.sluttiness > 80:
                the_girl.char "You are so big... its so full when you push it in me like this."
            else:
                the_girl.char "It better... I can't believe I let you talk me into this..."
        "Talk Dirty":
            mc.name "I love how your ass gets so stretched out with my cock fucking it."
            if SB_check_fetish(the_girl, anal_fetish_role):
                "[the_girl.possessive_title] moans enthusiastically. She wiggles her hips back and forth, caressing your dick with her forbidden hole."
                the_girl.char "[the_girl.mc_title]... fuck my ass... fuck me hard!"
                "You give her what she wants. You grab her hips and start thrusting into her hard and fast."
                the_girl.char "Oh [the_girl.mc_title]... [the_girl.mc_title]!"
                $ the_girl.change_arousal(the_girl.get_opinion_score("anal sex"))
                "[the_girl.possessive_title] is moaning your name over and over. You continue to give her the anal reeming she is begging for."

            elif the_girl.get_opinion_score("being submissive") > 0 or the_girl.obedience > 130:
                "[the_girl.possessive_title] moans enthusiastically."
                the_girl.char "[the_girl.mc_title]... use me... fuck me! Make me your little slut!"
                "You give her what she wants. You grab her hips and start thrusting into her hard and fast."
                $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive") * 3 + 3)
                "You give her the anal reeming she is begging for."
            elif the_girl.get_opinion_score("anal sex") < 0 :
                "[the_girl.possessive_title] looks back at you with a scowl."
                the_girl.char "Don't get used to it, [the_girl.mc_title]... I'm not sure how I let you talk me into this..."
                $ the_girl.discover_opinion("anal sex")
                "You decide for now to keep your pace nice a slow."
            else:
                "[the_girl.possessive_title] looks back at you and manages to smile throug the intense sensation of having her ass fucked."
                the_girl.char "You are stretching me out so much... Be careful back there, I'm not sure how much of this I can take!"
                "You reassure her, and then slowly begin to fuck her tightest hole again."
        "Choke Her" if (the_girl.get_opinion_score("being submissive") > 0 and the_girl.get_opinion_status("being submissive")):   #Can only be done if the girl is known submissive#
            "You take your hands off her hips and run them up her back. With one hand you grab the back of her hair and pull her head back."
            the_girl.char "Mmm, thats it, you can be rough with me if you want..."
            "You pull her hair back hard enough to hurt a little, she arches her back in pleasure as you start to fuck her ass more roughly."
            mc.name "Of course I can, I can do anything I want to you, my little slut."
            "You run your other hand along the side of her neck. She begins to say something but you squeeze her neck and she stops."
            mc.name "Sshhh, theres no need for words right now."
            "You tighten your hold around her neck, constricting her airway. [the_girl.title] shoves her ass back hard against you."
            "You loosen your grip for a second and she moans loudly and takes a couple deep breaths. You cut the third one off and begin to really pound her ass."
            "Her ass cheeks quake from your relentless fucking. [the_girl.possessive_title] begins to squirm against you, fighting for air."
            $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive") * 10)
            "You hold on for a few more seconds, until you feel her knees start to buckle before letting go. [the_person.possessive_title] gasps for air."
            the_girl.char "Oh my god, that was so hot..."
            "You spank her ass hard and continue to fuck her tightest hole."
        "Choke Her\n{size=22}Must be submissive{/size} (disabled)" if (the_girl.get_opinion_score("being submissive") <= 0 or not the_girl.get_opinion_status("being submissive")):
            pass
    return


label outro_SB_anal_standing(the_girl, the_location, the_object, the_round):
    "[the_girl.possessive_title]'s tight ass draws you closer to your orgasm with each thrust. You finally pass the point of no return and speed up, fucking her as hard as you can manage."
    $the_girl.call_dialogue("sex_responses_anal")
    mc.name "Ah, I'm going to cum!"
    if mc.condom:
        the_girl.char "Oh god do it! Show me how much you love my ass!"
    elif the_girl.get_opinion_score("creampies") > 0:
            the_girl.char "Yes! Shove it in deep [the_girl.mc_title]!"
    elif the_girl.sluttiness < 80:
        the_girl.char "Oh my god I can't believe I'm letting you do this..."
    else:
        the_girl.char "That's it baby, cum for me! Show me how much you love my ass!"

    menu:
        "Cum inside of her.":
            if mc.condom:
                "You pull back on [the_girl.possessive_title]'s hips and drive your cock deep inside of her as you cum."
                "She gasps with every final thrust as you fill your condom, which is slowly expanding inside her to accomodate your seed."
                if the_girl.get_opinion_score("bareback sex") > 0:
                    the_girl.char "Oh god, imagine if you weren't wearing that fucking rubber! I could feel you filling me up..."
                else:
                    the_girl.char "That's it, cum deep!"
                "You wait until your orgasm has passed completely, then pull out and sit back. Her asshole gapes slightly. You condom is full of your potent seed."
                if SB_check_fetish(the_girl, cum_internal_role):
                    "[the_girl.possessive_title] quickly reachs back and grabs your cock. She hastily pulls your condom off, careful not to spill a drop."
                    the_girl.char "I'm not letting a drop of this delicious cum go to waste!"
                    "She brings the condom to her mouth and drains it all into her mouth in one quick motion. You can see her pupils dilate as she feeds her cum fetish."
                    "She turns the condom inside out and licks the inside of it, desperate to get every drop of cum she possibly can."
                elif the_girl.get_opinion_score("drinking cum") > 0 and the_girl.sluttiness > 50:
                    $ the_girl.discover_opinion("drinking cum")
                    "[the_girl.possessive_title] reaches over for your cock. With delicate fingers she slides the condom off of you, pinching it off do your cum doesn't spill out."
                    the_girl.char "It would be a shame to waste all of this, right?"
                    "She smiles and brings the condom to her mouth. She tips the bottom up and drains it into her mouth."
                    $ the_girl.change_slut_temp(the_girl.get_opinion_score("drinking cum"))
                else:
                    "[the_girl.possessive_title] reaches over for your cock, removes the condom, and ties the end in a knot for you."
                    the_girl.char "Mmmm, look at all that cum. I guess that means my ass was pretty good!"
                return
            "[the_girl.possessive_title]'s ass is just too good. You decide to cum inside it."
            "You pull back on [the_girl.possessive_title]'s hips and drive your cock deep inside of her as you cum. She gasps softly in time with each new shot of hot semen inside of her."
            if the_girl.get_opinion_score("creampies") > 0:
                the_girl.char  "Yes! Fill my ass with your cum!"
            if the_girl.arousal > 110:
                "You feel her bowel contracting around your dick as she also starts to orgasm."
                $ the_girl.change_happiness(5)
            $ cum_in_ass(the_girl)
            $ SB_anal_standing.redraw_scene(the_girl)
            if SB_check_fetish(the_girl, cum_internal_role):
                "[the_girl.possessive_title]'s body goes rigid as your cum poors into her ass. Goosebumps erupt all over her body as her brain registers her creampie."
                the_girl.char "Oh.. OH! Yes [the_girl.mc_title]! Pump it deep! You were meant to cum inside me!"
                "[the_girl.possessive_title] revels in having her cum fetish fulfilled."
            elif the_girl.get_opinion_score("creampies") > 0:
                the_girl.char "Oh god... its inside me... right where it belongs. Thank you so much [the_girl.mc_title]!"
            elif the_girl.sluttiness > 110:
                the_girl.char "Oh god it's so good. It doesn't matter which hole you do it in, I love it when you cum inside me."
            else:
                the_girl.char "Oh fuck, I can't believe I let you cum in my ass..."

            "You wait until your orgasm has passed completely, then pull out and sit back. Her asshole gapes slightly and you can see a hint of your cum start to dribble out, but most of it stays buried with her bowel"

        "Cum on her ass.":
            if mc.condom:
                "You pull out of [the_girl.possessive_title] at the last moment, pulling your condom off as your blow your load all over her ass."
                "She holds still for you as you cover her with your sperm."
            else:
                "You pull out of [the_girl.possessive_title] at the last moment, stroking your shaft as you blow your load over her ass. She holds still for you as you cover her with your sperm."
            if the_girl.get_opinion_score("being covered in cum") > 0:
                 the_girl.char "Yes! Paint me with your sticky cum!"
            $ the_girl.cum_on_ass()
            $ SB_anal_standing.redraw_scene(the_girl)
            if SB_check_fetish(the_girl, cum_external_role):
                "[the_girl.possessive_title]'s body goes rigid as your cum coats her ass. Goosebumps erupt all over her body as her brain registers your cum on her skin."
                "[the_girl.possessive_title] revels in bliss as your dick sprays jet after jet of seed across her ass. She moans lewdly."
                "She truly is addicted to your cum."
            elif the_girl.sluttiness > 120:
                the_girl.char "Oh god your seed is so hot! Does it look sexy, having it plastered all over my ass?"
                "She reaches back and runs a finger through the puddles of cum you've put on her, then licks her finger clean."
            else:
                the_girl.char "Oh! Its so warm..."
            "You sit back and sigh contentedly, enjoying the sight of [the_girl.possessive_title]'s ass covered in your semen."
        "Cum on her face.":
            mc.name "Fuck, get ready [the_girl.title], I wanna cum on your face!"
            if mc.condom:
                "You pull your cock out of [the_girl.possessive_title]'s ass with a satisfying pop. You pull your condom off as she turns around on gets on her knees in front of you."
            else:
                "You pull your cock out of [the_girl.possessive_title]'s ass with a satisfying pop. She immediately turns around on gets on her knees in front of you."
            $ the_girl.draw_person(position = "blowjob")
            if the_girl.get_opinion_score("being covered in cum") > 0 or the_girl.get_opinion_score("cum facials") > 0:
                "[the_girl.possessive_title] reaches up and immediately begins stroking you off for you final few seconds."
                "Your orgasm hits hard. Your first jet sprays across her face."
                $ the_girl.cum_on_face()
                $ the_girl.draw_person(position = "blowjob")
                if SB_check_fetish(the_girl, cum_external_role):
                    "You can see [the_girl.possessive_title]'s pupils dilate as you fulfil her cum fetish."
                    "[the_girl.possessive_title] revels in bliss as your dick sprays jet after jet of seed across her face. She moans lewdly."
                    "She truly is addicted to your cum."
                else:
                    "[the_girl.possessive_title] moans as your dick sprays jet after jet of seed across her face."
            elif the_girl.sluttiness > 80:
                "[the_girl.possessive_title] sticks out her tongue for you and holds still, eager to take your hot load."
                $ the_girl.cum_on_face()
                $ the_girl.draw_person(position = "blowjob")
                "You let out a shudder moaning as you cum, pumping your sperm onto [the_girl.possessive_title]'s face and into her open mouth. She makes sure to wait until you're completely finished."
                the_girl.char "Oh god... it feels so good on my skin..."
            elif the_girl.sluttiness > 60:
                "[the_girl.possessive_title] closes her eyes and waits patiently for you to cum."
                $ the_girl.cum_on_face()
                $ the_girl.draw_person(position = "blowjob")
                "You let out a shudder moaning as you cum, pumping your sperm onto [the_girl.possessive_title]'s face. She waits until she's sure you're finished, then opens one eye and looks up at you."
            else:
                "[the_girl.possessive_title] closes her eyes and turns away, presenting her cheek to you as you finally climax."
                $ the_girl.cum_on_face()
                $ the_girl.draw_person(position = "blowjob")
                "You let out a shudder moaning as you cum, pumping your sperm onto [the_girl.possessive_title]'s face. She flinches as the first splash of warm liquid lands on her cheek, but doesn't pull away entirely."
            "You take a deep breath to steady yourself once you've finished orgasming. [the_girl.possessive_title] looks up at you from her knees, face covered in your semen."
            $ the_girl.call_dialogue("cum_face")


    return


label transition_default_SB_anal_standing(the_girl, the_location, the_object, the_round):
    "[the_girl.possessive_title] turns and puts her hands on [the_object.name]. You bounce your hard shaft on her ass a couple of times before lining yourself up with her sphincter."
    "Once you're both ready you push yourself forward, slipping your hard shaft deep inside of her. She lets out a gasp under her breath."
    return

label transition_SB_anal_standing_doggy_anal(the_girl, the_location, the_object, the_round):
    mc.name "Get down on your knees [the_girl.title], i'm going to fuck you like the little bitch you are."
    the_girl.char "Oh yes, [the_girl.mc_title], make me your little bitch."
    return

label transition_SB_anal_standing_SB_doggy_standing(the_girl, the_location, the_object, the_round):
    "You pull out of [the_girl.title]'s asshole, leaving it gaping and her sighing in relief."
    "You shift your cock downwards and rub the tip of it along the slit of her vagina."
    if the_girl.effective_sluttiness() < the_girl.get_no_condom_threshold():
        the_girl.char "Mmm, fuck me [the_girl.mc_title]. Use all of my holes for your pleasure!"
        $ wants_condom = False
    else:
        the_girl.char "Wait, wait... I can't risk getting pregnant, I need you to put on a condom."
        $ wants_condom = True

    if wants_condom and not mc.condom:
        menu:
            "Put on a condom.":
                "You pull your dick back and quickly put on a condom. Then you line up your dick with her dripping wet pussy."

            "Ram it home!":
                if wants_condom:
                    mc.name "Don't worry, I'll pull out."
                    $ the_girl.change_happiness(-5)
                else:
                    pass

    "You grab her by the hips and thrust yourself deep inside her tight, pulsating pussy."
    return    

label strip_SB_anal_standing(the_girl, the_clothing, the_location, the_object, the_round):
    "[the_girl.possessive_title] leans forward a little further and pops off your cock."
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing, position =  SB_anal_standing.position_tag)
    "[the_girl.possessive_title] struggles out of her [the_clothing.name] and throws it to the side. Then she gets herself lined up in front of you again."
    "She groans happily when you push back inside of her."
    return

label strip_ask_SB_anal_standing(the_girl, the_clothing, the_location, the_object, the_round):
    the_girl.char "Sir, I'd like to take off my [the_clothing.name], would you mind?"
    "[the_girl.char] pants as you fuck her from behind."
    menu:
        "Let her strip.":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = SB_anal_standing.position_tag)
            "[the_girl.possessive_title] struggles out of her [the_clothing.name] and throws it to the side. Then she gets herself lined up in front of you again."
            "She groans happily when you push back inside of her."

        "Leave it on.":
            mc.name "No, I like how you look with it on."
            if the_girl.sluttiness < 80:
                the_girl.char "Do you think I look sexy in it?"
                "You speed up, fucking her faster in response to her question."
            elif the_girl.sluttiness < 100:
                the_girl.char "Does it make me look like a good little slut? All I want to be is your good little slut sir."
                "She pushes her hips back into you and moans happily."
            else:
                the_girl.char "Does it make me look like the cum hungry slut that I am? Or is it your cock in my ass that makes me look that way?"
                "She grinds her hips back into you and moans ecstatically."
    return


label orgasm_SB_anal_standing(the_girl, the_location, the_object, the_round):
    "[the_girl.possessive_title]'s legs start to quiver, and then suddenly she tenses up."
    $ the_girl.call_dialogue("climax_responses_anal")
    "You bury your cock in deep in [the_girl.possessive_title]'s ass while she cums. Her bowel grips you tightly."
    "After a couple of seconds [the_girl.possessive_title] sighs and the tension drains from her body."
    if the_girl.get_opinion_score("anal sex") < 0:
        the_girl.char "I can't believe that just happened... oh god now you're going to keep going, aren't you?"
    else:
        the_girl.char "Don't stop... it still feels so good!"
    return



init:
    python:
        def cum_in_ass(the_girl):
            mc.listener_system.fire_event("sex_cum_ass", the_person = the_girl)
            the_girl.change_slut_temp(5*the_girl.get_opinion_score("creampies"))
            the_girl.change_happiness(5*the_girl.get_opinion_score("creampies"))
            the_girl.discover_opinion("creampies")

            the_girl.change_slut_temp(5*the_girl.get_opinion_score("anal sex"))
            the_girl.change_happiness(5*the_girl.get_opinion_score("anal sex"))
            the_girl.discover_opinion("anal sex")

            return
