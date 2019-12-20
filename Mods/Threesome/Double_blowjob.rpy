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

        threesome_double_blowjob_oral_girl_one = Threesome_MC_position(name = "oral_girl_1",
            description = "Get blowjob from left girl",
            skill_tag_p1 = "Oral",
            skill_tag_p2 = "Oral",
            girl_one_arousal = 6,
            girl_two_arousal = 4,
            girl_one_source = 0,
            girl_two_source = 0,
            girl_one_energy = 15,
            girl_two_energy = 15,
            guy_arousal = 20,
            guy_source = 1,
            guy_energy = 5,
            skill_tag_guy = "Oral",
            intro = "intro_threesome_double_blowjob_oral_girl_one",
            scenes = ["scene_threesome_double_blowjob_oral_girl_one_1", "scene_threesome_double_blowjob_oral_girl_one_2"],
            outro = "outro_threesome_double_blowjob_oral_girl_one",
            strip_description = "strip_threesome_double_blowjob_oral_girl_one",
            strip_ask_description = "strip_ask_threesome_double_blowjob_oral_girl_one",
            orgasm_description = "orgasm_threesome_double_blowjob_oral_girl_one",
            swap_description = "swap_threesome_double_blowjob_oral_girl_one",
            requirement = requirement_test)

        threesome_double_blowjob_oral_girl_two = Threesome_MC_position(name = "oral_girl_2",
            description = "Get blowjob from right girl",
            skill_tag_p1 = "Oral",
            skill_tag_p2 = "Oral",
            girl_one_arousal = 4,
            girl_two_arousal = 6,
            girl_one_source = 0,
            girl_two_source = 0,
            girl_one_energy = 15,
            girl_two_energy = 15,
            guy_arousal = 20,
            guy_source = 2,
            guy_energy = 5,
            skill_tag_guy = "Oral",
            intro = "intro_threesome_double_blowjob_oral_girl_two",
            scenes = ["scene_threesome_double_blowjob_oral_girl_two_1", "scene_threesome_double_blowjob_oral_girl_two_2"],
            outro = "outro_threesome_double_blowjob_oral_girl_two",
            strip_description = "strip_threesome_double_blowjob_oral_girl_two",
            strip_ask_description = "strip_ask_threesome_double_blowjob_oral_girl_two",
            orgasm_description = "orgasm_threesome_double_blowjob_oral_girl_two",
            swap_description = "swap_threesome_double_blowjob_oral_girl_two",
            requirement = requirement_test)


        threesome_double_blowjob = Threesome_Position(name = "Sixty Nine Plus One",
            slut_requirement = 60,
            position_one_tag = "blowjob",
            position_two_tag = "blowjob",
            girl_one_final_description = "On your knees too",
            girl_two_final_description = "On your knees too",
            requires_location = "Kneel",
            requirements = requirement_disable_position,
            verb = "throat",
            p1_transform = threesome_double_blowjob_one_transform,
            p2_transform = threesome_double_blowjob_two_transform,
            can_swap = True,)

        threesome_double_blowjob.mc_position = [threesome_double_blowjob_oral_girl_one,threesome_double_blowjob_oral_girl_two]
        list_of_threesomes.append(threesome_double_blowjob)

label intro_threesome_double_blowjob_oral_girl_one(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "This scene in progress"

label scene_threesome_double_blowjob_oral_girl_one_1(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "This scene in progress"

label scene_threesome_double_blowjob_oral_girl_one_2(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "This scene in progress"

label outro_threesome_double_blowjob_oral_girl_one(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "This scene in progress"

label strip_threesome_double_blowjob_oral_girl_one(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "This scene in progress"

label strip_ask_threesome_double_blowjob_oral_girl_one(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "This scene in progress"

label orgasm_threesome_double_blowjob_oral_girl_one(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "This scene in progress"

label swap_threesome_double_blowjob_oral_girl_one(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "This scene in progress"





#Girl two

label intro_threesome_double_blowjob_oral_girl_two(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "This scene in progress"

label scene_threesome_double_blowjob_oral_girl_two_1(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "This scene in progress"

label scene_threesome_double_blowjob_oral_girl_two_2(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "This scene in progress"

label outro_threesome_double_blowjob_oral_girl_two(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "This scene in progress"

label strip_threesome_double_blowjob_oral_girl_two(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "This scene in progress"

label strip_ask_threesome_double_blowjob_oral_girl_two(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "This scene in progress"

label orgasm_threesome_double_blowjob_oral_girl_two(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "This scene in progress"

label swap_threesome_double_blowjob_oral_girl_two(the_girl_1, the_girl_2, the_location, the_object, the_round):
    "This scene in progress"
