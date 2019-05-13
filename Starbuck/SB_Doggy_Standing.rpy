init:
    python:
        SB_doggy_standing = Position("Standing Doggy",70,90,"standing_doggy","Low","Vagina","Vaginal",20,20,[],
        "intro_SB_doggy_standing",
        ["scene_SB_doggy_standing_1","scene_SB_doggy_standing_2"],
        "outro_SB_doggy_standing",
        "transition_default_SB_doggy_standing",
        "strip_SB_doggy_standing", "strip_ask_SB_doggy_standing",
        "orgasm_SB_doggy_standing",
        opinion_tags = ["doggy style sex" "vaginal sex" "sex standing up"])
        list_of_positions.append(SB_doggy_standing)

#init 1:
    #python:
        #SB_doggy_standing.link_positions_two_way(doggy, "transition_SB_doggy_standing_doggy", "transition_doggy_SB_doggy_standing")

label intro_SB_doggy_standing(the_girl, the_location, the_object, the_round):
    "You turn [the_girl.title] around, and she leans over [the_object.name], presenting her ass to you."
    mc.name "Good girl, [the_girl.title], I'm going to fuck you hard."
    if the_girl.get_opinion_score("doggy style sex") > 2 :
        the_girl.char "Oh thank god, I've been day dreaming about you bending me over all day long."
    elif the_girl.get_opinion_score("sex standing up") > 2 :
        the_girl.char "Oh thank god, I've been day dreaming about this all day long."
    elif the_girl.get_opinion_score("doggy style sex") > 0 :
        the_girl.char "I can't wait! It's so good when you bend me over."
    elif the_girl.effective_sluttiness() > 80:
        the_girl.char "Oh god I love it when you do this to me..."
    elif the_girl.effective_sluttiness() > 60:
        the_girl.char "Mmmm, this is gonna be fun."
    else:
        the_girl.char "Okay [mc.name], I'll play along this time."

    if the_girl.arousal > 60:
        "You rub the tip of your cock against [the_girl.title]'s cunt, feeling how nice and wet she is already. She moans, anticipating your penetration."
        "You continue to rub your dick against her pussy and gather more of her juices. She is already so wet you are soon slick with her secretions"
    else:
        "You rub the tip of your cock against [the_girl.title]'s cunt."
    "When you're ready you push forward. Her pussy feels amazing wrapped around your erection."
    if the_girl.get_opinion_score("doggy style sex") > 0 :
        the_girl.char "Oh my god..."
        $ the_girl.discover_opinion("doggy style sex")
    if the_girl.get_opinion_score("sex standing up") > 0 :
        "Her legs shake a bit as she gets used to the depth of your penetration."
        $ the_girl.change_arousal(5)
        $ the_girl.discover_opinion("sex standing up")
    return

label scene_SB_doggy_standing_1(the_girl, the_location, the_object, the_round):
    "Your hips slap against [the_girl.title]'s ass as you fuck her vigorously."
    $ the_girl.call_dialogue("sex_responses")
    if the_girl.sex_skills["Vaginal"] < 2: #Inexperienced
        "After a particularly hard thrust, [the_girl.title] reflexively starts to pull away. You grab her hips to keep her from pulling off completely."
        the_girl.char "I'm sorry [mc.name], thats a little too rough. Can you go a little slower?"
        "You pull her hips back toward you slowly. She sighs, still trying to get accustomed to your girth, penetrating her at such a deep angle."
        "The next time you push yourself in you push a little faster. She seems to be adapting to your fucking."
    elif SB_get_fetish(the_girl) == "Vaginal Fetish":          #vaginal fetish
        "After a particularly hard thrust, [the_girl.title] moans lewdly."
        the_girl.char "That's it, fuck me harder! God I can't imagine going a single day without your cock inside me..."
        "With one hand on her hip to control the pace, you grope and worship her ass cheeks with the other hand."
        "[the_girl.title] rocks her hips side to side each time you slam into her. Each time you pull back you can see her labia clinging to you."
        "You use both hands to grab her hips and slam yourself into her as deep as you can go."
        "Buried deep inside, you give her ass a smack. Her pussy trembles and caresses you in response."
    else:
        "Fucking her hard, [the_girl.title] moans, matching each hip movement of yours with movement of her own."
        the_girl.char "Oh god, you fuck me so good, I can barely keep up!"
        "[the_girl.title] reaches back with one hand and pulls an ass cheek back, giving you a great view of her pussy stretched wide to accomodate you."
        "Buried deep inside, you give her ass a smack. Her pussy trembles and caresses you in response."
    menu:
        "Spank her":
            "With your erection buried deep inside her, you give her ass a firm spank. Her sexy cheeks quake in response."
            mc.name "[the_girl.title], your ass looks amazing when I spank it. You are such a slut. I bet you love it don't you?"
            if the_girl.get_opinion_score("being submissive") > 0 or the_girl.obedience > 130:
                "[the_girl.title] moans at your words."
                "You pull her ass cheeks apart. You give her a hard spank with your other hand and enjoy the feeling of her silky cunt."
                mc.name "Do you let any guy with a hard cock fuck you and spank you like this? Or just me?"
                "[the_girl.title] responds quietly."
                the_girl.char "Just you, [mc.name]. I don't know why but it just feels so good... so right when you dominate me..."
                if the_girl == mom:
                    the_girl.char "It makes mommy so happy to serve you like this... To be your milfy slut!"
                "You give her pussy a few rough thrusts before bottoming out again."
                mc.name "That's right bitch, you're my little fuckhole. I'll bend you over and fuck you anytime I please."
                $ the_girl.discover_opinion("being submissive")
                $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive") * 3 + 5)
            else:
                the_girl.char "Mmm, it feels good but kinda hurts... could you hit a little more softly?"
                "You give her plaint ass another swat, this time not quite as hard."
                "Her ass quivers slightly as you spank her. Her pussy clenches around you each time you spank her."
            if mc.arousal > 70:
                "[the_girl.title]'s' tight pussy feels so good. You are getting close to cumming."
                mc.name "You feel amazing. You're gonna make me cum soon."
                if the_girl.get_opinion_score("creampies") > 0 or the_girl.get_opinion_score("risking getting pregnant") > 0:
                    "[the_girl.title] looks back at you and smiles."
                    the_girl.char "Oh [mc.name], I can't wait to feel you fill me up. I hope you finish deep!"
                    "[the_girl.title]'s ass quivers a bit, as she imagines you cumming deep inside her."
                    $ the_girl.discover_opinion("creampies")
                    $ the_girl.discover_opinion("risking getting pregnant")
                    $ the_girl.change_arousal(5)
                    if the_girl.get_opinion_score("being covered in cum") > 0:
                        the_girl.char "You could always pull out too... your cum feels so good when it splashes all over my skin..."
                        $ the_girl.discover_opinion("being covered in cum")
                        $ the_girl.change_arousal(the_girl.get_opinion_score("being covered in cum") * 3)
                        if the_girl.get_opinion_score("cum facials") > 0:
                            the_girl.char "Or my face! You haven't cum on my face in a while either..."
                            $ the_girl.discover_opinion("cum facials")
                            $ the_girl.change_arousal(the_girl.get_opinion_score("cum facials") * 3)
                            "[the_girl.title] starts muttering to herself, fantasizing about all the different ways you could cum on, or in her."
            "You put your hands on her hips and continue fucking her."



        "Play with her clit":
            "You lean forward a bit and reach down with one hand and begin to move it in circles around her clit."
            if the_girl.get_opinion_score("being fingered"):
                "[the_girl.title] moans loudly in response."
                the_girl.char "Oh [mc.name], I love when you touch me there."
                "You slide your fingers around her slit a few times."
                "You give your hips a few long, slow strokes as your circle her clit with your fingers."
                $ the_girl.discover_opinion("being fingered")
                $ the_girl.change_arousal(the_girl.get_opinion_score("being fingered") * 3 + mc.sex_skills["Foreplay"])
                "She really enjoys the extra stimulation."
                if the_girl.arousal > 80:
                    "You can feel her juices dripping down from her slit in response to your touch."
            elif mc.sex_skills["Foreplay"] > 4:
                "[the_girl.title] moans in response."
                "After a few moments of stimulation, she starts to move her hips back and forth, stirring your dick inside her."
                $ the_girl.change_arousal(mc.sex_skills["Foreplay"])
                if the_girl.arousal > 80:
                    "You can feel her juices dripping down from her slit in response to your touch."

            else:
                "[the_girl.title] moans in response."
                "After a few moments of stimulation, she starts to move her hips back and forth, stirring your dick inside her."
                $ the_girl.change_arousal(mc.sex_skills["Foreplay"])
                if the_girl.arousal > 80:
                    "You can feel her juices dripping down from her slit in response to your touch."
            if the_girl.arousal > 90:
                the_girl.char "Oh fuck! Don't stop! Don't you dare stop!"
                "Her moans clearly indicate an impending orgasm. As best as you can, you fuck her while you roughly rub her clit."
            else:
                "After a bit longer of touching her, you straighten your back and begin to rock your hips again, continuing to fuck her."
    return


label scene_SB_doggy_standing_2(the_girl, the_location, the_object, the_round):
    "You take a breather and slow up the pace a bit."
    if the_girl.outfit.tits_available():
        "You reach around her body with one hand and grasp her tit. You pinch and pull at her nipple roughly as you fuck her saturated slit."
    else:
        "You run your hands along her hips. You grab her hips and smack her ass roughly as you fuck her saturated slit."

    if the_girl.arousal > 130:
        the_girl.char "Ohhh my god, I already came... and you're still fucking me!"
        "[the_girl.title]'s legs are shaking. Her orifice clenches and spasms around you."
        "Her pussy spasming around you feels spectacular."
        $ mc.change_arousal(5)
    elif the_girl.arousal > 80:
        the_girl.char "Ohhh, [mc.name]... You are gonna make me cum so hard..."
        "You can feel a slight quiver in [the_girl.title]'s body as you fuck her. She's probably going to cum soon!"
    else:
        "[the_girl.title] groans in response to one particularly deep thrust."
        the_girl.char "It's so big... it feels so good buried inside me."
    "You push yourself in as deep as you can go. [the_girl.title] moans as you fill her completely."
    menu:
        "Gentle Sex":
            "You grasp her ass with both hands and begin to grope her. You kneed her cheeks as your hips slowly work your erection in and out of her."
            mc.name "[the_girl.title], your pussy is so good. I love how eager you are to fuck me."
            if SB_get_fetish(the_girl) == "Vaginal Fetish":
                the_girl.char "I love being your little slut! Fuck me good [mc.name]!"
            elif the_girl.sluttiness > 80:
                the_girl.char "Of course I'm eager. Your cock fills me just right. Fuck me good [mc.name]!"
            else:
                the_girl.char "Mmm, I can't help it, you make me feel so good."
        "Rough Sex":
            "You take one hand and start to need the back of her scalp. You grab a fistful of hair and pull."
            "[the_girl.title] arches her back in response."
            mc.name "That's a good slut. Take it nice and deep."
            if the_girl.get_opinion_score("being submissive") > 0 or the_girl.obedience > 130:
                "[the_girl.title] moans enthusiastically."
                the_girl.char "[mc.name]! I love it deep. Fuck me good!"
                "[the_girl.title] begs you for more."
                "You give her what she wants. You grab her hips and start thrusting into her hard and fast."
                $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive") * 3 + 3)
            elif the_girl.get_opinion_score("being submissive") < 0 :
                "[the_girl.title] looks back at you with a scowl."
                the_girl.char "Don't get used to it, [mc.name]... I'm not sure how I let you talk me into this..."
                $ the_girl.discover_opinion("being submissive")
                "You let go of her hair and decide for now to keep your pace nice and slow."
            else:
                "[the_girl.title] moans."
                the_girl.char "You are so deep... It feels good having you so deep inside me."
                "You stir the depths of her pussy with your erection by moving your hips side to side."

    return


label outro_SB_doggy_standing(the_girl, the_location, the_object, the_round):
    "[the_girl.title]'s creamy cunt draws you closer to your orgasm with each thrust. You finally pass the point of no return and speed up, fucking her as hard as you can manage."
    $the_girl.call_dialogue("sex_responses")
    mc.name "Ah, I'm going to cum!"
    if the_girl.get_opinion_score("creampies") > 0:
        the_girl.char "Yes! Shove it in deep [mc.name]!"
    if the_girl.get_opinion_score("risking getting pregnant") > 0:
        the_girl.char "Don't let a drop of that seed go to waste!"
    else:
        the_girl.char "That's it, cum for me!"

    menu:
        "Cum inside of her.":
            "[the_girl.title]'s drenched cunt is just too good. You decide to cum inside it."
            "You pull back on [the_girl.title]'s hips and drive your cock as deep inside of her as you cum. She gasps softly in time with each new shot of hot semen inside of her."
            if the_girl.get_opinion_score("creampies") > 0:
                the_girl.char  "Yes! Fill my ass with your cum!"
            if the_girl.arousal > 110:
                "You feel her pussy spasming around your dick as she also starts to orgasm."
                $ the_person.change_happiness(5)
            $ the_girl.cum_in_vagina()
            $ SB_doggy_standing.redraw_scene(the_girl)
            if SB_get_fetish(the_girl) == "Internal Cum Fetish":
                "[the_girl.title]'s body goes rigid as your cum poors into her pussy. Goosebumps erupt all over her body as her brain registers her creampie."
                the_girl.char "Oh.. OH! Yes [mc.name]! Pump it deep! I was made to take your cum inside me!"
                "[the_girl.title] revels in having her cum fetish fulfilled."
            if the_girl.get_opinion_score("risking getting pregnant") > 0:
                the_girl.char "Oh god... I can feel it so deep. I mean... it could... hopefully..."
                "[the_girl.title]'s voice starts to trail off."
            elif the_girl.sluttiness > 110:
                the_girl.char "Oh god it's so deep."
            else:
                the_girl.char "Oh fuck...  Good thing I'm on the pill..."



            "You wait until your orgasm has passed completely, then pull out and stand back."

            if the_girl.get_opinion_score("risking getting pregnant") > 0:
                "As your cum starts to leak out, [the_girl.title] reaches back and tries to keep it inside with her hand."
            else:
                "You cum leaks out of her well used pussy."

        "Cum on her ass.":
            "You pull out of [the_girl.title] at the last moment, stroking your shaft as you blow your load over her ass. She holds still for you as you cover her with your sperm."
            if the_girl.get_opinion_score("being covered in cum") > 0:
                 the_girl.char "Yes! Paint me with your sticky cum!"
            $ the_girl.cum_on_ass()
            $ SB_doggy_standing.redraw_scene(the_girl)
            if SB_get_fetish(the_girl) == "External Cum Fetish":
                "[the_girl.title]'s body goes rigid as your cum coats her ass. Goosebumps erupt all over her body as her brain registers your cum on her skin."
                "[the_girl.title] revels in bliss as your dick sprays jet after jet of seed across her ass. She moans lewdly."
                "She truly is addicted to your cum."
            if the_girl.sluttiness > 120:
                the_girl.char "Oh god your seed is so hot! Does it look sexy, having it plastered all over my ass?"
                "She reaches back and runs a finger through the puddles of cum you've put on her, then licks her finger clean."
            else:
                the_girl.char "Oh! Its so warm..."
            "You sit back and sigh contentedly, enjoying the sight of [the_girl.title]'s ass covered in your semen."
        "Cum on her face.":
            mc.name "Fuck, get ready [the_girl.title], I wanna cum on your face!"
            "You pull your cock out of [the_girl.title]. She immediately turns around on gets on her knees in front of you."
            $ the_girl.draw_person(position = "blowjob")
            if the_girl.get_opinion_score("being covered in cum") > 0 or the_girl.get_opinion_score("cum facials") > 0:
                "[the_girl.title] reaches up and strokes you off for your final few seconds."
                "Your orgasm hits hard. Your first jet sprays across her face."
                $ the_girl.cum_on_face()
                $ the_girl.draw_person(position = "blowjob")
                if SB_get_fetish(the_girl) == "External Cum Fetish":
                    "You can see [the_girl.title]'s pupils dilate as you fulfil her cum fetish."
                    "[the_girl.title] revels in bliss as your dick sprays jet after jet of seed across her face. She moans lewdly."
                    "She truly is addicted to your cum."
                else:
                    "[the_girl.title] moans as your dick sprays jet after jet of seed across her face."
            elif the_girl.sluttiness > 80:
                "[the_girl.title] sticks out her tongue for you and holds still, eager to take your hot load."
                $ the_girl.cum_on_face()
                $ the_girl.draw_person(position = "blowjob")
                "You let out a shudder moaning as you cum, pumping your sperm onto [the_girl.title]'s face and into her open mouth. She makes sure to wait until you're completely finished."
                the_girl.char "Oh god... it feels so good on my skin..."
            elif the_girl.sluttiness > 60:
                "[the_girl.title] closes her eyes and waits patiently for you to cum."
                $ the_girl.cum_on_face()
                $ the_girl.draw_person(position = "blowjob")
                "You let out a shudder moaning as you cum, pumping your sperm onto [the_girl.title]'s face. She waits until she's sure you're finished, then opens one eye and looks up at you."
            else:
                "[the_girl.title] closes her eyes and turns away, presenting her cheek to you as you finally climax."
                $ the_girl.cum_on_face()
                $ the_girl.draw_person(position = "blowjob")
                "You let out a shudder moaning as you cum, pumping your sperm onto [the_girl.title]'s face. She flinches as the first splash of warm liquid lands on her cheek, but doesn't pull away entirely."
            "You take a deep breath to steady yourself once you've finished orgasming. [the_girl.title] looks up at you from her knees, face covered in your semen."
            $ the_girl.call_dialogue("cum_face")


    return


label transition_default_SB_doggy_standing(the_girl, the_location, the_object, the_round):
    "[the_girl.title] turns and puts her hands on [the_object.name]. You bounce your hard shaft on her ass a couple of times before lining yourself up with her pussy."
    "Once you're both ready you push yourself forward, slipping your hard shaft deep inside of her. She lets out a gasp under her breath."
    return

label strip_SB_doggy_standing(the_girl, the_clothing, the_location, the_object, the_round):
    "[the_girl.title] leans forward a little further and pops off your cock."
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing, position =  SB_doggy_standing.position_tag)
    "[the_girl.title] struggles out of her [the_clothing.name] and throws it to the side. Then she gets herself lined up in front of you again."
    "She groans happily when you push back inside of her."
    return

label strip_ask_SB_doggy_standing(the_girl, the_clothing, the_location, the_object, the_round):
    the_girl.char "Sir, I'd like to take off my [the_clothing.name], would you mind?"
    "[the_girl.char] pants as you fuck her from behind."
    menu:
        "Let her strip.":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = SB_doggy_standing.position_tag)
            "[the_girl.title] struggles out of her [the_clothing.name] and throws it to the side. Then she gets herself lined up in front of you again."
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
                the_girl.char "Does it make me look like the cum hungry slut that I am? Or is it your cock inside me that makes me look that way?"
                "She grinds her hips back into you and moans ecstatically."
    return


label orgasm_SB_doggy_standing(the_girl, the_location, the_object, the_round):
    "[the_girl.title]'s legs start to quiver, and then suddenly she tenses up."
    $ the_girl.call_dialogue("climax_responses")
    "You bury your cock in deep in [the_girl.title]'s cunt while she cums. Her pussy spasms around you."
    "After a couple of seconds [the_girl.title] sighs and the tension drains from her body."
    if the_girl.get_opinion_score("doggy style sex") > 0:
        the_girl.char "Oh god, you've got me bent over and it feels so good I'm just cumming all over you..."
    the_girl.char "Don't stop... it still feels so good!"
    return
