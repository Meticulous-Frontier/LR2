transform Threesome_doggy_deluxe_girl_one_transform():
    xalign 1.0
    yalign 1.0
    xpos 1.0
    ypos 0.92
    zoom 0.65


transform Threesome_doggy_deluxe_girl_two_transform():
    xalign 1.0
    yalign 1.0
    xpos 1.0
    ypos 1.0
    zoom 0.8


init:
    python:
        Threesome_doggy_deluxe_fuck_girl_two = Threesome_MC_position(name = "fuck_girl_2",
            description = "Fuck [the_person_two.title]",
            skill_tag_p1 = "Oral",
            skill_tag_p2 = "Vaginal",
            girl_one_arousal = 18,
            girl_two_arousal = 22,
            girl_one_source = 2,
            girl_two_source = 0,
            girl_one_energy = 8,
            girl_two_energy = 13,
            guy_arousal = 20,
            guy_source = 2,
            guy_energy = 10,
            skill_tag_guy = "Vaginal",
            intro = "intro_threesome_doggy_deluxe_fuck_girl_two",
            scenes = ["scene_threesome_doggy_deluxe_fuck_girl_two_1", "scene_threesome_doggy_deluxe_fuck_girl_two_2"],
            outro = "outro_threesome_doggy_deluxe_fuck_girl_two",
            strip_description = "strip_threesome_doggy_deluxe_fuck_girl_two",
            strip_ask_description = "strip_ask_threesome_doggy_deluxe_fuck_girl_two",
            orgasm_description = "orgasm_threesome_doggy_deluxe_fuck_girl_two",
            swap_description = "swap_threesome_doggy_deluxe_fuck_girl_two",
            requirement = requirement_hard_both_vagina_available)

        Threesome_doggy_deluxe_anal_girl_two = Threesome_MC_position(name = "anal_girl_2",
            description = "Fuck [the_person_two.title]'s ass",
            skill_tag_p1 = "Oral",
            skill_tag_p2 = "Anal",
            girl_one_arousal = 18,
            girl_two_arousal = 22,
            girl_one_source = 2,
            girl_two_source = 0,
            girl_one_energy = 8,
            girl_two_energy = 14,
            guy_arousal = 22,
            guy_source = 2,
            guy_energy = 10,
            skill_tag_guy = "Anal",
            intro = "intro_threesome_doggy_deluxe_anal_girl_two",
            scenes = ["scene_threesome_doggy_deluxe_anal_girl_two_1", "scene_threesome_doggy_deluxe_anal_girl_two_2"],
            outro = "outro_threesome_doggy_deluxe_anal_girl_two",
            strip_description = "strip_threesome_doggy_deluxe_anal_girl_two",
            strip_ask_description = "strip_ask_threesome_doggy_deluxe_anal_girl_two",
            orgasm_description = "orgasm_threesome_doggy_deluxe_anal_girl_two",
            swap_description = "swap_threesome_doggy_deluxe_anal_girl_two",
            requirement = requirement_disable_position) #WIP for now

        Threesome_doggy_deluxe_watch_girls = Threesome_MC_position(name = "watch_girls",
            description = "Watch the Girls",
            skill_tag_p1 = "Oral",
            skill_tag_p2 = "Oral",
            girl_one_arousal = 15,
            girl_two_arousal = 15,
            girl_one_source = 2,
            girl_two_source = 1,
            girl_one_energy = 10,
            girl_two_energy = 10,
            guy_arousal = 6,
            guy_source = 0,
            guy_energy = 5,
            skill_tag_guy = "Foreplay",
            intro = "intro_threesome_doggy_deluxe_watch_girls",
            scenes = ["scene_threesome_doggy_deluxe_watch_girls"],
            outro = "outro_threesome_doggy_deluxe_watch_girls",
            strip_description = "strip_threesome_doggy_deluxe_watch_girls",
            strip_ask_description = "strip_ask_threesome_doggy_deluxe_watch_girls",
            orgasm_description = "orgasm_threesome_doggy_deluxe_watch_girls",
            swap_description = "swap_threesome_doggy_deluxe_watch_girls",
            requirement = requirement_disable_position) #WIP


        Threesome_doggy_deluxe = Threesome_Position(name = "Doggy Deluxe",
            slut_requirement = 60,
            position_one_tag = "missionary",
            position_two_tag = "doggy",
            girl_one_final_description = "On your back and let her eat you out",
            girl_two_final_description = "Eat her out while on your hands and knees",
            requires_location = "Lay",
            requirements = requirement_hard_both_vagina_available,
            verb = "fuck",
            p1_transform = Threesome_doggy_deluxe_girl_one_transform,
            p2_transform = Threesome_doggy_deluxe_girl_two_transform,
            can_swap = True,)

        Threesome_doggy_deluxe.mc_position = [Threesome_doggy_deluxe_fuck_girl_two,Threesome_doggy_deluxe_anal_girl_two, Threesome_doggy_deluxe_watch_girls]
        list_of_threesomes.append(Threesome_doggy_deluxe)






label intro_threesome_doggy_deluxe_fuck_girl_two(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "[the_girl_1.possessive_title] lays down on her back. [the_girl_2.possessive_title] gets down between her legs and start to lick her threesome partner."
    "Face down, ass up, exactly what you were looking for. You move forward behind [the_girl_2.title] and run your hands along her ass a few times."
    "You put your cock between her cheeks, enjoying the feeling of her soft, pliant flesh. She wiggles her hips back at you for a second before turning her head to look at you."
    if SB_check_fetish(the_girl_2, vaginal_fetish_role):
        the_girl_2.char "Go ahead and fuck me! I can't wait to feel you deep inside me again..."
    else:
        the_girl_2.char "I think I'm ready for you... go ahead and push it in!"
    "You don't need any encouragement! "
    return


label scene_threesome_doggy_deluxe_fuck_girl_two_1(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "You grab onto [the_girl_2.title] by her hips and settle into a steady rhythm, pumping your cock in and out of her tight pussy."
    if the_girl_2.arousal > 50:
        "A steady stream of moans are getting drown out as [the_girl_2.title] buries her face in [the_girl_1.title]'s slit."
    else:
        "You hear a low and steady moan coming from [the_girl_2.possessive_title], but its getting muffled by [the_girl_1.title]'s cunt."
    menu:
        "Talk dirty to [the_girl_2.title].":
            mc.name "How does that feel? Do you like getting used? I bet you do."
            mc.name "Your pussy feels great, hows her tongue, [the_girl_1.title]?"
            if the_girl_1.arousal > 65:
                the_girl_1.char "Mmmmm... God... its so good..."
            else:
                the_girl_1.char "It feels great... keep going!"
            if the_girl_2.get_opinion_score("being submissive") > 0 or the_girl_2.get_opinion_score("threesomes") > 0:
                "[the_girl_2.title] reaches back with one hand and spreads her cheeks and pushes back against you. She moans when you push deep into her."
                if the_girl_2 == mom and the_girl_1 == lily: #Special dialogue
                    mc.name "Mmm, you do like it, don't you? Your son and daughter, using you for their own pleasure. A slutty mommy's biggest dream!"
                else:
                    mc.name "Mmm, you do like it don't you. A guy and a girl at the same time, using you for their pleasure. Every slut's biggest dream!"
                $ the_girl_2.change_arousal(10)
                "She moans loudly now, but doesn't stop licking [the_girl_1.title]'s slit."
            else:
                "You tighten your grip on her hips and fuck her faster."
            "You fuck her a little faster for a while then settle back down to a slower, more sustainable rhythm."
        "Spank her ass.":
            "You take a hand off of [the_girl_1.title]'s hips and squeeze her ass cheeks with it. When she gives a yelp in response you give her a hard slap."
            the_girl_1.char "Oh! She's been a bad girl [the_girl_1.mc_title]. Give her a good spanking!"
            if the_girl_2.get_opinion_score("being submissive") > 0: #She likes it
                "[the_girl_2.possessive_title] leans forward a little farther, making sure her ass is as high as she can get it."
                "*SMACK*"
                mc.name "Is it true, [the_girl_2.title]? Have you been bad?"
                "She wiggles her ass back and forth a few times."
                "*SMACK*"
                "She moans loudly. You look up and see [the_girl_1.possessive_title] is enjoying the extra stimulation."
                "*SMACK*"
                "She moans again. A red handprint is starting to form on her ass cheek."
                "*SMACK*"
                the_girl_2.char "Ahh! Mmmmmmmm"
                "She cries out, enjoying your rough treatment of her body."
                $ the_girl_2.change_arousal(20)
                $ the_girl_1.change_arousal(7)
            else:
                "*SMACK*"
                "Her ass jiggles enticingly when you spank it."
            "You leave a hand planted on [the_girl_2.possessive_title]'s butt while you fuck her, kneading it and giving it the occasional slap."
    return


label scene_threesome_doggy_deluxe_fuck_girl_two_2(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "Your hips slap against [the_girl_2.possessive_title]'s ass as you fuck her vigorously."
    if the_girl_2.sex_skills["Vaginal"] < 2: #Inexperienced
        "After a particularly hard thrust, [the_girl_2.possessive_title] reflexively starts to pull away. You grab her hips to keep her from pulling off completely."
        the_girl_2.char "I'm sorry [the_girl_2.mc_title], thats a little too rough. Can you go a little slower?"
        "You pull her hips back toward you slowly. She sighs, still trying to get accustomed to your girth, penetrating her at such a deep angle."
        "The next time you push yourself in you push a little faster. [the_girl_2.title] goes back to licking [the_girl_1.title]."
    elif SB_check_fetish(the_girl_2, vaginal_fetish_role):          #vaginal fetish
        "After a particularly hard thrust, [the_girl_2.possessive_title] moans lewdly. She stops eating out [the_girl_1.title] for a second and looks back at you."
        the_girl_2.char "It's so... fucking... GOOD. Fuck me hard [the_girl_2.mc_title], I want it so bad!"
        "With one hand on her hip to control the pace, you grope and worship her ass cheeks with the other hand. Each time you pull back you can see her labia clinging to you."
        "[the_girl_2.possessive_title] is moaning non stop a she continues to lick [the_girl_1.title]."
        $ the_girl_2.change_arousal(5)
        "You use both hands to grab her hips and slam yourself into her as deep as you can go."
        "Buried deep inside, you give her ass a smack. Her pussy trembles and caresses you in response."
    else:
        "Fucking her hard, [the_girl_2.possessive_title] moans, matching each hip movement of yours with movement of her own."
        "[the_girl_2.possessive_title] reaches back with one hand and pulls her ass cheek back, giving you a great view of her pussy stretched wide to accomodate you."
        "Buried deep inside, you give her ass a smack. Her pussy trembles and caresses you in response."
    the_girl_1.char "I know it feels good, but don't forget you need to get me off too!"
    "[the_girl_1.possessive_title] reaches down and runs her hands through [the_girl_2.title]'s hair."
    if the_girl_1.get_opinion_score("taking control") > 0: #She gets rough with her
        "You watch as [the_girl_1.title] stop being gently and grasps [the_girl_2.possessive_title] by the hair."
        "You slow your pace a bit and just watch. [the_girl_1.title] is starting to move her hips aggressively, humping [the_girl_2.possessive_title]'s face."
        the_girl_1.char "Mmmm, that's it. Atta girl!"
        $ the_girl_1.change_arousal(5)
        "Eventually [the_girl_1.title] lets go of her hair."
    else:
        the_girl_2.char "Sorry! This is just so intense..."
        "[the_girl_2.title] doubles down on her efforts to please [the_girl_1.possessive_title]."
        "You slow your pace down a bit to give her a chance to catch her breath, watching [the_girl_1.title] running her hands through her hair intimately."
        "Eventually [the_girl_1.title] lets go of her hair."
    "You resume your normal pace, settling into rhythm."
    return


label outro_threesome_doggy_deluxe_fuck_girl_two(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "Pounding [the_girl_2.possessive_title] tight cunt, and watching her pleasure [the_girl_1.title] soon has you passing the point of no return."
    mc.name "Ah, I'm going to cum!"
    menu:
        "Cum inside of her.":
            "Her pussy is just too good. There's no way you are going to pull out."
            if mc.condom:  #Not sure how we have a condom on but I guess it could happen
                "You grab [the_girl_2.possessive_title]'s hips and thrust deep. You dump your load inside of the condom, filling it up."
                $ condom_break_chance = renpy.random.randint(0, 100)
                if condom_break_chance < 15: #15% chance of breaking, because its a game condoms don't actually break this much #TODO make a game condom break chance and rewrite some scenes.
                    "This time though, you feel something give way. You give her a couple more strokes as you finish dumping your load, then slightly pull back."
                    $ the_girl_2.cum_in_vagina()
                    $ scene_manager.draw_scene()
                    "Around the base of your cock you see the remains of a broken condom. You just dumped your load in [the_girl_2.title]!"
                    mc.name "Hey, sorry, but the condom broke..."
                    #TODO a variety of responses
                    the_girl_2.char "Mmmm, so that's what felt so good. It's okay, it happens!"
                    "When you pull back, you see your cum leaking out and down her legs. You enjoy your after orgasm bliss."
                else:
                    "You wait until your orgasm has passed completely, then pull out and sit back. The condom is ballooned and sagging with the weight of your seed."
                    "You tie the end in a knot and sit back, enjoying the post-orgasm feeling of relaxation."
            else:
                "You grab [the_girl_2.possessive_title]'s hips and thrust deep. You dump your load as deep inside of her as you can get it."
                if the_girl_2.get_opinion_score("creampies") > 0:
                    the_girl_2.char  "MMMM! Yes yes yeessshhhh"
                    "You can make out a few words of excitement from [the_girl_2.possessive_title] as she buries her face in [the_girl_1.title]'s cunt."
                $ the_girl_2.cum_in_vagina()
                $ scene_manager.draw_scene()
                if SB_check_fetish(the_girl_2, cum_internal_role):
                    "[the_girl_2.possessive_title]'s body goes rigid as your cum pours into her pussy. Goosebumps erupt all over her body as her brain registers her creampie."
                    "She revels in having her cum fetish fulfilled."
                "You slowly pull back. Your cum is dripping out of her cunt and down the inside of her legs."
                "You sit back and enjoy the feeling of post orgasm bliss."
        "Cum on her ass.":
            if mc.condom:
                "You pull out of [the_girl_2.title] at the last moment. You whip your condom off and stroke your cock as you blow your load over her ass."
                "She wiggles her ass for you as you cover her with your special sauce."
            else:
                "You pull out of [the_girl_2.title] at the last moment. She wiggles her ass for you as you cover her with your cum."
            $ the_girl_2.cum_on_ass()
            $ scene_manager.draw_scene()
            if SB_check_fetish(the_girl, cum_external_role):
                "[the_girl_2.possessive_title]'s body goes rigid as your cum coats her ass. Goosebumps erupt all over her body as her brain registers your cum on her skin."
                "[the_girl_2.possessive_title] revels in bliss as your dick sprays jet after jet of seed across her ass. She moans lewdly."
                "She truly is addicted to your cum."
            "You sit back and enjoy the site of [the_girl_2.title]'s ass, covered in your seed, while she eats out the other girl."
    return

label strip_threesome_doggy_deluxe_fuck_girl_two(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "This is just a test to see if this position is working."
    "This is the Strip Scene!"
    return

label strip_ask_threesome_doggy_deluxe_fuck_girl_two(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "This is just a test to see if this position is working."
    "This is the ask to strip Scene!"
    return

label orgasm_threesome_doggy_deluxe_fuck_girl_two(the_girl_1, the_girl_2, the_location, the_object, the_round):
    if the_girl_1.arousal > 100 and the_girl_2.arousal > 100:  #Both girls orgasm#
        "[the_girl_2.possessive_title] is moaning urgently now a she continues to service [the_girl_1.title] orally."
        the_girl_1.char "Oh hell that's so good. You're gonna cum soon too aren't you? Cum with me [the_girl_2.name]!"
        "[the_girl_2.title] is moaning loudly but it all gets muffled as [the_girl_1.title] grinds against her face roughly."
        "They both orgasm. You can feel [the_girl_2.possessive_title]'s cunt gripping you in time with her orgasmic waves."
        "As they start to wind down, you continue fucking [the_girl_2.title]'s now considerably slicker pussy."
        return

    elif the_girl_1.arousal > 100:   #Just girl 1 orgasms
        "[the_girl_1.possessive_title] is starting to moan more urgently. Her hips are moving on their own in time with [the_girl_2.title]'s oral ministrations."
        the_girl_1.char "Yes! That's it... right there! YES!!!"
        "[the_girl_1.title] grinds her pussy against the other girl's face as she orgasms."
        return

    elif the_girl_2.arousal > 100:   #Just girl 2 orgasms
        "[the_girl_2.possessive_title]'s legs start to quiver, and then suddenly she tenses up."
        $ the_girl_2.call_dialogue("climax_responses_vaginal")
        "She orgasms, her pussy quivering around your cock. You grab her hips and give a few extra rough thrusts."

    return


label swap_threesome_doggy_deluxe_fuck_girl_two(the_girl_1, the_girl_2, the_location, the_object, the_round):
    pass #TODO
    "This needs to be written"
    return
