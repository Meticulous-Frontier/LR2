

init 2 python:
    def ashley_mod_initialization(): #Add actionmod as argument#

        ashley_wardrobe = wardrobe_from_xml("Ashley_Wardrobe")
        ashley_base_outfit = Outfit("ashley's base accessories")
        the_eye_shadow = heavy_eye_shadow .get_copy()
        the_eye_shadow.colour = [.18, .54, .34, 0.95]
        the_rings = copper_ring_set.get_copy()   #Change this
        copper_ring_set.colour = [.1,.36,.19,1.0]
        ashley_base_outfit.add_accessory(the_eye_shadow)
        ashley_base_outfit.add_accessory(the_rings)

        # init ashley role
        ashley_role = Role(role_name ="Ashley", actions =[ashley_ask_date_classic_concert, ashley_ask_about_porn], hidden = True)

        #global ashley_role
        #TODO make most variables identical to Stephanie
        global ashley
        ashley = make_person(name = "Ashley", last_name =stephanie.last_name, age = 22, body_type = "standard_body", face_style = "Face_3",  tits="B", height = 0.92, hair_colour="brown", hair_style = ponytail, skin="white" , \
            eyes = "brown", personality = introvert_personality, name_color = "#228b22", dial_color = "228b22" , starting_wardrobe = ashley_wardrobe, \
            stat_array = [1,4,4], skill_array = [1,1,3,5,1], sex_array = [4,2,2,2], start_sluttiness = 7, start_obedience = -18, start_happiness = 119, start_love = 0, \
            title = "Ashley", possessive_title = "Your intern", mc_title = mc.name, relationship = "Single", kids = 0, force_random = True,
            forced_opinions = [["production work", 2, True], ["work uniforms", -1, False], ["flirting", 1, False], ["working", 1, False], ["the colour green", 2, False], ["pants", 1, False], ["the colour blue", -2, False], ["classical", 1, False]],
            forced_sexy_opinions = [["taking control", 2, False], ["getting head", 2, False], ["drinking cum", -2, False], ["giving blowjobs", -2, False], ["public sex", 2, False]])

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
        if mc.business.max_employee_count == mc.business.get_employee_count():
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
                if ashley.core_sluttiness >= 20:
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

    def add_ashley_hire_later_action():
        ashley_hire_directed = Action("Reconsider hiring Stephanie's sister", ashley_hire_directed_requirement, "ashley_hire_directed_label",
            menu_tooltip = "Talk to Stephanie about hiring her sister. She might be disappointed if you decide not to again...")
        mc.business.r_div.add_action(ashley_hire_directed)
        return

    def remove_ashley_hire_later_action():
        mc.business.r_div.remove_action("ashley_hire_directed_label")
        return

#Story labels
label ashley_intro_label():
    $ the_person = stephanie
    "You are deep in your work when a voice startles you from your concentration."
    the_person.char "Hey [the_person.mc_title]. Sorry to bug you, do you have a minute?"
    $ scene_manager = Scene()  #Clean Scene
    $ scene_manager.add_actor(the_person)
    mc.name "Of course. What can I do for you?"
    the_person.char "Well, I kind of need a favor."
    mc.name "Well, you've taken an awfully large risk coming to work for me here, so I suppose I owe you one."
    the_person.char "You see, it's my sister. She just graduated from college, but is having trouble finding work in her degree. She's had to move in with me because she can't find work!"
    the_person.char "She's really smart, but very introverted, it's been hard for her to get through interviews."
    mc.name "What is her degree in?"
    the_person.char "Errrmm... well, it's in Art History. Look, I know this isn't going to be her final career, but even just putting something down as an internship would really help her get a career started."
    the_person.char "I brought her resume, will you at least take a look at it? I think she would be great over in production."
    menu:
        "Take a look":
            pass
        "Not right now":
            mc.name "I'm sorry, I'm not hiring anyone like that right now. But if I change my mind I'll come find you, okay?"
            the_person.char "Of course, that's all I can ask, is that you will keep her in mind. Thanks!"
            $ add_ashley_hire_later_action()
            return
        "Blow me and I'll look" if the_person.sluttiness > 50:
            mc.name "I tell you what, why don't you come suck me off while I look over her documents."
            the_person.char "Oh! A favor for a favor then? Okay!"
            $ scene_manager.update_actor(the_person, position = "blowjob", emotion = "happy")
            "[the_person.possessive_title] gets on her knees and starts to undo your pants."
            the_person.char "You know I would do this anyway, right?"
            mc.name "Of course, but being reminded of your blowjob skills will probably help me make up my mind if I want to hire someone you're related to."
            call fuck_person(the_person, start_position = blowjob, skip_intro = False, position_locked = True) from _call_sex_description_ashley_intro_bonus_BJ_1
            $ the_report = _return
            $ scene_manager.update_actor(the_person, position = "stand4")
            if the_report.get("guy orgasms", 0) > 0:
                mc.name "God your mouth is amazing. If your sister sucks anything like you, this will be a no-brainer..."
                the_person.char "Hah! Well, to be honest, I don't think she really cares for giving blowjobs, but I guess you never know."
    "You pick up her documents and look over them."
    "From her skill set, it is obvious the best choice of department for her would be in production. The only question is, should you hire her or not?"
    call hire_select_process([ashley, 1]) from _call_hire_ashley_1
    $ the_person.draw_person()
    if _return == ashley:
        mc.name "I agree. She would be perfect for the production department. Would you pass along that she can start tomorrow? Or anytime in the next week."
        $ the_person.change_happiness(5)
        $ the_person.change_obedience(5)
        the_person.char "Oh! I didn't think you would say yes. This is great news! I'm sure she'll probably want to get started right away!"

        $ mc.business.hire_person(ashley, "Production")

        "You complete the necessary paperwork and hire [ashley.name], assigning her to the production department."
        "As you finish up, you notice [the_person.possessive_title] is already calling her sister with the news."
        $ scene_manager.update_actor(the_person, position = "walking_away")
        the_person.char "Hey Ash! Guess what? I got you a starting position at that place I've been..."
        "Her voice trails off as she leaves the room. You hope you made the right decision!"
        $ ashley.add_unique_on_talk_event(ashley_first_talk)
    else:
        mc.name "I'm sorry, I don't think she is a good fit at this time. But I will keep her in mind for the future, okay?"
        the_person.char "Ahhh, okay. I understand, but please let me know ASAP if you change your mind!"
        $ scene_manager.update_actor(the_person, position = "walking_away")
        "[the_person.possessive_title] gets up and leaves the room. Did you make the right decision? Oh well, if you change your mind, you can always talk to her again."
        $ add_ashley_hire_later_action
    return

label ashley_hire_directed_label():
    $ the_person = stephanie
    mc.name "I wanted to talk to you again about your sister."
    the_person.char "Oh? Have you decided to reconsider?"
    mc.name "I have. Do you still have her documents that I could look over them again?"
    the_person.char "Of course! Let me get them."
    "[the_person.possessive_title] runs over to her desk and comes back with a folder."
    the_person.char "Here you go!"
    "You pick up her documents and look over them."
    "From her skill set, it is obvious the best choice of department for here would be in production. The only question is, should you hire her or not?"
    call hire_select_process([ashley, 1]) from _call_hire_ashley_2
    $ the_person.draw_person()
    if _return == ashley:
        mc.name "I agree. She would be perfect for the production department. Would you pass along that she can start tomorrow? Or anytime in the next week."
        $ the_person.change_happiness(5)
        $ the_person.change_obedience(5)
        the_person.char "Oh! This is great news! I'm sure she'll probably want to get started right away!"
        $ remove_ashley_hire_later_action()
        $ mc.business.hire_person(ashley, "Production")

        "You complete the necessary paperwork and hire [ashley.name], assigning her to the production department."
        "As you finish up and start to leave, you notice [the_person.possessive_title] is already calling her sister with the news."
        $ scene_manager.update_actor(the_person, position = "walking_away")
        the_person.char "Hey Ash! Guess what? I got you a starting position at that place I've been..."
        "Her voice trails off as you leave the room. You hope you made the right decision!"
        $ ashley.add_unique_on_talk_event(ashley_first_talk)
    else:
        mc.name "I'm sorry, I don't think she is a good fit at this time. But I will keep her in mind for the future, okay?"
        the_person.char "Wow, really? Why did you even talk to me about this?"
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
    the_person.char "Oh!... hello sir. It's nice to meet you. I'm sorry, my sister said this place was all women..."
    mc.name "That's right. Except me, the owner."
    the_person.char "Ah... I see... Well, thank you for the opportunity. I appreciate the work."
    mc.name "Of course, [stephanie.title] is a good friend. Do you go by [the_person.name]? Or something else?"
    the_person.char "[the_person.title] is fine..."
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
    the_person.char "I know! I can't wait to go. All of my friends say it's so much fun..."
    "But as you enter the room, she notices, and immediately stops talking."
    $ the_person.draw_person()
    the_person.char "..."
    "Clearly she has no issue talking to her co-workers... why is she so quiet with you? Maybe you should ask her sister about it."
    $ stephanie.add_unique_on_talk_event(ashley_ask_sister_about_attitude)
    $ ashley.event_triggers_dict["excitement_overhear"] = True
    return

label ashley_ask_sister_about_attitude_label(the_person):
    "You approach [the_person.title], intent to ask her about her sister."
    mc.name "Hello [the_person.title]. Do you have a moment?"
    the_person.char "Of course sir. What can I do for you?"
    "You lower your voice. You don't necessarily need anyone overhearing you."
    mc.name "Well... I'm not sure how to say this but, I'm a little concerned about [ashley.title]."
    "A grimace forms on her face, but she waits for you to continue."
    mc.name "Earlier, I was walking by and I could hear her carrying on with her coworkers. But as soon as I entered the room, she went completely silent."
    "[the_person.title] nods her head as you keep going."
    mc.name "She barely says a word anytime I talk to her. I feel like I've gotten off to a bad start with her. Do you have any advice?"
    "[the_person.title] clears her throat."
    the_person.char "Well... [ashley.title] is a bit complicated. She has trouble talking to, and being around men in general..."
    mc.name "Oh? Oh! I see, I mean I guess that makes sense, not everyone is heterosexual..."
    the_person.char "Noooo, no. It isn't that. She's had boyfriends in the past. But something happened between her and her last boyfriend in college."
    the_person.char "They broke up all of a sudden, and she's never been the same way around men since then."
    mc.name "Hmm, that sounds like something bad might have happened."
    the_person.char "Yeah... honestly, I can't really talk about it."
    "[the_person.title] shakes her head, lost in thought."
    mc.name "Thank you for the insight. I appreciate it."
    the_person.char "Of course."
    $ ashley.add_unique_on_room_enter_event(ashley_room_warming_up)
    $ ashley.event_triggers_dict["attitude_discussed"] = True
    return

label ashley_room_warming_up_label(the_person):
    $ the_person = ashley # on_room_enter_event so the_person isn't defined
    $ the_person.draw_person(position = "standing_doggy")
    "As you step into the room, you can overhear [the_person.title] talking excitedly to another coworker."
    the_person.char "I know, I just need to find someone to go with!"
    "As you enter the room, she looks and stops talking."
    $ the_person.draw_person()
    the_person.char "Ahh... hello sir. Having a good day?"
    "Whoa. She actually said hi to you? Maybe she is warming up to you a little bit?"
    mc.name "It's been great so far. And you?"
    the_person.char "Oh... it's been good I guess..."
    mc.name "Glad to hear it."
    $ mc.business.add_mandatory_crisis(ashley_porn_video_discover)
    $ ashley.add_unique_on_room_enter_event(ashley_room_overhear_classical)
    return

label ashley_room_overhear_classical_label(the_person):
    $ the_person = ashley # on_room_enter_event so the_person isn't defined
    $ the_person.draw_person(position = "standing_doggy")
    "As you step into the room, you can overhear [the_person.title] talking excitedly to another coworker."
    the_person.char "I know, the city symphony is performing a collection of Johannes Brahms' symphonies. I want to go so bad, but I can't find anyone to go with..."
    "As you enter the room, she looks and stops talking."
    $ the_person.draw_person()
    the_person.char "Ahh... hello sir. Having a good day?"
    "She has been slowly warming up to you over the last few weeks."
    mc.name "It's been great so far. And you?"
    the_person.char "Oh, I've been good. Thanks for asking."
    mc.name "Glad to hear it."
    "Hmm... she is looking for someone to go with her to a classical music concert. Maybe that person could be you?"
    $ ashley.event_triggers_dict["concert_overheard"] = True
    return

label ashley_ask_date_classic_concert_label(the_person):
    mc.name "So... I couldn't help hearing earlier, you are looking to go to the Brahms symphony recital, but you don't have anyone to go with?"
    the_person.char "Ummm yeah, something like that..."
    "She is looking down, avoiding eye contact with you."
    mc.name "That sounds like a great cultural event. I was wondering if you would be willing to let me take you?"
    "She is caught off guard. She wasn't expecting you to ask something like this!"
    the_person.char "Oh! I uhh, I'm not sure..."
    if stephanie.love > 30 or stephanie.obedience > 130:
        the_person.char "I suppose... I mean... Steph keeps telling me you are a nice guy..."
    else:
        the_person.char "I don't know, I mean you seem like a nice guy but..."
        mc.name "I'll tell you what. We could let [stephanie.title] know when it is. She could drop you off and pick you up afterwards."
        "[the_person.title] mumbles something for a second, then relents."
        the_person.char "I suppose... I mean... Steph keeps telling me I need to go out more."
    mc.name "Ah, great! Do you know when the concert is?"
    the_person.char "It's on Thursday night."
    mc.name "Ok. I'll plan to meet you there on Thursday night then?"
    the_person.char "Okay, if you're sure about this..."
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
    # ashley is wearing something nice
    $ the_person.apply_outfit(the_person.decide_on_outfit(sluttiness_modifier = 0.2))
    "Soon, you see the sisters."
    $ scene_manager.add_actor (the_person, position = "stand4", emotion = "happy")
    $ scene_manager.add_actor(stephanie, display_transform = character_center_flipped)
    stephanie.char "Oh hey, there's [stephanie.mc_title]. Don't worry, I'm sure everything will be great."
    the_person.char "I know, I know... are you sure you don't want to go?"
    stephanie.char "Don't be silly, you've only got two tickets. You two will have a blast!"
    the_person.char "Okay..."
    "You walk over and greet the pair."
    #TODO when making story branch, use this first conversation to begin setting up paths. For now, love path only.
    #love: compliment ash. neutral: compliment both. corrupt: crude compliment
    mc.name "Hello! Thanks for this, I've been looking forward to this ever since we arranged it. [the_person.title], you look great tonight!"
    the_person.char "Ah... thank you."
    $ the_person.change_happiness(1)
    $ the_person.change_love(1)
    "[stephanie.title] gives you a smile after your kind words to her sister."
    $ stephanie.change_obedience(1)
    $ stephanie.change_love(1)
    #End of love option
    stephanie.char "Alright you two, go enjoy your classical concert. Ash, just text me when you get done, I'm gonna go have a couple drinks."
    the_person.char "Okay. Bye Steph!"
    $ scene_manager.remove_actor(stephanie)
    mc.name "Shall we?"
    #TODO find concert hall background image to change to.
    "You step into the concert hall, show your tickets, and make you way to your seats."
    $ scene_manager.update_actor(the_person, position = "sitting")
    "You have a few minutes before the concert starts, so you try making some small talk."
    mc.name "So, have you ever been to a concert like this before?"
    the_person.char "Oh, a few times, when I was in college, but not for over a year."
    mc.name "I'll admit it, this is my first time going to something like this. I'm really excited to have the chance to try something new, though."
    the_person.char "Oh yeah? I think most guys find classical music a bit boring..."
    #TODO next path branch. different responses. love: glad to be here with you. neutral: glad to be here to watch. corrupt: just here to be with sexy girl
    mc.name "I'll admit I'm not an avid follower, but I think experiencing a variety of cultural events is an important thing for someone to do."
    the_person.char "Yeah, that's very insightful."
    mc.name "Plus, I'm glad to be able to spend some time with you and get to know you better."
    "You notice her blush a bit, but you can also see her smile."
    $ the_person.change_stats(love = 2, happiness = 2)
    #end branch
    "Soon, the lights dim, and the music begins. It begins with a splendid piano melody."
    "You and [the_person.possessive_title] sit together silently, enjoying the music."
    "It goes through emotional highs and lows. At one point, you look over and you think you see a tear on [the_person.title]'s cheek."
    #TODO next path branch. hold hand (love), put arm around (neutral), or put hand on leg(corrupt)
    "You reach down and take her hand. She jumps at the contact, but quickly takes your hand in hers as the music reaches an especially poignant moment."
    $ the_person.change_stats(love = 5, happiness = 5)
    "You hold hands for the duration of the concert. You both share comments now and then about specific parts that you liked."
    "When the concert is over, the lights slowly come back on. You let go of her hand as you both start to get up."
    $ scene_manager.update_actor(the_person, position = "stand3")
    "You slowly file out of the concert hall, chatting about the concert."
    #TODO change to downtown background
    $ mc.change_location(downtown)
    $ mc.location.show_background()
    "When you get outside, [the_person.title] looks around."
    the_person.char "Oh! I was supposed to text Steph. I was having fun and totally forgot!"
    "She pulls out her phone and texts her sister."
    the_person.char "Okay, she says she'll be right over... You don't have to stay, I'm sure she won't be long."
    mc.name "And leave a pretty girl like you all by herself? Not a chance."
    $ the_person.change_stats(love = 2, happiness = 2)
    "She smiles, looking down at her feet."
    mc.name "So was it everything you hoped it would be?"
    "She thinks about it before responding. One of the things you appreciate about [the_person.title] is that she always thinks before she speaks."
    the_person.char "It was, and more. I really had a good time tonight."
    mc.name "Great! If you hear about another orchestra in town, I'd love to go again."
    the_person.char "I haven't heard anything, but I'll definitely keep it in mind. I'd like to do this again."
    $ scene_manager.add_actor(stephanie, display_transform = character_center_flipped)
    stephanie.char "Hey Ash! Hey [stephanie.mc_title]! How'd it go?"
    the_person.char "Steph! We had a great time. The performers were amazing..."
    stephanie.char "And I assume you were a perfect gentleman?"
    "[stephanie.title] gives you a look. She smiles, but you can tell she is genuinely protective of [the_person.title]."
    mc.name "As always, [stephanie.title]."
    the_person.char "He really was. Thanks again [the_person.mc_title]!"
    "It's late, so you all agree to part ways."
    mc.name "Alright, don't forget work tomorrow. I'll see you both then."
    the_person.char "Bye!"
    stephanie.char "See ya then!"
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
    "There's a guy and a girl, who you immediately recognize as [the_person.title]. This looks like one of those hidden camera type videos."
    "The guy is tied up, with his four limbs tied to the four corners of a bed. You watch as [the_person.title] gets up on the bed and crawls on top of him."
    $ scene_manager.update_actor(the_person, position = "doggy")
    "She turns and puts her ass right in his face. She starts to ride his face roughly."
    "[the_person.possessive_title] strokes the guy a little bit, but basically ignores his cock as she rides his face."
    "She does this for several minutes, until she starts to moan and really ride the guy roughly. Her moans get loud, sounds like she is finishing."
    $ scene_manager.update_actor(the_person, position = "cowgirl")
    "She turns around and puts a condom on the guy. She starts to tease him."
    the_person.char "You want this in my pussy, bitch? Yeah right... like you deserve that."
    "Wow, she is definitely nailing the whole dominatrix role..."
    "She starts to dry hump the poor guy. With his limbs down at his sides, there's not much he can really do."
    "She keeps going, speeding up and slowing down multiple times."
    "Eventually, you can hear the guy starting to moan, it's clear he is getting ready to cum."
    "She quickly hops off. The guy fills up the condom while [the_person.title] basically ignores him."
    the_person.char "Pathetic... maybe someday I'll let you touch me... but not today, that's for sure!"
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
    the_person.char "Of course."
    $ ceo_office.show_background()
    "You enter your office an gesture for her to sit down."
    $ scene_manager.update_actor(the_person, position = "sitting")
    if the_person.sluttiness > 50:
        "As she sits down, you notice [the_person.possessive_title]'s posture. She is sticking her chest out. She probably thinks you brought her to your office for some... personal time."
    mc.name "I wanted to talk to you again, about your sister, [ashley.title]."
    the_person.char "Oh!... right..."
    if the_person.sluttiness > 50:
        "Her back slumps noticeably when you say that."
    mc.name "This is not going to be an easy or pleasant conversation, but uhh, I found a video of your sister..."
    the_person.char "UGH! I thought we got that deleted from everywhere."
    mc.name "Oh... deleted?"
    $ scene_manager.update_actor (the_person, emotion = "sad")
    the_person.char "Yeah, she had this boyfriend a while back. It came out after they broke up that he was secretly filming them having sex and posting it online..."
    the_person.char "We did everything we could to shut it down once we found out, but the internet is crazy. Once it's out there, it's out there!"
    mc.name "Wow, I feel awful, I had no idea."
    the_person.char "Yeah. Unfortunately, having that happen really got to her. That was like, over a year ago? And she hasn't been out with anyone since."
    the_person.char "As you probably saw... she was pretty... adventurous... with guys."
    the_person.char "But now it's almost like she can't trust any guys anymore."
    "You both look at each other for a moment, considering the circumstance."
    mc.name "I want to do something, but I don't know what."
    if the_person.love > 30:
        the_person.char "I don't know either... I guess just... keep being you?"
        the_person.char "You are a wonderful guy. Just be there for her, okay? You are, like, the only guy she interacts with any more."
    else:
        the_person.char "I mean, you are, like, the only guy she interacts with... at all. She has completely cut herself off from men."
        the_person.char "Maybe you could try, like, you know, being there for her? Help her learn that not all men are total assholes?"
    mc.name "I suppose. Anything specific?"
    the_person.char "Honestly? I'm not really sure. Ash moving back in with me only just happened, and we didn't really see each other much while going through college."
    "After a few solemn moments, you decide to move on with your day."
    mc.name "That's enough for now I suppose. Let me know if you think of anything."
    the_person.char "Yes sir... and the same for you."
    "You both walk back to the [mc.location.formalName]."
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
    the_person.char "Oh... sure..."
    $ ceo_office.show_background()
    "[the_person.possessive_title] follows you to your office. After you enter, you close the door behind you."
    mc.name "Go ahead and have a seat."
    $ scene_manager.update_actor(the_person, position = "sitting", emotion = "sad")
    "You can tell she looks a little scared."
    mc.name "Are you okay?"
    the_person.char "I'm sorry sir... I'm working hard..."
    "What? She thinks you brought her here to discipline her?"
    #TODO Choice list
    mc.name "I didn't call you here to discipline you."
    $ scene_manager.update_actor(the_person, position = "sitting", emotion = "happy")
    "She looks visibly relieved."
    the_person.char "Oh... you're not? Then... what did you want me here for?"
    "You clear your throat. You are going to have to phrase this very carefully."
    mc.name "Well, I had a great time at the concert the other night, and honestly I've gotten very fond of you..."
    "[the_person.title] smiles and blushes a bit. She is so shy, but so cute when she does that."
    mc.name "So, before I move on, I just want you to know that I want to support you and help you in any way that I can."
    "Her face changes to a look of confusion."
    the_person.char "Help with what?"
    mc.name "I'm sorry, this is a difficult topic but... I was watching some pornography before I went to bed not long ago..."
    "The look on her face changes to pure horror."
    mc.name "I... was rather shocked to see a familiar face..."
    "She begins to stutter out a response."
    the_person.char "That... that wasn't... I'm sorry sir that..."
    mc.name "Sorry? [the_person.title] you don't need to apologize."
    the_person.char "I'm... huh? I don't?"
    mc.name "Of course not, it definitely looked like you were being filmed without your knowledge."
    the_person.char "Yeah... I had no idea... but what happened in the vid..."
    mc.name "It was between two consenting adults. Other than the recording anyway. It's okay."
    the_person.char "You aren't... grossed out by it?"
    mc.name "Grossed out? Why would I be grossed out?"
    the_person.char "I mean... the relationship I had with my last boyfriend was... not normal."
    mc.name "Hey, everyone has kinks. I'm not here to kink-shame you."
    mc.name "I just wanted to tell you, I'm sorry about what happened. If you need any assistance going forward, please don't hesitate. I want to help if I can."
    the_person.char "Well... Steph and I... We worked hard to get that video off the internet. But once it's out there, it's out there, I guess."
    "She looks down and thinks for a bit."
    the_person.char "The, umm... the video. Did you watch the whole thing?"
    mc.name "Yeah... yeah I did."
    "She looks a little sheepish, but continues."
    the_person.char "Did... you know... you like it?"
    "Wow, the conversation appears to be turning quickly."
    mc.name "I did. You're very sexy."
    "She gets a wide smile on her face."
    the_person.char "I'll admit it... I kind of like it... when guys let me take over a little bit..."
    $ the_person.discover_opinion("taking control")
    "Good to know for certain, but this was fairly obvious at this point."
    mc.name "A little bit?"
    "She chuckles."
    the_person.char "You've been so nice to me... Can I return the favor?"
    mc.name "You don't need to do that..."
    the_person.char "Oh, but I want to..."
    "She leans closer to you and whispers."
    the_person.char "I really want to... I want to make you feel good..."
    $ mc.change_arousal(30)
    "DAMN. You feel your pants get a little tight after that. You remember from the video the way [the_person.title] took control and rode her ex..."
    mc.name "I mean, you don't have to do that..."
    $ scene_manager.update_actor(the_person, position = "stand4")
    "She gets up and walks around your desk. You stand up too."
    the_person.char "It's okay. I'm going to. You just enjoy."
    "With nothing else to say, [the_person.possessive_title] reaches down and begins to stroke your cock through your pants."
    the_person.char "Mmmm, I can tell you want it too!"
    "[the_person.title] has some skilled hands... You close your eyes and enjoy her stroking you for a moment."
    $ mc.change_arousal(10)
    "You hear a zipper some fabric rustle for a moment, then suddenly feel her warm hand on your dick, skin to skin. You look down and see her pulling your dick out."
    if the_person.has_taboo("touching_penis"):
        the_person.char "Oh my god... it's so big... You've been hiding this from me, [the_person.mc_title]?"
        "She gives you a couple eager strokes. You can only moan in response. It feels good to finally feel her hands on you."
        $ the_person.break_taboo("touching_penis")
        $ mc.change_arousal(15)
    else:
        the_person.char "God, it's so big. I love getting your cock out..."
        "She gives you a couple eager strokes. You can only moan in response."
        $ mc.change_arousal(10)
    "She looks into your eyes as she continues to give you a handjob."
    the_person.char "Alright, don't hold back now."
    call get_fucked(the_person, start_position = handjob, private = True, skip_intro = True, allow_continue = False) from _ashley_first_handjob_01
    $ scene_manager.update_actor(the_person, position = "stand3")
    $ the_report = _return
    if the_report.get("guy orgasms", 0) > 0:
        "You stand there with your eyes closed, slowly recovering. When you open them, you survey the mess you made."
    else:
        "You haven't finished, but [the_person.title] is still standing there with your dick in her hand."
    "Suddenly you hear your office doorknob click and the door start to open. You forgot to lock it!"
    $ scene_manager.add_actor(stephanie, display_transform = character_left_flipped)
    stephanie.char "Hey [stephanie.mc_title] sorry to bug you but... oh fuck!"
    "It doesn't take [stephanie.title] long to survey the situation."
    stephanie.char "Holy shit, Ash! I didn't mean... I forgot to knock! Oh fuck!"
    $ scene_manager.update_actor(stephanie, position = "walking_away")
    "[stephanie.possessive_title] turns to flee the room."
    the_person.char "Oh my god... Steph this isn't what you think..."
    $ scene_manager.remove_actor(stephanie)
    "[stephanie.title] slams the door as she leaves the room."
    the_person.char "Oh no... oh god, how am I going to explain this?..."
    the_person.char "I'm sorry [the_person.mc_title]. I have to go!"
    "[the_person.title] quickly rushes to leave. You've barely had time to process everything that just happened."
    mc.name "[the_person.title]..."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    the_person.char "Don't say anything... I just need to go..."
    $ scene_manager.remove_actor(the_person)
    "[the_person.possessive_title] quickly leaves the room."
    "Welp, you just got a handjob from [the_person.title]... and then her sister promptly walked in and witnessed the whole thing."
    "You'll have to consider how to approach both girls carefully before you talk to them next."
    "You walk back to the [mc.location.formalName]."
    $ ashley.event_triggers_dict["porn_convo_avail"] = False
    $ mc.location.show_background()
    $ scene_manager.clear_scene()
    $ ashley.add_unique_on_talk_event(ashley_post_handjob_convo)
    jump game_loop # she runs after her sister so end talk with Ashley

label ashley_post_handjob_convo_label(the_person):
    $ mod_alpha_content_warning(ashley_sisterly_jealousy_feature)
    $ show_wip_screen(ashley_sisterly_jealousy_feature)
    "You decide not to give [the_person.title] too much time to overthink what happened in your office. You swing by her desk."
    $ the_person.draw_person()
    mc.name "Hey [the_person.title]..."
    the_person.char "Oh... haha, yeah, I figured something like this was coming... it's okay, I'll clean out my desk and be out before you know it..."
    mc.name "Clean out your desk? I'm not firing you. Come on let's go get some coffee."
    the_person.char "Oh, coffee? OK, I'm right behind you..."
    "[the_person.possessive_title] is blushing hard. It's kind of cute actually."
    $ downtown.show_background()
    "As you step out of the office building, [the_person.title] is following along behind you. You give her a second to catch up so you can walk side by side."
    "She's looking down at her feet. She's so shy, you can tell she is uncomfortable."
    menu:
        "Hold her hand" if the_person.love >= 20:
            mc.name "Don't worry, [the_person.title]. I just wanted to get out of the office to chat about things. Also to limit the possibility of an interruption..."
            "You reach your hand down and take her hand in yours. It startles her a little, but she quickly looks up at you."
            mc.name "I've really been enjoying spending time with you."
            the_person.char "Oh... that's... nice to hear. Thank you."
            $ the_person.change_stats(love = 5, happiness = 5, obedience = 5)
        "Hold her hand \n{color=#ff0000}{size=18}Requires 20 Love{/size}{/color} (disabled)" if the_person.love < 20:
            pass
        "Reassure her":
            mc.name "Don't worry, [the_person.title]. I know we both need a chance to think about things, and I always find that coffee helps me think."
            the_person.char "Yeah... I suppose a coffee would be good for that..."
            $ the_person.change_stats(obedience = 10)
        "Tell her it was hot" if the_person.sluttiness >= 20:
            mc.name "Don't worry, [the_person.title]. I had a great time at the concert... and what happened in my office was fucking hot..."
            "[the_person.possessive_title] looks up at you, a bit surprised by your comment."
            the_person.char "Oh... I'm glad you think so..."
            $ the_person.change_stats(obedience = 5, slut_temp = 3, slut_core = 3)
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
        the_person.char "Well... I mean... we're sisters, so we talk about everything. Ever since you started the business up, she's been talking about you, almost non-stop..."
        the_person.char "She definitely has a thing for you... it would be wrong for me to let you pursue anything further with me..."
        mc.name "I understand that, but isn't what I want important too? I've known Stephanie for years, but I've only just recently met you."
        the_person.char "I... I guess..."
    elif ashley_steph_relationship_status() == "ashley":
        the_person.char "Yeah... I mean, I guess this whole thing has just happened really fast, but I would be lying if I said it wasn't exciting me."
        the_person.char "I'm just not sure what to tell Steph... she means the world to me, and I feel like she might've sort of had a thing for you, but I'm not sure."
        mc.name "Yeah, that is something to consider."
    else:
        the_person.char "Honestly... I'm just really confused right now. Steph and I... we're sisters! She means the world to me and we talk about everything!"
        the_person.char "Ever since you started this business thing up, she's been talking about you non-stop. I can tell she really likes you..."
        the_person.char "But... I know we only just met... but I... errm..."
        mc.name "Yes?"
        "She sighs"
        the_person.char "I guess... I kinda like you too..."
        the_person.char "I know this is kinda weird but... I guess you'll just have to like... decide? Who do you want to be with more?"
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
            $ the_person.special_role.append(girlfriend_role)
        "Let's keep us secret \n{color=#ff0000}{size=18}Corruption path{/size}{/color}" if (ashley_steph_relationship_status() == "stephanie" or ashley.sluttiness > 30):
            mc.name "I think I know what to do, where we can all be happy."
            the_person.char "Oh?"
            mc.name "Alright, let me explain the whole thing before you make up your mind. What if we keep things between us strictly physical, and don't tell [stephanie.title]?"
            the_person.char "Errrm... you want to do what now?"
            $ the_person.change_stats(love = -5, happiness = -5, obedience = 5)
            mc.name "Look, [stephanie.title] was the one in the first place that told me to ask you out. She wants you to be happy, and I think she knows you're going through a dry spell."
            mc.name "I'll help take care of your physical needs... then if you happen to find another guy or if things with your sister don't work out..."
            the_person.char "I don't know... I'm not sure I'll be able to lie to her about this..."
            mc.name "You don't have to lie about it, just don't talk about it. It'll be just like friends with benefits... but just between you and me."
            "She is struggling with the idea a bit, but finally makes up her mind."
            the_person.char "I guess we could try... but if it gets weird, I'm out, okay?"
            mc.name "Okay."
            the_person.char "And you have to go talk to her about what happened... you know... in your office..."
            mc.name "I'm sure I can handle that."
            "She bites her lip."
            the_person.char "Okay... let's give it a shot."
            $ the_person.event_triggers_dict["story_path"] = "secret"
            $ assign_jealous_sister_role(the_person)
        "I want to be friends with both of you \n{color=#ff0000}{size=18}Friends with benefits path \n Not yet written{/size}{/color}" if (ashley_steph_relationship_status() == "both" or mc.charisma > 4):
            mc.name "There are a lot of feelings going on right now, but I think we all need to calm down a bit."
            mc.name "[stephanie.title] and I go back a ways, but I just think of her as a friend."
            mc.name "I'm not going to lie, I really enjoy the way things are developing between us... but I have to be honest. I'm not looking to get tied down right now."
            the_person "Ahh... I see..."
            mc.name "I understand though, that everyone has needs. If you want need some help relieving sexual tension, I'd be glad to help you out whenever you need it."
            "[the_person.title] looks confused for a moment."
            the_person "You mean... you want to be friends... with benefits?"
            mc.name "Exactly."
            the_person "Wow... I mean... I guess that would be okay..."
            $ the_person.event_triggers_dict["story_path"] = "fwb"
            the_person "I don't... I'm not sure how to talk to Steph about this though..."
            mc.name "Don't worry, I'll talk to her."
    "You drink your coffee with [the_person.title]. You are happy you were able to come up with a solution."
    the_person "This place is nice... maybe I should bring steph here some time..."
    "Eventually you finish up. You decide to head back to the office."
    mc.name "I'm going to head back, feel free to to take the rest of the day off if you need to."
    the_person "Ahh, thank you..."
    $ mc.location.show_background()
    $ stephanie.add_unique_on_talk_event(ashley_stephanie_arrange_relationship)
    $ hide_wip_screen()
    call advance_time from _call_advance_ashley_post_hj_01
    return

label ashley_stephanie_arrange_relationship_label(the_person):
    $ mod_alpha_content_warning(ashley_sisterly_jealousy_feature)
    $ show_wip_screen(ashley_sisterly_jealousy_feature)
    "It's time talk to [the_person.title]. You approach her in the lab."
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
            "I'm sorry for what happened. It won't happen again."
        else:
            the_person "I... I don't understand... Why aren't you interested in Ashley?"
            mc.name "It isn't that I'm not interested, as much as that I'm currently interested in someone else..."
            "You give [the_person.title] a wink. When she realizes what you mean, she blushes."
            the_person "Oh wow, I didn't realize that you felt the same way... Oh [the_person.mc_title]... Can we just make it official? I want everyone to know that I'm your girlfriend!"
            "Realizing that your plan to keep things secret with [ashley.title] isn't going to work unless you take things further with [the_person.title], you agree."
            mc.name "Here, let me do this, officially. [the_person.title], will you be my girlfriend?"
            the_person "Yes! Oh yay! I thought for sure you were gonna get with Ashley... I was so jealous... When I saw..."
            $ the_person.special_role.append(girlfriend_role)
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
            "We're all adults here. She knows that if she finds someone else there's no commitment. And she knows it's the same for me, if I were to happen to start dating someone."
        else:
            "It's nothing different than what has been going on between us. Don't worry, I know you have needs too."
        the_person "That's understandable. I mean, I get it, what is going on, it just surprises me."
        the_person "It might be a little weird... you know? Getting physical with a guy who is doing the same with my sister... but you're right. We're all adults here, getting what we want from each other, consensually."
        $ the_person.draw_person(position = "stand2")
        the_person "Alright. I'm glad we got to talk about it. It makes me feel better, knowing what is going on between you two. I think I'll get back to work."
        "[the_person.possessive_title] turns and walks out of your office. Both girls are sexy, and you feel like your prospects are better if you can keep them from competing with each other for your attention."
    else:
        mc.name "I honestly was not expecting this to happen so quickly either. We went on that date, and had a great time"
        mc.name "We started with just chatting, but it was like we couldn't keep our hands off each other... And then you walked in..."
        if the_person.love > 50:
            "[the_person.title] is looking down, not making eye contact. You know she has feelings for you also, and is struggling with your new found affection for her sister."
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
    $ hide_wip_screen()
    $ stephanie.set_alt_schedule(downtown, days = [6], times = [0])
    $ ashley.set_alt_schedule(downtown, days = [6], times = [0])
    $ ashley.add_unique_on_room_enter_event(ashley_stephanie_saturday_coffee_intro)
    call advance_time from _call_advance_ashley_arrangement_01
    return

label ashley_stephanie_saturday_coffee_intro_label(the_person):
    $ mod_alpha_content_warning(ashley_sisterly_jealousy_feature)
    $ show_wip_screen(ashley_sisterly_jealousy_feature)
    $ the_person_one = the_person
    $ the_person_two = stephanie
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person_one, display_transform = character_center_flipped, position = "sitting")
    $ scene_manager.add_actor(the_person_two, position = "sitting")
    "As you are walking downtown, you pass by the coffee shop. Looking inside, you are surprised to see Ashley and Stephanie sitting inside."
    "You decide to step inside and say hello."
    mc.name "Hey girls, good to see you."
    "They are surprised to see you. Ashley blushes and looks down at her coffee as Stephanie responds."
    the_person_two.char "Hey boss! Me and Ash are just having a cup of coffee before we go our separate ways. It's kind of become our little tradition every Sunday morning, since she moved in with me."
    "She looks over at her sister and starts to tease her. "
    the_person_two.char "I think she said something about hitting up the gym today... I think there's a guy she's trying to impress!"
    the_person_one.char "Oh my gosh Steph, stop it!"
    "[the_person_one.title] is blushing, and once in a while sneaks a peak up at you. Even though you've already discussed with her how you want things to be with her, it is cute to see her squirm a little."
    mc.name "Is that true [the_person_one.title]? Who might this lucky guy be?"
    the_person_one.char "Ah. Errm... Well..."
    "She's sputtering out unintelligible mumbles."
    the_person_two.char "Don't worry Ash. I'm sure whoever it is will appreciate you putting in the time to keep your body fit!"
    "[the_person_one.possessive_title] is relieved when her sister intervenes and changes the subject."
    the_person_two.char "Hey, why don't you grab a coffee and join us? It's kind of nice to hang out in a non-work environment."
    mc.name "Oh, I wouldn't want to interrupt you two having some family time together..."
    "Surprisingly, it's [the_person_one.title] that interrupts you."
    the_person_one.char "It's fine! We live together, remember?"
    "You raise an eyebrow. It's not often that she speaks up, but clearly [the_person_one.title] wants you to hang out too. Suddenly, she realizes she is speaking up and quiets down."
    the_person_one.char "I mean... It would be okay, right? We don't mind at all..."
    mc.name "Okay. Just give me a moment and I'll get something. Either of you two want something while I'm in line?"
    "The sisters look at each other. [the_person_one.title] shakes her head and [the_person_two.possessive_title] responds."
    the_person_two.char "No thanks! We're good for now, but maybe another time we'll let you buy us coffees!"
    "You excuse yourself and head up to the counter. You glance back at the two sisters as you wait in line."
    "It's amazing how similar the girls are, but still so different. [the_person_one.title] is so quiet and shy, but sometimes when you talk with her you can see glimpses of the fiery passions that drive [the_person_two.title]."
    "You order your coffee, and soon the hot brew is in your hand. As you walk back to the table, you decide to use the opportunity to try and get to know them both a little better."
    "The sisters are sitting opposite to each other at the booth... Who should you sit next to?"
    menu:
        "[the_person_one.title]" if not ashley_is_secret_path():    #Depending on previous choices, MC may have to sit next to a particular girl.
            "[the_person_one.possessive_title] scoots over to give you room to sit next to her. She sneaks a peek at you and you see a slight smile on her lips."
            $ scene_manager.update_actor(the_person_two, display_transform = character_right(yoffset = -.125, zoom = 0.75))
            $ scene_manager.update_actor(the_person_one, display_transform = character_center_flipped(yoffset = .125, zoom = 1.25))
            $ the_person_one.change_stats(love = 3, happiness = 5)
            $ ashley_set_coffee_partner(the_person_one)
        "[the_person_two.title]" if not ashley_is_normal_path():
            "[the_person_two.possessive_title] scoots over so you have room to sit next to her."
            the_person_two.char "Have a seat, [the_person_two.mc_title]."
            $ scene_manager.update_actor(the_person_two, display_transform = character_right(yoffset = .125, zoom = 1.25)) #TODO this is broken and I don't know why
            $ scene_manager.update_actor(the_person_one, display_transform = character_center_flipped(yoffset = -.125, zoom = .75))
            "She pats the seat next to her. You sit down and see her smirking at you before she keeps talking to her sister."
            $ the_person_two.change_stats(love = 3, happiness = 5)
            $ ashley_set_coffee_partner(the_person_two)
    "You listen to the two sisters chat for a bit as you enjoy your coffee. [the_person_one.title] seems to almost forget you are at the table, and you get a glimpse into her personality as she talks with her older sibling."
    $ overhear_topic = the_person_one.get_random_opinion(include_sexy = False)
    $ text_one = person_opinion_to_string(the_person_one, overhear_topic)[1]
    $ text_two = get_topic_text(overhear_topic)
    the_person_one.char "... but yeah, I have to say I [text_one] [text_two]"
    if the_person_one.discover_opinion(overhear_topic):
        "Oh! You didn't realize that [the_person_one.title] felt that way."
    "The sisters discuss it for a bit. You kind of zone out for a little bit as the conversation changes to clothing. The girls are discussing some different brands..."
    "Suddenly the girls stop talking. You look up and notice they are both looking out the window. A woman is walking by the coffee shop window out in the street."
    "TODO: Starbuck hasn't figured out how to code this yet. A third woman appears, walking by the window."
    the_person_two.char "Wow, what an outfit!"
    "[the_person_two.title] gushes. [Dialogue specific if she likes the color or not][second dialogue if she likes the type of outfit]"
    "[the_person_one.title] makes a similar comment."
    the_person_two.char "What do you think? Sometimes it's easy to fall into the trap of just wearing what is comfortable. Do you think we would look good in a [outfit description]?"
    menu:
        "Yes":
            pass
        "No":
            pass
    "[the_person_one.possessive_title] listens to your response intently. You can tell she is interested in your opinion."
    the_person_two.char "Well, I'd better get going. I've got some errands to run!"
    "You stand up and both girls also get up."
    mc.name "Thank you for the pleasant morning. You two have a good day."
    the_person_two.char "You bet boss! We do this pretty much every Sunday. Feel free to join us!"
    "[the_person_two.possessive_title]'s invitation is tempting. [the_person_one.title] is smiling at you, clearly mirroring her sisters invitation to join again."
    the_person_two.char "Next week you're buying the coffees though!"
    mc.name "That's acceptable. With us all being employees, I'll just put it down as a company expense."
    "You say your goodbyes and go separate ways. This could be an interesting opportunity in the future to learn more about about the sisters."
    $ hide_wip_screen()
    $ the_person_one.add_unique_on_room_enter_event(ashley_stephanie_saturday_coffee_recur)
    $ ashley_reset_coffee_partner()
    call advance_time from _call_advance_ashley_coffee_advance_01

    python:
        scene_manager.clear_scene()
        del the_person_one
        del the_person_two
    return

label ashley_stephanie_saturday_coffee_recur_label(the_person_one):
    $ mod_alpha_content_warning(ashley_sisterly_jealousy_feature)
    $ show_wip_screen(ashley_sisterly_jealousy_feature)
    $ the_person_two = stephanie
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person_one, display_transform = character_center_flipped, position = "sitting")
    $ scene_manager.add_actor(the_person_two, position = "sitting")
    "You swing by the coffee shop. Right on time, you see [the_person_one.title] and [the_person_two.title] in a booth. You walk over to the table."
    mc.name "Good morning! Whose up for coffee?"
    the_person_two "Good morning [the_person_two.mc_title]! That would be great! Can I get an Americano with two creams?"
    the_person_one "Good morning. I like mine black..."
    if the_person_two.sluttiness > 20:
        the_person_two "That's what she said!"
        "The girls are laughing at [the_person_two.possessive_title]'s joke as you head up to the counter and order the coffees."
    "TODO: add serums to coffees here"
    $ mc.business.funds -= 15
    if the_person_one.is_girlfriend():
        "As you wait for your coffees to get made, you spot a yummy looking blueberry muffin. You decide to get it to share with [the_person_one.title]"
        $ mc.business.funds -= 5
    elif the_person_two.is_girlfriend():
        "As you wait for your coffees to get made, you spot a yummy looking blueberry muffin. You decide to get it to share with [the_person_two.title]"
        $ mc.business.funds -= 5
    "You walk back to the table and give the girls their coffee."
    if the_person_one.is_girlfriend():
        the_person_one "Ohh, that looks good..."
        "[the_person_one.possessive_title] spots your muffin. You slide into the booth next to her."
        $ scene_manager.update_actor(the_person_two, display_transform = character_right(yoffset = -.125, zoom = 0.75))
        $ scene_manager.update_actor(the_person_one, display_transform = character_center_flipped(yoffset = .125, zoom = 1.25))
        mc.name "Got it for us to share."
        "You glance over at [the_person_two.title]. A hint of jealousy crosses her face, but she quickly hides it."
        $ ashley_set_coffee_partner(the_person_one)
    elif the_person_two.is_girlfriend():
        the_person_two "Ohh! Yum, that looks tasty [the_person_two.mc_title]"
        "[the_person_two.possessive_title] spots your muffin. You slide into the booth next to her."
        $ scene_manager.update_actor(the_person_two, display_transform = character_right(yoffset = .125, zoom = 1.25))
        $ scene_manager.update_actor(the_person_one, display_transform = character_center_flipped(yoffset = -.125, zoom = 0.75))
        mc.name "Got it for us to share."
        "You glance over at [the_person_one.title]. A hint of jealousy crosses her face, but she quickly hides it."
        $ ashley_set_coffee_partner(the_person_two)
    else:
        "The sisters are sitting opposite to each other at the booth... Who should you sit next to?"
        menu:
            "[the_person_one.title]":    #Depending on previous choices, MC may have to sit next to a particular girl.
                "[the_person_one.possessive_title] scoots over to give you room to sit next to her. She sneaks a peek at you and you see a slight smile on her lips."
                $ scene_manager.update_actor(the_person_two, display_transform = character_right(yoffset = -.125, zoom = 0.75))
                $ scene_manager.update_actor(the_person_one, display_transform = character_center_flipped(yoffset = .125, zoom = 1.25))
                $ the_person_one.change_stats(love = 3, happiness = 5)
                $ ashley_set_coffee_partner(the_person_one)
            "[the_person_two.title]":
                "[the_person_two.possessive_title] scoots over so you have room to sit next to her."
                the_person_two.char "Have a seat, [the_person_two.mc_title]."
                $ scene_manager.update_actor(the_person_two, display_transform = character_right(yoffset = .125, zoom = 1.25))
                $ scene_manager.update_actor(the_person_one, display_transform = character_center_flipped(yoffset = -.125, zoom = 0.75))
                "She pats the seat next to her. You sit down and see her smirking at you before she keeps talking to her sister."
                $ the_person_two.change_stats(love = 3, happiness = 5)
                $ ashley_set_coffee_partner(the_person_two)
    "As you sit down, the girls are sharing their plans for the weekend. You take a few sips of your coffee enjoying the flavor."

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
    the_person_two "Hey, you know where to find us next week!"
    the_person_one "Bye [the_person_one.mc_title]..."
    $ hide_wip_screen()
    $ the_person_one.add_unique_on_room_enter_event(ashley_stephanie_saturday_coffee_recur)
    call advance_time from _call_advance_ashley_coffee_advance_02

    python:
        scene_manager.clear_scene()
        del the_person_one
        del the_person_two
    return

#Coffee time labels
#Labels in this section are to be randomly called during the coffee time event.
#TODO should this be actions? It would make setting requirements way easier... parse just like  crisis list...
label coffee_time_innocent_chat_label():
    $ the_person_one = ashley
    $ the_person_two = stephanie
    "The two sisters are chatting about kinds of different things."
    "Its fun to be in a situation where [the_person_one.title] opens up and actually... talks..."
    $ overhear_topic = the_person_one.get_random_opinion(include_sexy = False)
    $ text_one = person_opinion_to_string(the_person_one, overhear_topic)[1]
    $ text_two = get_topic_text(overhear_topic)
    the_person_one.char "... but yeah, I'm not sure he realizes I [text_one] [text_two]"
    if the_person_one.discover_opinion(overhear_topic):
        "Oh! You didn't realize that [the_person_one.title] felt that way."
    "The girls keep talking. They keep bouncing back and forth between multiple topics. You just listen as you sip your coffee."
    $ overhear_topic = the_person_two.get_random_opinion(include_sexy = False)
    $ text_one = person_opinion_to_string(the_person_two, overhear_topic)[1]
    $ text_two = get_topic_text(overhear_topic)
    the_person_two.char "...But I [text_one] [text_two], so I'm not sure what to do."
    if the_person_two.discover_opinion(overhear_topic):
        "Wow, you knew they were sisters, but they really do talk about basically everything!"

    python:
        del overhear_topic
        del text_one
        del text_two
    return

label coffee_time_sexy_chat_label():
    $ the_person_one = ashley
    $ the_person_two = stephanie
    "The two sisters are chatting about all kinds of different things."
    "Not surprisingly, the subject of the chatting turns sexual, as the two sisters talk about different sexual encounters."
    $ overhear_topic = the_person_two.get_random_opinion(include_sexy = True, include_normal = False)
    $ text_one = person_opinion_to_string(the_person_two, overhear_topic)[1]
    $ text_two = get_topic_text(overhear_topic)
    the_person_two.char "... but yeah, I have to say I [text_one] [text_two]"
    if the_person_two.discover_opinion(overhear_topic):
        "Oh! You didn't realize that [the_person_two.title] felt that way."
    "The girls keep talking. They keep bouncing back and forth between multiple sexual topics."
    $ overhear_topic = the_person_one.get_random_opinion(include_sexy = True, include_normal = False)
    $ text_one = person_opinion_to_string(the_person_one, overhear_topic)[1]
    $ text_two = get_topic_text(overhear_topic)
    the_person_one.char "...But I [text_one] [text_two], so I'm not sure what to do."
    if the_person_one.discover_opinion(overhear_topic):
        "Wow, you didn't realize they talked about sex in such detail with each other."

    python:
        del overhear_topic
        del text_one
        del text_two
    return

label coffee_time_steph_gets_handsy_label():
    $ the_person_one = ashley
    $ the_person_two = stephanie
    $ cum_on_hand = False
    "Without any provocation, you feel [the_person_two.possessive_title]'s hand on your thigh. She is rubbing back and forth, but is slowly drifting higher."
    "[the_person_two.title] is keeping a completely inconspicuous attitude."
    the_person_two "So Ash, any good concerts coming up soon?"
    "As she asks her sister, her hand drifts up to your crotch. It rapidly hardens as she begins to stroke it carefully."
    the_person_one "No... Not that I'm aware of anyway... The Chicago symphony is doing a charity live-stream later though, so I might watch that..."
    $ mc.change_arousal(15)
    "You decide two can play at this game. In the same way, you carefully run your hand along her thigh until it's resting on her mound. She gives a small sigh when you start to apply pressure on it."
    $ the_person_two.change_arousal(15)
    if the_person_two.sluttiness < 40:
        "You and [the_person_two.title] pet each other for several minutes. You are both getting aroused, but with clothes in the way it's impossible to finish."
        "With the public setting of the booth, you don't dare to push things any farther."
        if the_person_two.is_girlfriend():
            "[the_person_two.title] leans over and whispers in your ear."
            the_person_two "Why don't I come over to your place tonight, and we can do something like this, but with way less clothes..."
            menu:
                "Have her come over" if schedule_sleepover_available():
                    "You give her a nod. She takes that as her cue to stop."
                    the_person_two "I'll see you tonight then..."
                    $ schedule_sleepover_in_story(the_person_two)
                "Have her come over (disabled)" if not schedule_sleepover_available():
                    pass
                "Not tonight":
                    mc.name "I can't tonight, maybe another night..."
    else:
        "You and [the_person_two.title] pet each other for a few minutes, but stroking each other thru you clothes can only take things so far."
        if the_person_two.get_opinion_score("public sex") > 0:
            "She decides to push things further. You feel her hand clumsily reach into your pants, eventually pulling your cock out. The soft skin of her hand feels great."
            "Not to be outdone, you bring your up Stephanie's body, then slowly slide it under her clothes. When you get to her slit, you push you middle finger inside of her, while pushing your palm against her clit."
            "She sighs, but doesn't seem particularly concerned about other people around."
        else:
            "Not content to leave things where they are, you take the next step. You bring your hand up [the_person_two.possessive_title]'s body, then slowly slide it under her clothes."
            "She squirms a bit and glances around nervously as your hand reaches her slit. She sighs when your middle finger pushes inside of her, but is on alert for anyone who might be watching."
            "Not to be outdone, [the_person_two.title] starts to undo your zipper. She clumsily reaches into your pants and pulls your cock out. The soft skin of her hand feels great as she starts to stroke you."
        $ mc.change_arousal(30)
        $ the_person_two.change_arousal(30)
        if the_person_one.sluttiness < 40:
            "You and [the_person_two.title] continue to pet each other at the booth, sipping your coffees once in a while with your free hands."
            "Across the table, [the_person_one.title] appears to be completely oblivious. [the_person_two.possessive_title] is beginning to squirm as you stroke her gspot with your finger."
            $ mc.change_arousal(30)
            $ the_person_two.change_arousal(30)
            the_person_one "So... I'm thinking about going to the spa later treat myself to something... Do you want to go Steph?"
            the_person_two "Oh!!! Uhh... Yesssss..."
            "[the_person_two.title] practically growls. She's getting close and having trouble hanging on. You use the palm of your hand to grip her pussy harder, while your finger runs circles around her g spot."
            $ the_person_two.change_arousal(30)
            "She stops stroking you as she finishes. She leans forward a bit, closing her eyes as her pussy begins quivering around your finger."
            "You wish your cock was inside her instead of your finger, but in a place like a coffee shop booth, you can't justify risking it."
            $ the_person_two.have_orgasm(half_arousal = False)
            if the_person_two.get_opinion_score("public sex") > 0: #[If Steph likes public sex, she finishes you no matter what.]
                "[the_person_two.possessive_title] eventually opens her eyes, taking a quick peak around, then begins stroking you again."
                "Seems she is intent on giving you a similar treatment. You slowly pull your hand out of her clothes."
                the_person_two "Are you going to look at those tops we were looking at the other day Ash?"
                "[the_person_two.title] picks up the conversation with her sister."
                the_person_two "I really liked the way that crop top look on you."
                "Some of your precum is starting to leak out. [the_person_two.possessive_title] uses her thumb to spread it around the tip then keeps stroking."
                the_person_one "I don't know... I like the shirt but I don't know if I like how much skin it shows..."
                the_person_two "Aww, you should try it anyway! Guys like seeing a little midriff. Don't you agree [the_person_two.mc_title]?"
                "This time it's you who is barely able to get a reply out."
                mc.name "Ah yes. Yes it's very nice."
                "[the_person_one.title] raises an eyebrow. You think she is probably finally beginning to sense something is up..."
                mc.name "I mean, only if you feel comfortable with it..."
                "You manage to get out. She seems to buy it for now."
                the_person_one "I guess..."
                "The conversation continues, but you stop listening. The soft hand of [the_person_two.title] drives you over the edge and you start to cum in her hand."
                "Your cum spurts up and hits the bottom of the table before falling back down onto [the_person_two.possessive_title]'s hand and your pants. Oh fuck you are making a mess..."
                $ cum_on_hand = True
            else: #[Steph neutral or doesn't like public sex, give player the option]
                "As [the_person_two.title] regains her senses, she looks around for a moment. She looks at you and gives you a couple tentative strokes, clearly unsure of what to do."
                menu:
                    "Keep going":
                        "You slowly pull your hand away from [the_person_two.possessive_title]'s crotch. You put your hand on hers and encourage her to stroke you, making it clear that you expect her to continue."
                        "She looks around nervously but begins jacking you off again on her own."
                        mc.name "So what are you thinking about getting done at the Spa? I hear they have really good service there."
                        "You keep the conversation going so Steph can concentrate on her work. You are starting to leak precum, making her handjob feel even better."
                        the_person_one "Oh, ahh, well I want to get my nails done for sure... "
                        "[the_person_one.possessive_title] starts to explain. However, [the_person_two.title] is looking around nervously and she is starting to notice."
                        the_person_one "You okay Steph? You seem preoccupied..."
                        "She startles and looks back at her sister."
                        the_person_two "Oh! Yeah I just thought I saw someone..."
                        "Under the table you are reaching your limit. The soft hand of [the_person_two.title] drives you over the edge and you start to cum in her hand."
                        "Your cum spurts up and hits the bottom of the table before falling back down onto [the_person_two.possessive_title]'s hand and your pants. Oh fuck you are making a mess..."
                        $ cum_on_hand = True
                    "Stop":
                        "While [the_person_one.possessive_title] is looking something up on her phone, you whisper into [the_person_two.title]'s ear."
                        mc.name "Sorry, I don't want to make a mess here..."
                        if the_person_two.is_girlfriend():
                            "[the_person_two.title] leans over and whispers in your ear."
                            the_person_two "That's okay... maybe I can come over tonight and make it up to you?"
                            menu:
                                "Have her come over" if schedule_sleepover_available():
                                    "You give her a nod. She takes that as her cue to stop."
                                    the_person_two "I'll see you tonight then..."
                                    $ schedule_sleepover_in_story(the_person_two)
                                "Have her come over (disabled)" if not schedule_sleepover_available():
                                    pass
                                "Not tonight":
                                    mc.name "I can't tonight, maybe another night..."
                        "[the_person_two.possessive_title] release your erection, leaving it aching with need. You quickly put yourself away and zip up as [the_person_one.title] finishes pulling up a picture on her phone."
                        the_person_one "So I was thinking about getting my haircut to something like this... What do you think?"
                        "You continue your coffee date with the sisters, with [the_person_one.title] unaware of you getting her sister off right in front of her."
        else:
            the_person_one "So I was thinking about going to the spa... Do you think I should..."
            "[the_person_one.title] stops mid question and is looking at her sister. She quickly realizes what is going on."
            if ashley_is_secret_path():
                the_person_one "Wow... I guess I should have expected you two wouldn't be able to keep your hands off each other. I'll just play on my phone while you two do your thing..."
                "[the_person_one.title] gives you a look of what you can only call pure jealousy, before she pulls out her phone and starts looking at it."
            elif ashley_is_fwb_path():
                "You feel [the_person_one.title]'s foot beneath the table begin to rub along your leg."
                the_person_one "Damn... Right here in the booth? That's kinda hot..."
            "You push the palm of your hand rigidly against [the_person_two.possessive_title]'s clit, while your middle finger strokes her gspot. Your attention to her sensitive spots soon haa her gasping."
            "Only a whimper escapes her lips when you feel her pussy begin to quiver around your finger. She stops stroking you as she focuses on the pleasure of orgasming in the palm of your hands."
            $ the_person_two.have_orgasm(half_arousal = False)
            "After several seconds, [the_person_two.title] slowly opens her eyes and glances around as you withdraw your hand."
            if ashley_is_fwb_path():
                "Wow, that looked hot... [the_person_one.mc_title] will you do something like that to me later?"
                "TODO give hookup option here"
            if the_person_two.get_opinion_score("public sex") >= 0 and the_person_two.get_opinion_score("giving blowjobs") >= 0 and (the_person_two.get_opinion_score("public sex") > 0 or the_person_two.get_opinion_score("giving blowjobs") > 0):
                the_person_two "Hey Ash... Can you act natural for a minute and cover me? I need to take care of something..."
                "[the_person_two.title] gives her sister a wink, and [the_person_one.title] gives her a nod." #TODO (If she's looking at her phone, ashley agrees but is embarrassed)
                "[the_person_two.possessive_title] looks around to make sure no one is watching, but then slowly sinks in her seat and then slips under the table."
                $ scene_manager.update_actor(the_person_two, position = "blowjob")
                "She gets between your legs and immediately goes to work, sucking you off. [the_person_one.possessive_title] hears the slurping noises start and looks at you."
                if ashley_is_fwb_path():
                    the_person_one "Wow. I bet that feels good."
                elif ashley_is_secret_path():
                    "[the_person_one.title] doesn't say a word, but she puts two fingers in the shape of a V, the brings it to her face and sticks her tongue out between them, then points to herself."
                    "She is making it clear she is expecting you to get her off later"
                "The wet tongue of [the_person_two.title] is driving you quickly to orgasm. Between the public setting, her partial handjob, and talented mouth, you are sure you can't take any more."
                "You relax and enjoy the blowjob. Soon your orgasm approaches. There's no easy way to warn [the_person_two.title], so you just let it go, firing your load into her mouth."
                $ the_person_two.cum_in_mouth()
                "Her talented mouth takes your load easily. When you finish, her mouth slowly releases your cock and you hear a loud gulp."
                "You look around to make sure you are still anonymous before putting your hand on her should and then helping her back up and into her seat."
                $ scene_manager.update_actor(the_person_two, position = "sitting")
                "Once back up, she wipes what little cum managed to get on her face with a napkin and sets it aside. [the_person_two.title] shakes her head."
                $ the_person_two.outfit.remove_all_cum()
                $ scene_manager.draw_scene()
            else:
                "[the_person_two.title] eventually opens her eyes, taking a quick peak around, then begins stroking you again."
                "Seems she is intent on giving you a similar treatment. You slowly pull your hand away from her crotch."
                the_person_two "Your cock feels so hot in my hand..."
                "[the_person_two.possessive_title] whispers in your ear.Some of your precum is starting to leak out. She uses her thumb to spread it around the tip then keeps stroking."
                "The soft hand of [the_person_two.title] drives you over the edge and you start to cum in her hand."
                "Your cum spurts up and hits the bottom of the table before falling back down onto [the_person_two.possessive_title]'s hand and your pants. Oh fuck you are making a mess..."
                $ cum_on_hand = True
    if cum_on_hand:
        "[the_person_two.title] checks her hand while it's still under the table. It is absolutely coated in your cum."
        if the_person_two.get_opinion_score("public sex") >= 0 and the_person_two.get_opinion_score("drinking cum") >= 0 and (the_person_two.get_opinion_score("public sex") > 0 or the_person_two.get_opinion_score("drinking cum") > 0):
            if the_person_one.sluttiness < 40:
                "[the_person_two.possessive_title] beings her hand up from underneath the table and begins to lick your cum off of it. [the_person_one.title] notices and looks puzzled for a second, then realizes what she is doing."
                if ashley_is_secret_path():
                    the_person_one "Jesus Steph... Can you two seriously not keep your hands off each other for two seconds? You are nuts!"
                    "[the_person_one.title] looks at you, jealousy clear on her face."
                    # TODO Ash gains sluttiness, loses obedience and love
                elif ashley_is_fwb_path():
                    the_person_one "Jesus... Right here? You two are crazy..."
                    "[the_person_one.title] looks at you with a sparkle in her eye."
                    "[the_person_one.mc_title]... Does that mean I get you after this?"
                    #TODO Ash gains sluttiness and obedience
                    #TODO [Give mc option to promise to get with Ashley after]
            else:
                "[the_person_one.title] just watches as [the_person_two.title] brings her hand up from underneath the table and begins to lick your cum off of it."
        else:
            "You pick up a napkin and bring it under the table. You hold it in place as [the_person_two.title] wipes her hand off on it. You grab another napkin and use it to clean yourself off as best as you can, hoping no one will notice."
    return

init 2 python: #Coffee time requirements function. #TODO should I pull out coffee times stuff to its own file? this file might get too big.
    def coffee_time_innocent_chat_requirement():
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

    ashley_coffee_time_action_list.append(coffee_time_innocent_chat)
    ashley_coffee_time_action_list.append(coffee_time_sexy_chat)
    steph_coffee_time_action_list.append(coffee_time_innocent_chat)
    steph_coffee_time_action_list.append(coffee_time_sexy_chat)
    steph_coffee_time_action_list.append(coffee_time_steph_gets_handsy)

    def ashley_coffee_time_get_random_action():
        possible_action_list = []
        for ashley_scene in steph_coffee_time_action_list:
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
