init 2 python:
    erica_workout_wardrobe = wardrobe_from_xml("Erica_W_Wardrobe")
    workout_wardrobe = wardrobe_from_xml("Workout_Wardrobe")
    def erica_mod_initialization(): #Add actionmod as argument#

        erica_wardrobe = wardrobe_from_xml("Erica_Wardrobe") # default wardrobe when not in gym (no xml file, no wardrobe)
        erica_base_outfit = Outfit("Erica's base accessories")
        the_eye_shadow = heavy_eye_shadow .get_copy()
        the_eye_shadow.colour = [.20, .20, .37, 0.50]
        the_rings = copper_ring_set.get_copy() #Change this
        copper_ring_set.colour = [.1,.36,.19,1.0]
        erica_base_outfit.add_accessory(the_eye_shadow)
        erica_base_outfit.add_accessory(the_rings)

        erica_student_job = Job("College Athlete", erica_role, job_location = university, work_times = [2])
        erica_student_job.schedule.set_schedule(gym, the_times = [1, 3])
        erica_student_job.schedule.set_schedule(gym, the_days = [5, 6], the_times = [1, 2])

        global erica
        erica = make_person(name = "Erica", age = 19, body_type = "thin_body", face_style = "Face_4", tits="B", height = 0.89, hair_colour="chestnut brown", hair_style = braided_bun, skin="white" , \
            eyes = "light blue", personality = erica_personality, name_color = "#89CFF0", dial_color = "89CFF0" , starting_wardrobe = erica_wardrobe, \
            stat_array = [2,4,4], skill_array = [4,1,3,3,1], sex_skill_array = [3,2,3,2], sluttiness = 3, obedience_range = [70, 85], happiness = 119, love = 0, \
            title = "Erica", possessive_title = "Your gym girl", mc_title = mc.name, relationship = "Single", kids = 0, force_random = True, base_outfit = erica_base_outfit, type = 'story', \
            forced_opinions = [["production work", 2, True], ["work uniforms", -1, False], ["flirting", 1, False], ["pants", 1, False], ["the colour blue", 2, False], ["yoga", 2, False], ["sports", 2, False]],
            forced_sexy_opinions = [["doggy style sex", 2, True], ["missionary style sex", -2, False], ["giving blowjobs", 1, False], ["getting head", 1, False], ["being submissive", 1, False], ["creampies", -2, False], ["public sex", 1, False]])

        erica.max_energy = 120
        erica.generate_home()
        erica.change_job(erica_student_job, job_known = True)
        erica.home.add_person(erica)

        erica.event_triggers_dict["reject_position"] = "standing_doggy"
        erica.event_triggers_dict["erica_progress"] = 0
        erica.event_triggers_dict["erica_workout"] = 0
        erica.event_triggers_dict["love_path"] = False
        erica.event_triggers_dict["fwb_path"] = False
        erica.event_triggers_dict["hate_path"] = False
        erica.event_triggers_dict["protein_day"] = 9999
        erica.event_triggers_dict["insta_pic_started"] = False
        erica.event_triggers_dict["insta_pic_intro_complete"] = False
        erica.event_triggers_dict["yoga_quest_started"] = False
        erica.event_triggers_dict["yoga_sessions_started"] = False
        erica.event_triggers_dict["nude_yoga"] = False
        erica.event_triggers_dict["looking_for_work"] = False
        erica.event_triggers_dict["yoga_assistant"] = None
        erica.event_triggers_dict["post_insta_handy"] = False
        erica.event_triggers_dict["wake_up_options"] = ["handjob"]
        erica.event_triggers_dict["team_reinstate_day"] = 9999
        erica.event_triggers_dict["morning_wakeup_pref"] = 0
        erica.event_triggers_dict["pre_insta_blowjob"] = False
        erica.event_triggers_dict["post_yoga_fuck"] = False
        erica.event_triggers_dict["kicked_off_team"] = False
        erica.event_triggers_dict["rejoin_team"] = False

        erica.fertility_percent = -100.0 #Erica refuses to get pregnant for MC, getting pregnant would cause her to be kicked from track team. Enabled with breeding fetish.

        erica.event_triggers_dict["story_dict"] = True
        erica.story_character_description = "A collegiate track and field athlete."
        erica.story_love_list = erica_story_love_list
        erica.story_lust_list = erica_story_lust_list
        erica.story_teamup_list = erica_story_teamup_list
        erica.story_other_list = erica_story_other_list


        town_relationships.update_relationship(nora, erica, "Friend")
        # town_relationships.update_relationship(lily, erica, "Friend")


        erica.add_unique_on_room_enter_event(erica_intro_action)

        #REMARKS: Erica has a few instance specific class overrides. This is my first time testing this type of programming, hopefully it works correctly.
        erica.apply_gym_outfit = erica_apply_gym_outfit

        # game_hints.append(Hint("College Athlete", "Get to know Erica to learn to give her a protein shake.", "erica_get_progress() > 0 and not erica_protein_shake_is_unlocked()", "erica_protein_shake_is_unlocked()"))
        # game_hints.append(Hint("College Athlete", "Get at least 120 max energy and Erica to at least 40 sluttiness.", "erica_get_progress() == 1 and erica_protein_shake_is_unlocked()", "erica_get_progress() > 1"))
        # game_hints.append(Hint("College Athlete", "Get at least 140 max energy and Erica to at least 60 sluttiness. Then challenge her to a race.", "erica_get_progress() == 2", "erica_get_progress() > 2"))

        return

    erica_yoga_poses = ["walking_away", "against_wall", "cowgirl", "doggy", "kissing", "missionary", "standing_doggy"]
    erica_yoga_pose_descriptions = {
        "walking_away" : "The girls are stretching one foot out in front of them, trying to maintain balance.",
        "against_wall" : "The girls are holding their arms out while balancing on one leg.",
        "cowgirl" : "The girls are on their knees, stretching out their backs.",
        "doggy" : "The girls are doing the downward facing dog.",
        "kissing" : "The girls are holding their arms out while doing breathing exercises.",
        "missionary" : "The girls are on their backs, stretching their legs out.",
        "standing_doggy" : "The girls are in a line, stretching their backs while they lean over."
    }

    erica_yoga_sexy_pose_descriptions = {
        "walking_away" : "The pose gives you a great view of their backsides.",
        "against_wall" : "Your eyes are drawn between their legs as they stretch.",
        "cowgirl" : "You can't help but imagine the girls mounting you in a similar pose...",
        "doggy" : "You watch intently at the room of asses pointed back at you. You think you see a couple wiggle...",
        "kissing" : "You wonder if the girls would be breathing so evenly if you were on your knees, eating them out.",
        "missionary" : "You can't help but fantasize about walking out, pinning one of the girls down, and having your way with her in this pose.",
        "standing_doggy" : "The sight of the class all bent over in front of you is breathtaking."
    }

    erica_yoga_nude_pose_descriptions = {
        "walking_away" : "Rows of ample backsides are available for your viewing pleasure.",
        "against_wall" : "Several of the girls' pussy lips are puffy, showing clear signs of arousal.",
        "cowgirl" : "You make eye contact with several of them. You can tell from the way they look at you they are thinking similar thoughts.",
        "doggy" : "Rows of fuckable cunts and asses are on display, ripe for the taking.",
        "kissing" : "You breathe deeply with them. The musk of feminine arousal is heavy in the air.",
        "missionary" : "You notice a couple girls' hands stray between their legs, their arousal on obvious display.",
        "standing_doggy" : "You wonder how many asses you could fill with cum before your cock refused to get hard again. You bet several."
    }

    #Pose list. [0] is lily's pose, [1] is ericas, [2] is playful text, [3] is sexy text.
    # erica_insta_pose_pairs = [
    #     ["back_peek", "standing_doggy", "The girls wiggle their asses a bit as you snap their pictures.", lily.title + " is twerking her hips while " + erica.possessive_title + " gives herself a couple playful spanks."],
    #     ["missionary","missionary", "The girl cross their inside legs across each other, getting close for the camera.", "The girls both put one hand between their legs, another on their chests, pretending they are masturbating."],
    #     ["doggy","stand4", erica.title + " puts a hand on "+ lily.possessive_title + "'s lower back.", erica.title + " gives a playful spank on " + lily.possessive_title + "'s ass."],
    #     ["kneeling1","kneeling1", "The girls run their hands along their sides sensually for the camera.", "The girls put a hand between their legs, pretending to masturbate for the camera."],
    #     ["blowjob","back_peek", lily.title + " licks her lips while " + erica.possessive_title + " leans forward a bit, angling her ass toward the camera.",lily.title + " gets on her knees next to " + erica.possessive_title + ", licking her lips and pretending to kiss her ass."]
    # ]

    def erica_make_insta_pose_pairs():
        insta_pose_list = [
            ["back_peek", "standing_doggy", "The girls wiggle their asses a bit as you snap their pictures.", lily.title + " is twerking her hips while " + erica.possessive_title + " gives herself a couple playful spanks."],
            ["missionary","missionary", "The girl cross their inside legs across each other, getting close for the camera.", "The girls both put one hand between their legs, another on their chests, pretending they are masturbating."],
            ["doggy","stand4", erica.title + " puts a hand on "+ lily.possessive_title + "'s lower back.", erica.title + " gives a playful spank on " + lily.possessive_title + "'s ass."],
            ["kneeling1","kneeling1", "The girls run their hands along their sides sensually for the camera.", "The girls put a hand between their legs, pretending to masturbate for the camera."],
            ["blowjob","back_peek", lily.title + " licks her lips while " + erica.possessive_title + " leans forward a bit, angling her ass toward the camera.",lily.title + " gets on her knees next to " + erica.possessive_title + ", licking her lips and pretending to kiss her ass."]
        ]
        return insta_pose_list

    def display_yoga_dialog(pose):
        renpy.say(None, erica_yoga_pose_descriptions[pose])
        if slutty_class:
            renpy.say(None, erica_yoga_sexy_pose_descriptions[pose])
            mc.change_arousal(20)
            if nude_class:
                renpy.say(None, erica_yoga_nude_pose_descriptions[pose])
                mc.change_locked_clarity(30)
            else:
                mc.change_locked_clarity(20)
        else:
            mc.change_locked_clarity(10)
        return


init -2 python:
    def erica_apply_gym_outfit(): #No access to self in object specific override
        if erica_workout_wardrobe:
            erica.apply_outfit(erica_workout_wardrobe.decide_on_outfit2(erica))
        elif workout_wardrobe:
            erica.apply_outfit(erica.personalize_outfit(workout_wardrobe.decide_on_outfit2(erica)))
        return

    def erica_intro_requirement(person):
        return person.location == gym

    def erica_get_to_know_requirement(person):
        if mc.max_energy >= 110:
            if mc.location == gym:
                return True
            else:
                return "Wait until you see her at the gym"
        else:
            return "Requires: 110 maximum energy"

    def erica_phase_one_requirement(person):
        if erica_get_progress() < 1:
            return False
        if not erica_workout_is_unlocked():
            return False
        if not erica_protein_shake_is_unlocked():
            return False
        if time_of_day < 4:
            if mc.max_energy >= 120:
                if person.effective_sluttiness() < 40:
                    return "Requires 40 Sluttiness"
                elif mc.location == gym:
                    return True
                else:
                    return "Only at the gym"
            else:
                return "Requires: 120 maximum energy"
        return False

    def erica_phase_two_requirement(person):
        if erica_get_progress() < 2 or erica_get_progress() > 3:
            return False
        if time_of_day < 4:
            if mc.max_energy >= 140:
                if person.effective_sluttiness() < 60:
                    return "Requires: 60 sluttiness"
                return True
            else:
                return "Requires: 140 maximum energy"
        return False

    def erica_race_crisis_requirement():
        return day % 7 == 5 and time_of_day == 1

    def erica_watch_race_intro_requirement(the_person):
        return False

    def erica_watch_race_requirement():
        return day % 7 == 5 and time_of_day == 1

    def erica_buy_protein_shake_requirement(person):
        if not erica_protein_shake_is_unlocked():
            return False
        if mc.location == gym:
            if day > erica_get_protein_day():
                return True
            else:
                return "Once per Day"
        else:
            return "Only at the Gym"

    def erica_house_call_requirement(person):
        if erica_get_progress() == 4:
            if mc.location == person.home:
                return True
        return False

    def erica_money_problems_sarah_talk_requirement(person):
        return mc.business.hr_director and person.is_at_work()

    def erica_money_problems_update_requirement(person):
        if time_of_day > 0 and time_of_day < 4:
            if erica_is_looking_for_work():
                return True
        return False

    def erica_money_problem_sarah_convincing_employee_requirement():
        if mc.business.is_open_for_business():
            if mc.business.hr_director and mc.is_at_work():
                if renpy.random.randint(0,100) < 25:
                    return True
        return False

    def erica_money_problems_sarah_update_requirement():
        if mc.business.is_open_for_business():
            if mc.business.hr_director and mc.is_at_work():
                if len(erica_get_yoga_class_list()) < 4:
                    if renpy.random.randint(0,100) < 10:
                        return True
        return False

    def erica_money_problems_sarah_final_update_requirement():
        if mc.business.is_open_for_business():
            if mc.business.hr_director and mc.is_at_work():
                if len(erica_get_yoga_class_list()) >= 4:
                    return True
        return False

    def erica_money_problems_yoga_start_requirement(person):
        return mc.business.hr_director and person.location == gym

    def erica_yoga_event_intro_requirement():
        return mc.business.hr_director and day%7 == 1

    def erica_weekly_yoga_requirement(person):
        return mc.business.hr_director and person.location == lobby and day%7 == 1

    def erica_lily_instapic_setup_requirement(person):
        return person.location == lily_bedroom

    def erica_lily_instapic_proposal_requirement(person):
        return person.location == gym

    def erica_lily_instapic_intro_requirement():
        return time_of_day == 4 and day%7 == 5

    def erica_lily_post_photoshoot_requirement(person):
        return time_of_day > 0 and day%7 < 5

    def erica_post_photoshoot_requirement(person):
        return person.location == gym

    def erica_lily_weekly_photoshoot_requirement(person):
        return person.location == lily.location and time_of_day == 4 and day%7 == 5

    def erica_lily_post_insta_handjob_requirement():
        if erica.is_willing(cowgirl_handjob, ignore_taboo = True) and day%7 == 6:
            return True
        return False

    def erica_post_insta_handjob_followup_requirement(the_person):
        return the_person.location == gym

    def erica_lily_post_insta_morning_requirement():
        if day%7 == 6 and erica_has_given_morning_handjob():
            return True
        return False

    def erica_breeding_fetish_followup_requirement(the_person):
        if the_person.location == gym and the_person.is_pregnant():
            if day >= the_person.event_triggers_dict.get("preg_tits_date", 9999) + 3:
                return True
        return False

    def erica_breeding_fetish_team_crisis_requirement():
        if time_of_day == 4 and erica.is_pregnant() and day%7 != 5: #SAturday pic nights
            if day >= erica.pregnancy_show_day() + 7:
                return True
        return False

    def erica_breeding_fetish_nora_followup_requirement(the_person):
        if the_person.location == university:
            return True
        return False

    def erica_breeding_nora_news_part_one_requirement():
        if time_of_day == 2:
            if renpy.random.randint(0,100) < 20: #I should probably just time this a week or something but I'm just so lazy
                return True
        return False

    def erica_breeding_nora_news_part_two_requirement():
        if time_of_day == 2:
            if renpy.random.randint(0,100) < 15: #Just to make F95 people QQ
                return True
        return False

    def erica_breeding_fetish_team_rejoin_requirement(the_person):
        return True

    def erica_discuss_morning_wakeup_requirement(the_person):
        if erica_has_given_morning_handjob() and time_of_day != 0 and time_of_day != 4:
            return True
        return False

    def erica_pre_insta_love_requirement(the_person):
        if the_person.love > 40 and the_person.is_willing(blowjob):
            return the_person.location == lily.location and time_of_day == 4 and day%7 == 5
        return False

    def erica_ghost_requirement():
        if renpy.random.randint(0,100) < 20:
            return True
        return False

    def add_erica_ghost_action(person): #Hopefully delete this soon
        mc.business.remove_mandatory_crisis("erica_ghost_label")
        erica_ghost = Action("Casual Athlete Ghosts you", erica_ghost_requirement, "erica_ghost_label", args = person)
        mc.business.add_mandatory_crisis(erica_ghost)
        return

    def make_bench():
        return Object("bench",["Sit","Lay","Low"], sluttiness_modifier = 0, obedience_modifier = 0)

#*************Create Casual Athlete Role***********#
init -1 python:
    erica_intro_action = Action("Meet Erica", erica_intro_requirement, "erica_intro_label",
        menu_tooltip = "Meet your new gym girl.")
    erica_get_to_know = Action("Get to know Her {image=gui/heart/Time_Advance.png}", erica_get_to_know_requirement, "erica_get_to_know_label",
        menu_tooltip = "Make an observation about her.")
    erica_phase_one = Action("Workout Together {image=gui/heart/Time_Advance.png}", erica_phase_one_requirement, "erica_phase_one_label",
        menu_tooltip = "Work up a sweat.")
    erica_phase_two = Action("Challenge to Race {image=gui/heart/Time_Advance.png}", erica_phase_two_requirement, "erica_phase_two_label",
        menu_tooltip = "No risk, no reward.")
    erica_protein_shake = Action("Buy Protein Shake\n{color=#ff0000}{size=18}Costs: $5{/size}{/color}", erica_buy_protein_shake_requirement,"erica_buy_protein_shake_label", menu_tooltip = "Slip some serum in.")
    erica_house_call = Action("Take Charge {image=gui/heart/Time_Advance.png}", erica_house_call_requirement, "erica_house_call_label",
        menu_tooltip = "Pick her up.")
    erica_money_problems_sarah_talk = Action("Talk to HR Director", erica_money_problems_sarah_talk_requirement, "erica_money_problems_sarah_talk_label")
    erica_money_problems_update = Action("Ask about finances", erica_money_problems_update_requirement, "erica_money_problems_update_label",
        menu_tooltip = "See if Erica has found work.")
    erica_money_problem_sarah_convincing_employee = Action("Sarah doses another employee", erica_money_problem_sarah_convincing_employee_requirement, "erica_money_problem_sarah_convincing_employee_label")
    erica_money_problems_sarah_update = Action("Sarah doesn't have enough attendants", erica_money_problems_sarah_update_requirement, "erica_money_problems_sarah_update_label")
    erica_money_problems_sarah_final_update = Action("Sarah has enough attendants", erica_money_problems_sarah_final_update_requirement, "erica_money_problems_sarah_final_update_label")
    erica_money_problems_yoga_start = Action("Talk to Erica about yoga", erica_money_problems_yoga_start_requirement, "erica_money_problems_yoga_start_label")
    erica_yoga_event_intro = Action("First yoga class", erica_yoga_event_intro_requirement, "erica_yoga_event_intro_label")
    erica_weekly_yoga = Action("Weekly yoga class", erica_weekly_yoga_requirement, "erica_weekly_yoga_label")
    erica_lily_instapic_setup = Action("Talk to Lily about Erica", erica_lily_instapic_setup_requirement, "erica_lily_instapic_setup_label")
    erica_lily_instapic_proposal = Action("Propose InstaPic session to Erica", erica_lily_instapic_proposal_requirement, "erica_lily_instapic_proposal_label")
    erica_lily_instapic_intro = Action("InstaPic session with Lily and Erica", erica_lily_instapic_intro_requirement, "erica_lily_instapic_intro_label")
    erica_lily_post_photoshoot = Action("Ask Lily about InstaPic results", erica_lily_post_photoshoot_requirement, "erica_lily_post_photoshoot_label")
    erica_post_photoshoot = Action("Convince Erica to continue Insta", erica_post_photoshoot_requirement, "erica_post_photoshoot_label")
    erica_lily_weekly_photoshoot = Action("Weekly instapic session with Lily", erica_lily_weekly_photoshoot_requirement, "erica_lily_weekly_photoshoot_label")
    erica_lily_post_insta_handjob = Action("Erica wakes you up", erica_lily_post_insta_handjob_requirement, "erica_lily_post_insta_handjob_label")
    erica_post_insta_handjob_followup = Action("Talk about Handjob", erica_post_insta_handjob_followup_requirement, "erica_post_insta_handjob_followup_label")
    erica_lily_post_insta_morning_mand = Action("Erica wakes you up", erica_lily_post_insta_morning_requirement, "erica_lily_post_insta_morning_label")
    erica_breeding_fetish_followup = Action("Erica knocked up followup", erica_breeding_fetish_followup_requirement, "erica_breeding_fetish_followup_label")
    erica_breeding_fetish_team_crisis = Action("Erica gets kicked off the track team", erica_breeding_fetish_team_crisis_requirement, "erica_breeding_fetish_team_crisis_label")
    erica_breeding_fetish_nora_followup = Action("Talk to Nora about Erica", erica_breeding_fetish_nora_followup_requirement, "erica_breeding_fetish_nora_followup_label")
    erica_breeding_nora_news_part_one = Action("Nora follow up text", erica_breeding_nora_news_part_one_requirement, "erica_breeding_nora_news_part_one_label")
    erica_breeding_nora_news_part_two = Action("Nora good news", erica_breeding_nora_news_part_two_requirement, "erica_breeding_nora_news_part_two_label")
    erica_breeding_fetish_team_rejoin = Action("Erica gets good news", erica_breeding_fetish_team_rejoin_requirement, "erica_breeding_fetish_team_rejoin_label")
    erica_discuss_morning_wakeup = Action("Discuss wakeup plans", erica_discuss_morning_wakeup_requirement, "erica_discuss_morning_wakeup_label",
        menu_tooltip = "Talk to Erica about whether she should wake you up in the morning after spending the night with Lily.")
    erica_pre_insta_love = Action("Erica blows you", erica_pre_insta_love_requirement, "erica_pre_insta_love_label")
    #erica_post_yoga_fuck = Action("Erica fucks you", erica_post_yoga_fuck_requirement, "erica_post_yoga_fuck_label")

    erica_role = Role(role_name ="College Athlete", actions =[erica_get_to_know , erica_phase_one, erica_phase_two, erica_protein_shake, erica_house_call, erica_money_problems_update, erica_discuss_morning_wakeup], hidden = True)


#*************Mandatory Crisis******************#
init 1 python:
    def add_erica_race_crisis(person):
        erica_race_crisis.args = [person]
        mc.business.add_mandatory_crisis(erica_race_crisis)
        return

    erica_race_crisis = Action("Charity Race", erica_race_crisis_requirement, "erica_race_crisis_label")

init 2 python:

    erica_lily_post_insta_morning_action = ActionMod("Erica wakes you up", erica_lily_post_insta_morning_requirement, "erica_lily_post_insta_morning_label",
        menu_tooltip = "Erica wakes you up after spending the night with Lily.", category = "Home", is_crisis = True, is_morning_crisis = True)

###Erica ACTION LABELS###
label erica_intro_label(the_person):
    "As you step into the gym, you glance back and forth, checking out some of the different girls."
    "The gym is a great place to get fit... and enjoy some eye candy at the same time."
    "You get ready to hop onto one of the machines, but one girl in particular stands out to you."
    $ the_person.draw_person()
    "Your eyes are drawn to her. It is clear she takes care of herself. Right now she is in between machines."
    "You decide to introduce yourself. You walk over to her and strike up a conversation."
    $ the_person.event_triggers_dict["erica_progress"] = 1
    mc.name "Hey, you are making short work of these machines."
    the_person "Yeah, I come here pretty often."
    mc.name "I can tell. Can you show me how to use this machine? I'm kind of new here."
    the_person "Sure! It's not too hard, but you need to make sure you set this..."
    $ the_person.draw_person(position = "standing_doggy")
    "You watch as she bends over and starts setting up some of the weights on the machine."
    "Damn she's got a nice ass."
    "You make sure to keep your eyes up when she starts to stand back up. Don't want to get caught ogling her..."
    $ the_person.draw_person()
    the_person "There, now it should be good to go!"
    mc.name "Thanks! That is really helpful. I'm [mc.name]."
    the_person "[the_person.fname]. Nice to meet you."
    $ the_person.set_title(the_person.name)
    $ the_person.set_possessive_title("Your gym girl")
    $ the_person.set_mc_title(mc.name)
    mc.name "Likewise. You come here often?"
    the_person "Yeah! You could say that. I'm actually on the state college track and field team!"
    "You aren't surprised, she certainly has the look of an athlete."
    "You talk with her for a while about sports. She has a healthy interest in just about all things physical."
    $ the_person.discover_opinion("sports")
    the_person "Well, I need to get going. It was nice talking with you, [the_person.mc_title]!"
    "[the_person.title] seems like an interesting person. You should keep an eye out for her at the gym in the future."
    return

label erica_get_to_know_label(the_person):
    if "erica_progress" not in the_person.event_triggers_dict:
        $ the_person.event_triggers_dict["erica_progress"] = 0
        call erica_intro_label(the_person) from _erica_recall_intro_if_skipped_somehow_01
        #Introduction scene#
    elif erica_protein_shake_is_unlocked() and not erica_is_looking_for_work() and the_person.love > 20:
        call erica_money_problems_label(the_person) from _erica_start_job_quest_01
    elif erica_get_progress() == 1:
        "You decide to ask [the_person.title] a bit more about her athletics."
        mc.name "I see you here a lot. Are you getting ready for a race?"
        the_person "Yeah! I'm getting ready for a big race soon, so I try to get in here before and after class each day."
        "Wow, going to college, and dedicated to sports. Sounds like she doesn't have much free time."
        mc.name "So, where does that leave you? Any time left over for a social life? Or a boyfriend?"
        the_person "Oh, with everything going on, there is no way I would have time for a boyfriend."
        "[the_person.title] starts to move to the next workout machine."
        the_person "So a relationship is not really an option for me right now, or a job for that matter."
        mc.name "Yeah, sounds like an intense schedule."
        if not erica_protein_shake_is_unlocked():
            the_person "It'd be nice to have a little extra money for some protein powder or something. Money is pretty tight!"
            "You think about it for a bit. You could offer to buy her a protein shake, they serve them here at the gym. That would be a good opportunity to slip some serum in..."
            mc.name "They have protein shakes here. Maybe I could grab you one? It'd be no trouble."
            #Charisma role to unlock the buy protein shake option#
            $ ran_num = renpy.random.randint(0,100)
            $ ran_num += (mc.charisma * 10)
            if ran_num > 50: #Base line 50:50 chance at charisma = 0. 100% chance at charisma = 5
                the_person "That... actually would be nice! You have to be careful accepting drinks from strangers, but you seem genuine enough."
                "You now have the option to buy [the_person.title] a protein shake at the gym."
                $ the_person.event_triggers_dict["erica_protein"] = 1
                $ erica.event_triggers_dict["protein_day"] = 0
            else:
                "[the_person.title] hesitates when you offer."
                the_person "I appreciate it, but I'll have to pass. It wouldn't feel right to take freebies like that..."
        else:
            the_person "I appreciate you buying me a protein shake now and then. I definitely feel the effects of them. I feel stronger... even sexier since you started doing that!"
        "[the_person.title] moves on to the free weights area of the gym."
        if mc.max_energy >= 110:
            the_person "I think I'm going to do some squats..."
            "[the_person.title] looks over at you. She gives you a quick appraisal."
            the_person "Hey, you look like you're fairly fit yourself. You should work out with me sometime."
            mc.name "That sounds like a good idea, actually."
            the_person "Yeah... you're kinda cute. It'd be nice to have a guy around for a bit. It's been a while since I uhh..."
            "You raise your eyebrow."
            the_person "I mean uhh, with school and track, I'm so busy. It'd be nice to spend some time in the company of the opposite sex for a while! Nothing wrong with that, right?"
            $ the_person.event_triggers_dict["erica_workout"] = 1
            "You should consider working out with [the_person.title] sometime. It sounds like she might appreciate some male company!"
        else:
            the_person "I think I'm going to do some squats..."
            "[the_person.title] looks over at you. She gives you a quick appraisal."
            the_person "Hey, have you ever thought about working out a bit more? It does wonders for your energy..."
            "You consider her statement for a moment."
            the_person "Anyway, I'm going to get back to my workout. I'll see you around [the_person.title]!"
            "If you want to get further with her, maybe you should work on increasing your energy!"

        #Had sex in the locker room#
    elif erica_get_progress() == 2:
        "You notice that [the_person.title] is really pushing herself hard today on the treadmill."
        mc.name "Hey [the_person.title]. You're really going at it! Have an event coming up?"
        "[the_person.title] slows the treadmill down so she can carry on a conversation."
        the_person "Yeah! I have a big 5k coming up. I really want to do well for this, with it coming up on track season!"
        "You chitchat with [the_person.title] for a bit about the upcoming race."
        if mc.max_energy >= 140:
            the_person "Hey, you seem pretty fit too. You should consider entering! It's for a great cause!"
            mc.name "Okay... I'll consider it. Things are pretty busy at work lately, but I'll get back to you if I have time."
            the_person "Just don't be sore about it when I beat you to the finish line. I'm a serious athlete!"
            mc.name "Oh, I see! Well, maybe we should make it a race! But what would the stakes be?"
            "[the_person.title] chuckles before responding. She gives you a quick wink."
            the_person "I'm sure we could come up with something... be careful though, don't bet anything you aren't willing to lose!"
        else:
            the_person "Hey, it has been nice chatting with you, but I need to get back to my workout!"
        "You say goodbye and head on your way."

        #You've challenged her to a race!#
    elif erica_get_progress() == 3:
        "You try to strike up a conversation with [the_person.title]."
        the_person "Hey now, no distractions! Your ass is mine on Saturday!"
        mc.name "Ha! We'll see about that!"


        #You've won the race#
    elif erica_get_progress() == 4:
        mc.name "Hey [the_person.title]."
        the_person "Hey, [the_person.mc_title]!"
        "You catch up with her for a bit with what she's been up to."
        the_person "Well, it was good to see you. We should work out again sometime, or... you haven't lost my address, have you?"
        mc.name "Of course not!"
        the_person "Then swing by some evening, it would be good to get a little time working out some tension!"
        "You tell her you'll look her up soon, say goodbye and head on your way."

    else:
        "Debug: How did you end up here???"

    # $ the_person.review_outfit()
    call advance_time from _call_advance_erica_get_to_know
    return

#CSA10
label erica_phase_one_label(the_person):
    if erica_get_progress() == 1:
        mc.name "Hey [the_person.title]. I figured I would find you here. Want to work out together?"
        "[the_person.title] is just hopping off the treadmill. You can tell she just finished getting warmed up."
        the_person "[the_person.mc_title]! Hey, I was wondering if you would take me up on my offer to work out sometime. That sounds great! I'm going to be doing free weights today."
        mc.name "Sounds good! I'll head to the locker room and get changed and meet you over by the free weights."
        "You quickly get yourself changed into workout clothes and meet [the_person.title]."
        the_person "This will be perfect! Today is strength day and with you around to spot me I can really push myself to the limit."
        $ the_person.draw_person( position = "stand4")
        "You begin a workout with [the_person.title]. You start it out with some basic free lifting, taking turns on the equipment. She strikes up a conversation as you work out."
        the_person "Alright, time for some curls. Thanks again for doing this. It's been nice having a guy around... a lot of times when I do workouts over here I have a lot of guys hitting on me..."
        "You nod in understanding."
        mc.name "Well, I can't say I blame them, you train hard, and it shows with how good your body looks!"
        "She chuckles."
        the_person "Thanks. Honestly, it's not that I don't like the attention, but with everything going on with me right now, I just don't have time for a relationship."
        the_person "You've been a good friend though."
        "You finish up your curls with [the_person.title]. You move on to the pull-up bar."
        $ the_person.draw_person( position = "stand3")
        "You start to do a few pull-ups."
        mc.name "So, I get that you don't have time for a relationship, but... how do you deal with your, you know, needs?"
        the_person "Well, I used to have a few friends from class that came with, well... benefits, I guess you could say."
        "You grunt as you exert yourself as you finish your set."
        the_person "The last few I've had have kind of fizzled though. The last one started getting too attached, wanting to move in with me, and the one before that graduated and moved out of state."
        the_person "So, I guess you could say I'm going through a bit of a dry spell right now."
        "You let go of the pull-up bar and she steps up to it."
        the_person "Hey, could you do me a favor? Could you pull me down a little bit while I do my reps, you know, to give a little resistance?"
        mc.name "Sure, I can do that."
        "[the_person.title] reaches up and grabs the pull-up bar. You put your hands on her hips and lightly push down, giving her some extra weight for her pull-ups."
        "As she begins to pull herself up, her hips, waist, and ass are in perfect position, right in front of your face. You check her out while she struggles through her reps."
        $ mc.change_locked_clarity(10)
        "[the_person.title]'s tight, thin body is undeniably sexy and athletic. Your hands on her hips gives you a naughty idea."
        mc.name "I stay busy with my business. I know that feeling, not having time for a relationship, but looking for some casual hookups."
        "[the_person.title] drops down off of the pull-up bar. You let your hands linger on her hips a little longer than necessary."
        the_person "Exactly! Why can't two adults just have casual sex once in a while?"
        mc.name "Friends with benefits can be great for meeting needs during busy times in your life."
        "[the_person.title] looks up at you when you finish your sentence. It quickly dawns on her that you are suggesting hooking up."
        the_person "Let's keep going, next up are squats."
        $ the_person.draw_person( position = "stand2")
        "[the_person.title] helps you add some weights to the squat bar. You decide to get a little bolder."
        mc.name "Add one more weight to the end there, I want to really push myself today."
        "She does as you ask, and you get in position under the bar."
        mc.name "Stay close, I've never done this much weight before."
        "As you get in position, you feel [the_person.title] get in position behind you to spot you. You can feel her a little closer than she needs to be though."
        "With a grunt, you begin your reps. The weight is tough, but you get through your reps without help. When you finish you slowly stand up and turn to her."
        $ the_person.draw_person( position = "stand4")
        $ mc.change_locked_clarity(20)
        if the_person.outfit.tits_available():
            "[the_person.title] has a little more color in her cheeks than she did a minute ago. You also notice her nipples are a little more prominent."
        else:
            "[the_person.title] has a little more color in her cheeks than she did a minute ago, and it looks like her nipples are poking out a little bit against the fabric containing them."
        "She must be getting a little bit excited!"
        mc.name "Alright, your turn."
        "You help her reset the weights to something appropriate for her. She gets in position and gets ready to do some squats, and you get behind her, ready to spot for her."
        "As she begins her reps, you get a little bit closer to her. As she stands up with each squat, her lower back starts to brush up against your crotch."
        mc.name "See? Two friends, helping each other out. I take a turn, then you take a turn..."
        "[the_person.title] grunts... or was that a groan? You lean forward just a bit farther. It is now obvious you are using the opportunity to put your body up against hers as she finishes her squats."
        "At the top of her last squat, she lingers a bit before she racks the weight. You feel an ever so slight wiggle of her hips up against you. She's getting turned on!"
        $ mc.change_locked_clarity(10)
        "She racks her weights with a groan, and you quickly retreat. Getting an erection here would be a bit embarrassing."
        the_person "Okay... let's finish with the bench press."
        "You head over to the bench and start racking some weights on it. You lay down on the bench while [the_person.title] stands by your head."
        "She looks around a bit, to see if anybody is watching you, before prompting you to begin."
        the_person "Ready? It's my turn now..."
        "As you lift the weight up over the bar and begin to bring it down to your chest, [the_person.title] slowly moves forward, maneuvering her legs until her crotch is right above your face."
        "You breathe deep. There is the normal gym smells of weights, rubber, and sweat, but also a smell that is distinctly, sweetly feminine."
        "You lift your head up for a second, making contact with her crotch with your face. She stifles a groan as you finish up your set."
        $ the_person.change_max_energy(5)
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(10)
        "[the_person.title] backs off and you quickly get up. She puts a hand on your shoulder and whispers in your ear."
        the_person "Do you want to fool around a little?"
        "You nod your head."
        the_person "There's a locker room here families can use with a lock on it. Meet me there in three minutes."
        $ the_person.draw_person( position = "walking_away")
        "You watch [the_person.title] walk off, fighting off an erection. Looks like you're about to hook up at the gym!"
        "After three minutes, you follow after [the_person.title]. When you find the family use room, you let yourself in."
        $ the_person.apply_outfit(Outfit("Nude"), update_taboo = True)
        $ the_person.draw_person( position = "stand2")
        $ mc.change_locked_clarity(20)
        "As you enter, you see that [the_person.title] is already naked."
        the_person "[the_person.mc_title], I'm so turned on. Can you finish what you started in the fitness area?"
        "She points to a bench sitting along the wall."
        "She looks nervous. You can tell she is just looking to fool around a bit."
        menu:
            "Service Her\n{color=#ff0000}{size=18}Increases Love{/size}{/color}":
                mc.name "I'd love to get a taste..."
                $ the_person.change_love(10)
                the_person "Wow, what a gentleman! Over here."
                "She leads you to the bench. You eagerly lie back on it. She climbs on top of you."
                $ the_person.draw_person(position = "kneeling1")
                "She slowly climbs up your body until her cunt is inches from your face."
                "You lean forward and run your tongue along her slit. She moans softly as soon as you make contact."
                the_person "Oh [the_person.mc_title]..."
                $ the_person.break_taboo("licking_pussy")
                call get_fucked(the_person, the_goal = "get off", private= True, start_position = cowgirl_cunnilingus, start_object = make_bench(), skip_intro = True, ignore_taboo = True, allow_continue = False) from _erica_first_oral_01
                the_person "Wow, I needed that so bad..."
                "For a bit she just sits on top of you, recovering. Soon, however, you feel her reach back and start to stroke your cock."
                the_person "Mmm, it wouldn't be fair for me be the only one getting some relief... I bet you taste good..."
                the_person "I want to taste you..."
                "She kisses you on the neck, then starts slowly working her way down your chest."
                "When she reaches your waist, she slowly undoes your pants, then pulls them down and off, revealing your erection."
                the_person "Oh [the_person.mc_title]..."
                "[the_person.possessive_title] looks down at your shaft for a moment, giving it a couple strokes. She leans forward and kisses the tip of your dick gingerly."
                "Her mouth opens and you feel the warm wetness of her gullet envelop your cock. It feels great as she starts to bob her head up and down on it."
                $ the_person.break_taboo("sucking_cock")
                call get_fucked(the_person, the_goal = "oral creampie", private= True, start_position = cowgirl_blowjob, start_object = make_bench(), skip_intro = True, ignore_taboo = True, allow_continue = False) from _erica_first_oral_02
                "You lie back and catch your breath as [the_person.title] gets up."
                $ the_person.draw_person()
                the_person "Mmm, that was really nice. I could get used to that."
                the_person "I'm gonna shower really quick. We should probably get out of here ASAP."
                mc.name "You're right. I'll join you."
                the_person "Okay, but no funny business."
                $ gym_shower.show_background()
                $ the_person.draw_person(position = "back_peek")
                "You join [the_person.title] in the shower. You splash around a bit and grab her ass once or twice, but go no further."
                $ the_person.apply_planned_outfit()
                $ the_person.draw_person()
                the_person "Alright, I'm gonna sneak out. Wait a couple minutes, then leave too, okay?"
                "You agree. [the_person.title] slips out of the room, leaving you alone with your thoughts."
                $ mc.location.show_background()
                $ clear_scene()
                "You know she is young, and not looking for anything serious, but you are really starting to take a liking to this girl."
                "Maybe with a bit more time, more serums, and some mind blowing sex, you can convince her to go steady with you."

            "Exchange Services\n{color=#ff0000}{size=18}Increases sluttiness{/size}{/color} (disabled)": #TODO FWB PATH
                pass
            "Force her to Service You\n{color=#ff0000}{size=18}Increases Obedience and sluttiness\nDecreases Love{/size}{/color} (disabled)": #TODO HATE FUCK PATH
                pass

        $ the_person.event_triggers_dict["erica_progress"] = 2

        # "You walk over to her and quickly strip. You grab [the_person.title] by that ass and pick her up. You carry her to the wall and pin her up against it."
        # $ the_person.draw_person( position = "against_wall")
        # "[the_person.possessive_title] is grinding her hips up against yours. The sweat from your workouts mingles together as you prepare yourself to enter her."
        #
        # $ the_person.add_situational_slut("horny", 20, "She is desperate to be fucked")
        #
        # # NOTE skip intro prevents taboo break from executing
        #
        # call condom_ask(the_person) from _erica_mod_condom_ask_CS010
        #
        # "As you begin to push yourself inside her, she drags her nails across your back."
        # $ the_person.break_taboo("vaginal_sex")
        # if not mc.condom:
        #      $ the_person.break_taboo("condomless_sex")
        # the_person "Oh fuck, that's good. Give it to me good, [the_person.mc_title]!"
        # call fuck_person(the_person, start_position = against_wall, start_object = make_wall(), skip_intro = True, skip_condom = True) from _call_casual_sex_mod_CS010
        # $ the_report = _return
        # if the_report.get("girl orgasms", 0) > 0:
        #     "As you slowly let [the_person.title] down from the wall, you can see her trembling, caused by aftershocks from her orgasm."
        #
        # the_person "Mmm... that was nice..."
        # "[the_person.title] stutters for a moment."
        # $ the_person.clear_situational_slut("horny")
        # the_person "But... you know... I really can't get involved in a serious relationship right now."
        # mc.name "I agree. We need some ground rules. Want to have coffee and figure it out?"
        # the_person "That sounds good. But it's not a date, okay? Just need to set boundaries."
        # "You agree. You and [the_person.title] take a quick shower, then get ready and leave the gym."
        #
        # $ the_person.apply_planned_outfit()
        #
        # "You head to a nearby coffee shop. You grab yourself a coffee, letting [the_person.title] pay for her own. You grab a seat at a booth away from any other people."
        # $ renpy.show("restaurant", what = restaraunt_background, layer = "master")
        # $ the_person.draw_person( position = "sitting")
        #
        # the_person "So... are you interested in a friends with benefits set up?"
        # "You give a quick nod."
        # the_person "Okay, so, some ground rules. First off, if either of us starts to catch feelings for the other person, we break it off. I sure as fuck don't have time for that stuff right now..."
        # mc.name "I agree. We'll keep it physical. No dates or whatever. Just hit me up when you want to fuck around."
        # the_person "Right... here, let's exchange numbers. I'll text you and if we're both free, we can screw around, no strings attached."
        # "You agree. You and [the_person.title] finish up with your coffees. You both get up to leave."
        # $ the_person.draw_person(position = "stand3")
        # the_person "Well, see you around, stud! I'd better go work on some homework."
        # "You say your goodbyes. This should be interesting. You wonder what kind of crazy sex you'll have with your new friends with benefits."
        #
        # $ the_person.event_triggers_dict["booty_call"] = True
        #
        # "You now have [the_person.title]'s phone number."
        # $ the_person.event_triggers_dict["erica_progress"] = 2

    elif erica_get_progress() > 1:
        mc.name "Hey [the_person.title]. I figured I would find you here. Want to work out together?"
        the_person "That sounds great, [the_person.mc_title]! I always enjoy working up a sweat with you."
        mc.name "Sounds good! I'll head to the locker room and get changed and meet you over by the free weights."
        "You quickly get yourself changed into workout clothes and meet [the_person.title]."
        $ the_person.draw_person( position = "stand4")
        "It is obvious from the beginning of your workout with [the_person.possessive_title] that she intends to get frisky with you when you're done."
        "While doing squats, she gets right behind you, pressing her body against yours as she spots you."
        $ mc.change_locked_clarity(10)
        "You try to be as covert as possible, but a couple of the other guys in the gym shoot you knowing looks as you go about your workout."
        "During the bench press, [the_person.title] stands right above you, her crotch tantalizingly close to your face."
        $ mc.change_locked_clarity(10)
        # $ the_person.change_max_energy(5)
        #TODO change dialogue based on path
        the_person "Wow, what a workout! So... are you gonna go hit the showers now?"
        "It is clear from the way she is asking she is curious if you are going to follow her to the secluded locker room."
        menu:
            "Hit the Shower":
                #TODO some kind of innuendo joke here#

                mc.name "Yeah, I'm pretty sweaty. I'd better get cleaned up!"
                $ the_person.draw_person( emotion = "happy")
                "She gets close to you and whispers in your ear."
                the_person "You know where to go... meet me in 5."
                $ the_person.draw_person( position = "walking_away")
                "You watch [the_person.title]'s amazing ass as she walks away. You swear there's a bit of a swagger there."
                "You give her a few minutes, then follow after her."

                #locker room sex scene.
                call erica_locker_room_label(the_person) from _erica_locker_room_transition_01



            "Not Today": #lol what a tease#
                the_person "Oh. Okay, I understand. Well, I'll see you around, [the_person.mc_title]!"
                $ the_person.change_happiness(-3)

    $ the_person.apply_planned_outfit()
    call advance_time from _call_advance_erica_workout
    return

label erica_locker_room_label(the_person): #TODO this will be Erica's sluttiness scaling event. As sluttiness increases, she does crazier stuff in the locker room.
    $ the_person.apply_outfit(Outfit("Nude"), update_taboo = True)
    $ the_person.draw_person( position = "stand2")
    "As you enter, you see that [the_person.title] is already naked."
    $ mc.change_locked_clarity(20)
    if erica_on_love_path():
        mc.name "Oh god, I'll never get tired of seeing your fit body naked."
        if mc.max_energy > 200:
            the_person "Me? You have the body of a god. Get those clothes off, mister."
            "As you start to undress, she runs her hands up and down your chiseled frame. She clearly enjoys your body."
            $ the_person.change_arousal(20)
        elif mc.max_energy > 160:
            the_person "You're pretty fit yourself there, mister. Why don't you get those clothes off?"
            "As you start to undress, she runs her hands up and down your chest. She enjoys your body."
            $ the_person.change_arousal(10)
        else:
            the_person "Mmm, save your flattery and get naked."
            "You undress and walk over to her."
        the_person "So... want to fool around some? If you want I'd be glad to take the lead..."
        menu:
            "Fuck her":
                "You step closer to her. You put your hands on her hips and pull her in."
                $ the_person.draw_person(position = "kissing")
                "You lean in and kiss [the_person.possessive_title] hungrily. Her hips are grinding against yours."
                $ the_person.change_arousal(10)
                $ mc.change_locked_clarity(10)
                $ the_person.add_situational_slut("horny", 10, "You take charge")
                $ the_person.add_situational_obedience("submissive", 20, "She submits to you")
                the_person "Mmm, I'm ready... do whatever you want, [the_person.mc_title]..."
                call fuck_person(the_person, private = True) from _erica_gets_fucked_by_her_man_in_lockerroom_01
            "Let her take the lead":
                mc.name "I'd like to see how you handle this thing."
                "You give your dick a stroke. She chuckles and leans forward."
                $ mc.change_locked_clarity(20)
                the_person "Don't worry, I know just what to do."
                $ the_person.add_situational_slut("horny", 10, "She takes the lead")
                $ the_person.add_situational_obedience("submissive", -20, "You submit to her")
                "She is excited to take the lead."
                call get_fucked(the_person, private= True) from _erica_pleases_her_man_in_lockerroom_01
        $ the_report = _return
        $ the_person.draw_person(position = "sitting")
        $ the_person.clear_situational_slut("horny")
        $ the_person.clear_situational_obedience("submissive")
        if the_report.get("girl orgasms", 0) > 0:
            "[the_person.title] sits down on the bench. You can see her trembling, feeling the aftershocks of her orgasm."
            the_person "Mmm... god I'm glad you know how to use that cock."
        else:
            "[the_person.title] sits down on the bench, catching her breath."
        "Without another word, you and [the_person.title] take a quick shower, then get ready and leave the gym."
        "You share a quick kiss before you part ways."
    elif erica_on_hate_path():
        pass

    else:
        if the_person.sluttiness > 50:
            the_person "[the_person.mc_title], give me that cock! It's been too long since you fucked me good!"
            "You walk over to her and quickly strip. You grab [the_person.title] by the ass and pick her up. You carry her to the wall and pin her up against it."
            $ the_person.draw_person( position = "against_wall")
            $ mc.change_locked_clarity(20)
            "[the_person.possessive_title] is grinding her hips up against yours. The sweat from your workouts mingles together as you prepare yourself to enter her."

            $ the_person.add_situational_slut("horny", 20, "She is desperate to be fucked")

            call condom_ask(the_person) from _erica_mod_condom_ask_CS011
            "As you begin to push yourself inside her, she drags her nails across your back."
            if not mc.condom:
                $ the_person.break_taboo("condomless_sex")
            the_person "Oh fuck, that's good. Give it to me good, [the_person.mc_title]!"
            call fuck_person(the_person, start_position = against_wall, start_object = make_wall(), skip_intro = True, skip_condom = True) from _call_casual_sex_mod_CS011
            $ the_report = _return
            if the_report.get("girl orgasms", 0) > 0:
                "As you slowly let [the_person.title] down from the wall, you can see her trembling, feeling the aftershocks of her orgasm."
                the_person "Mmm... god I'm glad you know how to use that cock."
            $ the_person.clear_situational_slut("horny")
            $ the_person.draw_person()
            "Without another word, you and [the_person.title] take a quick shower, then get ready and leave the gym."
        else:
            the_person "[the_person.mc_title], I really need to get off. Can you get naked please?"
            "You walk over to her and quickly strip. She runs her hands along your chest."
            the_person "I'm going to do what I want with you... don't worry, it will be good for both of us."
            "She is trying to push you back on to the bench. Do you want to let her take the lead?"
            menu:
                "Take Charge":
                    "You decide not to let her take charge. You stop and grab her wrists."
                    mc.name "I don't think so. I'm the man here. Lie down, I'll lick your pussy for a bit first."
                    $ mc.change_locked_clarity(20)
                    "She starts to protest, but quickly stops when she realizes you are going to eat her out."
                    $ the_person.change_stats(happiness = -3, obedience = 5)
                    $ the_person.add_situational_slut("horny", 10, "You take charge")
                    $ the_person.add_situational_obedience("submissive", 20, "She submits to you")
                    $ the_person.draw_person(position = "missionary")
                    call fuck_person(the_person, private = True, start_position = cunnilingus, start_object = make_bench()) from _erica_gets_fucked_by_her_man_in_lockerroom_02
                "Let her take the lead":
                    "You decide to let her take charge. She gently pushes you back onto the bench."
                    $ the_person.change_stats(happiness = 3, obedience = -5)
                    $ mc.change_locked_clarity(20)
                    the_person "Don't worry, I know just what to do."
                    $ the_person.add_situational_slut("horny", 10, "She takes the lead")
                    $ the_person.add_situational_obedience("submissive", -20, "You submit to her")
                    "She is excited to take the lead."
                    call get_fucked(the_person, private= True) from _erica_pleases_her_man_in_lockerroom_02

            $ the_report = _return
            $ the_person.clear_situational_slut("horny")
            $ the_person.clear_situational_obedience("submissive")
            $ the_person.draw_person(position = "sitting")
            if the_report.get("girl orgasms", 0) > 0:
                "[the_person.title] sits down on the bench. You can see her trembling, feeling the aftershocks of her orgasm."
                the_person "Mmm... god I'm glad you know how to make a girl cum so hard."
            else:
                "[the_person.title] sits down on the bench, catching her breath."
            "Without another word, you and [the_person.title] take a quick shower, then get ready and leave the gym."
    return

#CSA20
label erica_phase_two_label(the_person):
    if erica_get_progress() == 2:
        "You see [the_person.title] on the treadmill. She is running hard, and has been training for a race coming up soon. She pauses the treadmill as you walk up to her."
        the_person "Hey [the_person.mc_title], here for another workout?"
        mc.name "Not today, [the_person.title]. How goes training? Is that big race coming up soon?"
        if day % 7 == 4: #It is friday, the race is tomorrow!
            the_person "Yeah! As a matter of fact, it's tomorrow!"
        else:
            the_person "Yeah! It's coming up quick, on Saturday morning!"
        "She checks you out for a minute, before continuing."
        the_person "You know, it's a charity race, with proceeds going to breast cancer! You seem pretty fit, and I know how much you love tits. Maybe you should race too?"
        "You give her a smile."
        mc.name "Ah, that sounds like a good cause, but I couldn't. I'd hate for our arrangement to come to an end because we are in the same race and I beat you and you get mad."
        the_person "Hah! You wish! You seem awfully confident. I tell you what, why don't we make a little bet?"
        "You are intrigued by where she is going with this."
        mc.name "Go on."
        the_person "You come out and race. When the race is over, we go back to my place, and whoever won gets to do anything they want with the loser!"
        mc.name "Anything?"
        "She gives you a wink."
        the_person "That's what I said, isn't it?"
        mc.name "You've got a deal. Saturday morning downtown. I'll be there."
        $ the_person.draw_person (position = "stand4")
        the_person "Yes! Oh [the_person.mc_title], no backing out now! I'll have to find my handcuffs..."
        "[the_person.title] seems pretty confident in herself, but you are pretty sure you have good odds in a race."
        "You wave goodbye to [the_person.title], wondering what you've gotten yourself into."

        $ add_erica_race_crisis(the_person)
        "Things have been progressing well with [the_person.title], but soon, you might have to make a decision."
        "Is she someone you are interested in dating? Just a friend with benefits? Or do you want to turn her into a mindless fucktoy?"
        "You have a feeling the outcome of your bet could change your relationship with her."

        $ the_person.event_triggers_dict["erica_progress"] = 3
    elif erica_get_progress() == 3:
        mc.name "Hey [the_person.title], I just wanted to verify, the race is this Saturday, right?"
        the_person "That's right! I can't wait to beat your ass in the race, and then spank it again later at my place!"
        mc.name "Yeah right, I'll be bending you over before you can even get your front door closed."
        "[the_person.title] has a spark in her eyes. Whoever wins, you have a feeling the sex is going to be amazing after the race."
        "You wave goodbye to [the_person.title], wondering what you've gotten yourself into."

    $ the_person.apply_planned_outfit()
    call advance_time from _call_advance_erica_race_challenge
    return

#CSA30
label erica_race_crisis_label(the_person):
    $ scene_manager = Scene()
    $ yoga_assistant = erica_get_yoga_assistant()
    "It's race day! You make your way downtown, ready for your race with [the_person.title]."
    $ mc.change_location(downtown)
    $ mc.location.show_background()
    "You find where they are organizing the race. It is a 5 kilometer race, which is about three miles long."
    "You look around and eventually find [the_person.title]."
    $ the_person.apply_gym_outfit()
    $ the_person.draw_person(position = "stand3")
    $ scene_manager.add_actor(the_person)
    the_person "Hey, there you are! I was starting to think you had chickened out!"
    mc.name "Not a chance. I hope you don't have any plans for tomorrow, because when I get done with you tonight you won't be able to get out of bed until Monday at least!"
    the_person "Oh my, brave words for a brave boy! Let's just see what happens!"
    if erica_get_is_doing_yoga_sessions() and erica_get_is_doing_insta_sessions():
        "As you are trash-talking each other, [lily.title] and [yoga_assistant.title] surprise you when they walk up."
        $ scene_manager.add_actor(lily, display_transform = character_left)
        $ scene_manager.add_actor(yoga_assistant, display_transform = character_center)
        lily "Wow bro, you're running in a charity race? And I had to hear about it from [the_person.fname]?"
        yoga_assistant "I know right? And for breast cancer research? I don't run much, but I probably would've signed up if I'd known about it earlier!"
        the_person "Ah! Thanks for coming out!"
        "Caught by surprise, you can't think of anything to say, so you let the girls chat."
        yoga_assistant "Wouldn't miss it!"
        lily "You should have told mom, [lily.mc_title]. I bet she would have come out to help cheer you on too!"
        mc.name "Sorry. Honestly, this is the first time I've ever done something like this. I didn't realize it was normal for people to come watch."
        yoga_assistant "Maybe next time they do one of these races, we could do some kind of corporate sponsorship?"
        "You chat with the girls, but soon it is about time for the race to begin."
        yoga_assistant "We're gonna find a place to go cheer you on. Good luck you two!"
        $ scene_manager.hide_actor(lily)
        $ scene_manager.hide_actor(yoga_assistant)
    elif erica_get_is_doing_yoga_sessions():
        "As you are trash-talking each other, [yoga_assistant.title] surprises you when she walks up."
        $ scene_manager.add_actor(yoga_assistant, display_transform = character_center)
        yoga_assistant "Wow, a charity race? This is great!"
        the_person "Ah! Thanks for coming out!"
        yoga_assistant "Of course! I'm surprised to you see you here, [yoga_assistant.mc_title]! I'm glad you're doing your part for breast cancer research though!"
        mc.name "Yeah, this is my first time doing something like this."
        yoga_assistant "Well, I think it's great. Maybe next time they do one of these races, we could do some kind of corporate sponsorship?"
        "You chat with the girls, but soon it is about time for the race to begin."
        yoga_assistant "I'm gonna find a place to go cheer you on. Good luck you two!"
        $ scene_manager.hide_actor(yoga_assistant)
    elif erica_get_is_doing_insta_sessions():
        "As you are trash-talking each other, [lily.title] surprises you when she walks up."
        $ scene_manager.add_actor(lily, display_transform = character_center)
        lily "Wow, so it is true? My brother is running a charity race? And I had to hear it from [the_person.fname]."
        the_person "Ah! Thanks for coming out!"
        lily "I wouldn't miss it! This is going to be so exciting, watching you whip [lily.mc_title] in the race!"
        "You start to defend yourself, but [the_person.possessive_title] jumps in first."
        the_person "It's all for a good cause. It's not about winning or losing!"
        "She gives you a quick wink. Yeah right, it's not about winning! You have a prize to claim!"
        lily "You should have told mom, [lily.mc_title]. I bet she would have come out to help cheer you on too!"
        mc.name "Sorry. Honestly, this is the first time I've ever done something like this. I didn't realize it was normal for people to come watch."
        "You chat with the girls, but soon it is about time for the race to begin."
        $ scene_manager.hide_actor(lily)
    "You and [the_person.title] do some stretches and warmups, but soon it is time for the race to begin."
    "You line up together at the starting line, ready for the race to begin."
    "*BANG*"
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "The official starts the race with a shot from the gun and the race begins! [the_person.title] jumps out in front of you, setting a fast pace."
    "You are tempted to chase after her, but think better of it. This is a long race, and you need to pace yourself."
    $ scene_manager.hide_actor(the_person)
    "As you near the first kilometer, you lose sight of [the_person.title] in the crowd of racers, but you are sure you aren't far behind."
    "You settle into your pace, determined to let your energy carry you through the race, no matter what happens. You pass the second kilometer marker."
    if erica_get_is_doing_yoga_sessions() and erica_get_is_doing_insta_sessions():
        $ scene_manager.show_actor(lily)
        $ scene_manager.show_actor(yoga_assistant)
        "[lily.title] and [yoga_assistant.possessive_title] are standing next to the course, and they begin cheering when they see you."
        yoga_assistant "Go [yoga_assistant.mc_title]!"
        lily "She's just barely ahead, you can do it!"
        $ scene_manager.hide_actor(lily)
        $ scene_manager.hide_actor(yoga_assistant)
        "You pass the girls and keep running."
    elif erica_get_is_doing_yoga_sessions():
        $ scene_manager.show_actor(yoga_assistant)
        "[yoga_assistant.possessive_title] is standing next to the course, and begins cheering when she sees you."
        yoga_assistant "Go [yoga_assistant.mc_title]! She's just ahead of you, you can do it!"
        $ scene_manager.hide_actor(yoga_assistant)
        "You pass by her and keep running."
    elif erica_get_is_doing_insta_sessions():
        $ scene_manager.show_actor(lily)
        "[lily.possessive_title] is standing next to the course, and begins cheering when she sees you."
        lily "You can do it bro! Keep going!"
        $ scene_manager.hide_actor(lily)
        "You pass by her and keep running."
    "You breathe in, you breathe out. You take pace after pace, determined to race with the best of your abilities."
    "As you approach the third kilometer marker, you can see yourself catching up to a familiar form."
    $ scene_manager.show_actor(the_person, position = "walking_away")
    $ mc.change_locked_clarity(10)
    "God she is hot, her ass swaying back and forth with each step she takes. You imagine all the things you want to do with those delightfully tight cheeks."
    "You are breathing hard. It's getting so hard to keep up. She starts to pull away from you."
    "No! It's time to dig deep! You pump your arms and breathe."
    "After a few moments, you catch your second wind. You get a burst of energy and run faster."
    "You are catching up to her, and you find yourself running with a renewed vigor from the flow of testosterone in your bloodstream, daydreaming about [the_person.possessive_title]."
    "You pass the marker for the fourth kilometer. This is it, it's now or never!"
    "You surge forward, and soon you are right beside her. She is gasping for air, she is completely winded!"
    the_person "[the_person.mc_title]? Oh god..."
    "She barely gets her words out as you pass her."
    $ scene_manager.hide_actor(the_person)
    "You keep pushing forward, not daring to turn around."
    "You round a corner. The finish line! You give it everything you have! Your breathing is heavy and ragged, sucking in every ounce of air you can."
    "You cross the finish line. You beat her!"
    "You are catching your breath, and turn to see her cross the finish line just a few seconds behind you."
    $ scene_manager.show_actor(the_person, position = "standing_doggy")
    "[the_person.title] is breathing hard. She walks up to a table nearby and bends over with her hands on it, trying desperately to catch her breath."
    $ mc.change_locked_clarity(10)
    "You walk up behind her and put your hands on her back. You are careful not to be too obvious, but you make some contact with her backside with your hips."
    mc.name "Hey there, [the_person.title]! Nice race! I'm so glad you invited me out here to support such a charitable cause..."
    $ scene_manager.update_actor(the_person, position = "stand4")
    "She stands up and turns to face you."
    the_person "Yeah!... I mean, it's all for a good cause, right?"
    $ the_person.change_max_energy(10)
    #$ the_person.draw_person(position = "stand4", emotion = "happy")
    "You think you see a little smirk on the corner of her mouth."

    if erica_get_is_doing_yoga_sessions() and erica_get_is_doing_insta_sessions():
        "[lily.title] and [yoga_assistant.title] walk up as you are catching your breath."
        $ scene_manager.show_actor(lily)
        $ scene_manager.show_actor(yoga_assistant)
        yoga_assistant "Wow! What a finish! That was amazing! And you won, [yoga_assistant.mc_title]!"
        lily "But don't get a big head. She probably let you win!"
        "[the_person.possessive_title] is still catching her breath so she doesn't have a response yet."
        mc.name "Maybe so. Maybe she wanted me to win all along? That's definitely a possibility."
        the_person "No no... I gave it my all..."
        yoga_assistant "Well it was a great race, thank you so much for inviting us!"
        the_person "Do you want to... go get some coffee?"
        "You aren't sure if she's just being polite, or if she's putting off paying up from the bet."
        yoga_assistant "Unfortunately, I have other commitments."
        lily "Same here, I'm going to meet up with a classmate to do some studying."
        the_person "Ah, okay. Well, thanks for coming!"
        "The girls say goodbye, leaving you with [the_person.possessive_title]."
        $ scene_manager.remove_actor(lily)
        $ scene_manager.remove_actor(yoga_assistant)
        $ del yoga_assistant
    elif erica_get_is_doing_yoga_sessions():
        "[yoga_assistant.title] walks up as you are catching your breath."
        $ scene_manager.show_actor(yoga_assistant)
        yoga_assistant "Wow! What a finish! That was amazing! And you won, [yoga_assistant.mc_title]!"
        mc.name "Thank you! I'm not sure though, I think maybe [the_person.title] let me win on purpose..."
        the_person "No no... I gave it my all..."
        yoga_assistant "Well it was a great race, thank you so much for inviting me!"
        the_person "Do you want to... go get some coffee?"
        "You aren't sure if she's just being polite, or if she's putting off paying up from the bet."
        yoga_assistant "Unfortunately, I have other commitments."
        the_person "Ah, okay. Well, thanks for coming!"
        "She says goodbye, leaving you with [the_person.possessive_title]."
        $ scene_manager.remove_actor(yoga_assistant)
        $ del yoga_assistant
    elif erica_get_is_doing_insta_sessions():
        "[lily.title] walks up as you are catching your breath."
        $ scene_manager.show_actor(lily)
        lily "Wow, can't say I saw that coming! It was a great race, but you won, [lily.mc_title]."
        mc.name "Thank you! I'm not sure though, I think maybe [the_person.title] let me win on purpose..."
        the_person "No no... I gave it my all..."
        lily "Well it was a great race, thank you so much for inviting me!"
        the_person "Do you want to... go get some coffee?"
        "You aren't sure if she's just being polite, or if she's putting off paying up from the bet."
        lily "Unfortunately, I have other commitments."
        the_person "Ah, okay. Well, thanks for coming!"
        "She says goodbye, leaving you with [the_person.possessive_title]."
        $ scene_manager.remove_actor(lily)

    "You both take a few minutes to recover, and soon you are ready to go."
    the_person "Alright, you won the race. I guess it's time to head back to my place?"
    $ scene_manager.clear_scene(reset_actor = False)
    $ the_person.learn_home()
    "You call for an Uber and she gives you her address. Soon you are walking into [the_person.title]'s apartment."
    $ mc.change_location(the_person.home)
    $ mc.location.show_background()
    "Your mind is racing. She is going to be completely at your mercy. It's now or never, time to make a decision on which direction you want to take things."
    "You walk in the door. What do you want to do? WARNING: This decision is permanent."
    menu:
        # "Take her ass \n{color=#ff0000}{size=18}Corruption path \n Not yet written{/size}{/color} (disabled)":
        #     "This path is not yet written"
        #     pass
        "Fuck her rough \n{color=#ff0000}{size=18}FWB path{/size}{/color}":
            "You decide not to push her for anything serious. She is busy with her athletics, and she's mentioned she doesn't really have time for anything anyway."
            "Your mind is made up. There's nothing wrong with having a friend with benefits!"
            call erica_post_race_fwb_label(the_person) from _erica_fwb_decision_post_race_1
        "Make love \n{color=#ff0000}{size=18}Girlfriend path{/size}{/color}":
            "You watch [the_person.possessive_title] as she walks into her apartment. She is so sexy and fun, you find yourself wanting to spend all your free time with her."
            "You make up your mind. You know she's mentioned she doesn't really have time for something serious right now... but maybe you could find a way to work around that?"
            "You can be patient. And for a girl like [the_person.title], you feel like it might be worth it."
            "Your mind is made up. You are going to ask her out. But first, you need to take advantage of your current situation..."
            call erica_post_race_love_label(the_person) from _erica_love_decision_post_race_1

    return

label erica_post_race_corruption_label(the_person):
    pass
    return

label erica_post_race_fwb_label(the_person):
    $ the_person.change_to_hallway()
    "As soon as you walk in the door, you grab [the_person.title]. You pick her up and push her against the wall."
    $ the_person.draw_person(position = "against_wall")
    $ the_person.add_situational_slut("Lost Bet",25,"Be ready for anything!")
    $ mc.change_locked_clarity(20)
    the_person "Fuck! Mmm, are we gonna start right here? I remember the terms, do what you want to with me..."
    "You growl into her neck as you grind your hips into hers."
    mc.name "That's right, you're my sexy bitch for the day."
    "You back up from the wall, but hold her tight, keeping her feet from reaching the floor. You turn and take her into her bedroom."
    $ the_person.change_to_bedroom()
    $ the_person.draw_person(position = "missionary")
    "You throw her down on her bed."
    if the_person.outfit.vagina_available() and the_person.outfit.tits_available():
        "You stop for a second and admire [the_person.title], her body on display in front of you."
        $ the_person.change_arousal(20)
        "You notice some moisture building around her slit. She is definitely enjoying your hungry eyes roaming her body."
    else:
        "Your mind red with lust, you begin to rip [the_person.title]'s clothes off."

        $ the_person.strip_outfit(position = "missionary")
        $ the_person.change_arousal(20)

        "[the_person.possessive_title] moans as you strip her down, enjoying your rough treatment of her."
    "When she is fully naked, you grab her hips and flip her over."
    $ the_person.draw_person(position = "doggy")
    $ the_person.change_arousal(5)
    $ mc.change_locked_clarity(10)
    "There it is, the ass that inspired your final push in the race. She lowers her face to the bed and wiggles her hips at you."
    "In a moment you are naked. You hop up on the bed and get behind her. You grab her hips and roughly pull her back toward you."
    "You rub her slit up and down with your furious erection, coating it with her juices. You give her ass a rough spank, eliciting a yelp."
    $ the_person.change_arousal(10)
    the_person "Oh fuck, please just put it in. I feel like I'm on fire!"
    "You consider for a second putting on a condom first. Nope, not a fucking chance. In one smooth motion you push yourself into her sopping, needy cunt."
    $ mc.change_locked_clarity(20)
    the_person "Yes! Oh god, please fuck me good!"
    "You have every intention of doing exactly that."
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    call fuck_person(the_person, private=True, start_position = doggy, start_object = make_bed(), skip_intro = True, skip_condom = True) from _call_casual_sex_mod_CS030
    $ the_report = _return

    $ the_person.clear_situational_slut("Lost Bet")
    "When you finish with her, [the_person.possessive_title] lies down on her bed."
    $ the_person.draw_person(position = "missionary")
    if the_report.get("girl orgasms", 0) > 0:
        the_person "[the_person.mc_title]... I am so sore... My legs from the race... and... you know..."
        the_person "But that was amazing... Look, I'll be your sexy bitch anytime you want, okay? You have my address now, feel free to stop by. Just promise you'll fuck me like that again."
        "You laugh."
    else:
        the_person "This was really great... Look, I'll be your sexy bitch anytime you want, okay? You know where I live now, so stop by anytime you feel like it."

    mc.name "Sounds good. You have my number, let me know if you wanna hook up sometime, or if you want a rematch!"
    the_person "Ayup! Don't worry. If it's all the same to you, I think I'm gonna take a nap now..."
    "You excuse yourself. You grab your clothes and head out. You now know [the_person.title]'s address, with a standing offer to come over and fuck her silly!"
    $ the_person.event_triggers_dict["erica_progress"] = 4
    $ perk_system.add_stat_perk(Stat_Perk(description = "Training for the big race has helped improve your energy level. +20 max energy, +40 energy cap.", energy_bonus = 20, bonus_is_temp = False, energy_cap = 40), "Athlete Energy Bonus")
    $ perk_system.add_ability_perk(Ability_Perk(description = "You take a few deep breaths and recover a bit of your energy. Use this perk to regain half your max energy, once per day.", toggle = False, usable = True, usable_func = second_wind_func, usable_cd = 1), "Second Wind")
    "You walk away with a spring in your step. You feel like training for and running the race has given you more energy."
    "You have gained the Second Wind ability perk. You can now recover half your max energy, once per day!"
    $ erica.event_triggers_dict["fwb_path"] = True
    return

label erica_post_race_love_label(the_person):
    $ the_person.change_to_hallway()
    "As soon as you walk in the door, you grab [the_person.title]. You pick her up and push her against the wall."
    $ the_person.draw_person(position = "against_wall")
    $ the_person.add_situational_slut("Lost Bet",25,"Be ready for anything!")
    $ mc.change_locked_clarity(20)
    the_person "Fuck! Mmm, are we gonna start right here? I remember the terms, do what you want to with me..."
    "You whisper into her ear as you grind your hips into hers."
    mc.name "That's right, you're mine for the day!"
    "You back up from the wall, but hold her tight, keeping her feet from reaching the floor. You turn and take her into her bedroom."
    $ the_person.change_to_bedroom()
    $ the_person.draw_person(position = "missionary")
    "You throw her down on her bed."
    if the_person.outfit.vagina_available() and the_person.outfit.tits_available():
        "You stop for a second and admire [the_person.title], her tight body on display in front of you."
        $ the_person.change_arousal(20)
        "You notice some moisture building around her slit. She is definitely enjoying your hungry eyes roaming her body."
    else:
        "Your mind red with lust, you begin to rip [the_person.title]'s clothes off."

        $ the_person.strip_outfit(position = "missionary")
        $ the_person.change_arousal(20)

        "[the_person.possessive_title] moans as you strip her down, enjoying your rough treatment of her."
    "When she is fully naked, you get on top of her."
    $ the_person.change_arousal(5)
    $ mc.change_locked_clarity(20)
    the_person "Mmm, you can do anything you want with me, and you go for missionary?"
    mc.name "I thought you were mine for the whole day?"
    the_person "Fair enough."
    mc.name "Besides, I want to be able to look you in the eyes the first time I make love to you."
    "She gives you a cheesy grin."
    $ the_person.change_love(3)
    the_person "Getting sentimental on me? Look... we can talk about stuff later... right now I just need you inside me."
    "She reaches down and takes hold of your cock. She points it at her entrance. Her legs wrap around you as she tries to pull you into her."
    mc.name "So needy, are you? Don't worry, I think we can both get what we want."
    $ mc.change_locked_clarity(30)
    "You relax your arms and legs, letting her pull you in. Your cock sinks into her steaming cunt raw."
    the_person "Oh! Yes, that feels so good..."
    "You moan in appreciation. Her eyes are staring into yours as you bottom out inside of her."
    mc.name "Alright [the_person.title]. I didn't take it easy on you at the race, and I'm not about to go easy on you now!"
    the_person "Mmmm, prove it!"
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    call fuck_person(the_person, private=True, start_position = missionary, start_object = make_bed(), skip_intro = True, skip_condom = True) from _call_casual_sex_mod_CS031
    $ the_report = _return
    "When you finish with her, [the_person.possessive_title] lies down on her bed."
    $ the_person.draw_person(position = "missionary")
    if the_report.get("girl orgasms", 0) > 0:
        the_person "[the_person.mc_title]... I am so sore... My legs from the race... and... you know..."
        mc.name "Mmm, yeah that was nice. I can't wait to do that again."
        the_person "Me too."
    else:
        the_person "This was really great... I can't wait to do that again."

    "You lay down next to her, just enjoying the heat of your bodies together. You want to experience this again and again with her."
    "You work up the courage to ask her out."
    mc.name "Look... I know you are busy with school and your athletics. But I love spending time with you, whenever you have free time..."
    the_person "Ohh [the_person.mc_title]..."
    mc.name "I'm not asking you to change anything about your life, I'm just asking to be a part of it."
    "She looks at you, thinking for a bit. Then cracks a grin."
    the_person "You're very charming, you know that? Before I met you, I was pretty sure I was going to just stay single through my college life..."
    the_person "But after getting to know you, I feel the same. I'm going to keep doing what I'm doing, but I want to spend my free time getting to know you better."
    mc.name "So... can I introduce you as my girlfriend?"
    the_person "Yeah... I'm not sure if this is going to work out, but I want to give it a try!"
    $ the_person.add_role(girlfriend_role)
    $ erica.event_triggers_dict["love_path"] = True
    "You roll over back on top of her and start to kiss her neck."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(20)
    the_person "Mmm, you're so fit too... I hope you're thinking what I'm thinking..."
    mc.name "It is definitely time for round two."
    "You feel yourself get a second wind as you start to play with [the_person.possessive_title]. You can see her do the same."
    $ second_wind_func()
    $ the_person.energy = the_person.max_energy
    the_person "Oh god you get me so hot... hang on."
    "She pushes you off her for a second. She turns over and gets on her hands and knees, pointing her ass at you."
    $ the_person.draw_person(position = "doggy")
    $ mc.change_locked_clarity(30)
    the_person "I want it like this... please! Please take me!"
    $ the_person.change_arousal(15)
    $ the_person.discover_opinion("doggy style sex")
    "Mmm, seems she likes it doggy style... and maybe has a bit of a submissive streak? You aren't sure about the latter yet, but you look forward to finding out."
    call fuck_person(the_person, private=True, start_position = doggy, start_object = make_bed(), skip_intro = True) from _call_casual_sex_mod_CS033
    $ the_report = _return
    "When you finish you are both spent."
    if the_report.get("girl orgasms", 0) > 0:
        the_person "Wow, I didn't think you could do that to me again."

    the_person "That was amazing... but I need to study, I've got a test on Monday. I love spending time with you, but you ARE a bit distracting..."
    mc.name "I understand. Tell you what, I'll head out, but before I go I'll order some lunch to get delivered, that way you can study without having to worry about making food."
    $ the_person.change_love(5)
    $ the_person.draw_person(position = "kissing")
    the_person "Aww, you don't have to do that. You are such a sweetheart."
    $ clear_scene()
    "While [the_person.possessive_title] gets cleaned up, you order her a healthy lunch on your phone. You know she is a college student, so she probably doesn't have much disposable income."
    $ the_person.apply_outfit()
    $ the_person.draw_person()
    $ mc.business.change_funds(-10)
    $ title_choice = get_random_from_list(["BBQ rainbow beef salad", "fresh salmon and Thai noodle salad", "spicy chicken and avocado wrap"])
    mc.name "Alright, I got you a [title_choice], it should be here soon. Good luck with your studying!"
    the_person "Goodbye [the_person.mc_title]. I'll see you soon! And you know where I live now. Feel free to swing by once in a while..."
    $ clear_scene()
    $ downtown.show_background()
    "You let yourself out and start to walk away. Wow, what an amazing day! You've managed to convince [the_person.title] to go out with you."
    "You can't wait to explore her tight little body more... but one thing at a time now."
    $ the_person.clear_situational_slut("Lost Bet")
    $ the_person.event_triggers_dict["erica_progress"] = 4
    $ perk_system.add_stat_perk(Stat_Perk(description = "Training for the big race has helped improve your energy level. +20 max energy, +40 energy cap.", energy_bonus = 20, bonus_is_temp = False, energy_cap = 40), "Athlete Energy Bonus")
    $ perk_system.add_ability_perk(Ability_Perk(description = "You take a few deep breaths and recover a bit of your energy. Use this perk to regain half your max energy, once per day.", toggle = False, usable = True, usable_func = second_wind_func, usable_cd = 1), "Second Wind")
    "You walk away with a spring in your step. You feel like training for and running the race has given you more energy."
    "You have gained the Second Wind ability perk. You can now recover half your max energy, once per day!"
    #call advance_time from _call_advance_erica_love_decision_01
    return

label erica_buy_protein_shake_label(the_person):
    if the_person.is_pregnant() and not the_person.knows_pregnant() and time_of_day == 1: #She has morning sickness
        mc.name "Care for a protein shake today, [the_person.title]?"
        the_person "Oh... actually no. I'm not sure why, but I've been feeling nauseated all morning... sorry!"
        return
    if erica_on_love_path():
        mc.name "Hey [the_person.title], looking good! Can I get you a protein shake babe?"
        "[the_person.possessive_title] looks at you and smiles wide."
        the_person "Oh! Hey [the_person.mc_title], that would be great! I skipped the protein this morning..."
        "She lowers her voice."
        the_person "Maybe we should work out together... and you could give me another shot of protein when we get done..."
        mc.name "Mmm, that's a tempting offer. Let me get you set up with this for now though."
    elif erica_on_fwb_path():
        mc.name "Hey [the_person.title]. I see you're working hard today, can I get you the usual?"
        the_person "Hey! That sounds great! I need all the protein I can get."
        "She lowers her voice."
        the_person  "Especially from you... up for a workout today? And... you know..."
        mc.name "Mmm, that's a tempting offer. Let me get you set up with this for now though."
    elif erica_on_hate_path():
        mc.name "Damn, work it [the_person.title]. I'll go get you a protein shake."
        "She gives you a wary eye. At this point, she is probably beginning to suspect you are messing with the shakes, but she knows better than to refuse."
        the_person "I guess that would be okay."
        mc.name "Good girl. I'll be right back."
    else:
        mc.name "Hey [the_person.fname], I see you're working pretty hard today! Can I get you a protein shake?"
        "[the_person.possessive_title] looks at you and smiles."
        the_person "That sounds great!"
    $ clear_scene()

    "You head over to the counter where they have the supplements. You order her a protein shake."
    $ mc.business.change_funds(-5)
    $ erica.event_triggers_dict["protein_day"] = day
    "Before you take it back to her, you have a moment with no one around. You can add a serum to it if you do it quickly!"
    menu:
        "Add a dose of serum to [the_person.title]'s shake" if mc.inventory.get_any_serum_count() > 0:
            call give_serum(the_person) from _call_give_serum_erica
            "You mix the serum into [the_person.title]'s protein shake. You take it over to her."

        "Add a dose of serum to [the_person.title]'s shake\n{color=#ff0000}{size=18}Requires: Serum{/size}{/color} (disabled)" if mc.inventory.get_any_serum_count() == 0:
            pass

        "Leave her drink alone":
            "You decide not to test a dose of serum out on [the_person.title] and take the shake back to her."

    if erica_on_love_path():
        $ the_person.draw_person(emotion = "happy")
        the_person "Thanks! I really appreciate this. Anything else I can do for you?"
    elif erica_on_fwb_path():
        $ the_person.draw_person(emotion = "happy")
        the_person "Thanks! So... you ready to work out?"
    elif erica_on_hate_path():
        "She takes the shake warily. She hesitates to take a sip."
        mc.name "Go on now. Don't worry, it's good for you."
        $ the_person.change_stats(love = -2, obedience = 3)
        "She starts to drink it. She waits to see if you need anything else."
    else:
        $ the_person.draw_person(emotion = "happy")
        the_person "I appreciate this. Anything else you wanted to talk about?"
    return

#CSA40
label erica_house_call_label(the_person):
    mc.name "Don't worry, I'm not here for business. I'm here for pleasure!"
    $ the_person.draw_person( position = "against_wall")
    "You reach around with both hands and grab her ass. You roughly pick her up, holding her tightly against you."
    $ mc.change_locked_clarity(20)
    the_person "Oh! Yes, I was hoping that's why you were here..."
    "[the_person.possessive_title] wraps her legs around you and you begin to grind your hips together. Heat is quickly building between the two of you."
    "You carry her to her bedroom. The whole way there she is kissing and nipping at your neck and earlobe."
    $ the_person.change_to_bedroom()
    $ the_person.draw_person(position = "missionary")
    "You throw her down on her bed."
    if the_person.outfit.vagina_available() and the_person.outfit.tits_available():
        "You stop for a second and admire [the_person.title], her body on display in front of you."
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(20)
        "You notice some moisture building around her slit. She is definitely enjoying your hungry eyes roaming her body."
    else:
        "Your mind red with lust, you begin to rip [the_person.title]'s clothes off."

        $ the_person.strip_outfit(position = "missionary")
        $ the_person.change_arousal(20)

        $ mc.change_locked_clarity(20)
        "[the_person.possessive_title] moans as you strip her down, enjoying your rough treatment of her."
    call fuck_person(the_person) from _call_casual_sex_mod_CSA040
    $ the_report = _return
    "After you finish with her, you get up and start to gather your clothes."
    if the_report.get("girl orgasms", 0) > 0:
        "[the_person.possessive_title] is in an orgasm-fueled daze, enjoying the effects it has on her."
        call check_date_trance(the_person) from _call_check_date_trance_erica_house_call
    the_person "Thanks for stopping by... I think I'm just gonna lie down for a bit..."
    $ the_person.draw_person(position = "missionary")
    "Once you finish getting dressed, you say goodbye and let yourself out. You head home and fall into bed, too tired to do anything else."

    $ mc.change_location(bedroom) # go home
    call advance_time from _call_advance_erica_house_call
    return

label erica_money_problems_label(the_person):
    mc.name "Hey, [the_person.title]. How've you been lately?"
    the_person "I'm doing okay, I guess."
    "Her uncertain response leaves you curious."
    mc.name "You guess?"
    the_person "Yeah... Can I vent to you about something though?"
    mc.name "Certainly."
    the_person "I'm trying to find a part-time job... One that will work with me and my school schedule, you know? I've got rent for a bit longer... But I need to find something soon."
    "She takes a deep breath before she continues."
    the_person "Normally you can get student loans to help with university costs, but my father recently decided not to assist me anymore. The amount you can get assumes your parents chip in a certain amount..."
    mc.name "I'm sorry to hear that. Why won't he support you anymore?"
    the_person "Well, he thinks I shouldn't be wasting my time on sports... He thinks I should dedicate myself to my studies full time."
    the_person "I told him I loved track though, and I refused to drop out of it... So he said he wasn't going to support me financially anymore."
    mc.name "Ah. I'm sorry to hear that."
    "She looks down at the ground. It's tough being a university student. You were lucky that you could live at home while going through it."
    the_person "Hey... I hate to ask, but... You wouldn't happen to have something part-time open... Would you?"
    "You consider her question for a bit. Unfortunately, all of your openings are for full time positions, and you can't think of anything you could have her do."
    mc.name "I'm sorry, I don't have anything at this time."
    the_person "It's okay, I figured as much..."
    "You continue some small talk with [the_person.title], but you keep trying to think about something you could have her do."
    if mc.business.hr_director:
        "Maybe you could check with [mc.business.hr_director.title] and see if she has any ideas?"
        $ erica.event_triggers_dict["yoga_quest_started"] = True
        $ erica.event_triggers_dict["yoga_sessions_started"] = False
        $ mc.business.hr_director.add_unique_on_talk_event(erica_money_problems_sarah_talk)
        if lily.event_triggers_dict.get("sister_instathot_pic_count", 0) > 0:
            "Or maybe even talk to [lily.title], see about including [erica.fname] in some of her InstaPic sessions once in a while?"
            $ erica.event_triggers_dict["insta_pic_started"] = True
            $ lily.add_unique_on_talk_event(erica_lily_instapic_setup)
    elif lily.event_triggers_dict.get("sister_instathot_pic_count", 0) > 0:
        "Maybe you could talk to [lily.title] into letting [the_person.title] join her for some of her InstaPic sessions once in a while?"
        $ erica.event_triggers_dict["insta_pic_started"] = True
        $ lily.add_unique_on_talk_event(erica_lily_instapic_setup)
    $ erica.event_triggers_dict["looking_for_work"] = True

    return


label erica_money_problems_update_label(the_person):
    if erica_get_is_doing_yoga_sessions() and erica_get_is_doing_insta_sessions():
        the_person "Actually, since you helped me out, my financial situation has been much improved!"
    elif erica_get_is_doing_yoga_sessions() or erica_get_is_doing_insta_sessions():
        the_person "It's going OK... Since you helped me out, I'm at least treading water, but it would be nice to find just a little more somewhere."
    else:
        the_person "Oh hey. I'm still looking for a part time job... Heard of anything?"
        mc.name "Not yet, sorry."
    if the_person.event_triggers_dict.get("insta_pic_started", False) == False and lily.event_triggers_dict.get("sister_instathot_pic_count", 0) > 0:
        "Maybe you should try talking to [lily.title]? You recently started taking InstaPics of her. Maybe [the_person.title] could join in for a session once in a while?"
        $ the_person.event_triggers_dict["insta_pic_started"] = True
        $ lily.add_unique_on_talk_event(erica_lily_instapic_setup)
    if the_person.event_triggers_dict.get("yoga_quest_started", False) == False and mc.business.hr_director:
        "Maybe you could check with [mc.business.hr_director.title] and see if she has any ideas?"
        $ erica.event_triggers_dict["yoga_quest_started"] = True
        $ mc.business.hr_director.add_unique_on_talk_event(erica_money_problems_sarah_talk)
    return

label erica_watch_race_intro_label(the_person):
    pass
    return

label erica_watch_race_label():
    $ the_person = erica
    return

label erica_money_problems_sarah_talk_label(the_person):
    mc.name "Hey, I have a question for you."
    the_person "Okay, shoot..."
    mc.name "My sister has a friend at the local university who is struggling to make ends meet while taking her classes."
    mc.name "She's looking for a part-time job. Would you happen to know of anything around here I could hire her to do? It has to be on a fairly flexible schedule, she needs to be able to focus on her education."
    "[the_person.possessive_title] pauses as she considers your inquiry."
    the_person "Well... Things are running fairly smoothly here to be honest... I'm not sure what we could have her do. What are her qualifications?"
    "You share what you know about her and what she is studying. Nothing really seems to pique her interest until you mention her doing track and field."
    the_person "Oh! She's an athlete?"
    mc.name "Yeah. Very accomplished in fact. Sometimes we work out together at the gym."
    "The wheels in her head are turning. She seems to have the beginning of an idea in her head."
    if get_HR_director_tag("business_HR_gym_tier", 0) > 0:
        the_person "Some of the girls here are really enjoying the gym membership you've offered... But I've gotten some complaints that after a long day here they are just too tired to make it to the gym."
    else:
        the_person "Some of the girls go to the gym after work, but it is very taxing to go into the gym after work."
    "You consider what she is saying, but you aren't sure how [erica.title] could help. After a pause though, [the_person.title] continues, clearly brainstorming out loud."
    the_person "What if we like... Hired her... To come in, like once a week, and run a personal fitness class?"
    mc.name "Here at the office?"
    the_person "Sure! It could be company sanctioned, and optional, but I think if it were supported, we would get good attendance. You could even start it like an hour before normal start time so it doesn't affect productivity."
    mc.name "Wouldn't having people work out in the morning like that affect their energy for the rest of the day?"
    the_person "You could make it something low impact? And focus on general well-being... Maybe like a yoga class?"
    "Hmm. Having [erica.title] come in and teach a yoga class once a week is actually a pretty good idea. But having it start before normal business hours, you wonder if there would be enough participation to make it worth it."
    mc.name "Can you do something for me? Take an informal poll with the employees... See how many would be interested in something like that. I don't want to arrange it just to have nobody show up."
    the_person "Well I can tell you straight away I'll come. I love yoga! How many do you think we need to make it happen?"
    $ the_person.update_opinion_with_score("yoga", 2, add_to_log = True) #If she doesn't already love yoga, she does now. TODO Maybe make different dialogue and let her not like it, but go along with it?
    mc.name "I think at least 5 total, so with you hopefully we can get 4 more."
    the_person "What about you? Can I count you to come also?"
    "Hmm... A bunch of your employees... In gym gear... Doing a bunch of crazy poses... That would be a pleasant use of the morning. But you don't want to effect the numbers too much."
    mc.name "I think I'd prefer not to be counted in that."
    if len(mc.business.get_employee_list()) < 5:
        the_person "But we don't even have that many employees?"
        mc.name "That's true. It might have to wait until we have enough employees."
    the_person "Ah okay..."
    "She looks a bit disappointed. Your company is pretty small, so you may not have the numbers. She seems to have another idea though."
    the_person "What if, umm... You know... When we do our employee meetings... We could add counseling about... errm... Yoga?"
    "You sigh. It seems [the_person.char] really likes this idea and is looking for ways to make it happen."
    if get_HR_director_tag("business_HR_coffee_tier", 0) > 0:
        mc.name "Tell you what. We don't need to push it officially, but if you happen to take some of the serum and use it for that purpose... I would be willing to look the other way."
    else:
        mc.name "I don't think that is a good idea. But if you really want to make it happen, you could always use the power of persuasion to see if you can get people to come."
    "[sarah.fname] gets a mischievous smile."
    the_person "Okay! I'll let you know in a couple days if we have the people to make it happen... And if we don't... We'll see."
    "You part ways with [the_person.title] for now. You feel pretty confident at this point that, even if you don't have the numbers now, you'll have enough people to make it happen soon."
    if len(erica_get_yoga_class_list()) < 4:
        $ mc.business.add_mandatory_crisis(erica_money_problems_sarah_update)
    else:
        $ mc.business.add_mandatory_crisis(erica_money_problems_sarah_final_update)
    return

label erica_money_problems_sarah_update_label():
    $ the_person = mc.business.hr_director
    $ the_person.draw_person(emotion = "sad")
    "[the_person.title] seeks you out as you work. She seems a bit disappointed."
    $ count = __builtin__.len(erica_get_yoga_class_list())
    if count > 0:
        the_person "Hey... So I was asking around with the girls... unfortunately, I could only get [count] interested in joining the morning yoga class... for now..."
    else:
        the_person "Hey... So I was asking around with the girls... unfortunately, I couldn't find anybody interested in joining the morning yoga class... for now..."

    "You admit you are a bit disappointed as well."
    if get_HR_director_tag("business_HR_coffee_tier", 0) > 0:
        the_person "So... Do you think that... you know, it would be okay if I, umm... used some of the serum we have for the one-on-ones...?"
        "You had forgotten about her using the serum, and you are glad she reminded you."
        mc.name "Yeah, that sounds fine. Let me know if you manage to convince enough employees and I'll speak with [erica.fname] about starting that morning yoga class."
    else:
        the_person "So, do you think it would be okay if I tried to talk people into coming? I think over time I might be able to convince enough people to come."
        mc.name "That sounds fine. Let me know if you manage to convince enough people and I'll speak with [erica.fname] about starting that program."
    $ the_person.draw_person(emotion = "happy")
    "[the_person.possessive_title] smiles wide. She seems to really be into this..."
    the_person "Yes sir! Don't worry, I'm sure we'll be able to get this going soon!"
    $ mc.business.add_mandatory_crisis(erica_money_problem_sarah_convincing_employee)
    return

label erica_money_problem_sarah_convincing_employee_label():
    python:
        scene_manager = Scene()
        the_person = mc.business.hr_director
        the_target = get_yoga_convince_employee_target()

    if the_target is None:
        $ mc.business.add_mandatory_crisis(erica_money_problem_sarah_convincing_employee)
        #For now we add the crisis back so that when we finally have enough employees we can still finish this scenario.
        return

    # change location to lobby, since break room is located here
    $ mc.change_location(lobby)
    $ mc.location.show_background()

    "Passing by the break room, you can hear [the_person.possessive_title] talking to someone else inside."
    $ scene_manager.add_actor(the_person, position = "sitting")
    $ scene_manager.add_actor(the_target, position = "sitting", display_transform = character_center_flipped)
    the_person "Yeah, it has lots of health benefits too!"
    the_target "I've heard that, but I don't know, I'm just really busy right now."
    if get_HR_director_tag("business_HR_coffee_tier", 0) > 0:
        the_person "I'm sure you are... more coffee? I just brewed some!"
        $ scene_manager.update_actor(the_person, position = "back_peek")
        the_target "Yeah! That would be great."
        "Sounds like she is using some of the serum you produced for HR meetings to help her persuade [the_target.possessive_title] to come to the yoga class."
        $ scene_manager.update_actor(the_person, position = "stand3")
        the_person "Here you go... now, I know we're all busy, but trust me, the benefits of doing yoga really are worth the time!"
        $ scene_manager.update_actor(the_person, position = "sitting")
        the_target "Yeah... maybe you're right..."
        $ scene_manager.update_actor(the_person, emotion = "happy")
        "Sounds like [the_person.possessive_title] is hard at work, convincing some of your employees to give the yoga session a shot!"
        $ the_target.update_opinion_with_score("yoga", 1)
    else:
        if (the_person.charisma * 10 + the_target.suggestibility) > renpy.random.randint(0,100):
            the_person "The science is behind it! People who do yoga live longer, happier lives. Not to mention the general benefits of the extra flexibility."
            the_target "Yeah... maybe you're right..."
            $ scene_manager.update_actor(the_target, emotion = "sad")
            "Sounds like [the_person.possessive_title] is hard at work, convincing some of your employees to give the yoga session a shot!"
            $ the_target.update_opinion_with_score("yoga", 1)
        else:
            the_person "It's good for you! I'm sure of it!"
            the_target "There's a lot of things that are good for you. I'm sorry, I just don't think I'm interested."
            $ scene_manager.update_actor(the_person, emotion = "sad")
            the_person "... I understand."
            "Sounds like [the_person.possessive_title] is still trying to convince employees to give the yoga class a try. You appreciate her dedication to it."

    python:
        scene_manager.clear_scene()
        clear_scene()
        if len(erica_get_yoga_class_list()) < 4:
            mc.business.add_mandatory_crisis(erica_money_problem_sarah_convincing_employee)
        else:
            mc.business.add_mandatory_crisis(erica_money_problems_sarah_final_update)
        the_target = None
    return

label erica_money_problems_sarah_final_update_label():
    if len(erica_get_yoga_class_list()) < 4:
        $ mc.business.add_mandatory_crisis(erica_money_problem_sarah_convincing_employee)
        return
    $ the_person = mc.business.hr_director
    $ the_person.draw_person()
    "[the_person.title] comes and finds you as you work. She seems excited."
    the_person "Hey! Guess what! As of this morning, I have enough girls willing to attend a morning yoga class once a week! As soon as you give me the day, I'll put out a notice."
    mc.name "Great! Let me talk to [erica.fname] about it. I'm not sure what day it will be yet, it will probably depend on her class schedule, but I will let you know."
    the_person "Alright. I'm going to get back to work. Looking forward to it though!"
    $ erica.add_unique_on_talk_event(erica_money_problems_yoga_start)
    return

label erica_money_problems_yoga_start_label(the_person):
    mc.name "I have an idea I wanted to share with you, an opportunity to make some money to help with tuition."
    "[the_person.title] smiles, but you can tell she is also a little apprehensive."
    the_person "That's great!... Something I can fit into my schedule? I need to be flexible you know..."
    "You can't help but make the obvious joke."
    mc.name "Oh, don't worry. You HAVE to be flexible for this!"
    the_person "I'm not sure what you mean..."
    mc.name "Dumb joke. But how about this: How would you like to teach a yoga class?"
    "She looks at you a bit skeptically."
    the_person "A yoga class? They already offer those here... And the instructor has been doing it for years..."
    mc.name "Not here. It would be once a week, in the morning, on a day of your choosing... At the business I run."
    the_person "At... your company?"
    mc.name "Yeah. We've recently been running some promotions for employees, encouraging them to stay fit, and eat right. What better way to encourage them to do that than with a personal yoga instructor?"
    the_person "That would be... incredible! I didn't realize that you took fitness so seriously! I mean... I know YOU do..."
    "She glances down at your fit chest before she continues."
    the_person "But to make it a company policy... That's a great program!"
    mc.name "I've been working with my HR director. I asked her for help coming up with something you could do at the company, and she helped me come up with the whole thing."
    mc.name "She's already got a list of the people interested, all they need to know is what day works for you to come in. We want to do it in the morning, you know, before your classes."
    "[the_person.title] looks at you, stunned."
    the_person "Wow... It's like you thought of everything!"
    $ the_person.draw_person(position = "kissing")
    $ mc.change_locked_clarity(10)
    "[erica.fname] gives you a big hug. When she steps back, she ponders a moment."
    the_person "How about Tuesday mornings? I could go straight from there to class."
    mc.name "I'll make it happen. For compensation, I'll start you at $100 per session. Are you good to start next week?"
    the_person "That's great! I'll be ready!"
    mc.name "Okay. I'm going to give your number to my HR director. She'll contact you to set up the final details. Her name is [mc.business.hr_director.name]."
    the_person "I'll look for it. I'm going to get back to my workout, thank you so much!"
    "After you finish up your conversation, you text [mc.business.hr_director.title], your HR director. You give her [the_person.possessive_title]'s contact info."
    $ the_person.set_override_schedule(lobby, the_days = [1], the_times = [0])
    $ mc.business.hr_director.set_override_schedule(lobby, the_days = [1], the_times =[0])
    $ mc.business.add_mandatory_morning_crisis(erica_yoga_event_intro)
    return

label erica_yoga_event_intro_label():
    python: # setup yoga class
        scene_manager = Scene() # only use one scene manager per event

        the_person = erica
        yoga_assistant = mc.business.hr_director
        yoga_list = erica_get_yoga_class_list()

        erica_apply_yoga_outfit_to_class([the_person, yoga_assistant] + yoga_list)
        erica.event_triggers_dict["yoga_assistant"] = yoga_assistant.identifier

    "It's Tuesday morning, it is weekly morning yoga day! While you don't think you'll need to go every time, since this is the inaugural session, it might be good for you to oversee it, just in case there are any issues."
    if mc.is_at_work():
        "You go down to the lobby to see how things are working out."
        $ mc.change_location(lobby)
        $ mc.location.show_background()
        "As you walk into the main lobby, you see some of your employees just getting ready to set up."
    else:
        "You head to the office early, to see how things are working out."
        $ mc.change_location(lobby)
        $ mc.location.show_background()
        "When you walk into the main lobby, you see some of your employees just getting ready to set up."

    $ scene_manager.add_actor(the_person)
    $ scene_manager.add_actor(yoga_assistant, display_transform = character_center_flipped)
    "At the front, you see [the_person.possessive_title] doing some light stretching. She brought a portable Bluetooth speaker, playing some upbeat music."
    "Next to her you see [yoga_assistant.title]. She has been the biggest supporter of this event from the get-go, and it doesn't surprise you to see her at the front of the group. As you walk up, you can hear the two chatting. They seem to be hitting it off..."
    yoga_assistant "Oh! Wow that's a really good time! I could never do something like that, I just don't have the endurance..."
    the_person "Yeah, I've been running since I was little. I don't know why, I've just always loved it! But I know it's not for everyone."
    if yoga_assistant.has_large_tits():
        if yoga_assistant is sarah:
            yoga_assistant "Yeah... I recently, umm... filled out a bit... Running long distances isn't really practical with these!"
            "[yoga_assistant.title] gives her pleasantly [yoga_assistant.tits_description] a shake."
        else:
            yoga_assistant "I've been keeping in shape by doing some exercises, but I'm not there yet."
            the_person "Hey, I'm glad you're still taking steps to stay fit though. You gotta work with the assets you've been given!"
        "The girls share a laugh."
    else:
        yoga_assistant "Yeah. Everyone is different. This class is going to be great though! I think with time and some training, just about everyone can get something out of yoga!"
        the_person "I agree! No one can do everything... Sometimes you just have to work with the assets you've been given!"
        "The girls share a laugh."

    "Okay ... [yoga_assistant.title] and [the_person.possessive_title] seem to REALLY be hitting it off. You make a mental note. You walk up to the front and greet them."
    mc.name "Hello [the_person.title] and [yoga_assistant.title]. Looks like this is going to be a good training class!"
    the_person "Oh hey [the_person.mc_title]!"
    the_person "I'm glad to see you. I wasn't sure if you were going to be here or not."
    yoga_assistant "Hello [yoga_assistant.mc_title]! The man of the hour! Here to make sure company funds are being spent wisely?"
    "[the_person.title] chuckles."
    mc.name "I have no doubt that you two will make this class a success. I'm just here to make sure all the first session jitters get worked out and to lend a hand if any problems arise."
    the_person "Thanks, [the_person.mc_title]. I really appreciate your support with this. It's just a yoga class, but having you here definitely helps me feel more confident trying to tackle this!"
    yoga_assistant "Yeah, don't worry [the_person.fname], [mc.name] is a great guy to work for! He really knows how to treat his employees!"
    mc.name "Alright, I'll be over there, getting some of the morning paperwork started. Let me know if you need anything."
    "You head to the side of the room and sit down at a computer terminal. You pull up some serum designs and get to work, analyzing them. After a bit, you glance up when you hear [the_person.possessive_title] starting things up."
    the_person "Good morning everyone! Thanks for coming out. Since today is our first session, we are going to start out with just some basic poses and breathing techniques! Does anyone have any questions before we get started?"
    "You watch as your employees start out doing some light stretching. Everyone seems to be paying attention and trying their best."
    "This really does seem like it could be a good benefit for your employees who are willing to come out a bit early. You turn back to the computer and get to work."
    call erica_yoga_loop_label(the_person, yoga_assistant) from _erica_yoga_loop_call_01
    "As you finish up with your work, you hear [the_person.title] calling out instructions for the cool down. Sounds like the yoga session is wrapping up as well. The girls finish and start rolling up their mats."
    $ scene_manager.add_actor(the_person)
    "You walk up to [the_person.possessive_title]."
    mc.name "Congratulations, that seemed like a very successful first meeting!"
    the_person "Thank you!"
    call erica_getting_watched_reaction_label(the_person, _return) from _erica_gets_watched_during_yoga_intro_01
    $ scene_manager.add_actor(yoga_assistant, display_transform = character_center_flipped)
    yoga_assistant "Alright, I know everyone is thirsty. Anyone who needs water, head for the break room."
    "You can hear [yoga_assistant.possessive_title] calling out. The room starts to clear. She walks over to you and [the_person.possessive_title]."
    yoga_assistant "That went great!"
    "[yoga_assistant.title] seems pretty enthusiastic."
    the_person "You think so? I honestly wasn't sure... But it seemed like everyone did well."
    "[the_person.possessive_title] seems a little apprehensive, but you think she probably just needs to build some confidence."
    mc.name "Well, is there anything I can do to help for next time?"
    "[the_person.title] thinks about it for a bit, but [yoga_assistant.possessive_title] quickly speaks up."
    yoga_assistant "It's actually kind of a pain, having to go all the way to the break room to get water. Maybe we could get one of those 5 gallon water dispensers?"
    "It's not THAT hard to just walk to the break room... But at the same time, if you had a water source that all the girls at the yoga session used, you could dose it with serum and every girl attending would get some..."
    mc.name "Can you get that ordered and just put it on the company account?"
    yoga_assistant "Yes sir!"
    mc.name "Also, could you make sure [the_person.title] gets paid? For now her standard fee is $100 per session."
    yoga_assistant "Sure thing!"
    mc.name "One last thing... I think I'd like to follow your previous request, and add yoga as a topic to discuss with employees at our HR meetings."
    mc.name "With a little work, I think we could really make something special here."
    "You say goodbye to [the_person.title] and [yoga_assistant.title]. They turn and walk off, with [the_person.possessive_title] following so they can work out payment details. You can hear them chattering as they start to walk off."
    the_person "You did great! I was overall really impressed with all the girls who came. Seems like most of the girls here take care of themselves..."
    yoga_assistant "Yeah, but not all of them were here today... Hopefully I can drag more of them out here next week..."
    "It seems the two girls have struck up a friendship. You wonder how things will develop between them."
    $ town_relationships.update_relationship(the_person, yoga_assistant, "Best Friend")

    python:
        # setup yoga events
        erica.event_triggers_dict["yoga_sessions_started"] = True
        erica.add_unique_on_room_enter_event(erica_weekly_yoga)

        # cleanup yoga class
        yoga_list.append(yoga_assistant) #Add assistant to yoga list to make sure she gets appropriate energy increase and outfit cleanup.
        erica_after_class_outfit_cleanup(yoga_list) #NOTE we rely on Erica moving to gym next to make sure her outfit gets cleaned up.
        erica_class_energy_increase(yoga_list)

        # make sure we set the schedule right (fixes room change)
        the_person.set_override_schedule(lobby, the_days = [1], the_times = [0])
        yoga_assistant.set_override_schedule(lobby, the_days = [1], the_times =[0])

        scene_manager.clear_scene()
        yoga_list = None
        yoga_assistant = None


    call advance_time(no_events = True) from _call_advance_time_erica_yoga_intro
    return

label erica_yoga_loop_label(the_person, yoga_assistant):
    python: # init loop
        scene_manager.clear_scene(reset_actor = False)
        slutty_class = erica_get_class_average_sluttiness(yoga_list) > 50
        nude_class = erica_get_is_yoga_nude()
        back_row = erica_get_back_of_class(yoga_list)
        erica_num_watched = 0
        erica_only_watch = False

    "As you start your morning paperwork, you come across a personnel list of possible personality conflicts from the HR department."
    "If you focus on this, you could probably improve company efficiency by quite a bit."
    "As you listen, you hear [the_person.possessive_title] begin the warmups. Maybe you should just sit back and watch the girls do their yoga, too?"
    "[back_row[0].title], [back_row[1].title], and [back_row[2].title] are the three girls in the back, closest to where you are."
    if erica.love >= 60 and not erica_post_yoga_fuck_complete() and erica.is_willing(against_wall):
        "However, something about [erica.possessive_title] really grabs your attention."
        "You've been getting closer and closer to her lately. Despite the women in the room, you feel like you can barely take your eyes off of her."
        $ erica_only_watch = True
    elif nude_class:
        "However, with the class being nude... surely work can get done at another time, right?"
    elif slutty_class:
        "The outfits that you've seen around the room... a lot of them really draw your attention. The class has been getting sluttier and sluttier each week..."
    $ the_pose = get_random_from_list(erica_yoga_poses)
    menu:
        #"Work on efficiency (disabled)": #We aren't here to get work done! Probably actually make this possible in the future though.
        #    pass
        "Watch [the_person.title]":
            "You look up and see [the_person.possessive_title] and [yoga_assistant.title] near the front of the class."
            $ switch_to_class_front(the_person, yoga_assistant, the_pose)
            $ display_yoga_dialog(the_pose)
            "You watch for a while, but soon turn your attention back to the computer."
            $ erica_num_watched += 1
        "Watch the class" if not erica_only_watch:
            "You decide to watch the girls in their class instead. How often do you get the chance to watch a show like this?"
            $ switch_to_back_of_class(back_row, the_pose)
            $ display_yoga_dialog(the_pose)
            "You watch for a while, but soon turn your attention back to the computer."

    $ scene_manager.clear_scene(reset_actor = False)
    "You decide to pull up one of the recent medical journals that you usually read."
    "You stumble across an article that has some interesting implications with one of the serums you recently began testing."
    "If you read the article, it might help reduce the number of side effects that serum usually has."
    "Before you start reading, you can hear [the_person.title] calling out more instructions. The girls are starting to get into the yoga session!"
    "Maybe you should watch it..."
    if erica_only_watch:
        "Once again, your eyes are drawn to [the_person.possessive_title]. Her sexy form looks so good doing the different poses, you can't look away."
    elif nude_class:
        "Sweat is beginning to form a sheen on the stunning nude bodies that are presented to you in incredible poses."
        "You note that several of the girls are occasionally touching themselves between poses, pulling at hard nipples and stroking increasingly wet cunts."
    elif slutty_class:
        "Some of the girls are starting to work up a good sweat, giving a nice shine to their nubile bodies."
    $ the_pose = get_random_from_list(erica_yoga_poses)
    menu:
        #"Work on research (disabled)": #We aren't here to get work done! Probably actually make this possible in the future though.
        #    pass
        "Watch [the_person.title]":
            "You look up and see [the_person.possessive_title] and [yoga_assistant.title] near the front of the class."
            $ switch_to_class_front(the_person, yoga_assistant, the_pose)
            $ display_yoga_dialog(the_pose)
            "You watch for a while, but soon turn your attention back to the computer."
            $ erica_num_watched += 1
        "Watch the class" if not erica_only_watch:
            "You decide to watch the girls in their class instead. Your eyes are treated to the girls in the back of the class."
            $ switch_to_back_of_class(back_row, the_pose)
            $ display_yoga_dialog(the_pose)
            "You watch for a while, but soon turn your attention back to the computer."

    # SHORTENED LOOP BY ONE SCENE, it gets tedious watching it over and over.
    # $ scene_manager.clear_scene(reset_actor = False)
    # "You decide to pull up a list of suppliers for some of your chemical components."
    # "As you look at a few of their websites, you discover that one of them is dumping stock of a component they accidentally over produced!"
    # "If you order it right now, you could get a bunch of supplies at a steeply discounted rate."
    # "Before you make the order, you can hear [the_person.title] encouraging the class to keep with it. The yoga session is getting intense!"
    # "Maybe you should watch it..."
    # if nude_class:
    #     "When you glance up, sexual tension in the room is really ramping up."
    #     "A couple girls are now actively making out, and another pair are doing their poses so close together their bodies are rubbing against each other."
    # elif slutty_class:
    #     "The sound of heavy breathing and gasps coming from the class makes it hard to pay attention to the computer terminal."
    # $ the_pose = get_random_from_list(erica_yoga_poses)
    # menu:
    #     "Work on supply (disabled)": #We aren't here to get work done! Probably actually make this possible in the future though.
    #         pass
    #     "Watch [the_person.title]":
    #         "You look up at and see [the_person.possessive_title] and [yoga_assistant.title] near the front of the class."
    #         $ switch_to_class_front(the_person, yoga_assistant, the_pose)
    #         $ display_yoga_dialog(the_pose)
    #         $ erica_num_watched += 1
    #     "Watch the class":
    #         "You can't help it, this might be your last chance for today to watch the girls posing. You look up at the class and watch intently"
    #         $ switch_to_back_of_class(back_row, the_pose)
    #         $ display_yoga_dialog(the_pose)

    # if mc.arousal <= 10:
    #     "The class is wrapping up now, and you feel pretty good about the amount of work you were able to get done."
    # elif mc.arousal <= 30:
    #     "The class is wrapping up now. You didn't get as much done as you would have liked, but the views from where you were sitting were worth it!"
    # elif mc.arousal <= 60:
    #     "The class is wrapping up now. Your erection is hard to ignore after watching the girls do all kinds of sexy poses."
    # else:
    #     "The class is wrapping up now. It appears to be degenerating into an outright orgy. You consider joining the fray."

    python:
        # cleanup loop
        scene_manager.clear_scene(reset_actor = False)
        back_row = None

    return erica_num_watched

label erica_weekly_yoga_label(the_person):
    if not erica.is_available:
        call erica_no_yoga_session_this_week() from _call_erica_no_yoga_session_this_week_1
        return

    python: # setup yoga class
        scene_manager = Scene() # only use one scene manager per event

        the_person = erica
        yoga_assistant = erica_get_yoga_assistant()
        yoga_list = erica_get_yoga_class_list()
        schedule_assistant = True

        erica_apply_yoga_outfit_to_class([the_person, yoga_assistant] + yoga_list)

    "As you walk into the lobby, you see the now-familiar sight of some of your employees gathering for their weekly yoga session."
    if erica_get_is_yoga_nude():
        "The girls are all naked, as has been previously decided. Nude yoga is probably your favorite spectator sport right now."

    $ scene_manager.add_actor(the_person)
    if not yoga_assistant.available:
        mc.name "Hey [the_person.title], I see [yoga_assistant.name] is not here today?"
        the_person "Yeah, [yoga_assistant.name] couldn't make it this week."
        $ yoga_assistant = erica_get_alternative_assistant(yoga_list)
        $ erica_apply_yoga_outfit_to_class([yoga_assistant])
        the_person "But [yoga_assistant.name] is filling in for her."
        $ scene_manager.add_actor(yoga_assistant, display_transform = character_center_flipped)
        $ schedule_assistant = False
    else:
        $ scene_manager.add_actor(yoga_assistant, display_transform = character_center_flipped)
        "At the front, you see [the_person.possessive_title] doing some light stretching. She has a speaker out, playing some upbeat music."
        "Next to her you see [yoga_assistant.title]. They have become good friends and are chatting idly as you walk up."
        the_person "Oh hey [the_person.mc_title]!"

    if not erica_get_is_yoga_nude() and erica_get_class_average_sluttiness(yoga_list) > 80: #Average class sluttiness is super slutty. They want to do it nude from now on
        the_person "I'm glad you're here. Several of the girls have approached me about something, but I wanted to run it by you before it became an official policy."
        the_person "The class and I both agree, this is a great, safe place to celebrate the feminine form and what we are capable of."
        the_person "It has been requested by multiple people here that our yoga sessions adopt an au naturel dress code."
        yoga_assistant "Because the office is currently closed, this technically falls outside of the employee uniform requirements..."
        yoga_assistant "But we decided that it would probably be better to run it by you before me make it official. It IS your office building, after all!"
        $ mc.change_locked_clarity(20)
        "Holy fuck, they want to do yoga in the nude. You rack your brain, trying to think of a logical reason to say no. Only one thing comes to mind."
        mc.name "Umm... I think I'm okay with that... except... Everyone still needs to wear shoes."
        the_person "Shoes?"
        mc.name "If there is a nail or something that happens to be on the floor, I don't want to be held liable in case someone gets injured."
        yoga_assistant "Oh! That makes total sense."
        the_person "This is great! I'll make an announcement."
        "[the_person.possessive_title] raises her voice extra loud so everyone in the room can hear it."
        the_person "Hey everyone! Good news! We just got the okay, from now on - in celebration of the female body - this will be a nude yoga class!"
        "You hear several cheers go up from the group."
        "You notice that [yoga_assistant.possessive_title] has already started to strip down..."
        $ scene_manager.strip_full_outfit(person = yoga_assistant)
        $ mc.change_locked_clarity(20)
        the_person "We only ask, please leave your shoes on! This is a safety issue, in case a piece of glass or other object is left on the floor!"
        "When she finishes the announcement, [the_person.title] starts to strip down also."
        $ scene_manager.strip_full_outfit(person = the_person)
        $ mc.change_locked_clarity(20)
        "You look around and watch as the all the girls are also stripping. It is a surreal moment."
        # "You walk over to the computer terminal in a daze. You sit down, and let the girls get started in their official, company sponsored, all nude yoga class."
        $ the_person.event_triggers_dict["nude_yoga"] = True
        $ erica_apply_yoga_outfit_to_class([the_person, yoga_assistant] + yoga_list)

    else:
        $ class_size = __builtin__.len([the_person, yoga_assistant] + yoga_list)
        the_person "Glad you could make it! We are just getting ready to get started."
        yoga_assistant "Hello [yoga_assistant.mc_title]! I was just getting ready to fill up the water jug for the attendants."
        "You consider offering to fill it for her. It would give you a chance to distribute a dose of serum to all [class_size] of the girls gathered."
        menu:
            "Fill it for her\n{color=#00FF00}{size=18}Give class serum{/size}{/color}":
                call screen serum_inventory_select_ui(mc.inventory)
                if not _return == "None":
                    $ the_serum = _return
                    if mc.inventory.get_serum_count(the_serum) > __builtin__.len([the_person, yoga_assistant] + yoga_list):
                        "You decide to add [class_size] doses of [the_serum.name] to the water jug. You quickly return and place it on the counter."
                        $ dose_yoga_class_with_serum([the_person, yoga_assistant] + yoga_list, the_serum)
                    else:
                        "You have insufficient doses to make the serum effective in that much water."
                        "You quickly return with the water jug with absolutely no serum in it and place it on the counter."
                    $ the_serum = None
                else:
                    "You quickly return with the water jug with absolutely no serum in it and place it on the counter."
            "Chat with [the_person.title]":
                mc.name "Don't let me keep you."
                yoga_assistant "Right..."
                "[yoga_assistant.title] grabs the jug and leaves the room."
                $ scene_manager.hide_actor(yoga_assistant)
                "You turn to [the_person.title]."
                mc.name "Thank you again for doing this. I really feel like this is a huge benefit for the company."
                the_person "Of course! Glad to do it. I get the feeling from talking to the girls here that you are a great boss to work for, too!"
                mc.name "Alright, I'll let you get to it. I'm going to try and get some work done, let me know if you need anything."

    "You head to the side of the room and sit down at a computer terminal. You pull up some serum designs and get to work, analyzing them. After a bit, you glance up when you hear [the_person.possessive_title] starting things up."
    the_person "Good morning everyone! Thanks for coming out. We are going to start things out slowly this morning with some stretching!"
    "You watch as your employees start out doing some light stretching. Everyone seems to be paying attention and trying their best."
    "You turn back to the computer and get to work."
    call erica_yoga_loop_label(the_person, yoga_assistant) from _erica_yoga_loop_call_02
    if erica_get_is_yoga_nude():
        "As the all-nude yoga session finishes, several girls are REALLY celebrating the feminine form."
        "As you walk over to [the_person.possessive_title], you pass a pair of girls in a sixty-nine, moaning as they eat each other out."
        "Another couple are on their hands and knees, ass to ass... with a double-sided dildo? Where the hell did that come from?"
    else:
        "As you finish up with your work, you hear [the_person.title] calling out instructions for the cool down. Sounds like the yoga session is wrapping up as well. The girls finish and start rolling up their mats."
    $ scene_manager.add_actor(the_person)
    "You walk up to [the_person.title]."
    mc.name "Looks like another highly successful yoga class."
    the_person "Thank you!"
    "She has a definite hint of pride in her voice."
    call erica_getting_watched_reaction_label(the_person, _return) from _erica_gets_watched_during_yoga_recurrent_01
    $ scene_manager.add_actor(yoga_assistant, display_transform = character_center_flipped)
    "As you are talking, [yoga_assistant.title] walks up to you."
    yoga_assistant "Great class!"
    $ remaining_person = None
    if erica.love >= 60 and not erica_post_yoga_fuck_complete() and erica.is_willing(against_wall): #Love scene
        mc.name "[the_person.title], could you come to my office for a minute? I have some ideas for additional things you could do during the session."
        the_person "Oh, sure! I have some time before my first class."
        yoga_assistant "Ah, guess I'll get to work then."
        $ scene_manager.remove_actor(yoga_assistant)
        call erica_post_yoga_love_label() from _erica_60_love_post_yoga_scene_01
    elif mc.arousal >= 30: #Use 30 so that this is possible from the start
        "Unfortunately, there is no hiding your erection from the duo. Watching the class has you way too excited."
        if willing_to_threesome(the_person, yoga_assistant) and renpy.random.randint(0,2) == 0: #Give a chance, if possible, to get a double blowjob after the show
            "[yoga_assistant.title] is blatantly gawking at your tent, when [the_person.title] speaks up."
            the_person "Yup, there's only one thing left to do!"
            mc.name "Oh? Whats that?"
            the_person "The best way to make gains after a workout is with a shot of protein!"
            "[the_person.possessive_title] is clearly referencing your cum."
            yoga_assistant "Oh! That sounds good! Can I get some too?"
            mc.name "I think there's enough for both of you. Let's step into my office really quick."
            "The duo quickly follow you to your office. As you walk in, you turn and lock the door."
            $ ceo_office.show_background()
            "Before you can say anything, the girls are already getting down on their knees, ready to earn their protein."
            "You take out your cock and let them get to work."
            call start_threesome(the_person, yoga_assistant, start_position = threesome_double_blowjob, position_locked = True) from _after_yoga_protein_yum_1
            $ the_report = _return
            if the_report.get("guy orgasms", 0) > 0:
                "You enjoy your post-orgasm bliss for a few moments while [the_person.possessive_title] and [yoga_assistant.possessive_title] swap your cum back and forth for a bit."
                "When you look back down, they seem to have swallowed most of it, but [yoga_assistant.title] is licking the last few remnants of your cum off of [the_person.possessive_title]'s face."
            $ scene_manager.update_actor(the_person, position="stand3", display_transform = character_center_flipped)
            $ scene_manager.update_actor(yoga_assistant, position = "stand4", display_transform = character_right)
            "The girls stand back up."
            mc.name "God, what a way to start the day."
            yoga_assistant "I know! Starting the day off right."
            the_person "Yeah. Sorry, but I need to get going. [yoga_assistant.name], did you want to hang out later this week?"
            yoga_assistant "I'll have to text you later, I'm not sure yet."
            the_person "Ok! " #Make a small chance, if possible, to have a threesome.
        elif renpy.random.randint(0,1) == 0:
            if the_person.sluttiness > 40:
                "[the_person.title] looks at you longingly, but you can tell she has to get going."
            the_person "Sorry, I really need to get going."
            "As she starts to walk by you, she whispers in your ear."
            the_person "If you need help with that later, swing by the gym..."
            $ mc.change_locked_clarity(10)
            "She walks off leaving you with [yoga_assistant.title]."
            $ scene_manager.remove_actor(the_person)
            $ remaining_person = yoga_assistant
            # call erica_after_yoga_office_session_label(yoga_assistant) from _sarah_after_yoga_fun_01
        else:
            if yoga_assistant.sluttiness > 40:
                "[yoga_assistant.title] looks at you longingly, but you can tell she has to get going."
            yoga_assistant "Sorry, I really need to get going."
            "As she starts to walk by you, she whispers in your ear."
            yoga_assistant "If you need help with that, I'm sure we can find a private place after the workday starts..."
            $ mc.change_locked_clarity(10)
            "She walks off leaving you with [the_person.title]."
            $ scene_manager.remove_actor(yoga_assistant)
            $ remaining_person = the_person
            # call erica_after_yoga_office_session_label(the_person) from _erica_after_yoga_fun_01

        if remaining_person:
            if remaining_person.effective_sluttiness() > 40:
                "[remaining_person.title] looks at you, smiling."
                remaining_person "Guess it's just you and me. Why don't we find somewhere... private?"
                $ threesome_partner = get_random_from_list(yoga_list)
                menu:
                    "Head to your office":
                        mc.name "I know just the place."
                        call erica_after_yoga_office_session_label(remaining_person) from _erica_after_yoga_fun_01
                    "Ask [threesome_partner.title] to join" if erica_get_is_yoga_nude() and willing_to_threesome(remaining_person, threesome_partner):
                        mc.name "Private? Look around... why would we have to go somewhere private?"
                        remaining_person "Ah, okay."
                        "Off to one side, you see [threesome_partner.possessive_title], apparently taking a break by herself."
                        mc.name "Let's go over there and have some fun with [threesome_partner.title]."
                        remaining_person "Sounds good! I'll follow your lead!"
                        "You and [remaining_person.title] walk over to [threesome_partner.title]. Her eyes light up when she sees the two of you approaching her."
                        $ scene_manager.add_actor(threesome_partner, display_transform = character_left)
                        threesome_partner "Hello! I was just getting ready to get to work, sir..."
                        mc.name "No need for that yet. Let's have a little fun first."
                        threesome_partner "Yay! I was hoping you would say that!"
                        call start_threesome(remaining_person, threesome_partner) from _nude_yoga_aftermath_threesome_01
                        "Satisfied for now, you decide to get cleaned up and ready for work."
                        call erica_nude_yoga_office_aftermath_label() from _nude_yoga_lobby_survey_01
                    "Decline":
                        mc.name "Sorry, but the workday is approaching quickly. I have a lot to get done today."
                        $ remaining_person.change_happiness(-3)
                        remaining_person "Wow... okay, I guess..."
                        "Rejected, [remaining_person.possessive_title] quickly walks off."
            else:
                "[remaining_person.title] gives you a shy smile."
                remaining_person "Well... I, umm... I'm glad you enjoyed the class. I should probably get going as well..."

    elif erica_get_is_yoga_nude(): #You didn't really watch, but the girls having sex all around you is distracting.
        "You try to make conversation with the duo, but the sounds of sex building in the room is getting to be distracting."
        yoga_assistant "It's amazing, isn't it? A group of women, getting together, getting empowered, taking their pleasure into their own hands."
        mc.name "Yes, it's amazing for sure."
        if willing_to_threesome(the_person, yoga_assistant):
            the_person "I have some time before I have to get to class... want to mess around some?"
            yoga_assistant "Oh! Yeah, me too, me too!"
            "The girls look at you, hungrily. It is clear they want to have some fun with you before they clean up."
            menu:
                "Have a threesome":
                    "The girls watch you hungrily as you get undressed. When you take your underwear off, your cock springs free."
                    call start_threesome(the_person, yoga_assistant) from _nude_yoga_aftermath_threesome_02
                    "Satisfied for now, you decide to get cleaned up and ready for work."
                    the_person "Mmm, that was great!"
                    yoga_assistant "Hey [the_person.fname], did you want to get together this weekend?"
                    the_person "I'm not sure yet, I'll have to see how much homework I get! I'll text you."
                    "It's been amazing witnessing the two girls develop such a deep friendship."
                    call erica_nude_yoga_office_aftermath_label() from _nude_yoga_lobby_survey_02
                "Decline":
                    mc.name "Sorry, but the workday is approaching quickly. I have a lot to get done today."
                    $ the_person.change_happiness(-3)
                    $ yoga_assistant.change_happiness(-3)
                    yoga_assistant "Wow... okay, I guess..."
                    the_person "Your loss!"
                    "Rejected, [remaining_person.possessive_title] quickly walks off."
                    yoga_assistant "Guess we'll just have some fun without you..."
                    $ scene_manager.update_actor(the_person, position = "kissing")
                    $ scene_manager.update_actor(yoga_assistant, position = "walking_away", display_transform = character_right)
                    "The two girls embrace each other and start to kiss as you walk away."
        elif the_person.sluttiness > 40 and yoga_assistant.sluttiness > 40:
            "The two girls look at you a bit awkwardly, as if waiting for you to do something."
            the_person "So... umm... you want to do anything, [the_person.mc_title]?"
            yoga_assistant "Yeah... I mean... didn't you want to talk to me, in your office or something?"
            "The girls seem to want you to pick one of them."
            menu:
                "Private time with [the_person.title]":
                    "You're right [the_person.title]. Do you have a minute? I need to discuss something with you in my office."
                    $ the_person.change_stats(happiness = 5, love = 3)
                    $ yoga_assistant.change_stats(happiness = -5, love = -3)
                    the_person "Oh! Yeah I definitely have some time."
                    "[yoga_assistant.possessive_title] clearly looks a little rejected."
                    yoga_assistant "I guess I'll get to work..."
                    call erica_after_yoga_office_session_label(the_person) from _erica_after_yoga_fun_02
                "Private time with [yoga_assistant.title]":
                    "You're right [yoga_assistant.title]. I have a problem with some time sheets. I printed them in my office, can you follow me?"
                    $ the_person.change_stats(happiness = -5, love = -3)
                    $ yoga_assistant.change_stats(happiness = 5, love = 3)
                    yoga_assistant "Oh! Yeah, I remember now! Let's go."
                    "[the_person.possessive_title] clearly looks a little rejected."
                    the_person "I guess I'll get to the university..."
                    call erica_after_yoga_office_session_label(yoga_assistant) from _erica_after_yoga_fun_03
                "Get to work":
                    mc.name "I'm sorry, I have some work that I need to accomplish. The session today was great though. Keep up the good work you two!"
                    "They both look at you disappointed, but nothing more comes of it. You say your goodbyes and soon you are starting your workday."
        else:
            "Awkwardly, you decide it would be best to get to work."
            mc.name "I'm sorry, I have some work that I need to accomplish. The session today was great though. Keep up the good work, you two!"
            "They are both watching the orgy unfolding. You say your goodbyes and soon you are starting your workday."
        $ the_person.change_stats(slut = 1, max_slut = 70)
        $ yoga_assistant.change_stats(slut = 1, max_slut = 70)
    else:
        the_person "Yeah, that was great!"
        yoga_assistant "Hey [the_person.fname], did you want to get together this weekend?"
        the_person "I'm not sure yet, I'll have to see how much homework I get! I'll text you."
        "It's been amazing witnessing the two girls develop such a deep friendship. You decide it is time for you to start your workday proper now also."
    python:
        # setup next event
        erica.add_unique_on_room_enter_event(erica_weekly_yoga)
        remaining_person = None
        threesome_partner = None
        # cleanup yoga class
        yoga_list.append(yoga_assistant) #Add assistant to yoga list to make sure she gets appropriate energy increase and outfit cleanup.
        erica_after_class_outfit_cleanup(yoga_list)
        erica_class_energy_increase(yoga_list)

        # make sure we set the schedule right (fixes room change)
        the_person.set_override_schedule(lobby, the_days = [1], the_times = [0])
        if schedule_assistant:
            yoga_assistant.set_override_schedule(lobby, the_days = [1], the_times =[0])

        scene_manager.clear_scene()
        yoga_list = None
        yoga_assistant = None

    call advance_time(no_events = True) from _call_advance_time_erica_yoga_weekly_recurring
    return

label erica_no_yoga_session_this_week():
    python: # setup yoga class
        scene_manager = Scene() # only use one scene manager per event
        yoga_assistant = erica_get_yoga_assistant()

    if not yoga_assistant.is_available:
        "As you walk into the lobby, you expected to see the yoga class, but nobody is here."
        "You suddenly remember that [erica.possessive_title] is not available and they probably rescheduled the class."
    else:
        $ scene_manager.add_actor(yoga_assistant)
        mc.name "Hey [yoga_assistant.title], no class today?"
        yoga_assistant "Hey [yoga_assistant.mc_title], nah, [erica.fname], couldn't make it today, we rescheduled to next week."
        mc.name "Ok, thanks."

    python:
        # setup next event
        erica.add_unique_on_room_enter_event(erica_weekly_yoga)
        scene_manager.clear_scene()
        yoga_assistant = None
    return


label erica_getting_watched_reaction_label(the_person, watched_count = 0): #A short label to describe how Erica feels when you watch her doing yoga.
    if watched_count == 0:
        return # we didn't look at her

    if erica.love >= 60 and not erica_post_yoga_fuck_complete() and erica.is_willing(against_wall):
        the_person "So... enjoy the class? Or did you even notice there were other girls in the room?"
        "She is blushing heavily and looking down."
        mc.name "What can I say, I really enjoyed watching the class, but watching the instructor in particular. Her form is fantastic."
        "She gives you a genuine smile, but otherwise doesn't say anything."
        $ the_person.change_stats(love = 3, slut = 2, max_slut = 40)
    elif (watched_count * 20) + 10 > the_person.effective_sluttiness(): #She is embarrassed how much you watched her. sluttiness gain.
        if watched_count == 1:
            the_person "I couldn't help but notice you sneaking glances at me... during the session."
            "She is blushing slightly."
            mc.name "Sorry, being in the same room as you doing yoga is a little bit distracting."
            the_person "It's okay! I actually don't mind. That's totally normal, right?"
            mc.name "Of course."
            $ the_person.change_stats(love = -1, slut = 1, max_slut = 30)
        # elif watched_count == 2:
        #     the_person "I couldn't help but notice you looking at me during the session."
        #     "She is blushing."
        #     mc.name "You're a beautiful woman, [the_person.title]. I'm sorry, I'll try not to stare so much next time."
        #     the_person "It's okay! I mean, I guess that's pretty normal, considering the circumstances."
        #     $ the_person.change_stats(happiness = 2)
        else:
            the_person "I couldn't help but notice you staring at me the entire session. I could feel your eyes every time I posed..."
            "She is blushing heavily and looking down."
            mc.name "I'm sorry. You're a sexy woman, and having you in the same room doing yoga is very distracting."
            "She smiles at you, but you can tell she is a little uncomfortable."
            the_person "It's okay I guess... considering the circumstances."
            $ the_person.change_stats(love = -3, slut = 2, max_slut = 40)
    else:
        if watched_count == 1:
            the_person "I couldn't help but notice you sneaking glances at me during the session."
            "She is smiling at you."
            the_person "It's kind of nice, having you here to watch. Did you like what you saw?"
            mc.name "Of course. You're very flexible, and a great yoga instructor."
            the_person "Aww, thank you."
            $ the_person.change_stats(love = 1, happiness = 1, slut = 1, max_slut = 20, add_to_log = False)
        # elif watched_count == 2:
        #     the_person "I couldn't help but notice you looking at me during the session."
        #     "She is smiling wide."
        #     the_person "I can't say I blame you. Should I assume from the drool that was coming out of the side of your mouth that you liked what you saw?"
        #     mc.name "Definitely. You have a great figure, and being in the same room during yoga, I couldn't help but watch."
        #     the_person "Aww, you're sweet."
        #     $ the_person.change_stats(love = 2, happiness = 2)
        else:
            the_person "I couldn't help but notice you staring at me the entire session. I could feel your eyes every time I posed..."
            "She is giving you a mischievous smile."
            if erica_get_is_yoga_nude():
                the_person "I love the atmosphere in here, with everyone naked. But I love it even more that your eyes were glued to me the entire time."
                mc.name "I can't help it, your figure is absolutely stunning."
                the_person "Thank you... do you think we have time to help you take care of... this?"
                $ mc.change_locked_clarity(20)
                "She puts her hand on your erection and gives it a few strokes."
            else:
                the_person "I could feel you undressing me with your eyes every time I posed."
                "She lowers her voice to a soft growl."
                the_person "Maybe later you can undress me with your hands."
                mc.name "Don't worry, I intend to."
            $ the_person.change_stats(happiness = 3, love = 3, slut = 2, max_slut = 50,add_to_log = False)
    return

label erica_after_yoga_office_session_label(the_person): #Theoretically this could be anyone, don't use any specific reference to a person.
    "You head to your office, bringing [the_person.possessive_title] with you. You open the door, walk in, then close and lock it behind you."
    $ ceo_office.show_background()
    "You quickly grab her and pin her to the wall."
    $ scene_manager.update_actor(the_person, position = "kissing", display_transform = character_right)
    $ mc.change_locked_clarity(20)
    "She wraps her arms around you and you start to make out, your mouths meeting and exploring each other."
    "[the_person.title] moans when she feels your erection pressing against her."
    $ the_person.change_arousal(20)
    $ initial_outfit = the_person.outfit.get_copy() # store outfit
    menu:
        "Fuck her against the wall" if the_person.sluttiness >= 70:
            "You don't have the patience to wait any longer, you are going to fuck her right here against the wall."
            if the_person.vagina_available():
                "You quickly pull your cock out and put it in between her legs, getting it into position."
            else:
                "You quickly move away every piece of cloth between you and [the_person.possessive_title]'s cunt."
                $ scene_manager.strip_to_vagina(person = the_person, prefer_half_off = True)
                "You pull your cock out and put it in between her legs, getting it into position."
            $ scene_manager.update_actor(the_person, position = "against_wall")
            $ mc.change_locked_clarity(30)
            "She lifts one leg to give you better access. Your grab her ass with both hands, lifting her up slightly."
            "She looks you right in the eyes as you slowly lower her, your cock sliding inside her. She gasps as you bottom out inside of her."
            #TODO relevant you better pull out / cum inside / knock me up / other appropriate dialogue here.
            $ the_person.change_arousal(20)
            "All she can do is cling to you as you start to fuck her."
            call fuck_person(the_person, start_position = against_wall, private = True, start_object = make_wall(), skip_intro = True, skip_condom = True) from _call_fuck_after_yoga_01
            $ the_person.call_dialogue("sex_review", the_report = _return)

        "Fuck her against the wall (disabled) " if the_person.sluttiness < 70:
            pass
        "Make her service you" if the_person.obedience >= 130:
            "As things are starting to get heated, you slowly back off. You walk over to your desk and sit down at the edge of it, leaving her confused."
            the_person "Sir?"
            "You unzip your pants and take your cock out."
            mc.name "I want you to come take care of this for me."
            if the_person.love < 0:
                the_person "You? What about what I want? I didn't come in here so you could have all the fun."
                mc.name "Shut up, slut. You came in here because you love cock and you know it. If you want to have some fun, then use your pussy. Either way, service me."
                $ the_person.change_stats(obedience = 5, love = -3, slut = 1, max_slut = 50)
                $ mc.change_locked_clarity(20)
                "She looks upset, but you can tell her obedience and her sluttiness are overcoming her reservations."
                the_person "Fine, since you asked so nicely."
                "She spits her last sentence out sarcastically. But it doesn't matter, she starts walking over to you."
                the_person "I'll be damned before I let your cum touch me though."
                call get_fucked(the_person, the_goal = "waste cum") from _after_yoga_hate_fuck_01
            else:
                the_person "Yes [the_person.mc_title]... with my mouth? or?"
                mc.name "You can use your imagination."
                "She smiles as she starts to walk over to you."
                $ mc.change_locked_clarity(20)
                the_person "Okay! I think I can think of a good way to do this..."
                call get_fucked(the_person) from _after_yoga_get_serviced
        "Make her service you (disabled) " if the_person.obedience < 130:
            pass
        "Mess around":
            "You reach down and grab her ass, pulling her close to you. Through your pants, you grind your erection against her mound."
            "Soon, you decide it's time to take things to the next level."
            call fuck_person(the_person, private = True) from _call_fuck_after_yoga_02
    "Finished, you get yourself cleaned up and walk over to your desk."
    $ the_person.apply_outfit(initial_outfit)
    $ initial_outfit = None
    $ the_person.draw_person()
    if the_person == erica:
        the_person "Mmm, that was fun! I guess I'll head to class now..."
    else:
        the_person "I suppose I'll get back to work now..."
    $ the_person.apply_planned_outfit()
    $ the_person.draw_person(position = "walking_away")
    "[the_person.title] puts on her clothes, turns around and opens the door to your office, leaving you to begin your work day properly."
    return

label erica_nude_yoga_office_aftermath_label(): #We use this to describe the state of the lobby after the nude yoga orgy.
    "As the orgy that resulted from the nude yoga class is winding down, you do a quick survey of the lobby."
    "The girls are all winding down. A couple of them are cuddling but most have gotten up and either cleared out or are getting cleaned up."
    "You notice the absolutely undeniable scent of feminine musk in the room. It smells of pussy and sex in the best way possible."
    "You are pretty sure that any employees who weren't at the class this morning will know exactly what happened when they walk in the door."
    "And even if they don't, you're sure that word will get around quick about it."
    return


label erica_lily_instapic_setup_label(the_person):#This should be an event assigned to Lily
    mc.name "Hey sis. I have an idea for your InstaPic channel."
    the_person "Oh? Having a male perspective on the channel is always good!"
    mc.name "I have a friend I recently made at the gym. You might actually know her, she goes to your university too."
    mc.name "She's on the track and field team, but is having some cash flow problems. I was wondering if you would be willing to guest host her on your channel."
    if mom.event_triggers_dict.get("mom_instathot_pic_count",0) > 0:
        mc.name "Something similar to what we've done with mom. You know how things took off with her, right?"
    the_person "What's her name?"
    mc.name "Her name is [erica.fname]."
    "[the_person.title] thinks about it for a minute."
    the_person "I think I know her... We might have had a general class together a year ago?"
    "She's considering it, but you can tell she isn't a big fan of the idea. You might have to sweeten the deal a little bit to get her to agree to it."
    the_person "I think I'm okay with it. But what if it doesn't pull in any extra money? I don't want to have to split the profit if it turns out to be a dud."
    mc.name "Tell you what... For the first session, I'll donate the $100 you normally pay me to run the camera. I'll tell [erica.fname] for the first session it's a straight $100 fee, and if it is successful there may be more opportunities in the future?"
    the_person "Aww, you're gonna let her have your share? You must like this girl!"
    "[the_person.title] starts to tease you, but you also detect a hint of jealousy in her voice."
    the_person "You have a crush on this girl, don't you? Does mom know you're *in love*?"
    mc.name "Hey, she's a good person, just trying to make ends meet. Do we have a deal?"
    the_person "Yeah, we have a deal. You think this will really help my channel?"
    mc.name "Speaking as a guy... Yes... Having two hot college girls dressing up for pics will be perfect!"
    the_person "Good point! Okay, Did you need anything else?"
    $ erica.add_unique_on_room_enter_event(erica_lily_instapic_proposal)

    return

label erica_lily_instapic_proposal_label(the_person): #This should be assigned to Erica
    $ the_person.draw_person()
    "You spot [the_person.possessive_title]. She appears to be in between workout equipment."
    mc.name "I have an idea for something you could do to bring in a little extra money."
    the_person "Oh? What is it?"
    mc.name "My sister, who you may actually know from your classes, runs an InstaPic channel where she makes some extra money modeling clothes."
    the_person "You're not suggesting I make my own InstaPic channel, are you? You know how much work those are?"
    mc.name "No, actually I talked it over with her and thought maybe you could appear as a guest on her channel once in a while."
    the_person "Oh! You mean like, we get together and take pictures of both of us?"
    mc.name "Exactly. She makes pretty good money doing it. I'll be the one taking pictures, and we agreed for your first session she'd pay you a $100 fee, with more opportunities in the future if it goes well."
    the_person "You're taking the pictures? Do you... Always do that for your sister?"
    mc.name "Yeah it's usually me."
    if the_person.get_opinion_score("incest") < 0:
        the_person "I don't know... that's kinda creepy..."
        $ the_person.change_love(-3)
    elif the_person.get_opinion_score("incest") > 0:
        the_person "That's awful nice of you! You sound like a good big brother!"
        $ the_person.change_love(3)
    the_person "What was your sister's name?"
    mc.name "It's [lily.fname]. She said she thinks you might have had a class together once."
    "She wrinkles her nose as she tries to remember. It's kind of a cute look for her."
    the_person "I think I remember her... She seemed pretty nice. Kinda chatty?"
    mc.name "That's her."
    the_person "Okay... But you can't use my name or anything! I'm not sure I'm supposed to do stuff like that while I'm on a college sports team."
    mc.name "Yeah, [lily.fname] doesn't use any personally identifying info in the channel."
    the_person "Oh god... Okay! I'll try it! My schedule is pretty busy right now... Maybe this weekend? Saturday night?"
    mc.name "Okay. I'll text you my address. I'll give [lily.fname] your contact info also. She might need your clothes sizes."
    the_person "Alright. I'll see you on Saturday!"
    "You let [the_person.possessive_title] get back to her workout. You text [lily.title] about [the_person.title]'s info. You can't wait to snap some sexy pics of the duo!"
    $ mc.business.add_mandatory_crisis(erica_lily_instapic_intro)
    return

label erica_lily_instapic_intro_label():
    if not lily.is_available or not erica.is_available:
        return
    $ erica.event_triggers_dict["insta_pic_intro_complete"] = True
    $ scene_manager = Scene() #Clean Scene

    "It's Saturday evening, which means it's time for a sexy photo shoot with [lily.title] and [erica.title]! You head home and knock on [lily.possessive_title]'s door. She swings it open."
    $ lily_bedroom.show_background()
    $ scene_manager.add_actor(lily)
    lily "Hey, any word from your friend?"
    mc.name "Not yet."
    lily "Are you sure she's gonna make it? I teased on my channel that I have a surprise for them tonight. It's gonna be hard to come up with something if she doesn't show up!"
    mc.name "She'll be here."
    "You chat with [lily.possessive_title] for a bit. Soon you feel a vibration in your pocket as your phone goes off."
    erica "I'm here! Come let me in!"
    $ scene_manager.clear_scene()
    $ hall.show_background()
    "You go to your front door and open it. [erica.title] gives you a nervous smile as she steps inside."
    $ scene_manager.add_actor(erica)
    erica "Sorry I'm late. I almost didn't come... This whole thing is just a little... crazier than anything I would normally do."
    mc.name "Don't worry, [lily.title] is great at this. I was pretty skeptical about it at first too, but she's been pretty successful with this."
    "You lead her to [lily.possessive_title]'s room. As she steps in, you see the two girls make eye contact. Recognition dawns on both of their faces."
    $ lily_bedroom.show_background()
    $ scene_manager.add_actor(lily, display_transform = character_center_flipped)
    lily "Oh my gosh... [erica.fname]? I totally remember you! You were in my psych class! You sat next to that girl that kept flirting with the professor!"
    erica "Ah! Yes I remember you now! You were at the study group for the midterm!"
    lily "I never realized you were on the track team! But God, I can tell now! You look amazing! No wonder my brother is crushing on you."
    erica "Aww, thank you!... Wait, your brother what?"
    mc.name "[lily.title], let's not..."
    lily "He's totally into you. Did he tell how much the fee was for today?"
    erica "He just said $100..."
    mc.name "[lily.title], could you not do this right now..."
    lily "Yeah! That's totally his normal cameraman fee. He offered to donate it to you to help you out!"
    "[erica.possessive_title] looks at you, surprise on her face."
    erica "[erica.mc_title]... Is that true?"
    mc.name "Well... yeah... I mean, about where the fee is coming from. I just want everyone here to be successful. This is gonna be great for both of you, and there's no strings attached to the money."
    $ erica.change_love(3)
    "[erica.title] smirks at you."
    erica "I see. Well, I'm here now! We should get started."
    lily "Right! Let me show you what I got for us for tonight!"
    "The girls start to chat as [lily.title] pulls out a few outfits. You are glad that they seem to be hitting it off so well... But also a little fearful. [lily.possessive_title] seems to be enjoying this a little TOO much."
    "After a bit, [lily.title] moves to get things started."
    lily "Alright, let's go with these!"
    # todo start stripping
    $ scene_manager.strip_full_outfit(person = lily, strip_feet = True)
    "[lily.title] starts to take her clothes off, surprising [erica.title]."
    erica "Whoa, like, right here? In front of him?"
    "[erica.possessive_title] seems a little unsure."
    lily "It's okay, he doesn't mind!"
    "She starts to protest again, but [lily.title] continues to strip down. Soon she decides to just follow her and starts to strip also."
    $ scene_manager.strip_full_outfit(person = erica, strip_feet = True)
    if erica.has_taboo(["bare_pussy", "bare_tits"]):
        "[erica.title] uses her hands to try and cover herself up after she finishes stripping down. She looks at you and blushes."
        $ erica.break_taboo("bare_pussy")
        $ erica.break_taboo("bare_tits")

    "When they finish, [lily.title] hands her the outfit. They both quickly get dressed. The outfits look great."
    $ lily.apply_outfit(insta_wardrobe.pick_random_outfit(), update_taboo = True)
    $ erica.apply_outfit(erica.personalize_outfit(insta_wardrobe.pick_random_outfit(), coloured_underwear = True, max_alterations = 2, allow_skimpy = False), update_taboo = True)
    $ scene_manager.update_actor(lily)
    $ scene_manager.update_actor(erica)
    $ mc.change_locked_clarity(25)
    erica "It's... A little skimpy, don't you think?"
    lily "That's the point! A little showy, but leave the guys thirsty and they'll come back again and again!"
    "[erica.possessive_title] looks at you. At first, you see uncertainty in her eyes, but then your eyes meet. You can almost see her confidence return when she observes your reaction."
    erica "What do you think, [erica.mc_title]? Will this bring in lots of views?"
    $ scene_manager.update_actor(erica, position = "back_peek")
    "[erica.title] turns and gives you a good look at her back side. There's a large lump in your throat as you try to reply."
    mc.name "I mean... I can only speak for myself, and I would check it out..."
    $ erica.change_stats(happiness = 3, love = 2, slut = 1, max_slut = 30)
    lily "Oh god, look at him! His brain cells can barely respond! You gonna be able to take these pictures [lily.mc_title]?"
    $ scene_manager.update_actor(erica, position = "stand3")
    mc.name "Yeah, of course, I got this."
    erica "Ok... how do we start?"
    lily "It's easy! Just follow my lead."
    "[lily.possessive_title] hops up on her bed and gets down on her knees in a seductive pose."
    $ scene_manager.update_actor(lily, position = "kneeling1", emotion = "happy")
    "She pats the bed next to her, and soon [erica.title] is awkwardly climbing up next to her."
    $ scene_manager.update_actor(erica, position = "kneeling1", emotion = "happy")
    $ mc.change_locked_clarity(25)
    lily "That's it. Just relax! You're so tense."
    erica "Sorry... I've just never done anything like this before."
    lily "I know, just look over at the dumb goofy face my brother is giving us right now."
    "[erica.possessive_title] looks over at you, and her smile goes from obviously forced to much more genuine."
    lily "Heyyyyy, that's it! Just pretend like we're not even taking pictures... you're just posing for [lily.mc_title]!"
    "[lily.title] turns to you and you start taking pictures. It isn't long until [erica.title] gets the hang of it."
    $ scene_manager.update_actor(lily, position = "back_peek", emotion = "happy")
    $ scene_manager.update_actor(erica, position = "stand4", emotion = "happy")
    $ mc.change_locked_clarity(25)
    "You fit in a couple different poses, but all throughout [erica.possessive_title] watches your reactions closely."
    $ scene_manager.update_actor(lily, position = "missionary", emotion = "happy")
    $ scene_manager.update_actor(erica, position = "missionary", emotion = "happy")
    "For the final set of pics you capture them laying in bed next to each other. It is undeniably sexy."
    mc.name "Alright, I think we've got all the shots we need."
    $ scene_manager.update_actor(erica, position = "stand2", emotion = "happy")
    "[erica.title] stands up."
    erica "That was actually really fun... Do you think the pictures will make any money?"
    mc.name "Definitely."
    $ scene_manager.update_actor(lily, position = "stand3", emotion = "happy")
    "[lily.title] gives [erica.title] money as payment for the session."
    lily "Now, the question is, are you up for doing this again?"
    erica "I'm not sure... I had fun tonight, but I need to think about it."
    "[erica.possessive_title] quickly changes back into her regular clothes. You do your best not to make it obvious you are watching..."
    $ scene_manager.strip_full_outfit(person = erica, strip_feet = True)
    "She looks over and gives you a little smirk."
    $ mc.change_locked_clarity(15)
    $ erica.apply_planned_outfit()
    $ scene_manager.update_actor(erica, position = "stand2", emotion = "happy")
    erica "Alright, well I have to get up early tomorrow for track practice, so I'd better get going."
    lily "See you soon!"
    $ scene_manager.remove_actor(lily)
    $ hall.show_background()
    "You walk with [erica.possessive_title] to the front door. When you get there, she turns to you and gives you a big hug."
    $ scene_manager.update_actor(erica, position = "kissing")
    "She gives you a quick kiss, then turns and leaves."
    $ scene_manager.remove_actor(erica)
    $ mc.change_location(bedroom)
    $ mc.location.show_background()
    "You turn around and walk to your room. Damn... what a hot photo session!"
    "You should wait a couple days, then talk to [lily.title] and see how the pics did..."
    $ lily.add_unique_on_talk_event(erica_lily_post_photoshoot)
    return

label erica_lily_post_photoshoot_label(the_person):
    the_person "[the_person.mc_title]! You won't believe it."
    mc.name "Yeah?"
    the_person "My follower count went up almost FORTY PERCENT from the pics we did with [erica.fname] the other night!"
    mc.name "Wow, that's great!"
    the_person "I know! I'm already getting all kinds of requests from people. You HAVE to convince her to do it again, okay?"
    the_person "Do you think we could make this a regular thing? Every Saturday night?"
    mc.name "I mean, that is kind of up to her, but I'll do what I can..."
    the_person "Don't take no for an answer! I know you can do it bro! Tell her I'll double her fee!"
    "Sounds like you should probably talk to [erica.possessive_title] about doing more InstaPics..."
    $ erica.add_unique_on_room_enter_event(erica_post_photoshoot)
    return

label erica_post_photoshoot_label(the_person):
    $ the_person.draw_person(position = "walking_away")
    "[erica.possessive_title] is pushing herself hard on the treadmill as you walk up to her."
    mc.name "Hey, I've got good news."
    the_person "Oh hey [the_person.mc_title]! What's the good news?"
    mc.name "It's my sister. She said the photos were a huge success and she wants to know if you can take more photos."
    the_person "Oh! Were they really? I wasn't sure that whole thing was going to work out."
    mc.name "Apparently they turned out great. She wants to know if you want to meet up every Saturday night from here on out, and offered to double your fee."
    the_person "Holy shit... one second..."
    "[the_person.title] turns off the treadmill and hops off so she can talk to you better."
    $ the_person.draw_person(position = "stand2")
    the_person "That's $200 per session? That would be amazing!"
    mc.name "So I'll tell her you'll be there?"
    the_person "Are you going to be the one taking all the pictures?"
    mc.name "I'll do my best, but I won't necessarily be able to do it every week. Don't worry, [lily.title] has a pretty good tripod she invested in recently."
    the_person "Okay. I'll do it! But just so you know, it would really mean a lot to me if you were the one there taking pictures. I don't know why, but having you there made it a lot easier."
    mc.name "If I'm not busy, I'll be there."
    the_person "Wow! Okay. This is going to be a huge change for me."
    $ the_person.change_stats(happiness = 3, love = 3)
    the_person "[the_person.mc_title]... I really appreciate this. I owe you so many favors at this point."
    mc.name "Nonsense. I'm just glad to see you reach your potential. Plus... the pics ARE really hot."
    "[the_person.title] gives you a playful punch on the shoulder."
    the_person "Was there anything else you needed?"
    $ the_person.set_override_schedule(lily_bedroom, the_days = [5], the_times = [4])
    $ lily.set_override_schedule(lily_bedroom, the_days = [5], the_times = [4]) #This should already be set, but just in case, make sure she is there.
    $ erica.add_unique_on_room_enter_event(erica_pre_insta_love)
    $ erica.add_unique_on_room_enter_event(erica_lily_weekly_photoshoot)
    $ erica.event_triggers_dict["insta_pic_intro_complete"] = True
    return

label erica_lily_weekly_photoshoot_label(the_person):
    if not lily.is_available or not erica.is_available:
        return
    $ scene_manager = Scene()
    $ lily_insta_outfit = insta_wardrobe.pick_random_outfit()
    $ mc.change_location(lily_bedroom)
    $ mc.location.show_background()
    "You walk down the hall toward [lily.possessive_title]'s room. As you approach her door, you can hear laughter and giggling from the other side."
    "Sounds like [erica.title] is already here! You knock on the door."
    lily "Come in!"
    $ scene_manager.add_actor(lily, display_transform = character_center_flipped, position = "back_peek")
    $ scene_manager.add_actor(erica, position = "back_peek")
    "As you open the door, the two girls are standing in front of [lily.title]'s closet, looking back at you."
    lily "Oh hey [lily.mc_title]. Good timing! We were just picking out what to wear for tonights photos!"
    erica "[lily.fname] thinks we should match, but I was thinking about just wearing something else. What do you think?"
    "It's clear the your opinion is important to her. You think about it for a moment."
    menu:
        "You should match":
            $ erica_insta_outfit = lily_insta_outfit.get_copy()
        "You should wear something similar, but not matching":
            $ erica_insta_outfit = erica.personalize_outfit(lily_insta_outfit.get_copy(), allow_skimpy = False)
        "You should wear your own thing":
            $ erica_insta_outfit = erica.personalize_outfit(insta_wardrobe.pick_random_outfit(), allow_skimpy = False)
    erica "Thanks! I'm still pretty new at this, so it's nice to have your opinion on it."
    $ erica.change_stats(happiness = 1, obedience = 1)
    lily "Alright, before we get going, I need to grab a soda or something. I'm parched!"
    erica "Yeah, me too. Do you have any flavored seltzers?"
    "You think for a second. You could offer to go get them their drinks, and that would give you an opportunity to give them a serum..."
    "If you do, you will probably miss the chance to watch them change..."
    menu:
        "Grab the drinks":
            mc.name "Yeah we have seltzer. Let me go grab drinks for everyone while you two get changed."
            erica "Thanks! Lots of ice with mine please!"
            lily "Me too. You're gonna like the outfits we got for this week bro!"
            $ scene_manager.clear_scene()
            "You step out of [lily.possessive_title]'s room and head to the kitchen."
            $ mc.change_location(kitchen)
            $ mc.location.show_background()
            "First, you make a glass with lots of ice for [erica.title]..."
            menu:
                "Add serum to [erica.title]'s drink" if mc.inventory.get_any_serum_count() > 0:
                    call give_serum(erica) from _call_give_serum_erica_insta_20
                    if _return:
                        "You add a dose to her drink, then top it off with seltzer."
                    else:
                        "You think about adding a dose of serum to her drink, but decide against it."

                "Add serum to [erica.title]'s drink\n{color=#ff0000}{size=18}Requires: Serum{/size}{/color} (disabled)" if mc.inventory.get_any_serum_count() == 0:
                    pass

                "Leave her drink alone":
                    "You top it off with seltzer."
            "Next, you grab another glass for [lily.title] and a soda."
            menu:
                "Add serum to [lily.title]'s drink" if mc.inventory.get_any_serum_count() > 0:
                    call give_serum(lily) from _call_give_serum_lily_insta_20
                    if _return:
                        "You add a dose to her drink, then top it off with soda."
                    else:
                        "You think about adding a dose of serum to her drink, but decide against it."

                "Add serum to [lily.title]'s drink\n{color=#ff0000}{size=18}Requires: Serum{/size}{/color} (disabled)" if mc.inventory.get_any_serum_count() == 0:
                    pass

                "Leave her drink alone":
                    "You top it off with soda."
            "You pick up both drinks and walk back down the hall to [lily.title]'s room. You open the door and step inside."
            $ mc.change_location(lily_bedroom)
            $ mc.location.show_background()
            $ lily.apply_outfit(lily_insta_outfit, update_taboo = True)
            $ erica.apply_outfit(erica_insta_outfit, update_taboo = True)
            $ scene_manager.add_actor(lily, display_transform = character_center_flipped)
            $ scene_manager.add_actor(erica)
            $ mc.change_locked_clarity(25)
            "When you step into the room, you see the girls are both dressed and ready for their photoshoot."
        "Watch them strip":
            lily "Yeah, we have seltzer I think. Let me go grab drinks."
            $ scene_manager.remove_actor(lily)
            "[lily.possessive_title] leaves the room, leaving you for a minute with [erica.title]."
            #TODO small talk?
            "You make a little bit of awkward small talk until she gets back."
            $ scene_manager.add_actor(lily, display_transform = character_center_flipped)
            lily "Alright, let's get ready!"
            "The girls start to strip down."
            $ scene_manager.strip_full_outfit(strip_feet = True) # strip both simultaneously
            $ mc.change_locked_clarity(40)
            "[erica.possessive_title] gives you a sly smile before she starts putting on her outfit."
            $ erica.change_stats(happiness = 2, slut = 2, max_slut = 30)
            $ lily.apply_outfit(lily_insta_outfit, update_taboo = True)
            $ erica.apply_outfit(erica_insta_outfit, update_taboo = True)
            $ scene_manager.update_actor(lily)
            $ scene_manager.update_actor(erica)
            $ mc.change_locked_clarity(20)
            "Once they get dressed, the girls are ready for their photoshoot."
    $ erica_insta_pose_pairs = erica_make_insta_pose_pairs()
    $ current_pos = get_random_from_list(erica_insta_pose_pairs)
    $ erica_insta_pose_pairs.remove(current_pos)
    $ scene_manager.update_actor(lily, position = current_pos[0], emotion = "happy")
    $ scene_manager.update_actor(erica, position = current_pos[1], emotion = "happy")
    "You snap the first round of pictures."
    if (erica.sluttiness > 20 and lily.sluttiness > 20):
        "The girls seem relaxed. The pictures are coming out natural and they look great together."
        $ mc.change_locked_clarity(10)
        mc.name "Alright, let's do another set, these are great."
        $ current_pos = get_random_from_list(erica_insta_pose_pairs)
        $ erica_insta_pose_pairs.remove(current_pos)
        $ scene_manager.update_actor(lily, position = current_pos[0], emotion = "happy")
        $ scene_manager.update_actor(erica, position = current_pos[1], emotion = "happy")
        "You snap the second round of pictures"
        if (erica.sluttiness > 40 and lily.sluttiness > 40):
            mc.name "That looks great. Remember, be playful!"
            "[current_pos[2]!i]"
            $ mc.change_locked_clarity(30)
            mc.name "Nice, these are great. How about one more set?"
            "The girls agree and get into a new position."
            $ current_pos = get_random_from_list(erica_insta_pose_pairs)
            $ erica_insta_pose_pairs.remove(current_pos)
            $ scene_manager.update_actor(lily, position = current_pos[0], emotion = "happy")
            $ scene_manager.update_actor(erica, position = current_pos[1], emotion = "happy")
            if (erica.sluttiness > 60 and lily.sluttiness > 60):
                mc.name "Remember, these are for the thirsty InstaPic boys. Work it for the camera!"
                "[current_pos[3]!i]"
                $ mc.change_locked_clarity(50)
            else:
                "You snap the final set of pictures. This should be good!"
        else:
            "You snap a second set of pictures. This should be good!"
    else:
        "As you snap the first set of pictures, it is clear that girls are faking the smiles and the pictures are looking unnatural."
        mc.name "I'm not sure this is going to do it. Maybe we should try a different pose?"
        $ current_pos = get_random_from_list(erica_insta_pose_pairs)
        $ scene_manager.update_actor(lily, position = current_pos[0], emotion = "happy")
        $ scene_manager.update_actor(erica, position = current_pos[1], emotion = "happy")
        "The girls get into a second pose, but the pictures still feel a little mechanical."
        "They look okay, but you wonder if they could do even better if you could loosen them up a bit more."
    $ scene_manager.update_actor(lily, position = lily.idle_pose)
    $ scene_manager.update_actor(erica, position = erica.idle_pose)
    #TODO special requests. IE topless, kissing, etc.
    #TODO add outfits to wardrobes if they like them.
    #TODO add new outfits?
    "With the pictures done, you give the camera back to [lily.possessive_title]."
    lily "Thanks, [lily.mc_title]! You're the best!"
    erica "Yeah, thanks, [erica.mc_title]. [lily.fname] is it still okay if I spend the night?"
    lily "Of course! I could really use your help studying for my exam coming up."
    "You wish you could come up with a good excuse to stick around, but can't think of anything, so you say goodnight."
    $ scene_manager.clear_scene()
    if erica.sluttiness > 20 and erica.event_triggers_dict.get("post_insta_handy", False) == False:
        $ mc.business.add_mandatory_morning_crisis(erica_lily_post_insta_handjob)
    elif erica_get_morning_wakeup_pref() == 2 or (erica_get_morning_wakeup_pref() == 1 and renpy.random.randint(0,2) == 1):
        # make sure we add this if it's not already present
        $ mc.business.add_mandatory_morning_crisis(erica_lily_post_insta_morning_mand)

    $ erica.add_unique_on_room_enter_event(erica_lily_weekly_photoshoot)
    $ del lily_insta_outfit
    $ del erica_insta_outfit
    $ del current_pos
    $ del erica_insta_pose_pairs
    call advance_time(no_events = False) from _call_advance_time_erica_insta_night_01
    return

label erica_lily_post_insta_handjob_label():
    $ the_person = erica
    $ mc.change_location(bedroom) # switch to mc bedroom
    $ mc.location.show_background()
    $ mc.location.lighting_conditions = dark_lighting
    $ erica.event_triggers_dict["post_insta_handy"] = True
    "You hear the door to your room slowly open, slowly waking you up."
    $ the_person.draw_person()
    "A figure appears in your door. Is that [the_person.possessive_title]? She slowly makes her way over to your bed, then sits on the side of it."
    $ the_person.draw_person(position = "sitting")
    mc.name "[the_person.title]? Is that you? What time is it?"
    the_person "Yeah, it's me. I am just getting ready to head out for an early morning run. It's 5 am."
    mc.name "Wow. Your commitment to fitness is amazing, you know that?"
    "She chuckles before responding."
    the_person "Thank you. I was just going to head out, but I wanted to come in and say thank you, for setting me up with [lily.fname] and the InstaPic stuff..."
    mc.name "It's fine, you don't have to come in at 5am to tell me that though."
    the_person "I know, but I wanted to make sure I had you alone for what I want to do to show you how thankful I am..."
    "Over your blankets, [the_person.title] reaches over and puts her hand on your chest, then starts to slide it down your body."
    "When she gets to your morning wood, she starts to stroke it."
    $ mc.change_locked_clarity(20)
    "Your sleep addled brain only lets you moan as she starts to work it."
    the_person "Can you pull your blanket down?"
    "You pull your blanket down and your shorts. When your cock springs free, she takes it in her hand and starts stroking it again."
    "Her hands feel soft and warm."
    if the_person.has_taboo("touching_penis"):
        the_person "I know I've never really been this forward with you before..."
        the_person "But when I was trying to come up with a way to say thanks, this was the best way I could think of."
        mc.name "This is great, but I'm a little tired to reciprocate..."
        the_person "That's okay! Just lay back and let me take care of it."
        $ the_person.break_taboo("touching_penis")
    else:
        mc.name "This is great, but I'm pretty tired. I'm not sure I'll be able to reciprocate."
        the_person "Don't worry, I just want to take care of this for you!"
    "You lay back in your bed and just enjoy it as [the_person.possessive_title] starts to give you a handjob."
    call get_fucked(the_person, start_position = cowgirl_handjob, the_goal = "get mc off", private = True, skip_intro = True, allow_continue = False) from _erica_first_handjob_01
    "[the_person.possessive_title] slowly gets up after you finish."
    the_person "Take care [the_person.mc_title]. I'll see you soon!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.title] quietly leaves your room and you quickly fall back asleep."
    $ clear_scene()
    "You wake up a few hours later. Did [the_person.possessive_title] really come in your room in the middle of the night? Or was that just a dream?"
    $ the_person.add_unique_on_talk_event(erica_post_insta_handjob_followup)
    $ mc.location.lighting_conditions = standard_indoor_lighting
    return

label erica_lily_post_insta_morning_label():
    $ the_person = erica
    if erica_get_morning_wakeup_pref() == 0:
        return
    if the_person.sex_record.get("Last Sex Day", 9999) == day: #If mandatory and random crisis happen to fire on the same day, suppress the second event.
        return

    $ mc.change_location(bedroom) # switch to mc bedroom
    $ mc.location.show_background()
    $ mc.location.lighting_conditions = dark_lighting
    $ option_list = erica_get_wakeup_options()
    "You hear the door to your room slowly open, waking you up."
    $ the_person.draw_person()
    "A figure appears in your door. It's [the_person.possessive_title] again. She tip toes over to your bed, then sits on the side of it."
    $ the_person.draw_person(position = "sitting")
    "Hearing you stir, she leans down and whispers in your ear."
    the_person "Good morning."
    mc.name "Mmm, it's just regular morning right now, but I have a feeling it is about to get good."
    "She chuckles as she reaches down your body and grabs your morning wood through your blankets. She starts to stroke it."
    if the_person.is_willing(drysex_cowgirl) and "drysex" not in option_list:
        the_person "Mmm, it's so hard..."
        "Her voice trails off as she strokes you a few more times."
        the_person "I kind of just want to feel it up against me... do you mind?"
        mc.name "Go ahead."
        "You pull down your blanket, but she leaves your underwear on you as she climbs up on top of you."
        $ the_person.draw_person(position = "cowgirl")
        "As she settles into place, she starts to rub her crotch up against yours."
        "The friction of your clothes and her body rubbing against you feels good, and soon there is a significant amount of heat coming from her crotch that makes it feel even better."
        $ the_person.change_arousal(20)
        $ mc.change_arousal(20)
        $ the_person.break_taboo("touching_body")
        call get_fucked(the_person, start_position = drysex_cowgirl, the_goal = "get mc off", private = True, skip_intro = True, allow_continue = False) from _erica_morning_drysex_01
        $ erica_get_wakeup_options().append("drysex")
        $ the_person.apply_planned_outfit()
        $ the_person.change_slut(1, 40)
        "When she finishes, [the_person.possessive_title] gets up and straightens up her outfit."
        the_person "Thanks, that was nice. I'll see you soon [the_person.mc_title]."
        $ the_person.draw_person(position = "walking_away")
        "[the_person.title] quietly leaves your room and you quickly fall back asleep."
        $ clear_scene()
        $ mc.location.lighting_conditions = standard_indoor_lighting
        return

    if the_person.is_willing(cowgirl_blowjob) and "blowjob" not in option_list:
        the_person "Mmm, it's so hard..."
        "Her voice trails off as she strokes you a few more times."
        the_person "You know, I usually take a protein supplement before I workout, but I don't have any with me..."
        the_person "Do you think you could donate some?"
        mc.name "Hmm, well I suppose if it's for a good cause..."
        "You pull your blanket down and your shorts. When your cock springs free, she takes it in her hand and starts stroking it again."
        $ the_person.draw_person(position = "blowjob")
        "[the_person.title] lowers herself down your body until you feel her warm breath on your crotch. She opens her mouth and licks your pre-cum from the tip."
        the_person "Mmm, you taste better than those protein powders too..."
        "Opening her mouth, she slides her wet lips down over the tip and runs her tongue all up and down it a few times."
        "You run your hand thru her hair as she begins to suck you off."
        $ the_person.break_taboo("sucking_cock")
        $ mc.change_arousal(20)
        call get_fucked(the_person, start_position = cowgirl_blowjob, the_goal = "oral creampie", private = True, skip_intro = True, allow_continue = False) from _erica_morning_blowjob_01
        $ erica_get_wakeup_options().append("blowjob")
        $ the_person.apply_planned_outfit()
        $ the_person.change_slut(1, 60)
        "When she finishes swallowing, [the_person.possessive_title] gets up and straightens up her outfit."
        the_person "Thanks for the protein... I'll see you later [the_person.mc_title]."
        $ the_person.draw_person(position = "walking_away")
        "[the_person.title] quietly leaves your room and you quickly fall back asleep."
        $ clear_scene()
        $ mc.location.lighting_conditions = standard_indoor_lighting
        return

    if willing_to_threesome(the_person, lily) and "threesome" not in option_list:
        the_person "God, you are so hard this morning. I need to feel it in me... can I put it in me?"
        mc.name "Of course."
        "As you pull down your blankets and shorts, [the_person.title] gets naked."
        $ the_person.strip_outfit(position = "stand4")
        the_person "Mmm, I can't wait!"
        mc.name "Shhh, you'll wake..."
        $ the_person.draw_person(position = "cowgirl")
        "[the_person.possessive_title] jumps on top of you. She grabs your cock, points it towards her hungry cunt, then sits down on it."
        the_person "Mmmm, oh fuck..."
        $ the_person.change_arousal(20)
        $ mc.change_arousal(10)
        the_person "Sorry, I couldn't help it. Taking all those sexy photos last night for all the thirsty guys out there, when the only one I want to fuck was just in the next bedroom over..."
        "[the_person.title] starts to ride you pretty aggressively. You lay back and enjoy it."
        #Swap to scene manager because I was too lazy to do it earlier.
        $ scene_manager = Scene()
        "You close your eyes, just enjoying the sensations. However, an out of place gasp causes you to open your eyes."
        $ scene_manager.add_actor(the_person, position = "cowgirl")
        $ scene_manager.add_actor(lily, display_transform = character_left_flipped(zoom = 0.7))
        "When you open your eyes, you see another figure in your doorway. Is that [lily.possessive_title]?"
        $ scene_manager.update_actor(lily,display_transform = character_left_flipped(zoom = 1.0))
        "She steps into your room."
        lily "Ah, here you are [erica.fname]. I guess I should have known you would sneak in here."
        "[the_person.title] suddenly stops rocking her hips."
        the_person "[lily.fname]? Oh my..."
        lily "You guys are going to wake up mom if you aren't careful, but now that I'm up, can I join you?"
        the_person "You want to join... us?"
        lily "Sure, you just keep doing what you are doing, I'm sure I can put [lily.mc_title]'s tongue to good use."
        "[the_person.title] looks at you, unsure."
        mc.name "Sounds good to me, but like you said, keep it down, we don't want to wake mom up..."
        if mc.business.event_triggers_dict.get("family_threesome", False) == True:
            mc.name "I'm not sure I have the stamina to satisfy all three of you..."
            "[the_person.possessive_title] gasps at your joke."
            the_person "Ha... that's... funny... right?"
            lily "Yeah, he's totally just joking."
        "[lily.title] starts to strip as [the_person.possessive_title] starts moving her hips again."
        $ scene_manager.strip_full_outfit(person = lily)
        "When she finishes, [lily.possessive_title] swings her legs up over your head and brings her pussy to your face."
        call start_threesome(the_person,lily, start_position = Threesome_double_down) from _erica_wakeup_threesome_01
        $ erica_get_wakeup_options().append("threesome")
        $ scene_manager.update_actor(the_person, position = "back_peek", display_transform = character_center_flipped)
        $ scene_manager.update_actor(lily, position = "missionary", display_transform = character_right)
        $ the_report = _return
        if the_report.get("girl one orgasms", 0) > 0 and the_report.get("girl two orgasms", 0) > 0 and the_report.get("guy orgasms", 0) > 0: #Happy family
            $ the_person.change_slut(2, 100)
            $ lily.change_slut(2, 100)
            "[the_person.possessive_title] falls into your bed on one side of you on her side, while [lily.title] lays on her back next to you."
            "You actually start to fall asleep, enjoying the afterglow of your collective orgasms, until you feel [the_person.title] stir."
        else:
            $ the_person.change_slut(1, 100)
            $ lily.change_slut(1, 100)
            "The girls fall into your bed beside you. You relax for a little bit, enjoying the warmth of their bodies."
        the_person "I think I'm going to take it easy during my workout this morning... you two about wore me out."
        lily "God I know, I think I'm gonna go back to bed..."
        the_person "Next Saturday then [lily.fname]?"
        lily "Of course, and if you're gonna sneak into my brother's room let me know next time okay?"
        the_person "Mmm, maybe. I might want him all to myself though..."
        $ scene_manager.clear_scene()
        "The two girls get up. You fall asleep as they slip out of your room."
        $ mc.location.lighting_conditions = standard_indoor_lighting
        return


    the_person "So, up for anything in particular today?"
    $ position_choice = erica_wakeup_choose_position()
    if position_choice == "Surprise me":
        the_person "Mmmm, okay."
        $ mc.change_arousal(20)
        $ the_person.change_stats(happiness = 5, obedience = -5)
        $ position_choice = get_random_from_list(erica_get_wakeup_options())

    if position_choice == "handjob":
        the_person "I don't know why, I just love the feeling of your thick cock in my hand..."
        "You pull your blanket down and your shorts. When your cock springs free, she takes it in her hand and starts stroking it again."
        the_person "God it's so warm..."
        "[the_person.possessive_title] doesn't waste any time and starts stroking you off."
        call get_fucked(the_person, start_position = cowgirl_handjob, the_goal = "get mc off", private = True, skip_intro = True, allow_continue = False) from _erica_wakeup_handjob_02
        $ the_person.change_slut(1, 40)
    elif position_choice == "drysex":
        the_person "It's so big, I want to feel it against me."
        "You pull your blanket down as [the_person.possessive_title] climbs on top of you."
        $ the_person.draw_person(position = "cowgirl")
        "She gets into position and starts to grind up against you. The friction of your clothes and her body feels great."
        call get_fucked(the_person, start_position = drysex_cowgirl, the_goal = "get mc off", private = True, skip_intro = True, allow_continue = False) from _erica_morning_drysex_02
    elif position_choice == "blowjob":
        the_person "Let me have a dose of your protein before I go work out."
        "You pull your blanket down and your shorts. When your cock springs free, she takes it in her hand and starts stroking it again."
        $ the_person.draw_person(position = "blowjob")
        "She moves her head down to your crotch and licks your pre-cum from the tip."
        the_person "Mmm, I should do this every time I need some extra protein... you taste so good."
        "[the_person.possessive_title] opens her mouth and begins to bob her head up and down on your morning wood."
        call get_fucked(the_person, start_position = cowgirl_blowjob, the_goal = "oral creampie", private = True, skip_intro = True, allow_continue = False) from _erica_morning_blowjob_02
        $ the_person.change_slut(1, 60)
    elif position_choice == "anal cowgirl":
        the_person "Mmm, that sounds amazing. But try to be gentle, okay? I still want to go for a run today."
        mc.name "Hey, you're the one who will need to be gentle then, you're the one on top!"
        "[the_person.possessive_title] stands up and starts to strip down."
        $ the_person.strip_outfit(position = "stand4")
        "While she strips, you pull the blanket down and take your shorts off."
        "When she finishes stripping, she gets on top of you, takes your cock in her hand and brings her face down to it."
        $ the_person.draw_person(position = "blowjob")
        "[the_person.title] opens her mouth and licks your morning wood up and down several times, slathering it in her saliva."
        the_person "Mmm, you taste so good..."
        "[the_person.possessive_title] opens her mouth and gives you a couple strokes with her mouth before stopping."
        the_person "God, I could keep going, but it's time to put this someplace a little more fun..."
        $ the_person.draw_person(position = "cowgirl")
        "She climbs on top of you, and with one hand she points your erection up at her puckered hole."
        "She lowers herself gently, but easily takes your hardness into her well trained back passage."
        the_person "Ahhh! Oh fuck it's so big..."
        "It takes her a moment, but soon [the_person.possessive_title] starts to rock her hips. Time to fuck her silly."
        call get_fucked(the_person, the_goal = "anal creampie", start_position = SB_anal_cowgirl, start_object = make_bed(), allow_continue = False) from _anal_fetish_erica_morning_wakeup_01
        $ the_person.change_slut(2, 100)
    elif position_choice == "threesome":
        the_person "I'll go get [lily.fname]. She DID say to let her know when I sneak back in anyway..."
        $ clear_scene
        "[the_person.possessive_title] leaves the room. A minute later, she returns with [lily.title] following her."
        $ scene_manager = Scene()
        $ scene_manager.add_actor(the_person)
        $ scene_manager.add_actor(lily, display_transform = character_center_flipped)
        lily "*Yawn* Mmm, I should have known you two would be up to shenanigans again."
        "You pull your blanket down as the two girls get naked."
        $ scene_manager.strip_full_outfit()
        "You can only stare in awe at the two sexy college coeds who are naked, in your room, and ready for a threesome."
        lily "Mmm, I'm too tired to think. [lily.mc_title], how do you want us?"
        call start_threesome(lily, the_person) from _threesome_erica_wakeup_02
        $ scene_manager.update_actor(lily, position = "back_peek", display_transform = character_center_flipped)
        $ scene_manager.update_actor(the_person, position = "missionary", display_transform = character_right)
        $ the_report = _return
        if the_report.get("girl one orgasms", 0) > 0 and the_report.get("girl two orgasms", 0) > 0 and the_report.get("guy orgasms", 0) > 0: #Happy family
            $ the_person.change_slut(2, 100)
            $ lily.change_slut(2, 100)
            "[lily.possessive_title] falls into your bed on one side of you on her side, while [the_person.title] lays on her back next to you."
            mc.name "God you two are so hot. I must be the luckiest man alive."
            the_person "Mmm, and don't you forget it."
            if the_person.is_girlfriend():
                the_person "Not many girls would be okay with their boyfriend banging their sister..."
                $ the_person.change_love(2)
        else:
            "The girls fall into your bed beside you. You relax for a little bit, enjoying the warmth of their bodies."
        the_person "I better get up, or I'm going to miss my workout..."
        $ scene_manager.update_actor(the_person, position = "walking_away")
        "[the_person.title] gets up and grabs her clothes. She carries them with her, probably going to change in the bathroom on her way out."
        lily "Goodnight [the_person.fname]! I'd better get back to my room too, as fun as it would be to sleep in here..."
        $ scene_manager.remove_actor(the_person)
        $ scene_manager.update_actor(lily, position = "walking_away", display_transform = character_right)
        "You watch as [lily.possessive_title] gets up and excuses herself, her ass swaying back and forth as she walks away."
        $ scene_manager.remove_actor(lily)
        "You fall back asleep. What an incredible midnight rendezvous..."
        $ mc.location.lighting_conditions = standard_indoor_lighting
        return


    $ the_person.apply_planned_outfit()
    "[the_person.possessive_title] slowly gets up after you finish, straightening up her outfit."
    the_person "Take care [the_person.mc_title]. I'll see you soon!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.title] quietly leaves your room and you quickly fall back asleep."
    $ clear_scene()
    $ mc.location.lighting_conditions = standard_indoor_lighting
    return

label erica_post_insta_handjob_followup_label(the_person):
    the_person "Hey [the_person.mc_title]."
    mc.name "Hey [the_person.title]. You know, I had the craziest dream the other day."
    the_person "Oh?"
    mc.name "Yeah, I had this dream that you came into my room in the middle of the night..."
    the_person "Ah... did this dream have a happy ending?"
    mc.name "Mostly, except it ended with you leaving instead of hopping in bed with me and falling back asleep."
    $ the_person.change_slut(1, 60)
    the_person "Ah, well, that actually wasn't a dream."
    mc.name "Really? I was so tired, I wasn't sure..."
    the_person "Did you... you know... like it?"
    mc.name "Yeah, it was REALLY nice!"
    the_person "Mmm, okay. Maybe I'll do that again next time I come over and spend the night with your sister!"
    mc.name "That would be nice."
    the_person "Did you need something?"
    # continue talk event
    call talk_person(the_person) from _call_talk_person_handjob_followup
    return

label erica_pre_insta_love_label(the_person):
    "You walk down the hall to [lily.possessive_title]'s room, ready to help out with InstaPic."
    "You knock on the door, but are surprised when it is answered by [the_person.possessive_title]."
    $ the_person.draw_person()
    mc.name "Oh! Hey [the_person.title]."
    the_person "Hey! [lily.fname] just left, she is going to pick us up some sushi tonight!"
    mc.name "Oh, that's great. Have her come get me when she gets back and we can start."
    the_person "Ok... why don't you just come in now? Actually I've been meaning to talk to you about something."
    mc.name "Oh, okay. Sure."
    "You step into [lily.title]'s room and close the door behind you. You and [the_person.possessive_title] walk over and sit on the bed."
    $ the_person.draw_person(position = "sitting")
    mc.name "Is something wrong?"
    the_person "No, not at all. The opposite actually."
    the_person "I just wanted to tell you, I really appreciate all the help you have been giving me."
    the_person "I feel like the more I get to know you, the more I like you. You workout with me, helped me pay for classes, even welcomed me into your home."
    if erica_get_is_doing_yoga_sessions():
        the_person "You even welcomed me into your business, teaching yoga to a bunch of really neat ladies."
    the_person "I'm not really sure where everything is going, but I see all the hard work you put into things, and I guess I just want you to know that I notice and appreciate it."
    the_person "Just understand... I'm really busy, right? With school, and track, and everything. I don't have much more time for extracurricular stuff!"
    mc.name "That is very kind of you to say, and don't worry, I understand we can't spend every waking moment together, and I'm okay with that."
    the_person "So... I was thinking, since [lily.fname] is gonna be gone for a bit, maybe I could SHOW you how much I appreciate you!"
    "[the_person.possessive_title] slides down onto the floor on her knees in front of you."
    $ the_person.draw_person(position = "blowjob")
    $ mc.change_locked_clarity(20)
    mc.name "I think I'm supposed to say that you don't have to do this, but I can tell you want to, so I'll say what I'm really thinking."
    mc.name "I can't wait to feel your mouth on me."
    the_person "Mmm, glad to hear it!"
    "[the_person.title] pulls at your zipper then reaches in, fishing out your dick. She gives it a few strokes and smiles up at you."
    if the_person.has_taboo("sucking_cock"):
        the_person "I've been wanting to do this for a while. Mmm, you smell so manly."
        "[the_person.possessive_title] gives the tip a few exploring licks."
        the_person "I guess I'd better get to work... I'm not sure how long [lily.fname] is going to be gone."
        "[the_person.title] opens her mouth. She slides her wet, velvet lips down your erection."
        $ the_person.break_taboo("sucking_cock")
        $ mc.change_locked_clarity(50)
    else:
        the_person "Mmm, you smell so manly. I love the way you taste and the way you feel so hot in my mouth."
        "[the_person.possessive_title] gives the tip a few exploring licks."
        the_person "I guess I'd better get to work... I'm not sure how long [lily.fname] is going to be gone."
        "[the_person.title] opens her mouth. She slides her wet, velvet lips down your erection"
        $ mc.change_locked_clarity(50)
    "[the_person.title] starts to bob her head up and down, eager to satisfy you with her mouth."
    $ mc.change_arousal(10)
    "It's so hot, getting a blowjob from [the_person.possessive_title] while sitting on your sister's bed!"
    call get_fucked(the_person, the_goal = "oral creampie", private= True, start_position = blowjob, skip_intro = True, ignore_taboo = True, allow_continue = False) from _erica_pre_insta_oral_01
    "When you finish, [the_person.possessive_title] quickly starts to straighten up her clothes and wipes the cum from her face."
    $ the_person.apply_planned_outfit()
    $ the_person.draw_person()
    mc.name "[the_person.title]... that was awesome."
    the_person "Mmm, thanks! But you should probably get out before [lily.fname] gets back!"
    the_person "Just go back to your room and pretend like nothing happened."
    mc.name "Should I come back to take pics?"
    the_person "Up to you! Now go!"
    $ clear_scene()
    $ mc.change_location(bedroom)
    $ mc.location.show_background()
    "You clear out of [lily.possessive_title]'s room and head back to yours. Damn, now you feel so tired."
    "Should you go back and take pics? You have a bit to think about it."
    $ erica.event_triggers_dict["pre_insta_blowjob"] = True
    return

label erica_post_yoga_love_label():
    "You head to your office, bringing [the_person.possessive_title] with you. You open the door, walk in, then close and lock it behind you."
    $ ceo_office.show_background()
    the_person "So... what was it you wanted to talk abo... AH!"
    "You quickly grab her and pin her to the wall."
    $ scene_manager.update_actor(the_person, position = "kissing", display_transform = character_right)
    $ mc.change_locked_clarity(20)
    "She wraps her arms around you and you start to make out, your mouths meeting and exploring each other."
    "[the_person.title] moans when she feels your erection pressing against her."
    $ the_person.change_arousal(20)
    # $ initial_outfit = the_person.outfit.get_copy() # store outfit
    mc.name "I'm sorry I couldn't stop staring at you. Watching your sexy body all morning has me so worked up... I need you right now!"
    the_person "Oh god, me too!"
    "You don't have the patience to wait any longer, you are going to fuck her right here against the wall."
    if the_person.vagina_available():
        "You quickly pull your cock out and put it in between her legs, getting it into position."
    else:
        "You quickly move away every piece of cloth between you and [the_person.possessive_title]'s cunt."
        $ scene_manager.strip_to_vagina(person = the_person, prefer_half_off = True)
        "You pull your cock out and put it in between her legs, getting it into position."
    $ scene_manager.update_actor(the_person, position = "against_wall")
    $ mc.change_locked_clarity(30)
    "She lifts one leg to give you better access. Your grab her ass with both hands, lifting her up slightly."
    "She looks you right in the eyes as you slowly lower her, your cock sliding inside her. She gasps as you bottom out inside of her."
    the_person "Oh fuck... we forgot... we forgot a condom!"
    mc.name "Want me to stop?"
    the_person "No! Oh god, just promise me you'll pull out, okay?"
    mc.name "I'll try."
    the_person "You'll try? Oh my god..."
    $ the_person.change_arousal(20)
    "All she can do is cling to you as you start to fuck her."
    call fuck_person(the_person, start_position = against_wall, private = True, start_object = make_wall(), skip_intro = True, skip_condom = True) from _call_fuck_erica_after_yoga_01
    $ the_person.draw_person(position = "stand4")
    if the_person.has_creampie_cum():
        the_person "Oh god, you were supposed to pull out!"
        $ the_person.change_love(-2)
        "Your cum is dribbling down between her legs."
        if the_person.on_birth_control:
            the_person "You have got to be more careful... thankfully I'm on birth control..."
        else:
            the_person "I'm not on birth control! I'll have to get a plan B before class..."
        mc.name "I'm sorry, I just couldn't help it, you are so amazing."
        the_person "I'm a little mad... but it's okay. You just really need to do a better job controlling yourself if this is gonna work!"
    else:   #Check and make sure MC finished before this
        the_person "Wow, I don't know what came over you, but then YOU came over ME, and it was amazing."
        $ the_person.change_love(2)
        the_person "I know that was really sudden, but thanks for not cumming inside me. I really can't get pregnant right now."
        the_person "I need you to have some self control if this is gonna work!"
    mc.name "If what is going to work?"
    the_person "I ummm... errmm... I mean..."
    "She stutters, suddenly realizing what she said. Then she sighs."
    the_person "I guess I mean us? Like, we've gotten really close lately... tell me it isn't just me feeling this way?"
    menu:
        "I feel the same way":
            the_person "Yes! Oh god, you have no idea how happy I am to hear that."
            $ the_person.change_stats(happiness = 15, love = 5)
            "She kisses you, and you kiss her back."
            the_person "So like... are we official now? I can call you my boyfriend?"
            mc.name "Yes that would be appropriate."
            $ the_person.add_role(girlfriend_role)
            the_person "Yay! Oh my god, this is great!"

        "Let's just be friends":
            the_person "Ah... okay wow, I guess I was just... totally misinterpreting things between us..."
            $ the_person.change_stats(happiness = -15, love = -20)
            the_person "I didn't realize you just wanted things to be strictly physical between us. Is that what you want? Friends with benefits?"
            mc.name "Yes that is what I am looking for right now."
            the_person "Okay... I'm sorry I didn't realize. But I think I can manage that."
    "Suddenly, [the_person.possessive_title] checks the time."
    the_person "Oh fuck! I have to get to class!"
    $ the_person.apply_planned_outfit()
    $ the_person.draw_person()
    if the_person.is_girlfriend():
        the_person "I'll see you around, I'm sure! If you get busy I'll still be over on Saturday night!"
    else:
        the_person "Well, I'll see you around."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.title] turns around and opens the door to your office, leaving you to begin your work day properly."
    $ erica.event_triggers_dict["post_yoga_fuck"] = True
    return

label erica_ghost_label(the_person):
    "You get a message on your phone. Looks like it is from [the_person.possessive_title]."
    the_person "Hey, I'm really sorry to have to do this, but I think I'm catching feelings."
    the_person "We agreed at the beginning we wouldn't let that happen, so I don't think we should see each other anymore."
    the_person "I'm changing to a different gym, and after I send this, I'm going to block your number. I'm sorry."
    "Damn. Sounds like you pushed things with her a little too far..."
    $ the_person.remove_person_from_game()
    $ casual_sex_create_athlete() #Create a new athlete so MC can try again if they choose.
    return

label erica_breeding_fetish_followup_label(the_person):
    "When you enter the gym, you look around for [the_person.possessive_title]. She is usually here this time of day."
    $ the_person.draw_person(position = "sitting")
    "You notice her over on a bike machine, which is odd since she usually likes to jog. You walk over to say hello."
    mc.name "Good day [the_person.title]."
    the_person "Oh, hey [the_person.mc_title]!"
    mc.name "I was surprised to see you on the bike machine, no treadmill today?"
    the_person "Not today. I've been having some joint pain in my knees the last few days, so I decided to do something more low impact."
    the_person "I'm pretty sure it's just pregnancy related, but I still want to try and stay fit, even as I get bigger."
    mc.name "That's great. How is it going with the track team?"
    the_person "Ahh, well... I know I need to tell the coach soon..."
    mc.name "You haven't told them?"
    the_person "I'm going to! I just... the timing hasn't been right!"
    mc.name "Yeah but... wouldn't it be better if you told them, you know... BEFORE your belly starts to get bigger?"
    the_person "I know, I'm just scared! I love track and field, but the coach has a history of being a total bitch to girls who get knocked up..."
    the_person "I don't regret this whatsoever... I just wish there was a way to make this easier."
    mc.name "Surely they can't kick you off the team for getting pregnant?"
    the_person "No, but the coach will just go around people's backs and go to their instructors, forcing them to give them bad marks."
    the_person "If a person's grades drop too much they kick you off the team... and sometimes even out of school..."
    mc.name "That's crazy! Surely there is some way to stop that?"
    $ the_person.draw_person(position = "stand3")
    "[the_person.possessive_title] stops her bike and stands up to continue talking with you."
    the_person "I don't think so. I know at least one other girl that it happened to, and some of the seniors say it happened to a couple girls a few years ago..."
    "Hmm. This is a distressing development. Despite being a model student athlete, a coach with a vendetta is not an easy thing to get around."
    the_person "Anyway, was there something that you wanted?"
    $ mc.business.add_mandatory_crisis(erica_breeding_fetish_team_crisis)
    call talk_person(the_person) from _call_talk_erica_followup_111
    return

label erica_breeding_fetish_team_crisis_label():
    $ the_person = erica
    $ the_person.happiness = 70
    $ mc.change_location(bedroom)
    $ mc.location.show_background()
    "You are in your room, getting ready for bed when your phone vibrates. It's [the_person.possessive_title]."
    $ mc.start_text_convo(the_person)
    the_person "Hey, sorry I know it's late. Can I come over?"
    mc.name "Sure. Everything okay?"
    the_person "No, I'll be over soon."
    $ mc.end_text_convo()
    "Yikes. You quickly straighten up your room and then wait for [the_person.title] to arrive."
    "In a few minutes, your phone goes off again, and soon you are leading [the_person.possessive_title] back to your room."
    $ the_person.draw_person(emotion = "sad")
    the_person "I'm so sorry to just invite myself over like this..."
    mc.name "It's okay, no need to apologize. Is everything okay with you and the baby?"
    the_person "Aww, yeah, we're both doing okay..."
    mc.name "Have a seat."
    $ the_person.draw_person(position = "sitting")
    "[the_person.title] sits on the edge of your bed."
    mc.name "What is going on?"
    the_person "I was at home, working on some homework, when I got an email from my coach."
    the_person "He said I was being removed from the team for academic misconduct, that my grades had dropped too much."
    the_person "They are kicking me off the track team for good, and I'm going to lose my athletic scholarship!"
    mc.name "That doesn't make any sense, you've been keeping your grades up, right?"
    the_person "Of course! But when I looked them up, I couldn't believe it!"
    the_person "In the computer, they were all suddenly C's or worse, and to maintain my scholarship and spot on the team I have to maintain a 3.0 GPA!"
    the_person "It's the coach... He had to have talked to my instructors and they changed my grades because I got pregnant!"
    "It is crazy to imagine... You decide to look into it more."
    mc.name "Let me see, can you show me? Your class grades?"
    "[the_person.possessive_title] pulls up her grade sheet on her phone, then shows it to you."
    "Damn, D, C+, F?, D... wait."
    "You notice one of the classes, chemistry 201 with professor [nora.last_name] is now showing a D."
    mc.name "Chemistry... is that with [nora.fname] [nora.last_name]?"
    the_person "Yeah?"
    mc.name "I actually know her. Cooperating to get someone kicked off the track team because she got pregnant isn't something she would do."
    the_person "But... I mean... she did though?"
    "This doesn't add up. [nora.title] would never do something like that."
    mc.name "I can't promise anything, but before you give up on this, let me talk to her. Maybe I can find out what is going on."
    the_person "I... I don't know. I'm not sure you'll be able to anything."
    mc.name "Well, I'll try anyway. [nora.title] is a good person, she'll at least be able to tell me why she is going along with it."
    $ nora.add_unique_on_talk_event(erica_breeding_fetish_nora_followup)
    $ erica.event_triggers_dict["kicked_off_team"] = True
    the_person "Okay. I appreciate it."
    "You look down at [the_person.possessive_title], sitting on the edge of your bed. Her belly is really showing recently, and she looks amazing, although distraught."
    mc.name "Hey, it's getting late. Why don't you spend the night here?"
    $ the_person.change_happiness(5)
    $ the_person.draw_person(position = "sitting", emotion = "happy")
    "For the first time since she got here, she slips a slight smile."
    the_person "Oh? You don't think it's gross... my belly getting bigger?"
    mc.name "Gross? Geesh, every time I look at you I get so turned on, thinking about pinning you down and knocking you up."
    $ the_person.change_stats(happiness = 5, arousal = 20)
    "She looks away from you, but her smile gets a little wider."
    the_person "Yes, and as you can see you certainly did a good job of that, didn't you."
    mc.name "Yeah, but I could definitely use a little more practice."
    $ the_person.change_stats(happiness = 5, arousal = 20)
    the_person "Oh god, would you stop? You're making me leak..."
    mc.name "Seriously, you want me to stop?"
    the_person "Stop talking anyway... yeah..."
    "As you step toward [the_person.possessive_title], she lays back on your bed."
    $ the_person.draw_person(position = "missionary", emotion = "happy")
    if the_person.outfit.vagina_available():
        "When she spreads her legs, the aroused folds of [the_person.possessive_title] lay open and exposed to you."
        $ mc.change_locked_clarity(50)
    else:
        mc.name "Let's get these out of the way first..."
        "As you pull off the clothes from her lower body, she takes the initiative and takes her top off."
        $ the_person.strip_outfit(position = "missionary")
        "Now naked, when she spreads her legs, the aroused folds of [the_person.possessive_title] lay open and exposed to you."
        $ mc.change_locked_clarity(50)
    "With one hand you start to undo your pants, with the other you run your fingers along her slit. You slip a finger in and discover she is sopping wet."
    the_person "You don't need to do that, just give me that..."
    "When you finish pulling your dick out, she reaches down, grabs your dick and starts to stroke it."
    "You grab her hand, then pin it behind her head as you get on top of her. She starts to protest, but it dies in her throat when your cock pokes against her slit."
    "It takes a couple tries, but you find the right angle and then push forward, your erection piercing into her cunt."
    "[the_person.possessive_title]'s legs instinctually wrap around you as she pulls you in deeper. She moans when you bottom out."
    the_person "Agh, it feels so good like this. Cum deep for me, please?"
    $ mc.change_locked_clarity(50)
    call fuck_person(the_person, start_position = breeding_missionary , private = True, skip_intro = True, skip_condom = True, position_locked = True) from _erica_track_team_crisis_01
    the_person "Mmm, that was nice... are you sure it's okay if I sleep here?"
    mc.name "Of course."
    $ the_person.draw_person(position = "walking_away")
    $ clear_scene()
    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_erica_bred_night_01

    $ scene_manager = Scene()
    "You wake up. Next to you, the bed is empty, but it is still warm. [the_person.possessive_title] must have just gotten up..."
    "A few seconds later, you hear the toilet flush. The sink runs for several seconds, and then the door opens."
    $ the_person.apply_planned_outfit()
    $ scene_manager.add_actor(the_person, display_transform = character_center_flipped)
    mc.name "Good morning."
    the_person "Good morning [the_person.mc_title]... Sorry, but I need to leave early, I've got some things I need to figure out..."
    mc.name "Sure, let me just walk you to the door at least."
    "You jump up out of bed, grab a pair of shorts and a t-shirt and throw them on."
    "You open your bedroom door and start to walk [the_person.title] to the front door..."
    $ scene_manager.add_actor(lily)
    lily "Morning [lily.mc_title], you're up early... Oh! Hey [erica.fname]!"
    the_person "Hey..."
    if lily.sluttiness >= 40:
        lily "I thought I heard some action last night. Nice going!"
    else:
        lily "I thought I heard some... errm... strange noises last night..."
    the_person "Yeah... that was us..."
    lily "Wow, [erica.fname], you look amazing! You are positively glowing."
    lily "You're still coming over on Saturday right? Thirsty InstaPic boys are gonna love the way you are developing..."
    if lily.pregnancy_is_visible():
        lily "I have to say, I started making considerably more money on InstaPic when my tits starting swelling up with milk."
    elif lily.sluttiness >= 60:
        lily "I've been thinking about doing something to make my tits a little bigger too, though maybe not getting pregnant..."
    else:
        lily "I've noticed lately that girls with bigger tits seem to make more money on that platform."
    the_person "I don't know, things in my life are kind of crazy right now."
    lily "Aww, come on! You can just come over and hang out, even if we don't get around to taking pictures."
    the_person "Really?"
    lily "Of course! I mean... I feel like I have a pretty good idea of who did this to you..."
    the_person "That's true... I didn't even realize that you would be the aunt! Okay, I'll be here!"
    lily "Great!"
    "[lily.title] starts to talk about another subject, but [the_person.possessive_title] cuts her off."
    the_person "I'm sorry, but I really need to get going, I have a lot of things to figure out."
    if the_person.is_girlfriend():
        lily "Oh god! He didn't just..."
    else:
        "[lily.title] looks at you and raises her eyebrow."
        lily "He isn't playing around with your heart is he..."
    the_person "No! No, it's school related stuff."
    lily "Oh... right."
    "[the_person.title] says goodbye. You finish walking her to the door, then go back to your room."
    $ scene_manager.clear_scene()
    "You aren't sure if there is anything you can do to help [the_person.possessive_title], but one thing that really bugs you is that score in [nora.title]'s class."
    "You make up your mind. Next time you get the chance you are going to talk to her about it. Surely there is something more going on here?"
    return

label erica_breeding_fetish_nora_followup_label(the_person):
    "You step into [the_person.possessive_title]'s office."
    mc.name "Hey [the_person.title], have a minute?"
    the_person "I can give you a minunte."
    mc.name "I was hoping I could talk to you about one of your students. She is a friend of mine and is confused about a recent drop in her grades."
    the_person "Hmm, okay. What's her name?"
    mc.name "[erica.fname] [erica.last_name]. She is in your Chemistry 201 class."
    the_person "Mmmm... I'm not sure, there's a lot of students in that class."
    mc.name "She is on the track team. She got pregnant and is just starting to show."
    the_person "Oh! Yeah I think I remember her. Sweet girl. You say her grades have been dropping?"
    mc.name "Yeah..."
    the_person "Hmm, that IS odd. I don't recall anything like that. I think she has been doing well in my class."
    mc.name "Well, her grade is down to a D, and unfortunately she is on the verge of getting kicked off the track team."
    "[the_person.possessive_title] wrinkles her nose for a second as she thinks about it."
    the_person "Ah, well, if you like I could take a look at her grades on my computer really quick."
    mc.name "Sure, that would be great."
    $ the_person.draw_person(position = "sitting")
    "[the_person.title] sits down at her desk and pulls up her student records. After a short time, she pulls up [erica.possessive_title] records."
    the_person "Yeah, this is all fairly standard, good grades over all... hmm..."
    mc.name "Yeah, it's weird isn't it?"
    the_person "Actually, something went wrong here... this is a quiz I just got done grading yesterday. No one got less than 70 percent, but it shows in the record here that she got 17."
    the_person "And this? This grade was just an attendance grade. I had mandatory attendance for a guest speaker, so it should either be 0, or 100, and this is showing she got a 35..."
    $ the_person.draw_person(position = "sitting", emotion = "angry")
    "[the_person.possessive_title]'s brow furrows as she goes through some of her recent grades."
    the_person "[the_person.mc_title]... You wouldn't have come to me unless you thought something was going on... What exactly is going on here? I did NOT give her these grades!"
    mc.name "Well, this is kind of a longshot, but, [erica.fname] thinks her track coach is sabatoging her grades to get her kicked off the track team."
    the_person "Oh my. That is a very serious allegation. But yet, here in front of me is possible incriminating data."
    the_person "I'm going to save a copy of this and correct her grades immediately. While I do that, do you think you could get me a list of her other instructors?"
    mc.name "Sure."
    "You shoot [erica.title] a text and ask her for her full list of classes. It takes a minute, but she sends you a screenshot of her enrollement form with her class list."
    "You show [the_person.possessive_title] the list."
    the_person "Ahh, I see. Yes I am good friends with Professor Davis, I'll talk to her about this also and see if she is seeing the same thing."
    mc.name "Do you think... she could be right?"
    the_person "I'm not ready to jump to that conclusion yet, but the evidence I've seen has my attention."
    the_person "I don't know how those grades got changed the way they did, and I'd like to check with her other instructors before I move forward with anything."
    mc.name "Well, I really appreciate you looking in to this."
    the_person "Give me a couple of days, and I'll get back to you about what I find out, okay?"
    mc.name "Sounds great."
    $ the_person.draw_person(position = "stand2", emotion = "happy")
    the_person "Always happy to help. Is there anything else you needed?"
    $ mc.business.add_mandatory_crisis(erica_breeding_nora_news_part_one)
    return

label erica_breeding_nora_news_part_one_label():
    $ the_person = nora
    "Your phone goes off in your pocket. It's [the_person.possessive_title]."
    $ mc.start_text_convo(the_person)
    the_person "Hey, I just wanted to give you a quick update."
    the_person "I talked to all of Ms. [erica.last_name]'s other instructors, and they've all said similar things."
    the_person "None of them gave her those bad marks. I've kicked it up to internal affairs and IT."
    the_person "IT said there are some suspicious logs in the grade book program and are investigating."
    mc.name "That sounds promising."
    the_person "Yeah, I'll keep you updated, but give me a couple more days."
    mc.name "Got it. Thanks."
    $ mc.end_text_convo()
    $ mc.business.add_mandatory_crisis(erica_breeding_nora_news_part_two)
    return

label erica_breeding_nora_news_part_two_label():
    $ the_person = nora
    if mc.location != university:
        "Your phone goes off in your pocket. It's [the_person.possessive_title]."
        $ mc.start_text_convo(the_person)
        the_person "Hey, can you come out to the university? I have some big news."
        mc.name "Sure, I'll be right there."
        $ mc.end_text_convo()
        $ mc.change_location(university)
        $ mc.location.show_background()
    else:
        "Walking around the university grounds, [the_person.possessive_title] spots you and hurries over to you."
    $ the_person.draw_person()
    the_person "[the_person.mc_title], I have some incredible news."
    mc.name "Oh?"
    the_person "The track coach has been fired. IT and security traced the grade book changes back to a computer he was using and was able to trace everything back to him."
    the_person "He was fired and may even be facing some jail time. The boy's track coach has been named the interim coach until someone new can be hired."
    the_person "I already spoke with him and informed him of the sensitive situation with the student."
    the_person "The new coach has already reached out to her with an offer for a full ride, unconditional scholarship and placement back on the track team."
    mc.name "Wow, so the guy really was tampering with grades."
    the_person "Yes, he was."
    mc.name "Well that is great news. I'm sure [erica.fname] will be excited when she hears about it."
    $ erica.event_triggers_dict["team_reinstate_day"] = day
    $ erica.add_unique_on_talk_event(erica_breeding_fetish_team_rejoin)

    "You can't wait to talk to [erica.possessive_title] about the news."
    return

label erica_breeding_fetish_team_rejoin_label(the_person):
    if the_person.happiness < 130:
        $ the_person.happiness = 130
    $ the_person.draw_person()
    "You find [the_person.possessive_title]. When she notices you approaching you, she smiles wide."
    the_person "[the_person.mc_title]! I can't believe it!"
    $ the_person.draw_person(position = "kissing")
    "[the_person.title] throws her arms around you and gives you a hug, holding you closely for several seconds."
    the_person "It was you, wasn't it?"
    mc.name "That did what?"
    "You decide to play ignorant."
    the_person "The team! You got me back on the track team! And I got this email, they are giving me a full ride, unconditional scholarship!"
    mc.name "Who me? Couldn't be!"
    $ the_person.draw_person()
    $ the_person.change_stats(happiness = 15, love = 7, obedience = 12)
    the_person "Yeah right!"
    if the_person.knows_pregnant():
        "[the_person.possessive_title] rubs her belly."
        the_person "I won't be rejoining the team immediately... going to wait for the little one to come first."
        the_person "But it's amazing knowing I'll be able to go back to it!"
    else:
        the_person "Since I already had the baby, I can go straight back to the team..."
        the_person "But if you wanna knock me up again, I wouldn't mind it!"
        $ mc.change_locked_clarity(30)
    the_person "Anyway, I just want you to know, I'll never forget what you've done for me."
    the_person "Now, did you want something?"
    $ nora.add_unique_on_room_enter_event(college_intern_recruit_supply) #I added this here so we don't accidentally steamroll right into it with Nora.
    $ erica.event_triggers_dict["rejoin_team"] = False
    call talk_person(the_person) from _call_talk_erica_team_rejoin_010
    #fin
    return

label erica_discuss_morning_wakeup_label(the_person):
    mc.name "Hey, I wanted to talk to you about something."
    the_person "Yeah?"
    mc.name "You know how sometimes, you sneak into my room after spending the night with [lily.fname] in the early morning?"
    the_person "Oh yeah..."
    menu:
        "Don't do that anymore":
            $ erica.event_triggers_dict["morning_wakeup_pref"] = 0
            pass
        "Surprise me once in a while":
            $ erica.event_triggers_dict["morning_wakeup_pref"] = 1
            pass
        "Do it every chance you get":
            $ erica.event_triggers_dict["morning_wakeup_pref"] = 2
            pass
    the_person "Okay, I can do that! Anything else?"
    return


init 2 python:
    def switch_to_class_front(person_one, person_two, pose):
        # we assume we have a scene manager
        scene_manager.clear_scene(reset_actor = False)
        scene_manager.add_actor(the_person, position = pose)
        scene_manager.add_actor(yoga_assistant, position = pose, display_transform = character_left_flipped)
        return

    def switch_to_back_of_class(back_row, pose):
        transforms = [ character_right, character_center_flipped, character_left ]

        scene_manager.clear_scene(reset_actor = False)
        for idx in range(0, 3):
            # renpy.say(None, "Add actor: " + back_row[idx].name)
            scene_manager.add_actor(back_row[idx], position = pose, display_transform = transforms[idx])

        scene_manager.draw_scene()
        return

    def dose_yoga_class_with_serum(people, serum):
        for person in people:
            mc.inventory.change_serum(serum, -1)
            person.give_serum(copy.copy(serum))
        return

    #Erica specific python wrappers#
    def erica_on_love_path():
        return erica.event_triggers_dict.get("love_path", False)

    def erica_on_fwb_path():
        return erica.event_triggers_dict.get("fwb_path", False)

    def erica_on_hate_path():
        return erica.event_triggers_dict.get("hate_path", False)

    def erica_get_protein_day():
        return erica.event_triggers_dict.get("protein_day", 9999)

    def erica_protein_shake_is_unlocked():
        return erica.event_triggers_dict.get("erica_protein", 0) != 0

    def erica_workout_is_unlocked():
        return erica.event_triggers_dict.get("erica_workout", 0) != 0

    def erica_get_is_doing_yoga_sessions():
        return erica.event_triggers_dict.get("yoga_sessions_started", False)

    def erica_get_is_yoga_nude():
        return erica.event_triggers_dict.get("nude_yoga", False) == True

    def erica_get_is_doing_insta_sessions():
        return erica.event_triggers_dict.get("insta_pic_intro_complete", False) == True

    def erica_is_looking_for_work():
        return erica.event_triggers_dict.get("looking_for_work", False) == True

    def erica_has_given_morning_handjob():
        return erica.event_triggers_dict.get("post_insta_handy", False) == True

    def erica_get_wakeup_options():
        return erica.event_triggers_dict.get("wake_up_options", [])

    def erica_get_progress():
        return erica.event_triggers_dict.get("erica_progress", 0)

    def erica_get_yoga_class_list():
        yoga_list = []
        for person in [x for x in mc.business.get_employee_list() if x.get_opinion_score("yoga") > 0]:
            if not person is mc.business.hr_director:
                yoga_list.append(person)
        return yoga_list

    def erica_get_alternative_assistant(yoga_class):
        alt = next((x for x in mc.business.get_employee_list() if x not in yoga_class and x.get_opinion_score("yoga") > 0), None)
        if not alt:
            alt = renpy.random.choice(yoga_class)
            yoga_class.remove(alt)
        return alt

    def erica_get_yoga_assistant():
        identifier = erica.event_triggers_dict.get("yoga_assistant", None)
        if isinstance(identifier, Person):
            return identifier
        else:
            return get_person_by_identifier(identifier)
        return None

    def erica_apply_yoga_outfit_to_class(yoga_list):
        for person in yoga_list:
            if erica_get_is_yoga_nude():
                person.apply_yoga_shoes()
            else:
                person.apply_yoga_outfit()
        return

    def erica_after_class_outfit_cleanup(yoga_list):
        for person in yoga_list:
            person.apply_planned_outfit()
        return

    def erica_get_class_average_sluttiness(yoga_list):
        if __builtin__.len(yoga_list) == 0:
            return 0

        total_slut = 0
        for person in yoga_list:
            total_slut += person.sluttiness
        return int(total_slut / __builtin__.len(yoga_list))

    def erica_get_back_of_class(yoga_list):
        back_of_class = []
        back_of_class.append(get_random_from_list([x for x in yoga_list if x not in back_of_class]))
        back_of_class.append(get_random_from_list([x for x in yoga_list if x not in back_of_class]))
        back_of_class.append(get_random_from_list([x for x in yoga_list if x not in back_of_class]))
        return back_of_class

    def erica_class_energy_increase(yoga_list):
        for person in yoga_list:
            if person.max_energy < 150:
                person.change_max_energy(3)
        return

    def get_yoga_convince_employee_target():
        eligible_list = [x for x in mc.business.get_employee_list() if x not in erica_get_yoga_class_list() + [mc.business.hr_director]]
        return get_random_from_list(eligible_list)

    def erica_wakeup_choose_position():
        tuple_list = []
        for position in erica_get_wakeup_options():
            tuple_list.append([position.title(), position])
        tuple_list.append(["Surprise me", "Surprise me"])

        return renpy.display_menu(tuple_list,True,"Choice")

    def erica_get_morning_wakeup_pref():
        return erica.event_triggers_dict.get("morning_wakeup_pref", 0)

    def erica_pre_insta_blowjob_complete():
        return erica.event_triggers_dict.get("pre_insta_blowjob", False)

    def erica_post_yoga_fuck_complete():
        return erica.event_triggers_dict.get("post_yoga_fuck", False)

    def erica_fetish_is_kicked_off_team():
        return erica.event_triggers_dict.get("kicked_off_team", False)

    def erica_fetish_rejoin_team():
        return erica.event_triggers_dict.get("rejoin_team",False)

    # def erica_check_class_size_and_add_event():
    #     if len(erica_get_yoga_class_list()) < 4:
    #
    #     else:
    #
    #     return
