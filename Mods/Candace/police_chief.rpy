init 5 python:
    add_label_hijack("normal_start", "create_police_chief")

    def police_chief_titles(person):
        valid_titles = ["Officer " + person.last_name]
        if person.love > 30:
            valid_titles.append("Officer " + person.name)
        if person.sluttiness > 40:
            valid_titles.append("Officer Cumslut")
        if person.sluttiness > 70:
            valid_titles.append("Officer Cornhole")
        return valid_titles

    def police_chief_possessive_titles(person):
        valid_possessive_titles = ["The police chief"]
        if person.love > 30:
            valid_possessive_titles.append("Your police chief")
        if person.sluttiness > 40:
            valid_possessive_titles.append("Your police bitch")
        if person.sluttiness > 70:
            valid_possessive_titles.append("Your anal cop")
        return valid_possessive_titles

    def add_police_chief_character():
        police_chief_wardrobe = wardrobe_from_xml("Cop_Wardrobe")

        police_chief_personality = Personality("police_chief", default_prefix = "reserved",
            common_likes = ["pants", "small talk", "working", "the colour blue", "the colour black", "boots", "sports", "working", "work uniforms"],
            common_sexy_likes = ["taking control", "anal sex", "sex standing up", "anal creampies", "getting head"],
            common_dislikes = ["Mondays", "the colour yellow", "the colour pink", "skirts", "dresses", "high heels", "flirting"],
            common_sexy_dislikes = ["being submissive", "bareback sex", "skimpy outfit", "showing her tits", "showing her ass", "not wearing underwear", "cum facials", "incest"],
            titles_function = police_chief_titles, possessive_titles_function = police_chief_possessive_titles, player_titles_function = reserved_player_titles)

        global police_chief
        police_chief = make_person(name = "Christine", last_name = "Lavardin", age = 34, body_type = "thin_body", face_style = "Face_4", tits = "C", height = 0.91, \
            hair_colour = ["knight red", [0.745, 0.117, 0.235,1]], hair_style = short_hair, skin="white", eyes = "emerald", name_color = "#fcf7de", dial_color = "#fcf7de",  \
            stat_array = [4,6,2], skill_array = [2,1,4,1,2], sex_array = [0,1,1,4], start_sluttiness = -20, start_obedience = -40, start_happiness = 89, start_love = 0, \
            generate_insta = False, generate_dikdok = False, generate_onlyfans = False, relationship = "Single", \
            kids = 0, force_random = True, starting_wardrobe = police_chief_wardrobe, personality = police_chief_personality,
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
        police_chief.idle_pose = "stand3"   # forced idle pose
        police_chief.generate_home()
        police_chief.set_schedule(police_chief.home, times = [0,4])
        police_chief.set_schedule(police_station, times = [1,2,3])  # for now no free-roam (workaholic)
        police_chief.home.add_person(police_chief)
        return

label create_police_chief(stack):
    python:
        add_police_chief_character()
        execute_hijack_call(stack)
    return

label police_chief_introduction(the_person):
    mc.name "Excuse me, officer?"
    "She looks up and measures you with a methodical glance."
    $ the_person.set_title("???")
    the_person "Yes citizen, how can I be of service?"
    mc.name "Ah yes, how may I address you?"
    $ title_choice = get_random_title(the_person)
    $ formatted_title = the_person.create_formatted_title(title_choice)
    the_person "Well then, you can address me as [formatted_title]."
    $ the_person.set_title(title_choice)
    $ the_person.set_possessive_title(get_random_possessive_title(the_person))
    "[the_person.possessive_title] looks you straight in the eyes."
    the_person "What's your name, citizen?"
    return

label police_chief_greetings(the_person):
    if the_person.love < 0:
        the_person "Yes, citizen, how can I help you?"
    elif the_person.happiness < 90:
        the_person "Hello citizen, what's your problem?"
    else:
        if the_person.sluttiness > 60:
            if the_person.obedience > 130:
                the_person "Hello [the_person.mc_title], how can I be of assistance?"
            else:
                the_person "Hello [the_person.mc_title], what can I do for you today?"
        else:
            if the_person.obedience > 130:
                the_person "Hello [the_person.mc_title], is there something I can help you with?"
            else:
                the_person "Hello [the_person.mc_title], how can I help you today?"
    return
