#Prone bone position. Girl is pinned down on her front, very submissive position, so we make sure to use lots of references to submissive or dominant girls in dialogue and actions.
#These actions generally increase obedience and sluttiness in dominant girls,  increase happiness in submissives.
init:
    python:
        prone_bone = Position(name = "Prone", slut_requirement = 60, slut_cap = 90, requires_hard = True, requires_large_tits = False,
            position_tag = "back_peek", requires_location = "Lay", requires_clothing = "Vagina", skill_tag = "Vaginal",
            girl_arousal = 18, girl_energy = 8,
            guy_arousal = 16, guy_energy = 14,
            connections = [],
            intro = "intro_prone_bone",
            scenes = ["scene_prone_bone_1","scene_prone_bone_2"],
            outro = "outro_prone_bone",
            transition_default = "transition_default_prone_bone",
            strip_description = "strip_prone_bone", strip_ask_description = "strip_ask_prone_bone",
            orgasm_description = "orgasm_prone_bone",
            taboo_break_description = "taboo_break_prone_bone",
            opinion_tags = ["doggy style sex","vaginal sex", "being submissive"], record_class = "Vaginal Sex",
            default_animation = missionary_bob,
            associated_taboo = "vaginal_sex")
        list_of_positions.append(prone_bone)

# init 1:
#     python:
#         missionary.link_positions(piledriver,"transition_missionary_piledriver")

label intro_prone_bone(the_girl, the_location, the_object):
    "You turn [the_girl.title] so her back is to you, then push her down onto the [the_object.name]."
    mc.name "Just lay down. I'm going to have my way with you now."
    if the_girl.is_submissive():
        the_girl "I'll do whatever you want, you always make me feel so good too..."
        $ the_girl.change_happiness(1)
        $ the_girl.change_obedience(1)
        mc.name "Yeah, 'atta girl.'"
    elif the_girl.is_dominant():
        the_girl "Is that so? What do I get out of it?"
        mc.name "Why should I care? Lay down."
        "She murmurs but begins to lay down obediently."
        $ the_girl.change_happiness(-1)
        $ the_girl.change_obedience(2)
    else:
        the_girl "Okay, just don't do anything too crazy, okay?"
        $ the_girl.change_obedience(1)
    "She lies down on the [the_object.name], waiting while you climb on top of her. Before you get started, you give her ass a couple smacks with your dick."
    "[the_girl.possessive_title] looks back at you as you line your cock up with her pussy. She moans as you slide into her."
    return

label taboo_break_prone_bone(the_girl, the_location, the_object):
    "You take [the_girl.title]'s hands in yours and guide her down onto the [the_object.name]. You turn her back to you."
    mc.name "Lay down. I want to be in control for our first time."
    $ the_girl.call_dialogue(prone_bone.associated_taboo+"_taboo_break")
    the_girl "Okay, just don't do anything too crazy, okay?"
    $ the_girl.change_obedience(2)
    "She lies down on the [the_object.name] on her belly. She wiggles her ass at you, waiting while you climb on top of her."
    "[the_girl.possessive_title] loks back at you as you line your cock up with her pussy. She moans as you slide into her."
    return

label scene_prone_bone_1(the_girl, the_location, the_object):
    #Scene 1, focus on visuals of prone (ass, back)
    "You push down on [the_girl.possessive_title] with your weight as you fuck her. She is pinned to the [the_object.name]."
    if the_girl.body_is_thin():
        "Your hips slap up against [the_girl.possessive_title]'s fit ass."
        "Her cheeks are tight from the exercise and care she puts into her body."
    elif the_girl.body_is_average():
        "Your hips begin to slap up against [the_girl.possessive_title]'s delicious ass."
        "Her cheeks are round but firm with just a hint of quaking with each impact."
    elif the_girl.body_is_thick():
        "Your hips begin to slap up against [the_girl.possessive_title]'s thick ass."
        "Her cheeks are full and generous, and they quake back and forth enticingly as you pound her."
    elif the_girl.body_is_pregnant():
        "Your hips begin to slap up against [the_girl.possessive_title]'s wide ass."
        "Her cheeks make a pleasing heart shape since her body has been changing with the baby growing in her belly."
        "Her belly is up against the [the_object.name], forcing her ass up at a pleasing angle."
    else:
        "Your hips begin to slap up against [the_girl.possessive_title]'s ass."
        "Her cheeks respond delightfully with each thrust."
    menu:
        "Grab her shoulders":
            "You put your hands on [the_girl.title]'s shoulders. The leverage helps you pound her harder."

        "Grope her ass":
            pass
    return

label scene_prone_bone_2(the_girl, the_location, the_object):
    #Scene 2, focus on submissiveness of scene (spank, dirty talk, hair pulling)

    if the_girl.is_submissive():
        pass
    elif the_girl.is_dominant():
        the_girl ""

    return

label outro_prone_bone(the_girl, the_location, the_object):
    "You get to hear every little gasp and moan from [the_girl.title] as you're pressed up against her. Combined with the feeling of fucking her pussy it's not long before you're pushed past the point of no return."
    mc.name "I'm going to cum!"
    $ the_girl.call_dialogue("cum_pullout")
    $ climax_controller = ClimaxController(["Cum inside of her", "pussy"],["Cum on her chest","body"])
    $ the_choice = climax_controller.show_climax_menu()

    if the_choice == "Cum inside of her":
        "You use your full weight to push your cock deep inside of [the_girl.possessive_title]'s cunt as you climax. She gasps and claws lightly at your back as you pump your seed into her."

        if mc.condom:
            $ the_girl.call_dialogue("cum_condom")
            $ climax_controller.do_clarity_release(the_girl)
            "You take a moment to catch your breath, then roll off of [the_girl.possessive_title] and lie beside her."
            "Your condom is ballooned with your seed, hanging off your cock to one side."
            if the_girl.get_opinion_score("drinking cum") > 0 and the_girl.effective_sluttiness() > 50:
                $ the_girl.discover_opinion("drinking cum")
                "[the_girl.possessive_title] reaches over for your cock. With delicate fingers she slides the condom off of you, pinching it off do your cum doesn't spill out."
                the_girl.char "It would be a shame to waste all of this, right?"
                "She smiles and brings the condom to her mouth. She tips the bottom up and drains it into her mouth."
                $ the_girl.change_slut_temp(the_girl.get_opinion_score("drinking cum"))
            else:
                "[the_girl.possessive_title] reaches over for your cock, removes the condom, and ties the end in a knot for you."
                the_girl.char "Look at all that cum. Well done."

        else:
            $ climax_controller.do_clarity_release(the_girl)
            $ the_girl.call_dialogue("cum_vagina")
            $ the_girl.cum_in_vagina()
            $ prone_bone.redraw_scene(the_girl)
        "You take a moment to catch your breath, then roll off of [the_girl.possessive_title] and lie beside her."

    elif the_choice == "Cum on her chest":
        $ the_girl.cum_on_stomach()
        $ prone_bone.redraw_scene(the_girl)
        if mc.condom:
            "You pull out at the last moment and grab your cock. You whip off your condom and stroke yourself off, blowing your load over [the_girl.title]'s stomach."
        else:
            "You pull out at the last moment and grab your cock. You kneel and stroke yourself off, blowing your load over [the_girl.title]'s stomach."
        $ climax_controller.do_clarity_release(the_girl)
        the_girl.char "Ah... Good job... Ah..."
        "You sit back and sigh contentedly, enjoying the sight of [the_girl.possessive_title]'s body covered in your semen."
    return

label transition_prone_bone_piledriver(the_girl, the_location, the_object):
    "[the_girl.title]'s pussy feels so warm and inviting, you can't help but want to get deeper inside of her. You pause for a moment and reach down for her legs."
    the_girl "Hey, what's... Whoa!"
    "You pull her legs up and bend them over her shoulders. You hold onto her ankles as you start to fuck her again, pushing your hard cock nice and deep."
    return

label transition_default_prone_bone(the_girl, the_location, the_object):
    "You put [the_girl.title] on her back and lie down on top of her, lining your hard cock up with her tight cunt."
    "After running the tip of your penis along her slit a few times you press forward, sliding inside of her. She gasps softly and closes her eyes."
    return

label strip_prone_bone(the_girl, the_clothing, the_location, the_object):
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing, position = prone_bone.position_tag)
    "[the_girl.possessive_title] struggles out of her [the_clothing.name] and throws it to the side. Then she gets herself lined up in front of you again."
    "She sighs happily when you slip back inside of her."
    return

label strip_ask_prone_bone(the_girl, the_clothing, the_location, the_object):
    the_girl "[the_girl.mc_title], I'd like to take off my [the_clothing.name], would you mind?"
    "[the_girl.title] pants as you fuck her."
    menu:
        "Let her strip":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = prone_bone.position_tag)
            "You move back kneel for a moment while [the_girl.title] struggles out of her [the_clothing.name] and throws it to the side. Then she gets herself lined up in front of you again."
            "She sighs happily when you get on top of her and slide your cock back inside."

        "Leave it on":
            mc.name "No, I like how you look with it on."
            if the_girl.sluttiness < 80:
                the_girl "Do you think I look sexy in it?"
                "You speed up, fucking her faster in response to her question."
            elif the_girl.sluttiness < 100:
                the_girl "Does it make me look like a good little slut? All I want to be is your good little slut sir."
                "She pushes her hips against yours and moans happily."
            else:
                the_girl "Does it make me look like the cum hungry slut that I am? That's all I want to be for you sir, your dirty little cum dumpster!"
                "She grinds her hips against you and moans ecstatically."
    return

label orgasm_prone_bone(the_girl, the_location, the_object):
    "[the_girl.title] turns her head and pants loudly. Suddenly she bucks her hips up against yours and gasps."
    $ the_girl.call_dialogue("climax_responses_vaginal")
    "Her pussy is dripping wet as you fuck through her climax. She paws at the [the_object.name], trying to find something to hold onto."
    "After a few seconds she lets out a long sigh and all the tension drains out of her body. You slow down your thrusts to catch your own breath."
    the_girl "Don't stop [the_girl.mc_title], I might be able to get there again..."
    return
