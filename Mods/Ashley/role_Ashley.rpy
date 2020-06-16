
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
        ashley_role = Role(role_name ="Ashley", actions =[], hidden = True)

        #global ashley_role
        #TODO make most variables identical to Stephanie
        global ashley
        ashley = create_random_person(name = "Ashley", last_name =stephanie.last_name, age = 22, body_type = "standard_body", face_style = "Face_3",  tits="B", height = 0.92, hair_colour="brown", hair_style = ponytail, skin="white" , \
            eyes = "brown", personality = introvert_personality, name_color = "#228b22", dial_color = "228b22" , starting_wardrobe = ashley_wardrobe, \
            stat_array = [1,4,4], skill_array = [1,1,3,5,1], sex_array = [4,2,2,2], start_sluttiness = 7, start_obedience = -18, start_happiness = 119, start_love = 0, \
            title = "Ashley", possessive_title = "Your intern", mc_title = mc.name, relationship = "Single", kids = 0)

        ashley.set_schedule([0,4], stephanie.home)
        ashley.set_schedule([1,2,3], stephanie.home)

        ashley.home = stephanie.home

        # ashley.home.add_person(ashley)
        ashley.event_triggers_dict["intro_complete"] = False    #
        ashley.event_triggers_dict["excitement_overhear"] = False   #
        ashley.event_triggers_dict["attitude_discussed"] = False   #
        ashley.event_triggers_dict["porn_discovered"] = False       #
        ashley.event_triggers_dict["porn_discussed"] = False    #
        ashley.event_triggers_dict["concert_overheard"] = False    #True after overhearing
        ashley.event_triggers_dict["concert_date"] = 0   #0 = not started, 1 = date arranged, 2 = date complete

        # add appoint
        #office.add_action(HR_director_appointment_action)

        ashley_intro = Action("ashley_intro",ashley_intro_requirement,"ashley_intro_label") #Set the trigger day for the next monday. Monday is day%7 == 0
        mc.business.mandatory_crises_list.append(ashley_intro) #Add the event here so that it pops when the requirements are met.

        ashley.opinions["production work"] = [2, True]  # she loves prod work
        ashley.opinions["work uniforms"] = [-1, False]  # uniforms stifle creativity
        ashley.opinions["flirting"] = [1, False]  # she likes attention, even if she is awkward
        ashley.opinions["working"] = [1, False]  # Her first real job
        ashley.opinions["the colour green"] = [2, False] #She loves green!
        ashley.opinions["pants"] = [1, False]  #And pants
        ashley.opinions["the colour blue"] = [-2, False] #She hates blue
        ashley.opinions["classical"] = [1, False]  #like calm, relaxing music.


        ashley.sexy_opinions["taking control"] = [2, False]  # she likes taking control, closet dom
        ashley.sexy_opinions["getting head"] = [2, False] # Loves to be serviced
        ashley.sexy_opinions["giving blowjobs"] = [-2, False]  # ultimate act of submission

        #TODO make her know Nora from before graduation. She is familiar with serums and their effects
        #TODO add ashley to unique characters list?

        return

    ashley_first_talk = Action("Introduce yourself to Ashley",ashley_first_talk_requirement,"ashley_first_talk_label")
    ashley_room_excitement_overhear = Action("Overhear Ashley",ashley_room_excitement_overhear_requirement,"ashley_room_excitement_overhear_label")
    ashley_ask_sister_about_attitude = Action("Ask about Ashley's attitude",ashley_ask_sister_about_attitude_requirement,"ashley_ask_sister_about_attitude_label")
    ashley_room_warming_up = Action("Ashley is warming up",ashley_room_warming_up_requirement,"ashley_room_warming_up_label")
    ashley_porn_video_discover = Action("Discover Ashley's porn video",ashley_porn_video_discover_requirement,"ashley_porn_video_discover_label")
    ashley_ask_sister_about_porn_video = Action("Ask about Ashley in porn",ashley_ask_sister_about_porn_video_requirement,"ashley_ask_sister_about_porn_video_label")

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
        return False

    def ashley_ask_date_classic_concert_requirement(the_person):
        return False

    def ashley_classical_concert_date_requirement():
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

    def add_ashley_hire_later_action():
        ashley_hire_directed = Action("Reconsider hiring her sister.", ashley_hire_directed_requirement, "ashley_hire_directed_label",
            menu_tooltip = "Talk to Stephanie about hiring her sister. She might be disappointed if you decide not to again...")
        head_researcher.add_action(ashley_hire_directed)
        return

    def hire_ashley():
        mc.business.add_employee_production(ashley)
        town_relationships.update_relationship(ashley, stephanie, "Sister")
        town_relationships.update_relationship(nora, ashley, "Friend")
        town_relationships.update_relationship(lily, ashley, "Rival")
        head_researcher.remove_action_by_effect("ashley_hire_directed_label")
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
                mc.name "God your mouth is amazing. If your sister sucks anything like you this will be a no brainer..."
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

        $ hire_ashley()

        "You complete the necessary paperwork and hire [ashley.name], assigning her to the production department."
        #TODO make sure her home is set to Stephanie's house somehow.
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

        $ hire_ashley()

        "You complete the necessary paperwork and hire [ashley.name], assigning her to the production department."
        #TODO make sure her home is set to Stephanie's house somehow.
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
    "As you step into the production room, you can overhear [the_person.title] talking excitedly to another coworker."
    the_person.char "I know! I can't wait to go. All of my friend's say that is so much fun..."
    "But as you enter the room, she notices, and immediately stops talking."
    the_person.char "..."
    "Clearly she has no issue talking to her coworkers... why is she so quiet with you? Maybe you should ask her sister about it."
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
    "Hmm... she is looking for someone to go with her to a classical music concert. Maybe that person could be you?"
    $ mc.business.add_unique_mandatory_crisis(ashley_porn_video_discover)
    return

label ashley_room_overhear_classical_label(the_person):
    "As you step into the production room, you can overhear [the_person.title] talking excitedly to another coworker."
    the_person.char "I know, the city symphony is performing a collection of Johannes Brahm's symphonies. I want to go so bad but I can't find anyone to go with..."
    "As you enter the room, she looks and stops talking."
    the_person.char "Ahh... hello sir. Having a good day?"
    "Whoa. She actually said hi to you? Maybe she is warming up to you a little bit?"
    mc.name "It's been great so far. And you?"
    the_person.char "Oh... its been good I guess..."
    mc.name "Glad to hear it."
    "Hmm... she is looking for someone to go with her to a classical music concert. Maybe that person could be you?"
    $ ashley.event_triggers_dict["concert_overheard"] = True
    return

label ashley_ask_date_classic_concert_label(the_person):
    mc.name "So... I couldn't help hearing earlier, you are looking to go to the Brahm Symphony recital, but you don't have anyone to go with?"
    the_person.char "Ummm yeah, something like that..."
    "She is looking down, avoiding eye contact with you."
    mc.name "That sounds like a great cultural event. I was wondering if you would be willing to let me take you?"
    "She is caught off gaurd. She wasn't expecting you to ask something like this!"
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
    the_person.char "Sure! I'll plan on it."
    "You feel good about this as you finish up your conversation. Maybe you can finally get her to come out of her shell a little..."
    return

label ashley_classical_concert_date_label():
    #TODO move downtown.
    $ the_person = ashley
    "It's thursday. "
    return

label ashley_porn_video_discover_label():
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
    "She starts to dry hump the poor guy. With his limbs down at his sides, there's not much her can really do."
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

# label ashley_porn_video_update_label():
#     "It's been a few days since you found out that [ashley.title] starred, unwillingly, in a porn video."
#     "It has been a turmoil of emotions for you, discovering your good friend was used like that. But realistically, what can you do about it?"
#     "You've decided. There's no way you can talk to [ashley.title] about it. Not yet anyway."
#     "But... you could always talk to her sister, [stephanie.title]. She might have some ideas on what to do, or even how to track down this guy."
#
#     return

label ashley_ask_sister_about_porn_video_label(the_person):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person)
    mc.name "Hello [the_person.title]. I need to talk to you about something... sensitive. Could you please come with me to my office?"
    the_person.char "Of course."
    #TODO change background to office
    "You enter your office an gesture for her to sit down."
    $ scene_manager.update_actor(the_person, position = "sitting")
    if the_person.sluttiness > 50:
        "As she sits down, you notice [the_person.possessive_title]'s posture. She is sticking her chest out. She probably thinks you brought her to your office for some... personal time."
    mc.name "I wanted to talk to you again, about your sister, [ashley.title]."
    the_person.char "Oh!... right..."
    if the_person.sluttiness > 50:
        "Her back slumps noticeably when you say that."
    mc.name "This is not going to be an easy, or pleasant conversation, but uhh, I found a video of your sister..."
    the_person.char "UGH! I thought we got that deleted from everywhere."
    mc.name "Oh... deleted?"
    $ scene_manager.update_actor (the_person, emotion = "sad")
    the_person.char "Yeah, she had this boyfriend a while back, it came out after they broke up that he was secretly filming them having sex and posting it online..."
    the_person.char "We did everything we could to shut it down once we found out, but the internet is crazy. Once it's out there, its out there!"
    mc.name "Wow, I feel awful, I had no idea."
    the_person.char "Yeah. Unfortunately, having that happen really got to her. That was like, over a year ago? And she hasn't been out with anyone since."
    the_person.char "AS you probably saw... she was pretty... adventurous... with guys."
    the_person.char "But now its almost like she can't trust any guys anymore."
    "You both look at each other for a moment, considering the circumstance."
    mc.name "I want to do something, but I don't know what."
    if the_person.love > 30:
        the_person.char "I don't know either... I guess just... keep being you?"
        the_person.char "You are a wonderful guy. Just be there for her, okay? You are like the only guy she interacts with anymore."
    else:
        the_person.char "I mean, you are like, the only guy she interacts with... at all. She has completely cut herself off from men."
        the_person.char "Maybe you could try like, you know, being there for her? Help her learn that not all men are total assholes?"
    mc.name "I suppose. Anything specific?"
    the_person.char "Honestly? I'm not really sure. Ash moving back in with me only just happened, and we didn't really see each other much while going through college."
    "After a few solemn moments, you decide to move on with your day."
    mc.name "That's enough for now I suppose. Let me know if you think of anything."
    the_person.char "Yes sir... and the same for you."
    $ ashley.event_triggers_dict["porn_discussed"] = True
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
