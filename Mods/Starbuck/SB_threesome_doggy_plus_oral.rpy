init:
    python:
        SB_threesome_doggy_plus_oral = SB_Threesome_Position(name = "Doggy with Oral",
            slut_requirement = 80,
            slut_cap = 120,
            position_one_tag = "missionary",
            position_two_tag = "doggy",
            requires_location = "Lay",
            requires_clothing = "Vagina",
            skill_tag_p1 = "Oral",
            skill_tag_p2 = "Vaginal",
            girl_one_arousal = 25,
            girl_two_arousal = 20,
            girl_one_source = 2,
            girl_two_source = 0,
            guy_arousal = 20,
            guy_source = 2,
            skill_tag_guy = "Vaginal",
            current_girl = 2,
            connections = [],
            intro = "intro_SB_threesome_doggy_plus_oral",
            scenes = ["scene_SB_threesome_doggy_plus_oral_1", "scene_SB_threesome_doggy_plus_oral_2"],
            outro = "outro_SB_threesome_doggy_plus_oral",
            transition_default = "transition_default_SB_threesome_doggy_plus_oral",
            strip_description = "strip_SB_threesome_doggy_plus_oral",
            strip_ask_description = "strip_ask_SB_threesome_doggy_plus_oral",
            orgasm_description = "orgasm_SB_threesome_doggy_plus_oral",
            swap_description = "",
            verb = "fuck" ,
            opinion_tags = ["missionary style sex","vaginal sex","threesomes", "doggy style sex"],
            p1_x = 1.0,
            p1_y = 0.75,
            p1_zoom = 0.8,
            p2_x = 1.0,
            p2_y = 0.9,
            p2_zoom = 1.0,
            can_swap = False)
        SB_list_of_threesomes.append(SB_threesome_doggy_plus_oral)


label intro_SB_threesome_doggy_plus_oral(the_person_1, the_person_2, the_location, the_object, the_round):
    mc.name "[the_person_1.title], why don't you lay down. [the_person_2.title] can eat you out while I fuck her."
    "[the_person_1.possessive_title] smiles and agrees."
    if the_person_1.has_breeding_fetish():
        the_person_1.char "This should be a good warmup... but don't forget, [the_person_1.mc_title], I need you to fuck me sometime too..."
    elif the_person_1.has_cum_fetish():
        the_person_1.char "This should be good, I've heard [the_person_2.title] has a pretty good tongue..."
    elif the_person_1.has_role(anal_fetish_role):
        the_person_1.char "Mmm that sounds good... maybe she could stick a finger in my ass once in a while too..."
    else:
        the_person_1.char "Sounds good! I can't wait, I bet this is going to be amazing..."
    "[the_person_1.possessive_title] starts to lay down. [the_person_2.possessive_title] turns to you."
    if the_person_2.has_cum_fetish():
        the_person_2.char "Mmm I can't wait to taste that sweet pussy..."
    elif the_person_2.has_breeding_fetish():
        the_person_2.char "Mmm I can't wait to feel your raw cock sliding into me..."
    elif the_person_2.has_role(anal_fetish_role):
        the_person_1.char "Mmm that sounds good... maybe you could stick it in my ass for a bit too..."
    else:
        the_person_2.char "Alright! I've always thought [the_person_1.title] was kinda hot... I can't believe I finally get the opportunity to eat her out!"
    "[the_person_2.possessive_title] gets down on her hands and knees and slowly lowers her face into [the_person_1.possessive_title]'s crotch. [the_person_2.possessive_title] starts to lick between her legs"
    "You get down on your knees and grab [the_person_2.possessive_title]'s hips. You position your hips in line with hers and move your cock along her slit."
    if the_person_2.arousal > 60:
        "Her pussy is soaking wet. As you run your length along her hole you are soon slick with her juices."
    else:
        "Her pussy looks absolutely perfect. As you run your length along her hole she starts to squirm."
    "You take note of her puckered asshole, also beckoning your cock to come fill it. You decide to start with her pussy first though."
    "You push yourself into [the_person_2.possessive_title]'s steamy cunt and start to fuck her while she eats [the_person_1.possessive_title]'s pussy"
    return

label scene_SB_threesome_doggy_plus_oral_1(the_person_1, the_person_2, the_location, the_object, the_round):
    "This is just a test to see if this position is working."
    "This is the first scene!"
    return

label scene_SB_threesome_doggy_plus_oral_2(the_person_1, the_person_2, the_location, the_object, the_round):
    "This is just a test to see if this position is working."
    "This is the second scene!"
    return

label outro_SB_threesome_doggy_plus_oral(the_person_1, the_person_2, the_location, the_object, the_round):
    "This is just a test to see if this position is working."
    "This is the finish scene!"
    return

label transition_default_SB_threesome_doggy_plus_oral(the_person_1, the_person_2, the_location, the_object, the_round):
    "This is just a test to see if this position is working."
    "This is the default transition!"
    return

label strip_SB_threesome_doggy_plus_oral(the_person_1, the_person_2, the_location, the_object, the_round):
    "This is just a test to see if this position is working."
    "This is the Strip Scene!"
    return

label strip_ask_SB_threesome_doggy_plus_oral(the_person_1, the_person_2, the_location, the_object, the_round):
    "This is just a test to see if this position is working."
    "This is the ask to strip Scene!"
    return

label orgasm_SB_threesome_doggy_plus_oral(the_person_1, the_person_2, the_location, the_object, the_round):
    "This is just a test to see if this position is working."
    "This is the girl orgasm scene!"
    return

label swap_SB_threesome_doggy_play_oral(the_person_1, the_person_2, the_location, the_object, the_round, current_girl):
    #THIS FUNCTION NEEDS COMPLETELY REDONE
    if current_girl == 1:
        "You slowly pull out of [the_person_1.possessive_title]'s pussy. You run your hands through [the_person_2.possessive_title]'s hair for a second, then slowly pull her mouth down towards your cock."
        mc.name "Lick me clean, [the_person_2.title]."
        "[the_person_2.possessive_title] opens her mouth and begins to greedily slurp at your cock. Her mouth feels great sliding up and down your erection."
        "You reach down with one hand and hold [the_person_2.possessive_title]'s hair off to one side for her, and with your other hand you start to play with [the_person_1.possessive_title]'s pussy."
        $ guy_source = 2
        $ girl_one_source = 0
        $ girl_two_source = 1
        $ skill_tag_guy = "Oral"
        $ skill_tag_p1 = "Foreplay"
        $ skill_tag_p2 = "Oral"
        return
    else:
        "You pull back on [the_person_2.possessive_title]'s hair for a bit. Your cock springs free from her mouth with a satisfying plop. She looks up at you and smiles."
        mc.name "Mmm, that was good [the_person_2.title]. Time to get back to [the_person_1.title]..."
        "You lower yourself down until you are lined up with [the_person_1.possessive_title]'s pussy. She moans as you slide yourself back into her, but it is muffled by [the_person_2.possessive_title]'s hips as she rides her face."
        "You slide yourself into her slick cunt a few times, filling her eager hole with your dick."
        $ guy_source = 1
        $ girl_one_source = 0
        $ girl_two_source = 1
        $ skill_tag_guy = "Vaginal"
        $ skill_tag_p1 = "Vaginal"
        $ skill_tag_p2 = "Oral"
        return

    return
