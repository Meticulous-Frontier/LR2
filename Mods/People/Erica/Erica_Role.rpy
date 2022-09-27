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

    def erica_money_problems_update_requirement(person):
        if time_of_day > 0 and time_of_day < 4:
            if erica_is_looking_for_work():
                return True
        return False

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
    erica_money_problems_update = Action("Ask about finances", erica_money_problems_update_requirement, "erica_money_problems_update_label",
        menu_tooltip = "See if Erica has found work.")
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

label erica_instantiate_jobs(stack):
    python:
        erica_student_job = Job("College Athlete", [erica_role, generic_student_role], job_location = university, work_times = [2])
        erica_student_job.schedule.set_schedule(gym, the_times = [1, 3])
        erica_student_job.schedule.set_schedule(gym, the_days = [5, 6], the_times = [1, 2])

            # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

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
                $ the_person.draw_person(position = "kissing", special_modifier="kissing")
                "You lean in and kiss [the_person.possessive_title] hungrily. Her hips are grinding against yours."
                $ the_person.change_arousal(10)
                $ mc.change_locked_clarity(10)
                $ the_person.add_situational_slut("horny", 10, "You take charge")
                $ the_person.add_situational_obedience("submissive", 20, "She submits to you")
                $ the_person.draw_person(position = "kissing")
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

    def erica_fetish_is_kicked_off_team():
        return erica.event_triggers_dict.get("kicked_off_team", False)

    def erica_fetish_rejoin_team():
        return erica.event_triggers_dict.get("rejoin_team",False)
