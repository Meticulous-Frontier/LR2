#Ashley's story has two primary themes.
#First, dealing with jealousy involving her sister. The base story assumes Stephanie and MC get together.
#Ashley attempts to disrupt the relationship and/or corrupt MC
#Second is her obedience story. Via Serums Ashley attempts to enslave MC's mind.
#Possible bad end if MC alienates Stephanie and Ashley?
#The first plays out in Ashleys Love and Sluttiness stories
#The second plays out in her obedience story.
#Either story could get resolved at some point, and should have implications in the other.

init 2 python:
    def ashley_mod_initialization(): #Add actionmod as argument#
        ashley_wardrobe = wardrobe_from_xml("Ashley_Wardrobe")
        ashley_base_outfit = Outfit("ashley's base accessories")
        the_eye_shadow = heavy_eye_shadow.get_copy()
        the_eye_shadow.colour = [.18, .54, .34, 0.95]
        the_rings = copper_ring_set.get_copy()   #Change this
        copper_ring_set.colour = [.1,.36,.19,1.0]
        ashley_base_outfit.add_accessory(the_eye_shadow)
        ashley_base_outfit.add_accessory(the_rings)

        # init ashley role
        ashley_role = Role(role_name ="Ashley", actions =[ashley_ask_date_classic_concert], hidden = True)

        #global ashley_role
        global ashley
        ashley = make_person(name = "Ashley", last_name =stephanie.last_name, age = 22, body_type = "standard_body", face_style = "Face_3",  tits="DDD", height = 0.89, hair_colour="brown", hair_style = ponytail, skin="white" , \
            eyes = "brown", personality = introvert_personality, name_color = "#228b22", dial_color = "#228b22" , starting_wardrobe = ashley_wardrobe, \
            stat_array = [1,4,4], skill_array = [1,1,3,5,1], sex_skill_array = [4,2,2,2], sluttiness = 7, obedience_range = [70, 85], happiness = 119, love = 0, \
            relationship = "Single", kids = 0, force_random = True, base_outfit = ashley_base_outfit, type = 'story',
            forced_opinions = [["production work", 2, True], ["work uniforms", -1, False], ["flirting", 1, False], ["working", 1, False], ["the colour green", 2, False], ["pants", 1, False], ["the colour blue", -1, False], ["classical", 2, False]],
            forced_sexy_opinions = [["taking control", 2, False], ["getting head", 2, False], ["drinking cum", -1, False], ["giving blowjobs", -2, False], ["public sex", -1, False], ["giving tit fucks", -2, False], ["being submissive", -2, False]])

        ashley.change_job(unemployed_job)
        ashley.set_schedule(stephanie.home, the_days=[0,1,2,3,4,5,6], the_times = [0,1,2,3,4])
        ashley.home = stephanie.home
        ashley.home.add_person(ashley)

        ashley.event_triggers_dict["intro_complete"] = False    # True after first talk
        ashley.event_triggers_dict["excitement_overhear"] = False   #
        ashley.event_triggers_dict["attitude_discussed"] = False   #
        ashley.event_triggers_dict["porn_discovered"] = False       #
        ashley.event_triggers_dict["porn_discussed"] = False    #
        ashley.event_triggers_dict["concert_overheard"] = False    #True after overhearing
        ashley.event_triggers_dict["concert_date"] = 0   #0 = not started, 1 = date arranged, 2 = date complete
        ashley.event_triggers_dict["porn_convo_day"] = 9999
        ashley.event_triggers_dict["porn_convo_avail"] = False
        ashley.event_triggers_dict["story_path"] = None
        ashley.event_triggers_dict["lily_friend"] = False
        ashley.event_triggers_dict["second_date"] = False
        ashley.event_triggers_dict["sneaks_over_complete"] = False
        ashley.event_triggers_dict["mc_obedience"] = 0
        ashley.event_triggers_dict["sub_titfuck_count"] = 0
        ashley.event_triggers_dict["sub_blowjob_count"] = 0
        ashley.event_triggers_dict["sub_fuck_count"] = 0
        ashley.event_triggers_dict["sub_anal_count"] = 0
        ashley.event_triggers_dict["sub_titfuck_avail"] = False
        ashley.event_triggers_dict["sub_blowjob_avail"] = False
        ashley.event_triggers_dict["sub_fuck_avail"] = False
        ashley.event_triggers_dict["sub_anal_avail"] = False
        ashley.event_triggers_dict["after_hours_avail"] = False
        ashley.event_triggers_dict["dom_fingers"] = False
        ashley.event_triggers_dict["dom_oral"] = False
        ashley.event_triggers_dict["dom_fuck"] = False
        mc.business.event_triggers_dict["ashley_submission_complete"] = False   #Set to true if we complete her submission arc.
        mc.business.event_triggers_dict["mc_serum_duration"] = 3
        mc.business.event_triggers_dict["mc_serum_aura_tier"] = 0
        mc.business.event_triggers_dict["mc_serum_cum_tier"] = 0
        mc.business.event_triggers_dict["mc_serum_energy_tier"] = 0
        mc.business.event_triggers_dict["mc_serum_physical_tier"] = 0
        mc.business.event_triggers_dict["mc_serum_aura_unlocked"] = False
        mc.business.event_triggers_dict["mc_serum_cum_unlocked"] = False
        mc.business.event_triggers_dict["mc_serum_energy_unlocked"] = False
        mc.business.event_triggers_dict["mc_serum_physical_unlocked"] = False
        mc.business.event_triggers_dict["mc_serum_max_quant"] = 1
        global list_of_upgraded_mc_serums
        list_of_upgraded_mc_serums = [] #Use this list to store serums that have had their base tiers upgraded for save / load purposes.


        # add appoint
        #office.add_action(HR_director_appointment_action)

        ashley_intro = Action("ashley_intro",ashley_intro_requirement,"ashley_intro_label") #Set the trigger day for the next monday. Monday is day%7 == 0
        mc.business.add_mandatory_crisis(ashley_intro) #Add the event here so that it pops when the requirements are met.

        # set relationships
        town_relationships.update_relationship(ashley, stephanie, "Sister")
        town_relationships.update_relationship(nora, ashley, "Friend")
        town_relationships.update_relationship(lily, ashley, "Rival")

        #TODO make her know Nora from before graduation. She is familiar with serums and their effects
        #TODO add ashley to unique characters list?

        ashley.add_role(ashley_role)

        return


    # ashley_room_excitement_overhear = Action("Overhear Ashley",ashley_room_excitement_overhear_requirement,"ashley_room_excitement_overhear_label")
    # ashley_ask_sister_about_attitude = Action("Ask about Ashley's attitude",ashley_ask_sister_about_attitude_requirement,"ashley_ask_sister_about_attitude_label")
    # ashley_room_warming_up = Action("Ashley is warming up",ashley_room_warming_up_requirement,"ashley_room_warming_up_label")
    # ashley_porn_video_discover = Action("Discover Ashley's porn video",ashley_porn_video_discover_requirement,"ashley_porn_video_discover_label")
    # ashley_ask_sister_about_porn_video = Action("Ask about Ashley in porn",ashley_ask_sister_about_porn_video_requirement,"ashley_ask_sister_about_porn_video_label")

    # ashley_mandatory_ask_about_porn = Action("Decide to talk to Ashley about porn",ashley_mandatory_ask_about_porn_requirement,"ashley_mandatory_ask_about_porn_label")
    # ashley_ask_about_porn = Action("Ask about porn",ashley_ask_about_porn_requirement,"ashley_ask_about_porn_label")
    # ashley_post_handjob_convo = Action("Talk to Ashley", ashley_post_handjob_convo_requirement, "ashley_post_handjob_convo_label")
    # ashley_stephanie_arrange_relationship = Action("Talk to Stephanie", ashley_stephanie_arrange_relationship_requirement, "ashley_stephanie_arrange_relationship_label")
    # ashley_stephanie_saturday_coffee_intro = Action("Good Morning Coffee", ashley_stephanie_saturday_coffee_intro_requirement, "ashley_stephanie_saturday_coffee_intro_label")
    # ashley_stephanie_saturday_coffee_recur = Action("Good Morning Coffee", ashley_stephanie_saturday_coffee_recur_requirement, "ashley_stephanie_saturday_coffee_recur_label")
    # ashley_clothes_shopping = Action("Ashley goes clothes shopping", ashley_clothes_shopping_requirement, "ashley_clothes_shopping_label")
    # ashley_second_concert_date = Action("Ashley gets a second date", ashley_second_concert_date_requirement, "ashley_second_concert_date_label")
    # ashley_steph_second_date_confrontation = Action("Stephanie confronts you", ashley_steph_second_date_confrontation_requirement, "ashley_steph_second_date_confrontation_label")
    # ashley_blows_during_meeting = Action("Ashley loves a good meeting", ashley_blows_during_meeting_requirement, "ashley_blows_during_meeting_label")
    # ashley_sneaks_over = Action("Ashley sneaks over", ashley_sneaks_over_requirement, "ashley_sneaks_over_label")
    # ashley_steph_drinks_out = Action("Ashley and Stephanie date", ashley_steph_drinks_out_requirement, "ashley_steph_drinks_out_label")

    def ashley_steph_relationship_status():  #This function should return limited options back, to summarize the current status of MC relationship with Steph and Ashley
        if (ashley.sluttiness > 70 or ashley.is_girlfriend()) and (stephanie.sluttiness > 70 or stephanie.is_girlfriend()):
            return "both"
        elif ashley.is_girlfriend():
            return "ashley"
        elif stephanie.is_girlfriend():
            return "stephanie"
        elif __builtin__.abs(ashley.love - stephanie.love) < 20: # love difference < 20
            return "both"
        elif ashley.love > stephanie.love:
            return "ashley"
        elif ashley.love < stephanie.love:
            return "stephanie"

    def ashley_stay_after_work_setup(): #Use this to arrange ashleys schedule for after work activities
        ashley.set_override_schedule(mc.business.s_div, the_days = [0,1,2,3,4], the_times = [4])
        ashley.event_triggers_dict["after_hours_avail"] = True
        return

    def ashley_clear_after_work_setup():    #Clear her after work schedule.
        ashley.set_override_schedule(ashley.home, the_days = [0,1,2,3,4], the_times = [4])
        ashley.event_triggers_dict["after_hours_avail"] = False
        return

    def ashley_get_mc_obedience():
        return ashley.event_triggers_dict.get("mc_obedience", 0)

label jumpstart_ashley():
        $ ashley.sluttiness = 20
        $ ashley.obedience = 110
        $ ashley.love = 20
        call ashley_intro_label() from _ashley_jumpstart_function
        return

#Requirement Labels
init -1 python:
    def ashley_intro_requirement():   #After discovering an obedience serum trait and there is a position available. Must be at work.
        if day > TIER_3_TIME_DELAY and mc.is_at_work() and mc.business.is_open_for_business():
            if mc.business.get_employee_count() < mc.business.max_employee_count:
                return True
                #TODO Consider making this true only if recruiting increased via HR director? Would be much delayed intro
                # if sedatives_trait.researched or obedience_enhancer.researched or large_obedience_enhancer.researched: #TODO find a better trigger for this since we aren't doing MC serums anymore.
                #     return False
        return False

    def ashley_hire_directed_requirement():
        if not mc.business.head_researcher == stephanie:
            return False
        if not mc.business.is_open_for_business():
            return False
        if mc.business.get_employee_count() >= mc.business.max_employee_count:
            return "At employee limit"
        if not mc.is_at_work():
            return "Talk to her at work"
        return True

    def ashley_first_talk_requirement(the_person):
        if mc.is_at_work():
            return True
        return False

    def ashley_room_overhear_classical_requirement(the_person):
        if the_person.is_at_work():
            if the_person.days_employed > TIER_2_TIME_DELAY:
                return True
        return False

    def ashley_ask_date_classic_concert_requirement(the_person):
        if ashley_get_concert_overheard() and not ashley_get_concert_date_stage() > 0:
            return the_person.is_at_work()
        return False

    def ashley_classical_concert_date_requirement():
        if time_of_day == 3 and day%7 == 3:  #Thursday
            return ashley_get_concert_date_stage() == 1
        return False

    # def ashley_room_excitement_overhear_requirement(the_person):
    #     if the_person.is_at_work():
    #         if the_person.days_employed > 5: #Been working for at least a few days week.
    #             return True
    #     return False
    #
    # def ashley_ask_sister_about_attitude_requirement(the_person):
    #     if ashley_get_if_excitement_overheard():
    #         if the_person.is_at_work():
    #             return True
    #     return False
    #
    # def ashley_room_warming_up_requirement(the_person):
    #     if the_person.is_at_work():
    #         if the_person.days_employed > 12: #Been working for at least a week.
    #             return True
    #     return False
    #
    # def ashley_porn_video_discover_requirement():
    #     return False    #Disabled while working on her story.
    #     if time_of_day == 4 and ashley.sluttiness > 20 and mc.energy > 80:
    #         return ashley_get_attitude_discussed()
    #     return False
    #
    # def ashley_ask_sister_about_porn_video_requirement(the_person):
    #     return the_person.is_at_work() and ashley_get_porn_discovered()
    #
    # def ashley_mandatory_ask_about_porn_requirement():
    #     if time_of_day > 1 and ashley.sluttiness >= 20 and ashley.love >= 40 and stephanie.love >= 60:
    #         return day > ashley_get_porn_convo_day() and ashley_get_concert_date_stage() >= 2
    #     return False
    #
    # def ashley_ask_about_porn_requirement(the_person):
    #     return the_person.is_at_work() and ashley_get_porn_convo_avail()
    #
    # def ashley_post_handjob_convo_requirement(the_person):
    #     return the_person.is_at_work()
    #
    # def ashley_stephanie_arrange_relationship_requirement(the_person):
    #     return the_person.is_at_work()
    #
    # def ashley_stephanie_saturday_coffee_intro_requirement(the_person):
    #     return the_person.location == stephanie.location and day%7 == 6 and time_of_day == 0
    #
    # def ashley_stephanie_saturday_coffee_recur_requirement(the_person):
    #     return the_person.location == stephanie.location and day%7 == 6 and time_of_day == 0
    #
    # def ashley_second_concert_date_requirement():
    #     return time_of_day == 3
    #
    # def ashley_steph_second_date_confrontation_requirement():
    #     return time_of_day == 2 and mc.is_at_work() and ashley.sluttiness >= 60
    #
    def add_ashley_hire_later_action():
        ashley_hire_directed = Action("Reconsider hiring Stephanie's sister", ashley_hire_directed_requirement, "ashley_hire_directed_label",
            menu_tooltip = "Talk to Stephanie about hiring her sister. She might be disappointed if you decide not to again...")
        mc.business.r_div.add_action(ashley_hire_directed)
        return
    #
    def remove_ashley_hire_later_action():
        mc.business.r_div.remove_action("ashley_hire_directed_label")
        return
    #
    # def ashley_clothes_shopping_requirement(the_person):
    #     return the_person.location == clothing_store
    #
    # def ashley_blows_during_meeting_requirement():
    #     if time_of_day == 2 and mc.is_at_work():
    #         return ashley.sluttiness > 40 and ashley.is_willing(blowjob)
    #     return False

init 1 python:
    ashley_first_talk = Action("Introduce yourself to Ashley",ashley_first_talk_requirement,"ashley_first_talk_label")
    ashley_room_overhear_classical = Action("Ashley talks about concert",ashley_room_overhear_classical_requirement,"ashley_room_overhear_classical_label")
    ashley_ask_date_classic_concert = Action("Ask Ashley to the Concert",ashley_ask_date_classic_concert_requirement,"ashley_ask_date_classic_concert_label")
    ashley_classical_concert_date = Action("Ashley Date Night",ashley_classical_concert_date_requirement,"ashley_classical_concert_date_label")

#Ashley base line intro story.


#Intro Labels
label ashley_intro_label():
    if ashley.is_employee():    #We already hired her somehow.
        return
    $ the_person = stephanie
    "You are deep in your work when a voice startles you from your concentration."
    the_person "Hey [the_person.mc_title]. Sorry to bug you, do you have a minute?"
    $ scene_manager = Scene()  #Clean Scene
    $ scene_manager.add_actor(the_person)
    mc.name "Of course. What can I do for you?"
    the_person "Well, I kind of need a favor."
    mc.name "Well, you've taken an awfully large risk coming to work for me here, so I suppose I owe you one."
    the_person "You see, it's my sister. She just graduated from college, but is having trouble finding work in her degree. She's had to move in with me because she can't find work!"
    the_person "She's really smart, but kind of wild. It has been hard for her to get through interviews."
    mc.name "What is her degree in?"
    the_person "She actually just finished her nursing certification and pre-med degree, but is taking a year off before returning to school."
    mc.name "She's a nurse and... she can't find work?"
    the_person "Errr, well she had a little incident at the hospital with an HR issue..."
    the_person "Look, I know that this won't be her final job, but having something to help fill in the gaps would be huge for her."
    the_person "I brought her resume, will you at least take a look at it? I think she would be great over in production."
    the_person "And it would be a huge favor for me!"
    menu:
        "Take a look":
            pass
        "Not right now":
            mc.name "I'm sorry, I'm not hiring anyone like that right now. But if I change my mind I'll come find you, okay?"
            the_person "Of course, that's all I can ask, is that you will keep her in mind. Thanks!"
            $ add_ashley_hire_later_action()
            return
        "Blow me and I'll look" if the_person.is_willing(blowjob):
            mc.name "I tell you what, why don't you come suck me off while I look over her documents."
            the_person "Oh! A favor for a favor then? Okay!"
            $ scene_manager.update_actor(the_person, position = "blowjob", emotion = "happy")
            "[the_person.possessive_title] gets on her knees and starts to undo your pants."
            $ mc.change_locked_clarity(20)
            the_person "You know I would do this anyway, right?"
            mc.name "Of course, but being reminded of your blowjob skills will probably help me make up my mind if I want to hire someone you're related to."
            call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, position_locked = True) from _call_sex_description_ashley_intro_bonus_BJ_1
            $ the_report = _return
            $ scene_manager.update_actor(the_person, position = "stand4")
            if the_report.get("guy orgasms", 0) > 0:
                mc.name "God your mouth is amazing. If your sister sucks anything like you, this will be a no-brainer..."
                the_person "Hah! Well, to be honest, I don't think she really cares for giving blowjobs, but I guess you never know."
    "You pick up her documents and look over them."
    "From her skill set, it is obvious the best choice of department for her would be in production. The only question is, should you hire her or not?"
    call hire_select_process([ashley, 1]) from _call_hire_ashley_1
    $ the_person.draw_person()
    if _return == ashley:
        mc.name "I agree. She would be perfect for the production department. Would you pass along that she can start tomorrow? Or anytime in the next week."
        $ the_person.change_stats(happiness = 5, obedience = 5)
        the_person "Oh! I didn't think you would say yes. This is great news! I'm sure she'll probably want to get started right away!"

        $ mc.business.add_employee_production(ashley)
        $ ashley.set_schedule(None, the_times = [1,2,3]) #Free roam when not working


        "You complete the necessary paperwork and hire [ashley.fname], assigning her to the production department."
        "As you finish up, you notice [the_person.possessive_title] is already calling her sister with the news."
        $ scene_manager.update_actor(the_person, position = "walking_away")
        the_person "Hey Ash! Guess what? I got you a starting position at that place I've been..."
        "Her voice trails off as she leaves the room. You hope you made the right decision!"
        $ ashley.add_unique_on_room_enter_event(ashley_first_talk)
    else:
        mc.name "I'm sorry, I don't think she is a good fit at this time. But I will keep her in mind for the future, okay?"
        the_person "Ahhh, okay. I understand, but please let me know ASAP if you change your mind!"
        $ scene_manager.update_actor(the_person, position = "walking_away")
        "[the_person.possessive_title] gets up and leaves the room. Did you make the right decision? Oh well, if you change your mind, you can always talk to her again."
        $ add_ashley_hire_later_action
    return

label ashley_hire_directed_label():
    $ the_person = stephanie
    mc.name "I wanted to talk to you again about your sister."
    the_person "Oh? Have you decided to reconsider?"
    mc.name "I have. Do you still have her documents that I could look over again?"
    the_person "Of course! Let me get them."
    "[the_person.possessive_title] runs over to her desk and comes back with a folder."
    the_person "Here you go!"
    "You pick up her documents and look over them."
    "From her skill set, it is obvious the best choice of department for her would be in production. The only question is, should you hire her or not?"
    call hire_select_process([ashley, 1]) from _call_hire_ashley_2
    $ the_person.draw_person()
    if _return == ashley:
        mc.name "I agree. She would be perfect for the production department. Would you pass along that she can start tomorrow? Or anytime in the next week."
        $ the_person.change_stats(happiness = 5, obedience = 5)
        the_person "Oh! This is great news! I'm sure she'll probably want to get started right away!"
        $ remove_ashley_hire_later_action()
        $ mc.business.add_employee_production(ashley)


        "You complete the necessary paperwork and hire [ashley.fname], assigning her to the production department."
        "As you finish up and start to leave, you notice [the_person.possessive_title] is already calling her sister with the news."
        $ the_person.draw_person(position = "walking_away")
        the_person "Hey Ash! Guess what? I got you a starting position at that place I've been..."
        "Her voice trails off as you leave the room. You hope you made the right decision!"
        $ ashley.add_unique_on_talk_event(ashley_first_talk)
    else:
        mc.name "I'm sorry, I don't think she is a good fit at this time. But I will keep her in mind for the future, okay?"
        the_person "Wow, really? Why did you even talk to me about this?"
        $ the_person.change_stats(happiness = -10, love = -5, obedience = -5)
        $ the_person.draw_person(position = "walking_away")
        "[the_person.possessive_title] gets up and leaves the room. You should probably avoid getting her hopes up again like this."

    return

label ashley_first_talk_label(the_person):
    $ the_person.draw_person()
    mc.name "Hello there. You must be [the_person.fname]. I'm [mc.name], the one who owns this place."
    "She looks at you and smiles."
    the_person "Hello! So you're the guy my sister won't stop going on and on about. Nice to meet you."
    mc.name "Ah, yes I supposed that would be me."
    the_person "Thank you for the opportunity. I appreciate the work, especially in a pharma related field, it will really help my job prospects in the future."
    mc.name "Of course, [stephanie.fname] is a good friend. Do you go by [the_person.fname]? Or something else?"
    $ the_person.set_title(the_person.name)
    $ the_person.set_possessive_title("Your production assistant")
    $ the_person.set_mc_title(mc.name)
    the_person "[the_person.title] is fine..."
    mc.name "[the_person.title] it is then."
    $ ashley.event_triggers_dict["intro_complete"] = True
    $ ashley.add_unique_on_room_enter_event(ashley_room_overhear_classical)
    $ ashley.special_role.insert(0, prod_assistant_role)
    $ mc.business.prod_assistant = ashley
    $ ashley.add_unique_on_room_enter_event(mc_serum_intro)
    return

label ashley_room_overhear_classical_label(the_person):
    $ the_person = ashley # on_room_enter_event so the_person isn't defined
    $ the_person.draw_person(position = "standing_doggy")
    "As you step into the room, you can overhear [the_person.title] talking excitedly to another coworker."
    the_person "I know, the city symphony is performing a collection of Johannes Brahms' symphonies. I want to go so bad, but I can't find anyone to go with..."
    "As you enter the room, she looks up and stops talking."
    $ the_person.draw_person()
    the_person "Oh, hey [the_person.mc_title]. Having a good day?"
    "[the_person.title] has been stepping into a role on her own as your production assistant. You feel like you are really starting to warm up to her."
    mc.name "It's been great so far. And you?"
    the_person "Oh, I've been good. Thanks for asking."
    mc.name "Glad to hear it."
    "Hmm... she is looking for someone to go with her to a classical music concert. Maybe that person could be you?"
    $ ashley.event_triggers_dict["concert_overheard"] = True
    return

label ashley_ask_date_classic_concert_label(the_person):
    mc.name "So... I couldn't help hearing earlier, you are looking to go to the Brahms symphony recital, but you don't have anyone to go with?"
    the_person "Ummm yeah, something like that..."
    mc.name "That sounds like a great cultural event. I was wondering if you would be willing to let me take you?"
    "She is caught off guard. She wasn't expecting you to ask something like this!"
    the_person "Oh! I uhh, I'm not sure if Steph would be okay with that..."
    mc.name "Why wouldn't she be okay with it?"
    the_person "I... well..."
    "She mutters something unintelligible."
    the_person "I guess there's no reason, really."
    mc.name "Well, I would really like to take you, if you want to go."
    the_person "I suppose."
    mc.name "Ah, great! Do you know when the concert is?"
    the_person "It's on Thursday night."
    mc.name "Ok. I'll plan to meet you there on Thursday night then?"
    the_person "Okay, if you're sure about this..."
    "You feel good about this as you finish up your conversation."
    $ ashley.event_triggers_dict["concert_date"] = 1
    $ mc.business.add_mandatory_crisis(ashley_classical_concert_date)
    return

label ashley_classical_concert_date_label():
    $ the_person = ashley
    $ scene_manager = Scene()
    "It's Thursday. You have a date planned with [the_person.title]. It's taken a while for her to warm up to you, so you don't even consider cancelling."
    "You head downtown. The plan is just to meet up at the concert hall itself. [stephanie.title] is going to drop her sister off and pick her up afterwards."
    $ mc.change_location(downtown)
    # make sure stephanie is wearing normal clothes (instead of uniform)
    $ stephanie.apply_outfit(stephanie.decide_on_outfit())
    # ashley is wearing something nice
    $ the_person.apply_outfit(the_person.decide_on_outfit(sluttiness_modifier = 0.2))
    "Soon, you see the sisters."
    $ scene_manager.add_actor(the_person, position = "stand4", emotion = "happy")
    $ scene_manager.add_actor(stephanie, display_transform = character_center_flipped)
    stephanie "Oh hey, there's [stephanie.mc_title]. Don't worry, I'm sure everything will be great."
    the_person "I know, I know... are you sure you don't want to go?"
    stephanie "Don't be silly, you've only got two tickets. You two will have a blast!"
    the_person "Okay..."
    "You walk over and greet the pair."
    menu:
        "Cheerful greeting\n{color=#ff0000}{size=18}Increases love{/size}{/color}":
            mc.name "Hello! Thanks for this, I've been looking forward to this ever since we arranged it. [the_person.title], you look great tonight!"
            the_person "Ah... thank you."
            $ the_person.change_stats(happiness = 2, love = 1)
            "[stephanie.title] gives you a smile after your kind words to her sister."
            $ stephanie.change_stats(obedience = 1, love = 1)

        "Sexual greeting\n{color=#ff0000}{size=18}Increases sluttiness{/size}{/color}":
            mc.name "Wow. What a couple of hotties. You could hang on my other arm [stephanie.title]."
            "[stephanie.possessive_title] rolls her eyes."
            stephanie "Yeah right. Like you could handle both of us."
            mc.name "Is that a challenge?"
            stephanie "Not this time."
            "You glance at [the_person.title]. She is blushing a bit, but you notice a slight smile."
            $ the_person.change_stats(happiness = 1, slut = 1, max_slut = 50)
            $ stephanie.change_stats(obedience = 1, slut = 1, max_slut = 50)

        "Commanding greeting\n{color=#ff0000}{size=18}Increases obedience{/size}{/color}":
            mc.name "Yeah, don't be silly. [stephanie.title] doesn't need to hear us talk about her anyway."
            the_person "Ha! I suppose I could share some secrets of hers."
            stephanie "Wow, gossiping is starting already, is it?"
            $ the_person.change_stats(happiness = 1, obedience = 1)
            $ stephanie.change_stats(obedience = 1, love = -1)
            "[stephanie.possessive_title] frowns, but otherwise doesn't protest."

    #End of love option
    stephanie "Alright you two, go enjoy your classical concert. Ash, just text me when you get done, I'm gonna go have a couple drinks."
    the_person "Okay. Bye [stephanie.title]!"
    $ scene_manager.hide_actor(stephanie)
    mc.name "Shall we?"
    $ show_concert_hall_background()
    "You step into the concert hall, show your tickets, and make you way to your seats."
    $ scene_manager.update_actor(the_person, position = "sitting")
    "You have a few minutes before the concert starts, so you try making some small talk."
    mc.name "So, have you ever been to a concert like this before?"
    the_person "Oh, a few times, when I was in college, but not for over a year."
    mc.name "I'll admit it, this is my first time going to something like this. I'm really excited to have the chance to try something new, though."
    the_person "Oh yeah? I think most guys find classical music a bit boring..."
    mc.name "I'll admit I'm not an avid follower, but I think experiencing a variety of cultural events is an important thing for someone to do."
    the_person "Yeah, that's very insightful."
    mc.name "Plus, I'm glad to be able to spend some time with you and get to know you better."
    "You notice her blush a bit, but you can also see her smile."
    $ the_person.change_stats(love = 2, happiness = 2)
    #end branch
    "Soon, the lights dim, and the music begins. It begins with a splendid piano melody."
    "You and [the_person.possessive_title] sit together silently, enjoying the music."
    "It goes through emotional highs and lows. At one point, you look over and you think you see a tear on [the_person.title]'s cheek."
    menu:
        "Hold her hand\n{color=#ff0000}{size=18}Increases love{/size}{/color}":
            "You reach down and take her hand. She jumps at the contact, but quickly takes your hand in hers as the music reaches an especially poignant moment."
            $ mc.change_locked_clarity(5)
            $ the_person.change_stats(love = 5, happiness = 5)
            "You hold hands for the duration of the concert. You both share comments now and then about specific parts that you liked."
        "Put your hand on her leg\n{color=#ff0000}{size=18}Increases sluttiness{/size}{/color}":
            "You reach down and put your hand on her thigh, just above her knee. She jumps at the contact, but puts her hand on top of yours."
            $ mc.change_locked_clarity(15)
            $ the_person.change_stats(slut = 2, happiness = 5)
            "You leave your hand on her leg for the duration of the concert."
        "Put your arm around her\n{color=#ff0000}{size=18}Increases obedience{/size}{/color}":
            "You reach your arm around her and put your hand on her shoulder. You pull her closer to you."
            "At first she is a little reluctant, but after a tug, she leans towards you and puts her head on your shoulder."
            $ mc.change_locked_clarity(15)
            $ the_person.change_stats(obedience = 2, happiness = 5)
            "You watch the remainder of the concert in silence with her head against you."
    "When the concert is over, the lights slowly come back on. You let go of her as you both start to get up."
    $ scene_manager.update_actor(the_person, position = "stand3")
    "You slowly file out of the concert hall, chatting about the concert."
    $ mc.change_location(downtown)
    "When you get outside, [the_person.title] looks around."
    the_person "Oh! I was supposed to text Steph. I was having fun and totally forgot!"
    "She pulls out her phone and texts her sister."
    the_person "Okay, she says she'll be right over... You don't have to stay, I'm sure she won't be long."
    mc.name "And leave a pretty girl like you all by herself? Not a chance."
    $ the_person.change_stats(love = 2, happiness = 2)
    "She smiles, looking down at her feet."
    mc.name "So was it everything you hoped it would be?"
    "She thinks about it before responding. One of the things you appreciate about [the_person.title] is that she always thinks before she speaks."
    the_person "It was, and more. I really had a good time tonight."
    mc.name "Great! If you hear about another orchestra in town, I'd love to go again."
    the_person "I haven't heard anything, but I'll definitely keep it in mind. I'd like to do this again."
    $ scene_manager.show_actor(stephanie)
    stephanie "Hey Ash! Hey [stephanie.mc_title]! How'd it go?"
    the_person "Steph! We had a great time. The performers were amazing..."
    stephanie "And I assume you were a perfect gentleman?"
    "[stephanie.possessive_title] gives you a look. She smiles, but you can tell she is genuinely protective of [the_person.fname]."
    mc.name "As always, [stephanie.fname]."
    the_person "He really was. Thanks again [the_person.mc_title]!"
    "It's late, so you all agree to part ways."
    mc.name "Alright, don't forget work tomorrow. I'll see you both then."
    the_person "Bye!"
    stephanie "See ya then!"
    $ scene_manager.clear_scene()
    $ ashley.set_event_day("obedience_event")
    $ ashley.set_event_day("love_event")
    $ ashley.set_event_day("slut_event")
    $ ashley.set_event_day("story_event")
    $ ashley.event_triggers_dict["concert_date"] = 2
    #Add events for Ashley's three story lines
    $ mc.business.add_mandatory_crisis(ashley_porn_video_discover)
    $ mc.business.add_mandatory_crisis(ashley_after_hours)
    $ mc.business.add_mandatory_crisis(ashley_demands_relief)
    return



#Ashley Love Path
init -1 python:
    def ashley_after_hours_requirement():
        if mc.is_at_work() and time_of_day == 3:
            if ashley.love >= 20 and ashley.story_event_ready("love"):
                return True
        return False

    def ashley_asks_about_lily_requirement():
        return False
        if ashley.love >= 40 and ashley.story_event_ready("love"):
            if mc.is_at_work() and mc.business.is_open_for_business():
                return True
        return False

    def ashley_lily_hangout_requirement():
        if time_of_day == 4:
            return True
        return False

    def ashley_lily_shopping_selfies_requirement():
        if ashley.love >= 60 and ashley.story_event_ready("love"):
            if time_of_day != 0 and day%7 == 5: #Saturday
                return True
        return False

    def ashley_lily_shopping_aftermath_requirement():
        if time_of_day == 4:
            return True
        return False

    def ashley_lily_truth_or_dare_requirement():
        if ashley.love >= 80 and ashley.story_event_ready("love"):
            if time_of_day == 4 and day%7 != 5 and day%7 != 6: #not weekend
                return True
        return False

    def ashley_steph_harem_entry_requirement():
        return False


init 1 python:
    ashley_after_hours = Action("Ashley approach you", ashley_after_hours_requirement, "ashley_after_hours_label")
    ashley_asks_about_lily = Action("Ashley asks about Lily", ashley_asks_about_lily_requirement, "ashley_asks_about_lily_label")
    ashley_lily_hangout = Action("Ashley and Lily makeup", ashley_lily_hangout_requirement, "ashley_lily_hangout_label")
    ashley_lily_shopping_selfies = Action("Ashley sends you pics", ashley_lily_shopping_selfies_requirement, "ashley_lily_shopping_selfies_label")
    ashley_lily_shopping_aftermath = Action("Ashley sneaks into your room", ashley_lily_shopping_aftermath_requirement, "ashley_lily_shopping_aftermath_label")
    ashley_lily_truth_or_dare = Action("Ashley and Lily Truth or Dare", ashley_lily_truth_or_dare_requirement, "ashley_lily_truth_or_dare_label")
    ashley_steph_harem_entry = Action("Ashley and Steph join your harem", ashley_steph_harem_entry_requirement, "ashley_steph_harem_entry_label")

label ashley_after_hours_label():   #Ashley looks for an opportunity to get MC alone, waits until after closing when Steph is for sure gone to approach him.
    $ scene_manager = Scene()
    $ the_person = ashley
    $ the_person.story_event_log("love")
    "It is the end of the day, so you swing by your office to pick up your daily serum dose."
    $ ceo_office.show_background()
    $ scene_manager.add_actor(the_person, emotion = "happy")
    "As you open the door, you see [the_person.possessive_title] standing there, waiting for you."
    mc.name "Ah, hello [the_person.title]."
    the_person "Hello [the_person.mc_title]."
    mc.name "Is there something you needed?"
    "She gives you a sly smile."
    the_person "Oh, I wouldn't say I necessarily NEED something."
    the_person "I guess... I was just thinking about how much of a favor you did for me, hiring me here."
    the_person "I know that things with Steph are a little bit... complicated."
    the_person "But I feel like I don't get to just... spend time with you very much."
    mc.name "Oh?"
    the_person "So umm, I was just wondering... can I walk you home?"
    mc.name "Oh. Umm, sure. I guess that would be alright."
    the_person "Great!"
    mc.name "Just give me a moment to finish up."
    the_person "Sure."
    "You finish closing up the business, then step out into the evening."
    $ mc.change_location(downtown)
    "As you start to make your way home, you chat a bit with [the_person.possessive_title]."
    the_person "So... I never really understood something. How DID you meet Steph, anyway?"
    mc.name "Well, the summer before my senior year, I got to do this internship at the university."
    mc.name "She was already a lab assistant, so we met while I was doing that."
    mc.name "That internship actually led to a LOT of what we are doing now."
    the_person "Huh... interesting."
    the_person "I think I remember her saying something about that, but I was pretty busy with my own thing at the time."
    "You walk a little more while [the_person.title] reflects on some things."
    the_person "Actually... I was umm... not the nicest person in university, if I'm being honest."
    the_person "I kind of ignored my sister a lot... And to be honest I kind of had a bit of a drinking problem."
    the_person "It umm... wasn't uncommon for me to wakeup at a frat house with no idea how I got there. I had more than one girl get pissed at me for screwing around with their boyfriends..."
    the_person "I've never been one for exclusive relationship myself, but for some reason, I find guys who are in relationships with other girls to be very attractive."
    "You had a suspicion of much, with how [stephanie.title] warned you about her."
    the_person "I actually quit drinking this summer though! I got fired from my other job and I could feel things almost spiraling out of control."
    mc.name "That is an admirable thing, to feel yourself at the edge of the abyss and to pull yourself back. Not everyone manages to."
    the_person "Yeah... I suppose..."
    "You continue walking, eventually you get to your house."
    "You step up to your front door."
    mc.name "Well, this is my house. I live here with my sister and my mother."
    the_person "Oh? I figured you for a bachelor type, out living alone."
    mc.name "Not yet. Maybe someday, but to be honest, I'm really hoping for the business to do well so I can take care of my family."
    $ the_person.change_love(3)
    the_person "That sounds very nice..."
    lily "I SAID FUCK OFF, ASSHOLE!"
    $ scene_manager.add_actor(lily, emotion = "angry", display_transform = character_left_flipped)
    "Suddenly, the front door swings open and a very angry [lily.title] appears."
    lily "I'M SO SICK OF... Oh."
    $ scene_manager.update_actor(lily, emotion = "happy")
    lily "Hey bro, I'm sorry, I thought... there was this guy at the mall being super creepy and who started following me home..."
    "[lily.title] smiles at you, then looks at [ashley.fname] and suddenly gets angry again."
    lily "I... hey, what the hell? What is SHE doing here?"
    $ scene_manager.add_actor(lily, emotion = "angry", display_transform = character_left_flipped)
    the_person "AGH, oh boy..."
    mc.name "What do you mean? [lily.fname], this is..."
    lily "[the_person.fname], yes, believe me, I'm familiar!!!"
    lily "Remember the boyfriend I had last year? And things were starting to get serious but I caught him cheating on me?"
    "Oh no"
    the_person "Well, it probably a good time for me to go..."
    mc.name "[lily.title], she is an employee of mine."
    if lily.is_employee():
        mc.name "I'm surprised you haven't seen her around by now."
    mc.name "She was just walking me home. Thank you for that, [the_person.title], I appreciate it."
    the_person "Umm... right... I'm gonna go ahead and bail out now."
    "[lily.possessive_title] let's out an exasperated sigh and turns around, going back inside."
    $ scene_manager.remove_actor(lily)
    mc.name "Right. Well, I'll see you at work."
    the_person "Bye!"
    $ scene_manager.update_actor(the_person, position = "kissing")
    "Suddenly, [the_person.title] puts her arms around you and gives you a hug, then plants a quick kiss on your cheek."
    "As quickly as it started, she backs away."
    $ scene_manager.update_actor(the_person,position = "walking_away")
    "[the_person.title] turns and starts to walk away. You watch her for a bit, admiring her figure, before going inside."
    $ scene_manager.clear_scene()
    "So it turns out, your sister and [the_person.possessive_title] already know each other... but definitely not in a good way."
    "If you want to get close to [the_person.title], you might have to work on repairing their relationship."
    $ mc.business.add_mandatory_crisis(ashley_asks_about_lily)
    return

label ashley_asks_about_lily_label():   #Ashley talks to MC about Lily and how she is doing. Expresses remorse for cheating issue. 40 love
    $ the_person = ashley
    "You are deep in though as your work on some algorithms related to the latest set of research results. Suddenly, a throat clearing alerts you to someone standing next to you."
    $ the_person.draw_person()
    "It is [the_person.possessive_title]."
    mc.name "Ah, hello [the_person.title]."
    the_person "[the_person.mc_title]... have a sec?"
    mc.name "Sure."
    "She steps around the desk and sits down on the other side of it."
    $ the_person.draw_person(position = "sitting")
    the_person "So. I've been thinking about the other day, when I walked you back to your house, and then the thing... with your sister?"
    the_person "I feel really bad about it. I... was wondering if maybe we could like... try something."
    mc.name "Like what?"
    the_person "I really enjoyed just spending the time with you, walking back to your place... I was kind of hoping... maybe we could hang out at your place more often."
    the_person "It would be away from Steph, so she wouldn't know about it."
    the_person "But it won't work unless I get the chance to talk to your sister and apoligize."
    mc.name "Yeah, having you come by once in a while would be problematic if she's pissed at you."
    "You think about it for a bit."
    mc.name "You know what she loves? Old comedy movies. And all the feel good vibes that go with them."
    mc.name "I'll text her and see if she wants to hang out sometime and watch one. You can come over and hang out with us, and I won't tell her you're coming."
    mc.name "It would be a good chance for you two to maybe make up a little."
    the_person "Yeah... I mean, I kind of have my doubts, but that might actually work."
    the_person "I think it'll help that you're her brother, and not her boyfriend!"
    mc.name "Oh yeah, totally."


    "In this label, Ashley approach MC at work."
    "She brings up the encounter with Lily."
    "She shares that she has this problem. She finds taken men to be extremely attractive. Makes sense why she is stealing other girls boyfriends."
    "Says she doesn't want things with Lily to cause a problem with you. Asks if she can come over sometime just to hang out."
    "Add mandatory event for hanging out at MC's house next Saturday. MC texts Lily and she agrees to hang out that time, but doesn't know Ashley is coming over."
    $ mc.business.add_mandatory_crisis(ashley_lily_hangout)
    return

label ashley_lily_hangout_label():
    $ the_person = ashley
    $ the_person.story_event_log("love")
    "In this label, MC is hanging out with Lily and then Ashley comes over."
    "Lily gets pissed, but you are able to calm her down."
    "Ashley apologizes. Lily doesn't like it, but with your insistence, agrees to try and forgive her and get long with her."
    "The girls exchange numbers. Maybe they will even hang out once in a a while?"
    "They find out they both actually like a similar clothing line at the mall. Ashley likes to shop? You had no idea."
    "They agree to hang out and go shopping once in a while. Wait... maybe this is a bad idea... is ashley going to be a good influence on Lily?"
    $ mc.business.add_mandatory_crisis(ashley_lily_shopping_selfies)
    $ town_relationships.update_relationship(lily, ashley, "Friend")
    $ ashley.event_triggers_dict["lily_friend"] = True
    return

label ashley_lily_shopping_selfies_label(): #60
    $ the_person = ashley
    "In this label, Ashley starts sending MC some selfies of both her and Lily at the clothing store trying on outfits. Asks his opinion on a bunch."
    "At the end, sends one of both them in lingerie. Says Lily needs a special outfit for some kind of photo shoot."
    "Asks which girl looks better. Regardles of how MC answers, Ashley teases MC about it."
    $ mc.business.add_mandatory_crisis(ashley_lily_shopping_aftermath)
    return

label ashley_lily_shopping_aftermath_label():
    $ the_person = ashley
    $ the_person.story_event_log("love")
    "MC goes to bed the same day after receiving the text messages from Ashley. As he is falling asleep, Ashley sneaks into his room."
    "Says she can't stay long, but strips down to the lingerie she sent selfie of earlier."
    "She teases MC, winds up riding him cowgirl before leaving."
    "Begins weekly Ashley and Lily teamup at the clothing store. If MC goes they let him rate their outfits. If MC doesn't, Ashley sends some pics of the highlights."
    $ mc.business.add_mandatory_crisis(ashley_lily_truth_or_dare)
    return

label ashley_lily_truth_or_dare_label():    #80
    $ the_person = ashley
    $ the_person.story_event_log("love")
    "In this scene, MC comes home after work and Ashley and Lily are in the living room hanging out."
    "You wind up playing truth or dare. At some point Ashley selects truth and Lily asks her if shes in love with MC."
    "She tries to refuse to answer, but eventually she admits to being in love with him, but that things are complicated."
    "Lily apologizes for prying. Says you two should really try to work things out, she thinks you are perfect for each other."
    "Adds truth or dare as available for after shopping events."
    $ mc.business.add_mandatory_crisis(ashley_steph_harem_entry)
    $ town_relationships.update_relationship(lily, ashley, "Best Friend")
    return

label ashley_steph_harem_entry_label(): #100 Love AND requires both girls to be your girlfriend from bonus scenes.
    $ the_person = ashley
    $ the_person.story_event_log("love")
    "In this scene, you convince Stephanie AND Ashley to join your harem officially."
    return



#Ashley Slut Path
init -1 python:
    def ashley_porn_video_discover_requirement():
        if ashley.sluttiness >= 20 and ashley.story_event_ready("slut"):
            if time_of_day == 4:
                return True
        return False

    def ashley_ask_sister_about_porn_video_requirement(the_person):
        if the_person.is_at_work():
            return True
        return False

    def ashley_ask_about_porn_requirement(the_person):
        if the_person.is_at_work() and the_person.days_since_event("slut_event") >= TIER_1_TIME_DELAY and time_of_day < 3:
            return True
        return False

    def ashley_post_handjob_convo_requirement(the_person):
        if the_person.is_at_work():
            return True
        return False

    def ashley_stephanie_arrange_relationship_requirement(the_person):
        if the_person.is_at_work():
            return True
        return False

    def ashley_blows_during_meeting_requirement():
        if ashley.sluttiness >= 40 and ashley.story_event_ready("slut"):
            if mc.is_at_work() and ashley.is_willing(blowjob) and mc.business.is_open_for_business():
                return True
        return False

    def ashley_supply_closet_at_work_requirement():
        return False
        if ashley.sluttiness >= 60 and ashley.story_event_ready("slut"):
            if mc.is_at_work() and ashley.is_willing(against_wall) and mc.business.is_open_for_business():
                return True
        return False

    def ashley_asks_for_anal_requirement():
        if ashley.sluttiness >= 80 and ashley.story_event_ready("slut"):
            if mc.is_at_work() and mc.business.is_open_for_business():
                return True
        return False

    def ashley_tests_serum_on_sister_requirement():
        return False

init 1 python:
    ashley_porn_video_discover = Action("Ashley emails you", ashley_porn_video_discover_requirement, "ashley_porn_video_discover_label")
    ashley_ask_sister_about_porn_video = Action("Ask Steph about porn video", ashley_ask_sister_about_porn_video_requirement, "ashley_ask_sister_about_porn_video_label")
    ashley_ask_about_porn = Action("Ask Ashley about porn", ashley_ask_about_porn_requirement, "ashley_ask_about_porn_label")
    ashley_post_handjob_convo = Action("Confront Ashley", ashley_post_handjob_convo_requirement, "ashley_post_handjob_convo_label")
    ashley_stephanie_arrange_relationship = Action("Arrange things with Stephanie", ashley_stephanie_arrange_relationship_requirement, "ashley_stephanie_arrange_relationship_label")
    ashley_blows_during_meeting = Action("Ashley blows you", ashley_blows_during_meeting_requirement, "ashley_blows_during_meeting_label")
    ashley_supply_closet_at_work = Action("Ashley is needy", ashley_supply_closet_at_work_requirement, "ashley_supply_closet_at_work_label")
    ashley_asks_for_anal = Action("Ashley one ups her sister", ashley_asks_for_anal_requirement, "ashley_asks_for_anal_label")
    ashley_tests_serum_on_sister = Action("Ashley gives you a present", ashley_tests_serum_on_sister_requirement, "ashley_tests_serum_on_sister_label")

label ashley_porn_video_discover_label():   #20 Sluttiness
    # make sure we are in the bedroom
    $ mc.change_location(bedroom)
    $ the_person = ashley
    $ the_person.outfit = the_person.wardrobe.get_random_appropriate_underwear(50, sluttiness_min = 20, guarantee_output = True) #Hopefully this gets a slutty underwear set
    $ scene_manager = Scene()
    "It's been a long day. You consider heading for bed, but you've got a lot of energy, and you'd rather not just lie awake in bed."
    "You decide to hop on your PC and watch some porn and jack off before you go to bed. That always helps you fall asleep."
    "You load up your porn accounts and start browsing through some videos."
    "'Desperate Slut Begs for Creampie'? Nah! 'Guy Fucks Step Sister Stuck In Bear Trap'? Hmm... maybe later."
    "As you browse, you notice a clip thumbnail with a girl riding a guy tied down and in restraints. She looks kinda familiar? Reminds you of someone from work maybe?"
    "'Naughty Nurse Ties Up Boyfriend. RUINED ORGASM'? Eh, it's worth a shot anyway. You click on it and wait for the generic porn intro to finish."
    "You mouth falls open when the scene starts."
    $ scene_manager.add_actor (the_person, position = "stand4", emotion = "happy")
    $ mc.change_locked_clarity(10)
    "There's a guy and a girl, who you immediately recognize as [the_person.title]. This looks like one of those hidden camera type videos."
    "In the background is what appears to be some sort of medical office."
    "The guy is tied up, with his four limbs tied to the four corners of a medical bed. You watch as [the_person.title] gets up on the examination table and crawls on top of him."
    $ scene_manager.update_actor(the_person, position = "doggy")
    "She turns and puts her ass right in his face. She starts to ride his face roughly."
    $ mc.change_locked_clarity(10)
    "[the_person.possessive_title] strokes the guy a little bit, but basically ignores his cock as she rides his face."
    "She does this for several minutes, until she starts to moan and really ride the guy roughly. Her moans get loud, it sounds like she is finishing."
    $ scene_manager.update_actor(the_person, position = "cowgirl")
    "She turns around and puts a condom on the guy. She starts to tease him."
    the_person "You want this in my pussy, bitch? Yeah right... like you deserve that."
    "Wow, she is definitely nailing the whole dominatrix role..."
    "She starts to dry hump the poor guy. With his limbs down at his sides, there's not much he can really do."
    "She keeps going, speeding up and slowing down multiple times."
    "Eventually, you can hear the guy starting to moan, it's clear he is getting ready to cum."
    "She quickly hops off. The guy fills up the condom while [the_person.title] basically ignores him."
    the_person "Pathetic... maybe someday I'll let you touch me... but not today, that's for sure!"
    $ scene_manager.clear_scene()
    "Wow... [the_person.title]..."
    "This seems pretty crazy. She seems to be some kind of closet dom? It's hard to believe."
    "And the bakground... was this done in a real hospital room?"
    "There's no way you can talk to her about it yet. Maybe you should bring it up with [stephanie.title] first?"
    $ stephanie.add_unique_on_talk_event(ashley_ask_sister_about_porn_video)
    $ ashley.event_triggers_dict["porn_discovered"] = True
    return

label ashley_ask_sister_about_porn_video_label(the_person):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person)
    mc.name "Hello [the_person.title]. I need to talk to you about something... sensitive. Could you please come with me to my office?"
    the_person "Of course."
    $ ceo_office.show_background()
    "You enter your office an gesture for her to sit down."
    $ scene_manager.update_actor(the_person, position = "sitting")
    if the_person.sluttiness > 50:
        "As she sits down, you notice [the_person.possessive_title]'s posture. She is sticking her chest out. She probably thinks you brought her to your office for some... personal time."
        $ mc.change_locked_clarity(20)
    mc.name "I wanted to talk to you again, about your sister, [ashley.fname]."
    the_person "Oh!... right..."
    if the_person.sluttiness > 50:
        "Her back slumps noticeably when you say that."
    mc.name "This is not going to be an easy or pleasant conversation, but uhh, I found a video of your sister..."
    the_person "UGH! I thought we got that deleted from everywhere."
    mc.name "Oh... deleted?"
    $ scene_manager.update_actor (the_person, emotion = "sad")
    the_person "Yeah, she had this boyfriend a while back. It came out after they broke up that he was secretly filming them having sex and posting it online..."
    the_person "Unfortunately, they were doing it while she was on break at her job..."
    the_person "We did everything we could to shut it down once we found out, but the internet is crazy. Once it's out there, it's out there!"
    mc.name "Wow, I feel awful, I had no idea."
    the_person "Someone at the hospital eventually found out about it, and that was the HR issue that wound up getting her fired."
    mc.name "Ahhh, that makes sense."
    "You both look at each other for a moment, considering the circumstance."
    the_person "As you probably saw... she is pretty... adventurous... with guys."
    the_person "I don't know why but... she has this thing, ever since we were little. Some kind of sibling rivalry."
    if the_person.is_girlfriend():
        the_person "It wouldn't surprise me she takes a pass at you, especially since we are dating."
    else:
        the_person "I umm... I wouldn't be surprised if she takes a pass at you."
    "Interesting... but you wonder if getting busy with a dom like that is really what you want to do?"
    "Maybe with some serums, you could try taming her a bit... so she can see what the other side of it is like..."
    the_person "Look umm... just so I make myself clear here... be careful with her. She can be sneaky, and knows a lot more than she lets on."
    mc.name "I understand. Thank you [the_person.title]."
    "You both walk back to the [mc.location.formal_name]."
    $ mc.location.show_background()
    $ scene_manager.clear_scene()
    $ ashley.event_triggers_dict["porn_discussed"] = True
    $ ashley.story_event_log("slut")
    $ ashley.add_unique_on_room_enter_event(ashley_ask_about_porn)
    return


label ashley_ask_about_porn_label(the_person):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person)
    "You decide to broach the difficult topic of the porn video you discovered."
    mc.name "I was hoping to talk to you about something a little sensitive. Would you mind if we went to my office?"
    the_person "Oh... sure..."
    $ mc.change_location(ceo_office)
    "[the_person.possessive_title] follows you to your office. After you enter, you close the door behind you."
    mc.name "Go ahead and have a seat."
    $ scene_manager.update_actor(the_person, position = "sitting", emotion = "sad")
    "You can tell she looks a little scared."
    mc.name "Are you okay?"
    the_person "I'm sorry sir... I'm working hard..."
    "What? She thinks you brought her here to discipline her?"
    #TODO Choice list
    mc.name "I didn't call you here to discipline you."
    $ scene_manager.update_actor(the_person, position = "sitting", emotion = "happy")
    "She looks visibly relieved."
    the_person "Oh... you're not? Then... what did you want me here for?"
    "You clear your throat. You are going to have to phrase this very carefully."
    mc.name "Well, I had a great time at the concert the other night, and honestly I've gotten very fond of you..."
    "[the_person.title] smiles and blushes a bit. She is a little shy, but so cute when she does that."
    mc.name "So, before I move on, I just want you to know that I want to support you and help you in any way that I can."
    "Her face changes to a look of confusion."
    the_person "Help with what?"
    mc.name "I'm sorry, this is a difficult topic but... I was watching some pornography before I went to bed not long ago..."
    "The look on her face changes to pure horror."
    mc.name "I... was rather shocked to see a familiar face..."
    "She begins to stutter out a response."
    the_person "That... that wasn't... I'm sorry sir that..."
    mc.name "Sorry? [the_person.title] you don't need to apologize."
    the_person "I'm... huh? I don't?"
    mc.name "Of course not, it definitely looked like you were being filmed without your knowledge."
    the_person "Yeah... I had no idea... but what happened in the vid..."
    mc.name "It was between two consenting adults. Other than the recording anyway. It's okay."
    the_person "You aren't... grossed out by it?"
    mc.name "Grossed out? Why would I be grossed out?"
    the_person "I mean... the relationship I had with my last boyfriend was... not normal."
    mc.name "Hey, everyone has kinks. I'm not here to kink-shame you."
    the_person "And I mean... I was on break, but it was on company property... well my previous company anyway."
    mc.name "As far as I'm concerned, break time is yours to do what you want, as long as you can get some privacy anyway."
    "She looks down and thinks for a bit."
    the_person "The, umm... the video. Did you watch the whole thing?"
    mc.name "Yeah... yeah I did."
    "She looks a little sheepish, but continues."
    the_person "Did you... you know... like it?"
    "Wow, the conversation appears to be turning quickly."
    mc.name "I did. You're very sexy."
    "She gets a wide smile on her face."
    the_person "I'll admit it... I kind of like it... when guys let me take over a little bit..."
    $ mc.change_locked_clarity(10)
    $ the_person.discover_opinion("taking control")
    "Good to know for certain, but this was fairly obvious at this point."
    mc.name "A little bit?"
    "She chuckles."
    the_person "You've been so nice to me... Can I return the favor?"
    mc.name "You don't need to do that..."
    the_person "Oh, but I want to..."
    "She leans closer to you and whispers."
    the_person "I really want to... I want to make you feel good..."
    $ mc.change_locked_clarity(20)
    "DAMN. You feel your pants get a little tight after that. You remember from the video the way [the_person.title] took control and rode her ex..."
    mc.name "I mean, you don't have to do that..."
    $ scene_manager.update_actor(the_person, position = "stand4")
    "She gets up and walks around your desk. You stand up too."
    the_person "It's okay. I'm going to. You just enjoy."
    "With nothing else to say, [the_person.possessive_title] reaches down and begins to stroke your cock through your pants."
    the_person "Mmmm, I can tell you want it too!"
    "[the_person.title] has some skilled hands... You close your eyes and enjoy her stroking you for a moment."
    $ mc.change_locked_clarity(20)
    "You hear a zipper, some fabric rustles for a moment, then suddenly you feel her warm hand on your dick, skin to skin. You look down and see her pulling your dick out."
    if the_person.has_taboo("touching_penis"):
        the_person "Oh my god... it's so big... You've been hiding this from me, [the_person.mc_title]?"
        "She gives you a couple eager strokes. You can only moan in response. It feels good to finally feel her hands on you."
        $ the_person.break_taboo("touching_penis")
    else:
        the_person "God, it's so big. I love getting your cock out..."
        "She gives you a couple eager strokes. You can only moan in response."
    $ mc.change_locked_clarity(20)
    "She looks into your eyes as she continues to give you a handjob."
    the_person "Alright, don't hold back now."
    call get_fucked(the_person, start_position = handjob, private = True, skip_intro = True, allow_continue = False) from _ashley_first_handjob_01
    $ scene_manager.update_actor(the_person, position = "stand3")
    $ the_report = _return
    if the_report.get("guy orgasms", 0) > 0:
        "You stand there with your eyes closed, slowly recovering. When you open them, you survey the mess you made."
    else:
        "You haven't finished, but [the_person.title] is still standing there with your dick in her hand."
    "Suddenly you hear your office doorknob click and the door start to open. You forgot to lock it!"
    $ scene_manager.add_actor(stephanie, display_transform = character_left_flipped)
    stephanie "Hey [stephanie.mc_title] sorry to bug you but... oh fuck!"
    "It doesn't take [stephanie.title] long to survey the situation."
    stephanie "Holy shit, Ash! I didn't mean... I forgot to knock! Oh fuck!"
    $ scene_manager.update_actor(stephanie, position = "walking_away")
    "[stephanie.possessive_title] turns to flee the room."
    the_person "Oh my god... Steph this isn't what you think..."
    $ scene_manager.remove_actor(stephanie)
    "[stephanie.title] slams the door as she leaves the room."
    the_person "Oh no... oh god, how am I going to explain this?..."
    the_person "I'm sorry [the_person.mc_title]. I have to go!"
    "[the_person.title] quickly rushes to leave. You've barely had time to process everything that just happened."
    mc.name "[the_person.title]..."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    the_person "Don't say anything... I just need to go..."
    $ scene_manager.remove_actor(the_person)
    "[the_person.possessive_title] quickly leaves the room."
    "Welp, you just got a handjob from [the_person.title]... and then her sister promptly walked in and witnessed the whole thing."
    "You'll have to consider how to approach both girls carefully before you talk to them next."
    $ ashley.event_triggers_dict["porn_convo_avail"] = False
    $ scene_manager.clear_scene()
    $ ashley.add_unique_on_talk_event(ashley_post_handjob_convo)
    $ jump_game_loop() # she runs after her sister so end talk with Ashley
    return


label ashley_post_handjob_convo_label(the_person):
    "You decide not to give [the_person.title] too much time to overthink what happened in your office. You swing by her desk."
    $ the_person.draw_person()
    mc.name "Hey [the_person.title]..."
    the_person "Oh... haha, yeah, I figured something like this was coming... it's okay, I'll clean out my desk and be out before you know it..."
    mc.name "Clean out your desk? I'm not firing you. Come on, let's go get some coffee."
    if the_person.should_wear_uniform():
        the_person "Oh, coffee? Ok, I'm going to change and we can go."
        $ the_person.apply_outfit(the_person.planned_outfit)
        $ the_person.draw_person()
        the_person "I'm ready."
    else:
        the_person "Oh, coffee? I'm right behind you..."
    "[the_person.possessive_title] is blushing hard. It's kind of cute actually."
    $ downtown.show_background()
    "As you step out of the office building, [the_person.title] is following along behind you. You give her a second to catch up so you can walk side by side."
    "She's looking down at her feet, you can tell she is uncomfortable."
    menu:
        "Hold her hand" if the_person.love >= 20:
            mc.name "Don't worry, [the_person.title]. I just wanted to get out of the office to chat about things. Also to limit the possibility of an interruption..."
            "You reach your hand down and take her hand in yours. It startles her a little, but she quickly looks up at you."
            mc.name "I've really been enjoying spending time with you."
            the_person "Oh... that's... nice to hear. Thank you."
            $ the_person.change_stats(love = 5, happiness = 5, obedience = 5)
        "Hold her hand \n{color=#ff0000}{size=18}Requires 20 Love{/size}{/color} (disabled)" if the_person.love < 20:
            pass
        "Reassure her":
            mc.name "Don't worry, [the_person.title]. I know we both need a chance to think about things, and I always find that coffee helps me think."
            the_person "Yeah... I suppose a coffee would be good for that..."
            $ the_person.change_stats(obedience = 5)
        "Tell her it was hot" if the_person.sluttiness >= 20:
            mc.name "Don't worry, [the_person.title]. I had a great time at the concert... and what happened in my office was fucking hot..."
            "[the_person.possessive_title] looks up at you, a bit surprised by your comment."
            the_person "Oh... I'm glad you think so..."
            $ the_person.change_stats(obedience = 5, slut = 1, max_slut = 40)
        "Tell her it was hot \n{color=#ff0000}{size=18}Requires 20 Sluttiness{/size}{/color} (disabled)" if the_person.sluttiness < 20:
            pass
    "You get to the coffee shop. You order a couple coffees and sit down in a booth across from [the_person.possessive_title]."
    $ renpy.show("restaurant", what = restaraunt_background, layer = "master")
    #TODO if Alexia still works here
    $ the_person.draw_person(position = "sitting")
    "You take a few sips of your coffee. Finally you break the silence."
    mc.name "So... obviously working in an office with your sister, we should be careful about what we do... around the office..."
    "She takes a sip. She nods a bit, but doesn't yet chip in with her opinion."
    mc.name "I mean... I would like for things to continue... Is that what you are thinking?"
    "She takes a deep breath before speaking."
    if ashley_steph_relationship_status() == "stephanie":
        the_person "Well... I mean... we're sisters, so we talk about everything. Ever since you started the business up, she's been talking about you, almost non-stop..."
        the_person "She definitely has a thing for you... it would be wrong for me to let you pursue anything further with me..."
        mc.name "I understand that, but isn't what I want important too? I've known [stephanie.fname] for years, but I've only just recently met you."
        the_person "I... I guess..."
    elif ashley_steph_relationship_status() == "ashley":
        the_person "Yeah... I mean, I guess this whole thing has just happened really fast, but I would be lying if I said it wasn't exciting me."
        the_person "I'm just not sure what to tell Steph... she means the world to me, and I feel like she might've sort of had a thing for you, but I'm not sure."
        mc.name "Yeah, that is something to consider."
    else:
        the_person "Honestly... I'm just really confused right now. Steph and I... we're sisters! She means the world to me and we talk about everything!"
        the_person "Ever since you started this business thing up, she's been talking about you non-stop. I can tell she really likes you..."
        the_person "But... I know we only just met... but I... errm..."
        mc.name "Yes?"
        "She sighs."
        the_person "I guess... I kinda like you too..."
        the_person "I know this is kinda weird but... I guess you'll just have to like... decide? Who do you want to be with more?"
    "You consider your conversation carefully before deciding on how you want to proceed."
    menu:
        "Let's keep us secret":
            mc.name "I think I know what to do, where we can all be happy."
            the_person "Oh?"
            mc.name "Alright, let me explain the whole thing before you make up your mind. What if we keep things between us strictly physical, and don't tell [stephanie.fname]?"
            the_person "Errrm... you want to do what now?"
            $ the_person.change_stats(love = -5, happiness = -5, obedience = 5)
            mc.name "Look, [stephanie.fname] was the one in the first place that told me to ask you out. She wants you to be happy, and I think she knows you're going through a dry spell."
            mc.name "I'll help take care of your physical needs... then if you happen to find another guy or if things with your sister don't work out..."
            the_person "I don't know... I'm not sure I'll be able to lie to her about this..."
            mc.name "You don't have to lie about it, just don't talk about it. It'll be just like friends with benefits... but just between you and me."
            "She is struggling with the idea a bit, but finally makes up her mind."
            the_person "I guess we could try... but if it gets weird, I'm out, okay?"
            mc.name "Okay."
            the_person "And you have to go talk to her about what happened... you know... in your office..."
            mc.name "I'm sure I can handle that."
            "She bites her lip."
            the_person "Okay... let's give it a shot."
            $ the_person.event_triggers_dict["story_path"] = "secret"
            # $ assign_jealous_sister_role(the_person, stephanie)
        "I want to be friends with both of you" if ((ashley_steph_relationship_status() == "both" or mc.charisma > 4) and not stephanie.is_girlfriend()):
            mc.name "There are a lot of feelings going on right now, but I think we all need to calm down a bit."
            mc.name "[stephanie.fname] and I go back a ways, but I just think of her as a friend."
            mc.name "I'm not going to lie, I really enjoy the way things are developing between us... but I have to be honest. I'm not looking to get tied down right now."
            the_person "Ahh... I see..."
            mc.name "I understand though, that everyone has needs. If you want some help relieving sexual tension, I'd be glad to help you out whenever you need it."
            "[the_person.title] looks confused for a moment."
            the_person "You mean... you want to be friends... with benefits?"
            mc.name "Exactly."
            the_person "Wow... I mean... I guess that would be okay..."
            $ the_person.event_triggers_dict["story_path"] = "fwb"
            the_person "I don't... I'm not sure how to talk to Steph about this though..."
            mc.name "Don't worry, I'll talk to her."
    "You drink your coffee with [the_person.title]. You are happy you were able to come up with a solution."
    the_person "This place is nice... maybe I should bring Steph here some time..."
    "Eventually you finish up. You decide to head back to the office."
    mc.name "I'm going to head back, feel free to to take the rest of the day off if you need to."
    the_person "Ahh, thank you..."
    $ mc.location.show_background()
    $ stephanie.add_unique_on_talk_event(ashley_stephanie_arrange_relationship)
    call advance_time from _call_advance_ashley_post_hj_01
    return

label ashley_stephanie_arrange_relationship_label(the_person):
    $ ashley.story_event_log("slut")
    "It's time to talk to [the_person.title]. You approach her in the lab."
    mc.name "Hey, we need to chat. Can you come with me to my office?"
    the_person "Sounds good."
    "You walk to your office. She enters first, and you close the door behind your back as you both take a seat."
    $ ceo_office.show_background()
    $ the_person.draw_person(position = "sitting")
    mc.name "So, I want to talk to you about me and [ashley.name]..."
    the_person "Yeah, I figured. Look, I know, I encouraged the whole thing, so I shouldn't be surprised when you two were messing around..."
    if ashley_is_secret_path():
        mc.name "It's not like that, [the_person.title]. Me and [ashley.fname] got caught up in the moment, yes, but we've talked it over and decided to be just friends."
        "You feel a little bit bad about trying to keep your relationship with [ashley.possessive_title] a secret, but you're sure if you play your cards right it'll be worth it long term."
        if the_person.is_girlfriend():
            the_person "I have to admit... I'm a little bit relieved to hear that. I thought I was losing my boyfriend! And to my sister!.. we haven't always gotten along, but I was really hoping it hadn't come to that."
            mc.name "I'm sorry for what happened. It won't happen again."
        else:
            the_person "I... I don't understand... Why aren't you interested in [ashley.fname]?"
            mc.name "It isn't that I'm not interested, as much as that I'm currently interested in someone else..."
            "You give [the_person.title] a wink. When she realizes what you mean, she blushes."
            the_person "Oh wow, I didn't realize that you felt the same way... Oh [the_person.mc_title]... Can we just make it official? I want everyone to know that I'm your girlfriend!"
            "Realizing that your plan to keep things secret with [ashley.title] isn't going to work unless you take things further with [the_person.title], you agree."
            mc.name "Here, let me do this, officially. [the_person.title], will you be my girlfriend?"
            the_person "Yes! Oh yay! I thought for sure you were gonna get with [ashley.fname]... I was so jealous... When I saw..."
            $ the_person.add_role(girlfriend_role)
            mc.name "I'm sorry, it won't happen again."
        the_person "... I guess I should warn you about this. This isn't the first time this has happened..."
        mc.name "Oh?"
        the_person "When we were in high school, she was too shy to get any boyfriends... sometimes when I would bring a guy home, she would try to seduce him."
        the_person "It caused a lot of friction between us. She kept claiming she was just trying to 'protect me' by weeding out the bad ones."
        the_person "Sometimes though, they would fuck for weeks before I found out about it..."
        mc.name "I see."
        the_person "Anyway, I just wanted to give you a warning that this could come up again in the future."
        mc.name "Thank you for letting me know."
        "[the_person.title] jumps up, you stand up also as she walks around the desk."
        $ the_person.draw_person(position = "kissing")
        "You puts your arms around her and you pull her close. You bring your face to hers and you kiss for a few moments. She slowly steps back."
        $ the_person.draw_person(position = "stand2")
        the_person "Alright... I'm going to get back to work. I'm so glad we got to talk!"
        "As [the_person.possessive_title] leaves the room, you wonder if you are being smart. Keeping your relationship with her sister secret, even it's only physical, might be difficult."
    elif ashley_is_fwb_path():
        mc.name "I know it seems like things between [ashley.name] and I are moving really fast, but I want you to know it probably isn't what you are thinking."
        the_person "Oh? I mean... You went on a date and then she was giving you a handjob in your office..."
        mc.name "[ashley.fname] is an interesting girl, for sure, but I'm not interested in a relationship with her. We both have some physical needs, so we've decided to be friends... With benefits..."
        if the_person.love > 50:
            the_person "Wow... Okay... I did not see that coming."
        if the_person.has_taboo("vaginal_sex"):
            mc.name "We're all adults here. She knows that if she finds someone else there's no commitment. And she knows it's the same for me, if I were to happen to start dating someone."
        else:
            mc.name "It's nothing different than what has been going on between us. Don't worry, I know you have needs too."
        the_person "That's understandable. I mean, I get it, what is going on, it just surprises me."
        the_person "It might be a little weird... you know? Getting physical with a guy who is doing the same with my sister... but you're right. We're all adults here, getting what we want from each other, consensually."
        $ the_person.draw_person(position = "stand2")
        the_person "Alright. I'm glad we got to talk about it. It makes me feel better, knowing what is going on between you two. I think I'll get back to work."
        "[the_person.possessive_title] turns and walks out of your office. Both girls are sexy, and you feel like your prospects are better if you can keep them from competing with each other for your attention."
    else:
        mc.name "I honestly was not expecting this to happen so quickly either. We went on that date, and had a great time"
        mc.name "We started with just chatting, but it was like we couldn't keep our hands off each other... And then you walked in..."
        if the_person.love > 50:
            "[the_person.title] is looking down, not making eye contact. You know she has feelings for you also, and is struggling with your newfound affection for her sister."
            the_person "That's... I mean, I guess I'm a good matchmaker, eh? I encouraged the whole thing, I shouldn't be surprised by it..."
            mc.name "And thank you for that. If it weren't for you, I never would have met [ashley.fname]."
            the_person "Yeah... Just being honest here... It's hard not to be a little jealous?"
            mc.name "I'm sorry... I'll try not to make things awkward..."
            the_person "I guess that means we probably shouldn't fuck anymore..."
            mc.name "I guess not..."
        else:
            the_person "Honestly, I'm really happy for you two. I was just caught off guard when I walked in on you two..."
            if the_person.sluttiness > 40:
                the_person "It's going to be hard for me to keep my hands off of you from now on, but my sister deserves it. We may not have always gotten along, but I'm glad she's found someone like you."
            else:
                the_person "Ash is a special girl, okay? You better take good care of her. We may not have always gotten along, but I'm glad she's found someone to make her happy."
        mc.name "Thank you. It means a lot to get your approval of this."
        $ the_person.draw_person(position = "stand2")
        "[the_person.possessive_title] stands up and smiles. It looks a little forced, but she's trying to be genuine."
        the_person "Thank you for this chat. I feel better knowing what is going on with you two. Now... I think I'll get back to work?"
        "[the_person.title] turns and leaves your office. Things got a little sticky there, but you feel like you are now in the clear to pursue things with [ashley.title] from now on."
    $ clear_scene()
    # $ stephanie.set_override_schedule(coffee_shop, the_days = [6], the_times = [0])   #Coffee scene is currently broke af
    # $ ashley.set_override_schedule(coffee_shop, the_days = [6], the_times = [0])
    # $ ashley.set_override_schedule(clothing_store, the_days = [6], the_times = [2]) #She always tries on clothes later
    # $ ashley.add_unique_on_room_enter_event(ashley_stephanie_progression_scene_action)
    $ mc.business.add_mandatory_crisis(ashley_blows_during_meeting)
    call advance_time from _call_advance_ashley_arrangement_01
    return

label ashley_blows_during_meeting_label():      #40 Sluttiness
    $ scene_manager = Scene()
    $ ashley.story_event_log("slut")
    $ mc.arousal = 0
    "You get a text from [stephanie.possessive_title]."
    $ mc.start_text_convo(stephanie)
    stephanie "Hey, can you meet me in your office? I just found something I wanted to talk to you about."
    mc.name "Sure, I'll be right there."
    $ mc.end_text_convo()
    $ ceo_office.show_background()
    "You head to your office and sit down. Soon, you hear a knock on the door."
    mc.name "Come in."
    $ scene_manager.add_actor(ashley)
    mc.name "[ashley.title]?"
    ashley "Shh, Steph is coming! Don't say a word, or she'll know what I'm doing!"
    mc.name "And what exactly are you doing?"
    $ scene_manager.update_actor(ashley, position = "blowjob", display_transform = character_left_flipped(yoffset = .35, zoom = 1.45))
    "[ashley.possessive_title] quickly slides under your desk and unzips your pants, pulling your cock out."
    mc.name "Are you serious? Is this really the right time for..."
    "[ashley.title] engulfs the entirety of your rapidly hardening cock in her mouth, stopping your words in your throat."
    $ mc.change_locked_clarity(30)
    "It only takes a few moments to reach full hardness as she starts to work your cock over with her soft lips."
    "Of course, there is another knock at the door. You look up."
    $ scene_manager.add_actor(stephanie)
    stephanie "Hey, it's me."
    mc.name "Come in and have a seat."
    stephanie "Thanks."
    $ scene_manager.update_actor(stephanie, position = "sitting")
    "[ashley.title] continues to bob her head up and down your cock while her sister sits down across from you. Somehow she is completely silent?"
    $ mc.change_locked_clarity(30)
    mc.name "What can I do for you?"
    stephanie "Ah, well, I'm having some trouble with the synthesis on one of the latest serum designs, I was wondering if you could look at it."
    "Fuck, you aren't sure you can handle science talk right now..."
    "Those pouty lips are working wonders sliding up and down your cock... you just wanna grab her by the hair..."
    $ mc.change_locked_clarity(40)
    mc.name "What issues are you having?"
    "[stephanie.possessive_title] grabs a folder from her bag and hands it to you."
    stephanie "Well, some of the new components are separating out. We tried a basic emulsifier, but they seem to be immune to normal protein binding..."
    "With your right hand, you take the folder. With your left hand, you grab [ashley.possessive_title] by the back of her hair."
    mc.name "I see. Have you tried homogenizing it?"
    stephanie "We have, actually..."
    "[stephanie.title] starts to talk about some of the other methods they've been using. You use your hand in [ashley.title]'s hair and force your cock down her throat."
    "She manages to throat you for several seconds, but eventually sputters and gags. When you let go she quickly pulls off and gasps. You pretend to cough to cover up the noise."
    $ mc.change_locked_clarity(40)
    stephanie "Ah, you okay?"
    mc.name "Yes, sorry, please continue."
    "[ashley.possessive_title] takes you in her mouth again as her sister continues to talk about the serum issue."
    "[ashley.title]'s soft mouth is working your shaft hard. There is no way you don't cum soon."
    stephanie "Actually, maybe if I homogenized the base before we mixed in the catalyst, that would help..."
    mc.name "Yes I think that sounds... good..."
    $ mc.change_locked_clarity(40)
    "You put your hand on [ashley.possessive_title]'s head and force her down again as you start to cum, right down her throat."
    $ ashley.cum_in_mouth()
    $ scene_manager.update_actor(ashley)
    "You deliver spurt after spurt of your cum down her throat before finally relaxing your grip on her hair."
    "You do your best to remain absolutely silent, but you see [stephanie.title] looking at you confused."
    $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = ashley)
    stephanie "Are you okay? You seem a little... flushed."
    mc.name "Sorry, it has been a long day and I'm a bit tired."
    stephanie "Okay... well, I'll leave you alone for now then, and I think I have some new ideas for how to deal with the issue."
    stephanie "Thanks!"
    mc.name "Anytime."
    $ scene_manager.update_actor(stephanie, position = "walking_away")
    "You watch as [stephanie.possessive_title] walks out of your office and closes the door on her way out."
    $ scene_manager.remove_actor(stephanie)
    mc.name "Holy fuck, you couldn't pick a different time to do that?"
    "[ashley.title] looks up at you from below your desk, a bit of cum she didn't manage to swallow dribbling down her chin."
    ashley "Sure, but it wouldn't have been as fun otherwise."
    $ ashley.apply_outfit(ashley.planned_outfit)
    $ scene_manager.update_actor(ashley, position = "stand3", display_transform = character_center_flipped(yoffset = 0, zoom = 1.0))
    "[ashley.possessive_title] gets up and straightens her outfit."
    ashley "Until next time..."
    $ scene_manager.clear_scene()
    "Your office now empty, you can't help but shake your head. Are you in over your head with those two sisters?"
    $ mc.business.add_mandatory_crisis(ashley_supply_closet_at_work)
    return

label ashley_supply_closet_at_work_label():   #60 sluttiness
    $ ashley.story_event_log("slut")
    "In this label, Ashley approaches MC, jealous about how much he's been banging her sister and not her."
    "Drags him into a supply closet. MC pins her to the wall."
    $ mc.business.add_mandatory_crisis(ashley_asks_for_anal)
    return

label ashley_asks_for_anal_label(): #80 sluttiness
    $ ashley.story_event_log("slut")
    "In this label, Ashley approaches MC for anal."
    "If MC has had anal with Steph, Ashley talks about how hot it was she could barely walk when you got done with her."
    "If not, Ashley wants to one up her sister getting taken anally."
    $ mc.business.add_mandatory_crisis(ashley_tests_serum_on_sister)
    return

label ashley_tests_serum_on_sister_label(): #100 sluttiness, also requires drinks out and arousal serum quest complete.
    $ ashley.story_event_log("slut")
    "In this label, Ashley calls MC to the testing room, where she has drugged Stephanie with the arousal serum."
    "Offers her sister as a 'gift' for MC's enjoyment."
    "Watches as you fuck her sister senseless. When you finish, she blows MC back to erection, then gets on top of her sister and asks for the same treatment."
    "At the end they both enter MC's harem properly."
    return


#Ashley Obedience Path
#Ashley taking command path
init -1 python:
    def ashley_demands_relief_requirement():
        if ashley.event_triggers_dict.get("mc_obedience", 0) > 30 and ashley.days_since_event("obedience_event") >= TIER_1_TIME_DELAY:
            if time_of_day == 3:
                return True
        return False

    def ashley_demands_oral_requirement():
        return False    #Current writing place
        if ashley.event_triggers_dict.get("mc_obedience", 0) > 60 and ashley.days_since_event("obedience_event") >= TIER_1_TIME_DELAY:
            if time_of_day == 3:
                return True
        return False

    def ashley_arousal_serum_start_requirement():
        if ashley.event_triggers_dict.get("mc_obedience", 0) > 100 and ashley.days_since_event("obedience_event") >= TIER_1_TIME_DELAY:
            if time_of_day == 3:
                return True
        return False

    def ashley_demands_sub_requirement(the_person):
        if ashley.event_triggers_dict.get("mc_obedience", 0) > 150 and ashley.days_since_event("obedience_event") >= TIER_1_TIME_DELAY:
            if time_of_day == 3:
                return True
        return False

    def ashley_submission_titfuck_requirement():
        if ashley.obedience > 120 and ashley.days_since_event("obedience_event") >= TIER_1_TIME_DELAY:
            # ashley_stay_after_work_setup()
            if time_of_day == 3:
                return True
        return False

    def ashley_submission_blowjob_requirement():
        return False
        if ashley.obedience > 140 and ashley.days_since_event("obedience_event") >= TIER_1_TIME_DELAY:
            if time_of_day == 3:
                return True
        return False

    def ashley_submission_fuck_requirement():
        return False    #Current writing spot
        if ashley.obedience > 160 and ashley.days_since_event("obedience_event") >= TIER_1_TIME_DELAY:
            if time_of_day == 3:
                return True
        return False

    def ashley_submission_anal_requirement():
        if ashley.obedience > 180 and ashley.days_since_event("obedience_event") >= TIER_1_TIME_DELAY:
            if time_of_day == 3:
                return True
        return False

    def ashley_submission_titfuck_taboo_restore_requirement():
        if ashley.comp_sex_record("Tit Fucks") >= 1 and ashley_submission_taboo_restore_requirement():
            return True
        return False

    def ashley_submission_blowjob_taboo_restore_requirement():
        if ashley.comp_sex_record("Blowjobs") >= 1 and ashley_submission_taboo_restore_requirement():
            return True
        return False

    def ashley_submission_taboo_restore_requirement():    #For all the taboo restoration events.
        if mc.is_at_work() and mc.business.is_open_for_business() and time_of_day == 1:
            return True
        return False

    def ashley_final_submission_requirement():
        return False

init 1 python:
    ashley_demands_relief = Action("Ashley needs relief", ashley_demands_relief_requirement, "ashley_demands_relief_label")
    ashley_demands_oral = Action("Ashley needs oral relief", ashley_demands_oral_requirement, "ashley_demands_oral_label")
    ashley_arousal_serum_start = Action("Ashley takes arousal drug", ashley_arousal_serum_start_requirement, "ashley_arousal_serum_start_label")
    ashley_demands_sub = Action("Ashley takes charge", ashley_demands_sub_requirement, "ashley_demands_sub_label")
    ashley_submission_titfuck = Action("Fuck ashley's tits", ashley_submission_titfuck_requirement, "ashley_submission_titfuck_label")
    ashley_submission_titfuck_taboo_restore = Action("Taboo restoration", ashley_submission_titfuck_taboo_restore_requirement, "ashley_submission_titfuck_taboo_restore_label")
    ashley_submission_blowjob = Action("Fuck ashley's mouth", ashley_submission_blowjob_requirement, "ashley_submission_blowjob_label")
    ashley_submission_blowjob_taboo_restore = Action("Taboo restoration", ashley_submission_taboo_restore_requirement, "ashley_submission_blowjob_taboo_restor_label")
    ashley_submission_fuck = Action("Fuck ashley over your desk", ashley_submission_fuck_requirement, "ashley_submission_fuck_label")
    ashley_submission_fuck_taboo_restore = Action("Taboo restoration", ashley_submission_taboo_restore_requirement, "ashley_submission_fuck_taboo_restore_label")
    ashley_submission_anal = Action("Fuck ashley's desk", ashley_submission_anal_requirement, "ashley_submission_anal_label")
    ashley_submission_anal_taboo_restore = Action("Taboo restoration", ashley_submission_taboo_restore_requirement, "ashley_submission_anal_taboo_restore_label")
    ashley_final_submission = Action("Ashley's serum plot", ashley_final_submission_requirement, "ashley_final_submission_label")

#These labels are for MC hitting specific personal serum requirements.
label ashley_demands_relief_label():    #at 30
    $ the_person = ashley
    "In this label, Ashley approaches MC and demands he gets her off."
    "MC seems conflicted, but ultimately sides with her and gets her off, but questions why would he take orders from her."
    $ ashley_clear_after_work_setup()
    $ mc.business.add_mandatory_crisis(ashley_submission_titfuck)
    $ the_person.story_event_log("obedience")
    $ mc.business.add_mandatory_crisis(ashley_demands_oral)
    $ ashley.event_triggers_dict["dom_fingers"] = True
    return

label ashley_demands_oral_label():  #at 60
    $ the_person = ashley
    "In this scene, Ashley again approaches MC. This time she demands he eat her out."
    "We give players the opportunity to push back and ask for a favor in return for a small obedience boost."
    "If we submit, ashley loses some obedience."
    $ ashley_clear_after_work_setup()
    $ the_person.story_event_log("obedience")
    $ mc.business.add_mandatory_crisis(ashley_arousal_serum_start)
    $ ashley.event_triggers_dict["dom_oral"] = True
    return

label ashley_arousal_serum_start_label():  #at 100
    $ the_person = ashley
    "In this scene, it starts with Stephanie texting MC asking if he has seen ashley around."
    "He replies no, goes to his office to pickup his serums."
    "Once there, Ashley tries to handcuff him."
    "This is the scene that sets MCs non consent preferences. MC can submit, roleplay, or reject."
    "At the end, Stephanie walks in and gets angry. At the end, link to MC arousal serum quest."
    $ ashley_clear_after_work_setup()
    $ the_person.story_event_log("obedience")
    $ mc.business.add_mandatory_crisis(ashley_demands_sub)
    return

label ashley_demands_sub_label():   #at 150
    $ the_person = ashley
    "In this scene, Ashley approaches MC in private and gives him handcuffs, ordering him to put them on if he knows whats good for him"
    "Depending on non con preferences, MC will either submit, partially submit, or fake submission."
    "Choice provides a big swing in Ashley's obedience"
    $ ashley_clear_after_work_setup()
    $ the_person.story_event_log("obedience")
    $ mc.business.add_mandatory_crisis(ashley_final_submission)
    $ ashley.event_triggers_dict["dom_fuck"] = True
    return

#Ashley's obedience levels
label ashley_submission_titfuck_label():  #at 20
    $ the_person = ashley
    $ first_time = the_person.event_triggers_dict.get("sub_titfuck_count", 0) == 0
    $ ashley_clear_after_work_setup()
    $ the_person.story_event_log("obedience")
    if first_time:
        $ mc.business.add_mandatory_crisis(ashley_submission_titfuck_taboo_restore)
        "It is the end of the day, so you swing by your office to pick up your daily serum dose."
        $ ceo_office.show_background()
        $ the_person.draw_person(emotion = "happy")
        "As you open the door, you see [the_person.possessive_title] standing next to your desk."
        mc.name "Ah, hello [the_person.title]."
        the_person "Oh hey. I was just dropping off your serums for you. Have a good evening."
        if the_person.tits_visible():
            "[the_person.possessive_title]'s big tits are on full display for you. They heave a little with each breath and movement she makes."
        else:
            "You check her out. Her big tits seem to bounce enticingly with each movement she makes."
    "You've got a lot of pent up energy from the day. You decide to see if you can get her to play with you for a bit."
    if first_time:
        mc.name "Hey, before you go, can I tell you something?"
        the_person "Sure?"
        mc.name "This might be a little bit forward, but... you have some really incredible tits."
        $ the_person.change_happiness(2)
        the_person "Wow. You're right. That is really forward."
        "She smiles a bit."
    else:
        mc.name "You know, you really DO have some incredible tits."
        the_person "Ah geeze. This again?"
        $ the_person.change_happiness(2)
        "She questions you, but you notice a hint of a smile on her face."
        mc.name "I mean, can you blame me?"
        the_person "Yes. Yes I can."
    $ the_person.change_arousal(20)
    "You step closer to her. Now just an arms reach away."
    if not the_person.tits_visible():
        mc.name "Can I see them?"
        "She mutters under her breath for a moment. But then nods."
        $ the_person.strip_to_tits(prefer_half_off = False)
        "You help her take her top off, and her amazing tits spill free from their prior confines."
    "You notice a red tinge on her cheeks... her nipples are hard, ready to be sucked and pinched."
    mc.name "May I?"
    if first_time:
        the_person "You... you want to play with my tits?"
        mc.name "Yes."
        the_person "Umm, sure. That would be okay."
    else:
        "She mumbles under her breath, but nods."
        the_person "Yeah... but you can only touch them!"
        mc.name "Of course."
    "You reach forward with both hands and cup her big tits. They feel soft and hot to the touch."
    "You keep your touch light for now, but grasp both of them. She sighs as enjoy feeling her up."
    "She gives a little yelp when you pinch her nipples at the same time."
    if first_time:
        the_person "Ah! Easy..."
        mc.name "I don't know. I think you like it a little rough once in a while, don't you?"
        "She falls quiet. Her silence tells you what the answer is."
    else:
        the_person "Ah! You're always so rough..."
        mc.name "You like it rough though, don't you?"
        "She falls silent. She won't admit it, but you can tell you are turning her on."
    $ the_person.change_arousal(20)
    "[the_person.title]'s breathing is getting quicker. Groping her tits is getting you really turned on as well."
    $ mc.change_arousal(20)
    $ mc.change_locked_clarity(30)
    "After a bit longer, you decide it is time to make your move. You reach down and unzip your pants, pulling out your cock."
    if first_time:
        "She gasps when she sees what you are doing."
        the_person "What... what are you doing?"
    else:
        "She sighs when she sees what you are doing."
        the_person "Oh god... not again..."
    mc.name "[the_person.title], your tits are incredible. Get on your knees, I want to feel them wrapped around my cock."
    "You are careful to frame the statement as a command, not a question. She could say no, but you feel confident she will do it."
    if first_time:
        the_person "I... I guess... maybe just this once?"
        mc.name "Of course."
    else:
        the_person "We said... we weren't going to do this again..."
        mc.name "Are you saying you don't want to? You don't want to feel my hard cock between your big juicy tits?"
        the_person "I... I shouldn't..."
        mc.name "But you do. It's okay to want to."
    "She sighs, but obediently gets on her knees."
    $ the_person.draw_person(position = "blowjob")
    if first_time:
        "This is the first time you've gotten her to submit to you like this, and the sight of her on her knees for you gets you harder."
    else:
        "You got he on her knees again. Making her submit to you like this just gets you harder."
    $ mc.change_arousal(20)
    $ mc.change_locked_clarity(30)
    "She looks up at you, just a hint of defiance in her eyes. You step forward a bit until your cock is up against her cleavage."
    "The defiance dies when she feels your cock against her hot tit flesh."
    $ the_person.change_arousal(10)
    $ the_person.break_taboo("touching_penis")
    "[the_person.possessive_title] takes her tits in her hands and wraps them around your erection. At last her enticing melons are smothering your cock."
    mc.name "Mmm, your tits are amazing. This is going to feel so good."
    "She moves her tits up and down a couple times, but the friction feels a little rough. She looks down and spits a large glob of saliva that drips down into her cleavage."
    "She works her tits around your cock, spreading her saliva all over you. She repeats this a couple more times until your member glides easily back and forth between them."
    "[the_person.title] looks up at you and starts to move up and down a bit. Her heavenly titflesh massages your dick."
    $ mc.change_arousal(20) #60
    $ the_person.change_arousal(10)
    mc.name "God you are so hot. That's it [the_person.title], fuck my cock with your big tits."
    "You let her do all the work for now. Her breasts wobble enticingly as the slide up and down your length."
    $ mc.change_arousal(20) #60
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(50)
    mc.name "You like it too, don't you?"
    $ the_person.increase_opinion_score("giving tit fucks")
    if first_time:
        mc.name "Is this your first time, letting a guy fuck those massive sweater puppies?"
        the_person "No... I've had boyfriends in the past do this... but I've never liked it... before..."
        mc.name "Well, you hadn't met me before, had you? You just needed to find the right man to make getting on your knees feel this good."
        "[the_person.title] is quiet. She is clearly enjoying herself now, but is having trouble letting herself go."
        "She has stopped moving for now as she thinks about what you said."
    elif the_person.opinion_score_giving_tit_fucks() >= 2:  #She orgasms.
        $ the_person.change_arousal(20)
        "[the_person.title] is looking up at you, but her eyes are glazing over. She's... going to orgasm?"
        mc.name "Oh my god, look at you. You are going to cum aren't you? Just from giving me a titty fuck!"
        the_person "Oh shit... Oh fuck!"
        $ the_person.change_arousal(20)
        mc.name "Look at me and tell me how much you love it and cum while you fuck me with those enormous titties you little slut!"
        the_person "Fuck! I love it! I love fucking your hot cock with my tits! Oh fuck [the_person.mc_title] I'm cumming!"
        "Her whole body starts to quake as she cums. Her tits tremble all around you as her body twitches in pleasure."
        $ the_person.have_orgasm(force_trance = True)
        "When she is finished she stops moving."
        $ mc.change_locked_clarity(100)
    else:
        the_person "That doesn't matter."
        mc.name "Of course it matters. Why are you doing this to yourself? Don't hold out on yourself. Just admit that you love it and move on."
        the_person "Love and like are two very different things."
        mc.name "Fine. Just admit that you like it. You like getting on your knees for me."
        "[the_person.possessive_title] stops moving and remains quiet. Sometimes she drives you nuts, remaining quiet when she should just be honest and submit."
    mc.name "Tired? That's okay, I can finish myself."
    "You reach down and grab her tits. You start to move yourself up down, fucking her tits in earnest."
    the_person "Ahhh, you don't need to..."
    mc.name "Nah, I can tell you are wearing out. Don't worry, I'm almost ready to cum. I can't wait to cover those tits of yours!"
    if mc_serum_cum_serum_is_active():
        "She suddenly looks up at you. She obviously knows you are on a serum now that changes you cum's properties."
        the_person "No... not on me!"
        mc.name "Of course on you. How do you think a tit fuck ends?"
    $ mc.change_arousal(40)
    $ mc.change_locked_clarity(50)
    "You speed up, hitting the point of no return. You pull out from between her tits at the last second and fire your load off all over her chest."
    $ the_person.cum_on_tits()
    $ the_person.draw_person(position = "blowjob")
    "You fire wave after wave onto her breasts. When you finish, you look down at your incredible artwork."
    mc.name "Fuck, that was amazing."
    the_person "Yes... incredible..."
    if first_time:
        "Hah! You finally got her to admit it."
    else:
        "Hah! You got her to admit it again."
    $ the_person.draw_person(position = "stand2")
    "[the_person.possessive_title] slowly stands up. A small drip of cum slowly oozes off the edge of one her breasts and onto the floor."
    if first_time:
        the_person "I can't believe I just did that."
    else:
        the_person "I can't believe I just did that. Again."
    mc.name "It's okay. I'm sure it won't be that good EVERY time."
    the_person "I need to go..."
    "[the_person.title] quickly grabs her stuff and walks away."
    $ the_person.draw_person(position = "walking_away")
    "She quickly steps out of your office and then disappears into the hall."
    $ clear_scene()
    if first_time:
        "[the_person.possessive_title] has always been a little bit hard to predict."
        "You have a feeling you are going to hear about this event again from her."
    else:
        "You sigh. Maybe now she'll be able to accept that it is okay to be the submissive partner during sex once in a while?"
        "Either way, you are sure you'll hear about this soon."


    $ ashley.sex_record["Tit Fucks"] += 1   #Make sure to augment this so the break functions
    return

label ashley_submission_titfuck_taboo_restore_label():
    $ outcome_convince = False
    $ the_person = ashley
    $ ashley.event_triggers_dict["sub_titfuck_count"] = ashley.event_triggers_dict.get("sub_titfuck_count", 0) + 1
    $ first_time = the_person.event_triggers_dict.get("sub_titfuck_count", 0) == 1
    $ the_person.draw_person(emotion = "angry")
    $ ashley.tag_sex_record("Tit Fucks")
    "[the_person.possessive_title] gives you a curt nod when she sees you walk into the room. She quickly walks over to you."
    the_person "[the_person.mc_title], I need to talk to you."
    mc.name "Okay, is everything alright?"
    if first_time:
        the_person "Umm, no? Not at all?"
        the_person "Look, I know what kind of drugs we're making around here. AND the serums I've been making you."
        the_person "It didn't take me long last night to put two and two together."
        the_person "I'm not just a pair of tits for you to fuck whenever you feel like it. Okay?"
    else:
        the_person "No? It isn't?"
        the_person "We already had this talk... but you seem to have forgotten."
        the_person "I'm not just a pair of big tits for you to fuck whenever you want to get off, okay?"

    mc.name "Are you saying you don't want to meet up now and then after closing anymore?"
    the_person "No... I'm not saying that. I'm just saying that I'm not going to stay late just to fulfill your crazy fantasies."
    if the_person.opinion_score_giving_tit_fucks() == -1:
        mc.name "Admit it though. It wasn't as bad as you were expecting."
        the_person "I mean, I didn't HATE it. But that doesn't mean I don't like it!"
    elif the_person.opinion_score_giving_tit_fucks() == -0:
        mc.name "Just admit it. Since we started doing this, you're coming around on giving tit fucks."
        the_person "I mean, I guess I'm just ambivalent about. I don't really care one way or the other, it is more the idea of it."
    elif the_person.opinion_score_giving_tit_fucks() == 1:
        mc.name "I saw the look in your eyes. You were really, truly, enjoying yourself."
        the_person "There are LOT of sex acts that are enjoyable, but that doesn't mean I have to be down for all of them!"
    elif the_person.opinion_score_giving_tit_fucks() == 2:
        mc.name "[the_person.title]... I saw the look in your eyes. You were loving every second of it."
        mc.name "I bet if I got you alone you'd do it again right now."
        "She stutters her rebuttal."
        the_person "I... yes, having your cock between my tits is amazing..."
        the_person "... but that doesn't mean I'm the kind of girl that just... drops to her knees to service her boss' big meaty cock anytime he wants!"
        mc.name "Who are you trying to convince? Exactly?"
    if the_person.opinion_score_giving_tit_fucks() < 2:
        the_person "Besides, I'm not the type to just get drop to her knees on demand."

    menu:
        # "We can avoid your sister staying late" if the_person.get_known_opinion_score("incest") > 0:
        #     mc.name "Why not [the_person.title]? I thought you told me when you walked me home the other night that you were enjoying spending time with me."
        #     the_person "That's not... I don't..."
        #     mc.name "It's okay that we enjoy spending time together, even if your sister does have feelings for me."
        #     "[the_person.possessive_title] seems torn."
        #     mc.name "I mean, at this point, we've both finished a day here with urges. If you can come to me when your sexual appetite is whet, why can't I do the same?"
        #     "She takes a deep breath and nods her approval."
        #     the_person "Fine... I'm willing to stick around after work once in a while for a little fun... but only if you reciprocate!"
        #     mc.name "Of course. That is perfectly reasonable."
        #     $ outcome_convince = True

        "I thought you liked to make me feel good\n{color=#ff0000}{size=18}Requires: Love Story Progress{/size}{/color} (disabled)":
            pass

        "You are that type of girl." if the_person.opinion_score_giving_tit_fucks() == 2:
            mc.name "You keep saying that you just aren't that type of girl, but it is obvious everytime it happens that you totally are."
            mc.name "It's okay, [the_person.title]. Boobs are sensitive. Cocks are warm. It's okay to enjoy the sensations of getting the two together."
            mc.name "You are only lying to yourself. You ARE the type of girl to drop to her knees and offer her tits for her boss' satisfaction."
            "[the_person.possessive_title] seems like she wants to argue, but even she can understand you're right."
            the_person "Fine. But don't kid yourself into thinking I'm going to take things any farther."
            $ outcome_convince = True

        "You are that type of girl.\n{color=#ff0000}{size=18}Requires: Ashley loves giving tit fucks{/size}{/color} (disabled)":
            pass

        "But it keeps happening..." if ashley.event_triggers_dict.get("sub_titfuck_count", 0) >= 3:
            mc.name "If it needs to stop why does it keep happening [the_person.title]?"
            mc.name "Let's stop pretending. You enjoy it when you service my cock with your tits once in a while."
            mc.name "I'm not saying it needs to be this way everyday, but once in a while, you need to take a turn being the submissive one."
            "[the_person.possessive_title] seems like she wants to argue, but even she can understand you're right."
            the_person "Fine. But don't kid yourself into thinking I'm going to take things any farther."
            $ outcome_convince = True

        "But it keeps happening...\n{color=#ff0000}{size=18}Requires repeated submission{/size}{/color} (disabled)" if ashley.event_triggers_dict.get("sub_titfuck_count", 0) < 3 and the_person.opinion_score_giving_tit_fucks() < 2:
            pass

        "Understood" if the_person.opinion_score_giving_tit_fucks() < 2:
            mc.name "I understand. You have boundaries and I won't cross them again without approval."
            "She looks at you suspiciously, but ultimately accepts your proposal.."
            the_person "Alright. Let's just not have this talk again, okay?"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] turns and walks back to her desk."

    if outcome_convince:
        $ mc.business.add_mandatory_crisis(ashley_submission_blowjob)
        $ ashley.event_triggers_dict["sub_titfuck_avail"] = True
        "[the_person.title] is now willing to stay after work once in a while for some discreet fun! Talk to her during the workday and she'll stay late for you."
        "For now, she's willing to let you fuck her tits, but if you can teach her to be more submissive, you're sure there's more she could do while she's on her knees for you..."
    else:
        $ the_person.change_obedience(-20)
        $ mc.business.add_mandatory_crisis(ashley_submission_titfuck_taboo_restore)
        "[the_person.title] isn't willing to make this a regular thing yet. You wonder if you can get her to be obedient if she would be willing to make this a more regular thing..."
    $ clear_scene()
    return


label ashley_submission_blowjob_label():  #140 obedience
    $ the_person = ashley
    $ first_time = the_person.event_triggers_dict.get("sub_blowjob_count", 0) == 0
    $ ashley_clear_after_work_setup()
    $ the_person.story_event_log("obedience")
    if first_time:
        $ mc.arousal = 0
        $ mc.business.add_mandatory_crisis(ashley_submission_titfuck_taboo_restore)
        "It is the end of the day, so you swing by your office to pick up your daily serum dose."
        $ ceo_office.show_background()
        $ the_person.draw_person(emotion = "happy")
        "As you open the door, you see [the_person.possessive_title] standing next to your desk."
        mc.name "Ah, hello [the_person.title]."
        the_person "Oh hey. I was just dropping off your serums for you. Have a good evening."
        if the_person.tits_visible():
            "[the_person.possessive_title]'s big tits are on full display for you. They heave a little with each breath and movement she makes."
        else:
            "You check her out. Her big tits seem to bounce enticingly with each movement she makes."
        "You've been having fun with her tits lately, and she notices you checking her out."
        the_person "Oh my... I know that look."
        "She reaches up and gives her chest a couple heaves."
        the_person "Thinking about getting that cock of yours between the girls again?"
        mc.name "Well, if I wasn't before, I certainly am now!"
        the_person "I think I'm up for that."
        "You pull your cock out from your pants."
        mc.name "Good, because I wasn't going to bother asking."
        if not the_person.tits_visible():
            the_person "Give me one moment."
            $ the_person.strip_to_tits(prefer_half_off = False)
            "She quietly strips down until her big tits spring free."
            mc.name "Damn. That never gets old."
        "[the_person.possessive_title] steps toward you, then drops to her knees."
        $ the_person.draw_person(position = "blowjob")
        $ the_person.change_arousal(20)
        "She reaches out and gives your cock a couple strokes with her hand. She spits into her hand then gives you a couple more strokes."
        "She spends several seconds getting your cock lubed up, then lets some of her saliva drop from her mouth down between her tits."
        the_person "Mmm, okay. Here we go..."
        "[the_person.title] slides your erection in between her soft, pillowy tit flesh and start to move them up and down on you."
        $ mc.change_arousal(20) #20
        "She bites her lip as she looks up at you. [the_person.possessive_title] is finally servicing you the way a good employee should."
        "You are getting so turned on, a bit of pre-cum starts to drip from the tip. You decide it is time to push her boundaries a little bit further."
        mc.name "Hang on a second."
        "She stops."
        the_person "Yeah?"
        mc.name "Look how much you are turning me on."
        "You reach down and give yourself a firm stroke, gripping hard to squeeze as much pre-cum from the shaft as you can, it gathers on the tip."
        the_person "Yeah..."
        mc.name "Taste it. Taste how much you are turning me on."
        the_person "I... what? Are you serious right now?"
        mc.name "Of course I am. Go on now, just stick out your tongue."
        the_person "I don't want to taste... that!"
        mc.name "Sure you do. Go on now."
        "You put your hand on the back of her head. You don't force her, but you give a gentle pull toward your crotch."
        the_person "I... I guess..."
        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
        "[the_person.possessive_title] licks the tip of your cock, then quickly pulls back and closes her mouth, grimacing."
        $ the_person.draw_person(position = "blowjob", special_modifier=None)
        mc.name "There, see? Damn, that was hot. You liked that, didn't you?"
        the_person "No, not at all. That's gross."
        mc.name "Aww don't talk like that. You liked it, tasting my arousal. That's what happens when you turn a man on with those big tits of yours."
        "She looks up at you, realizing what you are planning."
        the_person "Look, I licked it, can we just go back to my tits?"
        mc.name "Sure."
        "For a little bit, anyway. You think to yourself. You decide to go back to using her tits for a bit, until you have another sample of pre-cum to give her."
        "She seems relieved, and after adding a bit more saliva as lubricant, she happily wraps her tits around you and resumes pumping up and down."
        "You reach down and grab [the_person.title]'s tits. You hold them in place for her as she works them up an down."
        $ mc.change_arousal(20) #40
        "Her bust feels great as she strokes you, but you are filled with desire to take it one step further. You look down and see a long dribble of pre-cum leaking out the tip now."
        $ the_person.change_arousal(15)
        mc.name "Look, you did it again. Be a good girl and lick that up too."
        "She stops and glares up at you."
        the_person "Again? I already did it once..."
        mc.name "I know, and it felt amazing. Why don't you suck on the tip a little and make sure you get it all out this time."
        the_person "No way! I'll just lick it off again..."
        "Your subtle mind game has successfully shifted the goal again, making it seem like licking your pre-cum is a compromise."
        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
        "[the_person.possessive_title] leans forward and licks the tip again. Her tongue lingers a little longer this time, and her breath on your skin makes you twitch."
        mc.name "Mmm, wait hang on, you missed some..."
        "She circles the tip with her tongue a couple times, looking for the pre-cum she missed. Then she pulls back again."
        $ the_person.draw_person(position = "blowjob", special_modifier=None)
        mc.name "Perfect. Let's keep going."
        "You grab her tits and lean forward, pushing yourself between them. You make sure to start before she has a chance to spit on you again."
        "[the_person.title] just holds still while you use her breasts, on her knees looking up at you."
        "It doesn't take long until the friction starts to build up from the lack of saliva. You let go of her tits and then put your hand on the back of her head."
        mc.name "Mmm, it is getting kind of dry. Just stick your tongue out for a bit."
        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
        "Surprisingly, she obediently opens her mouth and sticks out her tongue. Without giving her a chance to rethink it, you pull her head toward you."
        "Her eyes close when her tongue makes contact with the shaft. Her wet, slick tongue feels heavenly as you start to slide it up and down your hardness."
        $ the_person.change_arousal(15)
        the_person "Mmmf..."
        "Was... was that a moan? This is progressing better than you expected. She starts to move her head a bit now, moving her tongue side to side as you move your hips up and down."
        $ mc.change_arousal(20)
        "Fuck it feels so good. At one point the tip of your cock rubs against her check and long strand of pre-cum connects it to you as you keeping stroking yourself with her tongue."
        "You pull back and she opens her eyes, looking up at you."
        $ the_person.draw_person(position = "blowjob", special_modifier=None)
        mc.name "It's leaking again. Now be a good girl and..."
        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
        "Before you can finish the sentence, she leans forward and sucks the tip of your cock into her mouth."
        "Her tongue swirls around the tip several times, cleaning the tip of your pre-cum, then pulls back, her lips smacking."
        $ the_person.draw_person(position = "blowjob", special_modifier=None)
        the_person "You aren't going to settle for anything less than a blowjob, are you?"
        mc.name "Nope! Those lips feel amazing."
        "You put your hand on the back of her head again. She sighs."
        the_person "Fine, just this once!"
        mc.name "Yeah, yeah, of course..."
        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
        "[the_person.possessive_title] opens her mouth obediently and leans forward, sliding the tip of your cock past her red, pouty lips."
    elif the_person.opinion_score_giving_blowjobs() < 2:
        mc.name "You know, you really DO have some incredible tits."
        the_person "Ah geeze. This again?"
        $ the_person.change_happiness(2)
        "She questions you, but you notice a hint of a smile on her face."
        mc.name "I mean, can you blame me?"
        the_person "Yes. Yes I can."

    "[the_person.title]'s head starts to bob up and down on your dick, the blowjob beginning in earnest now."
    "You savor the sensations of the busty girl, servicing you obediently with her mouth."
    "Her soft lips give you shivers as they stroke your length repeatedly."
    $ mc.change_arousal(20)
    if first_time:
        mc.name "Fuck, your mouth is incredible. "
    "You reach forward with both hands and cup her big tits. They feel soft and hot to the touch."
    "You keep your touch light for now, but grasp both of them. She sighs as enjoy feeling her up."
    "She gives a little yelp when you pinch her nipples at the same time."
    if first_time:
        the_person "Ah! Easy..."
        mc.name "I don't know. I think you like it a little rough once in a while, don't you?"
        "She falls quiet. Her silence tells you what the answer is."
    else:
        the_person "Ah! You're always so rough..."
        mc.name "You like it rough though, don't you?"
        "She falls silent. She won't admit it, but you can tell you are turning her on."
    $ the_person.change_arousal(20)
    "[the_person.title]'s breathing is getting quicker. Groping her tits is getting you really turned on as well."
    $ mc.change_arousal(20)
    $ mc.change_locked_clarity(30)
    "After a bit longer, you decide it is time to make your move. You reach down and unzip your pants, pulling out your cock."
    if first_time:
        "She gasps when she sees what you are doing."
        the_person "What... what are you doing?"
    else:
        "She sighs when she sees what you are doing."
        the_person "Oh god... not again..."
    mc.name "[the_person.title], your tits are incredible. Get on your knees, I want to feel them wrapped around my cock."
    "You are careful to frame the statement as a command, not a question. She could say no, but you feel confident she will do it."
    if first_time:
        the_person "I... I guess... maybe just this once?"
        mc.name "Of course."
    else:
        the_person "We said... we weren't going to do this again..."
        mc.name "Are you saying you don't want to? You don't want to feel my hard cock between your big juicy tits?"
        the_person "I... I shouldn't..."
        mc.name "But you do. It's okay to want to."
    "She sighs, but obediently gets on her knees."
    $ the_person.draw_person(position = "blowjob")
    if first_time:
        "This is the first time you've gotten her to submit to you like this, and the sight of her on her knees for you gets you harder."
    else:
        "You got he on her knees again. Making her submit to you like this just gets you harder."
    $ mc.change_arousal(20)
    $ mc.change_locked_clarity(30)
    "She looks up at you, just a hint of defiance in her eyes. You step forward a bit until your cock is up against her cleavage."
    "The defiance dies when she feels your cock against her hot tit flesh."
    $ the_person.change_arousal(10)
    $ the_person.break_taboo("touching_penis")
    "[the_person.possessive_title] takes her tits in her hands and wraps them around your erection. At last her enticing melons are smothering your cock."
    mc.name "Mmm, your tits are amazing. This is going to feel so good."
    "She moves her tits up and down a couple times, but the friction feels a little rough. She looks down and spits a large glob of saliva that drips down into her cleavage."
    "She works her tits around your cock, spreading her saliva all over you. She repeats this a couple more times until your member glides easily back and forth between them."
    "[the_person.title] looks up at you and starts to move up and down a bit. Her heavenly titflesh massages your dick."
    $ mc.change_arousal(20) #60
    $ the_person.change_arousal(10)
    mc.name "God you are so hot. That's it [the_person.title], fuck my cock with your big tits."
    "You let her do all the work for now. Her breasts wobble enticingly as the slide up and down your length."
    $ mc.change_arousal(20) #60
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(50)
    mc.name "You like it too, don't you?"
    $ the_person.increase_opinion_score("giving tit fucks")
    if first_time:
        mc.name "Is this your first time, letting a guy fuck those massive sweater puppies?"
        the_person "No... I've had boyfriends in the past do this... but I've never liked it... before..."
        mc.name "Well, you hadn't met me before, had you? You just needed to find the right man to make getting on your knees feel this good."
        "[the_person.title] is quiet. She is clearly enjoying herself now, but is having trouble letting herself go."
        "She has stopped moving for now as she thinks about what you said."
    elif the_person.opinion_score_giving_tit_fucks() >= 2:  #She orgasms.
        $ the_person.change_arousal(20)
        "[the_person.title] is looking up at you, but her eyes are glazing over. She's... going to orgasm?"
        mc.name "Oh my god, look at you. You are going to cum aren't you? Just from giving me a titty fuck!"
        the_person "Oh shit... Oh fuck!"
        $ the_person.change_arousal(20)
        mc.name "Look at me and tell me how much you love it and cum while you fuck me with those enormous titties you little slut!"
        the_person "Fuck! I love it! I love fucking your hot cock with my tits! Oh fuck [the_person.mc_title] I'm cumming!"
        "Her whole body starts to quake as she cums. Her tits tremble all around you as her body twitches in pleasure."
        $ the_person.have_orgasm(force_trance = True)
        "When she is finished she stops moving."
        $ mc.change_locked_clarity(100)
    else:
        the_person "That doesn't matter."
        mc.name "Of course it matters. Why are you doing this to yourself? Don't hold out on yourself. Just admit that you love it and move on."
        the_person "Love and like are two very different things."
        mc.name "Fine. Just admit that you like it. You like getting on your knees for me."
        "[the_person.possessive_title] stops moving and remains quiet. Sometimes she drives you nuts, remaining quiet when she should just be honest and submit."
    mc.name "Tired? That's okay, I can finish myself."
    "You reach down and grab her tits. You start to move yourself up down, fucking her tits in earnest."
    the_person "Ahhh, you don't need to..."
    mc.name "Nah, I can tell you are wearing out. Don't worry, I'm almost ready to cum. I can't wait to cover those tits of yours!"
    if mc_serum_cum_serum_is_active():
        "She suddenly looks up at you. She obviously knows you are on a serum now that changes you cum's properties."
        the_person "No... not on me!"
        mc.name "Of course on you. How do you think a tit fuck ends?"
    $ mc.change_arousal(40)
    $ mc.change_locked_clarity(50)
    "You speed up, hitting the point of no return. You pull out from between her tits at the last second and fire your load off all over her chest."
    $ the_person.cum_on_tits()
    $ the_person.draw_person(position = "blowjob")
    "You fire wave after wave onto her breasts. When you finish, you look down at your incredible artwork."
    mc.name "Fuck, that was amazing."
    the_person "Yes... incredible..."
    if first_time:
        "Hah! You finally got her to admit it."
    else:
        "Hah! You got her to admit it again."
    $ the_person.draw_person(position = "stand2")
    "[the_person.possessive_title] slowly stands up. A small drip of cum slowly oozes off the edge of one her breasts and onto the floor."
    if first_time:
        the_person "I can't believe I just did that."
    else:
        the_person "I can't believe I just did that. Again."
    mc.name "It's okay. I'm sure it won't be that good EVERY time."
    the_person "I need to go..."
    "[the_person.title] quickly grabs her stuff and walks away."
    $ the_person.draw_person(position = "walking_away")
    "She quickly steps out of your office and then disappears into the hall."
    $ clear_scene()
    if first_time:
        "[the_person.possessive_title] has always been a little bit hard to predict."
        "You have a feeling you are going to hear about this event again from her."
    else:
        "You sigh. Maybe now she'll be able to accept that it is okay to be the submissive partner during sex once in a while?"
        "Either way, you are sure you'll hear about this soon."


    $ ashley.sex_record["Tit Fucks"] += 1   #Make sure to augment this so the break functions
    return

    $ mc.business.add_mandatory_crisis(ashley_submission_blowjob_taboo_restore)
    $ ashley.event_triggers_dict["sub_titfuck_count"] = ashley.event_triggers_dict.get("sub_blowjob_count", 0) + 1
    return

label ashley_submission_blowjob_taboo_restore_label():
    $ outcome_convince = False
    $ the_person = ashley

    $ first_time = the_person.event_triggers_dict.get("sub_blowjob_count", 0) == 1
    $ the_person.draw_person(emotion = "angry")
    $ ashley.tag_sex_record("Blowjobs")
    "[the_person.possessive_title] gives you a curt nod when she sees you walk into the room. She quickly walks over to you."
    the_person "[the_person.mc_title], I need to talk to you."
    mc.name "Okay, is everything alright?"
    if first_time:
        the_person "No. Its not."
        the_person "First with my tits... and now with my mouth!"
        the_person "I know what you're doing now, and I'm not going to fall for it."
        the_person "I'm not just another slut for you to keep around and suck your cock whenever you want!"
    else:
        the_person "No? It isn't?"
        the_person "We already had this talk... but you seem to have forgotten."
        the_person "I'm not just a slut here to suck you off whenever you please, okay?"

    mc.name "Are you saying you don't like meeting up after work once in a while?"
    the_person "No... I'm not saying that. I'm just saying that I'm not going to stay late just to fulfill your crazy fantasies."

    menu:
        "But it keeps happening..." if ashley.event_triggers_dict.get("sub_blowjob_count", 0) >= 3:
            mc.name "If it needs to stop why does it keep happening [the_person.title]?"
            mc.name "Let's stop pretending. You love going down on me. Especially at the end when I fill your mouth with cum and you swallow every last drop."
            mc.name "Frankly, I don't understand what the problem is? Just admit that you like it. It's okay.."
            "[the_person.possessive_title] seems like she wants to argue, but even she can understand you're right."
            the_person "Fine. But just because I'm willing to suck you off once in a while, doesn't make me one of your airheaded sluts, okay?"
            mc.name "I never said you were."
            $ outcome_convince = True

        "But it keeps happening...\n{color=#ff0000}{size=18}Requires repeated submission{/size}{/color} (disabled)" if ashley.event_triggers_dict.get("sub_blowjob_count", 0) < 3:
            pass

        "Understood":
            mc.name "I understand. You have boundaries and I won't cross them again without approval."
            "She looks at you suspiciously, but ultimately accepts your proposal.."
            the_person "Alright. Let's just not have this talk again, okay?"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] turns and walks back to her desk."

    if outcome_convince:
        $ mc.business.add_mandatory_crisis(ashley_submission_fuck)
        $ ashley.event_triggers_dict["sub_blowjob_avail"] = True
        "[the_person.title] is willing to suck you off once in a while. You feel like you are finally tapping into her submissive side."
        "You can't wait. You know it is just a matter of time until she is willing to go even farther..."
    else:
        $ the_person.change_obedience(-20)
        $ mc.business.add_mandatory_crisis(ashley_submission_blowjob_taboo_restore)
        "[the_person.title] isn't willing to make this a regular thing yet. You wonder if you can get her to be obedient if you could give it another shot..."
    return


label ashley_submission_fuck_label(): #160 obedience
    $ the_person = ashley
    $ first_time = the_person.event_triggers_dict.get("sub_fuck_count", 0) == 0
    $ ashley_clear_after_work_setup()
    $ the_person.story_event_log("obedience")

    "In this event, [the_person.title] offers to give MC a blowjob, but MC refuses."
    "He bends her over his desk and fucks her roughly. She loves it."
    "At the end, MC chooses where to cum, and she gains a point towards being submissive."

    $ mc.business.add_mandatory_crisis(ashley_submission_fuck_taboo_restore)
    $ ashley.event_triggers_dict["sub_fuck_count"] = ashley.event_triggers_dict.get("sub_fuck_count", 0) + 1
    return

label ashley_submission_fuck_taboo_restore_label():
    $ outcome_convince = False
    $ the_person = ashley

    $ first_time = the_person.event_triggers_dict.get("sub_fuck_count", 0) == 1
    $ the_person.draw_person(emotion = "angry")
    "[the_person.possessive_title] gives you a curt nod when she sees you walk into the room. She quickly walks over to you."
    the_person "[the_person.mc_title], I need to talk to you."
    mc.name "Okay, is everything alright?"
    if first_time:
        the_person "Seriously? Is everything alright?"
        the_person "You don't have any limits do you? I'm not just some cum hungry slut for you to bend over everytime you get a hard on!"
    else:
        the_person "No? It isn't?"
        the_person "We already had this talk... but you seem to have forgotten."
        the_person "I'm not just a slut here to bend over and take your cock whenever you feel like it, okay?"

    mc.name "Are you saying you don't like fucking once in a while?"
    the_person "No... I'm not saying that. I'm just saying that I'm not going to stay late just to fulfill your crazy fantasies."

    menu:
        "But it keeps happening..." if ashley.event_triggers_dict.get("sub_fuck_count", 0) >= 3:
            mc.name "If it needs to stop why does it keep happening [the_person.title]? You aren't bending over my desk on accident."
            mc.name "Let's stop pretending. You love it when I bend you over and have my way with you."
            mc.name "Frankly, I don't understand what the problem is? It is completely natural for a woman to enjoy submitting to a strong male figure in that way."
            "[the_person.possessive_title] pouts for a moment, but even she can understand you're right."
            the_person "Fine. Please just... maybe we can keep this between you and me, okay? I don't want Steph to find out."
            mc.name "Sure. This will be our little secret."
            $ outcome_convince = True

        "But it keeps happening...\n{color=#ff0000}{size=18}Requires repeated submission{/size}{/color} (disabled)" if ashley.event_triggers_dict.get("sub_fuck_count", 0) < 3:
            pass

        "Understood":
            mc.name "I understand. But if you bend over my desk again, I can't promise I'll be able to resist having my way with you again."
            "She bites her lip, but nods her agreement."
            the_person "Right. We'll just keep things from getting that serious again."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] turns and walks back to her desk."

    if outcome_convince:
        $ mc.business.add_mandatory_crisis(ashley_submission_anal)
        $ ashley.event_triggers_dict["sub_fuck_avail"] = True
        "You've finally gotten [the_person.title]'s submissive side trained. She's willing to let you bend her over your desk after work is closed for the day once in a while."
        "You wonder to yourself... is this really the end of the road for her submission training? She has still one forbidden hole you haven't plundered yet..."
    else:
        $ the_person.change_obedience(-20)
        $ mc.business.add_mandatory_crisis(ashley_submission_fuck)
        "[the_person.title] isn't willing to make this a regular thing yet. You wonder if you can get her to be obedient if you could give it another shot..."
    return

label ashley_submission_anal_label():
    $ the_person = ashley
    $ first_time = the_person.event_triggers_dict.get("sub_anal_count", 0) == 0
    $ ashley_clear_after_work_setup()
    $ the_person.story_event_log("obedience")

    "In this event, MC bends [the_person.title] over his desk again."
    "After sex begins, however, he sticks a finger in her ass. Then two."
    "Once she is warmed up, he pulls out of her pussy and fucks her ass."
    "At the end, MC chooses where to cum, and she gains a point torwards liking anal sex."

    $ mc.business.add_mandatory_crisis(ashley_submission_anal_taboo_restore)
    $ ashley.event_triggers_dict["sub_anal_count"] = ashley.event_triggers_dict.get("sub_anal_count", 0) + 1
    return

label ashley_submission_anal_taboo_restore_label():
    $ outcome_convince = False
    $ the_person = ashley

    $ first_time = the_person.event_triggers_dict.get("sub_anal_count", 0) == 1
    $ the_person.draw_person(emotion = "sad")
    "[the_person.possessive_title] gives you a nod when she sees you walk into the room. She quickly walks over to you."
    the_person "[the_person.mc_title], I need to talk to you."
    mc.name "Okay, is everything alright?"
    if first_time:
        the_person "Seriously? Is everything alright?"
        the_person "I can barely walk today... Was it really not enough to have my pussy anytime you want it? You have to put it in my ass too?"
    else:
        the_person "No? It isn't?"
        the_person "I thought that you were okay with it before. I don't want it in my ass like that."
        the_person "I can barely walk today!"

    mc.name "You didn't like having your ass fucked? It seemed like you came pretty hard..."
    the_person "I'm not saying it wasn't good. But it is just so weird to take it in the ass like that. Can we please stop?"

    menu:
        "But it keeps happening..." if ashley.event_triggers_dict.get("sub_anal_count", 0) >= 3:
            mc.name "If it needs to stop why does it keep happening [the_person.title]?"
            mc.name "You bent over my desk and you were practically BEGGING me for it."
            mc.name "Let's stop pretending. You love it when I fuck you. And you don't care what hole I choose. They are all mine to use anytime, any way I want."
            mc.name "You're a slut, [the_person.title]. Stop denying it."
            "[the_person.possessive_title] pouts for a moment, but even she can understand you're right."
            the_person "I know. But you're wrong about one thing."
            the_person "I'm not just A slut, you idiot. I'm YOUR slut. That's what makes this different."
            the_person "I'm not just a set of holes for any random man to please himself with. "
            mc.name "Sure. This will be our little secret."
            $ outcome_convince = True

        "But it keeps happening...\n{color=#ff0000}{size=18}Requires repeated submission{/size}{/color} (disabled)" if ashley.event_triggers_dict.get("sub_anal_count", 0) < 3:
            pass

        "Understood":
            mc.name "I don't agree that it is weird. But if you don't want to have sex like that again, I can settle for your sweet little pussy."
            "She bites her lip, but nods her agreement."
            the_person "Right. We'll just keep things from getting that serious again."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] turns and walks back to her desk."

    if outcome_convince:
        # $ mc.business.add_mandatory_crisis(ashley_submission_anal)
        $ ashley.event_triggers_dict["sub_anal_avail"] = True
        "[the_person.title] is willing to take your cock in any hole. You mind wanders, thinking about how and when you can take advantage of her total submission to you again."
    else:
        $ the_person.change_obedience(-20)
        $ mc.business.add_mandatory_crisis(ashley_submission_anal)
        "[the_person.title] isn't willing to make anal sex a regular thing yet. You wonder if you can get her to be obedient if you could give it another shot..."
    return


#Breaking Ashley path
label ashley_second_concert_intro_label(the_person):    #120 obedience, requires first concert date complete.
    #We assume this is at the beginning of a coffee time event. Ashley is the_person and the scene is already set up.
    #MC has just bought a muffin for stephanie and sat down next to her
    $ the_person.event_triggers_dict["second_date"] = True

    "As you sit down next to [stephanie.title], [the_person.possessive_title] goes back to her phone, clearly distracted by something."
    mc.name "So... any big plans this weekend?"
    stephanie "Not for me! I was thinking maybe we could do something later tonight?"
    "[stephanie.possessive_title] gives you a little wink and puts her hand on your thigh. Suddenly [the_person.title] speaks up."
    the_person "Yes!!! Oh my god, Steph! I need to borrow your boyfriend tonight!"
    stephanie "I... errrmm... I guess?"
    the_person "The Los Angeles Philharmonic had sold out for the show tonight... fucking scalpers... but this morning they released a bunch of extra tickets. I managed to grab two!"
    stephanie "Ok... but... why do you need to borrow my boyfriend?"
    the_person "I mean, I know you hate going to classical shows, and I don't know anyone else who would want to go... Please? It's just one night!"
    "[stephanie.title] mumbles something under her breath. She is clearly not happy with the situation, but relents."
    stephanie "I guess..."
    "She leans over and whispers in your ear."
    stephanie "Don't let her get handsy with you again..."
    "[stephanie.possessive_title]'s hand moves to your crotch, giving it a couple quick strokes."
    $ mc.change_locked_clarity(10)
    stephanie "I know she's hot, but you're MY boyfriend. Got it?"
    "Well, sounds like the two sisters have made plans for you tonight. From the excitement on [the_person.title]'s face, you decide to go with it."
    "You nod at [stephanie.title]."
    mc.name "Sounds good. When do you want to meet [the_person.title]?"
    the_person "Meet me there at 6:30. I'll text you the address!"
    stephanie "I don't know..."
    the_person "Relax Steph! I'm sure [the_person.mc_title] will be a perfect gentleman."
    stephanie "It's not him I'm worried about!"
    "Desperate to defuse the situation, you take control of the conversation."
    mc.name "We'll go to the concert, then I'll bring her straight home. I'll have her home by, say, 10? If you're still up we can hang out a bit."
    stephanie "Why don't you stay the night?"
    "[stephanie.title] is getting territorial. You decide for now to indulge her."
    mc.name "Okay. I'll plan to stay the night."
    "You take a sip of your coffee. It seems the sisters are finally ready to move on with their conversation."
    $ mc.business.event_triggers_dict["girlfriend_sleepover_scheduled"] = True
    $ mc.business.add_mandatory_crisis(ashley_second_concert_date)
    return



#Obedience line finale

label ashley_final_submission_label():
    "In this label, things come to a head with Ashley."
    "If we got her to submit, she admits she's been trying to get MC to obey her by lacing his serums."
    "If MC is submissive, she prepares a final 'male bimbo' dosage."
    "If Stephanie is still on good terms with MC, she stops her."
    "If Stephanie is a bimbo another employee with high love stat walks in and stops things before they can progress."
    "If none of those things are true... possible bad end? Or large setback?"
    $ mc.business.event_triggers_dict["ashley_submission_complete"] = True
    return


#Bonus scenes.
init -1 python:
    def ashley_repeatable_after_hours_requirement(the_person):
        return False

    def ashley_asks_for_second_date_requirement():
        if ashley_lily_are_friends() and ashley_dom_oral_avail():
            if ashley.days_since_event("story_event") >= TIER_1_TIME_DELAY:
                if mc.is_at_work() and mc.business.is_open_for_business():
                    return True
        return False

    def ashley_second_concert_date_requirement():
        if time_of_day == 3 and day%7 == 4:  #Friday
            return True
        return False

    def ashley_steph_second_date_confrontation_requirement():
        if time_of_day == 1:
            return True
        return False

    def ashley_sneaks_over_requirement():
        if ashley.love > 60 and ashley.sluttiness > 60:
            if time_of_day == 4 and ashley.days_since_event("story_event") >= TIER_1_TIME_DELAY:
                return True
        return False

    def ashley_steph_drinks_out_requirement():
        return False


init 1 python:
    ashley_repeatable_after_hours = Action("Ashley needs relief crisis", ashley_repeatable_after_hours_requirement, "ashley_repeatable_after_hours_label")
    ashley_asks_for_second_date = Action("Ashley asks for a second concert date", ashley_asks_for_second_date_requirement, "ashley_asks_for_second_date_label")
    ashley_second_concert_date = Action("Ashley's second concert date", ashley_second_concert_date_requirement, "ashley_second_concert_date_label")
    ashley_steph_second_date_confrontation = Action("Stephanie breaks up with you", ashley_steph_second_date_confrontation_requirement, "ashley_steph_second_date_confrontation_label")
    ashley_sneaks_over = Action("Ashley spends the night", ashley_sneaks_over_requirement, "ashley_sneaks_over_label")
    ashley_steph_drinks_out = Action("Ashley and Steph bar date", ashley_steph_drinks_out_requirement, "ashley_steph_drinks_out_label")

label ashley_repeatable_after_hours_label():
    $ the_person = ashley
    if not ashley.is_employee():
        return
    # stage 1, set the scene. You walk in on Ashley at the end of the day in your office.


    #stage 2, determine if ashley is controlling or MC
    $ dom_attempt = False
    if ashley_dom_finger_avail():
        if ashley_dom_fuck_avail():
            the_person "Hey, sit in your chair and put your handcuffs on. I have needs and I know just how I want them met."
        elif ashley_dom_oral_avail():
            the_person "Hey, I could really use a good orgasm right now. I want to sit on your desk while you go down on me again."
        else:   #She has taken control atleast once.
            the_person "Hey, while were here... alone..."
            the_person "I could really use a good orgasm. Could you use your fingers and get me off again?"
        call ashley_obedience_struggle() from _ashley_crisis_obedience_check_01
        $ dom_attempt = _return
    else:
        the_person "Well, I think I'll get going now..."
    if dom_attempt: #She is successful and has her way with MC
        "In this section, we replay a scene where Ashley has her way with MC."
        "These scenes still need to be written."
        $ ashley.change_obedience(-2)
    else:
        #Next, determine if MC wants to try and take charge.
        if the_person.event_triggers_dict.get("sub_titfuck_count", 0) >= 1 and not ashley_sub_titfuck_avail() and ashley.obedience > 120:
            mc.name "I have a better idea."
            "You've been working on getting her to obediently service you with her tits lately, and you feel like you've pushed her obedience far enough to try again."
            call ashley_submission_titfuck_label() from _ashley_random_crisis_sub_titfuck_scene_01
            return
        "You think about it for a moment. Maybe you should try and take charge? Maybe you should order HER to do something!"
        menu:
            "Demand tit fuck" if ashley_sub_titfuck_avail():
                "Sorry, I haven't written this yet!"
                pass
            "Demand blowjob" if ashley_sub_oral_avail():
                "Sorry, I haven't written this yet!"
                pass
            "Demand bare sex" if ashley_sub_fuck_avail():
                "Sorry, I haven't written this yet!"
                pass
            "Demand anal sex" if ashley_sub_anal_avail():
                "Sorry, I haven't written this yet!"
                pass
            "Demand tit fuck\n{color=#ff0000}{size=18}Not obedient enough{/size}{/color} (disabled)" if ashley_sub_titfuck_avail():
                pass
            "Demand blowjob\n{color=#ff0000}{size=18}Not obedient enough{/size}{/color} (disabled)" if ashley_sub_oral_avail():
                pass
            "Demand bare sex\n{color=#ff0000}{size=18}Not obedient enough{/size}{/color} (disabled)" if ashley_sub_fuck_avail():
                pass
            "Demand anal sex\n{color=#ff0000}{size=18}Not obedient enough{/size}{/color} (disabled)" if ashley_sub_anal_avail():
                pass
            "Just mess around":
                pass
            "Just say goodnight.":
                mc.name "Goodnight [the_person.title]."
                the_person "Goodnight then."
                "You leave your office."
                return

    return

label ashley_asks_for_second_date_label():  #requires 40 love and 60 mc obedience scenes complete.
    "In this label, Ashley interrupts a conversation MC is having with Steph."
    "Asks Steph if she can steal you for a second concert date. Steph has reservations but relents."
    "Sets up the second concert date."
    $ mc.business.add_mandatory_crisis(ashley_second_concert_date)
    return

label ashley_second_concert_date_label():
    $ the_person = ashley
    $ arousal_gain = __builtin__.round((100 - the_person.arousal) / 4)
    $ date_outcome = None
    $ cum_clue = False
    $ caught_ashley_cheating = False
    $ the_person.planned_outfit = the_person.wardrobe.get_outfit_with_name("Ashley Night Out Outfit") or the_person.get_random_appropriate_outfit(guarantee_output = True)
    $ the_person.apply_outfit(the_person.planned_outfit)
    $ the_person.event_triggers_dict["second_date_complete"] = True
    $ ashley.set_event_day("story_event")
    "Evening falls and soon it is time to make your way downtown to meet [the_person.title], your girlfriend's sister, for a date to another classical music concert."
    "Things with the two girls have gotten complicated. [ashley.fname] has been able to keep things between you a secret from her sister, but is getting more and more demanding and needy."
    "Lately it seems like [stephanie.title] is getting a little suspicious, and [the_person.possessive_title]'s demand to share you for a date is certain to have her unsettled."
    $ mc.change_location(downtown)
    "When you arrive, you looked around for a minute, but don't see [ashley.fname] yet at your agreed on meeting place. You decide to give her a few minutes. You are just about to pull out your phone and text her when you see her approaching."
    "She is wearing a sexy black dress, and your eyes are immediately drawn to its curves. There's not a doubt in your mind that [the_person.title] has something planned for you this evening..."
    $ mc.change_locked_clarity(20)
    $ the_person.draw_person()
    ashley "Hey! My eyes are up here."
    mc.name "Yeah but I wasn't looking at your eyes."
    "When you finally lift your eyes from her body and meet hers, she has a mischievous smile."
    ashley "Good. God I finally get you all to myself for one evening."
    mc.name "Are we still going to the concert?"
    ashley "Of course! I wasn't lying, and I'll be damned if I miss the opportunity to see the Los Angeles Philharmonic. Tickets weren't cheap you know! And my cheapskate boss barely pays me enough to cover the cost of living."
    "Wow, she is pretty sassy this evening. You tease each other a bit more but make your way into the concert."
    $ show_concert_hall_background()
    "As you take your seats, you try and fit in one last remark."
    mc.name "I would think as an intern, YOU should be the one on your knees under the desk servicing the boss during the workday, not the other way around."
    "A couple people near you give you a questioning look, but seem relieved when [the_person.title] starts to laugh."
    $ the_person.draw_person(position = "sitting")
    ashley "Thanks, I'll try to remember that for my next performance review."
    "You sit down beside [the_person.possessive_title]. You are a bit surprised when she takes your hand and holds it."
    "Even though things between you are supposed to be just physical, you have to wonder... Is she catching feelings for you? Normally, a situation with two sisters and one man could only possibly end in disaster."
    "But with the serums... Maybe you could eventually convince the two girls that they can both get what they want? You decide to plant that seed now, and see how she reacts."
    mc.name "You know what? I can't wait."
    ashley "Oh? What for?"
    mc.name "When we can go do stuff like this more often, then go back to your place after, and me, you, and [stephanie.fname] all hop in bed together and screw until the sun comes up."
    ashley "Ha! Oh wow. You've been watching some good porn lately huh? I don't think Steph is really the sharing type... I'm usually not either..."
    mc.name "And yet, here you are, with your sister's boyfriend. Maybe you just haven't met someone worth sharing before?"
    "[the_person.title] is quiet. Right on cue, the lights turn down and the music begins."
    $ show_concert_hall_background(darken = True)
    "The music begins, playing through some classical music that you aren't familiar with, but it is quite enjoyable. When you look over at [the_person.possessive_title] she seems to be really enjoying herself."
    "After a while, as the music goes through a crescendo, you feel her squeeze your hand, then turn it over, so her palm is against the back of your hand."
    "She puts your hand on her leg, then slowly starts to push it up, under her dress..."
    $ mc.change_locked_clarity(15)
    $ the_person.change_arousal(arousal_gain)
    "You are delighted but not surprised to discover she isn't wearing any panties. She lets go of your hand and takes a quick peek around."
    "With the darkness in the room, no one notices your hand under her dress as you slowly start to push a finger inside her cunt."
    "[the_person.title]'s body responds rapidly to your touch. After barely a minute her pussy is soaked, and you can see her chest rising and falling faster out of the corner of your eye."
    "The angle is rough, but you do your best to rub the palm of your hand against her clit as you finger her."
    "Her hips are beginning to wiggle gently in her seat as she squirms at your touch. You feel like she has to be close to cumming."
    $ the_person.change_arousal(arousal_gain)
    "What happens next surprises even you. She grabs your hand and stops you. You can't help but look at her questioningly. She leans over and whispers to you."
    ashley "Go slow. It'll be more fun if you take your time..."
    "She takes your hand and brings it back to her cunt, but this time she lifts her hips slightly and sits on it. She slowly grinds herself down on your hand."
    $ mc.change_locked_clarity(20)
    $ the_person.change_arousal(arousal_gain)
    "She is using your hand to edge herself?"
    "As the music continues, [the_person.possessive_title] keeps stimulating herself with your hand. Sometimes she goes completely still, letting herself calm down."
    "Other times she lets you push your fingers back inside her for a minute or two, and other times just grinding against it. However, she never lets herself cum; each time she gets close, she stops. Your cock is getting uncomfortably hard."
    "The music seems to be winding down. Is she going to let herself finish?"
    mc.name "You umm..."
    ashley "Of course. But not here. I decided earlier when I cum I want your face between my legs, not your hand..."
    $ mc.change_locked_clarity(30)
    "You slowly pull your hand away from her crotch. It's been wet with her arousal for so long it's starting to get a little wrinkled. She opens her clutch and starts to pull out a handkerchief, but you have another idea."
    "You bring it to your mouth and taste it. Her flavor is musky but sweet. You can't wait to taste the source."
    "[the_person.title] just watches as you clean your fingers."
    $ show_concert_hall_background()
    "The lights come back on and people start to get up. You can see [ashley.title]'s chest rising and falling rapidly. She is breathing heavy and is really turned on."
    $ the_person.draw_person()
    mc.name "Well, I promised to get you home straight away."
    "You give her a wink as you say it. She chuckles and winks back."
    $ mc.change_location(downtown)
    "You step outside and start to walk her home. However, as you pass an empty alleyway, you feel her hand tug at yours as she drags you back into the alley."
    "You both take a quick look around. Certain that you are alone, you push her up against the wall."
    $ the_person.draw_person(position = "kissing")
    "[the_person.possessive_title] moans as you kiss her neck. You feel her hands on your shoulders, pushing you down on your knees."
    "You go with it. You're sure that after all that edging, she is probably close to cumming anyway."
    $ the_person.draw_person(position = "against_wall")
    "[the_person.title] props her leg up on a box, giving you easy access to her cunt. As you start to lick along the inside of her thighs, she runs her hands through your hair."
    the_person "Mmm, do a good job and I'll repay the favor..."
    "If you do good, she'll probably repay you. But you should be careful, you still have to go see [stephanie.possessive_title] later! If you make it too obvious, she'll probably know something is up..."
    call fuck_person(the_person, start_position = standing_cunnilingus, skip_intro = True, position_locked = True, private = True) from _call_sex_description_ashley_second_date_cunnilingus_01
    $ the_report = _return
    #TODO make sure MC arousal stays the same?
    if the_report.get("girl orgasms", 0) == 0:
        $ the_person.draw_person()
        "[the_person.title] puts her leg down. She is incredulous."
        the_person "Seriously? [stephanie.fname] really has you wrapped around her finger, doesn't she? I don't know why I bother with you..."
        $ the_person.change_stats(happiness = -10, obedience = -5)
        "She seems pretty pissed you couldn't even get her off."
    elif the_report.get("girl orgasms", 0) == 1:
        $ the_person.draw_person()
        "[the_person.title] puts her leg down. She gives you a little smile."
        the_person "Mmm... not bad... but honestly, I was expecting more."
        menu:
            "Lean in for a kiss":
                "When you stand up, you lean in for a kiss, but she pushes against you to keep her distance."
                the_person "Easy now, remember where that tongue just was?"
                the_person "Look, I'll give you a handy... an orgasm for an orgasm, okay?"
                "[the_person.possessive_title] reaches down and undoes your fly. You look down and see her pulling your dick out."
                $ mc.change_locked_clarity(20)
                "She looks into your eyes as she starts to give you a handjob."
                the_person "Alright, don't hold back now."
                $ date_outcome = "handjob"
                call get_fucked(the_person, start_position = handjob, the_goal = "get mc off", private = True, skip_intro = True, allow_continue = False) from _ashley_handjob_second_date_01
                $ the_report = _return
                if the_report.get("guy orgasms", 0) > 0:
                    if the_person.has_face_cum():
                        if the_person.outfit.has_dress():
                            "[the_person.possessive_title]'s face is covered in your cum. Somehow, it doesn't seem like any of it got on her dress..."
                        else:
                            "[the_person.possessive_title]'s face is covered in your cum. Thankfully her dress came off at some point, so no cum dripped on it."
                    elif the_person.has_mouth_cum():
                        "[the_person.possessive_title] has a bit of cum on her chin, but is able to quickly clean it up."
                    elif the_person.has_tits_cum():
                        if the_person.outfit.has_dress():
                            "[the_person.possessive_title]'s chest looks great covered in your cum. But you slowly realize... it's all over her dress."
                            $ cum_clue = True
            "Tease her":
                "You stand up and tease her."
                mc.name "Wow, complaining about a free orgasm? Doesn't matter, I'm about to go back to your place and get my world rocked anyway."
                the_person "Geeze, okay. I was about to offer you a handjob as thanks, but I guess you'd better save that load then champ."
                "[the_person.possessive_title] pulls a couple wipes from her clutch and wipes herself clean."
    elif the_report.get("girl orgasms", 0) == 2:
        $ the_person.draw_person(position = "kissing")
        "When you finish, you start to stand up. [the_person.possessive_title]'s legs are a little wobbly, and she reaches out for you for support."
        the_person "Fuck that was nice... you made me cum twice!"
        "You lean in and start to make out. Her tongue searches out yours eagerly, tasting herself on your tongue. You make out for several seconds before she backs away."
        the_person "God, I don't think my legs work anymore! I'd better get down on my knees I guess..."
        menu:
            "Stop her":
                mc.name "What are you doing? This is supposed to be a one way thing. I'll cum in your sister later."
                the_person "You're serious? Why not do both?"
                mc.name "I promised her I wouldn't go too far. You got your satisfaction, I'll get mine later."
                the_person "Geeze, okay. I was about to offer to drink your cum as thanks, but I guess you'd better save that load then champ."
                "[the_person.possessive_title] pulls a couple wipes from her clutch and wipes herself clean."
            "Let her continue":
                $ the_person.draw_person(position = "blowjob")
                "As she gets down on her knees, she quickly undoes your zipper and pulls your cock out."
                "She gives it a couple strokes, then looks up at you and smiles."
                the_person "You'd probably better cum in my mouth... don't want to get it all over my clothes before we go back and see [stephanie.fname]."
                $ mc.change_locked_clarity(30)
                $ date_outcome = "blowjob"
                "You put your hand on the back of her head."
                mc.name "You say that like you have a choice."
                "She smirks for a second, but quickly opens her mouth as you pull her head down. Her velvet lips wrap around you and start to eagerly suck you off."
                call get_fucked(the_person, the_goal = "oral creampie", private= True, start_position = blowjob, skip_intro = True, ignore_taboo = True, allow_continue = False) from _ashley_second_date_blowjob_01
                $ the_report = _return
                if the_report.get("guy orgasms", 0) > 0:
                    if the_person.has_face_cum():
                        if the_person.outfit.has_dress():
                            "[the_person.possessive_title]'s face is covered in your cum. Somehow, it doesn't seem like any of it got on her dress..."
                        else:
                            "[the_person.possessive_title]'s face is covered in your cum. Thankfully her dress came off at some point, so no cum dripped on it."
                    elif the_person.has_mouth_cum():
                        "[the_person.possessive_title] has a bit of cum on her chin, but is able to quickly clean it up."
    else:
        $ the_person.draw_person(position = "standing_doggy")
        "When you finish, [the_person.possessive_title]'s legs wobble, then start to give out. She catches herself up against the wall but has trouble standing up."
        $ the_person.change_stats(happiness = 10, obedience = 5, love = 5, slut = 2)
        the_person "Fuck that was good... where the hell have you been all my life?"
        "She tries to stand up for a second, but quickly leans against the wall again."
        the_person "My legs... they don't work... I'm going to have to pay you back for this another time. Don't worry I swear I'm good for it."
        menu:
            "Take her against the wall" if the_person.is_willing(SB_facing_wall):
                mc.name "I'm not sure I believe you. I think I'll take my reward like this."
                the_person "I'm sorry... you what?"
                $ the_person.draw_person(position = "back_peek")
                "You pull your cock out, then push her roughly against the wall, pinning her to it."
                the_person "Oh fuck! You'd better wrap that thing up, or my sister will figure out what we did!"
                menu:
                    "Take her raw":
                        $ date_outcome = "raw sex"
                        $ mc.condom = False
                        "You growl at [the_person.possessive_title]."
                        mc.name "You let me worry about [stephanie.fname]."
                        "Without waiting for further response, you line yourself up and push your cock into [the_person.title]'s drenched pussy."
                    "Put on a condom":
                        $ date_outcome = "protected sex"
                        $ mc.condom = True
                        mc.name "Good idea."
                        "You quickly pull a condom out of your wallet and put it on."
                        "You line yourself up and push your cock into [the_person.title]'s drenched pussy."
                "You slide in easily after her multiple orgasms."
                call fuck_person(the_person, start_position = SB_facing_wall, skip_intro = True, position_locked = True, private = True, skip_condom = True) from _call_sex_description_ashley_second_date_fuck_01
                $ the_report = _return
                if the_report.get("guy orgasms", 0) == 0:
                    "You decide to pull out before you finish. You want to give your load to [stephanie.possessive_title] later..."
                elif the_person.has_creampie_cum():
                    "When you look down, you can see some cum running down the inside of [the_person.possessive_title]'s legs, but it doesn't seem like any got on her clothes."
                elif the_person.has_ass_cum():
                    if the_person.outfit.has_dress():
                        "[the_person.possessive_title]'s ass looks amazing covered in your cum. But you slowly realize... it's all over her dress."
                        $ cum_clue = True
                    else:
                        "[the_person.possessive_title]'s ass looks amazing covered in your cum. Thankfully her dress came off at some point, so no cum got on it."
                elif the_person.has_face_cum():
                    if the_person.outfit.has_dress():
                        "[the_person.possessive_title]'s face is covered in your cum. Somehow, it doesn't seem like any of it got on her dress..."
                    else:
                        "[the_person.possessive_title]'s face is covered in your cum. Thankfully her dress came off at some point, so no cum dripped on it."
            "Help her recover":
                mc.name "I understand. Here, let me help you."
                "You grab her arm and help her stand. It takes her several minutes, but she finally gets her legs back."
                $ the_person.draw_person()
    if date_outcome:
        if cum_clue:
            the_person "Oh fuck... it's all over my dress!"
            "[the_person.possessive_title] gets some wipes from her clutch, but despite wiping it down as best she can, it is still obvious she's been sprayed down."
            the_person "Well... maybe my sister won't notice?"
            mc.name "Yeah. Maybe."
            "There's no way [stephanie.possessive_title] doesn't notice. But you have to get her home..."
        else:
            the_person "Damn that was hot... let me just clean up real quick..."
            $ the_person.apply_outfit(the_person.planned_outfit)
            $ the_person.draw_person()
            "[the_person.possessive_title] gets some wipes from her clutch and straightens her clothes out."
    "You take a couple wipes for yourself, cleaning your face and hands of her juices."
    the_person "Alright, ready to escort me home like a gentleman?"
    $ mc.change_location(the_person.home)
    $ scene_manager = Scene()
    $ scene_manager.add_actor(ashley)
    $ scene_manager.add_actor(stephanie, display_transform = character_center_flipped)
    "You walk into [the_person.title] and [stephanie.possessive_title]'s apartment. Of course, she is right there waiting for you."
    stephanie "You're here! I was starting to get worried."
    if cum_clue:
        "[the_person.title] quickly starts walking toward the hall. [stephanie.title] raises an eyebrow."
        the_person "Hey sis, sorry I gotta pee really bad!"
        $ scene_manager.update_actor(ashley, position = "walking_away")
        "As she walks by [stephanie.possessive_title]..."
        stephanie "Hey, you got something on your dress..."
        $ stephanie.change_stats(happiness = -10, love = -5)
        $ scene_manager.remove_actor(the_person)
        "[the_person.title] disappears into the restroom, leaving you with [stephanie.title]. You can tell she is suspicious, but for now, she decides not to say anything about it."
    else:
        the_person "Hey sis! We had a great time, and don't worry, your boyfriend was a gentleman."
        stephanie "Ah, that's good."
        the_person "I'm worn out. I think I'm going to go have a shower. You two try to keep it down so I can get some sleep tonight, okay?"
        stephanie "No promises."
        $ scene_manager.remove_actor(the_person)
        "[the_person.title] disappears into the restroom, leaving you with [stephanie.title]."
    $ scene_manager.update_actor(stephanie, position = "kissing")
    "She gives you a hug and whispers in your ear."
    stephanie "I'm so glad to finally have you for myself. Let's go to my room!"
    $ scene_manager.clear_scene()

    $ stephanie.change_to_bedroom()
    $ stephanie.draw_person(position = "walking_away")
    "You follow [stephanie.possessive_title] to her bedroom. She closes the door, then pushes you back onto her bed."
    "She strips down in front of you."
    $ stephanie.strip_outfit(position = "stand4")
    "She climbs up on top of you and starts to undo your pants. Soon, your cock springs free."
    $ stephanie.draw_person(position = "cowgirl")
    stephanie "Mmm, I've been thinking about riding on this all night. Let's get you nice and hard."
    "[stephanie.title] leans forward and licks all around the top of the shaft, then starts to suck on the tip."
    $ mc.change_locked_clarity(30)
    if (date_outcome == "handjob" and not cum_clue) or date_outcome is None:
        "Her tongue swirls all around you, licking up your pre-cum. Soon you are hard as a rock."
    elif date_outcome == "handjob" and cum_clue:
        "She pulls off for a bit, giving you a few strokes with her hand."
        stephanie "I need to be honest... it looked like Ash had a little something on her dress... you two didn't get naughty again did you?"
        menu:
            "Of course not (Lie)":
                mc.name "I would never do that to you."
                stephanie "Hmm... okay... I think I believe you..."
                "She starts to suck on your cock again. Her tongue swirls all around you, licking up your pre-cum and soon you are hard as a rock."
    elif date_outcome == "blowjob" and not cum_clue:
        "She pulls off for a bit, giving you a few strokes with her hand."
        stephanie "You taste kind of funny... you and Ash didn't do anything naughty, did you?"
        menu:
            "Make up an excuse (Lie)":
                mc.name "No, but I have to be honest about something."
                stephanie "Oh? About what?"
                mc.name "I was a little worried I might get tempted... so I masturbated beforehand."
                stephanie "Oh! I guess that makes sense..."
                "She starts to suck on your cock again. You think she bought your excuse."
                "Her tongue swirls all around you, licking up your pre-cum and soon you are hard as a rock."
    elif date_outcome == "blowjob" and cum_clue:
        "She pulls off you."
        $ stephanie.draw_person(position = "cowgirl", emotion = "angry")
        stephanie "You taste funny... and Ash... that was cum on her dress, wasn't it!?!"
        menu:
            "Make up an excuse (Lie)" if mc.charisma > 3:
                mc.name "What? Cum? A bird tagged her as we were walking back to the apartment."
                stephanie "But... why do you taste like this? This isn't how you normally taste..."
                mc.name "I was worried that I might get tempted, so before I left my house I masturbated to help me keep a clear head."
                $ stephanie.change_happiness(-2)
                $ stephanie.draw_person(position = "cowgirl")
                "[stephanie.possessive_title] seems just on the verge of calling your excuse bullshit... but then calms down."
                stephanie "You promise me, [stephanie.mc_title]?"
                mc.name "I promise."
                "Whew! She bought it. She leans forward and starts to suck on your cock again."
                "Her tongue swirls all around you, licking up your pre-cum and soon you are hard as a rock."
            "Make up an excuse (Lie)\n{color=#ff0000}{size=18}Not enough Charisma{/size}{/color} (disabled)" if mc.charisma <= 3:
                pass
            "Confess":
                $ caught_ashley_cheating = True
                "Unfortunately, you can't think of a way out of this."
                mc.name "Umm, yeah... it was..."
                $ stephanie.draw_person(position = "cowgirl", emotion = "angry")
    elif date_outcome == "protected sex" and not cum_clue:
        "Her tongue swirls all around you, licking up your pre-cum. It takes a little longer than usual to get it up, having fucked [the_person.title] earlier..."
    elif date_outcome == "protected sex" and cum_clue:
        "She pulls off for a bit, giving you a few strokes with her hand."
        stephanie "I need to be honest... it looked like Ash had something on her dress... you two didn't get naughty again did you?"
        menu:
            "Of course not (Lie)":
                mc.name "I would never do that to you."
                stephanie "Hmm... okay... I think I believe you..."
                "She starts to suck on your cock again. Her tongue swirls all around you, licking up your pre-cum and soon you are hard as a rock."
    elif date_outcome == "raw sex":
        "She pulls off you suddenly."
        $ stephanie.draw_person(position = "cowgirl", emotion = "angry")
        stephanie "What the fuck? You taste like pussy!"
        if stephanie.sex_record.get("Last Sex Day", 0) == day:
            mc.name "Chill out, we had sex earlier today, remember?"
            stephanie "That's... right..."
            stephanie "Wow! I am so sorry, I must seem completely paranoid..."
            "Whew... you also fucked her sister, but at least she seems to have bought it for now..."
            "She starts to suck on your cock again. Her tongue swirls all around you, licking up your pre-cum and soon you are hard as a rock."
        elif cum_clue:
            stephanie "I knew that was cum all over her dress in the hall! Just admit it! You fucked her!"
            "It seems there is no way of talking your way out of this one. You are totally busted."
            $ caught_ashley_cheating = True
        else:
            stephanie "I knew she couldn't keep her hands off you. You fucked her, didn't you?"
            "It seems there is no way of talking your way out of this one. You are totally busted."
            $ caught_ashley_cheating = True


    if caught_ashley_cheating:
        stephanie "I can't believe it... you promised!!!"
        $ the_person.change_love(-50)
        mc.name "I..."
        stephanie "You should go."
        "There is probably no way for you to patch things up right now... You decide to do as she asks."
        "You gather your stuff and leave."
        $ mc.business.add_mandatory_crisis(ashley_steph_second_date_confrontation)
        $ ashley.event_triggers_dict["caught_cheating"] = True
        #TODO make a mandatory event to trigger in a day or two where you and stephanie make up.
    else:
        stephanie "Mmm, you taste good... but that's not the only thing I want from you tonight..."
        "[stephanie.title] slowly moves up your body until her hips are on yours. She grinds her cunt a few times along your length, enjoying the pressure against her groin."
        $ stephanie.change_arousal(10)
        $ mc.change_locked_clarity(30)
        if stephanie.has_cum_fetish() or stephanie.has_breeding_fetish() or stephanie.wants_creampie():
            "She reaches down and takes your cock in her hand and lines it up with her raw cunt."
            stephanie "I want to feel you cum inside me tonight. I'm going give you the ride of your life and then finish you off deep..."
            "[stephanie.possessive_title] lowers her hips, sheathing your erection. She sighs in satisfaction when she bottoms out."
            call get_fucked(stephanie, the_goal = "vaginal creampie", start_position = cowgirl, private = True, skip_intro = True, allow_continue = False) from _ashley_second_date_creampie_steph_01
        elif stephanie.is_willing(cowgirl):
            "She reaches over to her nightstand and pulls out a pack of condoms. She grabs one and quickly rolls it onto you with her hand."
            stephanie "I know you don't like this, but I don't trust myself to pull off in time..."
            if date_outcome == "protected sex":
                "Fine with you. This isn't the first time tonight you've had a condom on."
            $ mc.condom = True
            "She reaches down and takes your cock in her hand and lines it up with her cunt."
            "[stephanie.possessive_title] lowers her hips, sheathing your erection. She sighs in satisfaction when she bottoms out."
            call get_fucked(stephanie, the_goal = "get mc off", start_position = cowgirl, private = True, skip_intro = True, allow_continue = False) from _ashley_second_date_fuck_steph_01
        else:
            call get_fucked(stephanie, the_goal = "get mc off", start_position = drysex_cowgirl, private = True, skip_intro = True, allow_continue = False) from _ashley_second_date_drysex_steph_01
        $ stephanie.draw_person(position = "back_peek")
        "[stephanie.possessive_title] turns her back to you. You cuddle up with her, wrapping your arm around her."
        mc.name "Goodnight..."
        stephanie "Night..."

        $ stephanie.next_day_outfit = stephanie.outfit # stay in current outfit next day
        call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_ashley_date_2_01

        $ picked_event = get_random_girlfriend_morning_action(stephanie)
        if picked_event:
            call expression picked_event.effect pass (*picked_event.args) from _call_picked_event_stephanie_after_ashley_concert
            $ del picked_event
        else:
            "You wake up, but [stephanie.possessive_title] isn't there. She must have gotten up early and left."
            $ stephanie.planned_outfit = stephanie.decide_on_outfit() # choose a new outfit for the day
            $ stephanie.apply_planned_outfit()

    python:
        mc.business.event_triggers_dict["girlfriend_person"] = None
        mc.business.event_triggers_dict["girlfriend_sleepover_scheduled"] = False  #Reset these so we can have another girlfriend sleepover.
        mc.business.add_mandatory_crisis(ashley_sneaks_over)
        del cum_clue
        del caught_ashley_cheating
        del date_outcome
    return

label ashley_steph_second_date_confrontation_label():
    $ the_person = stephanie
    "Your phone is ringing. It's [the_person.possessive_title]..."
    mc.name "Hello?"
    the_person "Hey. I'm going to keep this brief."
    the_person "I'm okay with work. I'm okay with working for you. I'm okay with even having a booty call now and then."
    the_person "But as a romantic partner, I'm not okay with you sleeping around, ESPECIALLY with my sister!"
    the_person "I'm sorry, but I'm breaking up with you."
    mc.name "Okay, I understand."
    the_person "I'll see you on Monday."
    $ the_person.remove_role(girlfriend_role)
    "[the_person.title] hangs up. Well, that could have gone better. Maybe you can still patch things up somehow?"
    return

label ashley_sneaks_over_label():   #Requires 60 love and 60 sluttiness events complete.
    python:
        mc.change_location(bedroom)
        the_person = ashley
        the_person.event_triggers_dict["sneaks_over_complete"] = True
        ashley.set_event_day("story_event")

    "After a long day, you sit down at your computer to work on a couple things before bedtime."
    "After getting through some emails, your phone vibrates."
    $ mc.start_text_convo(the_person)
    the_person "Hey, are you busy?"
    mc.name "Not really. Whats up?"
    the_person "Good. I'm outside, can I come in?"
    $ mc.end_text_convo()
    "She's what? How does she even know where you live?"
    $ hall.show_background()
    $ the_person.draw_person()
    "You get up and walk to the front door. When you open it, sure enough, there stands [the_person.possessive_title]."
    mc.name "[the_person.title]... what?"
    the_person "I know I don't usually do stuff like this, but I wanted to see you... can I come in?"
    mc.name "Umm, of course..."
    $ mc.location.show_background()
    "You quickly take [the_person.possessive_title] back to your room and close the door."
    if ashley_caught_cheating_on_sister():
        the_person "I just wanted to... apologize."
        the_person "Steph and I have always had a bit of sibling rivalry, but she's never been into anyone the way she was into you."
        the_person "I know it was both of us messing around, but I started a lot of it, so..."
        the_person "I'm sorry."
        $ the_person.change_obedience(20)
        mc.name "It's okay. I'm not sure what is going to happen with [stephanie.fname], but I'm hopeful I can patch things up somehow."
        "[the_person.possessive_title] nods in understanding."
        the_person "So you really like her too..."
        mc.name "Yes."
        the_person "I understand that, I really do. But tonight... I'm here. Maybe for one night, we could just like, pretend?"
        the_person "I know I'm just a booty call to you, but can I spend the night tonight? And would you treat me the way you treated her?"
    else:
        the_person "So, ever since our date the other night, I can't stop thinking about how hot it was."
        the_person "I'm so tired of the subterfuge... I swiped [stephanie.fname]'s phone and saw you didn't have any plans with her tonight..."
        mc.name "[the_person.title]..."
        the_person "I get it, that you and Steph are like, banging each other's brains out every chance you get."
        the_person "I understand that, I really do. But tonight... I'm here. Maybe for one night, we could just like, pretend?"
        the_person "I know I'm just a booty call to you, but can I spend the night tonight? And can you treat me the way you treat her?"
    "Obviously [the_person.possessive_title] has been having jealousy issues for a while, but you assumed they were mostly physical needs."
    "Now, she's exposing her real feelings, and it seems she's caught feelings for you that run deeper than just sex."
    $ mc.energy = mc.max_energy
    $ mc.change_locked_clarity(20)
    "Seeing her expose herself in this way gives you a burst of energy. She wants the girlfriend treatment? You can give it to her."
    mc.name "Of course you can stay the night. Don't get mad at me though if [stephanie.fname] gets suspicious when you have trouble walking tomorrow."
    $ the_person.change_stats(happiness = 10, love = 3)
    the_person "Me? You'll be lucky if you can get out of bed at all tomorrow!"
    $ the_person.draw_person(position = "against_wall")
    "[the_person.title] jumps on to you."
    "You stumble backwards, falling on to your bed. [the_person.possessive_title] lands on top of you."
    $ the_person.draw_person(position = "cowgirl")
    "[the_person.title] is so eager, she starts pulling her clothes out of the way."
    $ the_person.strip_to_vagina(prefer_half_off = True, visible_enough = True, position = "cowgirl")
    the_person "What are you waiting for? Get your cock out, geesh!"
    "[the_person.possessive_title] licks her lips as you quickly pull your pants and underwear down. She grabs your erection and gives it a couple strokes."
    the_person "Oh god, this thing is mine ALL NIGHT. It's about fucking time..."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(30)
    $ ashley_sex_goal = None
    if stephanie.has_broken_taboo("condomless_sex") and the_person.has_taboo("condomless_sex"):
        the_person "Steph told me you guys go at it raw sometimes. I'm not usually into that, but hearing her talk about it makes it sounds amazing."
        the_person "I think it's about time we went for it too."
        "[the_person.title] points your cock toward her slit, then starts to rub against it. Her arousal glistens at the tip as she moves her hips back and forth."
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(30)
        mc.name "Wouldn't it be a bit risky? What if you got knocked up?"
        if the_person.wants_creampie():
            the_person "What of it? Isn't that part of the thrill? The risk of pregnancy?"
            the_person "Wouldn't it be hot to knock up your girlfriend's sister?"
            $ mc.change_arousal(15)
            mc.name "I'm not sure how she would like it..."
            the_person "She doesn't have to know. I could just tell her I had a one night stand and got a little crazy. She'd totally believe it..."
            $ ashley_sex_goal = "vaginal creampie"
            mc.name "Then do it."
        else:
            the_person "That is part of the challenge. Get as close as you can to going over the edge, then pull off at the last second."
            mc.name "Still sounds risky, but if you think you can do it, go ahead and try."
            $ ashley_sex_goal = "body shot"
        "[the_person.possessive_title] stops rolling her hips. With one smooth movement she slides you raw deep into her tight cunt."
        $ the_person.break_taboo("condomless_sex")
    elif the_person.has_taboo("condomless_sex") and the_person.effective_sluttiness() >= the_person.get_no_condom_threshold():  #She would normally be willing to go bare
        the_person "I was talking to Steph about you the other day, and something she told me surprised me."
        mc.name "Oh?"
        the_person "She said every time you guys have, you know, she always makes you wrap it up."
        "[the_person.title] points your bare cock toward her slit, then starts to rub against it. Her arousal glistens at the tip as she moves her hips back and forth."
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(30)
        the_person "Wanna feel the real thing? Something my sister never gives you?"
        mc.name "Wouldn't it be a bit risky? What if you got knocked up?"
        if the_person.wants_creampie():
            the_person "What of it? Isn't that part of the thrill? The risk of pregnancy?"
            the_person "Wouldn't it be hot to knock up your girlfriend's sister?"
            $ mc.change_arousal(15)
            mc.name "I'm not sure how she would like it..."
            the_person "She doesn't have to know. I could just tell her I had a one night stand and got a little crazy. She'd totally believe it..."
            $ ashley_sex_goal = "vaginal creampie"
            mc.name "Then do it."
        else:
            the_person "That is part of the challenge. Get as close as you can to going over the edge, then pull off at the last second."
            mc.name "Still sounds risky, but if you think you can do it, go ahead and try."
            $ ashley_sex_goal = "body shot"
        "[the_person.possessive_title] stops rolling her hips. With one smooth movement she slides you deep into her tight cunt."
        $ the_person.break_taboo("condomless_sex")

    elif the_person.effective_sluttiness() >= the_person.get_no_condom_threshold():
        the_person "Mmm, it feels so hot. I just wanna slip it in..."
        "[the_person.title] points your cock toward her slit, then starts to rub against it. Her arousal glistens at the tip as she moves her hips back and forth."
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(30)
        the_person "What would you do if I just sat on it right now? Not even a condom between us?"
        mc.name "Sounds hot. Do it."
        if the_person.wants_creampie():
            the_person "What if I can't stop and pull off in time? What if I just ride you until you shoot your load right up inside me?"
            mc.name "Are you on birth control?"
            the_person "Does it matter? Birth control isn't perfect. You could knock me up either way. Do you want to knock up your girlfriend's sister?"
            $ mc.change_arousal(15)
            mc.name "I'm not sure how she would like it..."
            the_person "She doesn't have to know. I could just tell her I had a one night stand and got a little crazy. She'd totally believe it..."
            $ ashley_sex_goal = "vaginal creampie"
            mc.name "Then do it."
        else:
            the_person "Mmm, god I hope I can pull off in time..."
            $ ashley_sex_goal = "body shot"
        "[the_person.possessive_title] stops rolling her hips. With one smooth movement she slides your raw cock deep into her tight cunt."
    else:
        the_person "Where do you keep your condoms at? I hope you have enough, you're going to need them!"
        "You point to the nightstand. She quickly grabs the box and throws them on the bed after grabbing one."
        $ ashley_sex_goal = "get mc off"
        "[the_person.possessive_title] rolls it onto you, then points you at her entrance."
        $ mc.condom = True
        "[the_person.title] points your cock toward her slit, then starts to rub against it. Her arousal glistens at the tip of the condom as she moves her hips back and forth."
        the_person "Here we go. Round one!"
        "[the_person.possessive_title] stops rolling her hips. With one smooth movement she slides you deep into her tight cunt."
    call get_fucked(the_person, start_position = cowgirl, the_goal = ashley_sex_goal, private = True, skip_intro = True, allow_continue = False) from _ashley_comes_over_cowgirl_01
    $ the_person.draw_person(position = "missionary")

    $ the_report = _return

    $ done = False
    $ girl_came = the_report.get("girl orgasms", 0)
    $ energy_gain_amount = 50 #Drops each round, representing your flagging endurance.
    if perk_system.has_ability_perk("Lustful Youth"):
        $ energy_gain_amount += 70
    while done == False:

        if mc.energy < 40 and energy_gain_amount <= 20: #Forced to end the fuck date, so we set done to True.
            "The spirit is willing, but the flesh is spent. Try as she might [the_person.title] can't coax your erection back to life."
            if girl_came > 0:
                the_person "Mmm, I wore you out! That was fun."
                "She kisses you and runs her hand over your back."
            else:
                $ the_person.change_stats(slut = -1, love = -3)
                the_person "Well I guess we're done then... Maybe next time you can get me off as well."
            $ done = True

        else:
            "After a short rest you've recovered some of your energy and [the_person.possessive_title]'s eager to get back to work."
            $ mc.change_energy(energy_gain_amount)
            $ the_person.change_energy(energy_gain_amount) #She gains some back too
            if energy_gain_amount >= 10:
                $ energy_gain_amount += -10 #Gain less and less energy back each time until eventually you're exhausted and gain nothing back.
            menu:
                "Fuck her again":
                    "With your cock hard again, you pull [the_person.title] towards you."
                    $ mc.change_locked_clarity(30)
                    call fuck_person(the_person, private = True) from _call_fuck_ashley_sleepover_gf_04
                    $ the_report = _return
                    $ girl_came += the_report.get("girl orgasms", 0)
                    if the_person.energy + energy_gain_amount < 30:
                        "[the_person.title] is panting. She is completely out of breath."
                        the_person "That's enough... oh my god, I can't move a muscle..."
                        the_person "I'm sorry honey, you wore me out! I need to be done for the night..."
                        $ done = True
                "Call it a night":
                    mc.name "Sorry, I need to get some sleep. I need to be done for tonight."
                    if girl_came:
                        the_person "Mmm, okay! That was nice."
                        "She kisses you and runs her hand over your back."
                    else:
                        $ the_person.change_stats(slut = -1, love = -3)
                        the_person "Well... Maybe next time you can get me off as well?"
                    $ done = True
    $ the_person.draw_person(position = "back_peek")
    "[the_person.possessive_title] turns her back to you. You cuddle up with her, wrapping your arm around her."
    mc.name "Goodnight..."
    the_person "Night..."
    $ del ashley_sex_goal

    $ the_person.next_day_outfit = the_person.outfit # stay in current outfit next day
    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_ashley_sleepover_01

    $ the_person.draw_person(position = "walking_away")
    "You slowly wake up, with your arms around [the_person.possessive_title], spooning with her."
    $ mc.change_locked_clarity(50)
    "She stirs at the same time as you. She gives a big yawn."
    the_person "... [the_person.mc_title]?"
    mc.name "Good morning."
    $ the_person.change_love(5)
    the_person "Mmm... so this is what it's like? To wake up next to someone you fucked all night sober?"
    "Her ass wiggles a bit back against you."
    the_person "It's nice... I could get used to this..."
    $ the_person.change_happiness(5)
    "[the_person.title]'s ass wiggling against you soon has you getting hard. She wiggles more when she feels it."
    the_person "One more for the road? No telling if we'll have this chance again..."
    mc.name "Sounds good to me..."
    $ mc.change_locked_clarity(50)
    "You reach down and run your fingers between her legs. She is already getting wet."
    "You wipe her juices on your dick, then do you best to point it between her closed legs. You push between her closed thighs, searching for her cunt."
    if the_person.has_taboo("condomless_sex") and the_person.wants_creampie():
        the_person "Mmmm... oh my god. I'm way too tired, fuck getting a condom."
        "She reaches down and parts her legs slightly. She guides your cock towards her slick entrance."
        "You push yourself partway inside of her, but due to the angle it is hard to get deep penetration. However, [the_person.title] seems to enjoy the angle."
        $ the_person.change_arousal(20)
        the_person "Ahhh, that feels amazing."
        "She sighs."
        the_person "Look... Do what you want when you finish... okay? Just make sure you know what could happen if you cum inside me."
        mc.name "Mmmm, okay."
    elif the_person.has_taboo("condomless_sex"):
        the_person "Mmm, god. I'm way too tired... you can pullout... right?"
        "She reaches down and parts her legs slightly. She guides your cock towards her slick entrance."
        "You push yourself partway inside of her, but due to the angle it is hard to get deep penetration. However, [the_person.title] seems to enjoy the angle."
        $ the_person.change_arousal(20)
        the_person "Ahhh, that feels amazing."
    else:
        "She reaches down and parts her legs slightly. She guides your cock towards her slick entrance."
        "You push yourself partway inside of her, but due to the angle it is hard to get deep penetration. However, [the_person.title] seems to enjoy the angle."
        $ the_person.change_arousal(20)
        the_person "Ahhh, that feels amazing."
    "You give her a few tentative strokes, and soon you are established in a nice, easy rhythm."
    call fuck_person(the_person, private=True, start_position = spooning_sex, start_object = make_bed(), skip_intro = True, skip_condom = True) from _call_ashley_sleepover_wakeup_sex_01
    $ the_person.reset_arousal()
    $ mc.arousal = 0
    "You lay in bed together for a little longer, but soon it is time to start the day."
    $ the_person.planned_outfit = the_person.decide_on_outfit() # choose a new outfit for the day
    $ the_person.apply_planned_outfit()
    $ the_person.draw_person(position = "stand4")
    "You both get ready for the day."
    the_person "Alright, well, hopefully this doesn't make things at work awkward. I'm going to head out. Why don't you wait for a bit before you go anywhere?"
    mc.name "Okay, have a good day [the_person.title]."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] turns and walks out your door. You can't help but notice a slight change to her gait."
    $ clear_scene()

    "Things between [stephanie.title] and her sister are starting to get out of hand. You need to put a stop to their jealousy."
    "You start to concoct a plan. What if you got them together, the three of you for some drinks, and you dosed them with some serums?"
    "Maybe you could finally break through and get them to mess around with you, together, so you can stop keeping all this stuff secret."
    "You should develop some serums that can increase love, and then talk to [the_person.title]."
    $ the_person.add_unique_on_talk_event(ashley_steph_drinks_out)
    return  #60

label ashley_steph_drinks_out_label():  #80 Love and sneaks over event complete.
    "This scene not yet written."
    "In this scene, you convince the two sisters to share you."
    $ ashley.event_triggers_dict["is_jealous"] = False
    $ stephanie.event_triggers_dict["is_jealous"] = False
    return

label ashley_obedience_struggle():  #Use this label to describe an internal struggle MC has with obeying ashley.
    $ the_person = ashley
    "[the_person.title] looks at you, waiting for you to comply."
    #First, determine if outright willpower failure is possible. Must have performed sub sex scene with ashley and given in.
    if ashley_dom_fuck_avail() and persistent.mc_noncon_pref == 2:
        if ashley_mc_submission_score() > 200 and ashley.obedience < 180:
            "You look back at her. You just don't have the will to resist her demands."
            return False
    if persistent.mc_noncon_pref == 2:
        if ashley_mc_submission_score() > 100:
            "You look back at her. You just don't have the will to resist her demands."
            return False
        if ashley_mc_submission_score() > 0:
            "You look back at her. You could summon your energy and resist her demands, but it won't be easy."
            menu:
                "Refuse" if mc.energy >= 20:
                    return True
                "Refuse\n{color=#ff0000}{size=18}Not enough Energy{/size}{/color} (disabled)" if mc_energy < 20:
                    pass
                "Give in":
                    "You just don't have the energy to resist her demands."
                    return False
        else:
            "You look back at her. You could let her have her fun, as crazy at it might get, or you could take things in a different direction."
            menu:
                "Refuse":
                    return True
                "Give in":
                    "You decide to play along and see how things go, for now."
                    return False
    if persistent.mc_noncon_pref == 1:
        "You look back at her. You could let her have her fun, as crazy at it might get, or you could take things in a different direction."
        menu:
            "Refuse":
                return True
            "Give in":
                "You decide to play along and see how things go, for now."
                return False
    if persistent.mc_noncon_pref == 0:
        "You look back at her. Yeah right! Like you would let her take control like that."
        return False

    return True

# label ashley_room_excitement_overhear_label(the_person):
#     $ the_person = ashley # on_room_enter_event so the_person isn't defined
#     $ the_person.draw_person(position = "standing_doggy")
#     "As you step into the room, you can overhear [the_person.title] talking excitedly to another coworker."
#     the_person "I know! I can't wait to go. All of my friends say it's so much fun..."
#     "But as you enter the room, she notices, and immediately stops talking."
#     $ the_person.draw_person()
#     the_person "..."
#     "Clearly she has no issue talking to her coworkers... why is she so quiet with you? Maybe you should ask her sister about it."
#     $ stephanie.add_unique_on_talk_event(ashley_ask_sister_about_attitude)
#     $ ashley.event_triggers_dict["excitement_overhear"] = True
#     return
#
# label ashley_ask_sister_about_attitude_label(the_person):
#     "You approach [the_person.title], intending to ask her about her sister."
#     mc.name "Hello [the_person.title]. Do you have a moment?"
#     the_person "Of course sir. What can I do for you?"
#     "You lower your voice. You don't necessarily need anyone overhearing you."
#     mc.name "Well... I'm not sure how to say this but, I'm a little concerned about [ashley.fname]."
#     "A grimace forms on her face, but she waits for you to continue."
#     mc.name "Earlier, I was walking by and I could hear her carrying on with her coworkers. But as soon as I entered the room, she went completely silent."
#     "[the_person.title] nods her head as you keep going."
#     mc.name "She barely says a word anytime I talk to her. I feel like I've gotten off to a bad start with her. Do you have any advice?"
#     "[the_person.title] clears her throat."
#     the_person "Well... [ashley.fname] is a bit complicated. She has trouble talking to, and being around men in general..."
#     mc.name "Oh? Oh! I see, I mean I guess that makes sense, not everyone is heterosexual..."
#     the_person "Noooo, no. It isn't that. She's had boyfriends in the past. But something happened between her and her last boyfriend in college."
#     the_person "They broke up all of a sudden, and she's never been the same way around men since then."
#     mc.name "Hmm, that sounds like something bad might have happened."
#     the_person "Yeah... honestly, I can't really talk about it."
#     "[the_person.title] shakes her head, lost in thought."
#     mc.name "Thank you for the insight. I appreciate it."
#     the_person "Of course."
#     $ ashley.add_unique_on_room_enter_event(ashley_room_warming_up)
#     $ ashley.event_triggers_dict["attitude_discussed"] = True
#     return
#
# label ashley_room_warming_up_label(the_person):
#     $ the_person = ashley # on_room_enter_event so the_person isn't defined
#     $ the_person.draw_person(position = "standing_doggy")
#     "As you step into the room, you can overhear [the_person.title] talking excitedly to another coworker."
#     the_person "I know, I just need to find someone to go with!"
#     "As you enter the room, she looks up and stops talking."
#     $ the_person.draw_person()
#     the_person "Ahh... hello sir. Having a good day?"
#     "Whoa. She actually said hi to you? Maybe she is warming up to you a little bit?"
#     mc.name "It's been great so far. And you?"
#     the_person "Oh... it's been good I guess..."
#     mc.name "Glad to hear it."
#
#     $ ashley.add_unique_on_room_enter_event(ashley_room_overhear_classical)
#     return
#
#
# label ashley_mandatory_ask_about_porn_label():
#     "You've had some time to think about [ashley.possessive_title], since you went on your date and discovered she was in a porn video unwittingly."
#     "She seems to have warmed up to you enough; you decide that maybe it is the right time to talk to her about it."
#     $ ashley.event_triggers_dict["porn_convo_avail"] = True
#     return
#
# label ashley_clothes_shopping_label(the_person):
#     $ ashley.set_override_schedule(None, the_days = [6], the_times = [2])
#     "You decide to swing by the clothing store, where [the_person.title] said she would be at. After a few awkward minutes poking around the women's clothing, you spot her."
#     $ the_person.draw_person()
#     "She seems preoccupied and doesn't notice you until you walk up."
#     mc.name "Hey [the_person.title]. I thought I might find you here."
#     the_person "Ah... Hello..."
#     if ashley_is_fwb_path():
#         mc.name "I remembered at the coffee shop this morning you said you were gonna come here. I was in the area and thought I could swing by. I thought you might appreciate a male perspective on your outfits?"
#         the_person "Oh, I suppose that would be okay..."
#         "Without the security of her sister nearby, [the_person.possessive_title]'s shy demeanor is really showing."
#     elif ashley_is_secret_path():
#         mc.name "You said you were gonna try on a couple things. I thought maybe you would appreciate the opinion of a secret admirer..."
#         the_person "Ah, that sounds good..."
#     elif ashley_is_normal_path():
#         mc.name "When you said you were gonna swing by here later, I knew I wanted to come out and see some of these outfits for myself."
#         "She smiles and replies shyly."
#         the_person "Ah, that's good. Let's see what we can find."
#
#     "[the_person.title] looks around at a few different clothing racks and puts an outfit together. It looks very similar to the outfit you saw earlier today. You follow her over to the changing rooms."
#     if ashley.is_girlfriend():
#         the_person "Here... Come on in with me. You're my boyfriend I'm sure no one will mind."
#         "You quickly slip into the dressing room with [the_person.title]."
#     elif the_person.sluttiness > 30:
#         "She looks around and sees that there isn't anyone around."
#         the_person "Here... Come in with me, before anyone notices..."
#         "You quietly slip into the dressing room with [the_person.title]."
#     "You sit down at the bench and watch as [the_person.possessive_title] starts to strip down."
#     $ the_person.strip_outfit(exclude_upper = False)
#     $ mc.change_locked_clarity(30)
#     if the_person.sluttiness > 50:
#         "Although she doesn't say a word, [the_person.title] doesn't make any move to cover herself either. Her body is on display as she reaches for her outfit..."
#     else:
#         "[the_person.title] absentmindedly covers her mound with one hand as she reaches for her outfit."
#     $ the_person.apply_outfit(the_person.personalize_outfit(ashley_get_observed_outfit(), coloured_underwear = True))
#     $ the_person.draw_person()
#     "When she finishes putting on her new outfit, she steps back so you can get a good look."
#     the_person "Okay... What do you think?"
#     $ the_person.draw_person(position = "back_peek")
#     "She gives a quick twirl, letting you check her out from all angles. You make sure to take in all of the details."
#     $ the_person.draw_person()
#     menu:
#         "Keep it":
#             mc.name "I like it. You should get it."
#             the_person "I think so too. Thanks!"
#             $ the_person.wardrobe.add_outfit(the_person.outfit)
#         "Not for you":
#             mc.name "Sorry, it's an interesting outfit, but I don't think it's right for you."
#             the_person "Yeah... I was thinking the same thing..."
#     if the_person.is_girlfriend():
#         # the_person "So, I know that like... Clothes shopping can be pretty boring for guys... So I was wandering..."
#         # "Her voice trails off. You can tell she is trying to suggest something fun, but she's to shy to say it out loud."
#         # mc.name "You want to make this more interesting?"
#         # the_person "Err, kind of... I was thinking, maybe while I change, you could go pick something out for me? As a reward for helping me... I'll try on anything you want me to..."
#         # "That does sound like a fun proposition!"
#         # the_person "If it's too crazy though, maybe it's an outfit we could save for the bedroom..."
#         # mc.name "Sounds good! I'm sure I can find something..."
#         # "You step out of the dressing and browse the clothes racks, looking for a nice outfit for your girlfriend."
#         # [Outfit screen]
#         # [If not outfit]
#         # For some reason, you can't seem to put together a good look for Ashley. You head back to the dressing room and apologize through the door.
#         # "Hey, sorry Ashley, for some reason I couldn't come up with anything..."
#         # "Oh! That's okay... Sorry to put you on the spot like that..."
#         # [Have outfit]
#         # You put something together and take it back to the dressing room. Making sure no one is around, you quietly slip into the room.
#         # [Draw naked ashley]
#         # You hand her the outfit. When she finishes putting it on, she checks herself in the mirror.
#         # [Draw outfit backpeek]
#         # [If normal outfit]
#         # "Hmm... Interesting..."
#         # [Draw standing]
#         # "I could wear this... For you anyway..."
#         # Ashley gives you a shy smile.
#         # "I'll get it for you. Now go out and wait for me! I'll be right out..."
#         # [If slutty]
#         # "Oh... Oh my..."
#         # [Draw standing]
#         # "Would this excite you? If you came over and when I answered the door I was wearing this?.."
#         # "Definitely..."
#         # "Mmm... Okay... I'll get it... But I'm only gonna wear it for you!"
#         # "Now go out and wait for me..."
#         # [Clear ashley]
#         $ clear_scene()
#         $ the_person.apply_outfit(the_person.planned_outfit)
#         "She shoos you out of the changing room. In a few minutes, she emerges from the changing room."
#         $ the_person.draw_person()
#         the_person "Thanks for waiting..."
#         the_person "Say, do you wanna come over tonight? You could, you know, stay over..."
#         $ mc.change_locked_clarity(20)
#         menu:
#             "Come over later" if schedule_sleepover_available():
#                 mc.name "I wouldn't mind a sleepover."
#                 the_person "I'll see you tonight then..."
#                 $ schedule_sleepover_in_story(the_person)
#             "Come over later (disabled)" if not schedule_sleepover_available():
#                 pass
#             "Not tonight":
#                 mc.name "I can't tonight, maybe another night..."
#
#         "You say goodbye to [the_person.title] for now."
#     elif the_person.jealous_score() > 0:
#         "Before she starts to change back, [the_person.title] starts to tease you."
#         the_person "So... I can't help but notice that [stephanie.fname] has been getting a lot of attention lately..."
#         $ the_person.strip_outfit(exclude_lower = True)
#         $ desc_tuple = the_person.jealous_sister_get_revenge_tuple()
#         the_person "[desc_tuple[0]]"
#         $ the_person.strip_outfit()
#         the_person "I can't help but feel like it should be my turn to get off..."
#         "She walks over to you. Sitting on the bench, her cunt is now just inches away."
#         $ mc.change_locked_clarity(20)
#         $ the_position = cowgirl
#         if desc_tuple[1] == 1: #Foreplay
#             $ the_position = drysex_cowgirl
#         elif desc_tuple[1] == 2:
#             $ the_position = standing_cunnilingus
#         elif desc_tuple[1] >= 4:    #If 4 let the system make a position for her.
#             $ the_position = None
#         call get_fucked(the_person, the_goal = "get off", private= True, start_position = the_position, allow_continue = True) from _ashley_jealous_clothes_tryout_01
#         if _return.get("girl orgasms", 0):
#             the_person "Ahhh, that was nice. Good to know my sister isn't getting ALL your attention!"
#             $ the_person.reset_all_jealousy()
#             $ the_person.change_stats(slut = 1, love = 3)
#         else:
#             the_person "Wow, really? You can't give me the same treatment that [stephanie.fname] gave you? She got you all worn out?"
#             "She looks pissed."
#             $ the_person.change_stats(slut = -1, love = -3)
#             $ the_person.jealous_change_score(3) #Add points to jealous score so ashley gets more desperate.
#         $ the_person.draw_person(position = "stand2")
#         "You get yourself put back together."
#         mc.name "I'm going to slip out."
#         the_person "Okay, I'll see you around [the_person.mc_title]."
#         $ clear_scene()
#         "You quietly exit the changing room."
#     else:
#         the_person "Thanks for the opinion. I'm going to go ahead and change back..."
#         mc.name "I'm going to slip out."
#         the_person "Okay, I'll see you around [the_person.mc_title]."
#         $ clear_scene()
#         "You quietly exit the changing room."
#
#     # make sure she changes back into her normal outfit
#     $ the_person.apply_planned_outfit()
#     return
#
# label ashley_test_outfit_scene():
#     $ scene_manager = Scene()
#     $ the_person = ashley
#     $ preferences = WardrobePreference(the_person)
#     $ bystander = get_random_from_list(known_people_in_the_game(excluded_people = [ashley, stephanie]))
#
#     if not bystander:
#         return  # exit loop if we have no bystander
#
#     "Enjoying your coffee, you zone out for a minute while the two sisters are chatting, when suddenly the talking stops. You look up and see them both looking out the restaurant window."
#     "Outside is a woman who has stopped and is checking her phone for something. The girls are checking her out."
#
#     $ scene_manager.add_actor(bystander, display_transform = character_right_flipped, position = "stand3")
#     "She takes a moment to look at something on her phone."
#     "Then she walks away."
#     $ scene_manager.add_actor(bystander, display_transform = character_right_flipped, position = "walking_away")
#     "The girls watch as she walks away."
#     $ scene_manager.remove_actor(bystander)
#     the_person "Wow, did you see that?"
#
#     $ new_outfit = the_person.personalize_outfit(bystander.outfit, opinion_color = "the colour green", coloured_underwear = True)
#
#     $ ashley.apply_outfit(new_outfit)
#     $ stephanie.apply_outfit(new_outfit)
#     $ scene_manager.add_actor(ashley)
#     "[ashley.fname] models her new outfits for you."
#
#     python:
#         del bystander
#         del preferences
#     $ scene_manager.clear_scene()
#     return
#
#
# label ashley_unit_test():
#     python:
#         the_person = ashley
#         the_person.situational_sluttiness = {} #A dict that stores a "situation" string and the corresponding amount it is contributing to the girls sluttiness.
#         the_person.situational_obedience = {}
#         the_person.arousal = 0
#         the_person.energy = the_person.max_energy
#         the_person.sluttiness = 0
#         the_person.sluttiness = 0
#         the_person.obedience = 0
#         the_person.happiness = 100
#         the_person.love = 0
#     "Unit Test Ashley hiring scene."
#     call ashley_intro_label from _unit_test_ashley_01
#     if ashley.is_employee():
#         "You hired Ashley"
#     else:
#         "You did not hire Ashley."
#         call ashley_hire_directed_label from _unit_test_ashley_02
#         "You still have not hired Ashley. Aborting unit test."
#
#     "Unit test Ashley Intro."
#     call ashley_first_talk_label(the_person) from _unit_test_ashley_03
#
#     "A few days later"
#     call ashley_first_talk_label(the_person) from _unit_test_ashley_04
#
#
#     call ashley_room_excitement_overhear_label(the_person) from _unit_test_ashley_05
#     call ashley_ask_sister_about_attitude_label(stephanie)from _unit_test_ashley_06
#     call ashley_room_warming_up_label(the_person) from _unit_test_ashley_07
#     call ashley_room_overhear_classical_label(the_person) from _unit_test_ashley_08
#     call ashley_ask_date_classic_concert_label(the_person) from _unit_test_ashley_09
#     call ashley_ask_date_classic_concert_label(the_person) from _unit_test_ashley_10
#     call ashley_classical_concert_date_label() from _unit_test_ashley_11
#     call ashley_porn_video_discover_label() from _unit_test_ashley_12
#     call ashley_ask_sister_about_porn_video_label(stephanie) from _unit_test_ashley_13
#     python:
#         the_person.situational_sluttiness = {}
#         the_person.situational_obedience = {}
#         the_person.arousal = 0
#         the_person.energy = the_person.max_energy
#         the_person.sluttiness = 20
#         the_person.sluttiness = 20
#         the_person.obedience = 0
#         the_person.happiness = 100
#         the_person.love = 0
#
#     call ashley_mandatory_ask_about_porn_label() from _unit_test_ashley_14
#     call ashley_ask_about_porn_label(the_person) from _unit_test_ashley_15
#     return
#
# label ashley_unit_test2():
#     python:
#         the_person = ashley
#         the_person.situational_sluttiness = {}
#         the_person.situational_obedience = {}
#         the_person.arousal = 0
#         the_person.energy = the_person.max_energy
#         the_person.sluttiness = 40
#         the_person.sluttiness = 40
#         the_person.obedience = 0
#         the_person.happiness = 100
#         the_person.love = 0
#         stephanie.love = 100
#         stephanie.sluttiness = 40
#         stephanie.sluttiness = 40
#         stephanie.energy = stephanie.max_energy
#         mc.max_energy = 200
#         mc.energy = mc.max_energy
#     call ashley_post_handjob_convo_label(the_person) from _unit_test_ashley_16
#     call ashley_stephanie_arrange_relationship_label(stephanie) from _unit_test_ashley_17
#     call ashley_stephanie_saturday_coffee_intro_label(the_person) from _unit_test_ashley_18
#     python:
#         the_person.situational_sluttiness = {}
#         the_person.situational_obedience = {}
#         the_person.arousal = 0
#         the_person.energy = the_person.max_energy
#         the_person.sluttiness = 40
#         the_person.sluttiness = 40
#         the_person.obedience = 0
#         the_person.happiness = 100
#         the_person.love = 0
#         stephanie.love = 100
#         stephanie.sluttiness = 40
#         stephanie.sluttiness = 40
#         stephanie.energy = stephanie.max_energy
#     "Coffee recurring. She should be ready for second date to proc from this."
#     call ashley_stephanie_saturday_coffee_recur_label(the_person) from _unit_test_ashley_19
#     #ashley_second_concert_intro_label(the_person)
#     call ashley_second_concert_date_label() from _unit_test_ashley_20
#     "Test staphanie's breakup dialogue"
#     call ashley_steph_second_date_confrontation_label from unit_test_ashley_21
#     python:
#         the_person.situational_sluttiness = {}
#         the_person.situational_obedience = {}
#         the_person.arousal = 0
#         the_person.energy = the_person.max_energy
#         the_person.sluttiness = 60
#         the_person.sluttiness = 60
#         the_person.obedience = 0
#         the_person.happiness = 100
#         the_person.love = 40
#         stephanie.love = 100
#         stephanie.sluttiness = 40
#         stephanie.sluttiness = 40
#         stephanie.energy = stephanie.max_energy
#         mc.max_energy = 200
#         mc.energy = mc.max_energy
#     "Blowjob test"
#     call ashley_blows_during_meeting_label from unit_test_ashley_22
#
#
#     return
#
# init 2 python: #Coffee time requirements function. #TODO should I pull out coffee times stuff to its own file? this file might get too big.
#     def coffee_time_innocent_chat_requirement():
#         return True
#
#     def coffee_time_woman_walks_by_requirement():
#         return True
#
#     def coffee_time_sexy_chat_requirement():
#         if stephanie.sluttiness > 40 and ashley.sluttiness > 40:
#             return True
#         return False
#
#     def coffee_time_steph_gets_handsy_requirement():
#         if stephanie.sluttiness > 40:
#             if ashley_get_coffee_partner() == stephanie:
#                 return True
#         return False
#
# init 3 python:
#     ashley_coffee_time_action_list = []
#     steph_coffee_time_action_list = []
#
#     coffee_time_innocent_chat = Action("Sister Talk", coffee_time_innocent_chat_requirement, "coffee_time_innocent_chat_label")
#     coffee_time_sexy_chat = Action("Sister Sexy Talk", coffee_time_sexy_chat_requirement, "coffee_time_sexy_chat_label")
#     coffee_time_steph_gets_handsy = Action("Stephanie gets handsy", coffee_time_steph_gets_handsy_requirement, "coffee_time_steph_gets_handsy_label")
#     coffee_time_woman_walks_by_label = Action("Woman walks by", coffee_time_woman_walks_by_requirement, "coffee_time_woman_walks_by_label")
#
#     ashley_coffee_time_action_list.append(coffee_time_innocent_chat)
#     ashley_coffee_time_action_list.append(coffee_time_sexy_chat)
#     ashley_coffee_time_action_list.append(coffee_time_woman_walks_by_label)
#     steph_coffee_time_action_list.append(coffee_time_innocent_chat)
#     steph_coffee_time_action_list.append(coffee_time_sexy_chat)
#     steph_coffee_time_action_list.append(coffee_time_steph_gets_handsy)
#
#     def ashley_coffee_time_get_random_action():
#         possible_action_list = []
#         for ashley_scene in ashley_coffee_time_action_list:
#             if ashley_scene.is_action_enabled(): #Get the first element of the weighted tuple, the action.
#                 possible_action_list.append(ashley_scene) #Build a list of valid crises from ones that pass their requirement.
#         return get_random_from_list(possible_action_list)
#
#     def steph_coffee_time_get_random_action():
#         possible_action_list = []
#         for steph_scene in steph_coffee_time_action_list:
#             if steph_scene.is_action_enabled(): #Get the first element of the weighted tuple, the action.
#                 possible_action_list.append(steph_scene) #Build a list of valid crises from ones that pass their requirement.
#         return get_random_from_list(possible_action_list)
#

#End coffee time code

#Python wrappers for Ashley's story progression.
init 3 python:
    def ashley_get_intro_complete():
        return ashley.event_triggers_dict.get("intro_complete", False)

    def ashley_get_if_excitement_overheard():
        return ashley.event_triggers_dict.get("excitement_overhear", False)

    def ashley_get_attitude_discussed():
        return ashley.event_triggers_dict.get("attitude_discussed", False)

    def ashley_get_porn_discovered():
        return ashley.event_triggers_dict.get("porn_discovered", False)

    def ashley_get_porn_discussed():
        return ashley.event_triggers_dict.get("porn_discussed", False)

    def ashley_get_concert_overheard():
        return ashley.event_triggers_dict.get("concert_overheard", False)

    def ashley_get_concert_date_stage():
        return ashley.event_triggers_dict.get("concert_date", 0)

    def ashley_get_porn_convo_day():
        return ashley.event_triggers_dict.get("porn_convo_day", 9999)

    def ashley_get_porn_convo_avail():
        return ashley.event_triggers_dict.get("porn_convo_avail", False)

    def ashley_get_story_path():
        return ashley.event_triggers_dict.get("story_path", None)

    def ashley_is_secret_path():
        if ashley.event_triggers_dict.get("story_path", None) == "secret":
            return True
        return False

    def ashley_is_fwb_path():
        if ashley.event_triggers_dict.get("story_path", None) == "fwb":
            return True
        return False

    def ashley_is_normal_path():
        if ashley.event_triggers_dict.get("story_path", None) == "normal":
            return True
        return False

    def ashley_get_coffee_partner():
        identifier = ashley.event_triggers_dict.get("coffee_partner", None)
        if isinstance(identifier, Person):
            return identifier
        else:
            return get_person_by_identifier(identifier)
        return None

    def ashley_set_coffee_partner(person):
        ashley.event_triggers_dict["coffee_partner"] = person.identifier
        return

    def ashley_reset_coffee_partner():
        ashley.event_triggers_dict["coffee_partner"] = None
        return

    def ashley_set_observed_outfit(the_outfit):
        ashley.event_triggers_dict["observed_outfit"] = the_outfit.get_copy()
        return

    def ashley_get_observed_outfit():
        return ashley.event_triggers_dict.get("observed_outfit", None)

    def ashley_second_date_complete():
        return ashley.event_triggers_dict.get("second_date_complete", None)

    def ashley_sneaks_over_complete():
        return ashley.event_triggers_dict.get("sneaks_over_complete", False)

    def ashley_caught_cheating_on_sister():
        return ashley.event_triggers_dict.get("caught_cheating", False)

    def ashley_non_con_enabled():
        return ashley.event_triggers_dict.get("non_con", False)

    def ashley_on_default_path():
        if stephanie.is_girlfriend() and not ashley.is_girlfriend() and stephanie == mc.business.head_researcher:
            return True
        return False

    def ashley_mc_submission_story_complete():
        return mc.business.event_triggers_dict.get("ashley_submission_complete", False)

    def ashley_mc_submission_score():
        sub_score = ashley.event_triggers_dict.get("mc_obedience", 0) - (ashley.obedience - 80)
        return sub_score

    def ashley_lily_are_friends():
        return ashley.event_triggers_dict.get("lily_friend", False)

    #Sub and Dom scenes completed
    def ashley_dom_finger_avail():
        return ashley.event_triggers_dict.get("dom_fingers", False)

    def ashley_dom_oral_avail():
        return ashley.event_triggers_dict.get("dom_oral", False)

    def ashley_dom_fuck_avail():
        return ashley.event_triggers_dict.get("dom_fuck", False)

    def ashley_sub_titfuck_avail():
        return ashley.event_triggers_dict.get("sub_titfuck_avail", False)

    def ashley_sub_oral_avail():
        return ashley.event_triggers_dict.get("sub_blowjob_avail", False)

    def ashley_sub_fuck_avail():
        return ashley.event_triggers_dict.get("sub_fuck_avail", False)

    def ashley_sub_anal_avail():
        return ashley.event_triggers_dict.get("sub_anal_avail", False)
