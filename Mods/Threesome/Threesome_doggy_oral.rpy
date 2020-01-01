transform threesome_doggy_oral_girl_one_transform():
    xalign 1.0
    yalign 1.0
    xpos 1.0
    ypos 0.92
    zoom 0.65


transform threesome_doggy_oral_girl_two_transform():
    xalign 1.0
    yalign 1.0
    xpos 1.0
    ypos 1.0
    zoom 0.8

init:
    python:
        threesome_doggy_oral_fuck_girl_two_vagina = Threesome_MC_position(name = "fuck_girl_2_vagina",
            description = "Fuck [the_person_two.title]",
            skill_tag_p1 = "Foreplay",
            skill_tag_p2 = "Vaginal",
            girl_one_arousal = 15,
            girl_two_arousal = 20,
            girl_one_source = 0,
            girl_two_source = 1,
            girl_one_energy = 8,
            girl_two_energy = 12,
            guy_arousal = 20,
            guy_source = 1,
            guy_energy = 10,
            skill_tag_guy = "Vaginal",
            intro = "intro_threesome_doggy_oral_fuck_girl_two_vagina",
            scenes = ["scene_threesome_doggy_oral_fuck_girl_two_vagina_1", "scene_threesome_doggy_oral_fuck_girl_two_vagina_2"],
            outro = "outro_threesome_doggy_oral_fuck_girl_two_vagina",
            strip_description = "strip_threesome_doggy_oral_fuck_fuck_girl_two_vagina",
            strip_ask_description = "strip_ask_threesome_doggy_oral_fuck_fuck_girl_two_vagina",
            orgasm_description = "orgasm_threesome_doggy_oral_fuck_fuck_girl_two_vagina",
            swap_description = "swap_threesome_doggy_oral_fuck_fuck_girl_two_vagina",
            requirement = requirement_hard_both_vagina_available)

        threesome_doggy_oral_fuck_girl_two_anal = Threesome_MC_position(name = "fuck_girl_2_anal",
            description = "Ass fuck [the_person_two.title]",
            skill_tag_p1 = "Foreplay",
            skill_tag_p2 = "Anal",
            girl_one_arousal = 15,
            girl_two_arousal = 22,
            girl_one_source = 0,
            girl_two_source = 1,
            girl_one_energy = 8,
            girl_two_energy = 12,
            guy_arousal = 22,
            guy_source = 1,
            guy_energy = 11,
            skill_tag_guy = "Anal",
            intro = "intro_threesome_doggy_oral_fuck_girl_two_anal",
            scenes = ["scene_threesome_doggy_oral_fuck_girl_two_anal_1", "scene_threesome_doggy_oral_fuck_girl_two_anal_2"],
            outro = "outro_threesome_doggy_oral_fuck_girl_two_anal",
            strip_description = "strip_threesome_doggy_oral_fuck_fuck_girl_two_anal",
            strip_ask_description = "strip_ask_threesome_doggy_oral_fuck_fuck_girl_two_anal",
            orgasm_description = "orgasm_threesome_doggy_oral_fuck_fuck_girl_two_anal",
            swap_description = "swap_threesome_doggy_oral_fuck_fuck_girl_two_anal",
            requirement = requirement_hard_both_vagina_available)


        threesome_doggy_oral = Threesome_Position(name = "Doggy Girl With Cunnilingus",
            slut_requirement = 70,
            position_one_tag = "missionary",
            position_two_tag = "doggy",
            girl_one_final_description = "On your back and play with yourself",
            girl_two_final_description = "On your knees and lick her pussy",
            requires_location = "Lay",
            requirements = requirement_test,
            verb = "fuck",
            p1_transform = threesome_doggy_oral_girl_one_transform,
            p2_transform = threesome_doggy_oral_girl_two_transform,
            can_swap = True,)

        threesome_doggy_oral.mc_position = [threesome_doggy_oral_fuck_girl_two_vagina, threesome_doggy_oral_fuck_girl_two_anal]
        #list_of_threesomes.append(threesome_doggy_oral)
