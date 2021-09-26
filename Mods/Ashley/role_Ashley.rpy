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
        ashley_role = Role(role_name ="Ashley", actions =[ashley_ask_date_classic_concert, ashley_ask_about_porn], hidden = True)

        #global ashley_role
        global ashley
        ashley = make_person(name = "Ashley", last_name =stephanie.last_name, age = 22, body_type = "standard_body", face_style = "Face_3",  tits="B", height = 0.89, hair_colour="brown", hair_style = ponytail, skin="white" , \
            eyes = "brown", personality = introvert_personality, name_color = "#228b22", dial_color = "228b22" , starting_wardrobe = ashley_wardrobe, \
            stat_array = [1,4,4], skill_array = [1,1,3,5,1], sex_array = [4,2,2,2], start_sluttiness = 7, start_obedience = -18, start_happiness = 119, start_love = 0, \
            title = "Ashley", possessive_title = "Your intern", mc_title = mc.name, relationship = "Single", kids = 0, force_random = True, base_outfit = ashley_base_outfit,
            forced_opinions = [["production work", 2, True], ["work uniforms", -1, False], ["flirting", 1, False], ["working", 1, False], ["the colour green", 2, False], ["pants", 1, False], ["the colour blue", -2, False], ["classical", 1, False]],
            forced_sexy_opinions = [["taking control", 2, False], ["getting head", 2, False], ["drinking cum", -1, False], ["giving blowjobs", -1, False], ["public sex", -1, False]])

        ashley.set_schedule(stephanie.home, times = [0,1,2,3,4])
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
        ashley.event_triggers_dict["second_date"] = False

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

    ashley_first_talk = Action("Introduce yourself to Ashley",ashley_first_talk_requirement,"ashley_first_talk_label")
    ashley_room_excitement_overhear = Action("Overhear Ashley",ashley_room_excitement_overhear_requirement,"ashley_room_excitement_overhear_label")
    ashley_ask_sister_about_attitude = Action("Ask about Ashley's attitude",ashley_ask_sister_about_attitude_requirement,"ashley_ask_sister_about_attitude_label")
    ashley_room_warming_up = Action("Ashley is warming up",ashley_room_warming_up_requirement,"ashley_room_warming_up_label")
    ashley_porn_video_discover = Action("Discover Ashley's porn video",ashley_porn_video_discover_requirement,"ashley_porn_video_discover_label")
    ashley_ask_sister_about_porn_video = Action("Ask about Ashley in porn",ashley_ask_sister_about_porn_video_requirement,"ashley_ask_sister_about_porn_video_label")
    ashley_room_overhear_classical = Action("Ashley talks about concert",ashley_room_overhear_classical_requirement,"ashley_room_overhear_classical_label")
    ashley_ask_date_classic_concert = Action("Ask Ashley to the Concert",ashley_ask_date_classic_concert_requirement,"ashley_ask_date_classic_concert_label")
    ashley_classical_concert_date = Action("Ashley Date Night",ashley_classical_concert_date_requirement,"ashley_classical_concert_date_label")
    ashley_mandatory_ask_about_porn = Action("Decide to talk to Ashley about porn",ashley_mandatory_ask_about_porn_requirement,"ashley_mandatory_ask_about_porn_label")
    ashley_ask_about_porn = Action("Ask about porn",ashley_ask_about_porn_requirement,"ashley_ask_about_porn_label")
    ashley_post_handjob_convo = Action("Talk to Ashley", ashley_post_handjob_convo_requirement, "ashley_post_handjob_convo_label")
    ashley_stephanie_arrange_relationship = Action("Talk to Stephanie", ashley_stephanie_arrange_relationship_requirement, "ashley_stephanie_arrange_relationship_label")
    ashley_stephanie_saturday_coffee_intro = Action("Good Morning Coffee", ashley_stephanie_saturday_coffee_intro_requirement, "ashley_stephanie_saturday_coffee_intro_label")
    ashley_stephanie_saturday_coffee_recur = Action("Good Morning Coffee", ashley_stephanie_saturday_coffee_recur_requirement, "ashley_stephanie_saturday_coffee_recur_label")
    ashley_clothes_shopping = Action("Ashley goes clothes shopping", ashley_clothes_shopping_requirement, "ashley_clothes_shopping_label")
    ashley_second_concert_date = Action("Ashley gets a second date", ashley_second_concert_date_requirement, "ashley_second_concert_date_label")
    ashley_steph_second_date_confrontation = Action("Stephanie confronts you", ashley_steph_second_date_confrontation_requirement, "ashley_steph_second_date_confrontation_label")

    def ashley_get_days_employed():
        return day - ashley.event_triggers_dict.get("employed_since", 9999)

    def ashley_steph_relationship_status():  #This function should return limited options back, to summarize the current status of MC relationship with Steph and Ashley
        if (ashley.sluttiness > 70 or ashley.is_girlfriend()) and (stephanie.sluttiness > 70 or stephanie.is_girlfriend()):
            return "both"
        elif ashley.is_girlfriend():
            return "ashley"
        elif stephanie.is_girlfriend():
            return "stephanie"
        elif ashley.love - stephanie.love < 20 and ashley.love - stephanie.love > -20:
            return "both"
        elif ashley.love > stephanie.love:
            return "ashley"
        elif ashley.love < stephanie.love:
            return "stephanie"


#Requirement Labels
init -1 python:
    def ashley_intro_requirement():   #After discovering an obedience serum trait and there is a position available. Must be at work.
        if day > 14 and mc.is_at_work() and mc.business.is_open_for_business():
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

    def ashley_room_excitement_overhear_requirement(the_person):
        if the_person.location == the_person.work:
            if ashley_get_days_employed() > 5: #Been working for at least a few days week.
                return True
        return False

    def ashley_ask_sister_about_attitude_requirement(the_person):
        if ashley_get_if_excitement_overheard():
            if the_person.location == the_person.work:
                return True
        return False

    def ashley_room_warming_up_requirement(the_person):
        if the_person.location == the_person.work:
            if ashley_get_days_employed() > 12: #Been working for at least a week.
                return True
        return False

    def ashley_room_overhear_classical_requirement(the_person):
        if the_person.location == the_person.work:
            if ashley_get_days_employed() > 18:
                return True
        return False

    def ashley_ask_date_classic_concert_requirement(the_person):
        if ashley_get_concert_overheard() and not ashley_get_concert_date_stage() > 0:
            if the_person.location == the_person.work:
                return True
        return False

    def ashley_classical_concert_date_requirement():
        if time_of_day == 3:
            if day%7 == 3:  #Thursday
                if ashley_get_concert_date_stage() == 1:
                    return True
        return False

    def ashley_porn_video_discover_requirement():
        if ashley_get_attitude_discussed():
            if time_of_day == 4:
                if mc.energy > 80:
                    return True
        return False

    def ashley_ask_sister_about_porn_video_requirement(the_person):
        if ashley_get_porn_discovered():
            if the_person.location == the_person.work:
                return True
        return False

    def ashley_mandatory_ask_about_porn_requirement():
        if day > ashley_get_porn_convo_day() and ashley_get_concert_date_stage() >= 2:
            if time_of_day > 1:
                if ashley.sluttiness >= 20:
                    return True
        return False

    def ashley_ask_about_porn_requirement(the_person):
        if ashley_get_porn_convo_avail():
            if the_person.location == the_person.work:
                return True
        return False

    def ashley_post_handjob_convo_requirement(the_person):
        if the_person.location == the_person.work:
            return True
        return False

    def ashley_stephanie_arrange_relationship_requirement(the_person):
        if the_person.location == the_person.work:
            return True
        return False

    def ashley_stephanie_saturday_coffee_intro_requirement(the_person):
        if the_person.location == stephanie.location and day%7 == 6 and time_of_day == 0:
            return True
        return False

    def ashley_stephanie_saturday_coffee_recur_requirement(the_person):
        if the_person.location == stephanie.location and day%7 == 6 and time_of_day == 0:
            return True
        return False

    def ashley_second_concert_date_requirement():
        if time_of_day == 3:
            return True
        return False

    def ashley_steph_second_date_confrontation_requirement():
        return False    #This event currently disabled.

    def add_ashley_hire_later_action():
        ashley_hire_directed = Action("Reconsider hiring Stephanie's sister", ashley_hire_directed_requirement, "ashley_hire_directed_label",
            menu_tooltip = "Talk to Stephanie about hiring her sister. She might be disappointed if you decide not to again...")
        mc.business.r_div.add_action(ashley_hire_directed)
        return

    def remove_ashley_hire_later_action():
        mc.business.r_div.remove_action("ashley_hire_directed_label")
        return

    def ashley_clothes_shopping_requirement(the_person):
        if the_person.location == clothing_store:
            return True
        return False

#Story labels
label ashley_intro_label():
    $ the_person = stephanie
    "You are deep in your work when a voice startles you from your concentration."
    the_person "Hey [the_person.mc_title]. Sorry to bug you, do you have a minute?"
    $ scene_manager = Scene()  #Clean Scene
    $ scene_manager.add_actor(the_person)
    mc.name "Of course. What can I do for you?"
    the_person "Well, I kind of need a favor."
    mc.name "Well, you've taken an awfully large risk coming to work for me here, so I suppose I owe you one."
    the_person "You see, it's my sister. She just graduated from college, but is having trouble finding work in her degree. She's had to move in with me because she can't find work!"
    the_person "She's really smart, but very introverted, it's been hard for her to get through interviews."
    mc.name "What is her degree in?"
    the_person "Errrmm... well, it's in Art History. Look, I know this isn't going to be her final career, but even just putting something down as an internship would really help her get a career started."
    the_person "I brought her resume, will you at least take a look at it? I think she would be great over in production."
    menu:
        "Take a look":
            pass
        "Not right now":
            mc.name "I'm sorry, I'm not hiring anyone like that right now. But if I change my mind I'll come find you, okay?"
            the_person "Of course, that's all I can ask, is that you will keep her in mind. Thanks!"
            $ add_ashley_hire_later_action()
            return
        "Blow me and I'll look" if the_person.sluttiness > 50:
            mc.name "I tell you what, why don't you come suck me off while I look over her documents."
            the_person "Oh! A favor for a favor then? Okay!"
            $ scene_manager.update_actor(the_person, position = "blowjob", emotion = "happy")
            "[the_person.possessive_title] gets on her knees and starts to undo your pants."
            $ mc.change_locked_clarity(20)
            the_person "You know I would do this anyway, right?"
            mc.name "Of course, but being reminded of your blowjob skills will probably help me make up my mind if I want to hire someone you're related to."
            call fuck_person(the_person, start_position = blowjob, skip_intro = False, position_locked = True) from _call_sex_description_ashley_intro_bonus_BJ_1
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
        $ the_person.change_happiness(5)
        $ the_person.change_obedience(5)
        the_person "Oh! I didn't think you would say yes. This is great news! I'm sure she'll probably want to get started right away!"

        $ mc.business.hire_person(ashley, "Production")

        "You complete the necessary paperwork and hire [ashley.name], assigning her to the production department."
        "As you finish up, you notice [the_person.possessive_title] is already calling her sister with the news."
        $ scene_manager.update_actor(the_person, position = "walking_away")
        the_person "Hey Ash! Guess what? I got you a starting position at that place I've been..."
        "Her voice trails off as she leaves the room. You hope you made the right decision!"
        $ ashley.add_unique_on_talk_event(ashley_first_talk)
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
    mc.name "I have. Do you still have her documents that I could look over them again?"
    the_person "Of course! Let me get them."
    "[the_person.possessive_title] runs over to her desk and comes back with a folder."
    the_person "Here you go!"
    "You pick up her documents and look over them."
    "From her skill set, it is obvious the best choice of department for here would be in production. The only question is, should you hire her or not?"
    call hire_select_process([ashley, 1]) from _call_hire_ashley_2
    $ the_person.draw_person()
    if _return == ashley:
        mc.name "I agree. She would be perfect for the production department. Would you pass along that she can start tomorrow? Or anytime in the next week."
        $ the_person.change_happiness(5)
        $ the_person.change_obedience(5)
        the_person "Oh! This is great news! I'm sure she'll probably want to get started right away!"
        $ remove_ashley_hire_later_action()
        $ mc.business.hire_person(ashley, "Production")

        "You complete the necessary paperwork and hire [ashley.name], assigning her to the production department."
        "As you finish up and start to leave, you notice [the_person.possessive_title] is already calling her sister with the news."
        $ scene_manager.update_actor(the_person, position = "walking_away")
        the_person "Hey Ash! Guess what? I got you a starting position at that place I've been..."
        "Her voice trails off as you leave the room. You hope you made the right decision!"
        $ ashley.add_unique_on_talk_event(ashley_first_talk)
    else:
        mc.name "I'm sorry, I don't think she is a good fit at this time. But I will keep her in mind for the future, okay?"
        the_person "Wow, really? Why did you even talk to me about this?"
        $ the_person.change_happiness(-10)
        $ the_person.change_obedience(-10)
        $ the_person.change_love(-10)
        $ the_person.draw_person(position = "walking_away")
        "[the_person.possessive_title] gets up and leaves the room. You should probably avoid getting her hopes up again like this."

    return

label ashley_first_talk_label(the_person):
    $ the_person.draw_person()
    mc.name "Hello there. You must be [the_person.name]. I'm [mc.name], the one who owns this place."
    "She looks at you, and see a hint of surprise on her face."
    the_person "Oh!... hello sir. It's nice to meet you. I'm sorry, my sister said this place was all women..."
    mc.name "That's right. Except me, the owner."
    the_person "Ah... I see... Well, thank you for the opportunity. I appreciate the work."
    mc.name "Of course, [stephanie.title] is a good friend. Do you go by [the_person.name]? Or something else?"
    the_person "[the_person.title] is fine..."
    mc.name "[the_person.title] it is then."
    "You chit chat with [the_person.title] for a minute, but she speaks in short, one- or two-word replies. She seems very reserved."
    "Maybe she is just shy? You decide to let her get back to work."
    $ ashley.event_triggers_dict["intro_complete"] = True
    $ ashley.add_unique_on_room_enter_event(ashley_room_excitement_overhear)
    return

label ashley_room_excitement_overhear_label(the_person):
    $ the_person = ashley # on_room_enter_event so the_person isn't defined
    $ the_person.draw_person(position = "standing_doggy")
    "As you step into the room, you can overhear [the_person.title] talking excitedly to another co-worker."
    the_person "I know! I can't wait to go. All of my friends say it's so much fun..."
    "But as you enter the room, she notices, and immediately stops talking."
    $ the_person.draw_person()
    the_person "..."
    "Clearly she has no issue talking to her co-workers... why is she so quiet with you? Maybe you should ask her sister about it."
    $ stephanie.add_unique_on_talk_event(ashley_ask_sister_about_attitude)
    $ ashley.event_triggers_dict["excitement_overhear"] = True
    return

label ashley_ask_sister_about_attitude_label(the_person):
    "You approach [the_person.title], intent to ask her about her sister."
    mc.name "Hello [the_person.title]. Do you have a moment?"
    the_person "Of course sir. What can I do for you?"
    "You lower your voice. You don't necessarily need anyone overhearing you."
    mc.name "Well... I'm not sure how to say this but, I'm a little concerned about [ashley.title]."
    "A grimace forms on her face, but she waits for you to continue."
    mc.name "Earlier, I was walking by and I could hear her carrying on with her coworkers. But as soon as I entered the room, she went completely silent."
    "[the_person.title] nods her head as you keep going."
    mc.name "She barely says a word anytime I talk to her. I feel like I've gotten off to a bad start with her. Do you have any advice?"
    "[the_person.title] clears her throat."
    the_person "Well... [ashley.title] is a bit complicated. She has trouble talking to, and being around men in general..."
    mc.name "Oh? Oh! I see, I mean I guess that makes sense, not everyone is heterosexual..."
    the_person "Noooo, no. It isn't that. She's had boyfriends in the past. But something happened between her and her last boyfriend in college."
    the_person "They broke up all of a sudden, and she's never been the same way around men since then."
    mc.name "Hmm, that sounds like something bad might have happened."
    the_person "Yeah... honestly, I can't really talk about it."
    "[the_person.title] shakes her head, lost in thought."
    mc.name "Thank you for the insight. I appreciate it."
    the_person "Of course."
    $ ashley.add_unique_on_room_enter_event(ashley_room_warming_up)
    $ ashley.event_triggers_dict["attitude_discussed"] = True
    return

label ashley_room_warming_up_label(the_person):
    $ the_person = ashley # on_room_enter_event so the_person isn't defined
    $ the_person.draw_person(position = "standing_doggy")
    "As you step into the room, you can overhear [the_person.title] talking excitedly to another coworker."
    the_person "I know, I just need to find someone to go with!"
    "As you enter the room, she looks and stops talking."
    $ the_person.draw_person()
    the_person "Ahh... hello sir. Having a good day?"
    "Whoa. She actually said hi to you? Maybe she is warming up to you a little bit?"
    mc.name "It's been great so far. And you?"
    the_person "Oh... it's been good I guess..."
    mc.name "Glad to hear it."
    $ mc.business.add_mandatory_crisis(ashley_porn_video_discover)
    $ ashley.add_unique_on_room_enter_event(ashley_room_overhear_classical)
    return

label ashley_room_overhear_classical_label(the_person):
    $ the_person = ashley # on_room_enter_event so the_person isn't defined
    $ the_person.draw_person(position = "standing_doggy")
    "As you step into the room, you can overhear [the_person.title] talking excitedly to another coworker."
    the_person "I know, the city symphony is performing a collection of Johannes Brahms' symphonies. I want to go so bad, but I can't find anyone to go with..."
    "As you enter the room, she looks and stops talking."
    $ the_person.draw_person()
    the_person "Ahh... hello sir. Having a good day?"
    "She has been slowly warming up to you over the last few weeks."
    mc.name "It's been great so far. And you?"
    the_person "Oh, I've been good. Thanks for asking."
    mc.name "Glad to hear it."
    "Hmm... she is looking for someone to go with her to a classical music concert. Maybe that person could be you?"
    $ ashley.event_triggers_dict["concert_overheard"] = True
    return

label ashley_ask_date_classic_concert_label(the_person):
    mc.name "So... I couldn't help hearing earlier, you are looking to go to the Brahms symphony recital, but you don't have anyone to go with?"
    the_person "Ummm yeah, something like that..."
    "She is looking down, avoiding eye contact with you."
    mc.name "That sounds like a great cultural event. I was wondering if you would be willing to let me take you?"
    "She is caught off guard. She wasn't expecting you to ask something like this!"
    the_person "Oh! I uhh, I'm not sure..."
    if stephanie.love > 30 or stephanie.obedience > 130:
        the_person "I suppose... I mean... Steph keeps telling me you are a nice guy..."
    else:
        the_person "I don't know, I mean you seem like a nice guy but..."
        mc.name "I'll tell you what. We could let [stephanie.title] know when it is. She could drop you off and pick you up afterwards."
        "[the_person.title] mumbles something for a second, then relents."
        the_person "I suppose... I mean... Steph keeps telling me I need to go out more."
    mc.name "Ah, great! Do you know when the concert is?"
    the_person "It's on Thursday night."
    mc.name "Ok. I'll plan to meet you there on Thursday night then?"
    the_person "Okay, if you're sure about this..."
    "You feel good about this as you finish up your conversation. Maybe you can finally get her to come out of her shell a little..."
    $ ashley.event_triggers_dict["concert_date"] = 1
    $ mc.business.add_mandatory_crisis(ashley_classical_concert_date)
    return

label ashley_classical_concert_date_label():
    $ the_person = ashley
    $ scene_manager = Scene()
    "It's Thursday. You have a date planned with [the_person.title]. It's taken a while for her to warm up to you, so you don't even consider cancelling."
    "You head downtown. The plan is just to meet up at the concert hall itself. [stephanie.title] is going to drop her sister off and pick her up afterwards."
    $ mc.change_location(downtown)
    $ mc.location.show_background()
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
    #TODO when making story branch, use this first conversation to begin setting up paths. For now, love path only.
    #love: compliment ash. neutral: compliment both. corrupt: crude compliment
    mc.name "Hello! Thanks for this, I've been looking forward to this ever since we arranged it. [the_person.title], you look great tonight!"
    the_person "Ah... thank you."
    $ the_person.change_happiness(1)
    $ the_person.change_love(1)
    "[stephanie.title] gives you a smile after your kind words to her sister."
    $ stephanie.change_obedience(1)
    $ stephanie.change_love(1)
    #End of love option
    stephanie "Alright you two, go enjoy your classical concert. Ash, just text me when you get done, I'm gonna go have a couple drinks."
    the_person "Okay. Bye Steph!"
    $ scene_manager.hide_actor(stephanie)
    mc.name "Shall we?"
    #TODO find concert hall background image to change to.
    "You step into the concert hall, show your tickets, and make you way to your seats."
    $ scene_manager.update_actor(the_person, position = "sitting")
    "You have a few minutes before the concert starts, so you try making some small talk."
    mc.name "So, have you ever been to a concert like this before?"
    the_person "Oh, a few times, when I was in college, but not for over a year."
    mc.name "I'll admit it, this is my first time going to something like this. I'm really excited to have the chance to try something new, though."
    the_person "Oh yeah? I think most guys find classical music a bit boring..."
    #TODO next path branch. different responses. love: glad to be here with you. neutral: glad to be here to watch. corrupt: just here to be with sexy girl
    mc.name "I'll admit I'm not an avid follower, but I think experiencing a variety of cultural events is an important thing for someone to do."
    the_person "Yeah, that's very insightful."
    mc.name "Plus, I'm glad to be able to spend some time with you and get to know you better."
    "You notice her blush a bit, but you can also see her smile."
    $ the_person.change_stats(love = 2, happiness = 2)
    #end branch
    "Soon, the lights dim, and the music begins. It begins with a splendid piano melody."
    "You and [the_person.possessive_title] sit together silently, enjoying the music."
    "It goes through emotional highs and lows. At one point, you look over and you think you see a tear on [the_person.title]'s cheek."
    #TODO next path branch. hold hand (love), put arm around (neutral), or put hand on leg(corrupt)
    "You reach down and take her hand. She jumps at the contact, but quickly takes your hand in hers as the music reaches an especially poignant moment."
    $ mc.change_locked_clarity(5)
    $ the_person.change_stats(love = 5, happiness = 5)
    "You hold hands for the duration of the concert. You both share comments now and then about specific parts that you liked."
    "When the concert is over, the lights slowly come back on. You let go of her hand as you both start to get up."
    $ scene_manager.update_actor(the_person, position = "stand3")
    "You slowly file out of the concert hall, chatting about the concert."
    #TODO change to downtown background
    $ mc.change_location(downtown)
    $ mc.location.show_background()
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
    "[stephanie.title] gives you a look. She smiles, but you can tell she is genuinely protective of [the_person.title]."
    mc.name "As always, [stephanie.title]."
    the_person "He really was. Thanks again [the_person.mc_title]!"
    "It's late, so you all agree to part ways."
    mc.name "Alright, don't forget work tomorrow. I'll see you both then."
    the_person "Bye!"
    stephanie "See ya then!"
    $ scene_manager.clear_scene()
    $ ashley.event_triggers_dict["concert_date"] = 2
    if ashley_get_porn_discussed():
        $ ashley.event_triggers_dict["porn_convo_day"] = day + 3
    return

label ashley_porn_video_discover_label():
    # make sure we are in the bedroom
    $ mc.change_location(bedroom)
    $ mc.location.show_background()
    $ the_person = ashley
    $ the_person.outfit = the_person.wardrobe.get_random_appropriate_underwear(50, sluttiness_min = 20, guarantee_output = True) #Hopefully this gets a slutty underwear set
    $ scene_manager = Scene()
    "It's been a long day. You consider heading for bed, but you've got a lot of energy, and you'd rather not just lie awake in bed."
    "You decide to hop on your PC and watch some porn and jack off before you go to bed. That always helps you fall asleep."
    "You load up your porn accounts and start browsing through some videos."
    "'Desperate Slut Begs for Creampie'? Nah! 'Guy Fucks Step Sister Stuck In Bear Trap'? Hmm... maybe later."
    "As you browse, you notice a clip thumbnail with a girl riding a guy tied down and in restraints. She looks kinda familiar? Reminds you of someone from work maybe?"
    "'Naughty Co-Ed Ties Up Boyfriend. RUINED ORGASM'? Eh, it's worth a shot anyway. You click on it and wait for the generic porn intro to finish."
    "You mouth falls open when the scene starts."
    $ scene_manager.add_actor (the_person, position = "stand4", emotion = "happy")
    $ mc.change_locked_clarity(10)
    "There's a guy and a girl, who you immediately recognize as [the_person.title]. This looks like one of those hidden camera type videos."
    "The guy is tied up, with his four limbs tied to the four corners of a bed. You watch as [the_person.title] gets up on the bed and crawls on top of him."
    $ scene_manager.update_actor(the_person, position = "doggy")
    "She turns and puts her ass right in his face. She starts to ride his face roughly."
    $ mc.change_locked_clarity(10)
    "[the_person.possessive_title] strokes the guy a little bit, but basically ignores his cock as she rides his face."
    "She does this for several minutes, until she starts to moan and really ride the guy roughly. Her moans get loud, sounds like she is finishing."
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
    "Wow... shy [the_person.title]..."
    "This seems pretty crazy. She seems to some kind of closet dom? It's hard to believe."
    "She is so quiet... there's no way you can talk to her about it yet. Maybe you should bring it up with [stephanie.title] first?"
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
    mc.name "I wanted to talk to you again, about your sister, [ashley.title]."
    the_person "Oh!... right..."
    if the_person.sluttiness > 50:
        "Her back slumps noticeably when you say that."
    mc.name "This is not going to be an easy or pleasant conversation, but uhh, I found a video of your sister..."
    the_person "UGH! I thought we got that deleted from everywhere."
    mc.name "Oh... deleted?"
    $ scene_manager.update_actor (the_person, emotion = "sad")
    the_person "Yeah, she had this boyfriend a while back. It came out after they broke up that he was secretly filming them having sex and posting it online..."
    the_person "We did everything we could to shut it down once we found out, but the internet is crazy. Once it's out there, it's out there!"
    mc.name "Wow, I feel awful, I had no idea."
    the_person "Yeah. Unfortunately, having that happen really got to her. That was like, over a year ago? And she hasn't been out with anyone since."
    the_person "As you probably saw... she was pretty... adventurous... with guys."
    the_person "But now it's almost like she can't trust any guys anymore."
    "You both look at each other for a moment, considering the circumstance."
    mc.name "I want to do something, but I don't know what."
    if the_person.love > 30:
        the_person "I don't know either... I guess just... keep being you?"
        the_person "You are a wonderful guy. Just be there for her, okay? You are, like, the only guy she interacts with any more."
    else:
        the_person "I mean, you are, like, the only guy she interacts with... at all. She has completely cut herself off from men."
        the_person "Maybe you could try, like, you know, being there for her? Help her learn that not all men are total assholes?"
    mc.name "I suppose. Anything specific?"
    the_person "Honestly? I'm not really sure. Ash moving back in with me only just happened, and we didn't really see each other much while going through college."
    "After a few solemn moments, you decide to move on with your day."
    mc.name "That's enough for now I suppose. Let me know if you think of anything."
    the_person "Yes sir... and the same for you."
    "You both walk back to the [mc.location.formal_name]."
    $ mc.location.show_background()
    $ scene_manager.clear_scene()
    $ ashley.event_triggers_dict["porn_discussed"] = True
    if ashley_get_concert_date_stage() > 1:
        $ ashley.event_triggers_dict["porn_convo_day"] = day + 3
    $ mc.business.add_mandatory_crisis(ashley_mandatory_ask_about_porn)
    return

label ashley_mandatory_ask_about_porn_label():
    "You've had some time to think about [ashley.possessive_title], since you went on your date and discovered she was in a porn video unwittingly."
    "She seems to have warmed up to you enough; you decide that maybe it is the right time to talk to her about it."
    $ ashley.event_triggers_dict["porn_convo_avail"] = True
    return

label ashley_ask_about_porn_label(the_person):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person)
    "You decide to broach the difficult topic of the porn video you discovered."
    mc.name "I was hoping to talk to you about something a little sensitive. Would you mind if we went to my office?"
    the_person "Oh... sure..."
    $ ceo_office.show_background()
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
    "[the_person.title] smiles and blushes a bit. She is so shy, but so cute when she does that."
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
    mc.name "I just wanted to tell you, I'm sorry about what happened. If you need any assistance going forward, please don't hesitate. I want to help if I can."
    the_person "Well... Steph and I... We worked hard to get that video off the internet. But once it's out there, it's out there, I guess."
    "She looks down and thinks for a bit."
    the_person "The, umm... the video. Did you watch the whole thing?"
    mc.name "Yeah... yeah I did."
    "She looks a little sheepish, but continues."
    the_person "Did... you know... you like it?"
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
    $ mc.change_arousal(30)
    $ mc.change_locked_clarity(20)
    "DAMN. You feel your pants get a little tight after that. You remember from the video the way [the_person.title] took control and rode her ex..."
    mc.name "I mean, you don't have to do that..."
    $ scene_manager.update_actor(the_person, position = "stand4")
    "She gets up and walks around your desk. You stand up too."
    the_person "It's okay. I'm going to. You just enjoy."
    "With nothing else to say, [the_person.possessive_title] reaches down and begins to stroke your cock through your pants."
    the_person "Mmmm, I can tell you want it too!"
    "[the_person.title] has some skilled hands... You close your eyes and enjoy her stroking you for a moment."
    $ mc.change_arousal(10)
    $ mc.change_locked_clarity(20)
    "You hear a zipper some fabric rustle for a moment, then suddenly feel her warm hand on your dick, skin to skin. You look down and see her pulling your dick out."
    if the_person.has_taboo("touching_penis"):
        the_person "Oh my god... it's so big... You've been hiding this from me, [the_person.mc_title]?"
        "She gives you a couple eager strokes. You can only moan in response. It feels good to finally feel her hands on you."
        $ the_person.break_taboo("touching_penis")
        $ mc.change_arousal(15)
    else:
        the_person "God, it's so big. I love getting your cock out..."
        "She gives you a couple eager strokes. You can only moan in response."
        $ mc.change_arousal(10)
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
    "You walk back to the [mc.location.formal_name]."
    $ ashley.event_triggers_dict["porn_convo_avail"] = False
    $ mc.location.show_background()
    $ scene_manager.clear_scene()
    $ ashley.add_unique_on_talk_event(ashley_post_handjob_convo)
    $ jump_game_loop() # she runs after her sister so end talk with Ashley
    return

label ashley_post_handjob_convo_label(the_person):
    "You decide not to give [the_person.title] too much time to overthink what happened in your office. You swing by her desk."
    $ the_person.draw_person()
    mc.name "Hey [the_person.title]..."
    the_person "Oh... haha, yeah, I figured something like this was coming... it's okay, I'll clean out my desk and be out before you know it..."
    mc.name "Clean out your desk? I'm not firing you. Come on let's go get some coffee."
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
    "She's looking down at her feet. She's so shy, you can tell she is uncomfortable."
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
    $ renpy.show("restaurant", what = restaraunt_background)
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
        mc.name "I understand that, but isn't what I want important too? I've known Stephanie for years, but I've only just recently met you."
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
    "WARNING: This decision will have lasting consequence on your relationships with [the_person.title] and [stephanie.title]!"
    menu:
        "I want to be with you \n{color=#ff0000}{size=18}Love path{/size}{/color}" if (ashley_steph_relationship_status() == "ashley" or ashley.love > 30):
            mc.name "I know this is kind of crazy, but I have really enjoyed my time with you."
            mc.name "[stephanie.title] and I go back a ways... but I don't really think of her as more than just a friend."
            mc.name "But you... I find myself thinking about you constantly. [the_person.title], will you be my girlfriend?"
            "[the_person.possessive_title] is smiling wide, it takes her a moment to answer."
            the_person "Oh... I don't know how to talk to Steph about this... but I want that really bad! Yes I'll be your girlfriend."
            mc.name "Don't worry, I'll talk to [stephanie.title]."
            $ the_person.event_triggers_dict["story_path"] = "normal"
            $ the_person.change_stats(love = 5, happiness = 5, obedience = 5)
            $ the_person.add_role(girlfriend_role)
        "Let's keep us secret \n{color=#ff0000}{size=18}Corruption path{/size}{/color}" if (ashley_steph_relationship_status() == "stephanie" or ashley.sluttiness > 30):
            mc.name "I think I know what to do, where we can all be happy."
            the_person "Oh?"
            mc.name "Alright, let me explain the whole thing before you make up your mind. What if we keep things between us strictly physical, and don't tell [stephanie.title]?"
            the_person "Errrm... you want to do what now?"
            $ the_person.change_stats(love = -5, happiness = -5, obedience = 5)
            mc.name "Look, [stephanie.title] was the one in the first place that told me to ask you out. She wants you to be happy, and I think she knows you're going through a dry spell."
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
            $ assign_jealous_sister_role(the_person, stephanie)
        "I want to be friends with both of you \n{color=#ff0000}{size=18}Friends with benefits path \n Not yet written{/size}{/color}" if (ashley_steph_relationship_status() == "both" or mc.charisma > 4):
            mc.name "There are a lot of feelings going on right now, but I think we all need to calm down a bit."
            mc.name "[stephanie.title] and I go back a ways, but I just think of her as a friend."
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
    "It's time to talk to [the_person.title]. You approach her in the lab."
    mc.name "Hey, we need to chat. Can you come with me to my office?"
    the_person "Sounds good."
    "You walk to your office. She enters first, and you close the door behind your you both take a seat."
    $ ceo_office.show_background()
    $ the_person.draw_person(position = "sitting")
    mc.name "So, I want to talk to you about me and [ashley.title]..."
    the_person "Yeah, I figured. Look, I know, I encouraged the whole thing, so I shouldn't be surprised when you two were messing around..."
    if ashley_is_secret_path():
        mc.name "It's not like that, [the_person.title]. Me and [ashley.title] got caught up in the moment, yes, but we've talked it over and decided to be just friends."
        "You feel a little bit bad about trying to keep your relationship with [ashley.possessive_title] a secret, but you're sure if you play your cards right it'll be worth it long term."
        if the_person.is_girlfriend():
            the_person "I have to admit... I'm a little bit relieved to hear that. I thought I was losing my boyfriend! And to my sister!.. we haven't always gotten along, but I was really hoping it hadn't come to that."
            mc.name "I'm sorry for what happened. It won't happen again."
        else:
            the_person "I... I don't understand... Why aren't you interested in Ashley?"
            mc.name "It isn't that I'm not interested, as much as that I'm currently interested in someone else..."
            "You give [the_person.title] a wink. When she realizes what you mean, she blushes."
            the_person "Oh wow, I didn't realize that you felt the same way... Oh [the_person.mc_title]... Can we just make it official? I want everyone to know that I'm your girlfriend!"
            "Realizing that your plan to keep things secret with [ashley.title] isn't going to work unless you take things further with [the_person.title], you agree."
            mc.name "Here, let me do this, officially. [the_person.title], will you be my girlfriend?"
            the_person "Yes! Oh yay! I thought for sure you were gonna get with Ashley... I was so jealous... When I saw..."
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
        "You puts her arms around her and you pull her close. You bring your face to hers and you kiss for a few moments. She slowly steps back."
        $ the_person.draw_person(position = "stand2")
        the_person "Alright... I'm going to get back to work. I'm so glad we got to talk!"
        "As [the_person.possessive_title] leaves the room, you wonder if you are being smart. Keeping your relationship with her sister secret, even it's only physical, might be difficult."
    elif ashley_is_fwb_path():
        mc.name "I know it seems like things between [ashley.title] and I are moving really fast, but I want you to know it probably isn't what you are thinking."
        the_person "Oh? I mean... You went on a date and then she was giving you a handjob in your office..."
        mc.name "[ashley.title] is an interesting girl, for sure, but I'm not interested in a relationship with her. We both have some physical needs, so we've decided to be friends... With benefits..."
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
            mc.name "And thank you for that. If it weren't for you, I never would have met [ashley.title]."
            the_person "Yeah... Just being honest here... It's hard not to be a little jealous?"
            mc.name "I'm sorry... I'll try not to make things awkward..."
            the_person "I guess that means we probably shouldn't fuck anymore..."
            mc.name "I guess not..."
        else:
            the_person "Honestly, I'm really happy for you two. I was just caught off guard when I walked in on you two..."
            if the_person.sluttiness > 40:
                the_person "It's going to be hard for me to keep my hands off of you from now on, but my sister deserves it. We may not have always gotten along, but I'm glad she's found someone like you."
            else:
                "Ash is a special girl, okay? You better take good care of her. We may not have always gotten along, but I'm glad she's found someone to make her happy."
        mc.name "Thank you. It means a lot to get your approval of this."
        $ the_person.draw_person(position = "stand2")
        "[the_person.possessive_title] stands up and smiles. It looks a little forced, but she's trying to be genuine."
        the_person "Thank you for this chat. I feel better knowing what is going on with you two. Now... I think I'll get back to work?"
        "[the_person.title] turns and leaves your office. Things got a little sticky there, but you feel like you are now in the clear to pursue things with [ashley.title] from now on."
    $ clear_scene()
    $ stephanie.set_alt_schedule(coffee_shop, days = [6], times = [0])
    $ ashley.set_alt_schedule(coffee_shop, days = [6], times = [0])
    $ ashley.add_unique_on_room_enter_event(ashley_stephanie_saturday_coffee_intro)
    call advance_time from _call_advance_ashley_arrangement_01
    return

label ashley_stephanie_saturday_coffee_intro_label(the_person):
    $ the_person = ashley
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person, display_transform = character_center_flipped, position = "sitting")
    $ scene_manager.add_actor(stephanie, position = "sitting")
    "As you are walking downtown, you pass by the coffee shop. Looking inside, you are surprised to see Ashley and Stephanie sitting inside."
    "You decide to step inside and say hello."
    mc.name "Hey girls, good to see you."
    "They are surprised to see you. Ashley blushes and looks down at her coffee as Stephanie responds."
    stephanie "Hey boss! Me and Ash are just having a cup of coffee before we go our separate ways. It's kind of become our little tradition every Sunday morning, since she moved in with me."
    "She looks over at her sister and starts to tease her. "
    stephanie "I think she said something about hitting up the gym today... I think there's a guy she's trying to impress!"
    the_person "Oh my gosh Steph, stop it!"
    "[the_person.title] is blushing, and once in a while sneaks a peek up at you. Even though you've already discussed with her how you want things to be with her, it is cute to see her squirm a little."
    mc.name "Is that true [the_person.title]? Who might this lucky guy be?"
    the_person "Ah. Errm... Well..."
    "She's sputtering out unintelligible mumbles."
    stephanie "Don't worry Ash. I'm sure whoever it is will appreciate you putting in the time to keep your body fit!"
    "[the_person.possessive_title] is relieved when her sister intervenes and changes the subject."
    stephanie "Hey, why don't you grab a coffee and join us? It's kind of nice to hang out in a non-work environment."
    mc.name "Oh, I wouldn't want to interrupt you two having some family time together..."
    "Surprisingly, it's [the_person.title] that interrupts you."
    the_person "It's fine! We live together, remember?"
    "You raise an eyebrow. It's not often that she speaks up, but clearly [the_person.title] wants you to hang out too. Suddenly, she realizes she is speaking up and quiets down."
    the_person "I mean... It would be okay, right? We don't mind at all..."
    mc.name "Okay. Just give me a moment and I'll get something. Either of you two want something while I'm in line?"
    "The sisters look at each other. [the_person.title] shakes her head and [stephanie.possessive_title] responds."
    stephanie "No thanks! We're good for now, but maybe another time we'll let you buy us coffees!"
    "You excuse yourself and head up to the counter. You glance back at the two sisters as you wait in line."
    "It's amazing how similar the girls are, but still so different. [the_person.title] is so quiet and shy, but sometimes when you talk with her you can see glimpses of the fiery passions that drive [stephanie.title]."
    "You order your coffee, and soon the hot brew is in your hand. As you walk back to the table, you decide to use the opportunity to try and get to know them both a little better."
    "The sisters are sitting opposite to each other at the booth... Who should you sit next to?"
    menu:
        "[the_person.title]" if not ashley_is_secret_path():    #Depending on previous choices, MC may have to sit next to a particular girl.
            "[the_person.possessive_title] scoots over to give you room to sit next to her. She sneaks a peek at you and you see a slight smile on her lips."
            $ scene_manager.update_actor(stephanie, display_transform = character_right(yoffset = .125, zoom = 1.25))
            $ scene_manager.update_actor(the_person, display_transform = character_center_flipped(yoffset = -.125, zoom = 0.75))
            $ the_person.change_stats(love = 3, happiness = 5)
            $ ashley_set_coffee_partner(the_person)
        "[stephanie.title]" if not ashley_is_normal_path():
            "[stephanie.possessive_title] scoots over so you have room to sit next to her."
            stephanie "Have a seat, [stephanie.mc_title]."
            $ scene_manager.update_actor(stephanie, display_transform = character_right(yoffset = -.125, zoom = 0.75)) #TODO this is broken and I don't know why
            $ scene_manager.update_actor(the_person, display_transform = character_center_flipped(yoffset = .125, zoom = 1.25))
            "She pats the seat next to her. You sit down and see her smirking at you before she keeps talking to her sister."
            $ stephanie.change_stats(love = 3, happiness = 5)
            $ ashley_set_coffee_partner(stephanie)
    "You listen to the two sisters chat for a bit as you enjoy your coffee. [the_person.title] seems to almost forget you are at the table, and you get a glimpse into her personality as she talks with her older sibling."
    $ overhear_topic = the_person.get_random_opinion(include_sexy = False)
    $ text_one = person_opinion_to_string(the_person, overhear_topic)[1]
    $ text_two = get_topic_text(overhear_topic)
    the_person "... but yeah, I have to say I [text_one] [text_two]"
    if the_person.discover_opinion(overhear_topic):
        "Oh! You didn't realize that [the_person.title] felt that way."
    "The sisters discuss it for a bit. You kind of zone out for a little bit as the conversation changes to clothing. The girls are discussing some different brands..."
    "Suddenly the girls stop talking. You look up and notice they are both looking out the window. A woman is walking by the coffee shop window out in the street."
    call coffee_time_woman_walks_by_label() from _coffee_time_intro_outfit_01
    stephanie "Well, I'd better get going. I've got some errands to run!"
    "You stand up and both girls also get up."
    mc.name "Thank you for the pleasant morning. You two have a good day."
    stephanie "You bet boss! We do this pretty much every Sunday. Feel free to join us!"
    "[stephanie.possessive_title]'s invitation is tempting. [the_person.title] is smiling at you, clearly mirroring her sisters invitation to join again."
    stephanie "Next week you're buying the coffees though!"
    mc.name "That's acceptable. With us all being employees, I'll just put it down as a company expense."
    "You say your goodbyes and go separate ways. This could be an interesting opportunity in the future to learn more about the sisters."
    $ the_person.add_unique_on_room_enter_event(ashley_stephanie_saturday_coffee_recur)
    $ ashley_reset_coffee_partner()
    call advance_time from _call_advance_ashley_coffee_advance_01

    python:
        scene_manager.clear_scene()
    return

label ashley_stephanie_saturday_coffee_recur_label(the_person):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person, display_transform = character_center_flipped, position = "sitting")
    $ scene_manager.add_actor(stephanie, position = "sitting")
    "You swing by the coffee shop. Right on time, you see [the_person.title] and [stephanie.title] in a booth. You walk over to the table."
    mc.name "Good morning! Who's up for coffee?"
    stephanie "Good morning [stephanie.mc_title]! That would be great! Can I get an Americano with two creams?"
    the_person "Good morning. I like mine black..."
    if stephanie.sluttiness > 20:
        stephanie "That's what she said!"
        "The girls are laughing at [stephanie.possessive_title]'s joke as you head up to the counter and order the coffees."
    # TODO: add serums to coffees here
    $ mc.business.funds -= 15
    if the_person.is_girlfriend():
        "As you wait for your coffees to get made, you spot a yummy looking blueberry muffin. You decide to get it to share with [the_person.title]."
        $ mc.business.funds -= 5
    elif stephanie.is_girlfriend():
        "As you wait for your coffees to get made, you spot a yummy looking blueberry muffin. You decide to get it to share with [stephanie.title]."
        $ mc.business.funds -= 5
    "You walk back to the table and give the girls their coffee."
    if the_person.is_girlfriend():
        the_person "Ohh, that looks good..."
        "[the_person.possessive_title] spots your muffin. You slide into the booth next to her."
        $ scene_manager.update_actor(stephanie, display_transform = character_right(yoffset = -.1, zoom = 0.9))
        $ scene_manager.update_actor(the_person, display_transform = character_center_flipped(yoffset = .1, zoom = 1.1))
        mc.name "Got it for us to share."
        "You glance over at [stephanie.title]. A hint of jealousy crosses her face, but she quickly hides it."
        $ ashley_set_coffee_partner(the_person)
    elif stephanie.is_girlfriend():
        stephanie "Ohh! Yum, that looks tasty [stephanie.mc_title]."
        "[stephanie.possessive_title] spots your muffin. You slide into the booth next to her."
        $ scene_manager.update_actor(stephanie, display_transform = character_right(yoffset = .1, zoom = 1.1))
        $ scene_manager.update_actor(the_person, display_transform = character_center_flipped(yoffset = -.1, zoom = 0.9))
        mc.name "Got it for us to share."
        "You glance over at [the_person.title]. A hint of jealousy crosses her face, but she quickly hides it."
        $ ashley_set_coffee_partner(stephanie)
    else:
        "The sisters are sitting opposite to each other at the booth... Who should you sit next to?"
        menu:
            "[the_person.title]":    #Depending on previous choices, MC may have to sit next to a particular girl.
                "[the_person.possessive_title] scoots over to give you room to sit next to her. She sneaks a peek at you and you see a slight smile on her lips."
                $ scene_manager.update_actor(stephanie, display_transform = character_right(yoffset = .1, zoom = 1.1))
                $ scene_manager.update_actor(the_person, display_transform = character_center_flipped(yoffset = -.1, zoom = 0.9))
                $ the_person.change_stats(love = 3, happiness = 5)
                $ ashley_set_coffee_partner(the_person)
            "[stephanie.title]":
                "[stephanie.possessive_title] scoots over so you have room to sit next to her."
                stephanie "Have a seat, [stephanie.mc_title]."
                $ scene_manager.update_actor(stephanie, display_transform = character_right(yoffset = -.1, zoom = 0.9))
                $ scene_manager.update_actor(the_person, display_transform = character_center_flipped(yoffset = .1, zoom = 1.1))
                "She pats the seat next to her. You sit down and see her smirking at you before she keeps talking to her sister."
                $ stephanie.change_stats(love = 3, happiness = 5)
                $ ashley_set_coffee_partner(stephanie)
    "As you sit down, the girls are sharing their plans for the weekend. You take a few sips of your coffee enjoying the flavor."
    if not the_person.event_triggers_dict.get("second_date", False) and the_person.sluttiness > 40 and stephanie.sluttiness > 40 and ashley_is_secret_path():
        call ashley_second_concert_intro_label(the_person) from _start_ashley_second_date_path_01

    $ steph_action = steph_coffee_time_get_random_action()
    if steph_action:
        $ steph_action.call_action()
        $ del steph_action
    else:
        "You sit and have a lively conversation with the girls while you drink your coffee, but nothing of any major consequence comes up."
    "Your coffee is almost gone. You consider getting another one, but continue to sit with the two sisters, enjoying the lively conversation."

    $ ashley_action = ashley_coffee_time_get_random_action()
    if ashley_action:
        $ ashley_action.call_action()
        $ del ashley_action
    else:
        "You sit and have a lively conversation with the girls while you drink your coffee, but nothing of any major consequence comes up."

    "The conversation is starting to die down a bit, and your coffee cup is dry. You decide to head out."
    mc.name "Thank you for the company. I think it's about time for me to go."
    stephanie "Hey, you know where to find us next week!"
    the_person "Bye [the_person.mc_title]..."
    $ the_person.add_unique_on_room_enter_event(ashley_stephanie_saturday_coffee_recur)
    call advance_time from _call_advance_ashley_coffee_advance_02

    python:
        scene_manager.clear_scene()
    return

label ashley_second_concert_intro_label(the_person):
    #We assume this is at the beginning of a coffee time event. Ashley is the_person and the scene is already set up.
    #MC has just bought a muffin for stephanie and sat down next to her
    $ the_person.event_triggers_dict["second_date"] = True

    "As you sit down next to [stephanie.title], [the_person.possessive_title] goes back to her phone, clearly distracted by something."
    mc.name "So... any big plans this weekend?"
    stephanie "Not for me! I was thinking maybe we could do something later tonight?"
    "[stephanie.possessive_title] gives you a little wink and puts her hand on your thigh. Suddenly [the_person.title] speaks up."
    the_person "Yes!!! Oh my god, Steph! I need to borrow your boyfriend tonight!"
    stephanie "I... errrmm... I guess?"
    the_person "The Los Angeles Philharmonic had sold out for the show tonight... fucking scalpers... but this morning they release a bunch of extra tickets. I managed to grab two!"
    stephanie "Ok... but... why do you need to borrow my boyfriend?"
    the_person "I mean, I know you hate going to classical shows, and I don't know anyone else who would want to go... Please? It's just one night!"
    "[stephanie.title] mumbles something under her breath. She is clearly not happy with the situation, but relents."
    stephanie "I guess..."
    "She leans over and whispers in your ear."
    stephanie "Don't let her get handsy with you again..."
    "[stephanie.possessive_title]'s hand moves to your crotch, giving it a couple quick strokes."
    $ mc.change_locked_clarity(10)
    stephanie "I know she's hot, but your MY boyfriend. Got it?"
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
    #TODO link up mandatory event for the date itself.
    $ mc.business.event_triggers_dict["girlfriend_sleepover_scheduled"] = True
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
    "Evening falls and soon it is time to make your way downtown to meet [the_person.title], your girlfriend's sister, for a date to another classical music concert."
    "Things with the two girls have gotten complicated. Ashley has been able to keep things between you a secret from her sister, but is getting more and more demanding and needy."
    "Lately it seems like [stephanie.title] is getting a little suspicious, and [the_person.possessive_title]'s demand to share you for a date is certain to have her unsettled."
    $ mc.change_location(downtown)
    $ mc.location.show_background()
    "When you arrive, you looked around for a minute, but don't see Ashley yet at your agreed on meeting place. You decide to give her a few minutes. You are just about to pull out your phone and text her when you see her approaching."
    "She is wearing a sexy black dress, and your eyes are immediately drawn to it's curves. There's not a doubt in your mind that [the_person.title] has something planned for you this evening..."
    $ mc.change_locked_clarity(20)
    $ the_person.draw_person()
    ashley "Hey! My eyes are up here."
    mc.name "Yeah but I wasn't looking at your eyes."
    "When you finally lift your eyes from her body and meet hers, she has a mischievous smile."
    ashley "Good. God I finally get you all to myself for one evening."
    mc.name "Are we still going to the concert?"
    ashley "Of course! I wasn't lying, and I'll be damned if I miss the opportunity to see the Los Angeles Philharmonic. Tickets weren't cheap you know! And my cheapskate boss barely pays me enough to cover the cost of living."
    "Wow, she is pretty sassy this evening. You tease each other a bit more but make your way into the concert."
    #[Change background]
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
    mc.name "When we can go do stuff like this more often, then go back to your place after, and me, you, and Stephanie all hop in bed together and screw until the sun comes up."
    ashley "Ha! Oh wow. You've been watching some good porn lately huh? I don't think Steph is really the sharing type... I'm usually not either..."
    mc.name "And yet, here you are, with your sister's boyfriend. Maybe you just haven't met someone worth sharing before?"
    "[the_person.title] is quiet. Right on cue, the lights turn down and the music begins."
    #[Change lighting to dark]
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
    # change lighting
    "The lights come back on and people start to get up. You can see [ashley.title]'s chest rising and falling rapidly. She is breathing heavy and is really turned on."
    $ the_person.draw_person()
    mc.name "Well, I promised to get you home straight away."
    "You give her a wink as you say it. She chuckles and winks back."
    $ mc.change_location(downtown)
    $ mc.location.show_background()
    "You step outside and start to walk her home. However, as you pass an empty alleyway, you feel her hand tug at your as she drags you back the alley."
    "You both take a quick look around. Certain that you are alone, you push her up against the wall."
    $ the_person.draw_person(position = "kissing")
    "[the_person.possessive_title] moans as you kiss her neck. You feel her hands on your shoulders, pushing you down on your knees."
    "You go with it. You're sure that after all that edging, she is probably close to cumming anyway."
    $ the_person.draw_person(position = "against_wall")
    "[the_person.title] props her leg up on a box, giving you easy access to her cunt. As you start to lick along the inside her thighs, she runs her hands through you hair."
    the_person "Mmm, do a good job and I'll repay the favor..."
    "If you do good, she'll probably repay you. But you should be careful, you still have to go see [stephanie.possessive_title] later! If you make it too obvious, she'll probably know something is up..."
    call fuck_person(the_person, start_position = standing_cunnilingus, skip_intro = True, position_locked = True, private = True) from _call_sex_description_ashley_second_date_cunnilingus_01
    $ the_report = _return
    #TODO make sure MC arousal stays the same?
    if the_report.get("girl orgasms", 0) == 0:
        $ the_person.draw_person()
        "[the_person.title] puts her leg down. She is incredulous."
        the_person "Seriously? [stephanie.name] really has you wrapped around her finger, doesn't she? I don't know why I bother with you..."
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
                        if the_person.outfit.is_dress():
                            "[the_person.possessive_title]'s face is covered in your cum. Somehow, it doesn't seem like any of it got on her dress..."
                        else:
                            "[the_person.possessive_title]'s face is covered in your cum. Thankfully her dress came off at some point, so no cum dripped on it."
                    elif the_person.has_mouth_cum():
                        "[the_person.possessive_title] has a bit of cum on her chin, but is able to quickly clean it up."
                    elif the_person.has_tits_cum():
                        if the_person.outfit.is_dress():
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
                mc.name "I promised her I wouldn't go to far. You got your satisfaction, I'll get mine later."
                the_person "Geeze, okay. I was about to offer to drink your cum as thank, but I guess you'd better save that load then champ."
                "[the_person.possessive_title] pulls a couple wipes from her clutch and wipes herself clean."
            "Let her continue":
                $ the_person.draw_person(position = "blowjob")
                "As she gets down on her knees, she quickly undoes your zipper and pulls your cock out."
                "She gives it a couple strokes, then looks up at you and smiles."
                the_person "You'd probably better cum in my mouth... don't want to get it all over my clothes before we go back and see [stephanie.name]."
                $ mc.change_locked_clarity(30)
                $ date_outcome = "blowjob"
                "You put your hand on the back of her head."
                mc.name "You say that like you have a choice."
                "She smirks for a second, but quickly opens her mouth as you pull her head down. Her velvet lips wrap around you and start to eagerly suck you off."
                call get_fucked(the_person, the_goal = "oral creampie", private= True, start_position = blowjob, skip_intro = True, ignore_taboo = True, allow_continue = False) from _ashley_second_date_blowjob_01
                $ the_report = _return
                if the_report.get("guy orgasms", 0) > 0:
                    if the_person.has_face_cum():
                        if the_person.outfit.is_dress():
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
                        "You growl at [the_person.possessive_title]"
                        mc.name "You let me worry about [stephanie.title]."
                        "Without waiting further response, you line yourself up and push your cock into [the_person.title]'s drenched pussy."
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
                    if the_person.outfit.is_dress():
                        "[the_person.possessive_title]'s ass looks amazing covered in your cum. But you slowly realize... it's all over her dress."
                        $ cum_clue = True
                    else:
                        "[the_person.possessive_title]'s ass looks amazing covered in your cum. Thankfully her dress came off at some point, so no cum got on it."
                elif the_person.has_face_cum():
                    if the_person.outfit.is_dress():
                        "[the_person.possessive_title]'s face is covered in your cum. Somehow, it doesn't seem like any of it got on her dress..."
                    else:
                        "[the_person.possessive_title]'s face is covered in your cum. Thankfully her dress came off at some point, so no cum dripped on it."


            "Help her recover":
                mc.name "I understand. Here, let me help you."
                "You grab her arm and help her stand. It takes her several minutes, but finally gets her legs back."
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
    $ mc.location.show_background()
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
        $ stephanie.change_happiness(-5)
        $ stephanie.change_love(-5)
        $ scene_manager.remove_actor(the_person)
        "[the_person.title] disappears into the restroom, leaving you with [stephanie.title]. You can tell she is suspicious, but for now, she decides not to say anything about it."
    else:
        the_person "Hey sis! We had a great time, and don't worry, your boyfriend was a gentleman."
        stephanie "Ah, that's good."
        the_person "I'm wore out. I think I'm going to go have a shower. You two try to keep it down so I can get some sleep tonight, okay?"
        stephanie "No promises."
        $ scene_manager.remove_actor(the_person)
        "[the_person.title] disappears into the restroom, leaving you with [stephanie.title]."
    $ scene_manager.update_actor(stephanie, position = "kissing")
    "She gives you a hug and whispers in your ear."
    stephanie "I'm so glad to finally have you for myself. Let's go to my room!"
    $ scene_manager.clear_scene()

    $ stephanie.draw_person(position = "walking_away")
    "You follow [stephanie.possessive_title] to her bedroom. She closes the door, then pushes you back onto her bed."
    "She strips down in front of you."
    $ stephanie.strip_outfit(position = "stand4")
    "She climbs up on top of you and starts to undo your pants. Soon, your cock springs free."
    $ stephanie.draw_person(position = "cowgirl")
    stephanie "Mmm, I've been thinking about riding on this all night. Let's get you nice and hard."
    "[stephanie.title] leans forward and licks all around the top of the shaft, then starts to suck on the tip."
    $ mc.change_locked_clarity(30)
    if (date_outcome == "handjob" and not cum_clue) or date_outcome == None:
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
                mc.name "I was little worried I might get tempted... so I masturbated beforehand."
                stephanie "Oh! I guess that makes sense..."
                "She starts to suck on your cock again. You think she bought your excuse. "
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
                pass
                #TODO this
                $ caught_ashley_cheating = True
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
        if cum_clue:
            stephanie "I knew that was cum all over her dress in the hall! Just admit it! You fucked her!"
        else:
            stephanie "I knew she couldn't keep her hands off you. You fucked her, didn't you?"
        "It seems there is no way of talking your way out of this one. You are totally busted."
        $ caught_ashley_cheating = True

    if caught_ashley_cheating:
        "Sorry, the repercussions for Stephanie catching you cheating with Ashley have not yet been written."
        #TODO make a mandatory event to trigger in a day or two where you and stephanie make up.
    else:
        stephanie "Mmm, you taste so good... but that's not the only thing I want from you tonight..."
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
                "Fine with you. This isn't the first time tonight you had a condom on."
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
            $ picked_event.call_action(stephanie)
        else:
            "You wake up, but [stephanie.possessive_title] isn't there. She must have gotten up early and left."
            $ stephanie.planned_outfit = stephanie.decide_on_outfit() # choose a new outfit for the day
            $ stephanie.apply_planned_outfit()

    python:
        mc.business.event_triggers_dict["girlfriend_person"] = None
        mc.business.event_triggers_dict["girlfriend_sleepover_scheduled"] = False  #Reset these so we can have another girlfriend sleepover.
        del cum_clue
        del caught_ashley_cheating
        del date_outcome
    return

label ashley_steph_second_date_confrontation_label():
    "This scene not yet written."
    return

#Coffee time labels
#Labels in this section are to be randomly called during the coffee time event.
#TODO should this be actions? It would make setting requirements way easier... parse just like  crisis list...
label coffee_time_innocent_chat_label():
    $ the_person = ashley
    "The two sisters are chatting about kinds of different things."
    "Its fun to be in a situation where [the_person.title] opens up and actually... talks..."
    $ overhear_topic = the_person.get_random_opinion(include_sexy = False)
    $ text_one = person_opinion_to_string(the_person, overhear_topic)[1]
    $ text_two = get_topic_text(overhear_topic)
    the_person "... but yeah, I'm not sure he realizes I [text_one] [text_two]"
    if the_person.discover_opinion(overhear_topic):
        "Oh! You didn't realize that [the_person.title] felt that way."
    "The girls keep talking. They keep bouncing back and forth between multiple topics. You just listen as you sip your coffee."
    $ overhear_topic = stephanie.get_random_opinion(include_sexy = False)
    $ text_one = person_opinion_to_string(stephanie, overhear_topic)[1]
    $ text_two = get_topic_text(overhear_topic)
    stephanie "...But I [text_one] [text_two], so I'm not sure what to do."
    if stephanie.discover_opinion(overhear_topic):
        "Wow, you knew they were sisters, but they really do talk about basically everything!"

    python:
        del overhear_topic
        del text_one
        del text_two
    return

label coffee_time_sexy_chat_label():
    $ the_person = ashley
    "The two sisters are chatting about all kinds of different things."
    "Not surprisingly, the subject of the chatting turns sexual, as the two sisters talk about different sexual encounters."
    $ overhear_topic = stephanie.get_random_opinion(include_sexy = True, include_normal = False)
    $ text_one = person_opinion_to_string(stephanie, overhear_topic)[1]
    $ text_two = get_topic_text(overhear_topic)
    stephanie "... but yeah, I have to say I [text_one] [text_two]"
    if stephanie.discover_opinion(overhear_topic):
        "Oh! You didn't realize that [stephanie.title] felt that way."
    $ mc.change_locked_clarity(10)
    "The girls keep talking. They keep bouncing back and forth between multiple sexual topics."
    $ overhear_topic = the_person.get_random_opinion(include_sexy = True, include_normal = False)
    $ text_one = person_opinion_to_string(the_person, overhear_topic)[1]
    $ text_two = get_topic_text(overhear_topic)
    the_person "...But I [text_one] [text_two], so I'm not sure what to do."
    if the_person.discover_opinion(overhear_topic):
        "Wow, you didn't realize they talked about sex in such detail with each other."
    $ mc.change_locked_clarity(10)

    python:
        del overhear_topic
        del text_one
        del text_two
    return

label coffee_time_steph_gets_handsy_label():
    $ the_person = ashley
    $ cum_on_hand = False
    "Without any provocation, you feel [stephanie.possessive_title]'s hand on your thigh. She is rubbing back and forth, but is slowly drifting higher."
    "[stephanie.title] is keeping a completely inconspicuous attitude."
    stephanie "So Ash, any good concerts coming up soon?"
    "As she asks her sister, her hand drifts up to your crotch. It rapidly hardens as she begins to stroke it carefully."
    $ mc.change_locked_clarity(20)
    the_person "No... Not that I'm aware of anyway... The Chicago symphony is doing a charity live-stream later though, so I might watch that..."
    $ mc.change_arousal(15)
    "You decide two can play at this game. In the same way, you carefully run your hand along her thigh until it's resting on her mound. She gives a small sigh when you start to apply pressure on it."
    $ stephanie.change_arousal(15)
    if stephanie.sluttiness < 30:
        "You and [stephanie.title] pet each other for several minutes. You are both getting aroused, but with clothes in the way it's impossible to finish."
        $ mc.change_locked_clarity(10)
        "With the public setting of the booth, you don't dare to push things any farther."
        if stephanie.is_girlfriend():
            "[stephanie.title] leans over and whispers in your ear."
            stephanie "Why don't I come over to your place tonight, and we can do something like this, but with way less clothes..."
            $ mc.change_locked_clarity(15)
            menu:
                "Have her come over" if schedule_sleepover_available():
                    "You give her a nod. She takes that as her cue to stop."
                    stephanie "I'll see you tonight then..."
                    $ schedule_sleepover_in_story(stephanie)
                "Have her come over (disabled)" if not schedule_sleepover_available():
                    pass
                "Not tonight":
                    mc.name "I can't tonight, maybe another night..."
    else:
        "You and [stephanie.title] pet each other for a few minutes, but stroking each other through you clothes can only take things so far."
        if stephanie.get_opinion_score("public sex") > 0:
            "She decides to push things further. You feel her hand clumsily reach into your pants, eventually pulling your cock out. The soft skin of her hand feels great."
            "Not to be outdone, you bring your hand up Stephanie's body, then slowly slide it under her clothes. When you get to her slit, you push you middle finger inside of her, while pressing your palm against her clit."
            "She sighs, but doesn't seem particularly concerned about other people around."
            $ mc.change_locked_clarity(20)
        else:
            "Not content to leave things where they are, you take the next step. You bring your hand up [stephanie.possessive_title]'s body, then slowly slide it under her clothes."
            "She squirms a bit and glances around nervously as your hand reaches her slit. She sighs when your middle finger pushes inside of her, but is on alert for anyone who might be watching."
            "Not to be outdone, [stephanie.title] starts to undo your zipper. She clumsily reaches into your pants and pulls your cock out. The soft skin of her hand feels great as she starts to stroke you."
            $ mc.change_locked_clarity(20)
        $ mc.change_arousal(30)
        $ stephanie.change_arousal(30)
        if the_person.sluttiness < 40:
            "You and [stephanie.title] continue to pet each other at the booth, sipping your coffees once in a while with your free hands."
            "Across the table, [the_person.title] appears to be completely oblivious. [stephanie.possessive_title] is beginning to squirm as you stroke her gspot with your finger."
            $ mc.change_arousal(30)
            $ stephanie.change_arousal(30)
            the_person "So... I'm thinking about going to the spa later treat myself to something... Do you want to go Steph?"
            stephanie "Oh!!! Uhh... Yesssss..."
            "[stephanie.title] practically growls. She's getting close and having trouble hanging on. You use the palm of your hand to grip her pussy harder, while your finger runs circles around her g spot."
            $ stephanie.change_arousal(30)
            $ mc.change_locked_clarity(20)
            "She stops stroking you as she finishes. She leans forward a bit, closing her eyes as her pussy begins quivering around your finger."
            "You wish your cock was inside her instead of your finger, but in a place like a coffee shop booth, you can't justify risking it."
            $ stephanie.have_orgasm(half_arousal = False, the_position = "sitting")
            if stephanie.get_opinion_score("public sex") > 0: #[If Steph likes public sex, she finishes you no matter what.]
                "[stephanie.possessive_title] eventually opens her eyes, taking a quick peek around, then begins stroking you again."
                "Seems she is intent on giving you a similar treatment. You slowly pull your hand out of her clothes."
                stephanie "Are you going to look at those tops we were looking at the other day Ash?"
                "[stephanie.title] picks up the conversation with her sister."
                stephanie "I really liked the way that crop top look on you."
                "Some of your precum is starting to leak out. [stephanie.possessive_title] uses her thumb to spread it around the tip then keeps stroking."
                $ mc.change_locked_clarity(20)
                the_person "I don't know... I like the shirt but I don't know if I like how much skin it shows..."
                stephanie "Aww, you should try it anyway! Guys like seeing a little midriff. Don't you agree [stephanie.mc_title]?"
                "This time it's you who is barely able to get a reply out."
                mc.name "Ah yes. Yes it's very nice."
                "[the_person.title] raises an eyebrow. You think she is probably finally beginning to sense something is up..."
                mc.name "I mean, only if you feel comfortable with it..."
                "You manage to get out. She seems to buy it for now."
                the_person "I guess..."
                "The conversation continues, but you stop listening. The soft hand of [stephanie.title] drives you over the edge and you start to cum in her hand."
                "Your cum spurts up and hits the bottom of the table before falling back down onto [stephanie.possessive_title]'s hand and your pants. Oh fuck you are making a mess..."
                $ ClimaxController.manual_clarity_release(climax_type = "air", the_person = stephanie)
                $ cum_on_hand = True
            else: #[Steph neutral or doesn't like public sex, give player the option]
                "As [stephanie.title] regains her senses, she looks around for a moment. She looks at you and gives you a couple tentative strokes, clearly unsure of what to do."
                menu:
                    "Keep going":
                        "You slowly pull your hand away from [stephanie.possessive_title]'s crotch. You put your hand on hers and encourage her to stroke you, making it clear that you expect her to continue."
                        "She looks around nervously but begins jacking you off again on her own."
                        $ mc.change_locked_clarity(20)
                        mc.name "So what are you thinking about getting done at the Spa? I hear they have really good service there."
                        "You keep the conversation going so Steph can concentrate on her work. You are starting to leak precum, making her handjob feel even better."
                        the_person "Oh, ahh, well I want to get my nails done for sure... "
                        "[the_person.possessive_title] starts to explain. However, [stephanie.title] is looking around nervously and she is starting to notice."
                        the_person "You okay Steph? You seem preoccupied..."
                        "She startles and looks back at her sister."
                        stephanie "Oh! Yeah I just thought I saw someone..."
                        "Under the table you are reaching your limit. The soft hand of [stephanie.title] drives you over the edge and you start to cum in her hand."
                        "Your cum spurts up and hits the bottom of the table before falling back down onto [stephanie.possessive_title]'s hand and your pants. Oh fuck you are making a mess..."
                        $ ClimaxController.manual_clarity_release(climax_type = "air", the_person = stephanie)
                        $ cum_on_hand = True
                    "Stop":
                        "While [the_person.possessive_title] is looking something up on her phone, you whisper into [stephanie.title]'s ear."
                        mc.name "Sorry, I don't want to make a mess here..."
                        if stephanie.is_girlfriend():
                            "[stephanie.title] leans over and whispers in your ear."
                            stephanie "That's okay... maybe I can come over tonight and make it up to you?"
                            $ mc.change_locked_clarity(20)
                            menu:
                                "Have her come over" if schedule_sleepover_available():
                                    "You give her a nod. She takes that as her cue to stop."
                                    stephanie "I'll see you tonight then..."
                                    $ schedule_sleepover_in_story(stephanie)
                                "Have her come over (disabled)" if not schedule_sleepover_available():
                                    pass
                                "Not tonight":
                                    mc.name "I can't tonight, maybe another night..."
                        "[stephanie.possessive_title] releases your erection, leaving it aching with need. You quickly put yourself away and zip up as [the_person.title] finishes pulling up a picture on her phone."
                        the_person "So I was thinking about getting my haircut to something like this... What do you think?"
                        "You continue your coffee date with the sisters, with [the_person.title] unaware of you getting her sister off right in front of her."
        else:
            the_person "So I was thinking about going to the spa... Do you think I should..."
            "[the_person.title] stops mid question and is looking at her sister. She quickly realizes what is going on."
            if ashley_is_secret_path():
                the_person "Wow... I guess I should have expected you two wouldn't be able to keep your hands off each other. I'll just play on my phone while you two do your thing..."
                "[the_person.title] gives you a look of what you can only call pure jealousy, before she pulls out her phone and starts looking at it."
            elif ashley_is_fwb_path():
                "You feel [the_person.title]'s foot beneath the table begin to rub along your leg."
                the_person "Damn... Right here in the booth? That's kinda hot..."
                $ mc.change_locked_clarity(30)
            "You push the palm of your hand rigidly against [stephanie.possessive_title]'s clit, while your middle finger strokes her gspot. Your attention to her sensitive spots soon haa her gasping."
            "Only a whimper escapes her lips when you feel her pussy begin to quiver around your finger. She stops stroking you as she focuses on the pleasure of orgasming in the palm of your hands."
            $ stephanie.have_orgasm(half_arousal = False, the_position = "sitting")
            "After several seconds, [stephanie.title] slowly opens her eyes and glances around as you withdraw your hand."
            if ashley_is_fwb_path():
                "Wow, that looked hot... [the_person.mc_title] will you do something like that to me later?"
                "TODO give hookup option here"
            if stephanie.get_opinion_score("public sex") >= 0 and stephanie.get_opinion_score("giving blowjobs") >= 0 and (stephanie.get_opinion_score("public sex") > 0 or stephanie.get_opinion_score("giving blowjobs") > 0):
                stephanie "Hey Ash... Can you act natural for a minute and cover me? I need to take care of something..."
                "[stephanie.title] gives her sister a wink, and [the_person.title] gives her a nod." #TODO (If she's looking at her phone, ashley agrees but is embarrassed)
                "[stephanie.possessive_title] looks around to make sure no one is watching, but then slowly sinks in her seat and then slips under the table."
                $ scene_manager.update_actor(stephanie, position = "blowjob")
                "She gets between your legs and immediately goes to work, sucking you off. [the_person.possessive_title] hears the slurping noises start and looks at you."
                $ mc.change_locked_clarity(40)
                if ashley_is_fwb_path():
                    the_person "Wow. I bet that feels good."
                elif ashley_is_secret_path():
                    "[the_person.title] doesn't say a word, but she puts two fingers in the shape of a V, the brings it to her face and sticks her tongue out between them, then points to herself."
                    "She is making it clear she is expecting you to get her off later."
                    $ mc.change_locked_clarity(20)
                    $ the_person.add_jealous_event("She blew you at the coffee shop!", 2)
                "The wet tongue of [stephanie.title] is driving you quickly to orgasm. Between the public setting, her partial handjob, and talented mouth, you are sure you can't take any more."
                "You relax and enjoy the blowjob. Soon your orgasm approaches. There's no easy way to warn [stephanie.title], so you just let it go, firing your load into her mouth."
                $ stephanie.cum_in_mouth()
                $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = stephanie)
                "Her talented mouth takes your load easily. When you finish, her mouth slowly releases your cock and you hear a loud gulp."
                "You look around to make sure you are still anonymous before putting your hand on her shoulder and then helping her back up and into her seat."
                $ scene_manager.update_actor(stephanie, position = "sitting")
                "Once back up, she wipes what little cum managed to get on her face with a napkin and sets it aside. [stephanie.title] shakes her head."
                $ stephanie.outfit.remove_all_cum()
                $ scene_manager.draw_scene()
            else:
                "[stephanie.title] eventually opens her eyes, taking a quick peek around, then begins stroking you again."
                "Seems she is intent on giving you a similar treatment. You slowly pull your hand away from her crotch."
                stephanie "Your cock feels so hot in my hand..."
                $ mc.change_locked_clarity(20)
                "[stephanie.possessive_title] whispers in your ear. Some of your precum is starting to leak out. She uses her thumb to spread it around the tip then keeps stroking."
                "The soft hand of [stephanie.title] drives you over the edge and you start to cum in her hand."
                $ ClimaxController.manual_clarity_release(climax_type = "air", the_person = stephanie)
                "Your cum spurts up and hits the bottom of the table before falling back down onto [stephanie.possessive_title]'s hand and your pants. Oh fuck you are making a mess..."
                $ cum_on_hand = True
    if cum_on_hand:
        "[stephanie.title] checks her hand while it's still under the table. It is absolutely coated in your cum."
        if stephanie.get_opinion_score("public sex") >= 0 and stephanie.get_opinion_score("drinking cum") >= 0 and (stephanie.get_opinion_score("public sex") > 0 or stephanie.get_opinion_score("drinking cum") > 0):
            if the_person.sluttiness < 40:
                "[stephanie.possessive_title] beings her hand up from underneath the table and begins to lick your cum off of it. [the_person.title] notices and looks puzzled for a second, then realizes what she is doing."
                if ashley_is_secret_path():
                    the_person "Jesus Steph... Can you two seriously not keep your hands off each other for two seconds? You are nuts!"
                    "[the_person.title] looks at you, jealousy clear on her face."
                    $ the_person.add_jealous_event("She gave you a handjob at the coffee shop!", 1)
                    # TODO Ash gains sluttiness, loses obedience and love
                elif ashley_is_fwb_path():
                    the_person "Jesus... Right here? You two are crazy..."
                    "[the_person.title] looks at you with a sparkle in her eye."
                    "[the_person.mc_title]... Does that mean I get you after this?"
                    $ mc.change_locked_clarity(20)
                    #TODO Ash gains sluttiness and obedience
                    #TODO [Give mc option to promise to get with Ashley after]
            else:
                "[the_person.title] just watches as [stephanie.title] brings her hand up from underneath the table and begins to lick your cum off of it."
                $ the_person.add_jealous_event("She gave you a handjob at the coffee shop!", 1)
        else:
            "You pick up a napkin and bring it under the table. You hold it in place as [stephanie.title] wipes her hand off on it. You grab another napkin and use it to clean yourself off as best you can, hoping no one will notice."
    return

label coffee_time_woman_walks_by_label(): #Whoever's turn it is should be the person one in this label.
    $ the_person = ashley
    $ preferences = WardrobePreference(the_person)
    $ bystander = get_random_from_list(known_people_in_the_game(excluded_people = [ashley, stephanie]))

    if not bystander:
        return  # exit loop if we have no bystander

    "Enjoying your coffee, you zone out for a minute while the two sisters are chatting, when suddenly the talking stops. You look up and see them both looking out the restaurant window."
    "Outside is a woman who has stopped and is checking her phone for something. The girls are checking her out."

    $ scene_manager.add_actor(bystander, display_transform = character_left_flipped, position = "stand3")
    "She takes a moment to look at something on her phone."
    "Then she walks away."
    $ scene_manager.add_actor(bystander, display_transform = character_left_flipped, position = "walking_away")
    "The girls watch as she walks away."
    $ scene_manager.remove_actor(bystander)
    the_person "Wow, did you see that?"
    $ temp_string = bystander.outfit.build_outfit_name()
    stephanie "The [temp_string]?"
    if preferences.evaluate_outfit(bystander.outfit, the_person.sluttiness + 10) == True:
        the_person "Yeah. I really liked it! I could totally see myself wearing something like that."
    else:
        $ temp_string = "I know that the outfit " + preferences.evaluate_outfit_get_return(bystander.outfit, the_person.sluttiness + 10) + ", but what if I did something similar?"
        the_person "[temp_string]"
    "[stephanie.title] considers it for a moment."
    if the_person.approves_outfit_color(bystander.outfit):
        stephanie "I suppose so. I mean the color was nice."
    else:
        stephanie "I don't know, I don't usually see you wear that colour."
        $ favorite_colour = the_person.favorite_colour()
        the_person "I could do something like that but in [favorite_colour]."
        stephanie "That would be interesting."
    "[the_person.possessive_title] sips her coffee and thinks about it for a bit."
    stephanie "What do you think [stephanie.mc_title]? Sometimes it's easy to fall into the trap of just wearing what is comfortable. Do you think she would look good in that?"
    if stephanie.is_girlfriend():
        "[the_person.possessive_title] glances at you. She tries not to show it, but you can tell she is interested in your opinion."
    else:
        "[the_person.possessive_title] listens to your response intently. You can tell she is interested in your opinion."
    menu:
        "Yes":
            the_person "I think I'm gonna go over to the mall this afternoon and try some stuff on. I could use a new outfit!"
            "Hmm, maybe you should swing by the mall later and help [the_person.title] go clothes shopping?"
            $ ashley_set_observed_outfit(bystander.outfit)
            $ ashley.set_alt_schedule(clothing_store, days = [6], times = [2])
            $ ashley.add_unique_on_room_enter_event(ashley_clothes_shopping)
        "No":
            the_person "Ahh..."
            "[the_person.possessive_title] sinks down in her seat a bit. You can tell she is a little embarrassed."

    python:
        del bystander
        del preferences
    return

label ashley_clothes_shopping_label(the_person):
    "You decide to swing by the clothing store, where [the_person.title] said she would be at. After a few awkward minutes poking around the women's clothing, you spot her."
    $ the_person.draw_person()
    "She seems preoccupied and doesn't notice you until you walk up."
    mc.name "Hey [the_person.title]. I thought I might find you here."
    the_person "Ah... Hello..."
    if ashley_is_fwb_path():
        mc.name "I remembered at the coffee shop this morning you said you were gonna come here. I was in the area and thought I could swing by. I thought you might appreciate a male perspective on your outfits?"
        the_person "Oh, I suppose that would be okay..."
        "Without the security of her sister nearby, [the_person.possessive_title]'s shy demeanor is really showing."
    elif ashley_is_secret_path():
        mc.name "You said you were gonna try on a couple things. I thought maybe you would appreciate the opinion of a secret admirer..."
        the_person "Ah, that sounds good..."
    elif ashley_is_normal_path():
        mc.name "When you said you were gonna swing by here later, I knew I wanted to come out and see some of these outfits for myself."
        "She smiles and replies shyly."
        the_person "Ah, that's good. Let's see what we can find."

    "[the_person.title] looks around at a few different clothing racks and puts an outfit together. It looks very similar to the outfit you saw earlier today. You follow her over to the changing rooms."
    if ashley.is_girlfriend():
        the_person "Here... Come on in with me. You're my boyfriend I'm sure no one will mind."
        "You quickly slip into the dressing room with [the_person.title]."
    elif the_person.sluttiness > 30:
        "She looks around and sees that there isn't anyone around."
        the_person "Here... Come in with me, before anyone notices..."
        "You quietly slip into the dressing room with [the_person.title]."
    "You sit down at the bench and watch as [the_person.possessive_title] starts to strip down."
    $ the_person.strip_outfit(exclude_upper = False)
    $ mc.change_locked_clarity(30)
    if the_person.sluttiness > 50:
        "Although she doesn't say a word, [the_person.title] doesn't make any move to cover herself either. Her body is on display as she reaches for her outfit..."
    else:
        "[the_person.title] absentmindedly covers her mound with one hand as she reaches for her outfit."
    $ the_person.apply_outfit(the_person.personalize_outfit(ashley_get_observed_outfit(), coloured_underwear = True, max_alterations = 1))
    $ the_person.draw_person()
    "When she finishes putting on her new outfit, she steps back so you can get a good look."
    the_person "Okay... What do you think?"
    $ the_person.draw_person(position = "back_peek")
    "She gives a quick twirl, letting you check her out from all angles. You make sure to take in all of the details."
    $ the_person.draw_person()
    menu:
        "Keep it":
            mc.name "I like it. You should get it."
            the_person "I think so too. Thanks!"
            $ the_person.wardrobe.add_outfit(the_person.outfit)
        "Not for you":
            mc.name "Sorry, it's an interesting outfit, but I don't think it's right for you."
            the_person "Yeah... I was thinking the same thing..."
    if the_person.is_girlfriend():
        # the_person "So, I know that like... Clothes shopping can be pretty boring for guys... So I was wandering..."
        # "Her voice trails off. You can tell she is trying to suggest something fun, but she's to shy to say it out loud."
        # mc.name "You want to make this more interesting?"
        # the_person "Err, kind of... I was thinking, maybe while I change, you could go pick something out for me? As a reward for helping me... I'll try on anything you want me to..."
        # "That does sound like a fun proposition!"
        # the_person "If it's too crazy though, maybe it's an outfit we could save for the bedroom..."
        # mc.name "Sounds good! I'm sure I can find something..."
        # "You step out of the dressing and browse the clothes racks, looking for a nice outfit for your girlfriend."
        # [Outfit screen]
        # [If not outfit]
        # For some reason, you can't seem to put together a good look for Ashley. You head back to the dressing room and apologize through the door.
        # "Hey, sorry Ashley, for some reason I couldn't come up with anything..."
        # "Oh! That's okay... Sorry to put you on the spot like that..."
        # [Have outfit]
        # You put something together and take it back to the dressing room. Making sure no one is around, you quietly slip into the room.
        # [Draw naked ashley]
        # You hand her the outfit. When she finishes putting it on, she checks herself in the mirror.
        # [Draw outfit backpeek]
        # [If normal outfit]
        # "Hmm... Interesting..."
        # [Draw standing]
        # "I could wear this... For you anyway..."
        # Ashley gives you a shy smile.
        # "I'll get it for you. Now go out and wait for me! I'll be right out..."
        # [If slutty]
        # "Oh... Oh my..."
        # [Draw standing]
        # "Would this excite you? If you came over and when I answered the door I was wearing this?.."
        # "Definitely..."
        # "Mmm... Okay... I'll get it... But I'm only gonna wear it for you!"
        # "Now go out and wait for me..."
        # [Clear ashley]
        $ clear_scene()
        $ the_person.apply_outfit(the_person.planned_outfit)
        "She shoos you out of the changing room. In a few minutes, she emerges from the changing room."
        $ the_person.draw_person()
        the_person "Thanks for waiting..."
        the_person "Say, do you wanna come over tonight? You could, you know, stay over..."
        $ mc.change_locked_clarity(20)
        menu:
            "Come over later" if schedule_sleepover_available():
                mc.name "I wouldn't mind a sleepover."
                the_person "I'll see you tonight then..."
                $ schedule_sleepover_in_story(the_person)
            "Come over later (disabled)" if not schedule_sleepover_available():
                pass
            "Not tonight":
                mc.name "I can't tonight, maybe another night..."

        "You say goodbye to [the_person.title] for now."
    elif the_person.jealous_score() > 0:
        "Before she starts to change back, [the_person.title] starts to tease you."
        the_person "So... I can't help but notice that [stephanie.name] has been getting a lot of attention lately..."
        $ the_person.strip_outfit(exclude_lower = True)
        $ desc_tuple = the_person.jealous_sister_get_revenge_tuple()
        the_person "[desc_tuple[0]]"
        $ the_person.strip_outfit()
        the_person "I can't help like feel like it should be my turn to get off..."
        "She walks over to you. Sitting on the bench, her cunt is now just inches away."
        $ mc.change_locked_clarity(20)
        $ the_position = cowgirl
        if desc_tuple[1] == 1: #Foreplay
            $ the_position = drysex_cowgirl
        elif desc_tuple[1] == 2:
            $ the_position = standing_cunnilingus
        elif desc_tuple[1] >= 4:    #If 4 let the system make a position for her.
            $ the_position = None
        call get_fucked(the_person, the_goal = "get off", private= True, start_position = the_position, allow_continue = True) from _ashley_jealous_clothes_tryout_01
        if _return.get("girl orgasms", 0):
            the_person "Ahhh, that was nice. Good to know my sister isn't getting ALL your attention!"
            $ the_person.reset_all_jealousy()
            $ the_person.change_love(3)
            $ the_person.change_slut(1)
        else:
            the_person "Wow, really? You can't give me the same treatment that [stephanie.name] gave you? She got you all worn out?"
            "She looks pissed."
            $ the_person.change_love(-3)
            $ the_person.change_slut(1)
            $ the_person.jealous_change_score(3) #Add points to jealous score so ashley gets more desperate.
        $ the_person.draw_person(position = "stand2")
        "You get yourself put back together."
        mc.name "I'm going to slip out."
        the_person "Okay, I'll see you around [the_person.mc_title]."
        $ clear_scene()
        "You quietly exit the changing room."
    else:
        the_person "Thanks for the opinion. I'm going to go ahead and change back..."
        mc.name "I'm going to slip out."
        the_person "Okay, I'll see you around [the_person.mc_title]."
        $ clear_scene()
        "You quietly exit the changing room."

    return

label ashley_test_outfit_scene():
    $ scene_manager = Scene()
    $ the_person = ashley
    $ preferences = WardrobePreference(the_person)
    $ bystander = get_random_from_list(known_people_in_the_game(excluded_people = [ashley, stephanie]))

    if not bystander:
        return  # exit loop if we have no bystander

    "Enjoying your coffee, you zone out for a minute while the two sisters are chatting, when suddenly the talking stops. You look up and see them both looking out the restaurant window."
    "Outside is a woman who has stopped and is checking her phone for something. The girls are checking her out."

    $ scene_manager.add_actor(bystander, display_transform = character_right_flipped, position = "stand3")
    "She takes a moment to look at something on her phone."
    "Then she walks away."
    $ scene_manager.add_actor(bystander, display_transform = character_right_flipped, position = "walking_away")
    "The girls watch as she walks away."
    $ scene_manager.remove_actor(bystander)
    the_person "Wow, did you see that?"

    $ new_outfit = the_person.personalize_outfit(bystander.outfit, the_colour = "the colour green", coloured_underwear = True, max_alterations = 1)

    $ ashley.apply_outfit(new_outfit)
    $ stephanie.apply_outfit(new_outfit)
    $ scene_manager.add_actor(ashley)
    "[ashley.name] models her new outfits for you."

    python:
        del bystander
        del preferences
    $ scene_manager.clear_scene()
    return


label ashley_unit_test():
    python:
        the_person = ashley
        the_person.situational_sluttiness = {} #A dict that stores a "situation" string and the corresponding amount it is contributing to the girls sluttiness.
        the_person.situational_obedience = {}
        the_person.arousal = 0
        the_person.energy = the_person.max_energy
        the_person.sluttiness = 0
        the_person.sluttiness = 0
        the_person.obedience = 0
        the_person.happiness = 100
        the_person.love = 0
    "Unit Test Ashley hiring scene."
    call ashley_intro_label from _unit_test_ashley_01
    if ashley.is_employee():
        "You hired Ashley"
    else:
        "You did not hire Ashley."
        call ashley_hire_directed_label from _unit_test_ashley_02
        "You still have not hired Ashley. Aborting unit test."

    "Unit test Ashley Intro."
    call ashley_first_talk_label(the_person) from _unit_test_ashley_03

    "A few days later"
    call ashley_first_talk_label(the_person) from _unit_test_ashley_04


    call ashley_room_excitement_overhear_label(the_person) from _unit_test_ashley_05
    call ashley_ask_sister_about_attitude_label(stephanie)from _unit_test_ashley_06
    call ashley_room_warming_up_label(the_person) from _unit_test_ashley_07
    call ashley_room_overhear_classical_label(the_person) from _unit_test_ashley_08
    call ashley_ask_date_classic_concert_label(the_person) from _unit_test_ashley_09
    call ashley_ask_date_classic_concert_label(the_person) from _unit_test_ashley_10
    call ashley_classical_concert_date_label() from _unit_test_ashley_11
    call ashley_porn_video_discover_label() from _unit_test_ashley_12
    call ashley_ask_sister_about_porn_video_label(stephanie) from _unit_test_ashley_13
    python:
        the_person.situational_sluttiness = {}
        the_person.situational_obedience = {}
        the_person.arousal = 0
        the_person.energy = the_person.max_energy
        the_person.sluttiness = 20
        the_person.sluttiness = 20
        the_person.obedience = 0
        the_person.happiness = 100
        the_person.love = 0

    call ashley_mandatory_ask_about_porn_label() from _unit_test_ashley_14
    call ashley_ask_about_porn_label(the_person) from _unit_test_ashley_15
    return

label ashley_unit_test2():
    python:
        the_person = ashley
        the_person.situational_sluttiness = {}
        the_person.situational_obedience = {}
        the_person.arousal = 0
        the_person.energy = the_person.max_energy
        the_person.sluttiness = 40
        the_person.sluttiness = 40
        the_person.obedience = 0
        the_person.happiness = 100
        the_person.love = 0
        stephanie.love = 100
        stephanie.sluttiness = 40
        stephanie.sluttiness = 40
        stephanie.energy = stephanie.max_energy
        mc.max_energy = 200
        mc.energy = mc.max_energy
    call ashley_post_handjob_convo_label(the_person) from _unit_test_ashley_16
    call ashley_stephanie_arrange_relationship_label(stephanie) from _unit_test_ashley_17
    call ashley_stephanie_saturday_coffee_intro_label(the_person) from _unit_test_ashley_18
    python:
        the_person.situational_sluttiness = {}
        the_person.situational_obedience = {}
        the_person.arousal = 0
        the_person.energy = the_person.max_energy
        the_person.sluttiness = 40
        the_person.sluttiness = 40
        the_person.obedience = 0
        the_person.happiness = 100
        the_person.love = 0
        stephanie.love = 100
        stephanie.sluttiness = 40
        stephanie.sluttiness = 40
        stephanie.energy = stephanie.max_energy
    "Coffee recurring. She should be ready for second date to proc from this."
    call ashley_stephanie_saturday_coffee_recur_label(the_person) from _unit_test_ashley_19
    #ashley_second_concert_intro_label(the_person)
    call ashley_second_concert_date_label() from _unit_test_ashley_20

    return

init 2 python: #Coffee time requirements function. #TODO should I pull out coffee times stuff to its own file? this file might get too big.
    def coffee_time_innocent_chat_requirement():
        return True

    def coffee_time_woman_walks_by_requirement():
        return True

    def coffee_time_sexy_chat_requirement():
        if stephanie.sluttiness > 40 and ashley.sluttiness > 40:
            return True
        return False

    def coffee_time_steph_gets_handsy_requirement():
        if stephanie.sluttiness > 40:
            if ashley_get_coffee_partner() == stephanie:
                return True
        return False

init 3 python:
    ashley_coffee_time_action_list = []
    steph_coffee_time_action_list = []

    coffee_time_innocent_chat = Action("Sister Talk", coffee_time_innocent_chat_requirement, "coffee_time_innocent_chat_label")
    coffee_time_sexy_chat = Action("Sister Sexy Talk", coffee_time_sexy_chat_requirement, "coffee_time_sexy_chat_label")
    coffee_time_steph_gets_handsy = Action("Stephanie gets handsy", coffee_time_steph_gets_handsy_requirement, "coffee_time_steph_gets_handsy_label")
    coffee_time_woman_walks_by_label = Action("Woman walks by", coffee_time_woman_walks_by_requirement, "coffee_time_woman_walks_by_label")

    ashley_coffee_time_action_list.append(coffee_time_innocent_chat)
    ashley_coffee_time_action_list.append(coffee_time_sexy_chat)
    ashley_coffee_time_action_list.append(coffee_time_woman_walks_by_label)
    steph_coffee_time_action_list.append(coffee_time_innocent_chat)
    steph_coffee_time_action_list.append(coffee_time_sexy_chat)
    steph_coffee_time_action_list.append(coffee_time_steph_gets_handsy)

    def ashley_coffee_time_get_random_action():
        possible_action_list = []
        for ashley_scene in ashley_coffee_time_action_list:
            if ashley_scene.is_action_enabled(): #Get the first element of the weighted tuple, the action.
                possible_action_list.append(ashley_scene) #Build a list of valid crises from ones that pass their requirement.
        return get_random_from_list(possible_action_list)

    def steph_coffee_time_get_random_action():
        possible_action_list = []
        for steph_scene in steph_coffee_time_action_list:
            if steph_scene.is_action_enabled(): #Get the first element of the weighted tuple, the action.
                possible_action_list.append(steph_scene) #Build a list of valid crises from ones that pass their requirement.
        return get_random_from_list(possible_action_list)


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


    def ashley_non_con_enabled():
        return ashley.event_triggers_dict.get("non_con", False)
