init 5 python:
    add_label_hijack("normal_start", "create_police_chief")

    def add_police_chief_character():
        police_chief_wardrobe = wardrobe_from_xml("Cop_Wardrobe")

        global police_chief
        police_chief = make_person(name = "Christine", last_name = "Lavardin", age = 34, body_type = "thin_body", face_style = "Face_4", tits = "C", height = 0.91, \
            hair_colour = ["knight red", [0.745, 0.117, 0.235,1]], hair_style = short_hair, skin="white", eyes = "emerald", name_color = "#fcf7de", dial_color = "#fcf7de",  \
            stat_array = [4,6,2], skill_array = [2,1,4,1,2], sex_array = [0,1,1,4], start_sluttiness = 5, start_obedience = -40, start_happiness = 89, start_love = 0, \
            kids = 0, force_random = True, starting_wardrobe = police_chief_wardrobe, personality = reserved_personality,
            forced_opinions = [
                ["pants", 2, False],
                ["the colour blue", 2, True],
                ["the colour black", 1, False],
                ["boots", 2, False],
                ["sports", 1, True],
                ["working", 2, False],
                ["work uniforms", 2, True],
            ], forced_sexy_opinions = [
                ["taking control", 2, False],
                ["anal sex", 2, False],
                ["sex standing up", 1, False],
                ["being submissive", -2, False],
                ["skimpy outfits", -2, False],
                ["showing her tits", -1, False],
                ["showing her ass", -1, False],
                ["not wearing underwear", -2, False],
            ])
        police_chief.generate_home()
        police_chief.set_schedule(police_chief.home, times = [0,4])
        police_chief.set_schedule(police_station, times = [1,2,3])  # for now no free-roam (workaholic)
        police_chief.home.add_person(police_chief)

        police_chief.set_possessive_title("the police chief")
        police_chief.set_mc_title("Mr." + mc.last_name)
        police_chief.set_title("Officer " + police_chief.last_name)
        return

label create_police_chief(stack):
    python:
        add_police_chief_character()
        execute_hijack_call(stack)
    return
