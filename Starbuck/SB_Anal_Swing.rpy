init:
    python:
        SB_anal_swing = Position("Swinging Anal",85,110,"sitting","Swing","Vagina","Anal",20,20,[],
        "intro_SB_anal_swing",
        ["scene_SB_anal_swing_1","scene_SB_anal_swing_2"],
        "outro_SB_anal_swing",
        "transition_default_SB_anal_swing",
        "strip_SB_anal_swing", "strip_ask_SB_anal_swing",
        "orgasm_SB_anal_swing",
        opinion_tags = ["doggy style sex" "anal sex" "sex standing up"])
        list_of_positions.append(SB_anal_swing)

#init 1:
    #python:
        #SB_anal_swing.link_positions_two_way(doggy, "transition_SB_anal_swing_doggy", "transition_doggy_SB_anal_swing")

label intro_SB_anal_swing(the_girl, the_location, the_object, the_round):
    "[the_girl.title] sits down in the [the_object.name]. Her ass is hanging off the back end."
    "You run your hands along her supple hips."
    if SB_get_fetish(the_girl) == "Anal Fetish":
        the_girl.char "Oh my god. This is so kinky... fuck me good [mc.name]!"
    elif the_girl.get_opinion_score("anal sex") > 0 :
        the_girl.char "I can't wait! It's so intense when you fuck me back there..."
    elif the_girl.effective_sluttiness() > 110:
        the_girl.char "Oh god I love it when you do this to me..."
    elif the_girl.effective_sluttiness() > 80:
        the_girl.char "Ok, just be careful [mc.name]..."
    else:
        the_girl.char "I don't know, are you sure this thing is safe?"

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
        elif the_girl == starbuck:
            "You work your cock up and down [the_girl.title]'s slit a few times, her wetness lubricating it."
            "You lean forward and whisper into her ear."
            mc.name "Baby... I'm going to fuck your ass now... just the way you like it!"
            "You can see goosebumps break out all over her body."
            the_girl.char "Oh god, I touch myself everytime I think about the first time you fucked in one of these at the shop."
            the_girl.char "Fuck me good, [mc.name]! I want it so bad!"
            $ the_girl.change_arousal(the_girl.get_opinion_score("anal sex"))
        else:
            "You slowly pull out the pink jewelled butt plug from [the_girl.title]'s rectum. She quivers in anticipation of what you are about to do to her."
            $ the_girl.change_arousal(the_girl.get_opinion_score("anal sex"))
            "You work a couple fingers into her bottom. It is clear she loves anal sex so much, she keeps herself lubed up with the plug in throughout the day hoping for you to come fuck it."
            "You decide to tease her before you put it in."
            mc.name "You're such a buttslut, [the_girl.title]. Are you sure you want it back there? Your pussy looks like it could use a proper fucking too..."
            "[the_girl.title] begs you not to stick it in her pussy."
            the_girl.char "No! I need you in my ass right now... I need the heat and intensity of you fucking my ass please!"
            "When you're ready you push forward. Her back passage greedily accepts your erection, eliciting a satisfied sigh from [the_girl.title]"
    elif the_girl.arousal > 60:
        "You rub the tip of your penis against [the_girl.title]'s cunt, feeling how nice and wet she is already. You rub your lubricated penis against her ass to help prepare her for your initial penetration."
        "You rub your dick against her pussy again and gather more of her juices. She is already so wet you are soon slick with her secretions"
    else:
        "You line yourself up with her ass, but the lack of lubricant makes it impossible to push it in. You pull on her hair to bring her head back around to face you."
        "You put your other hand in front of her face and she quickly opens her mouth and sucks on them. [the_girl.title] slobbers all over your fingers for a few a seconds before you pull them out with a loud pop"
        "You use your fingers to crudely work in and out of her ass a few times to help get it lubricated."
        "Deciding against making her suck on your fingers again after they've been in her ass, you spit a couple times down on her ass to get a bit more lubrication so you can penetrate her"
    "When you're ready you slowly push forward. It takes several seconds of steady pressure until you finally bottom out."
    if the_girl.get_opinion_score("anal sex") > 0 :
        the_girl.char "Oh my god it's so dirty... but it is so good too..."
        $ the_girl.discover_opinion("anal sex")
    return

label scene_SB_anal_swing_1(the_girl, the_location, the_object, the_round):
    "Your hips slap against [the_girl.title]'s as you plunder her rectum. You keep a slow but steady pace."
    "With each bounce in the swing, [the_girl.title]'s ass pulls off you almost completely, but you grab the ropes of the swing and forcefully slam her ass back into you."
    $ the_girl.call_dialogue("sex_responses")

    if SB_get_fetish(the_girl) == "Anal Fetish":           #Anal fetish
        "After a particularly hard bounce, [the_girl.title] moans ecstatically."
        if the_girl == mom:
            the_girl.char "That's it honey, fuck mommy harder! Tie me up and hang me from a swing and pound mommy's ass any way you want! It feels so good!"
        elif the_girl == lily:
            the_girl.char "That's it bro! Fuck me harder! I'm your slutty little sister, hanging from a swing just to please you!"
        elif the_girl == starbuck:
            the_girl.char "Yes! Don't let up! I think about you stringing me up like this everytime I see the swing in the store."
        else:
            the_girl.char "That's it, fuck me harder! Make me walk funny for a week!"
        "With your hands wrapped around the straps, you control the pace of your fucking."
        "[the_girl.title] clenches each time you pull back, and relaxes each time your push forward. The sensation is exquisite."
        "You grab the swing and pull her into you hard, slmaming yourself into her."
    else:
        "Fucking her hard, [the_girl.title] moans. She clutches onto the swing, holding on while you have your way with her ass."
        the_girl.char "Oh god, you fuck me so good."

    #menu:
    #    "Kneed her ass":


    #    "Play with her clit":

    return


label scene_SB_anal_swing_2(the_girl, the_location, the_object, the_round):
    "[the_girl.title] quivers as you slow up the pace a bit. You pull the straps on the swing towards you and thrust your hips forward, burying your cock as deep in her ass as you can."
    if the_girl.outfit.tits_available():
        "You reach around her body with both hands and grab her tits. You pinch and pull at her nipple roughly being careful to keep your cock deep inside her."
    else:
        "You reach around her body with both hands and grab as her tits. The frabric covering them is maddening. You decide to strip her down."
        mc.name "[the_girl.title]... I need to feel your skin!"
        while not the_girl.outfit.tits_available():    #If covered up, have her take her top off
            $ the_clothing = the_girl.outfit.get_upper_ordered()[-1]
            "You take off [the_girl.title]'s [the_clothing.name]"
            $ the_girl.draw_animated_removal(the_clothing)

        mc.name "Mmm, you tits are amazing."
        if the_girl.get_opinion_score("showing her tits") > 0:
            "You can see a blush in [the_girl.title]'s cheeks. She likes to show off her [the_girl.tit_size] tits!"
            $ the_girl.discover_opinion("showing her tits")
            $ the_girl.change_arousal(5)
    "You roll each of nipples between your thump and index fingers. [the_girl.title] arches her back and moans."
    "You grasp her tits with both hands and hold her in place and start to give her rapid thrusts with your hips."
    the_girl.char "Oh fuck! Yes! [mc.name]!"
    "She is writhing in the swing back against you, but she has no leverage. You have all the control."

    if the_girl.arousal > 130:
        the_girl.char "Ohhh my god, its so good..."
        "[the_girl.title]'s ass is quivering non stop."
        if SB_get_fetish(the_girl) == "Anal Fetish":
            the_girl.char "I just can't stop cumming! It feels so good [mc.name]! Fuck my ass and make it yours!"
    elif the_girl.arousal > 80:
        the_girl.char "Ohhh, it feels so good. You're gonna make me cum like this... aren't you?"
        "You can feel a slight quiver in [the_girl.title]'s body as you fuck her. She's probably going to cum soon!"
    else:
        "[the_girl.title] groans in response to one particularly deep thrust."
        the_girl.char "It's so big... How does it even fit back there?"
    "You push yourself in as deep as you can go. [the_girl.title] moans as you fill her completely."
    menu:
        "Kiss her neck":
            "You lean down and start to kiss [the_girl.title]'s neck. She tilts her head to the side to let you."
            if mc.sex_skills["Foreplay"] > 2:

                if the_girl.get_opinion_score("kissing") > 0:
                    $ the_girl.discover_opinion("kissing")
                    $ the_girl.change_arousal(the_girl.get_opinion_score("kissing") * 2)
                the_girl.char "[mc.name]! I don't know if I can take this!"
                "She moans erotically. Her senses are in overdrive."
                "Your lips on her neck, your fingers pinching her nipples, and your dick in her ass. You are giving her an incredible amount of stimulation."
                $ the_girl.change_arousal( mc.sex_skills["Foreplay"])
            else:
                "You do your best to split your focus between kissing [the_girl.title] and pumping your hips, but you find yourself slipping out of the steady rhythm you had established."
                "[the_girl.title] sighs happily."
                the_girl.char "That feels nice, but it feels better when you focus on fucking me."
            "You kiss her neck one more time, then move your hands back to the swing straps and continue fucking her. She gives a little yelp when you pinch one of her nipples."
        "Talk Dirty":
            mc.name "I love to fuck your ass. It's so tight! You make such a great butt slut."
            if SB_get_fetish(the_girl) == "Anal Fetish":
                "[the_girl.title] moans enthusiastically. She reaches back with one hand and grabs your hip, urging you to fuck her harder."
                the_girl.char "[mc.name]! I love being your butt slut. Now give it to your slut hard!"
                "You give her what she wants. You grab her hips and start thrusting into her hard and fast."
                the_girl.char "Oh fuck [mc.name]! Yes!"
                $ the_girl.change_arousal(the_girl.get_opinion_score("anal sex"))
                "[the_girl.title] is moaning your name over and over. Her whole body bounces and sways as you fuck her on the swing."

            elif the_girl.get_opinion_score("being submissive") > 0 or the_girl.obedience > 130:
                "[the_girl.title] moans enthusiastically."
                the_girl.char "[mc.name]... use me... fuck me! Make me your little slut!"
                "You give her what she wants. You grab her hips and start thrusting into her hard and fast."
                $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive") * 3 + 3)
                "You give her the anal reeming she is begging for."
            else:
                "[the_girl.title] looks back at you and manages to smile through the intense sensation of having her ass fucked."
                the_girl.char "You are stretching me out so much... Be careful back there, I'm not sure how much of this I can take!"
                "You reassure her, and then slowly begin to fuck her tightest hole again."

    return


label outro_SB_anal_swing(the_girl, the_location, the_object, the_round):
    "[the_girl.title]'s tight ass draws you closer to your orgasm with each thrust. You finally pass the point of no return and speed up, fucking her as hard as you can manage."
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
            "[the_girl.title]'s ass is just too good. You decide to cum inside it."
            "You pull back on the swing straps and drive your cock deep inside of her as you cum. She moans as you body dumps your load deep into her bowel."
            if the_girl.get_opinion_score("creampies") > 0:
                the_girl.char  "Yes! Fill your slut's ass with your cum! It's so hot!"
            if the_girl.arousal > 110:
                "You feel her bowel contracting around your dick as she also starts to orgasm."
                $ the_person.change_happiness(5)
            $ cum_in_ass(the_girl)
            $ SB_anal_swing.redraw_scene(the_girl)
            if SB_get_fetish(the_girl) == "Internal Cum Fetish":
                "[the_girl.title]'s body goes rigid as your cum poors into her ass. Goosebumps erupt all over her body as her brain registers her creampie."
                the_girl.char "Oh.. OH! Yes [mc.name]! Pump it deep! You were meant to cum inside me!"
                "[the_girl.title] revels in having her cum fetish fulfilled."
            elif the_girl.get_opinion_score("creampies") > 0:
                the_girl.char "Yes!... Thank you so much [mc.name]. It's inside me... you know I love that so much..."
            elif the_girl.sluttiness > 110:
                the_girl.char "Oh god it's so good. It makes me so happy to be pumped full like this."
            else:
                the_girl.char "Oh fuck, I can't believe I let you cum in my ass..."

            "You wait until your orgasm has passed completely, then pull out. Her asshole gapes and you can see a hint of your cum start to dribble out, but most of it stays buried with her bowel"

        "Cum on her ass.":
            "You pull out of [the_girl.title] at the last moment, stroking your shaft as you blow your load over her ass. She holds still for you as you cover her with your sperm."
            if the_girl.get_opinion_score("being covered in cum") > 0:
                 the_girl.char "Yes! Paint me with your sticky cum!"
            $ the_girl.cum_on_ass()
            $ SB_anal_swing.redraw_scene(the_girl)
            if SB_get_fetish(the_girl) == "External Cum Fetish":
                "[the_girl.title]'s body goes rigid as your cum coats her ass. Goosebumps erupt all over her body as her brain registers your cum on her skin."
                "[the_girl.title] revels in bliss as your dick sprays jet after jet of seed across her ass. She moans lewdly."
                "She truly is addicted to your cum."
            elif the_girl.sluttiness > 120:
                the_girl.char "Oh god your seed is so hot! Does it look sexy, having it plastered all over my ass?"
                "She reaches back and runs a finger through the streams of cum you've put on her, then licks her finger clean."
            else:
                the_girl.char "Oh! Its so warm..."
            "You sit back and sigh contentedly, enjoying the sight of [the_girl.title]'s ass covered in your semen."
        "Cum on her tits.":
            mc.name "Fuck, get ready [the_girl.title], I wanna cum on your tits!"
            "You pull your cock out of [the_girl.title]'s ass with a satisfying pop. You spin the swing around quickly so she faces you."
            if the_girl.get_opinion_score("being covered in cum") > 0:
                "[the_girl.title] reaches up and immediately begins stroking you off for you final few seconds."
                "Your orgasm hits hard. Your first jet sprays across her tits."
                $ the_girl.cum_on_tits()
                $ the_girl.draw_person(position = "sitting")
                if SB_get_fetish(the_girl) == "External Cum Fetish":
                    "You can see [the_girl.title]'s pupils dilate as you fulfil her cum fetish."
                    "[the_girl.title] revels in bliss as your dick sprays jet after jet of seed across her body. She moans lewdly."
                    "She truly is addicted to your cum."
                else:
                    "[the_girl.title] moans as your dick sprays jet after jet of seed across her body."
            elif the_girl.sluttiness > 80:
                "[the_girl.title] presses her tits together with her hands, eager to take your hot load."
                $ the_girl.cum_on_tits()
                $ the_girl.draw_person(position = "sitting")
                "You let out a shudder moaning as you cum, pumping your sperm onto [the_girl.title]'s chest. She makes sure to wait until you're completely finished."
                the_girl.char "Oh god... it feels so good on my skin..."
            elif the_girl.sluttiness > 60:
                "[the_girl.title] looks up at you and waits patiently for you to cum."
                $ the_girl.cum_on_tits()
                $ the_girl.draw_person(position = "sitting")
                "You let out a shudder moaning as you cum, pumping your sperm onto [the_girl.title]'s chest. She waits until she's sure you're finished."
            else:
                "[the_girl.title] closes her eyes and turns away."
                $ the_girl.cum_on_tits()
                $ the_girl.draw_person(position = "sitting")
                "You let out a shudder moaning as you cum, pumping your sperm onto [the_girl.title]'s chest. She flinches as the first splash of warm liquid lands on her body, but doesn't pull away entirely."
            "You take a deep breath to steady yourself once you've finished orgasming. [the_girl.title] looks up at you from the swing, her tits covered in your seed."
            the_girl.char "Wow, that was really intense..."


    return


label transition_default_SB_anal_swing(the_girl, the_location, the_object, the_round):
    "[the_girl.title] turns and puts her hands on [the_object.name]. You bounce your hard shaft on her ass a couple of times before lining yourself up with her sphincter."
    "Once you're both ready you push yourself forward, slipping your hard shaft deep inside of her. She lets out a gasp under her breath."
    return

label strip_SB_anal_swing(the_girl, the_clothing, the_location, the_object, the_round):
    #"[the_girl.title] leans forward a little further and pops off your cock."
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing, position =  SB_anal_swing.position_tag)
    "[the_girl.title] struggles out of her [the_clothing.name] and throws it to the side. Then she gets herself lined up in front of you again."
    "She groans happily when you push back inside of her."
    return

label strip_ask_SB_anal_swing(the_girl, the_clothing, the_location, the_object, the_round):
    the_girl.char "Sir, I'd like to take off my [the_clothing.name], would you mind?"
    "[the_girl.char] pants as you fuck her from behind."
    menu:
        "Let her strip.":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = SB_anal_swing.position_tag)
            "[the_girl.title] struggles out of her [the_clothing.name] and throws it to the side."
            "She groans happily when you resume fucking her tight rear."

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


label orgasm_SB_anal_swing(the_girl, the_location, the_object, the_round):
    "[the_girl.title]'s whole body starts to tremble, and then suddenly she tenses up."
    $ the_girl.call_dialogue("climax_responses")
    "You bury your cock in deep in [the_girl.title]'s ass while she cums. Her bowel grips you tightly."
    "After a couple of seconds [the_girl.title] sighs and the tension drains from her body."
    if the_girl.get_opinion_score("anal sex") < 0:
        the_girl.char "I can't believe that just happened... oh god now you're going to keep going, aren't you?"
    else:
        the_girl.char "Don't stop... it still feels so good!"
    return
