init:
    python:
        SB_anal_standing = Position("Standing Anal",70,95,"standing_doggy","Low","Vagina","Anal",18,18,[],
        "intro_SB_anal_standing",
        ["scene_SB_anal_standing_1","scene_SB_anal_standing_2"],
        "outro_SB_anal_standing",
        "transition_default_SB_anal_standing",
        "strip_SB_anal_standing", "strip_ask_SB_anal_standing",
        "orgasm_SB_anal_standing",
        opinion_tags = ["doggy style sex" "anal sex" "sex standing up"])
        list_of_positions.append(SB_anal_standing)

#init 1:
    #python:
        #SB_anal_standing.link_positions_two_way(doggy, "transition_SB_anal_standing_doggy", "transition_doggy_SB_anal_standing")

label intro_SB_anal_standing(the_girl, the_location, the_object, the_round):
    "With you arms wrapped around [the_girl.name], you make out for a bit with her back to the [the_object.name]"
    "You turn her around, and she leans over [the_object.name], presenting her ass to you."
    mc.name "That's it, [the_girl.name], I'm going to fuck your ass today."
    if SB_get_fetish(the_girl) == "Anal Fetish":
        the_girl.char "Oh thank god, I've been day dreaming about this all day long."
    elif the_girl.get_opinion_score("anal sex") > 0 :
        the_girl.char "I can't wait! It's so intense when you fuck me back there..."
    elif the_girl.effective_sluttiness() > 110:
        the_girl.char "Oh god I love it when you do this to me..."
    elif the_girl.effective_sluttiness() > 80:
        the_girl.char "Ok, just be careful [mc.name]..."
    else:
        the_girl.char "I don't know, are you sure that thing is gonna fit in me back there?"

    if SB_get_fetish(the_girl) == "Anal Fetish":
        if the_girl == mom:
            "You work your cock up and down your mom's slit a few times, her wetness lubricating it."
            "You lean forward and whisper into her ear."
            mc.name "Mommy... your little boy is about to fuck your ass now, just the way you like."
            "Her body shudders from your dirty talk. She wiggles her ass back up against you."
            the_girl.char "Do it honey. Mommy is ready for you!"
        elif the_girl == lily:
            "You work your cock up and down your sister's slit a few times, her wetness lubricating it."
            "You lean forward and whisper into her ear."
            mc.name "Hey sis, your big brother is about to fuck your ass now, just the way you like."
            "Her body shudders from your dirty talk. She wiggles her ass back up against you."
            the_girl.char "Do it! Stick it in me, you know I can take it!"
        else:
            "You slowly pull out the pink jewelled butt plug from [the_girl.name]'s rectum. She quivers in anticipation of what you are about to do to her."
            $ the_girl.change_arousal(the_girl.get_opinion_score("anal sex"))
            "You work a couple fingers into her bottom. It is clear she loves anal sex so much, she keeps herself lubed up with the plug in throughout the day hoping for you to come fuck it."
            "You decide to tease her before you put it in."
            mc.name "You're such a buttslut, [the_girl.name]. Are you sure you want it back there? Your pussy looks like it could use a proper fucking too..."
            "[the_girl.name] tries to push back against you and begins to beg."
            the_girl.char "No! I need you in my ass right now... I need the heat and intensity of you fucking my ass right now!"
            "When you're ready you push forward. Her back passage greedily accepts your erection, eliciting a satisfied sigh from [the_girl.name]"
    elif the_girl.arousal > 60:
        "You rub the tip of your penis against [the_girl.name]'s cunt, feeling how nice and wet she is already. You rub your lubricated penis against her ass to help prepare her for your initial penetration."
        "You rub your dick against her pussy again and gather more of her juices. She is already so wet you are soon slick with her secretions"
    else:
        "You line yourself up with her ass, but the lack of lubricant makes it impossible to push it in. You pull on her hair to bring her head back around to face you."
        "You put your other hand in front of her face and she quickly opens her mouth and sucks on them. [the_girl.name] slobbers all over your fingers for a few a seconds before you pull them out with a loud pop"
        "You use your fingers to crudely work in and out of her ass a few times to help get it lubricated."
        "Deciding against making her suck on your fingers again after they've been in her ass, you spit a couple times down on her ass to get a bit more lubrication so you can penetrate her"
    "When you're ready you slowly push forward. It takes several seconds of steady pressure until you finally bottom out."
    if the_girl.get_opinion_score("anal sex") > 0 :
        the_girl.char "Oh my god it's so dirty... but it is so good too..."
        $ the_girl.discover_opinion("anal sex")
    return

label scene_SB_anal_standing_1(the_girl, the_location, the_object, the_round):
    "Your hips slap against [the_girl.name]'s as you plunder her rectum."
    $ the_girl.call_dialogue("sex_responses")
    if the_girl.sex_skills["Anal"] < 2: #Inexperienced
        "After a particularly hard thrust, [the_girl.name] reflexively starts to pull away. You grab her hips to keep her from pulling off completely."
        the_girl.char "I'm sorry [mc.name], it hurts. Can you go a little slower?"
        "You pull her hips back toward you slowly. Her inexperienced ass yields to your penis and she sighs as you bottom out"
        "You pull yourself out a bit, then spit on her asshole and work it around a bit to provide a bit of extra lubrication."
        "Next time you push yourself in it goes in a bit easier, but you can tell she is having a hard time taking you in her back passage."
    elif SB_get_fetish(the_girl) == "Anal Fetish":           #Anal fetish
        "After a particularly hard thrust, [the_girl.name] moans lewdly."
        if the_girl == mom:
            the_girl.char "That's it honey, fuck me harder! God I wish I could walk around with you inside me all day..."
        elif the_girl == lily:
            the_girl.char "That's it bro! Fuck me harder! God I wish I could walk around with you inside me all day..."
        else:
            the_girl.char "That's it, fuck me harder! This is so much better than that plug, I wish I could walk around with you inside me all day..."
        "With one hand on her hip to control the pace, you grope and worship her ass cheeks with the other hand."
        "[the_girl.name] clenches each time you pull back, and relaxes each time your push forward. The sensation is exquisite."
        "You use both hands to grab her hips and slam yourself into her."
        "Buried deep inside, you stir your hips in a circular motion. Her rectum quivers and caresses you in response."
    else:
        "Fucking her hard, [the_girl.name] moans, matching each hip movement of yours with movement of her own."
        the_girl.char "Oh god, you fuck me so good, I can barely keep up!"
        "[the_girl.name] reaches back with one hand and pulls an ass cheek back, giving you a great view of her booty hole stretched wide to accomodate you."
        "Buried deep inside, you stir your hips in a circular motion. Her rectum quivers in response."
    menu:
        "Kneed her ass":
            "With your erection buried deep in her rump, you take both hands and kneed her ass cheeks."
            mc.name "[the_girl.name], your ass is so tight, I can't believe you let me sodomize you like this."
            if the_girl.get_opinion_score("being submissive") > 0 or the_girl.obedience > 130:
                "[the_girl.name] trembles at your words and touch. "
                "You pull her ass cheeks apart and revel in her ultimate submission, your cock in her forbidden hole."
                the_girl.char "I couldn't stop you from fucking me... any way you want... even if I wanted to..."
                "You reach forward and run a hand through her hair. You kneed her scalp for a few seconds, then grasp her hair and pull it towards you."
                mc.name "That's right bitch, you're here to pleasure me, when, how, and wherever I want."
                $ the_girl.discover_opinion("being submissive")
                $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive") * 3)
            elif the_girl.get_opinion_score("taking control") > 0 or the_girl.obedience < 80:
                "[the_girl.name] looks back at you and smiles."
                the_girl.char "It's definitely a... unique feeling [mc.name]. Maybe you should let me peg you sometime?"
                "You give [the_girl.name] a good, hard thrust in response."
                $ the_girl.discover_opinion("taking control")
            else:
                the_girl.char "I don't know what is about you, [mc.name]... I just want to make you feel good!"
                "You pull her ass cheeks apart. You give her a couple long, slow thrusts and enjoy the sight of your erection disappearing inside her bowel."
                if mc.arousal > 70:
                    "You moan at the sensations."
                    mc.name "You feel amazing. You're gonna make me cum soon."
                    if the_girl.get_opinion_score("creampies") > 0:
                        "[the_girl.name] looks back at you and smiles."
                        the_girl.char "Oh [mc.name], I can't wait to feel you fill me up. I hope you finish deep!"
                        "[the_girl.name]'s ass quivers a bit, as she imagines you cumming deep inside her."
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
                                "[the_girl.name] starts muttering to herself, fantasizing about all the different ways you could cum on, or in her."
            "You put your hands on her hips and resume your anal coupling."



        "Play with her clit":
            "You lean forward a bit and reach down with one hand and begin to move it in circles around her clit."
            if the_girl.get_opinion_score("being fingered"):
                "[the_girl.name] moans loudly in response."
                the_girl.char "Oh [mc.name], I love your hands on me... especially down there..."
                "You slide your middle finger along her slit a few times and then push up inside her pussy."
                "You give your hips a few long, slow strokes and you move your finger in time, penetrating both her holes at once."
                $ the_girl.discover_opinion("being fingered")
                $ the_girl.change_arousal(the_girl.get_opinion_score("being fingered") * 3 + mc.sex_skills["Foreplay"])
                "She really enjoys the extra stimulation."
            else:
                "[the_girl.name] moans in response."
                "After a few moments of stimulation, she starts to move her hips back and forth, stirring your dick inside her bowel."
                $ the_girl.change_arousal(mc.sex_skills["Foreplay"])
                if the_girl.arousal > 80:
                    "You can feel her juices dripping down from her slit in response to your touch."
            "After a bit longer of touching her, you straighten your back and begin to rock your hips again, continuing to fuck her ass."
    return


label scene_SB_anal_standing_2(the_girl, the_location, the_object, the_round):
    "[the_girl.name] quivers as you slow up the pace a bit. The sensation of burying yourself in her tight chute over and over is amazing."
    if the_girl.outfit.tits_available():
        "You reach around her body with one hand and grasp her tit. You pinch and pull at her nipple roughly as you plow her behind."
    else:
        "You run your hands along her hips. You grab her hips and smack her ass roughly as you plow her behind."

    if the_girl.arousal > 130:
        the_girl.char "Ohhh my god, its so good... I can't believe I came already..."
        "[the_girl.name]'s legs are shaking. She is thoroughly enjoying her anal plundering."
        if SB_get_fetish(the_girl) == "Anal Fetish":
            the_girl.char "This is it, this is why I love anal so much... I just can't stop cumming! It feels so good."
    elif the_girl.arousal > 80:
        the_girl.char "Ohhh, it feels so good. You're gonna make me cum like this... aren't you?"
        "You can feel a slight quiver in [the_girl.name]'s body as you fuck her. She's probably going to cum soon!"
    else:
        "[the_girl.name] groans in response to one particularly deep thrust."
        the_girl.char "It's so big... How does it even fit back there?"
    "You push yourself in as deep as you can go. [the_girl.name] moans as you fill her completely."
    menu:
        "Admire her":
            "You moan in appreciation."
            mc.name "[the_girl.name], your ass is so good. Your booty feels amazing."
            if SB_get_fetish(the_girl) == "Anal Fetish":
                the_girl.char "I love being your anal slut. Fuck me good [mc.name]!"
            elif the_girl.sluttiness > 80:
                the_girl.char "You are so big... its so full when you push it in me like this."
            else:
                the_girl.char "It better... I can't believe I let you talk me into this..."
        "Talk Dirty":
            mc.name "I love how your ass gets so stretched out with my cock fucking it."
            if SB_get_fetish(the_girl) == "Anal Fetish":
                "[the_girl.name] moans enthusiastically. She wiggles her hips back and forth, caressing your dick with her forbidden hole."
                the_girl.char "[mc.name]... fuck my ass... fuck me hard!"
                "You give her what she wants. You grab her hips and start thrusting into her hard and fast."
                the_girl.char "Oh [mc.name]... [mc.name]!"
                $ the_girl.change_arousal(the_girl.get_opinion_score("anal sex"))
                "[the_girl.name] is moaning your name over and over. You continue to give her the anal reeming she is begging for."

            elif the_girl.get_opinion_score("being submissive") > 0 or the_girl.obedience > 130:
                "[the_girl.name] moans enthusiastically."
                the_girl.char "[mc.name]... use me... fuck me! Make me your little slut!"
                "You give her what she wants. You grab her hips and start thrusting into her hard and fast."
                $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive") * 3 + 3)
                "You give her the anal reeming she is begging for."
            elif the_girl.get_opinion_score("anal sex") < 0 :
                "[the_girl.name] looks back at you with a scowl."
                the_girl.char "Don't get used to it, [mc.name]... I'm not sure how I let you talk me into this..."
                $ the_girl.discover_opinion("anal sex")
                "You decide for now to keep your pace nice a slow."
            else:
                "[the_girl.name] looks back at you and manages to smile throug the intense sensation of having her ass fucked."
                the_girl.char "You are stretching me out so much... Be careful back there, I'm not sure how much of this I can take!"
                "You reassure her, and then slowly begin to fuck her tightest hole again."

    return


label outro_SB_anal_standing(the_girl, the_location, the_object, the_round):
    "[the_girl.name]'s tight ass draws you closer to your orgasm with each thrust. You finally pass the point of no return and speed up, fucking her as hard as you can manage."
    $the_girl.call_dialogue("sex_responses")
    mc.name "Ah, I'm going to cum!"
    if the_girl.get_opinion_score("creampies") > 0:
            the_girl.char "Yes! Shove it in deep [mc.name]!"
    elif the_girl.sluttiness < 80:
        the_girl.char "Oh my god I can't believe I'm letting you do this..."
    else:
        the_girl.char "That's it baby, cum for me! Show me how much you love my ass!"

    menu:
        "Cum inside of her.":
            "[the_girl.name]'s ass is just too good. You decide to cum inside it."
            "You pull back on [the_girl.name]'s hips and drive your cock deep inside of her as you cum. She gasps softly in time with each new shot of hot semen inside of her."
            if the_girl.get_opinion_score("creampies") > 0:
                the_girl.char  "Yes! Fill my ass with your cum!"
            if the_girl.arousal > 110:
                "You feel her bowel contracting around your dick as she also starts to orgasm."
                $ the_girl.change_happiness(5)
            $ cum_in_ass(the_girl)
            $ SB_anal_standing.redraw_scene(the_girl)
            if SB_get_fetish(the_girl) == "Internal Cum Fetish":
                "[the_girl.name]'s body goes rigid as your cum poors into her ass. Goosebumps erupt all over her body as her brain registers her creampie."
                the_girl.char "Oh.. OH! Yes [mc.name]! Pump it deep! You were meant to cum inside me!"
                "[the_girl.name] revels in having her cum fetish fulfilled."
            elif the_girl.get_opinion_score("creampies") > 0:
                the_girl.char "Oh god... its inside me... right where it belongs. Thank you so much [mc.name]!"
            elif the_girl.sluttiness > 110:
                the_girl.char "Oh god it's so good. It doesn't matter which hole you do it in, I love it when you cum inside me."
            else:
                the_girl.char "Oh fuck, I can't believe I let you cum in my ass..."

            "You wait until your orgasm has passed completely, then pull out and sit back. Her asshole gapes slightly and you can see a hint of your cum start to dribble out, but most of it stays buried with her bowel"

        "Cum on her ass.":
            "You pull out of [the_girl.name] at the last moment, stroking your shaft as you blow your load over her ass. She holds still for you as you cover her with your sperm."
            if the_girl.get_opinion_score("being covered in cum") > 0:
                 the_girl.char "Yes! Paint me with your sticky cum!"
            $ the_girl.cum_on_ass()
            $ SB_anal_standing.redraw_scene(the_girl)
            if SB_get_fetish(the_girl) == "External Cum Fetish":
                "[the_girl.name]'s body goes rigid as your cum coats her ass. Goosebumps erupt all over her body as her brain registers your cum on her skin."
                "[the_girl.name] revels in bliss as your dick sprays jet after jet of seed across her ass. She moans lewdly."
                "She truly is addicted to your cum."
            elif the_girl.sluttiness > 120:
                the_girl.char "Oh god your seed is so hot! Does it look sexy, having it plastered all over my ass?"
                "She reaches back and runs a finger through the puddles of cum you've put on her, then licks her finger clean."
            else:
                the_girl.char "Oh! Its so warm..."
            "You sit back and sigh contentedly, enjoying the sight of [the_girl.name]'s ass covered in your semen."
        "Cum on her face.":
            mc.name "Fuck, get ready [the_girl.name], I wanna cum on your face!"
            "You pull your cock out of [the_girl.name]'s ass with a satisfying pop. She immediately turns around on gets on her knees in front of you."
            $ the_girl.draw_person(position = "blowjob")
            if the_girl.get_opinion_score("being covered in cum") > 0 or the_girl.get_opinion_score("cum facials") > 0:
                "[the_girl.name] reaches up and immediately begins stroking you off for you final few seconds."
                "Your orgasm hits hard. Your first jet sprays across her face."
                $ the_girl.cum_on_face()
                $ the_girl.draw_person(position = "blowjob")
                if SB_get_fetish(the_girl) == "External Cum Fetish":
                    "You can see [the_girl.name]'s pupils dilate as you fulfil her cum fetish."
                    "[the_girl.name] revels in bliss as your dick sprays jet after jet of seed across her face. She moans lewdly."
                    "She truly is addicted to your cum."
                else:
                    "[the_girl.name] moans as your dick sprays jet after jet of seed across her face."
            elif the_girl.sluttiness > 80:
                "[the_girl.name] sticks out her tongue for you and holds still, eager to take your hot load."
                $ the_girl.cum_on_face()
                $ the_girl.draw_person(position = "blowjob")
                "You let out a shudder moaning as you cum, pumping your sperm onto [the_girl.name]'s face and into her open mouth. She makes sure to wait until you're completely finished."
                the_girl.char "Oh god... it feels so good on my skin..."
            elif the_girl.sluttiness > 60:
                "[the_girl.name] closes her eyes and waits patiently for you to cum."
                $ the_girl.cum_on_face()
                $ the_girl.draw_person(position = "blowjob")
                "You let out a shudder moaning as you cum, pumping your sperm onto [the_girl.name]'s face. She waits until she's sure you're finished, then opens one eye and looks up at you."
            else:
                "[the_girl.name] closes her eyes and turns away, presenting her cheek to you as you finally climax."
                $ the_girl.cum_on_face()
                $ the_girl.draw_person(position = "blowjob")
                "You let out a shudder moaning as you cum, pumping your sperm onto [the_girl.name]'s face. She flinches as the first splash of warm liquid lands on her cheek, but doesn't pull away entirely."
            "You take a deep breath to steady yourself once you've finished orgasming. [the_girl.name] looks up at you from her knees, face covered in your semen."
            $ the_girl.call_dialogue("cum_face")


    return


label transition_default_SB_anal_standing(the_girl, the_location, the_object, the_round):
    "[the_girl.name] turns and puts her hands on [the_object.name]. You bounce your hard shaft on her ass a couple of times before lining yourself up with her sphincter."
    "Once you're both ready you push yourself forward, slipping your hard shaft deep inside of her. She lets out a gasp under her breath."
    return

label strip_SB_anal_standing(the_girl, the_clothing, the_location, the_object, the_round):
    "[the_girl.name] leans forward a little further and pops off your cock."
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing, position =  SB_anal_standing.position_tag)
    "[the_girl.name] struggles out of her [the_clothing.name] and throws it to the side. Then she gets herself lined up in front of you again."
    "She groans happily when you push back inside of her."
    return

label strip_ask_SB_anal_standing(the_girl, the_clothing, the_location, the_object, the_round):
    the_girl.char "Sir, I'd like to take off my [the_clothing.name], would you mind?"
    "[the_girl.char] pants as you fuck her from behind."
    menu:
        "Let her strip.":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = SB_anal_standing.position_tag)
            "[the_girl.name] struggles out of her [the_clothing.name] and throws it to the side. Then she gets herself lined up in front of you again."
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
    "[the_girl.name]'s legs start to quiver, and then suddenly she tenses up."
    $ the_girl.call_dialogue("climax_responses")
    "You bury your cock in deep in [the_girl.name]'s ass while she cums. Her bowel grips you tightly."
    "After a couple of seconds [the_girl.name] sighs and the tension drains from her body."
    if the_girl.get_opinion_score("anal sex") < 0:
        the_girl.char "I can't believe that just happened... oh god now you're going to keep going, aren't you?"
    else:
        the_girl.char "Don't stop... it still feels so good!"
    return



init:
    python:
        def cum_in_ass(the_person):
            mc.listener_system.fire_event("sex_cum_ass", the_person = the_person)
            the_person.change_slut_temp(5*the_person.get_opinion_score("creampies"))
            the_person.change_happiness(5*the_person.get_opinion_score("creampies"))
            the_person.discover_opinion("creampies")

            the_person.change_slut_temp(5*the_person.get_opinion_score("anal sex"))
            the_person.change_happiness(5*the_person.get_opinion_score("anal sex"))
            the_person.discover_opinion("anal sex")

            return
