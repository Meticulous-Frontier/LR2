transform threesome_double_blowjob_one_transform():
    xalign 1.0
    yalign 1.0
    xpos 0.87
    ypos 1.0
    xzoom -1.0


transform threesome_double_blowjob_two_transform():
    xalign 1.0
    yalign 1.0
    xpos 1.0
    ypos 1.0
    zoom 1.0

init:
    python:

        threesome_double_blowjob_focus_oral= Threesome_MC_position(name = "focus_oral",
            description = "Focus on Oral",
            skill_tag_p1 = "Oral",
            skill_tag_p2 = "Oral",
            girl_one_arousal = 5,
            girl_two_arousal = 5,
            girl_one_source = 0,
            girl_two_source = 0,
            girl_one_energy = 15,
            girl_two_energy = 15,
            guy_arousal = 20,
            guy_source = 1,
            guy_energy = 5,
            skill_tag_guy = "Oral",
            intro = "intro_threesome_double_blowjob_focus_oral",
            scenes = ["scene_threesome_double_blowjob_focus_oral_1", "scene_threesome_double_blowjob_focus_oral_2"],
            outro = "outro_threesome_double_blowjob_focus_oral",
            strip_description = "strip_threesome_double_blowjob_focus_oral",
            strip_ask_description = "strip_ask_threesome_double_blowjob_focus_oral",
            orgasm_description = "orgasm_threesome_double_blowjob_focus_oral",
            swap_description = "swap_threesome_double_blowjob_focus_oral",
            requirement = requirement_hard)

        threesome_double_blowjob_makeout = Threesome_MC_position(name = "Makeout",
            description = "Makeout",
            skill_tag_p1 = "Oral",
            skill_tag_p2 = "Oral",
            girl_one_arousal = 12,
            girl_two_arousal = 12,
            girl_one_source = 2,
            girl_two_source = 1,
            girl_one_energy = 15,
            girl_two_energy = 15,
            guy_arousal = 20,
            guy_source = 1,
            guy_energy = 5,
            skill_tag_guy = "Oral",
            intro = "intro_threesome_double_blowjob_makeout",
            scenes = ["scene_threesome_double_blowjob_makeout_1", "scene_threesome_double_blowjob_makeout_2"],
            outro = "outro_threesome_double_blowjob_makeout",
            strip_description = "strip_threesome_double_blowjob_makeout",
            strip_ask_description = "strip_ask_threesome_double_blowjob_makeout",
            orgasm_description = "orgasm_threesome_double_blowjob_makeout",
            swap_description = "swap_threesome_double_blowjob_makeout",
            requirement = requirement_disable_position)


        threesome_double_blowjob = Threesome_Position(name = "Sixty Nine Plus One",
            slut_requirement = 60,
            position_one_tag = "blowjob",
            position_two_tag = "blowjob",
            girl_one_final_description = "On your knees too",
            girl_two_final_description = "On your knees too",
            requires_location = "Kneel",
            requirements = requirement_hard,
            verb = "throat",
            p1_transform = threesome_double_blowjob_one_transform,
            p2_transform = threesome_double_blowjob_two_transform,
            can_swap = True,)

        threesome_double_blowjob.mc_position = [threesome_double_blowjob_focus_oral,threesome_double_blowjob_makeout]
        list_of_threesomes.append(threesome_double_blowjob)

label intro_threesome_double_blowjob_focus_oral(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "As the girls get on their knees, you run your hands through their hair."
    mc.name "I want you two to focus on me for a bit."
    if the_girl_1.get_opinion_score("giving blowjobs") > 0:
        the_girl_1.char "Mmm, you want to feel us slobbering all over your cock, [the_girl_1.mc_title]?"
    else:
        the_girl_1.char "I don't usually give blowjobs, but with [the_girl_2.name] here it should be fun!"
    if the_girl_2.get_opinion_score("giving blowjobs") > 0:
        the_girl_1.char "This is gonna great, I can lick your balls while she's blowing you, [the_girl_2.mc_title]!"
    else:
        the_girl_2.char "I wonder how long you can last with two girls on their knees for you, [the_girl_2.mc_title]."
    "[the_girl_1.possessive_title] and [the_girl_2.possessive_title] get to work servicing your cock."
    return

label scene_threesome_double_blowjob_focus_oral_1(the_girl_1, the_girl_2, the_location, the_object, the_round):
    #Girl 1 services you
    #TODO scene modifier for blowing
    "[the_girl_1.title] opens up and begins to blow you. Her tongue works circle around your head as she gives you shallow strokes."
    "[the_girl_2.title] moves her head lower and gently suckles on your ballsack. She gently sucks one into her mouth, then moves over to the other."
    if the_girl_2.get_opinion_score("giving blowjobs") > 0:
        "You feel a pleasrable vibration in your testicles as [the_girl_2.possessive_title] starts to hum a bit."
    "The sensations of having two mouths pleasuring you is intense."
    mc.name "Damn girls, that feels amazing!"
    "[the_girl_1.title] comes up for air, then runs her mouth along the side of your cock. [the_girl_2.title] notices and her mouth to the opposite side of your cock."
    "They slowly stroke your cock together, mouths on opposite sides of your acheing hard on."
    return

label scene_threesome_double_blowjob_focus_oral_2(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "[the_girl_2.title] opens up and takes a turn focusing on your. She takes the base in her hand and gives you long, deep strokes."
    $ scene_manager.update_actor(the_girl_1, position = "kissing")
    "[the_girl_1.title] takes a moment and stands up, wrapping her hands around you. She begins kissing your neck and along your jawline."
    "[the_girl_1.possessive_title]'s lips on your neck, her body against yours, and [the_girl_2.possessive_title]'s mouth on your cock. This must be heaven."
    "[the_girl_1.title] slowly kisses lower on your neck, moving down your collarbone. She continues to descend, licking and nipping at your chest and nipples."
    $ scene_manager.update_actor(the_girl_1, position = "blowjob")
    "She continues descending, kissing down your belly until she is back on her knees. When [the_girl_2.title] comes off she takes you in your hand and gives you a few strokes."
    return

label outro_threesome_double_blowjob_focus_oral(the_girl_1, the_girl_2, the_location, the_object, the_round):
    #Since the girls are pretty much in control, they determine where you cum.
    "Soon, the mouths of the beautiful girls on their knees in front of you drive you past the point of no return. Your orgasm is swiftly approaching."
    mc.name "Oh god, I'm gonna cum!"
    if the_girl_1.get_opinion_score("drinking cum") > 1:
        "[the_girl_1.possessive_title] immediately grabs your cock, opens up and takes your tip in her mouth."
        "[the_girl_2.title] moves down and strokes the side of your cock as you begin to ejaculate into [the_girl_1.title]'s eager mouth."
        $ the_girl_1.cum_in_mouth()
        $ scene_manager.draw_scene()
        "You dump wave after wave of cum into [the_girl_1.title]'s mouth."
        if the_girl_2.get_opinion_score("drinking cum") > 0:
            "As you finish, you slowly pull back. Some of your cum slowly dribbles out of her mouth."
            the_girl_2.char "Hey! Save some for me!"
            "[the_girl_2.title] leans toward's her blowjob partner and begins kissing and licking your cum off her face."
            "Soon, they are full on making out, swapping your cum between their mouths."
            $ the_girl_2.cum_in_mouth()
            $ scene_manager.draw_scene()
            "When they finish, they look up at you, remnants of your cum still visible at the corner of their mouths."
            return
        "You slowly pull back. Some of your cum slowly dribbles out of her mouth."
        return
    elif the_girl_2.get_opinion_score("drinking cum") > 0:
        "[the_girl_2.possessive_title] immediately grabs your cock, opens up and takes your tip in her mouth."
        "[the_girl_1.title] strokes your cock with her hand as you fire your load into the back of [the_girl_2.title]'s mouth."
        $ the_girl_2.cum_in_mouth()
        $ scene_manager.draw_scene()
        "As you finish, you slowly pull back. Some of your cum slowly dribbles out of her mouth."
        return
    "You take your cock and begin to stroke it. Both girls look up at you as you get ready to finish."
    "Your orgasm hits and you being spraying down their beautiful faces with their seed."
    $ the_girl_1.cum_on_face()
    $ scene_manager.draw_scene()
    "Your first couple of spurts hit [the_girl_1.title] in the face. She gives a sigh when she feels your warm seed."
    "You point your cock at [the_girl_2.title] and fire another couple of rounds."
    $ the_girl_2.cum_on_face()
    $ scene_manager.draw_scene()
    "When you finish, both of the girl's faces are covered in your sticky cum."
    return

label strip_threesome_double_blowjob_focus_oral(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "This scene in progress"

label strip_ask_threesome_double_blowjob_focus_oral(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "This scene in progress"

label orgasm_threesome_double_blowjob_focus_oral(the_girl_1, the_girl_2, the_location, the_object, the_round):
    if the_girl_1.arousal > 100 and the_girl_2.arousal > 100:  #Both girls orgasm#
        "You can feel the pace of the double blowjob pick up a bit as both girls begin moaning at each other."
        "When you look down, you can see that each girl has a hand along the other's crotch... have they been doing that the whole time?"
        "They both orgasm, almost in unison. As they do the kiss and grope each other, momentarily ignoring your erection."
        "As they start to wind down, you turn the attention back to you."
        mc.name "That was hot, but don't forget about me."
        return

    elif the_girl_1.arousal > 100:   #Just girl 1 orgasms
        "You can feel [the_girl_1.title] moaning around your cock with increasing intensity. When you look down, you notice [the_girl_2.title]'s hand petting her crotch."
        "An orgasm hits her. She takes your cock into her mouth and moans around it loudly. The vibrations feel amazing."
        "When she finishes, she briefly comes up for air."
        the_girl_1.char "Oh fuck that was good. I need a second."
        "She sits back and [the_girl_2.title] takes over for her while she recovers."
        return

    elif the_girl_2.arousal > 100:   #Just girl 2 orgasms
        "You can feel [the_girl_2.title] moaning around your cock with increasing intensity. When you look down, you notice [the_girl_1.title]'s hand petting her crotch."
        "An orgasm hits her. She takes your cock into her mouth and moans around it loudly. The vibrations feel amazing."
        "When she finishes, she briefly comes up for air."
        the_girl_2.char "Oh fuck that was good. I need a second."
        "She sits back and [the_girl_1.title] takes over for her while she recovers."
        return
    return

label swap_threesome_double_blowjob_focus_oral(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "You decide to change things up a bit. You run your hands through their hair, pulling them toward your cock."
    mc.name "I want you two to focus on me for a bit."
    if the_girl_1.get_opinion_score("giving blowjobs") > 0:
        the_girl_1.char "Mmm, you want to feel us slobbering all over your cock, [the_girl_1.mc_title]?"
    else:
        the_girl_1.char "I don't usually give blowjobs, but with [the_girl_2.name] here it should be fun!"
    if the_girl_2.get_opinion_score("giving blowjobs") > 0:
        the_girl_1.char "This is gonna great, I can lick your balls while she's blowing you, [the_girl_2.mc_title]!"
    else:
        the_girl_2.char "I wonder how long you can last with two girls on their knees for you, [the_girl_2.mc_title]."
    "[the_girl_1.possessive_title] and [the_girl_2.possessive_title] get to work servicing your cock."
    return




#Makeout. In this scene 1, the girls makeout while on their knees in front of you, touching and caressing each other.
#In scene 2, girls make out around MC's cock

label intro_threesome_double_blowjob_makeout(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "This scene in progress"

label scene_threesome_double_blowjob_makeout_1(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "This scene in progress"

label scene_threesome_double_blowjob_makeout_2(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "This scene in progress"

label outro_threesome_double_blowjob_makeout(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "This scene in progress"

label strip_threesome_double_blowjob_makeout(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "This scene in progress"

label strip_ask_threesome_double_blowjob_makeout(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "This scene in progress"

label orgasm_threesome_double_blowjob_makeout(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "This scene in progress"

label swap_threesome_double_blowjob_makeout(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "This scene in progress"
