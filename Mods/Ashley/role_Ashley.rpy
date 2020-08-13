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

        ashley.set_schedule([0,1,2,3,4], stephanie.home)
        ashley.home = stephanie.home
        ashley.home.add_person(ashley)

        ashley.event_triggers_dict["intro_complete"] = False    #
        ashley.event_triggers_dict["excitement_overhear"] = False   #
        ashley.event_triggers_dict["attitude_discussed"] = False   #
        ashley.event_triggers_dict["porn_discovered"] = False       #
        ashley.event_triggers_dict["porn_discussed"] = False    #
        ashley.event_triggers_dict["concert_overheard"] = False    #True after overhearing
        ashley.event_triggers_dict["concert_date"] = 0   #0 = not started, 1 = date arranged, 2 = date complete
        ashley.event_triggers_dict["porn_convo_day"] = 9999
        ashley.event_triggers_dict["porn_convo_avail"] = False

        # add appoint
        #office.add_action(HR_director_appointment_action)

        ashley_intro = Action("ashley_intro",ashley_intro_requirement,"ashley_intro_label") #Set the trigger day for the next monday. Monday is day%7 == 0
        mc.business.mandatory_crises_list.append(ashley_intro) #Add the event here so that it pops when the requirements are met.

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

    def ashley_get_days_employed():
        return day - ashley.event_triggers_dict.get("employed_since", 9999)

#Requirement Labels
init -1 python:
    def ashley_intro_requirement():   #After discovering an obedience serum trait and there is a position available. must be at work
        if day > 14 and mc.is_at_work() and mc.business.is_open_for_business():
            if mc.business.get_employee_count() < mc.business.max_employee_count:
                return True
                #TODO Consider making this true only if recruiting increased via HR director? Would be much delayed intro
                if sedatives_trait.researched or obedience_enhancer.researched or large_obedience_enhancer.researched: #TODO find a better trigger for this since we aren't doing MC serums anymore.
                    return False
        return False

    def ashley_hire_directed_requirement(the_person):
        if not the_person is stephanie:
            return False
        if ashley.event_triggers_dict.get("employed_since", 0) > 0:
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
        if the_person.location() == the_person.work:
            if ashley_get_days_employed() > 5: #Been working for at least a few days week.
                return True
        return False

    def ashley_ask_sister_about_attitude_requirement(the_person):
        if ashley_get_if_excitement_overheard():
            if the_person.location() == the_person.work:
                return True
        return False

    def ashley_room_warming_up_requirement(the_person):
        if the_person.location() == the_person.work:
            if ashley_get_days_employed() > 12: #Been working for at least a week.
                return True
        return False

    def ashley_room_overhear_classical_requirement(the_person):
        if the_person.location() == the_person.work:
            if ashley_get_days_employed() > 18:
                return True
        return False

    def ashley_ask_date_classic_concert_requirement(the_person):
        if ashley_get_concert_overheard() and not ashley_get_concert_date_stage() > 0:
            if the_person.location() == the_person.work:
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
            if the_person.location() == the_person.work:
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
            if the_person.location() == the_person.work:
                return True
        return False

    def add_ashley_hire_later_action():
        ashley_hire_directed = Action("Reconsider hiring her sister.", ashley_hire_directed_requirement, "ashley_hire_directed_label",
            menu_tooltip = "Talk to Stephanie about hiring her sister. She might be disappointed if you decide not to again...")
        head_researcher.add_action(ashley_hire_directed)
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
    mc.name "Well, you've taken an awfully large risk coming to work for me here, so I supposed I owe you one."
    the_person.char "You see, it's my sister. She just graduated from college, but is having trouble finding work in her degree. She's had to move in with me because she can't find work!"
    the_person.char "She's is really smart, but very introverted, it's been hard for her to get through interviews."
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
            mc.name "Of course, but being reminded of your blowjob skills will probably help me make up my mind if I want to hire someone you are related too."
            call fuck_person(the_person, start_position = blowjob, skip_intro = False, position_locked = True) from _call_sex_description_ashley_intro_bonus_BJ_1
            $ the_report = _return
            $scene_manager.update_actor(the_person, position = "stand4")
            if the_report.get("guy orgasms", 0) > 0:
                mc.name "God your mouth is amazing. If your sister sucks anything like you this will be a no-brainer..."
                the_person.char "Hah! Well, to be honest, I don't think she really cares for giving blowjobs, but I guess you never know."
    "You pick up her documents and look over them."
    "From her skill set, it is obvious the best choice of department for here would be in production. The only question is, should you hire her or not?"
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

label ashley_hire_directed_label(the_person):
    if the_person != stephanie:
        "Not steph? How did we get here?"
        return
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
        $ head_researcher.remove_action("ashley_hire_directed_label")
        $ mc.business.hire_person(ashley, "Production")

        "You complete the necessary paperwork and hire [ashley.name], assigning her to the production department."
        "As you finish up and start to leave, you notice [the_person.possessive_title] is already calling her sister with the news."
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
    mc.name "Hello there. You must be [the_person.name]. I'm [mc.name], the one who owns this place."
    "She looks at you, and see a hint of surprise on her face."
    the_person.char "Oh!... hello sir. It's nice to meet you. I'm sorry, my sister said this place was all women..."
    mc.name "That's right. Except me, the owner."
    the_person.char "Ah... I see... Well thank you for the opportunity. I appreciate the work."
    mc.name "Of course, [stephanie.title] is a good friend. Do you go by [the_person.name]? Or something else?"
    the_person.char "[the_person.title] is fine..."
    mc.name "[the_person.title] it is then."
    "You chit chat with [the_person.title] for a minute, but she speaks in short, one or two word replies. She seems very reserved."
    "Maybe she is just shy? You decide to let her get back to work."
    $ ashley.add_unique_on_room_enter_event(ashley_room_excitement_overhear)
    return

label ashley_room_excitement_overhear_label(the_person):
    $ the_person.draw_person()
    "As you step into the production room, you can overhear [the_person.title] talking excitedly to another co-worker."
    the_person.char "I know! I can't wait to go. All of my friends say that is so much fun..."
    "But as you enter the room, she notices, and immediately stops talking."
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
    mc.name "Earlier, I walked into production, and I could hear her carrying on with her coworkers. But as soon as I entered the room, she went completely silent."
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
    "As you step into the production room, you can overhear [the_person.title] talking excitedly to another coworker."
    the_person.char "I know, I just need to find someone to go with!"
    "As you enter the room, she looks and stops talking."
    the_person.char "Ahh... hello sir. Having a good day?"
    "Whoa. She actually said hi to you? Maybe she is warming up to you a little bit?"
    mc.name "It's been great so far. And you?"
    the_person.char "Oh... its been good I guess..."
    mc.name "Glad to hear it."
    $ mc.business.mandatory_crises_list.append(ashley_porn_video_discover)
    $ ashley.add_unique_on_room_enter_event(ashley_room_overhear_classical)
    return

label ashley_room_overhear_classical_label(the_person):
    "As you step into the production room, you can overhear [the_person.title] talking excitedly to another coworker."
    the_person.char "I know, the city symphony is performing a collection of Johannes Brahms' symphonies. I want to go so bad but I can't find anyone to go with..."
    "As you enter the room, she looks and stops talking."
    the_person.char "Ahh... hello sir. Having a good day?"
    "She has been slowly warming up to you over the last couple weeks."
    mc.name "It's been great so far. And you?"
    the_person.char "Oh, I've been good. Thanks for asking."
    mc.name "Glad to hear it."
    "Hmm... she is looking for someone to go with her to a classical music concert. Maybe that person could be you?"
    $ ashley.event_triggers_dict["concert_overheard"] = True
    return

label ashley_ask_date_classic_concert_label(the_person):
    mc.name "So... I couldn't help hearing earlier, you are looking to go to the Brahms Symphony recital, but you don't have anyone to go with?"
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
    $ mc.business.mandatory_crises_list.append(ashley_classical_concert_date)
    return

label ashley_classical_concert_date_label():
    $ the_person = ashley
    $ scene_manager = Scene()
    "It's Thursday. You have a date planned with [the_person.title]. It's taken a while for her to warm up to you, so you don't even consider cancelling."
    "You head downtown. The plan is just to meet up at the concert hall itself. [stephanie.title] is going to drop her sister off and pick her up afterwards."
    $ mc.change_location(downtown)
    $ mc.location.show_background()
    "Soon, you see the sisters."
    $ scene_manager.add_actor (the_person, position = "stand4", emotion = "happy")
    $ scene_manager.add_actor(stephanie, character_placement = character_center_flipped)
    stephanie.char "Oh hey, there's [stephanie.mc_title]. Don't worry I'm sure everything will be great."
    the_person.char "I know, I know... are you sure you don't want to go?"
    stephanie.char "Don't be silly, you've only got two tickets. You two will have a blast!"
    the_person.char "Okay..."
    "You walk over and greet the pair."
    #TODO when making story branch, use this first conversation to begin setting up paths. For now, love path only.
    #love: compliment ash. neutral: compliment both. corrupt: crude compliment
    mc.name "Hello! Thanks for this, I've been looking forward to this ever since we arranged this. [the_person.title] you look great tonight!"
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
    mc.name "I'll admit it, this is my first time going to something like this. I'm really excited to have the chance to do something like this though."
    the_person.char "Oh yeah? I think most guys find classical music a bit boring..."
    #TODO next path branch. different responses. love: glad to be here with you. neutral: glad to be here to watch. corrupt: just here to be with sexy girl
    mc.name "I'll admit I'm not an avid follower, but I think experiencing a variety of cultural events is an important thing for someone to do."
    the_person.char "Yeah, that's very insightful."
    mc.name "Plus, I'm glad to be able to spend some time with you and getting to know you better."
    "You notice her blush a bit, but you can also see her smile."
    $ the_person.change_stats(love = 2, happiness = 2)
    #end branch
    "Soon, the lights dim, and the music begins. It begins with a splendid piano melody."
    "You and [the_person.possessive_title] sit together silently, enjoying the music."
    "It goes through emotional highs and lows. At one point, you look over and you think you see a tear on [the_person.title]'s cheek."
    #TODO next path branch. hold hand (love), put arm around (neutral), or put hand on leg(corrupt)
    "You reach down and take her hand. She jumps at the contact, but quickly takes your hand in hers as the music goes through an emotional point."
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
    "She thinks about it before responding. One of the things you appreciate about [the_person.title] is she always thinks before she speaks."
    the_person.char "It was, and more. I really had a good time tonight."
    mc.name "Great! If you hear about another orchestra in town, I'd love to go again."
    the_person.char "I haven't heard anything, but I'll definitely keep it in mind. I'd like to do this again."
    $ scene_manager.add_actor(stephanie, character_placement = character_center_flipped)
    stephanie.char "Hey Ash! Hey [stephanie.mc_title]! How'd it go?"
    the_person.char "Steph! We had a great time. The performers were amazing..."
    stephanie.char "And I assume you were a perfect gentleman?"
    "[stephanie.title] gives you a look. She smiles, but you can tell she is genuinely protective of [the_person.title]"
    mc.name "Of course"
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
    "It's been a long day. You consider heading for bed, but you've got a lot of energy, you aren't sure you would be able to fall asleep."
    "You decide to hop on your PC and watch some porn and jack off before you go to bed. That always helps you fall asleep."
    "You load up your porn accounts and start browsing through some videos."
    "'Desperate Slut Begs for Creampie'? Nah! 'Guy Fucks Step Sister Stuck In Bear Trap'? hmm... maybe later."
    "As you browse, you notice a clip thumbnail with a girl riding a guy tied down and in restraints. She looks kinda familiar? Reminds you of someone from work maybe?"
    "'Naughty Co-Ed Ties Up Boyfriend. RUINED ORGASM'? EH, it's worth a shot anyway. You click on it and wait for the generic porn intro to finish."
    "You mouth falls open when the scene starts."
    $ scene_manager.add_actor (the_person, position = "stand4", emotion = "happy")
    "There's a guy and a girl, who you immediately recognize as [the_person.title]. This looks like one of those hidden camera type videos."
    "The guy is tied up, with his four limbs tied to the four corners of a bed. You watch as [the_person.title] gets up on the bed and gets on top of him."
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
    "Eventually, you can hear the guy starting to moan, its clear he is getting ready to cum."
    "She quickly hops off. The guy fills up the condom while [the_person.title] basically ignores him."
    the_person.char "Pathetic... maybe someday I'll let you touch me... but not today, that's for sure!"
    $ scene_manager.clear_scene()
    "Wow... shy [the_person.title]..."
    "This seems pretty crazy. She seems to some kind of closet dom? Its hard to believe."
    "She is so quiet... there's no way you can talk to her about it yet. Maybe you should try talking to [stephanie.title] about it?"
    $ stephanie.add_unique_on_talk_event(ashley_ask_sister_about_porn_video)
    $ ashley.event_triggers_dict["porn_discovered"] = True
    return

label ashley_ask_sister_about_porn_video_label(the_person):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person)
    mc.name "Hello [the_person.title]. I need to talk to you about something... sensitive. Could you please come with me to my office?"
    the_person.char "Of course."
    $ office.show_background()
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
    the_person.char "Yeah, she had this boyfriend a while back, it came out after they broke up that he was secretly filming them having sex and posting it online..."
    the_person.char "We did everything we could to shut it down once we found out, but the internet is crazy. Once it's out there, its out there!"
    mc.name "Wow, I feel awful, I had no idea."
    the_person.char "Yeah. Unfortunately, having that happen really got to her. That was like, over a year ago? And she hasn't been out with anyone since."
    the_person.char "As you probably saw... she was pretty... adventurous... with guys."
    the_person.char "But now it's almost like she can't trust any guys anymore."
    "You both look at each other for a moment, considering the circumstance."
    mc.name "I want to do something, but I don't know what."
    if the_person.love > 30:
        the_person.char "I don't know either... I guess just... keep being you?"
        the_person.char "You are a wonderful guy. Just be there for her, okay? You are like the only guy she interacts with any more."
    else:
        the_person.char "I mean, you are like, the only guy she interacts with... at all. She has completely cut herself off from men."
        the_person.char "Maybe you could try like, you know, being there for her? Help her learn that not all men are total assholes?"
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
    $ mc.business.mandatory_crises_list.append(ashley_mandatory_ask_about_porn)
    return

label ashley_mandatory_ask_about_porn_label():
    "You've had some time to think about [ashley.possessive_title], since you went on your date and discovered she was in a porn video unwittingly."
    "She seems to have warmed up to you enough, you decide maybe it is the right time to talk to her about it."
    $ ashley.event_triggers_dict["porn_convo_avail"] = True
    return

label ashley_ask_about_porn_label(the_person):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person)
    "You decide to breach the difficult topic of the porn video you discovered."
    mc.name "I was hoping to talk to you about something a little sensitive. Would you mind if we went to my office?"
    the_person.char "Oh... sure..."
    "[the_person.possessive_title] follows you to your office. After you enter, you close the door behind you."
    $ office.show_background()
    mc.name "Go ahead and have a seat."
    $ scene_manager.update_actor(the_person, position = "sitting", emotion = "sad")
    "You can tell she looks a little scared."
    mc.name "Are you okay?"
    the_person.char "I'm sorry sir, I'll work harder, you don't have to fire me..."
    "What? She thinks you brought her here to fire her?"
    #TODO Choice list
    mc.name "I didn't call you here to fire you. Hell, I'm not even disciplining you."
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
    mc.name "Hey, everyone has kinks. I'm not here to kink shame you."
    mc.name "I just wanted to tell you, I'm sorry about what happened. If you need any assistance going forward, please don't hesitate. I want to help if I can."
    the_person.char "Well... Steph and I... We worked hard to get that video off the internet. But once its out there, its out there I guess."
    "She looks down and thinks for a bit."
    the_person.char "The umm... the video. Did you watch the whole thing?"
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
    "DAMN. You feel your pants get a little tight after that. You remember from the video the way [the_person.title] took control and rode her ex..."
    mc.name "I mean, you don't have to do that..."
    $ scene_manager.update_actor(the_person, position = "stand4")
    "She gets up and walks around your desk. You stand up too."
    the_person.char "It's okay. I'm going to. You just enjoy."
    "With nothing else to say, [the_person.possessive_title] reaches down and begins to stroke your cock through your pants."
    the_person.char "Mmmm, I can tell you want to too!"
    "[the_person.title] has some skilled hands... You close your eyes and enjoy her stroking you for a moment."
    $ mc.change_arousal(10)
    "You hear a zipper some fabric rustle for a moment, then suddenly feel her warm hand on your dick, skin to skin. You look down and see her pulling your dick out."
    if the_person.has_taboo("touching_penis"):
        the_person.char "Oh my god... its so big... You've been hiding this from me, [the_person.mc_title]?"
        "She gives you a couple eager strokes. You can only moan in response. It feels good to finally feel her hands on you."
        $ the_person.break_taboo("touching_penis")
        $ mc.change_arousal(15)
    else:
        the_person.char "God, its so big. I love getting your cock out..."
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
    "Suddenly you here your office doorknob click and the door start to open. You forgot to lock it!!!"
    $ scene_manager.add_actor(stephanie, character_placement = character_left_flipped)
    stephanie.char "Hey [stephanie.mc_title] sorry to bug you but... oh fuck!"
    "It doesn't take [stephanie.title] long to survey the situation."
    stephanie.char "Holy shit, Ash! I didn't mean... I forgot to knock! Oh fuck!"
    $ scene_manager.update_actor(stephanie, position = "walking_away")
    "[stephanie.possessive_title] turns to flee the room."
    the_person.char "Oh my god... Steph this isn't what you think..."
    $ scene_manager.remove_actor(stephanie)
    "[stephanie.title] slams the door as she leaves the room."
    the_person.char "Oh no... oh god how am I going to explain this..."
    the_person.char "I'm sorry [the_person.mc_title]. I have to go!"
    "[the_person.title] quickly rushes to leave. You've barely had time to process everything that just happened."
    mc.name "[the_person.title]..."
    the_person.char "Don't say anything... I just need to go..."
    $ scene_manager.remove_actor(the_person)
    "[the_person.possessive_title] quickly leaves the room."
    "Welp, you just got a handjob from [the_person.title]... and then her sister promptly walks in and witnesses the whole thing."
    "You'll have to consider how to approach both girls carefully before you talk to them next."
    $ ashley.event_triggers_dict["porn_convo_avail"] = False

    $ scene_manager.clear_scene()
    return



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
