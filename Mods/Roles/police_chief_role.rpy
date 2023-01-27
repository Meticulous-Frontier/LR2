default police_chief = None

init 5 python:
    add_label_hijack("normal_start", "create_police_chief")

    def police_chief_hire_function(the_person):
        global police_chief
        if police_chief is None:
            police_chief = the_person

    def police_chief_quit_function(the_person):
        global police_chief
        if police_chief is the_person:
           police_chief = None

    def check_police_chief_met():
        if police_chief.title is None:  # haven't met, set title
            police_chief.set_possessive_title("The police chief")
            police_chief.set_mc_title("Mr. " + mc.last_name)
            police_chief.set_title("Officer " + police_chief.last_name)
        return

    def add_police_chief_character():
        police_chief_wardrobe = wardrobe_from_xml("Cop_Wardrobe")
        cop_outfit = police_chief_wardrobe.get_outfit_with_name("Cop")

        global police_chief_uniform_wardrobe
        police_chief_uniform_wardrobe = Wardrobe("Cop Uniform")
        police_chief_uniform_wardrobe.add_outfit(cop_outfit)
        police_chief_wardrobe.remove_outfit(cop_outfit)

        police_job = Job("Police Chief", critical_job_role, police_station, work_times = [1, 2],
            hire_function = police_chief_hire_function, quit_function = police_chief_quit_function)
        police_job.schedule.set_schedule(mall, the_days = [0,2,4], the_times = [1]) #patrol mall
        police_job.schedule.set_schedule(downtown, the_days=[1,3], the_times=[2]) # patrol downtown
        police_job.schedule.set_schedule(downtown_bar, the_days=[5,6], the_times=[3]) # patrol bar
        police_job.schedule.set_schedule(strip_club, the_days=[5,6], the_times=[4]) # patrol strip club (Does she have a kinky side?)

        global christine
        christine = make_person(name = "Christine", last_name = "Lavardin", age = 34, body_type = "thin_body", face_style = "Face_4", tits = "C", height = 0.91, \
            hair_colour = ["knight red", [.745, .117, .235, 1]], hair_style = short_hair, skin="white", eyes = "emerald", name_color = "#fcf7de", dial_color = "#fcf7de",  \
            stat_array = [4,6,2], skill_array = [2,1,4,1,2], sex_skill_array = [0,1,1,4], sluttiness = -20, obedience_range = [50, 70], happiness = 89, love = 0, \
            generate_insta = False, generate_dikdok = False, generate_onlyfans = False, relationship = "Single", job = police_job, \
            kids = 0, force_random = True, starting_wardrobe = police_chief_wardrobe, personality = cop_personality, type = 'story',
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
        christine.idle_pose = "stand3"   # forced idle pose
        christine.generate_home()
        christine.home.add_person(christine)
        christine.event_triggers_dict["times_arrested"] = 0
        return

label create_police_chief(stack):
    python:
        add_police_chief_character()
        execute_hijack_call(stack)
    return

label police_chief_public_sex_intervention(the_person):
    if police_chief is None:
        "You really should have been arrested for this."
        return

    police_chief "Hey! What are you doing? You can't do that at the [mc.location.formal_name]!"
    $ police_chief.draw_person()
    "Suddenly, a police officer arrives. You stop what you are doing with [the_person.possessive_title]."
    police_chief "God, get decent. I'm taking you two downtown!"
    $ the_person.apply_planned_outfit()
    $ mc.change_location(police_station)
    $ mc.location.show_background()
    $ scene_manager = Scene()
    $ scene_manager.add_actor(police_chief)
    $ scene_manager.add_actor(the_person, position = "sitting", display_transform = character_left_flipped)
    "You and [the_person.title] are escorted to the police station by the police officer. You spend a couple hours doing paperwork."
    call mc_arrested_penalties from _arrested_public_sex_01
    "You and [the_person.possessive_title] go your separate ways for now. She doesn't seem eager to chat about getting arrested."
    call advance_time from _call_advance_time_after_arrested_1
    jump game_loop
    return

label mc_arrested_penalties():
    if mc_times_arrested() == 0:
        $ mc.business.change_funds(-100)
        "Since this is your first offense, you get off with a light fine."
        $ police_chief.event_triggers_dict["times_arrested"] = 0
    elif mc_times_arrested() == 1:
        $ mc.business.change_funds(-500)
        "Since this is your second offense, you get fined."
        police_chief "Seriously, don't do that again. You can't be doing that stuff in public!"
    elif mc_times_arrested() == 2:
        $ mc.business.change_funds(-5000)
        "Since this is your third offense, you receive a heavy fine."
        police_chief "I guess you still haven't learned your lesson. I'm fining you the maximum amount under the law."
        police_chief "If this happens again, I'll have to let the city know you got problems with authority. Catch my drift?"
    elif mc_times_arrested() == 3:
        $ mc.business.change_funds(-5000)
        "You once again receive a heavy fine."
        police_chief "Damn, you just can't keep your hands to yourself, can you?"
        police_chief "Guess I'll have to call this in to the city. Where did you say you work again?"
        $ mc.business.attention += 20
    elif mc_times_arrested() == 3:
        $ mc.business.change_funds(-5000)
        "You once again receive a heavy fine."
        police_chief "Still screwing around with whores in public are you?"
        police_chief "Guess last time I didn't word my request with the city strongly enough."
        $ mc.business.attention += 50
    else:
        $ mc.business.change_funds(-5000)
        "You once again receive a heavy fine."
        police_chief "Again. You're here AGAIN. "
        police_chief "Enough is enough. Get out of here, I'm sure the city will be checking out your business now soon enough."
        $ mc.business.attention += 100
    $ police_chief.event_triggers_dict["times_arrested"] += 1
    return
init 2 python:
    def mc_times_arrested():
        return police_chief.event_triggers_dict.get("times_arrested", 0)
