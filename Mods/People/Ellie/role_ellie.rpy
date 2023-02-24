#Ellie's story is a coming of age story (even though she's 24) because she grew up in a strict religious family.
#Ellie has ZERO experience, and therefore ZERO sex opinions.
#During her story, MC will have choices in her initial sexual encounters. MC choices will shape her opinions
#E.G., if you make her fingering scene good, she loves getting fingered. If you degrade her during, she hates it.
#Good ending to scenes should be available to 90% of players based on stats. don't make them too restrictive.
#GOOD OPTIONS ALWAYS OPEN WITH LOVE. She is supposed to be your souther belle sweetheart.
#All sexual options are opened during story. EG she is completely frigid until players progress with her.
#Progressing with Ellie may also open up new nanobot improvements.
#Uses the date override code from the old casual sex code to modify her dates so MC can't go back to her place until appropriate point in the story.

init 2 python:
    def ellie_mod_initialization():
        ellie_wardrobe = wardrobe_from_xml("Ellie_Wardrobe")
        ellie_base_outfit = Outfit("ellie's base accessories")
        the_eye_shadow = heavy_eye_shadow.get_copy()
        the_eye_shadow.colour = [.71, .4, .85, 0.5]
        the_glasses = big_glasses.get_copy()
        the_glasses.colour = [.15, .15, .15, 1.0]
        the_lipstick = lipstick.get_copy()
        the_lipstick.colour = [.37, .02, .05, 0.75]
        the_necklace =gold_chain_necklace.get_copy()    #Closest thing we have to a cross necklace
        the_necklace.colour = [.95, .95, .78, 1.0]
        the_bracelet = copper_bracelet.get_copy()
        the_bracelet.colour = [.95, .95, .78, 1.0]
        ellie_base_outfit.add_accessory(the_eye_shadow)
        ellie_base_outfit.add_accessory(the_glasses)
        ellie_base_outfit.add_accessory(the_lipstick)
        ellie_base_outfit.add_accessory(the_necklace)
        ellie_base_outfit.add_accessory(the_bracelet)

        # init ellie job (make her hidden on start)
        ellie_job = Job("IT Specialist", critical_job_role, purgatory, work_days = [0,1,2,3,4,5,6], work_times = [1,2,3],
            mandatory_duties = [research_work_duty], available_duties = [] + general_duties_list + general_rd_duties)

        #global ellie
        global ellie
        ellie = make_person(name = "Ellie", age = 24, body_type = "thin_body", face_style = "Face_13",  tits="DDD", height = 0.92, hair_colour="dark auburn", hair_style = bobbed_hair, skin="white" , \
            eyes = "light blue", personality = ellie_personality, name_color = "#228b22", dial_color = "228b22" , starting_wardrobe = ellie_wardrobe, job = ellie_job, \
            stat_array = [1,4,4], skill_array = [1,1,3,5,1], sex_skill_array = [1,1,1,1], sluttiness = 0, obedience_range = [100, 110], happiness = 103, love = -3, \
            relationship = "Single", kids = 0, work_experience = 2, force_random = True, base_outfit = ellie_base_outfit, type = 'story',
            forced_opinions = [["production work", 2, True], ["work uniforms", 1, False], ["flirting", 1, False], ["working", 1, False], ["the colour green", 2, False], ["pants", 1, False], ["cooking", 2, False]])

        ellie.generate_home()
        ellie.home.add_person(ellie)
        ellie.idle_pose = "stand2"

        ellie.event_triggers_dict["intro_complete"] = False    # True after first talk
        ellie.event_triggers_dict["blackmail_stage"] = 0
        ellie.event_triggers_dict["squirts"] = False
        ellie.event_triggers_dict["been_fingered"] = False
        ellie.event_triggers_dict["given_handjob"] = False
        ellie.event_triggers_dict["given_blowjob"] = False
        ellie.event_triggers_dict["given_virginity"] = False
        ellie.event_triggers_dict["given_anal_virginity"] = False
        ellie.event_triggers_dict["brought_lunch"] = False
        ellie.event_triggers_dict["dinner_date"] = False
        ellie.event_triggers_dict["work_turnon"] = False

        ellie.event_triggers_dict["tit_fuck"] = False
        ellie.event_triggers_dict["has_submit"] = False
        ellie.event_triggers_dict["fetish_avail"] = False

        ellie.event_triggers_dict["foreplay_position_filter"] = ellie_foreplay_position_filter
        ellie.event_triggers_dict["oral_position_filter"] = ellie_oral_position_filter
        ellie.event_triggers_dict["vaginal_position_filter"] = ellie_vaginal_position_filter
        ellie.event_triggers_dict["anal_position_filter"] = ellie_anal_position_filter
        ellie.event_triggers_dict["unique_sex_positions"] = ellie_unique_sex_positions

        mc.business.add_mandatory_crisis(ellie_start_intro_note) #Add the event here so that it pops when the requirements are met.

        #We usually set progress screen info here, but we wait until appropriate in the story to do it, since Ellie is initially a ?????

        # set relationships
        # Ellie is relatively new in town and has no mutual relationship with MC
        ellie.text_modifiers.append(southern_belle)
        return

    def ellie_foreplay_position_filter(foreplay_positions):
        filter_out = []
        if not ellie_has_tit_fuck():
            filter_out.append(tit_fuck)
        if not ellie_has_been_fingered():
            filter_out.append(standing_finger)
            filter_out.append(standing_grope)
            filter_out.append(drysex_cowgirl)
            filter_out.append(standing_dildo)
        if not ellie_has_given_handjob():
            filter_out.append(handjob)
            filter_out.append(cowgirl_handjob)
        if foreplay_positions[1] in filter_out:
            return False
        else:
            return True
        return True

    def ellie_oral_position_filter(oral_positions):
        if ellie_has_given_blowjob():
            return True
        return False

    def ellie_vaginal_position_filter(vaginal_positions):
        if ellie_has_given_virginity():
            return True
        return False

    def ellie_anal_position_filter(anal_positions):
        if ellie_has_given_anal_virginity():
            return True
        return False

    def ellie_unique_sex_positions(person, prohibit_tags = []):
        positions = []

        return positions

    def take_virginity(the_person): #Use this to apply the appropriate "clothing" item
        the_blood = creampie_cum.get_copy()
        the_blood.colour = [.71, .1, .1, 0.8]
        the_blood.layer = 0
        the_person.outfit.add_accessory(the_blood)
        the_blood_2 = ass_cum.get_copy()
        the_blood_2.colour = [.71, .1, .1, 0.6]
        the_blood_2.layer = 0
        the_person.outfit.add_accessory(the_blood_2)
        the_person.break_taboo("vaginal_sex")
        the_person.event_triggers_dict["given_virginity"] = True
        return

    def restore_virginity(the_person):  #For testing purposes only.
        the_person.event_triggers_dict["given_virginity"] = False
        return

init -2 python: #Requirement Functions

    def ellie_start_intro_note_requirement():
        #return False
        if fetish_serum_unlock_count() >= 1 and get_fetish_basic_serum().mastery_level > 3.0 and mc.business.head_researcher:
            if time_of_day == 2 and day%7 == 2:
                return True
        return False

    def ellie_meet_ellie_intro_requirement():
        return time_of_day == 4 and day%7 == 3

    def ellie_head_researcher_halfway_intro_requirement():
        return time_of_day == 3 and day%7 == 0

    def ellie_unnecessary_payment_requirement():
        return time_of_day == 4 and day%7 == 3

    def ellie_self_research_identity_requirement():
        return time_of_day == 3 and day%7 == 0

    def ellie_end_blackmail_requirement():
        return time_of_day == 4 and day%7 == 3

    def ellie_work_welcome_requirement():
        return time_of_day == 0 and day%7 == 4

    def ellie_work_welcome_monday_requirement():
        return time_of_day == 0 and day%7 == 0

    def ellie_never_been_kissed_requirement(the_person):
        if ellie_is_working_on_nanobots() or ellie.sluttiness >= 20:
            if mc.business.days_since_event("hired_ellie_IT") >= TIER_2_TIME_DELAY:
                return True
        return False

    def ellie_grope_followup_requirement():
        if mc.is_at_work() and mc.business.is_open_for_business():
            return True
        return False

    def ellie_text_message_apology_requirement():
        if day%7 == 6:
            return True
        return False

    def ellie_never_given_handjob_requirement():
        if ellie.love >= 20 and mc.is_at_work() and mc.business.is_open_for_business():
            return True
        return False



init 1 python:
    ellie_start_intro_note = Action("Blackmail Note", ellie_start_intro_note_requirement, "ellie_start_intro_note_label")
    ellie_meet_ellie_intro = Action("Meet Your Blackmailer", ellie_meet_ellie_intro_requirement, "ellie_meet_ellie_intro_label")
    ellie_head_researcher_halfway_intro = Action("Blackmailer Identity", ellie_head_researcher_halfway_intro_requirement, "ellie_head_researcher_halfway_intro_label")
    ellie_unnecessary_payment = Action("Pay Blackmailer", ellie_unnecessary_payment_requirement, "ellie_unnecessary_payment_label")
    ellie_end_blackmail = Action("End Blackmail", ellie_end_blackmail_requirement, "ellie_end_blackmail_label")
    ellie_work_welcome = Action("Hire Ellie", ellie_work_welcome_requirement, "ellie_work_welcome_label")
    ellie_work_welcome_monday = Action("Review Ellie", ellie_work_welcome_monday_requirement, "ellie_work_welcome_monday_label")
    ellie_self_research_identity = Action("Blackmailer Identity", ellie_self_research_identity_requirement, "ellie_self_research_identity_label")
    ellie_never_been_kissed = Action("Ellie Gets Kissed", ellie_never_been_kissed_requirement, "ellie_never_been_kissed_label")
    ellie_grope_followup = Action("Ellie confronts you", ellie_grope_followup_requirement, "ellie_grope_followup_label")
    ellie_text_message_apology = Action("Ellie texts you", ellie_text_message_apology_requirement, "ellie_text_message_apology_label")
    ellie_never_tasted_cock = Action("Ellie wants to taste", ellie_never_tasted_cock_requirement, "ellie_never_tasted_cock_label")
    ellie_never_been_fucked = Action("Ellie wants to fuck", ellie_never_been_fucked_requirement, "ellie_never_been_fucked_label")
    ellie_never_tried_anal = Action("Ellie tries anal", ellie_never_tried_anal_requirement, "ellie_never_tried_anal_label")

    ellie_turned_on_while_working_intro = Action("Ellie gets horny", ellie_turned_on_while_working_intro_requirement, "ellie_turned_on_while_working_intro_label")
    ellie_turned_on_while_working = Action("Ellie gets horny", ellie_turned_on_while_working_requirement, "ellie_turned_on_while_working_label")    #NOTE: This should probably get moved to a separate crisis file

label ellie_start_intro_note_label():
    $ the_person = mc.business.head_researcher
    "You get an email notification on your phone. Normally you would brush something like this off as spam, but the subject line has your name in it."
    "You open it up and are surprised by what you read. It is short and to the point."
    "?????" "I know what your company is doing with the nanobots, and I'll go public with it if you don't meet my demands."
    "?????" "Meet me tomorrow night in alley between 3rd and 5th street downtown. Come alone, and bring cash."
    "Well that's not good. That sounds very not good. You find yourself panicking for a moment."
    "You take a deep breath. You should get with [the_person.possessive_title]. You quickly page her to meet you in your office."
    $ ceo_office.show_background()
    "You sit at your desk and anxiously wait for her to meet you."
    $ the_person.draw_person()
    the_person "Hey, you wanted to see me?"
    mc.name "Close the door and come sit down."
    $ the_person.draw_person(position = "sitting")
    "She slides quietly into the chair."
    the_person "Boy, you sure are somber... something on your mind?"
    mc.name "You could say that..."
    "You pull up the email and show it to her."
    "She is just as surprised as you."
    the_person "Wow... fuck... okay. What can I do to help?"
    mc.name "So, here is what I am thinking. Across from the alley is a bar where you can get on the roof fairly easily."
    mc.name "Can you come with me, but hide up on the roof with like... a camera or binoculars or something? Just watch while I deal with this."
    the_person "Yeah. I can do that. I think I know where you are talking about."
    mc.name "I'll pull out some cash the day of and be ready. Although the email doesn't even say how much cash to bring."
    the_person "Yeah... it's a little ambiguous... But I can do that."
    "You spend some time in your office with [the_person.title], making a quick and dirty plan for how to deal with the blackmail threat."
    mc.name "Alright, it's a plan. I won't meet with you tomorrow night, in case we are being watched or tracked, but it's a plan at least."
    the_person "Ok... We'll talk then."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] gets up and leaves your office. This is a precarious situation, and you can't help but worry about it."
    $ clear_scene()
    $ mc.location.show_background()
    $ mc.business.add_mandatory_crisis(ellie_meet_ellie_intro)
    #TODO link next scene.
    return

label ellie_meet_ellie_intro_label():
    $ the_person = mc.business.head_researcher
    "As night falls, you make your way downtown. Tonight you are meeting with your mysterious blackmailer."
    $ mc.change_location(downtown)
    $ mc.location.lighting_conditions = dark_lighting
    "You text [the_person.possessive_title] to make sure she is still going to be there."
    $ mc.start_text_convo(the_person)
    mc.name "In the alley between 3rd and 5th. Did you manage to find a good vantage point?"
    the_person "Sure did. I don't see anyone yet, and I brought a taser, you know, just in case."
    $ mc.end_text_convo()
    "You have no idea how organized this person or group is, but you doubt that if things turn sour a taser will make much of a difference. You decide to keep that to yourself, though."
    "Hopefully she will go unnoticed if the blackmailer decides to have reinforcements of his own."
    "The blackmail note said to bring cash... But not how much. You pulled some strings at the bank and got $1000 in 20s, hopefully that will be enough."
    "Your business is just getting off the ground, so you really don't have the cash to handle a huge demand."
    "Eventually, the time comes, so you head down the alley. As you hit the halfway mark, a shadowy figure emerges from behind a dumpster."
    $ ellie.draw_person()
    ellie "That's far enough, stay right there."
    "The first thing you notice is the heavy southern twang in her accent. Secondly, it is heavily feminine. A southern woman is blackmailing you? It catches you completely off guard."
    ellie "You got cash?"
    mc.name "Yeah, although the note failed to mention exactly how much you were expecting."
    ellie "I'm figuring a million dollars in cold hard cash."
    "You pause. She can't be serious? If she knows anything about your business, she has to know you have no way of pulling that kind of liquidity."
    mc.name "I'm sorry, my business is just founded, and I don't have the ability to pull that much, especially on such short notice."
    ellie "Ah lordie help me. Hmm. How about this. You give me some cash now as a show of good faith, and we'll meet again next week and you kin give me the money then."
    ellie "As a fellow criminal, surely you can understand that I got bills to pay."
    "You doubt you will be able to find a million dollars between now and next week, but at least this will give you some time to try and figure things out."
    mc.name "Alright, that's a deal."
    ellie "Alright. For now, let me have a hundred dollars. That'd outta get me thru until next week..."
    "This whole conversation is throwing up serious red flags. Is she really just asking a hundred for now? The whole thing reeks of amateurism."
    "You look up and around, trying to see if you see any motion or hint that she may have someone else watching, but don't see anything. You decide to play along for now."
    "You pull out a hundred dollars, being careful not to show the remaining bills you have with you, and extend your hand with them."
    $ mc.business.change_funds(-100)
    "She slowly walks forward and take she money from you. The alley is dark, but is that red hair? She quickly pulls away."
    ellie "Same time next week."
    "The mysterious blackmailer turns and quickly leaves the alley. You stand there observing her until she turns the corner, when you turn around and leave the alley."
    $ clear_scene()
    "Once you are a safe distance away from the alley, you pull out your phone and text [the_person.possessive_title]."
    $ mc.start_text_convo(the_person)
    mc.name "Hey, meet me at the bar. We have a lot to talk about."
    the_person "Okay, see you there"
    $ mc.end_text_convo()
    $ mc.location.lighting_conditions = standard_outdoor_lighting
    $ mc.change_location(downtown_bar)
    "You grab a secluded table away from the crowd around the bar with [the_person.title]."
    $ the_person.draw_person(position = "sitting")
    the_person "So, how'd it go?"
    mc.name "Confusing, to be honest. You see anything from where you were at?"
    the_person "Not much, to be honest. I could tell it was a woman, but I didn't see anyone else and couldn't make out much about her."
    mc.name "Well, first thing, she had a heavy southern accent. She could have been faking it, but I doubt it. The whole thing felt... Like she was an amateur, to be honest."
    the_person "Why do you say that?"
    mc.name "Well, she really seemed to have no idea how much money to ask for, so she just said she needed a million dollars."
    the_person "Wow, there's no way you could make a ransom like that, at least as far as I know."
    mc.name "Right? And then when I said I didn't have that kind of money, she told me had she had bills to pay?"
    mc.name "So she just asked for a hundred dollars as a show of good faith, and to meet again next week..."
    the_person "Wow... That's so weird."
    mc.name "It was hard to see, the alley was so dark but... When she took the money from me... I think she's a redhead."
    the_person "Ahhh, a southern redhead? Of all the luck you have, your blackmailer happens to be a southern redhead? Did she have another obvious feature? Missing a leg perhaps?"
    "Your head researcher is joking with you, but you can't help but laugh. This has to be a setup... Right? How many southern redheads could possibly live in this town?"
    mc.name "Nothing else that I noticed. But the bills to pay thing bugs me."
    the_person "You think she's unemployed maybe?"
    mc.name "Maybe. I don't know. Up for helping me out with some research?"
    the_person "Oi. I guess I can do that. I'll do some searching on the internet this weekend and see if anything comes up."
    mc.name "Thanks. I appreciate it."
    "You decide you've had quite enough adventure for one night, so you decide to head home."
    mc.name "Thanks for your help [the_person.title]. I appreciate it."
    $ the_person.change_happiness(2)
    the_person "Well, I admit, I feel partially responsible since I was the one to bring in the nanobots in the first place."
    mc.name "I don't know why, but I feel a lot better about this whole thing. If we can figure out who she is, maybe we can come up with an alternative solution."
    the_person "Err... you don't mean like... 'taking care of her' do you?"
    mc.name "Of course not! But there may be other things we can do about this, I think."
    "With your business concluded, you and [the_person.possessive_title] part ways."
    $ mc.change_location(bedroom)
    $ clear_scene()
    $ mc.business.add_mandatory_crisis(ellie_head_researcher_halfway_intro)
    return

label ellie_head_researcher_halfway_intro_label():
    $ the_person = mc.business.head_researcher
    if the_person is None:
        $ mc.business.add_mandatory_crisis(ellie_unnecessary_payment)
        return
    "You feel your phone vibrate in your pocket. It's [the_person.possessive_title]."
    $ mc.start_text_convo(the_person)
    the_person "I'm a genius. Meet me in your office!"
    mc.name "I'll be right there."
    $ mc.end_text_convo()
    $ ceo_office.show_background()
    "You step into your office, as you do, you see [the_person.title] sitting behind your desk."
    $ the_person.draw_person(position = "sitting")
    "You close the door and walk over."
    mc.name "What is it?"
    the_person "Well, following a hunch, I contacted the contact I had that got us the nanobots and the program in the first place."
    the_person "It was just too weird that this girl had so much info about them."
    the_person "I gave him a description of the blackmailer, and he finally got back to me this morning."
    the_person "The company launched an investigation trying to figure out who leaked the bots, but they got the wrong person."
    the_person "The company came down hard on a relatively new person. A woman they had hired about a year ago. A fresh computer science college graduate from University of Alabama..."
    mc.name "Ahhhhh."
    the_person "He sent me her basic details..."
    "[the_person.possessive_title] hands you a dossier she has put together on this person. The first thing you notice is her red hair."
    the_person "[ellie.name] [ellie.last_name]. Redhead, southern computer expert."
    mc.name "It's perfect. What happened with her employer?"
    the_person "She got fired. The kicker is, she signed a 5 year non-compete contract when she got hired, and so the company threatened her with a lawsuit if she tries to get another job in her field."
    mc.name "Wow... So now here she is, far away from home, and no way to pay the bills."
    the_person "That's right!"
    "You feel conflicted about this. Surely, this is the girl that is blackmailing you... but you are also partially responsible for it, having acquired the nanobots in the first place."
    "When you look at [the_person.title], she is looking at you funny."
    the_person "So... you're going to try and help her... aren't you?"
    mc.name "I mean... I am kind of responsible for her getting fired..."
    the_person "Maybe. But how do you want to help? You can't just give her easy money every week."
    mc.name "No. But that non-compete... Those are usually for specific position descriptions, right?"
    the_person "Yeah, usually..."
    mc.name "Maybe we could hire her? Having a computer person could be seriously handy around here... but we could make her official position something that isn't obvious."
    the_person "That might work actually."
    mc.name "If this other company ever calls us, we could just say she works in HR, for example. She's a college graduate, I'm sure she could handle that work too."
    the_person "Hey, you don't have to convince me. It would be nice to have a tech person around here for sure though."
    mc.name "Alright. Next time I meet with her, I'll consider trying to hire her. If nothing else, maybe I can at least scare her off."
    the_person "Okay. Let me know if there is anything else I can help out with, [the_person.mc_title]!"
    $ clear_scene()
    "[the_person.possessive_title] gets up and leaves you alone in your office."
    "You meet again with [ellie.fname] on Thursday night. You feel like you could definitely hire her."
    "WARNING: If you want to hire [ellie.fname], make sure you have an open employee position! You may miss the opportunity to hire her if you don't!"
    #TODO link up next event.
    $ mc.business.add_mandatory_crisis(ellie_end_blackmail)
    $ mc.location.show_background()
    return

label ellie_unnecessary_payment_label():    #Use this scene each week if MC can't find out info on Ellie for some reason (head researcher fired, etc)
    $ the_person = ellie
    "As night falls, you make your way downtown. Tonight you are meeting with your blackmailer."
    $ mc.change_location(downtown)
    $ mc.location.lighting_conditions = dark_lighting
    "The time comes so you head for the alley. As you approach, you hear the southern twang of her accent as she steps from the shadows."
    $ the_person.draw_person()
    the_person "'Ey. Got the money?"
    "You stop."
    if ellie.event_triggers_dict.get("blackmail_stage", 0) == 0:    #First time
        mc.name "I have some money... but a million dollars is a lot of money. My business doesn't pull that much in a year."
        the_person "Sounds like you have a problem then. I want my money."
        mc.name "What are you going to do with a million dollars, anyway? How are you going to keep it secret from the IRS?"
        the_person "You let me worry about that hun."
        mc.name "Well, for now, I have the same amount as last week. I'll keep working on it, but it's going to take me a while to get that much money."
        the_person "Work on it. I'll be watching you."
        "You hand the mysterious blackmailer $100 again. She turns and walks away."
        $ mc.business.change_funds(-100)
        $ ellie.event_triggers_dict["blackmail_stage"] = 1
        $ clear_scene()
        $ mc.business.add_mandatory_crisis(ellie_unnecessary_payment)
    elif ellie.event_triggers_dict.get("blackmail_stage", 0) == 1:
        mc.name "I'm still working on the million dollars. For today I have the same amount as last time."
        the_person "You are testing my patience. How am I supposed to live off of $100 a week? It's your fault I got fired in the first place!"
        "This is an interesting piece of information."
        mc.name "My fault? What did I do to get you fired?"
        the_person "Those damn nanobots..."
        "She suddenly realizes she is giving away too much information."
        the_person "Forget it. Give me the money you got. Don't make me wait much longer for my money, or the good Lord help you..."
        "You hand the mysterious blackmailer $100 again. She turns and walks away."
        $ mc.business.change_funds(-100)
        $ ellie.event_triggers_dict["blackmail_stage"] = 2
        $ clear_scene()
        $ mc.business.add_mandatory_crisis(ellie_unnecessary_payment)
    elif ellie.event_triggers_dict.get("blackmail_stage", 0) == 2:
        mc.name "I've almost got the million dollars. For today I have the same amount as last time."
        the_person "I'm starting to think you are just dragging this out. I'm not going to wait forever while you get the money!"
        the_person "Being jobless sucks. My family has been asking questions about what I'm doing out here."
        mc.name "Why don't you just get another job?"
        the_person "Lordie knows I've tried! But they told me I got a non-compete..."
        "Your blackmailer gives away a bit more information. You feel like this might finally be the final piece you need to figure out her identity."
        the_person "What do you care anyway? Bunch of godless drug makers. Just give me what you got, and next week you better have it all or I'm going straight to the police!"
        "You hand the mysterious blackmailer $100 again. She turns and walks away."
        $ mc.business.change_funds(-100)
        $ ellie.event_triggers_dict["blackmail_stage"] = 3
        $ clear_scene()
        $ mc.business.add_mandatory_crisis(ellie_self_research_identity)
    else:
        "You shouldn't be here!"

    $ mc.location.lighting_conditions = standard_outdoor_lighting

    return

label ellie_self_research_identity_label():
    "Suddenly, you make a connection in your head."
    "The strange southern woman who is blackmailing you. She recently got fired, and blames you. She must work at the company you stole the nanobots from!"
    "Unfortunately, your old head researcher isn't available anymore, but you think you can remember the name of the company."
    "You run a search for local job applications looking for work, with that company as a previous employer."
    "There are a couple that come up, but one specifically immediately jumps out at you. Her picture is perfect."
    $ ellie.draw_person()
    "[ellie.name] [ellie.last_name]. Graduate of University of Alabama in Computer Science. Worked at the other company for 6 months. Looking for non-IT-related work."
    "It HAS to be her! It's just too perfect."
    "You feel conflicted about this. Surely, this is the girl that is blackmailing you... but you are also partially responsible for it, having acquired the nanobots in the first place."
    "Her previous employer must have blamed her for the leak. Now they are keeping her from finding work in her field of study with a non-compete agreement."
    "You think to yourself... she got information on you pretty easily. Your IT setup here is okay... but it could definitely be improved if you brought an expert on board."
    "Maybe you should hire her?"
    "You meet again with [ellie.fname] on Thursday night. You feel like you could definitely hire her."
    "WARNING: If you want to hire [ellie.fname], make sure you have an open employee position! You may miss the opportunity to hire her if you don't!"
    $ mc.business.add_mandatory_crisis(ellie_end_blackmail)

label ellie_end_blackmail_label():
    $ the_person = ellie
    "As night falls, you make your way downtown. Tonight you are meeting with your blackmailer."
    $ mc.change_location(downtown)
    $ mc.location.lighting_conditions = dark_lighting
    "The time comes so you head for the alley. As you approach, you hear the southern twang of her accent as she steps from the shadows."
    $ the_person.draw_person()
    the_person "'Ey. Got the money?"
    "You stop."
    mc.name "I'm going to be honest. I don't have any money with me [ellie.name] [ellie.last_name]."
    "She gasps when she hears her full name."
    the_person "That's... Oh heavens..."
    mc.name "That's right. I figured out who you are. I did my research. I found out who you used to work for. I found out what happened. That you got fired."
    $ the_person.draw_person(emotion = "angry")
    "She hesitates for a moment, then gets angry."
    the_person "That was it! I'd finally found a good job, I was working hard..."
    $ the_person.draw_person(emotion = "sad")
    "Suddenly, she breaks down crying."
    the_person "Then... they told me that I'd been stealing! That I leaked company secrets! Me!"
    the_person "They fired me... but it was you! And now I can't find another job anywhere! Anytime I give my work history, I get an instant no thanks from any employer."
    "She seems ready to chat. Do you want to try and hire her?"
    menu:
        "Hire Her":
            pass
        "Scare her off":
            "She is so emotional. You can't imagine her being a good fit for your company now."
            "You scare her off from blackmailing you using dialogue that Starbuck hasn't written yet."
            # restore default lighting before exit label
            $ mc.location.lighting_conditions = standard_outdoor_lighting
            #TODO
            #Figure out a way to remove her from the game without breaking stuff.
            # Use this: $ the_person.remove_person_from_game()
            return
    mc.name "I get it. You just want to work, and something in your field."
    the_person "I... I just moved here a year ago... I just want to do my family proud..."
    mc.name "What if you came and worked for me?"
    "She startles. She clearly had not expected this at all."
    the_person "Me? You... after I blackmailed you and..."
    mc.name "How did you get information on my company anyway? About the nanobots?"
    the_person "Oh gee, finding your involvement was the hard part. Your password security is nonexistent. I used a dictionary attack and accessed [stephanie.fname]'s emails using those stolen passwords." #BB- Even dated servers would have some kind of firewall. Having poor password policies is much more common and exploitable
    mc.name "I could really use someone with your talents to help me with stuff like that."
    the_person "I could help... but I can't... I signed a non-compete..."
    mc.name "I run a small company. We all know each other. I could make your official position be in HR, but you could run IT projects for me on the side. Your prior employer doesn't need to know."
    mc.name "I'll match your previous salary plus ten percent. And if you decide to move on, I'll give you a proper reference."
    "She seems skeptical, but agrees."
    the_person "Okay... Let's say I decide I want to try it out."
    mc.name "Come on out to the business tomorrow morning. I'll show you around, give you a chance to settle in, and then you can think about it over the weekend."
    the_person "Okay mister. I'll come out tomorrow and you can show me the ropes."
    mc.name "That's all I ask. I think you'll fit right in."
    $ the_person.set_possessive_title("Your IT Girl")
    $ the_person.set_title(the_person.name)
    $ the_person.set_mc_title(mc.name)
    $ the_person.event_triggers_dict["story_dict"] = True
    $ the_person.story_character_description ="Fired from her previous job and desperate for work, you hired [ellie.name] to be your IT lead."
    $ ellie.story_love_list = ellie_story_love_list
    $ ellie.story_lust_list = ellie_story_lust_list
    $ ellie.story_teamup_list = ellie_story_teamup_list
    $ ellie.story_other_list = ellie_story_other_list
    "You exchange some information with [the_person.title]. You feel pretty certain she'll decide to stick around."
    $ mc.business.add_mandatory_crisis(ellie_work_welcome)
    $ mc.location.lighting_conditions = standard_outdoor_lighting
    $ mc.change_location(bedroom)
    $ mc.business.set_event_day("hired_ellie_IT")
    return

label ellie_work_welcome_label():
    $ the_person = ellie
    "You head into work a bit early. You are meeting [the_person.title], who you are hoping will be your new IT girl."
    $ ceo_office.show_background()
    "Shortly after you arrive, you hear a knock on your office door."
    mc.name "Come in."
    $ the_person.draw_person()
    the_person "Hello. I'm here..."
    mc.name "[the_person.title]! I'm glad you came. I wasn't sure if you would show up or not. Please come in."
    "Sheepishly, [the_person.title] steps inside your office, walks over and sits down across from you at your desk."
    $ the_person.draw_person(position = "sitting")
    mc.name "So, basically, this is a small company, as you know. I'd love to bring you onboard and have you primarily running cybersecurity / IT projects."
    mc.name "However, I'm not sure that, due to the size of the company, I'll be able to keep you busy full time with those projects, so when you have down time, I'll assign you to the Research department."
    mc.name "We'll make the Research department your official job position, with the other projects on the side. How does that sound?"
    the_person "Well... that sounds okay, I guess. What kind of security policies do you currently have in place?"
    mc.name "Ah, well... we use the anti-virus software that came with the computers..." #BB- I changed it to this because it seems like something someone unfamiliar with network security would say
    the_person "Lordie. You don't have any kind of security measures in place?"
    mc.name "That's just something we haven't given much thought..." #BB- Network security would be an oversight for a small business
    the_person "Alright. Tell you what, I'll look things over today and I'll see what I can do. I'll do some research over the weekend and on Monday I'll let you know what I decide."
    mc.name "Deal! Why don't we get your onboarding paperwork complete?"
    the_person "Okay."
    $ the_person.draw_person(position = "sitting")
    "You sit down at your desk, filling out some paperwork and getting her officially hired by the company."
    $ mc.business.add_employee_research(the_person)
    $ the_person.set_schedule(None, the_times = [1,2,3])    # free roam when not working
    $ mc.business.add_mandatory_crisis(ellie_work_welcome_monday)
    $ mc.location.show_background()

    return

label ellie_work_welcome_monday_label():
    $ the_person = ellie
    $ ceo_office.show_background()
    "When you arrive at work on Monday morning, you head to your office."
    "Shortly after you arrive, you hear a knock on your office door. It's [the_person.title]."
    $ the_person.draw_person()
    ellie "Hello. I've been looking at things over the weekend like I told you I would."
    mc.name "Great. Have a seat."
    $ the_person.draw_person(position = "sitting")
    ellie "Alright. So, your cybersecurity is basically nonexistent. Or, was, I should say."
    mc.name "Oh?"
    ellie "Before I left Friday, I was looking at login logs for your network... the only outside connections were from me, a few weeks ago, you know, when I got the access originally..." #Another reason to switch from no firewall to poor password - the servers are auditing events which AFAIK is not enabled by default
    ellie "So I set up a quick security layer with VPN access so I could work on it from home over the weekend..."
    mc.name "That's... good?"
    ellie "Well, it means it won't be as easy for someone to log in to your network with bogus credentials like I did anymore..."
    ellie "Anyways, I spent the weekend looking at your IT systems. They are... rather outdated?"
    mc.name "Umm, honestly when I bought the place there were some systems already in place so I just decided to use those..."
    ellie "Lordie... Okay well I made a short list of some new programs I could set up for you that will help in each department."
    ellie "None of them will be miracles, but you should see decent efficiency increases. Each one will probably take me about a week to set up."
    mc.name "That sounds great."
    ellie "The other thing I looked at..."
    "She lowers her voice a little."
    ellie "I... I get it that you are using the nanobots for... fornication..."
    ellie "So I looked through those programs a bit. There are definitely some gains to be made in those programs."
    ellie "I'm not saying I agree with what you are doing with them, but the programs themselves look like you just slapped them together over a weekend or something."
    mc.name "That's... basically what we did. The head researcher had a contact who put together the programs for us over a weekend..."
    ellie "You... bless your hearts. You are lucky he didn't put in some kinda back door or tracking program in there. He was probably just lazy."
    ellie "Anyway, I think I can improve those more for you, though if I'm honest, these bots are cutting edge tech. Some improvements might need more research into the bots themselves first."
    $ mc.business.it_director = the_person
    $ mc.business.it_director.IT_tags = {}
    #$ mc.business.hr_director.HR_unlocks = {}
    $ mc.business.it_director.add_role(IT_director_role)
    ellie "First round of those would also take me about a week. After that, I'm not sure."
    ellie "So, here's the first set of things I can work on. Take a look and let me know if you want me to start on something."
    call screen it_project_screen()
    if mc.business.IT_project_in_progress:
        ellie "Okay, I have a starting point. If you decide to have me work on something else just come talk to me."
    else:
        ellie "Alright well, when you decide what you want me to work on, let me know, I'll be in research."
    ellie "You might also consider, I was chatting with some of the other girls in the research department."
    ellie "If you need an IT project done quickly, some of them might be able to help me out to get things done a bit quicker."
    ellie "But it would be extra work, so the less experienced employees may not have time."
    mc.name "I'll keep that in mind. Thank you."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] gets up and starts to walk away. You have now unlocked IT projects!"
    "Talk to your IT director to change projects when she is at work. If she is working on developing a new project, she will be in the Research Department."
    "You have also unlocked the IT Work duty for the research department. If assigned, an employee will help work on IT projects."
    $ ellie.add_unique_on_room_enter_event(ellie_never_been_kissed)
    $ mc.location.show_background()
    return

label ellie_never_been_kissed_label(the_person):  #This is Ellies 20 sluttiness event. Also kick starts all other events
    "You step into your research division. It seems that progress is going well here. To one side you see [the_person.possessive_title], working on a nanobot project."
    $ the_person.draw_person(position = "sitting")
    $ the_person.arousal = 40
    $ mc.arousal = 0
    "As you approach her, you notice she seems to be breathing heavily and her cheeks are flushed."
    mc.name "Hey [the_person.title], are you okay?"
    "You startle her and she jumps up."
    $ the_person.draw_person(position = the_person.idle_pose)
    the_person "[the_person.mc_title]! I was just... you know... working on the nanobot program..."
    mc.name "Great! How's it going?"
    the_person "How's what going?"
    mc.name "... The program..."
    the_person "ah... OH. Right. Well, it's going I guess."
    mc.name "Are you feeling okay? If you are sick and need to go home that would be quite alright."
    the_person "I'm fine, I'm just... y'know... trying to figure out the details of this darned thing."
    "She leans towards you and lowers her voice."
    the_person "I just don't understand why you all got to use them bots for making women do that, you know, fornicating."
    the_person "A woman should be keeping to herself, like she's supposed to."
    the_person "'sides, not like sex is such an amazing thing anyway."
    mc.name "Well, it isn't so much making women do something, as lowering inhibitions and giving women the chance to experience what they already want, but are afraid to experience."
    "[the_person.title] scoffs a bit at your rebuttal."
    mc.name "And as for sex not being amazing, I'd have say you probably just haven't had a competent partner yet."
    "[the_person.possessive_title] rolls her eyes."
    the_person "I don't need no partner ta know that."
    "You take a moment to evaluate your conversation with [the_person.title]."
    "From the way she is talking, the way she brushes it off, is it possible she is still a virgin?"
    "You know she grew up in religious territory..."
    mc.name "Well, I'd say you should keep an open mind. I'm pretty competent, if you ever want to put it to the test."
    $ the_person.change_arousal(10) #50
    the_person "Ha! That's something, bless your heart. I'm saving myself fer marriage, like I'd like you do something like that..."
    "Aha. You wonder if she's even done anything with someone before?"
    mc.name "There are numerous other things other than going all the way that could be done as an alternative."
    "As you look at her, you realize why she is acting funny. She's aroused! Probably from working on the nanobot code..."
    "You give her a wide, genuine smile."
    mc.name "Like I said, I'd be glad to show you. You wouldn't even have to take off any clothes."
    the_person "Hah, you're such a joker. Like I'd let you... run your hands all over me... or whatever..."
    $ the_person.change_arousal(10) #60
    $ the_person.draw_person(position = "sitting")
    "[the_person.possessive_title] sits back down at her desk, and you decide to let her keep working, but you can tell you've struck a nerve with her."
    $ clear_scene()
    "You decide to leave her alone for now. You finish inspecting the research department then head to your office."
    $ mc.change_location(ceo_office)
    "You sit down and start to work on some paperwork. You pull up some emails and get to work responding to some supply requests from logistics."
    "*KNOCK KNOCK*"
    $ the_person.draw_person()
    "You look up. [the_person.title] is standing in your door."
    the_person "Hey uh, [the_person.mc_title]..."
    mc.name "Come in, close the door, and have a seat."
    the_person "Oh uh, sure..."
    "[the_person.title] does what you ask, then sits down across from you."
    $ the_person.draw_person(position = "sitting")
    mc.name "What can I do for you?"
    the_person "Well, I was working on that bot program, but I was kinda having trouble with parts of it..."
    mc.name "What kind of trouble?"
    the_person "It was a part about making some uh, things, a bit more sensitive, for ladies I mean..."
    the_person "And I kinda realized, you know that like... for the sake of being able to code it properly, I should probably have a better idea of... you know... what it feels like..."
    "Wow, she must be have been more ready for this than you realized. You thought it would be much more difficult to seduce her!"
    mc.name "Of course, and as your boss, it only makes sense that I would want to provide you with experiences that will make you better at your job."
    the_person "Exactly! Now... you said you could show me something that... that wouldn't involve me taking off clothes or something..."
    the_person "Just to make sure we are on the same page here, NOTHING goes inside of me... right?"
    mc.name "Not if you don't want something to."
    the_person "Well, I don't. I'm no whore! Working on this program just has me curious and distracted..."
    mc.name "It's okay. It's called getting aroused, and it is perfectly natural for this to happen in response to being exposed to sexual situations."
    the_person "I... I don't think I can talk about this stuff!"
    mc.name "It's okay. Tell you what, I'm going to talk to you through everything I'm doing, you don't have to say a word. If I start doing something you don't like, just stop me."
    the_person "Okay..."
    mc.name "Stand up."
    $ the_person.draw_person(position = the_person.idle_pose)
    "[the_person.possessive_title] does so obediently. You need to be careful not to push things too far, but this could be the beginning of a very interesting relationship between you two."
    "You walk over to her. You open up your arms and pull her close to you."
    $ the_person.draw_person(position = "kissing")
    "You pull her body close to yours. You rub your hands along her back for a while, feeling her chest slowly rise and fall with deep breaths against yours."
    "You slowly start to lower your hands down her back. You feel her tense up a bit."
    mc.name "I'm going to move my hands lower. It's okay, it felt good when I rubbed your back, right?"
    "She relaxes a bit and nods quietly. She is still tense but doesn't move as you lower your hands down to her ass."
    "You slowly start to knead her curvy cheeks. They are supple and soft and feel amazing in your hands."
    the_person "Mmm..."
    $ the_person.change_arousal(5) #65
    $ mc.change_locked_clarity(20)
    "[the_person.title] lets out a little moan. She slowly relaxes further as you continue to rub and caress her rear."
    mc.name "See? Rubbing your back feels good, and rubbing down here feels a little bit better, doesn't it?"
    the_person "It does..."
    "She leans forward and relaxes more, just enjoying the touch of your hands on her body. You really need to take this slow, so you take your time rubbing for several minutes."
    "However, you won't be able to make her cum just from this. Eventually it is time to move on."
    mc.name "Alright, now I'm going to need you to turn around, so I can keep making you feel good."
    "[the_person.possessive_title] just nods. She doesn't say a word but turns around for you."
    $ the_person.draw_person(position = "walking_away")
    "You run your hands along her hips, to her front and along her belly. You get close to her so her body is right up against yours."
    mc.name "Okay, next, I'm going to touch your chest, okay?"
    the_person "You're not... gonna put our hand up my shirt... right?"
    mc.name "Not unless you want me to. It'll be just like I'm rubbing your back, but it'll feel even better, I promise."
    "[the_person.title] doesn't respond, but just waits. You know you are pushing boundaries here, so you proceed carefully."
    "You let both hands creep up her belly until they reach the bottom of her rib cage. You slide them up a bit more until you are cupping the bottom of her tits."
    the_person "Ahhhhh..."
    $ the_person.change_arousal(5) #70
    $ mc.change_locked_clarity(20)
    "You start to grope and massage her tits earnestly now, being careful to avoid her sensitive nipples. Her breathing is getting heavier and an occasional moan escapes her lips."
    mc.name "It's nice, isn't it? Doesn't it make you feel good?"
    the_person "Yeah... It's good... but weird too. It's making me all warm... down there..."
    mc.name "That is arousal building up. We want to build that up as much as we can, and it will make you feel amazing when it releases."
    the_person "I... I dunno about that, but keep doing what you're doing... it's nice..."
    "The weight of her heavy tits feels great in your hands. You really wish you could touch her flesh there, but for now you need to take things one step at a time."
    "When you feel her arousal start to plateau, you make your next move. With two fingers and a thumb, you start to knead her engorged nipples."
    $ the_person.change_arousal(10) #80
    the_person "Ah!"
    "[the_person.possessive_title] cries out and for a second her knees buckle. She catches herself, but when she straightens out, her body rubs up against yours."
    "You've been rock hard throughout this whole process, but when she straightens up her ass rubs up against you, causing you to moan."
    $ mc.change_locked_clarity(30)
    "Her body goes rigid."
    the_person "Ah! Was that... your... your thing!?!"
    mc.name "Yes, that is my penis."
    the_person "Don't you dare try and put that thing in me!"
    mc.name "Shhh, don't worry. I'm not even going to get it out of my pants. I'm just aroused too. It's okay."
    the_person "Ahh... okay..."
    "You go back to groping [the_person.possessive_title]'s big tits. You take turns kneading them and pinching her nipples."
    "[the_person.title] is starting to whimper. The poor girl is so pent up, the time to finish her off is now."
    mc.name "Okay... I'm going to touch you between your legs now. I'm not going to put my hand under any of your clothing. Is that okay?"
    "She whimpers a response, but before you touch her you want to make sure she really consents."
    mc.name "[the_person.title]? I don't want to do something you don't want me to. Do you want me to touch you the way I described?"
    the_person "Yes please... Please touch me... [the_person.mc_title]..."
    $ the_person.change_obedience(10)
    "Ahhh, she even said please! It seems she is so aroused, her resistance is breaking down."
    "Your left hand still on her tits, you move your right hand down her body and between her legs."
    "When you start to apply pressure on her cunt through her clothes, she starts to melt. Her hips move a bit on their own."
    $ the_person.change_arousal(10) #90
    $ mc.change_locked_clarity(50)
    the_person "Oh Lordie... forgive me..."
    "[the_person.title]'s hip movements have her ass rubbing up against you now. You can't help but moan a bit at the contact with the red-haired belle."
    the_person "Yer thing... it's poking me..."
    mc.name "Do you want me to stop?"
    the_person "NO! No... it's kinda nice."
    mc.name "You can move your hips a bit. It will help you control the pace to something that feels good to you, and it'll feel nice for me too."
    the_person "... okay..."
    "Instinctually, [the_person.possessive_title] starts to move her hips forward and backwards a bit, helping set a pace that feels best for her."
    $ mc.change_locked_clarity(50)
    "You can't help pushing your hips a bit up against her as well. It feels nice to have her ass against your cock."
    "You wish you just rip off the clothes between you and her and bend her over your desk, but you know she isn't ready for that yet."
    "Her moaning is getting stronger and needy. She's going to cum soon."
    the_person "[the_person.mc_title]! Something is happening... I can't... I can't stop!"
    "You pinch her nipple forcefully with one hand and grab her by the pussy with the other. She cries out as she starts to cum."
    the_person "AH! OH!"
    $ the_person.have_orgasm(the_position = "back_peek")
    $ the_person.change_slut(3, 40)
    "Her body starts to collapse so you quickly grab her with your left hand, your right hand still rubbing her pussy through her orgasm."
    "Your hand quickly starts to get damp as she cums. She sure seems to be having a juicy orgasm."
    $ the_person.draw_person(position = the_person.idle_pose)
    "As soon as she regains control of her legs, [the_person.possessive_title] pulls away from you and turns."
    the_person "Oh heavens I just... no way... I couldn't have..."
    "She quickly puts a hand down her pants and then pulls it back out. It is shining wet. Did she just... squirt?"
    mc.name "That was just..."
    the_person "OH MY LORDIE I JUST PEED... oh my I'm so sorry, I have to go!!!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] quickly turns and flees your office, flinging your door open and running away."
    $ clear_scene()
    "You aren't certain... but you think you might have just brought her to her very first orgasm, ever."
    "It has left you extremely aroused, and you are sure she is probably very confused."
    "Is she a squirter? You can't say you have much experience with girls who tend to do that. If that was her first orgasm ever, maybe she was just really pent up."
    "A sexually repressed redhead that squirts. How do you feel about that?"
    "WARNING: The next menu will change future dialogue with [the_person.title]!"
    menu:
        "Squirting is hot!":
            $ ellie.event_triggers_dict["squirts"] = True
        "Squirting is gross!":
            $ ellie.event_triggers_dict["squirts"] = False

    "You'll want to speak with her soon though, about what just happened."
    $ mc.business.add_mandatory_crisis(ellie_grope_followup)
    $ the_person.event_triggers_dict["been_fingered"] = True

    "Your encounter has left you crazy horny."
    if mc.business.head_researcher.sluttiness > 60:
        $ the_person = mc.business.head_researcher
    elif mc.business.hr_director.sluttiness > 60:
        $ the_person = mc.business.hr_director
    else:
        "Unfortunately there isn't much you can do about it now. You spend a few minutes walking around your office until your boner finally goes down, then return to work."
        return
    "You decide to call [the_person.possessive_title] to your office to take care of it."
    "*KNOCK KNOCK*"
    $ the_person.draw_person()
    the_person "Hey [the_person.mc_title], you wanted to see me?"
    "When you turn to face them, they start to laugh."
    the_person "Jesus, you look like you just left a porn convention with your hands tied behind your back. Are you okay?"
    mc.name "I will be in a few minutes, hopefully."
    the_person "Ahhh, you need me to take care of that monster for you?"
    the_person "Okay!"

    if the_person.has_cum_fetish():
        "[the_person.title] closes your office door and locks it. Then she walks over to you and drops down to her knees."
        $ the_person.draw_person(position = "blowjob")
        $ mc.change_locked_clarity(50)
        "In a flash she has your cock out."
        call fuck_person(the_person, private=True, start_position = cum_fetish_blowjob, start_object = make_floor(), skip_intro = True, position_locked = True, self_strip = False) from _call_ellie_arousal_relief_01
    elif the_person.has_anal_fetish():
        "[the_person.title] closes your office door and locks it. Then she walks over to your desk, and bends over it."
        the_person "It's been a while since you had it in my ass... why don't you just take me for a quickie?"
        "You step behind her."
        $ mc.change_locked_clarity(50)
        call fuck_person(the_person, private=True, start_position = SB_anal_standing, start_object = make_desk()) from _call_ellie_arousal_relief_02
    elif the_person.has_breeding_fetish():
        "[the_person.title] closes your office door and locks it. Then she walks over to your desk, and bends over it."
        the_person "My hungry cunt could really use a fresh load of seed... why don't we have a quickie?"
        "You step behind her."
        $ mc.change_locked_clarity(50)
        call fuck_person(the_person, private=True, start_position = bent_over_breeding, start_object = make_desk()) from _call_ellie_arousal_relief_03
    else:
        "[the_person.title] closes your office door and locks it. Then she walks over to you and drops down to her knees."
        $ the_person.draw_person(position = "blowjob")
        $ mc.change_locked_clarity(50)
        "She fumbles with your pants a bit, but eventually managed to pull your cock out."
        "She gives it a couple licks before she gets started."
        call fuck_person(the_person, private=True, start_position = blowjob, start_object = make_floor(), skip_intro = True, position_locked = True, self_strip = False) from _call_ellie_arousal_relief_04

    $ report_log = _return
    if report_log.get("guy orgasms", 0) > 0:
        "After you finish, you feel much better."
        mc.name "Thank you [the_person.title], I really needed that."
        the_person "Glad to help!"
        $ the_person.change_stats(happiness = 10, love = 5, obedience = 10)
    $ the_person.draw_person()
    $ the_person.review_outfit()
    "She smiles at you while putting her clothes back in order."
    mc.name "Alright, now get back to work."
    $ the_person.draw_person(position = "walking_away")
    the_person "Of course, [the_person.mc_title]."
    $ clear_scene()
    "After you get yourself cleaned up, you get back to work."
    return

label ellie_grope_followup_label():
    $ the_person = ellie
    "You are going about your work, when [the_person.possessive_title] finds you."
    $ the_person.draw_person()
    the_person "Hey, can we talk somewhere private?"
    mc.name "Sure."
    $ ceo_office.show_background()
    "You take her to your office and close the door. You offer to let her sit down but she declines."
    the_person "I'll keep this short, I just didn't want any other girls to hear this..."
    the_person "I'm sorry for... yah know... peeing my pants like that..."
    $ the_person.draw_person(emotion = "angry")
    the_person "But to be fair, ya'll didn't tell me something like that could happen!"
    mc.name "[the_person.title]... did it feel good? When that happened?"
    the_person "I... I guess so... yeah it was nice..."
    mc.name "[the_person.title]... I don't think you peed yourself, I think you just had an orgasm."
    the_person "I had a... a what now?"
    mc.name "[the_person.title], have you ever masturbated?"
    the_person "What the hecking kind of question is that? Of course not, that's for unsavory folk."
    $ the_person.draw_person(emotion = "sad")
    "You sigh. She is struggling in her brain to overcome her sexual desires, and being exposed to your serums is starting to overwhelm her."
    "She is making progress, but you can tell it is going to be a long road before you can fully corrupt her."
    mc.name "I tell you what. I'm going to email you some sexual health websites. I want you to do some research on things this weekend."
    mc.name "With the work we do here on serums, it is important that you have a good understanding what is actually going on with your body."
    the_person "You're saying... this is a work assignment?"
    mc.name "That's right. It will help you do your job better."
    mc.name "I'm not saying you have to masturbate, but getting to know your body better might help you better understand what we are trying to achieve here, in general."
    the_person "Okay, I'll take a look."
    $ clear_scene()
    $ mc.location.show_background()
    "[the_person.possessive_title] leaves your office. You take a few minutes and email her some links to positive sex health websites and information."
    $ mc.business.add_mandatory_morning_crisis(ellie_text_message_apology)
    return

label ellie_text_message_apology_label():
    $ the_person = ellie
    "Sunday morning, you roll over and look at your phone. You have several missed text message."
    "Looking at your phone, you see they are all from [the_person.possessive_title], at about 3 am."
    $ mc.start_text_convo(the_person)
    the_person "Sorry, I know it's late, I was just up doing research on stuff you sent me..."
    the_person "I didn't know... all this stuff about my own body. No one ever told me this stuff."
    the_person "When I was in school, I just stayed busy with schoolwork and never had a boyfriend or anything."
    the_person "Anyway, thanks for sending me this, I appreciate yer helping me out with it."
    $ the_person.change_love(3)
    $ the_person.increase_sex_skill("Foreplay", 3, add_to_log = True)

    "You decide to send her a quick text back."
    mc.name "Happy to help. Let me know if you need any further demonstrations."
    $ the_person.change_slut(2)
    $ mc.end_text_convo()
    "You lay back down for a bit. You look at your phone and see the message was read, but she doesn't reply."
    $ mc.business.add_mandatory_crisis(ellie_never_given_handjob)
    return

#Love Events

init -1 python:

    def ellie_brings_lunch_requirement():
        if ellie.love >= 40 and mc.is_at_work() and mc.business.is_open_for_business() and time_of_day == 1 and ellie.story_event_ready("love"):
            return True
        return False

    def ellie_dinner_date_intro_requirement(the_person):
        if the_person.love >= 60 and mc.is_at_work() and mc.business.is_open_for_business() and ellie.story_event_ready("love"):
            return True

    def ellie_dinner_date_requirement():
        if day%7 == 6 and time_of_day == 3:
            return True
        return False

    def ellie_lingerie_shopping_requirement(the_person):
        if ellie.story_event_ready("love") and the_person.love >= 80:
            return False
        return False

init 1 python:
    ellie_never_given_handjob = Action("Ellie wants to touch", ellie_never_given_handjob_requirement, "ellie_never_given_handjob_label")
    ellie_brings_lunch = Action("Ellie likes cooking", ellie_brings_lunch_requirement, "ellie_brings_lunch_label")
    ellie_dinner_date_intro = Action("Ellie asks for a dinner date", ellie_dinner_date_intro_requirement, "ellie_dinner_date_intro_label")
    ellie_dinner_date = Action("Ellie cooks for you", ellie_dinner_date_requirement, "ellie_dinner_date_label")
    ellie_lingerie_shopping = Action("Ellie dresses up for you", ellie_lingerie_shopping_requirement, "ellie_lingerie_shopping_label")


label ellie_never_given_handjob_label():    #20 Love event. Requires 20 slut event.
    $ the_person = ellie
    $ the_person.arousal = 0
    $ mc.arousal = 0
    "You are going about your work, when [the_person.possessive_title] finds you."
    $ the_person.draw_person()
    the_person "Hey, can we talk somewhere private?"
    mc.name "Sure."
    $ ceo_office.show_background()
    "You bring her to your office. After stepping inside, she closes the door and locks it."
    mc.name "Have a seat?"
    the_person "Yes sir."
    $ the_person.draw_person(position = "sitting")
    mc.name "What can I do for you?"
    the_person "Are blue balls real?"
    "Wow she is getting right to the point. You have to smile at the way she pronounced blue though."
    mc.name "Wow, umm... yeah, yeah they are."
    the_person "And... and they hurt?"
    mc.name "Yeah, they can, I guess it depends on the situation..."
    the_person "The... other day... when you touched me? Did you get turned on too?"
    mc.name "Yes, it was very hot getting you off with my fingers..."
    the_person "When... when I ran oft... did you get..."
    "She lowers her voice to a whisper."
    the_person "Blue balls?"
    "You stifle your laughter."
    mc.name "Umm, maybe a little bit, but I wouldn't worry about..."
    the_person "So you got me off, for nothing in return? And it actually hurt you?"
    if the_person.has_taboo("touching_penis"):
        the_person "Can... can I try? I want to try something I read about."
        mc.name "Well, I might be up for that, but it depends on what exactly you have in mind."
        the_person "I mean, since then, I've seen all kinds of methods... but I think I can just use my hand... right?"
        mc.name "[the_person.title], are you saying you want to give me a handjob?"
        the_person "Eh!? I mean, you make it sound so dirty, I just..."
        "She is kind of cute when she gets disgruntled."
        the_person "I just want us to be even, okay? I hate the thought of leaving your poor thing all pent up..."
        "You keep quiet about the fact that you've had multiple releases since the incident."
        mc.name "Well I think that's great. I would love to have a nice handjob right now."

    else:
        the_person "Do... do you want me to do that thing, with my hand again?"
        mc.name "I would love a nice handjob right now."
    $ the_person.change_slut(2, 40)
    the_person "Geesh, you don't have to keep saying that..."
    mc.name "Why? I mean, it's what you call it. It's okay, say it. Tell me what you want me to do."
    "[the_person.possessive_title] takes a deep breath."
    the_person "[the_person.mc_title], can I give you a handjob?"
    mc.name "... and?"
    the_person "Wha? and?"
    mc.name "What do you say when you are asking your boss for something?"
    $ the_person.change_obedience(5)
    the_person "Ah... geesh. [the_person.mc_title], can I give you a handjob, please?"
    mc.name "Great! Yes that would be perfect right now."
    "You stand up and walk over to [the_person.title]. She looks up at you from her chair."
    the_person "I... can you get it out?"
    mc.name "Oh, I think it would be a good idea to make this more... educational. Why don't you give it a try?"
    $ the_person.change_arousal(5)
    the_person "Okay [the_person.mc_title]..."
    "Her hands have a little bit of a shake, but she slowly brings them up to your pants."
    mc.name "There you go, now just rub your hands along my pants until you find it."
    "She does as you order, and is soon rubbing her hand up and down your cock through your pants."
    $ mc.change_arousal(5)
    mc.name "Mmm, that's it... now pull down the zipper carefully..."
    "[the_person.possessive_title] pulls the zipper down, then pushes her fingers into your pants."
    "She keeps rubbing your dick with her hand now, but gets confused when she tries to figure how to get it out of your underwear."
    the_person "Isn't... isn't it just supposed to... pop out or something?"
    mc.name "Nope! Thank goodness! There's another hole in the fabric, usually on the side..."
    "She fishes around for several more seconds, but finally finds it."
    mc.name "Now back the other way..."
    "Finally, she gets her hand through. And for the first time in her life, she is holding a dick."
    $ mc.change_locked_clarity(20)
    $ the_person.change_arousal(10) #15
    $ the_person.break_taboo("touching_penis")
    the_person "Oh my stars... it's so warm! And hard!"
    "She starts to stroke you a bit, but having her hand through your pants and underwear makes it hard for her to move."
    "She struggles a bit more but finally manages to pull it out."
    the_person "Oh! It's so big! I... I thought people were exaggerating on the internet..."
    the_person "This thing is supposed to..."
    "She suddenly closes her legs."
    mc.name "Not yet. For now, just give it a couple strokes with your hand."
    $ the_person.change_obedience(2)
    "[the_person.possessive_title] grabs you with her hand and gives you a few slow strokes. Her grip is way too hard."
    mc.name "Gentle now. Think about how soft your vagina is. Try and replicate that with your hand."
    the_person "Ah! Sorry..."
    "[the_person.title] gives you a few softer strokes now. They are much more pleasant."
    $ the_person.increase_sex_skill("Foreplay", 4, add_to_log = True)
    $ mc.change_locked_clarity(20)
    $ the_person.draw_person(position = "blowjob")
    "[the_person.title] gets down on her knees next to you, watching you very closely as she starts her first ever handjob."
    "Thankfully, her hand is very soft as she strokes you off, and the taboo of defiling this southern belle makes it even hotter."
    the_person "One of the things I read about... boys like it when they have something to look at, right?"
    mc.name "That's true."
    the_person "Would you like to... see my boobies?"
    mc.name "I would love to see your titties. Get them out for me [the_person.title]."
    the_person "Ah, okay [the_person.mc_title]."
    $ the_person.strip_to_tits(position = "blowjob")
    $ mc.change_locked_clarity(30)
    $ the_person.change_arousal(5)
    "Her tits now out for your viewing pleasure, this little session is going great. When she looks back at your dick there is a little pre-cum leaking from it."
    the_person "Ah! It's got stuff coming out!"
    mc.name "Yeah, that is pre-cum. It starts to come out a little bit when I get really turned on."
    mc.name "Don't worry, it doesn't hurt you. Keep going, this feels great."
    "Slowly, [the_person.possessive_title] reaches out and starts to stroke you again. The pre-cum helps, but you wish there was more moisture."
    mc.name "How are you doing, are you getting turned on?"
    the_person "Yeah."
    mc.name "Are you getting wet?"
    the_person "I errm..."
    mc.name "Are you?"
    the_person "Yeah [the_person.mc_title]."
    mc.name "Feel how dry my dick is?"
    the_person "Errr... yeah... it is dry."
    mc.name "I would feel even better if there was more moisture, like what your body is making now."
    the_person "[the_person.mc_title], you can't stick it in there! I'm... that's not..."
    mc.name "That's not what I mean. Let me see your hand."
    the_person "Okay?"
    "You take her hand and bring it up to your mouth. You get a big bit of saliva and spit it into her hand."
    mc.name "Now keep going."
    the_person "Ohhh... okay..."
    $ mc.change_locked_clarity(30)
    $ the_person.change_arousal(5)
    "She resumes stroking you now, and the sensations are much more pleasant. When her hand gets a little dry, she gets the idea and spits into her own hand before resuming."
    "This is turning into an almost acceptable handjob. She might actually be able to get you off."
    mc.name "That's it. Just keep it wet."
    the_person "Got it..."
    "[the_person.title] is watching you closely as she strokes your cock. When she notices it getting dry again, she leans forward for a moment..."
    "You almost think she might actually put it in her mouth... but unfortunately she lets a large glob of saliva drip from her mouth to your erection."
    "She starts stroking again, and with her spit it actually feels really good..."
    "You look down at the busty red head as she strokes you off..."
    "You feel her breath on your skin as she keeps going. You stand and just enjoy the sensations."
    "She re-wets your cock a couple more times, and soon the sensations are really ramping up."
    mc.name "[the_person.title]... I'm going to cum soon..."
    the_person "Oh god, I read about this... okay..."
    "[the_person.possessive_title] keeps stroking you, clearly with no idea what is really about to happen, her face just inches from your cock."
    mc.name "Oh fuck don't stop... don't stop!"
    $ the_person.cum_on_face()
    $ the_person.draw_person(position = "blowjob")
    $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_person)
    "You start to blow your load right onto [the_person.title]'s face. She flinches with each shot, but dutifully keeps stroking you."
    "Spurt after spurt erupts onto her. When you finish, you look down and admire her handywork."
    the_person "Wow... I... that..."
    "She struggles to get a sentence out. Now might be a good time to encourage her..."
    menu:
        "Encourage Her.\n{color=#ff0000}{size=18}Increases love{/size}{/color}":
            mc.name "That felt amazing. Thank you so much [the_person.title]."
            the_person "I... yeah... felt good then?"
            mc.name "Very much so."
            $ the_person.change_love(3)
        "She looks hot.\n{color=#ff0000}{size=18}Increases sluttiness{/size}{/color}":
            mc.name "Fuck, you look so hot like that, covered in my cum."
            the_person "You like it... yeah?"
            mc.name "Definitely. Maybe next time I'll cover your tits too."
            the_person "Oh my... next time?"
            $ the_person.change_slut(3, 60)
        "Make her taste it.\n{color=#ff0000}{size=18}Increases obedience{/size}{/color}":
            mc.name "That's a good girl. Now why don't you lick your fingers clean and give it a taste."
            the_person "Do girls really... do that?"
            mc.name "All the time. Go on."
            "[the_person.title] slowly brings her fingers to her mouth, then licks your cum off them."
            "She grimaces for a second."
            the_person "Oi, that is pretty salty..."
            mc.name "It's an acquired taste. Don't worry, you'll get used to it."
            $ the_person.change_obedience(3)
    $ the_person.draw_person()
    "[the_person.title] stands up."
    the_person "Do you think we should do that again sometime?"
    mc.name "I would certainly like to."
    the_person "Yeah... me too. But I think I'm gonna go find the lady's room..."
    mc.name "Of course. I won't hold you up any longer."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] turns and starts walking out of your office. You watch her hips as she moves away."
    "You are a bit surprised how quickly she has opened up to you like this. Maybe she is more ready to move past her repressed childhood than you realized?"
    "Either way, you are certain there is more fun to be had with the busty redhead soon."
    $ clear_scene()
    #Load up the three story branches
    $ the_person.add_unique_on_room_enter_event(ellie_never_tasted_cock)
    $ mc.business.add_mandatory_crisis(ellie_brings_lunch)
    $ ellie.set_event_day("obedience_event")
    $ ellie.set_event_day("love_event")
    $ ellie.set_event_day("slut_event")
    $ ellie.set_event_day("story_event")
    $ mc.business.add_mandatory_crisis(ellie_tit_fuck)
    # Link to her team up scenes here also?
    return

label ellie_brings_lunch_label():   #40 love scene. Brings MC lunch to have a date in his office.
    if ellie_has_brought_lunch_date():  #I left a scenario in game where this could occur twice. IF this event has already occurred, just exit immediately.
        return
    $ the_person = ellie
    $ ellie.event_triggers_dict["brought_lunch"] = True
    $ ellie.story_event_log("love")
    "It's the end of the morning shift. You finish up with your work and are just getting ready to head to the breakroom for lunch."
    $ the_person.draw_person()
    the_person "Hey. Doing anything for lunch?"
    mc.name "Ah, hello [the_person.title]. Not in particular, I think I brought some instant noodles I was going to warm up."
    $ the_person.draw_person (emotion = "happy")
    the_person "Good! I got up early this morning and made a few things to bring in... I was wondering if you wanted t'eat with me?"
    mc.name "Oh, that is very kind of you. You enjoy cooking?"
    the_person "Oh, I do! It's hard, I can't find my favorites from growing up around here, so I have to make them myself."
    $ the_person.discover_opinion("cooking")
    the_person "But thankfully I've always loved cooking."
    "It was very kind of her to bring you some food. She has started to get affectionate with you, so you decide to ask if she wants to eat in private."
    mc.name "Want to eat in my office? We could chat a bit and wouldn't be disturbed."
    the_person "Oh! That sounds nice. Like a... errr..."
    mc.name "Like a lunch date?"
    the_person "Oh, yeah... I guess that is kind of silly..."
    mc.name "Oh? I quite like the sound of it. A lunch date sounds great."
    $ the_person.change_love (2, 60)
    the_person "Ah! Let me go get my stuff from the breakroom, I'll meet your at your office [the_person.mc_title]."
    $ clear_scene()
    $ ceo_office.show_background()
    "You head to your office. You wait a few minutes and soon [the_person.possessive_title] arrives."
    $ the_person.draw_person()
    the_person "Knock knock!"
    "[the_person.title] steps into your office and closes the door behind her. She brings over a container filled with food. It smells amazing."
    $ the_person.draw_person(position = "sitting")
    the_person "If there's anything you don't like, don't worry, just pick it out, I won't be offended."
    "You look down. A healthy portion of macaroni and cheese, ham slices, something fried?... and some fresh green beans."
    mc.name "Wow, [the_person.title], this looks delicious. These are?"
    the_person "Fried tomatoes! It's hard to get good tomatoes around here, but these'll do."
    "You take a few bites. The food is all homemade and tastes delicious."
    $ the_person.change_happiness(2)
    "You dig in and start eating. You look up and notice [the_person.title] smile a bit when she sees you enjoying her cooking."
    "She picks up a fork and starts eating with you."
    "When you are about halfway through your food, you realize you haven't said a word since you started eating."
    "You slow down and start to chat with her."
    call date_conversation(the_person) from _call_date_conversation_ellie_01
    "As you finish up with your meal, you look across the desk at [the_person.possessive_title]."
    "It was very kind of her to make this food for you, you want to make sure she knows that you appreciate it."
    mc.name "[the_person.title], that was amazing. Thank you so much for the meal."
    the_person "Oh, of course. I enjoyed making it, and being able to spend some time here with you."
    if ellie_has_given_blowjob():   #WE've already done the blowjob scene. Go straight to eating her out as thanks.
        "There is significant sexual tension in the air. You consider if you should take things with [the_person.title] further..."
        menu:
            "Eat her out":
                mc.name "I think it's time for dessert."
                the_person "Dessert? Oh, I didn't bring any... I could go get a candy bar from the machine..."
                mc.name "That won't be necessary. I have something else in mind."
                the_person "Oh?"
                "You notice some blush in her cheeks as she begins to realize you have something sexual in mind."
                mc.name "Last time you were in my office, you got to have dessert. I think it is my turn this time."
                mc.name "I want you to sit on my desk."
                "You get up and walk over to your office door and lock it. When you turn back, [the_person.title] has gotten up on your desk."
                call ellie_cunnilingus_office_label(the_person) from _ellie_lunch_date_dessert_ending_01
                $ the_person.draw_person (position = "missionary")
                "You stand up, leaving [the_person.possessive_title] on your desk, panting."
                the_person "That... was that like, how it made you feel? You know, when I sucked on yours?"
                mc.name "Probably not exactly the same, but similar, yes."
                the_person "Stars... [the_person.mc_title] I owe you... maybe if I practice I can do that as good to you as you did it to me..."
                mc.name "Of course. I'm going to get back to work now. You can recover for a bit if you want before getting back to work."
                the_person "Yes sir..."
                $ clear_scene()
                "You step out of your office, leaving [the_person.possessive_title] to recover. You head to the restroom and clean up your face before returning to work."
            "Finger her":
                mc.name "I think it's time for dessert."
                the_person "Dessert? Oh, I didn't bring any... I could go get a candy bar from the machine..."
                mc.name "Don't bother. I have something else in mind. Would you stand up please?"
                "As [the_person.possessive_title] stands up, you walk around behind her..."
                $ the_person.draw_person(position = "back_peek")
                "You let your hands start to roam all over the busty redheads body."
                "She flinches at first, still not used to your touch, but quickly leans back and begins to enjoy it."
                mc.name "Let me show you how thankful I am for that delicious meal."
                the_person "Ahh, okay... do you want you want then..."
                call fuck_person(the_person, private=True, start_position = standing_finger, skip_intro = False) from _call_ellie_post_lunch_finger_01
                $ the_report = _return
                if the_report.get("girl orgasms", 0) > 0:
                    "[the_person.possessive_title] is breathing heavy, recovering from her orgasm."
                    the_person "Mmm, that was good. I think I need a minute..."
                mc.name "I'm going to get back to work now. You can recover for a bit if you want before getting back to work."
                the_person "Yes sir..."
                $ clear_scene()
                "You step out of your office, leaving [the_person.possessive_title] to recover. You head to the restroom and clean up your face before returning to work."
    else:
        "There is some tension in the air... but you decide for now it would be better not to act on it."
        mc.name "Yes, it was great. Thank you again."
        "You stand up and [the_person.title] does the same."
        $ the_person.draw_person()
        "You leave your office together and go back to the work day."
    $ ellie.story_event_log("love")
    $ ellie.apply_planned_outfit()
    $ ellie.add_unique_on_talk_event(ellie_dinner_date_intro)
    $ clear_scene()
    $ mc.location.show_background()
    return

label ellie_cunnilingus_office_label(the_person):
    $ the_person.draw_person (position = "sitting")
    $ the_person.arousal = 0
    "You walk over to [the_person.title]. You can see her trembling slightly as you get close."
    mc.name "[the_person.title], I am going to eat you out now. Are you okay with that?"
    the_person "[the_person.mc_title], isn't that kind of gross?"
    mc.name "Nonsense. You already got to taste me. It's only fair I get to return the favor!"
    if the_person.vagina_available():
        mc.name "Now, go ahead and scoot to the end of the desk and open your legs. I want to see your beautiful cunt."
        "[the_person.possessive_title] obeys, but blushes in embarrassment at your words."
        $ the_person.change_slut(2, 60)
    else:
        "You slowly remove her bottoms. She doesn't resist and lets you strip her down."
        $ the_person.strip_to_vagina(position = "sitting")
        "Once exposed, you pull her to the edge of your desk and urge her legs apart."
    $ the_person.draw_person(position = "missionary")
    $ mc.change_locked_clarity(50)
    "You kneel down and look closely. [the_person.possessive_title]'s fresh, virgin cunt is inches away."
    "You are certain that you are the first person to do this with her, and it is really turning you on."
    the_person "You... you just gonna look mister?"
    "The nervous edge in her voice is so cute. You decide not to respond, instead you lean forward the last couple of inches."
    "You stick out your tongue and run it up and down her slit, just barely touching it."
    $ the_person.break_taboo("licking_pussy")
    the_person "Ah! Oh my..."
    $ the_person.change_arousal(10)
    "You slither you tongue inside of [the_person.title]'s pristine pussy. You take your time and explore her crevice."
    "Her smell and taste is musky but with a hint of vanilla. Your tongue travels all up and down her slit, although you purposefully detour around her clit."
    $ the_person.change_arousal(10)
    "Curious about her taste at the source, you snake your tongue down to her entrance proper. You tongue smoothly pushes slightly into her virgin hole."
    "The opening is so tight you can barely fit your tongue, but she moans at the intrusion."
    the_person "Ohhhh... that's so good..."
    $ the_person.change_arousal(20)
    "You feel her soft hand settle gently on your head as she gives in to the pleasure you are giving her."
    "You slide your tongue inside of [the_person.possessive_title]'s cunt as far as you can reach."
    "You swirl it around, enjoying all the soft sensations and tastes of her pussy."
    $ the_person.change_arousal(20)
    "So far, you've stayed away from her clit, but it is time to push her into the final stretch. You pull your tongue from her hole and then lick your way up her slit."
    the_person "Mmm, that was so... OH!"
    "You circle [the_person.title]'s clit once, the slide your tongue across it. Her back arches and the hand on the back of your head suddenly grabs your hair."
    "You slide it across again and again, each time with slightly increasing pressure. Then her hips begin to move with you."
    $ the_person.change_arousal(25)
    the_person "Stars, I can't... [the_person.mc_title]!"
    "Lapping eagerly at her clit, you run your hands along her stomach, down her legs and the insides of her thighs."
    "Her back arches and she moans loudly as she gets ready to cum."
    $ the_person.change_arousal(25)
    the_person "!!!!!!!"
    "The hand on the back of your head grabs your hair and pulls you closer. You can feel her legs wrap around your back as she starts to cum."
    $ the_person.have_orgasm(the_position = "missionary", half_arousal = True)
    $ mc.change_locked_clarity(50)
    $ the_person.increase_opinion_score("getting head", max_value = 1)
    if ellie_is_a_squirter():
        "Suddenly, your whole face is soaked in [the_person.possessive_title]'s juices. As her body writhes in pleasure, she squirts a bit with every wave."
        "You keep your attention on her clit, enjoying getting her off with such a strong orgasm."
    else:
        "[the_person.possessive_title] writhes in pleasure as she cums."
        "You keep your attention on her clit, enjoying getting her off with a strong orgasm."
    the_person "That... that was amazing..."
    menu:
        "Keep going" if mc.sex_skills["Oral"] >= 3:
            pass
        "Keep going \n{color=#ff0000}{size=18}Requires better oral skill{/size}{/color} (disabled)" if mc.sex_skills["Oral"] < 3:
            pass
        "Get up":
            "You look up from between [the_person.possessive_title]'s shapely legs and smile."
            mc.name "I suppose that is enough for now."
            return
    "{i}You haven't seen anything yet,{/i} you think to yourself. You give her a few moments to catch her breath, then begin licking at her slit again."
    the_person "Mmm... that's nice... I... you can stop..."
    "You bring your face away from her body for a second to say a single word."
    mc.name "No."
    "Her legs tremble slightly when you return to your work, licking at her sopping cunt."
    the_person "No? Wha... but dun... OH..."
    "You flick your tongue across her clit again, and suddenly she feels the spark of more arousal."
    $ the_person.change_arousal(10) #65
    $ the_person.change_obedience(5)
    "The hand on the back of your head is trying to pull you away now, but you easily fight it. Now instead of pressure, you flick your tongue across her clit in various rhythms and directions."
    "After experimenting some, you find a good rhythm and can feel her hips start to respond to your continuing licking."
    $ the_person.change_arousal(15) #80
    the_person "Buh... I read about... but I didn't think... more than once..."
    "You put both hands under her ass and grope her pliant cheeks. The hand on your head relaxes now, and [the_person.title] is having trouble forming sentences."
    the_person "Ah, stars! [the_person.mc_title]... keep... ah! I'm... YES!"
    $ the_person.change_arousal(15) #95
    "Legs start to wrap around your back again, and the hand on your head is pulling you closer. This seems to be a pattern for her as she gets ready to cum again."
    "As your finishing move, you latch onto her clit with your lips and start to lightly suckle on it. Her back arches and her cries grow urgent."
    the_person "[the_person.mc_title]! I'm... yer gonna!!! AH!"
    $ the_person.change_arousal(25) #120
    "Her body seizes as another orgasm hits her. Loud panting and moaning, and then suddenly release."
    $ the_person.have_orgasm(the_position = "missionary", half_arousal = True)
    $ mc.change_locked_clarity(50)
    $ the_person.increase_opinion_score("being submissive", max_value = 2)
    if ellie_is_a_squirter():
        "Another round of fluid erupts from her depths as she cums. She is making an absolute mess of your desk and your face, but you don't care."
        "Your mouth stays latched to her clit you push her through her second orgasm."
    else:
        "[the_person.title] is trying in vain to move her hips with you, but she has lost the ability to do any more than twitch now and then."
        "Your mouth stays latched to her clit you push her through her second orgasm."

    the_person "That... STARS... I never thought that... was possible..."
    the_person "You umm... yer done... right?"

    menu:
        "Not a chance" if mc.sex_skills["Oral"] >= 6:
            pass
        "Not a chance \n{color=#ff0000}{size=18}Requires better oral skill{/size}{/color} (disabled)" if mc.sex_skills["Oral"] < 6:
            pass
        "Done":
            "You look up from between [the_person.possessive_title]'s shapely legs and smile."
            mc.name "I suppose that is enough for now."
            return
    the_person "'Not a chance'? Seriously??? I can't... AH!"
    "Your mouth latches on to her clit again. Now you are alternating between hard and soft suckling as her body begins to respond again."
    $ the_person.change_arousal(10) #70
    "[the_person.possessive_title]'s body is responding to your tongue, but you know that this time you'll need to use more than just that."
    "You take a break from suckling her clit for a moment and lick her slit up and down. Then you bring your index up and push it up against her virgin hole."
    the_person "That feels good, but I'm not sure that I can do this again [the_person.mc_title]..."
    "Well, you'll be damned if you're not going to try anyway. With slow, gentle pressure, you push your finger into her incredible tight hole."
    the_person "Ah... Ohhh my..."
    "You manage to get it all the way in, but there isn't much room to work with. You turn your hand so your palm is facing up, and start to move it with a slow come-hither motion."
    $ the_person.change_arousal(10) #80
    "As you stroke her, you soon find the little g-spot in the front of her vagina and start to massage it with your finger. Her moans are starting to turn into growls."
    the_person "Agghghh... what is... ahhhhh. Maybe if you... aggghhhh..."
    "You continue to stroke and can feel her hips moving again. You lick her clit a few times now, and then start to suckle it again."
    $ the_person.change_arousal(15) #95
    "Your skillful assault on [the_person.possessive_title]'s body is paying off. She is writhing from your touch and her legs wrap around your back even more urgently now."
    the_person "I'M!... HOW IS THIS!?! [the_person.mc_title]??? I'M GONNA GO AGAIN!"
    "That's your cue. Thankfully [the_person.title] is very vocal, so it is easy to gauge when it is time to focus."
    "You suckle her clit urgently now, and your finger strokes her silky insides as her entire body begins to tremble."
    $ the_person.have_orgasm(the_position = "missionary", half_arousal = False)
    $ mc.change_locked_clarity(50)
    $ the_person.increase_opinion_score("getting head", max_value = 2)
    if ellie_is_a_squirter():
        "A third round of fluid is ejaculated forcefully as she cums. Her juices are now running down the side of your desk."
        "Your hand and face are soaked, but you focus your efforts and coax her through a third orgasm."
    else:
        "[the_person.title] lets out a moan as her body has a third powerful orgasm."
        "Your skillful mouth and finger guide her through it."
    "When she finishes, her body goes limp."
    the_person "Stop! You have to stop! I can't... I might die!"
    "You release her body and chuckle from between [the_person.possessive_title]'s shapely legs."
    the_person "Wha? I'm not joking! I'll have like... a heart attack or something!"
    "You can't help but laugh. She smacks your shoulder but doesn't have the strength to put any real force into it."
    return

label ellie_dinner_date_intro_label(the_person): #Ellie invites MC over for dinner
    $ the_person.draw_person(position = "sitting")
    "You walk into the research lab. You notice [the_person.possessive_title], sitting at her station and getting some work done."
    "Recently, you have grown a bit fond of the southern redhead. Something about her innocence has made your playtime fun."
    "You decide to go see how she is doing. You walk over to her desk."
    mc.name "Hey [the_person.title]. How's it going over here?"
    "She looks up from her work and smiles."
    the_person "Oh hey [the_person.mc_title]. I was hoping I would see you today."
    mc.name "Oh? And why is that?"
    the_person "I know you know this, but, I love to cook. I was thinking about making up something and thought maybe you'd like to come over and have dinner with me?"
    mc.name "Dinner? At your place?"
    the_person "Yeah, pretty much. I was thinking maybe Sunday night if it isn't any trouble for you."
    "Apparently [the_person.possessive_title] has been enjoying your time together, also. The chance to be alone with her, at her place, could make for some interesting opportunities."
    if ellie_has_given_virginity():
        "You can hardly forget how hot it was, when you took her virginity. It appears she is enjoying her new found sexuality also."
    else:
        "You wonder if this might be the opportunity you finally need to deflower the busty redhead..."
    mc.name "That sounds great. Sunday night. I'll bring a bottle of wine?"
    the_person "Oh, you don't have to bring anything, but if you really want to that would be sweet of you."
    mc.name "Sunday night then."
    $ clear_scene()
    "You step away from [the_person.title]'s desk. Sounds like you have a dinner date Sunday!"
    $ mc.business.add_mandatory_crisis(ellie_dinner_date)
    return

label ellie_dinner_date_label():
    $ the_person = ellie
    $ ellie.event_triggers_dict["dinner_date"] = False
    $ ellie.story_event_log("love")
    "It is Sunday night. You have a dinner date with [the_person.title] tonight. You shoot her a text and she sends you her address."
    "You swing by a store on the way there and pick up a bottle of mid range red wine. The make your way to her place."
    "Soon, you are at the front door to her apartment, knocking on her door."
    $ the_person.learn_home()
    $ the_person.draw_person()
    the_person "Ah! You're here! Come in!"
    $ mc.change_location(the_person.home)
    "When you step inside, you are immediately assaulted by number of heavenly smells."
    mc.name "Oh my god. It smells amazing in here."
    the_person "Ah, thank you! I made up some jambalaya and cornbread. Dessert is still in the oven but I hope you like peach cobbler..."
    "Your mouth is watering. This girl can cook!"
    mc.name "That sounds incredible. Here, I brought this."
    "You hand her the bottle of wine. She takes it and sets it on the counter."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.title] starts working on portioning out some food. You walk up behind her and wrap your arms around her stomach. She sighs."
    the_person "Ah it's almost... almost ready..."
    "You kiss her on the neck a bit, running one hand up her stomach and up to her generous chest..."
    $ the_person.change_arousal(10)
    $ the_person.draw_person(position = "back_peek")
    the_person "Ahh... sit yourself down... I didn't make this soup for nothing!"
    "Reluctantly, you let her go, then sit down at her table."
    $ the_person.draw_person(position = "sitting")
    "[the_person.possessive_title] finishes putting out food, then sits down beside you."
    "You dig in to the jambalaya. It has considerable heat, but tastes amazing."
    "As you eat, you make some small talk with [the_person.title]. However, you can feel sexual tension building throughout the meal."
    "At one point, you feel [the_person.possessive_title]'s foot next to yours, and she slides it up and down the side of your legs a couple times."
    "A buzzer goes off in the kitchen."
    the_person "Ah! The cobbler should be done! Let me go pull it out..."
    $ the_person.draw_person(position = "walking_away")
    "Last time anyone says that tonight..."
    "She jumps up and heads back to the kitchen. You watch her as she walks away from the table."
    $ the_person.draw_person(position = the_person.idle_pose)
    "In a few minutes, she re-emerges with two bowls of peach cobbler with a scoop of vanilla ice cream."
    "She sets one down next to you, then sits down."
    $ the_person.draw_person(position = "sitting")
    the_person "This is one of my favorites. My momma made this for me when I was growing up."
    "You take a bite. The peaches and ice cream meld together into a savory dessert."
    mc.name "Wow... this is really good..."
    "You dig in, barely saying a word as you down it."
    "You finish the last bite of your peach cobbler. You look up at [the_person.possessive_title]. There is an obvious tension in the air."
    if ellie_has_given_virginity():
        "Note from the author. You have already had sex with [the_person.title]."
        "However, you can reset her virginity status now to experience this part of the story as if it were her first time."
        "Would you like to experience this event as if she is still a virgin?"
        menu:
            "Yes. Take her virginity (again)":
                $ restore_virginity(the_person)
            "No.":
                pass
    if ellie_has_given_virginity():
        "You decide it is time to make your move. You get up from your chair and walk around to [the_person.title]."
        the_person "Ah, what are you coming over here for AH."
        "You pick her up roughly and she clings to you."
        $ the_person.draw_person(position = "against_wall")
        mc.name "Which way to the bedroom."
        the_person "Back there!"
        "She points to her bedroom door. You quickly open up and maneuver her through it, then throw her down on the bed."
        $ the_person.draw_person(position = "missionary")
        the_person "I know you aren't the typical romance type... but once in a while it is nice to do things the old fashioned way!"
        mc.name "Don't worry. What we are about to do is VERY old fashioned."
        "You decide to get her naked before you go any further."
        mc.name "Let's get these pesky clothes off you now, [the_person.title]."
        $ the_person.strip_outfit(position = "missionary")
        "You look down at [the_person.possessive_title]. Time to get some."
        call fuck_person(the_person, private = True) from _call_sex_description_ellie_after_dinner_encore_01
        $ had_sex = True
    else:
        mc.name "Thank you [the_person.title]. That was delicious."
        the_person "Aww, it was nothing..."
        "She scoops the last of her dessert from her bowl, finishing it off."
        the_person "You ummm... want some coffee or something?"
        mc.name "Not particularly, but I'm also not ready to leave yet."
        the_person "Well umm, I just realized, I hadn't give you a tour of the place yet..."
        "She looks around."
        the_person "I mean... it's just an apartment but ummm..."
        mc.name "Well I wouldn't mind seeing the inside of the bedroom."
        $ the_person.change_arousal(5)
        the_person "Oh! That's a great idea..."
        $ the_person.draw_person(position = "walking_away")
        "You get up and follow [the_person.possessive_title] into her bedroom."
        $ the_person.bedroom.show_background()
        $ the_person.draw_person(position = the_person.idle_pose)
        the_person "This is it... this is where I..."
        "Her voice drifts off as you close in on her."
        $ the_person.draw_person(position = "kissing")
        "You both wrap your arms around each other. Your tongues meet and you eagerly make out."
        $ the_person.change_arousal(5)
        $ mc.change_arousal(5)
        "You reach behind her and grab her ass. She gives a little moan as you start to knead it."
        "You grab her ass with both hands now and roughly lift her up."
        $ the_person.draw_person(position = "against_wall")
        the_person "Mmm... oh [the_person.mc_title]..."
        "[the_person.possessive_title] wraps her legs around you. Your cock is now nestled between her legs as she rubs herself against you."
        "You walk forward to her bed and then fall forward onto it."
        $ the_person.draw_person(position = "missionary")
        $ the_person.change_arousal(15)
        $ mc.change_arousal(15)
        the_person "Oh stars, you make me feel so good [the_person.mc_title]..."
        "You stop making out for a second, and she looks into your eyes."
        the_person "Will you... you know..."
        "She leaves her question unasked."
        mc.name "No... I don't know. What do you want?"
        the_person "I... I want you, [the_person.mc_title]..."
        the_person "I know it sounds crazy, but I can't stop thinking about you. I know you may not feel the same way but... I want my first time to be with you."
        "Yes! It is finally time to take [the_person.title]'s cherry."
        mc.name "[the_person.title]. If you are certain, I would be proud to be your first."
        the_person "I am. I know the first time is gonna hurt... but it's okay. I want you to take me, and don't stop until you finish, okay?"
        mc.name "Alright. If you're sure. But first, you're wearing way too many clothes..."
        "You quickly start to peel off all of [the_person.possessive_title]'s clothing."
        $ the_person.strip_outfit(position = "missionary")
        "Once she is naked, you quickly strip down yourself, then take a moment to admire the busty redhead beneath you."
        "It isn't every day you get to take a woman's virginity, so you want to savor this."
        mc.name "Do you... want me to wear a condom?"
        "[the_person.title] shakes her head."
        the_person "I know I should... but for my first time... I want to experience everything..."
        mc.name "Are you on birth control?"
        the_person "No... I... I never thought I would need to..."
        mc.name "Do you understand... it is possible that you could get pregnant?"
        the_person "Yes... I understand."
        "Fuck! Looks like it is up to you. Are you going to go into this raw?"
        menu:
            "Put on a condom":
                $ mc.condom = True
                mc.name "I'm sorry, but I don't trust myself to pull out, and I'm not quite ready to take that chance."
                the_person "I understand. Take me how you want."
                "You reach over to your pants, grab your wallet and quickly pull out a condom. You quickly slide it on."
            "Go bareback":
                mc.name "The odds are pretty slim... but it is possible that I won't be able to pull out in time."
                the_person "I know. I kind of want to know what it is like... to feel it... I mean..."
                "[the_person.possessive_title] blushes with the last of her words."
                $ the_person.increase_opinion_score("bareback sex")
                $ the_person.increase_opinion_score("creampies")
        "You get into position on top of her. She spreads her legs wide and puts her hands on your back."
        $ the_person.change_arousal(15)
        mc.name "Alright, last chance to back out. After this, there is no going back."
        the_person "Do it... I'm ready!"
        mc.name "Okay..."
        "With her legs spread wide, your cock easily finds her slick entrance. She is wet and about as ready as she can be."
        "You slowly push yourself inside her. Barely inside, you hit her hyman. She winces a bit."
        mc.name "Alright. Here we go. 1...2...3..."
        "At three, you push inside forcefully. Her body resists for just a moment, then gives way, giving you access to her depths."
        the_person "Fuck! Oh stars..."
        $ take_virginity(the_person)
        $ the_person.draw_person(position = "missionary")
        call fuck_person(the_person, private=True, start_position = missionary, start_object = make_bed(), skip_intro = True, skip_condom = True, condition = make_condition_taking_virginity()) from _call_fuck_person_ellie_love_60_01

    $ the_person.draw_person(position = "missionary")
    "When you are finish, you collapse onto [the_person.title]'s bed next to her."
    the_person "That was amazing."
    mc.name "Yeah."
    if the_person.is_girlfriend():
        pass
    else:
        the_person "So umm... I don't know if this is something you had considered or not but..."
        the_person "Don't people usually like... say they are boyfriend and girlfriend when they do stuff like that?"
        mc.name "Some people do."
        the_person "Ah... umm... do you?"
        "[the_person.possessive_title] is curious if you want to make your relationship a bit more official. What do you want to do?"
        menu:
            "Ask her to be your girlfriend":
                mc.name "I do. [the_person.title], will you make it official? Will you be my girlfriend?"
                the_person "Oh thank the stars, yes!"
                $ the_person.add_role(girlfriend_role)
                $ the_person.change_love(5, 80)
                $ the_person.change_happiness(10)
                "[the_person.possessive_title] rolls over and gives you a lingering kiss on the lips."
                the_person "You... you wanna stay the night?"
                mc.name "I'm sorry, I didn't arrange for that. But I definitely will soon."
                the_person "Okay."
            "Say you aren't sure yet":
                mc.name "I really enjoy spending time with you [the_person.title], but things are moving really fast. I'm not sure I'm ready to commit to that yet."
                the_person "Ah... yeah... they have moved really fast, ain't they."
                $ the_person.change_love(-2, 80)
                $ the_person.change_happiness(-2)
                "You can tell she is a little disappointed, but she tries to hide it."
    "You get up and get your clothes back on. [the_person.possessive_title] stays in bed."
    mc.name "I can see myself out. Have a good night."
    the_person "Goodnight [the_person.mc_title]! I'll see you at work tomorrow..."
    $ clear_scene()
    $ mc.change_location(downtown)
    "You step out of [the_person.possessive_title]'s apartment."
    $ the_person.add_unique_on_room_enter_event(ellie_lingerie_shopping)
    return

label ellie_lingerie_shopping_label(the_person):    #Ellie's 80 love event. She asks MC to take her shopping for exciting underwear to wear for him.
    $ ellie.story_event_log("love")
    return

#Sluttiness EVents

init -1 python:

    def ellie_never_tasted_cock_requirement(the_person):
        if the_person.sluttiness >= 40 and mc.is_at_work() and mc.business.is_open_for_business() and ellie.story_event_ready("slut"):
            if get_random_employees(1, exclude_list = [the_person], slut_required = 50):
                return True
        return False

    def ellie_never_been_fucked_requirement(the_person):
        if the_person.sluttiness >= 60 and mc.is_at_work() and mc.business.is_open_for_business() and ellie.story_event_ready("slut"):
            return True
        return False

    def ellie_never_tried_anal_requirement(the_person):
        return False

    def ellie_turned_on_while_working_intro_requirement(the_person):
        return False

    def ellie_turned_on_while_working_requirement():
        return False


label ellie_never_tasted_cock_label(the_person):  #This is Ellie's 40 sluttiness event.
    $ talk_person = get_random_employees(1, exclude_list = [the_person], slut_required = 50)
    $ scene_manager = Scene()
    $ ellie.story_event_log("slut")
    "As you walk towards the entrance of research and development, you begin to overhear a conversation."
    "You stop and listen in before walking in the door, not because of what is being talked about, but because of WHO is talking."
    if ellie_has_given_blowjob():
        the_person "So like, you've had one in your mouth before... right?"
        talk_person "Of course!"
        the_person "Do you ever like... yah know... in your mouth... when he finishes?"
        talk_person "Sure! Once in a while."
        the_person "But isn't it like... gross?"
        talk_person "Gross? No! I mean, it is a bit of acquired taste, but if you go into it with an open mind it is honestly not a bad taste."
        the_person "Sorry, I just... my mamma always said doing something like that was for whores..."
        talk_person "Nahh, as long as everyone is having a good time!"
        if the_person.get_opinion_score("cum facials") > the_person.get_opinion_score("drinking cum"):
            talk_person "Real talk here. Guy's love it when you just let them finish all over your face!"
            the_person "On... mah face?"
            talk_person "Yeah! They LOVE it. Plus it is actually kind of good for your skin."
            the_person "Ah... I see..."
        elif the_person.get_opinion_score("drinking cum") > 0:
            talk_person "Real talk here. I usually just swallow it all."
            the_person "Yeah?"
            talk_person "Yeah! Guys love it when you do that, and it makes cleanup stupid easy."
            the_person "Ah... I see..."
        else:
            talk_person "Real talk here. I usually just let guys finish however they want. On my face, my chest, in my mouth, whatever."
            the_person "Oh..."
        "You pick that moment to turn the corner into the room."
    else:
        the_person "So like, you've had one in your mouth before... right?"
        talk_person "Of course!"
        the_person "Isn't it, like, gross?"
        talk_person "Gross? No! I mean, it is a bit of acquired taste, but if you go into it with an open mind it is honestly not a bad taste."
        the_person "Sorry, I just... my mamma always said doing something like that was for whores..."
        talk_person "Nahh, as long as everyone is having a good time!"
        the_person "What do you do like, when he's finishing though?"
        if the_person.get_opinion_score("cum facials") > the_person.get_opinion_score("drinking cum"):
            talk_person "Real talk here. Guy's love it when you just let them finish all over your face!"
            the_person "On... mah face?"
            talk_person "Yeah! They LOVE it. Plus it is actually kind of good for your skin."
            the_person "Ah... I see..."
        elif the_person.get_opinion_score("drinking cum") > 0:
            talk_person "Real talk here. I usually just swallow it all."
            the_person "You... swallow?"
            talk_person "Yeah! Guys love it when you do that, and it makes cleanup stupid easy."
            the_person "Ah... I see..."
        else:
            talk_person "Real talk here. I usually just let guys finish however they want. On my face, my chest, in my mouth, whatever."
            the_person "Oh..."
        "You pick that moment to turn the corner into the room."
    $ scene_manager.add_actor(the_person, position = "sitting")
    $ scene_manager.add_actor(talk_person, position = "sitting", display_transform = character_center_flipped)
    "[the_person.possessive_title] is looking down when you enter and doesn't even notice you walk in. [talk_person.title] sees you, however, and smiles."
    talk_person "Oh hey [talk_person.mc_title]."
    "[the_person.title] startles and looks up at you."
    the_person "Ah! [the_person.mc_title]! I umm... I wasn't... we were just..."
    mc.name "Talking about some things highly inappropriate for work."
    the_person "Ohhh stars. I..."
    mc.name "Come with me. We'll talk about this in my office."
    the_person "Oh fudge... okay..."
    $ scene_manager.update_actor(the_person, position = "stand3")
    "[talk_person.possessive_title] looks at you a little concerned, but you give her quick wink. She gives a smile as you turn and walk back out of the room."
    $ scene_manager.clear_scene()
    $ del talk_person
    "Silently you lead [the_person.title] to your office."
    $ ceo_office.show_background()
    "You let her step inside, then close the door, locking it quietly, motioning for her to sit down."
    $ the_person.draw_person(position="sitting")
    "You sit down across from her."
    the_person "Look, it's not what you think!"
    mc.name "Oh, it's not, is it?"
    the_person "No, I was jus..."
    if ellie_has_given_blowjob():
        mc.name "You don't want to know what it is like to swallow cum?"
        the_person "I was curiou... wha???"
        mc.name "[the_person.title]. You don't have to go to other employees when you get curious about this stuff, okay? You can just come to me."
        "[the_person.possessive_title] is blushing hard."
        mc.name "Now... do you want to know what it's like to swallow my load?"
    else:
        mc.name "You don't want to know what it is like to suck dick?"
        the_person "I was curiou... wha???"
        mc.name "[the_person.title]. You don't have to go to other employees when you get curious about this stuff, okay? You can just come to me."
        "[the_person.possessive_title] is blushing hard."
        mc.name "Now... do you want to know what it's like to suck dick?"
    "[the_person.title] looks down for a few moments... but then gives a slow nod."
    mc.name "It's nothing to be ashamed about."
    the_person "I... I think I understand that sir... but I've spent so much of my life being told that kind of stuff is for... harlots..."
    "Her voice breaks a little with the last word."
    mc.name "It's okay. I understand that. If you don't want to try, that's fine. I don't want to pressure you into anything."
    mc.name "But I also want you to know that it is perfectly understandable to be curious."
    mc.name "Especially working here. We have a lot of work to be done here, researching chemicals and programs that change or enhance sexuality."
    mc.name "It's okay if the answer is no. Do you want to suck my dick?"
    "[the_person.possessive_title] nods her head."
    the_person "... Yes... I really do..."
    mc.name "There. Was that so hard? Come here. We'll go slow, okay?"
    $ the_person.draw_person()
    "[the_person.title] gets up and walks around your desk."
    mc.name "Go ahead and get down on your knees. There's a reason that's a classic."
    $ the_person.draw_person(position = "blowjob")
    "As she gets down, you pull your cock from your pants."
    mc.name "Alright, so there aren't really very many rules for this, but a basic one for while you are learning, no teeth!"
    the_person "No teeth?"
    mc.name "Right. Use your lips to cover up your teeth. Teeth hurt, okay?"
    the_person "Ah, okay, I'll try."
    mc.name "Alright, let's take this slow. Use your hand a little to get used to it."
    "[the_person.possessive_title] takes you in her hand and gives you a couple strokes. Not long ago, she had never done this either, but now she handles your meat with skill."
    $ mc.change_locked_clarity(20)
    mc.name "That's it. Now, just give it a little kiss."
    the_person "Okay... mmmm..."
    "[the_person.title] gives your cock a quick peck. Then another. Then three more."
    mc.name "See? It's not so bad, is it?"
    the_person "Nah, it's so hot. And it smells kind of... manly..."
    "[the_person.possessive_title] begins to kiss along the underside, down towards the base, then back up to the top."
    $ mc.change_locked_clarity(20)
    mc.name "Mmm, that feels nice."
    "When she gets to the tip, [the_person.title] looks up at you and makes eye contact. A bit of pre-cum is starting to leak from the tip."
    "She closes her eyes and sticks out her tongue. She slowly licks at the tip of the head, tasting your pre-cum for the first time."
    "It takes her a few moments to open her eyes."
    the_person "That... is certainly unique."
    if the_person.love > 40:
        the_person "It doesn't taste very good but like... because it's you, something about it makes it good anyways..."
    else:
        the_person "The taste isn't great... but the fact that it's coming from you makes it really hot anyways..."
    #Increase drinking cum score
    $ mc.change_locked_clarity(30)
    mc.name "Keep going, I'll be glad to get you some more."
    "[the_person.possessive_title] starts to run her tongue around the tip now. She goes up and down at first, then circles it a few times."
    "[the_person.title] gives you a couple more strokes with her hand while she licks the tip. She stops and looks up at you."
    the_person "Okay. Here goes!"
    "[the_person.possessive_title] opens her mouth and for the first time pushes your erection inside her lips."
    $ mc.change_locked_clarity(40)
    $ the_person.break_taboo("sucking_cock")
    "With the tip in her mouth, [the_person.title] swirls her tongue around it a few times. It feels so good."
    "After a few seconds, she bravely pushes down a little further. She is clearly testing her limits, unsure of how far she can take it."
    the_person "Mmmmmmm... UNGLCK"
    "[the_person.possessive_title] suddenly gags as she takes it a little too far. She quickly pulls off and catches her breath."
    the_person "Stars! Sorry I..."
    mc.name "It's okay. The tip is the most sensitive part, just do what you can, but don't force it."
    the_person "Mmm... okay..."
    $ mc.change_locked_clarity(40)
    $ the_person.increase_sex_skill("Oral", 4, add_to_log = True)
    "[the_person.title] looks up at you as she licks at the tip again. She maintains the eye contact as she opens her mouth and starts to suck on the tip again."
    $ the_person.change_arousal(10)
    the_person "Mmm... mmm..."
    "[the_person.possessive_title] gives a couple little moans as she keeps working you over. She seems to be be really getting into it."
    $ mc.change_locked_clarity(40)
    "[the_person.title] is getting braver. She pushes the tip past her lips now and starts bobbing her head gently."
    mc.name "That's it. You're doing great. If it starts to get uncomfortable, you can always back off and just use your hand for a bit."
    "[the_person.title] looks at you and nods for a second, but keeps going. Her silky tongue is working wonders traveling up and down your cock."
    $ mc.change_locked_clarity(40)
    "The sensations are getting more intense. She's going to make you cum."
    mc.name "[the_person.title], I'm gonna cum soon. What do you want me to do?"
    "She pulls off for a quick second."
    the_person "Whatever you want. I just want to make you feel good."
    "[the_person.possessive_title] opens up and starts sucking you off eagerly now. She is really working hard!"
    $ mc.change_locked_clarity(40)
    "The velvet soft tongue of [the_person.title] is driving you over the edge. What do you want to do?"
    menu:
        "Cum in her mouth":
            "You put your hand on the back of her head."
            mc.name "Get ready, I want to cum in your mouth... here it comes!"
            "With a moan you explode, your cock starts to dump its load in her eager mouth."
            $ the_person.cum_in_mouth()
            $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = the_person)
            $ the_person.draw_person(position = "blowjob")
            "[the_person.title] is startled by how forcefully you ejaculate. She gags almost immediately, but refuses to close her mouth."
            "Cumming in [the_person.possessive_title]'s hot, wet mouth feels incredible. When you finish, you look down and see that she still has the tip in her mouth."
            mc.name "[the_person.title], that was incredible. Now, I want you to look up at me and swallow."
            "Dutifully, she looks up at you and does as you order. It takes a couple gulps, and she winces a bit, but she swallows it all."
            $ the_person.change_slut(2, 60)
            mc.name "So... how was it?"
            "She thinks about it for a moment."
            the_person "It was... I don't know! It was gross, but amazing at the same time..."
            $ the_person.increase_opinion_score("giving blowjobs", max_value = 1)
            $ the_person.increase_opinion_score("drinking cum", max_value = 2)
            $ the_person.increase_opinion_score("being submissive", max_value = 1)
        "Cum on her face" if not ellie_has_given_blowjob():
            "You put your hand on the back of her head and pull her off."
            mc.name "Use your hand, I want you to jack me off all over your face."
            "[the_person.possessive_title] starts stroking you rapidly with her hand, pointing you at her face."
            the_person "That's it. Cum on my face [the_person.mc_title]!"
            $ the_person.cum_on_face()
            $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_person)
            $ the_person.draw_person(position = "kneeling1")
            "Hearing her words pushes you over the edge and your cock explodes. Spurt after spurt erupts all over her face."
            "She keeps jacking you off, and overall does a very good job of aiming your twitching manhood."
            "When the last wave finishes, you look down and survey [the_person.possessive_title]. Her face is plastered in your semen."
            $ the_person.change_slut(2, 60)
            mc.name "So... how was it?"
            the_person "It's... sticky? But hot, and watching you as you cum made me feel so incredible..."
            $ the_person.increase_opinion_score("giving blowjobs", max_value = 1)
            $ the_person.increase_opinion_score("cum facials", max_value = 2)
            $ the_person.increase_opinion_score("taking control", max_value = 1)

    "As you recover, you get yourself decent again."
    $ the_person.draw_person()
    $ the_person.event_triggers_dict["given_blowjob"] = True
    the_person "I... I think I'm gonna go to the lady's room..."
    if ellie_has_brought_lunch_date():  #You've already done a lunch date. Go straight to eating her out.
        menu:
            "Reciprocate by eating her out":
                mc.name "Already? But I want to return the favor."
                the_person "Ah, you want to... what now?"
                mc.name "I mean, it's only fair, right? You got to taste me... can't I taste you?"
                "[the_person.title] is shocked, she did not see this coming."
                the_person "I... I didn't like, shave or nothin'!"
                the_person "Aren't ladies supposed to do that?"
                mc.name "Nonsense. You can trim sometime if you would like, but I'm certain I can make my way through your red forest."
                $ the_person.change_slut(2, 60)
                "[the_person.title] thinks for several seconds. A drop of your cum slips off her face and onto the floor..."
                $ mc.change_locked_clarity(30)
                mc.name "Sit up on the desk. Don't worry, you won't regret it."
                the_person "Oh... stars! Okay..."
                call ellie_cunnilingus_office_label(the_person) from _ellie_post_bj_slam_dunk_01
                $ the_person.draw_person(position = "missionary")
                "You stand up. [the_person.possessive_title] is lying on your desk, recovering."
                the_person "Stars! [the_person.mc_title]... was that like how it was... when you...?"
                mc.name "It was."
                the_person "That felt so good... can we do this again sometime? I might need more practice."
                mc.name "Of course. I'm going to get back to work now. You can recover for a bit if you want before getting back to work."
                the_person "Yes sir..."
                $ clear_scene()
                "You step out of your office, leaving [the_person.possessive_title] to recover. You head to the restroom and clean up your face before returning to work."
            "Let her go":
                mc.name "That's a good idea."
                the_person "But umm... can we do this again sometime? I ummm... I might need more practice."
                mc.name "I think that can be arranged."
                $ the_person.draw_person(position = "walking_away")
                "[the_person.possessive_title] awkwardly turns and walks out of your office."
                $ clear_scene()
    else:
        mc.name "That's a good idea."
        the_person "But umm... can we do this again sometime? I ummm... I might need more practice."
        mc.name "I think that can be arranged."
        $ the_person.draw_person(position = "walking_away")
        "[the_person.possessive_title] awkwardly turns and walks out of your office."
        $ clear_scene()
    "Your conservative, southern belle has now given you a blowjob! And it sounds like she wants to do it again soon!"
    "[the_person.title] now has oral positions unlocked."
    $ the_person.add_unique_on_room_enter_event(ellie_turned_on_while_working_intro)
    $ the_person.add_unique_on_room_enter_event(ellie_never_been_fucked)
    $ the_person.apply_planned_outfit()
    $ mc.location.show_background()
    #"Ellie may now approach MC once in a while when she is working on nanobot programs because working on sex related code is getting in her head and she needs some relief"
    return

label ellie_never_been_fucked_label(the_person):  #This is Ellie's 60 sluttiness event. Also requires X number of oral encounters?
    $ ellie.story_event_log("slut")
    $ the_person.arousal = 70
    $ the_person.draw_person(position = "sitting")
    "You check up on [the_person.title] while she is working."
    "She appears to be getting herself really worked up again. She has one hand between her legs, touching herself, while she tries to type with the other."
    "You sigh. She has so many years of pent up sexual drive, she can barely control it now. Especially with all the serums you've been testing on her."
    mc.name "Trouble concentrating, [the_person.title]?"
    the_person "Ah!"
    "She startles, pulling her hand back from between her legs when she looks up from her work at you."
    the_person "No! No sir I was..."
    "She mumbles something you can't hear."
    mc.name "You were... what now?"
    "[the_person.possessive_title] sighs."
    the_person "I... I'm trying to work on this... but stars I just can't stop thinking about..."
    if ellie_has_given_virginity():
        the_person "You know... the thing we did the other day..."
        "Ever since you took her virginity, she has been looking for excuses to fuck you as often as possible."
    else:
        "She leaves off the end of her sentence. [the_person.title] has been working for you for a while now, but it is clear that she is finally ready."
        "You've fooled around with her a few times, but now it is time to take the final step and show her how good sex can be."
    mc.name "Come with me, I want to spend some time with you in my office."
    the_person "Oh! Okay!"
    $ the_person.draw_person(position = the_person.idle_pose)
    "She quickly jumps up and follows you out of R&D."
    $ ceo_office.show_background()
    "Once in your office, you close and lock the door."
    if ellie_has_given_virginity():
        "Note from the author. You have already had sex with [the_person.title]."
        "However, you can reset her virginity status now to experience this part of the story as if it were her first time."
        "Would you like to experience this event as if she is still a virgin?"
        menu:
            "Yes. Take her virginity (again)":
                $ restore_virginity(the_person)
            "No.":
                pass
    if ellie_has_given_virginity():
        mc.name "It is clear to me that you need some relief... again..."
        the_person "I... I do appreciate it [the_person.mc_title]."
        mc.name "I think it is time for you to take the lead though."
        the_person "Sir?"
        "You step close to her, putting on hand on her shoulder."
        mc.name "Let's get naked. I'll sit down in my chair, and then you can come sit on my lap."
        the_person "Ah, you want me to... be on top? Are you sure?"
        "She bites her lip. You lift your hand up from her shoulder to her cheek. She looks up into your eyes... then melts."
        the_person "Okay... I can try that..."
        mc.name "Alright, let's get naked."
        $ the_person.strip_outfit(position = the_person.idle_pose)
        "You both quickly get undressed. You check out [the_person.possessive_title]."
        "Her nipples are stiff, and her labia are puffy and aroused. Clearly she is really turned on already."
        "You step over to your chair and sit down."
        mc.name "Alright, come here."
        $ the_person.draw_person(position = "cowgirl")
        "[the_person.title] walks over to you, then gets on your lap, her amazing tits are right in your face."
        mc.name "God your tits are fantastic."
        "You cup one in your hand, bringing your mouth up to the other one. You quickly suck and nip at her nipple, eliciting a loud moan from [the_person.possessive_title]."
        "You feel her hand on the back of your head, running her hand through your hair as you suckle her tit."
        the_person "Ahh. Okay, just gonna... do this... for a bit..."
        "[the_person.title] slowly adjusts her hips wider, until you can feel her humid groin get closer to yours, and then finally makes contact."
        the_person "Stars! It's so hard! Ahhh..."
        "She groans as she starts to rub herself up against you. Her soaking wet cunt is leaking fluid as she presses her hips eagerly against you and starts to grind."
        $ the_person.change_arousal(15) #85
        "You let go of her chest with your hand and put both your hands on her ass. You grab it to use for leverage as you start to thrust yourself up against her."
        the_person "[the_person.mc_title]! Be careful I'm... I'm already so... so close!"
        "Fuck it. You're sure you can make her cum more than once like this. You give her ass a smack but don't let up."
        $ the_person.change_arousal(20) #105
        the_person "Ah! I can't take it...!"
        $ the_person.have_orgasm(the_position = "cowgirl", half_arousal = True, force_trance = True) #52
        "[the_person.possessive_title] suddenly starts to shake as she begins to orgasm. Her legs stop moving and she moans loudly."
        if ellie_is_a_squirter():
            "You feel an alarming amount of fluid in your lap as she orgasms, squirting as she cums."
        "She spends several seconds with her legs and arms rigid as you thrust up against her, your hands groping her ass."
        "When she finishes, she opens her eyes and looks at you."
        the_person "That was so good... your thing is so... hard..."
        "She pushes herself back a bit on your lap, then reaches down and takes your cock in her hand."
        $ the_person.draw_person(position = "kneeling1")
        "She gives you a few slow strokes with her hand, your cock is heavily lubricated from rubbing against her slit."
        the_person "Stars, it's throbbing!..."
        "[the_person.possessive_title] sits up a bit and leans forward. With your cock in hand, she rubs it up and down her slit again a few times."
        the_person "It's so hard... I can't wait to feel it inside..."
        $ the_person.change_arousal(10) #62
        "After several seconds, she looks at you."
        the_person "Okay... I think I'm ready."
        "After several seconds, she lifts her hips up and rotates them forward a bit. She takes the base of your cock in her hand."
        "Slowly, she lets her body weight down as you feel your tip push slightly up and into her vagina."
        the_person "Oh... [the_person.mc_title], it's so big... it feels amazing!"
        $ the_person.draw_person(position = "cowgirl")
        "[the_person.title] leans forward and wraps her arms around you. Your face is buried in her cleavage."
        "[the_person.title] takes a deep breath."
        "You feel movement a she begins to let herself down, using her body weight to sink down onto you."
        $ the_person.change_arousal(20)    #82
        $ the_person.draw_person(position = "cowgirl")
        the_person "Ah! Oh stars OH!"
        "Her body goes rigid for several seconds... Did... she cum again?"
        the_person "Whew... that was close... Ha!"
        "You start to lick and suck on her nipple, and you feel her body shudder for a moment."
        "You spend several seconds on her tits before you feel her start to move."
        $ the_person.change_arousal(30) #112
        the_person "Ah! I'm not gonna last... I'm... OH!"
        $ mc.change_arousal(20)
        $ the_person.have_orgasm(the_position = "cowgirl", half_arousal = True, force_trance = True) #56
        "[the_person.possessive_title] is cumming again! You grope her tits aggressively as her body twitches and spasms."
        if ellie_is_a_squirter():
            "Another orgasm, another flood as she squirters in your lap."
        the_person "Ah... I can't believe it..."
        "She leans back, her nipple leaves your mouth with a loud smack. You can feel her pussy quiver around you."
        mc.name "Damn. Twice already? Will I get a proper fuck?"
        the_person "Ah, of course... just give me a minute..."
        "[the_person.possessive_title]'s pussy is so warm and tight wrapped around you. It wasn't so long ago you took her virginity."
        "You reach with your hands behind her again and grab her ass. Her warm cheeks feel so good in your hands."
        the_person "Alright. I think I'm ready to get this thing going!"
        mc.name "What do you want me to do when I'm ready to finish?"
        if the_person.wants_creampie():
            the_person "You know how I want it. Right up inside me where it belongs..."
            mc.name "Alright. One cum stuffed cunt, coming right up."
        else:
            the_person "I should probably pull off... just in case..."
            mc.name "Alright. I'll warn you when I'm getting ready to cum, but that is up to you."
        "[the_person.title] starts to move her hips up and down."
        $ the_person.change_arousal(20) #76
        "[the_person.title]'s poor little cunt is quivering all around you. You have an almost overwhelming urge to grab her ass and slam it into her and fuck her silly, but you resist for now."
        mc.name "God damn your cunt is so good. Don't worry I probably won't last long either."
        "She leans forward to try a different angle now, her tits now back in range of your mouth. You eagerly sink your face into her tit flesh."
        $ the_person.change_arousal(20) #96
        the_person "[the_person.mc_title]! Your cock is so big, it's filling me up!"
        "You just murmur your agreement as you assault a nipple with your tongue. She is gasping with every thrust now."
        $ the_person.change_arousal(20) #92
        "The southern belle is moaning and gasping as you fuck her. She is getting close to cumming."
        "The heat of the situation is getting to you as well."
        "You grab her hips with your hands. Instead of allowing her to keeping move front to back, you pick up her body a few inches above you."
        the_person "[the_person.mc_title]? What are you..."
        "With room to work now, you thrust your hips forcefully up into hers. Her ass makes a loud smack as you begin to fuck her."
        $ the_person.change_arousal(20) #112
        the_person "Ah! Oh my stars it's too good! I'm... I'm cumming!"
        "[the_person.possessive_title]'s body goes rigid again as she starts to cum. Her tight, quivering little hole feels too good and pushes you over the edge too."
        mc.name "Oh fuck, me too!"
        $ the_person.have_orgasm(the_position = "cowgirl", half_arousal = True, force_trance = True)
        if the_person.wants_creampie():
            the_person "Do it! I have to feel it!"
            $ the_person.cum_in_vagina()
            $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_person)
            $ the_person.draw_person(position = "cowgirl")
            "You slam her hips down onto yours, pushing yourself as deep as possible as you start to cum."
            "Her entire body is twitching and spasming as she cums with you. It feels like her cunt is milking you for every last drop."
            if ellie_is_a_squirter():
                "You can feel her copious juices running down between your legs and onto your chair."
            "Your cock twitches and pulses as you send out the last few spurts of your cum inside her. She clings to you helplessly."
        else:
            the_person "Ah! I should... I should get up..."
            "Her voice is shaky as she tries to gather the will to pull off. With a push or a pull on her hips, you could probably finish any way you want..."
            $ climax_controller = ClimaxController(["Pull her down and cum inside her", "pussy"],["Let her pull off and cum on her stomach", "body"])
            $ the_choice = climax_controller.show_climax_menu()
            if the_choice == "Pull her down and cum inside her":
                "You reach up and grab [the_person.possessive_title] by the hips. With one confident pull she plunges back onto your cock, gasping with pleasure."
                "The feeling of her warm, wet pussy sliding down and engulfing your cock again pushes you over the edge. You pull [the_person.title] tight against you and unload inside of her."
                the_person "Ah! Just... Just this once!"
                $ the_person.call_dialogue("cum_vagina")
                $ climax_controller.do_clarity_release(the_person)
                $ the_person.cum_in_vagina()
                $ the_person.change_obedience(5)
                $ the_person.draw_person(position = "cowgirl")

            elif the_choice == "Let her pull off and cum on her stomach":
                "You reach up and grab [the_person.possessive_title] by the hips. With one push your cock slips out from her warm cunt."
                "She grinds the lips of her pussy against your shaft as you climax. You fire your hot load over her stomach."
                $ the_person.cum_on_stomach()
                $ climax_controller.do_clarity_release(the_person)
                $ cowgirl.redraw_scene(the_person)
                the_person "Whew, that was close..."
        "For several seconds, [the_person.title] just sits on top of you."
        the_person "That was incredible. Three... three times!"
        mc.name "Maybe now you can concentrate on work."
        "She laughs for a moment. You give her ass a playful smack."
        "There are several moments of silence."
        the_person "I don't want to get up."
        mc.name "Take your time. Work can wait."
        $ the_person.change_happiness(5)
        $ the_person.change_obedience(2)
        the_person "Ah... yes sir."
        "Eventually, she slowly gets up."
        $ the_person.draw_person(position = "standing_doggy")
        the_person "Ah, we made such a mess..."
        "She turns around and starts looking in your desk drawers for something to clean herself with."
        "You just watch her ass sway back and forth in front of you in an orgasm addled bliss."
        "Eventually, she finds your wipes and stands up."
        $ the_person.draw_person(position = the_person.idle_pose)
    else:
        mc.name "It is clear to me that you need some relief... again..."
        the_person "I... I do appreciate it [the_person.mc_title]."
        mc.name "However, I'm a bit worried. Honestly, I don't think that yet another round of oral or fingerbanging is going to help much."
        the_person "Sir?"
        "You step close to her, putting on hand on her shoulder."
        mc.name "I think we both know it is time for you experience the real thing."
        "She shudders for a second... but there is still a bit of resistance."
        the_person "Stars, I don't know... I'm scared to..."
        "You see as she bites her lip, thinking."
        mc.name "Tell you what, I have an idea."
        the_person "Yeah?"
        mc.name "Let's just get naked. I'll sit down in my chair, and then you can come sit on my lap."
        the_person "But..."
        mc.name "You don't have to put it in if you don't want to, or you could even try just the tip, see how it feels."
        the_person "I don't know..."
        mc.name "Or just grind against me for a bit. I won't push you to take any steps you aren't ready for, it'll all be up to you."
        "She bites her lip again. You lift your hand up from her shoulder to her cheek. She looks up into your eyes... then melts."
        the_person "Okay... I'll just put it up against me for a bit... yeah that would feel good..."
        "Whew. You convinced her. Of course, for now, she thinks she is just going to grind against you for a bit..."
        "But with all the serums she's been taking, there is no way she just stops there."
        mc.name "Alright, let's get naked."
        $ the_person.strip_outfit(position = the_person.idle_pose)
        "You both quickly get undressed. You check out [the_person.possessive_title]."
        "Her nipples are stiff, and her labia are puffy and aroused. Clearly she is really turned on already."
        "You step over to your chair and sit down."
        mc.name "Alright, come here."
        $ the_person.draw_person(position = "cowgirl")
        "[the_person.title] walks over to you, then gets on your lap, her amazing tits are right in your face."
        mc.name "God your tits are fantastic."
        "You cup one in your hand, bringing your mouth up to the other one. You quickly suck and nip at her nipple, eliciting a loud moan from [the_person.possessive_title]."
        "You feel her hand on the back of your head, running her hand through your hair as you suckle her tit."
        the_person "Ahh. Okay, just gonna... do this... for a bit..."
        "[the_person.title] slowly adjusts her hips wider, until you can feel her humid groin get closer to yours, and then finally makes contact."
        the_person "Stars! It's so hard! Ahhh..."
        "She groans as she starts to rub herself up against you. Her soaking wet cunt is leaking fluid as she presses her hips eagerly against you and starts to grind."
        $ the_person.change_arousal(15) #85
        "You let go of her chest with your hand and put both your hands on her ass. You grab it to use for leverage as you start to thrust yourself up against her."
        the_person "[the_person.mc_title]! Be careful I'm... I'm already so... so close!"
        "Fuck it. You're sure you can make her cum more than once like this. You give her ass a smack but don't let up."
        $ the_person.change_arousal(20) #105
        the_person "Ah! I can't take it...!"
        $ the_person.have_orgasm(the_position = "cowgirl", half_arousal = True) #52
        "[the_person.possessive_title] suddenly starts to shake as she begins to orgasm. Her legs stop moving and she moans loudly."
        if ellie_is_a_squirter():
            "You feel an alarming amount of fluid in your lap as she orgasms, squirting as she cums."
        "She spends several seconds with her legs and arms rigid as you thrust up against her, your hands groping her ass."
        "When she finishes, she opens her eyes and looks at you."
        the_person "That was so good... your thing is so... hard..."
        "She pushes herself back a bit on your lap, then reaches down and takes your cock in her hand."
        $ the_person.draw_person(position = "kneeling1")
        "She gives you a few slow strokes with her hand, your cock is heavily lubricated from rubbing against her slit."
        the_person "Stars, it's throbbing!..."
        "[the_person.possessive_title] sits up a bit and leans forward. With your cock in hand, she rubs it up and down her slit again a few times."
        the_person "It wants to go in... doesn't it?"
        mc.name "Of course. Our bodies are meant to come together this way."
        $ the_person.change_arousal(10) #62
        mc.name "The question is, do you want it to go in?"
        "[the_person.title] remains silent, but continues to rub your erection up and down her pussy."
        "After several seconds, she looks at you."
        the_person "Maybe... like you said earlier... you could put just the tip in? Just... to see how it feels..."
        mc.name "That's a great idea. You're on top. I'm ready whenever you are."
        "[the_person.possessive_title] sighs. She is nervous, but her desire is finally getting the better of her."
        "After several seconds, she lifts her hips up and rotates them forward a bit. She takes the base of your cock in her hand."
        "Slowly, she lets her body weight down as you feel your tip push slightly up and into her vagina."
        "It comes to an abrupt stop when you hit her virginity. She flinches for a second."
        the_person "Oh... [the_person.mc_title], it's so big..."
        mc.name "Shh, it's okay. Just enjoy it for a bit."
        $ the_person.draw_person(position = "cowgirl")
        "[the_person.title] leans forward and wraps her arms around you. Your face is buried in her cleavage."
        the_person "This... this is going to hurt... isn't it?"
        mc.name "Just for a bit. In just a few minutes, it'll turn into something incredible."
        the_person "You're right. I know you're right. Okay..."
        "[the_person.title] takes a deep breath."
        "You feel movement a she begins to let herself down, using her body weight to sink down onto you."
        "At first, nothing happens, but then suddenly her body gives way as her hymen tears."
        $ take_virginity(the_person)
        $ the_person.change_arousal(-50)    #12
        $ the_person.draw_person(position = "cowgirl")
        the_person "Ah! Oh stars oh snap!"
        "Her body goes rigid for several seconds. You glance down and see a bit of blood going down her thigh."
        the_person "[the_person.mc_title] this hurts! You are so big... it's tearing me apart!"
        mc.name "Shh, just relax. The worst of it is over. Here, let me help..."
        "You start to lick and suck on her nipple again, and you feel her body shudder for a moment."
        "You spend several seconds on her tits before you feel her start to move again."
        "She keeps letting her body sink down onto yours. It feels like ages, but soon you feel her push herself all the way down."
        "Fully impaled on you now, she gasps as you play with her tits."
        $ the_person.change_arousal(20) #32
        the_person "Ah... it's in... I can't believe it..."
        "She leans back, her nipple leaves your mouth with a loud smack. You can feel her pussy quiver around you."
        the_person "You better be right about this. It is starting to feel good now..."
        mc.name "Don't worry. This is the start of something amazing. You might be sore for a day or two, but you are going to love it everytime we fuck."
        "[the_person.possessive_title]'s pussy is so warm and tight wrapped around you. It isn't everyday you get to take a girl's virginity, so you just sit back and savor it."
        "You reach with your hands behind her again and grab her ass. Her warm cheeks feel so good in your hands."
        the_person "Alright... I think I'm ready to get this thing going..."
        mc.name "What do you want me to do... when I'm ready to finish?"
        the_person "Oh... I hadn't really thought about that."
        "She looks at you for a moment."
        the_person "I think... I want you to just finish... like this."
        mc.name "Inside you?"
        the_person "Yeah... this might be dumb but, this is my first time. I want to feel everything."
        mc.name "Okay. I'm ready when you are."
        the_person "Alright."
        "Slowly, gently, [the_person.possessive_title] rocks her hips forward a bit, and you slide partially out. Then she rocks her hips back, enveloping you fully again."
        the_person "Ahh!... oh wow..."
        "She does it again, going slowly. Her breath catches in her throat when she pushes it back again."
        the_person "[the_person.mc_title]...!"
        $ the_person.change_arousal(20) #52
        "[the_person.title]'s poor little cunt is quivering all around you. You have an almost overwhelming urge to grab her ass and slam it into her and fuck her silly, but you resist for now."
        mc.name "That's it. See? It is starting to feel good, isn't it?"
        "[the_person.possessive_title] is moving her hips back and forth now, her body quickly learning what feels good as she changes the angle a few times."
        the_person "It is... Oh stars it feels so good."
        "She leans forward to try a different angle now, her tits now back in range of your mouth. You eagerly sink your face into her tit flesh."
        $ the_person.change_arousal(20) #72
        the_person "[the_person.mc_title]! You're filling me up... it's so good!"
        "You just murmur your agreement as you assault a nipple with your tongue. She is gasping with every thrust now."
        $ the_person.change_arousal(20) #92
        "The southern belle is moaning and gasping as you fuck her for the first time. She is getting close to cumming."
        "The heat of the situation is getting to you as well. You decide it is time to fuck her proper and make her first time truly memorable."
        "You grab her hips with your hands. Instead of allowing her to keeping move front to back, you pick up her body a few inches above you."
        the_person "[the_person.mc_title]? What are you..."
        "With room to work now, you thrust your hips forcefully up into hers. Her ass makes a loud smack as you begin to fuck her."
        $ the_person.change_arousal(20) #112
        the_person "Ah! Oh my stars it's too good! I'm... I'm cumming!"
        "[the_person.possessive_title]'s body goes rigid again as she starts to cum. Her tight, quivering little hole feels too good and pushes you over the edge too."
        mc.name "Of fuck, me too!"
        $ the_person.have_orgasm(the_position = "cowgirl", half_arousal = True, force_trance = True)
        the_person "Do it! I have to feel it!"
        $ the_person.cum_in_vagina()
        $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_person)
        $ the_person.draw_person(position = "cowgirl")
        "You slam her hips down onto yours, pushing yourself as deep as possible as you start to cum."
        "Her entire body is twitching and spasming as she cums with you. It feels like her cunt is milking you for every last drop."
        if ellie_is_a_squirter():
            "You can feel her copious juices running down between your legs and onto your chair."
        "Your cock twitches and pulses as you send out the last few spurts of your cum inside her. She clings to you helplessly."
        the_person "That was incredible."
        mc.name "I told you it would be."
        "She laughs for a moment."
        the_person "Yeah... you did."
        "There are several moments of silence."
        the_person "I don't want to get up."
        mc.name "Take your time. Work can wait."
        $ the_person.change_happiness(5)
        $ the_person.change_obedience(2)
        the_person "Ah... yes sir."
        "You sit for for a while just like that, your softening cock still inside of [the_person.possessive_title]."
        "Eventually, she slowly gets up, not anticipating how much would leak out of her."
        $ the_person.draw_person(position = "standing_doggy")
        "She panics, quickly turning around and puts her hand between her legs to keep too much from leaking out."
        "You can see her blood mixed with cum running down her legs. It makes your cock twitch at the incredible sight."
        the_person "[the_person.mc_title]! Get me a tissue or something, stars!"
        "You laugh and quickly grab some wipes from your desk."
        $ the_person.draw_person(position = the_person.idle_pose)
    "[the_person.title] is standing in front of you, starting to clean herself up. You can tell from the look in her eyes she is in a bit of a daze."
    "Or is that a trance? You decide to try and do some post orgasm training..."
    call do_training(the_person) from _call_do_training_ellie_after_fuck_01
    "[the_person.possessive_title] cleans herself up."
    $ the_person.apply_planned_outfit()
    $ the_person.draw_person()
    the_person "I'm going to get back to work..."
    mc.name "Sounds good. I'll have to check your productivity at the end of the day. If it goes up, we might have to make this a regular thing."
    the_person "Oh... I'd better work hard then!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.title] turns and starts to walk out of your office. You can't believe how far she has come."
    "From a blackmailing virgin, she is getting to be one of your favorite office cumdumps."
    "You smile as you think about how far things are going to go with her."
    $ the_person.add_unique_on_room_enter_event(ellie_never_tried_anal)
    return

label ellie_never_tried_anal_label():   #This is Ellie's 80 sluttiness rating. Must have anal nanobots unlocked.
    pass
    $ ellie.story_event_log("slut")
    $ ellie.event_triggers_dict["given_anal_virginity"] = True
    return

label ellie_turned_on_while_working_intro_label(the_person):
    $ ellie.event_triggers_dict["work_turnon"] = False
    return

label ellie_turned_on_while_working_label():    #Crisis event. Can be triggered after unlocking Ellie's oral sex options, and procs when she is working on nanobot programming.
    "During a break, you make the rounds to the different departments. When you swing by R&D, you decide to check up on [ellie.title]"
    "[ellie.title] is masturbating, trying to type with one hand and playing with herself with the other."
    "She is sorry. Working on this stuff gets her so horny."
    "Initially, you can chastise her (dislikes masturbation), encourage her (likes masturbation), or offer to help her."
    "If you offer to help her, you can do it right there in R&D (likes public sex), or find somewhere private."
    "Her reactions change based on her story and corruption progress. At extreme sluttiness, when she sees you walk up she may jump MC or if submissive, pull down bottoms and bend over her desk and beg."
    "Sex scene."
    return

label ellie_asks_to_join_harem_label(the_person):   #100 sluttiness event. Ellie asks to join MCs harem.
    pass
    return

# Obedience Events
init -1 python: #Requirement functions
    def ellie_tit_fuck_requirement():
        if not ellie.story_event_ready("obedience"):
            return False
        if mc.location == mc.business.r_div and ellie.obedience >= 120 and mc.business.is_open_for_business():
            return True
        return False

    def ellie_start_search_requirement():
        if not (mc.is_at_work() or mc.business.is_open_for_business()):
            return False
        if ellie.days_since_event("obedience_event") <= TIER_2_TIME_DELAY or mc.business.get_event_day("IT_dir_nanobot_takeover_day") < TIER_3_TIME_DELAY:
            return False
        if ellie.obedience >= 140 and nanobot_program_is_IT() and mc.business.is_open_for_business():  #Need to make sure we know contact has ghosted head researcher.
            return True
        return False

    def ellie_search_update_requirement(the_person):
        if not (mc.is_at_work() or mc.business.is_open_for_business()):
            return False
        if not ellie.story_event_ready("obedience"):
            return False
        if not ellie_has_given_blowjob():
            return False
        return True

    def ellie_search_finish_requirement():
        if not (mc.is_at_work() or mc.business.is_open_for_business()):
            return False
        if ellie.story_event_ready("obedience") and time_of_day == 3:
            return True
        return False

    def ellie_submission_requirement():
        if not (mc.is_at_work() or mc.business.is_open_for_business()):
            return False
        if ellie.obedience > 160 and time_of_day == 3 and ellie.story_event_ready("obedience"):
            return True
        return False

    def ellie_nanobot_fetish_testing_requirement(the_person):
        return False

    def ellie_nanobot_fetish_requirement(the_person):
        return False

init 1 python:
    ellie_tit_fuck = Action("Use Ellie's Tits", ellie_tit_fuck_requirement, "ellie_tit_fuck_label")
    ellie_start_search = Action("Ellie was framed", ellie_start_search_requirement, "ellie_start_search_label")
    ellie_search_update = Action("Finding the Culprit", ellie_search_update_requirement, "ellie_search_update_label")
    ellie_search_finish = Action("Ellie's Revenge", ellie_search_finish_requirement, "ellie_search_finish_label")
    ellie_submission = Action("Ellie's submission", ellie_submission_requirement, "ellie_submission_label")
    ellie_nanobot_fetish_testing = Action("Ellie's first fetish", ellie_nanobot_fetish_testing_requirement, "ellie_nanobot_fetish_testing_label")
    ellie_nanobot_fetish = Action("Give Ellie another fetish", ellie_nanobot_fetish_requirement, "ellie_nanobot_fetish_label")

label ellie_tit_fuck_label(): #120 obedience. Unlocks Ellie's tit fucks
    $ the_person = ellie
    $ mc.arousal = 30
    $ the_person.event_triggers_dict["tit_fuck"] = True
    $ mc.change_location(mc.business.r_div)
    "You sit at a desk, working in the research department."
    "However, you are having an incredibly hard time concentrating. You look across the room at [the_person.possessive_title]"
    $ the_person.draw_person(position = "sitting")
    $ desc_string = "You hired her " + mc.business.string_since_event("hired_ellie_IT")
    "[desc_string]"
    "Since then you've found yourself getting closer with the buxom redhead. You gaze at her from across the lab."
    "Her chest heaves slightly with every breath. You can't help but fantasize about sliding your cock between her generous tits."
    $ mc.change_locked_clarity(30)
    "You imagine in your mind, pinching and rolling her nipples between your fingers as fuck her soft, pillowy tit flesh..."
    $ mc.change_locked_clarity(30)
    "[the_person.possessive_title] looks up, and realizes you are staring at her."
    the_person "You okay over there, [the_person.mc_title]?"
    "You see some color in her cheeks. She knows you were checking her out."
    "Instead of answering you, you stand up and walk over to her desk. You see her bite her lip as you approach."
    the_person "Sir?"
    "Something shifts in your mind. Why just fantasize? [the_person.title] is your employee."
    "She's been opening up to you recently, and you've been more than generous with her with her work. You deserve a kickback."
    mc.name "I need your help with something, can you come with me?"
    the_person "Of course..."
    $ the_person.draw_person(position = "stand2")
    "You walk quietly to your office with [the_person.possessive_title] following you."
    $ mc.change_location(ceo_office)
    "You step into your office. After she follows you in, you close and lock the door."
    the_person "[the_person.mc_title], you're scaring me..."
    mc.name "[the_person.title], you've been doing great work for me ever since I hired you. Your work on the company IT programs has been examplary."
    mc.name "However, if I'm being honest, sometimes working with you is a bit of a struggle for me."
    the_person "I'm sorry sir. I don't want to be a problem, what is wrong with my work?"
    mc.name "There's nothing wrong with your work. The problem is your body."
    the_person "My... body?"
    mc.name "You have incredible curves. After working with your for extended periods, it becomes impossible for me to concentrate."
    $ the_person.change_stats(slut = 2, max_slut = 40)
    "[the_person.possessive_title] gasps as you start to pull out your cock. It is rock hard from your previous fantasizing."
    mc.name "I need you to take care of this for me. On your knees."
    if the_person.sluttiness >= 40: #Gladly
        the_person "Of course [the_person.mc_title]. Sorry I'm still kinda new to this, I didn't realize you need me so bad."
    else:
        "[the_person.title] hesitates for a second, but then slowly, obediently, gets down on her knees."
    $ the_person.draw_person(position = "blowjob")
    if the_person.tits_available():
        "You look down at [the_person.possessive_title]. Her tits are out and she looks ready to service you."
    else:
        mc.name "Let's get this off..."
        "You quickly pull at her top before she has a chance to resist."
        $ the_person.strip_to_tits(position = "blowjob")
        $ the_person.break_taboo("bare_tits")
        "She looks up at you, waiting for you to take the lead."
    $ mc.change_locked_clarity(30)
    mc.name "I want you to do something different for me. I want you to put my cock between your tits."
    the_person "You want to put your thing between my... my boobies?"
    mc.name "Tits. When we are having sex, they're called tits. And yes, I want to fuck your tits."
    $ the_person.change_stats(obedience = 2)
    the_person "Ah ok... you can... fuck my titties..."
    "[the_person.title] hesitates a bit, but soon obediently complies, moving close to you."
    "[the_person.possessive_title] lifts up her knees a little. She looks up at you, obviously still a little unsure, but you nod your encouragement."
    "You help press forward a bit when her soft tit-flesh finally makes contact with your groin. You take her hands in yours and show her how to wrap her tits around you."
    $ the_person.break_taboo("touching_penis")
    mc.name "There, now just... bounce them a little."
    the_person "Ah, okay."
    "[the_person.title] uses her hands to move her big tits up and down your cock. The soft flesh feels amazing sliding up and down."
    $ mc.change_locked_clarity(30)
    $ the_person.change_arousal(20) #50
    "You let out a low, growling moan. It feels so good to finally have your cock buried between the buxom redheads tits."
    "Your pre-cum is starting to leak out, but you could definitely use some lube. You stop her for a moment."
    the_person "[the_person.mc_title]?... ahhhh."
    "You let a large amount of saliva out of the bottom of your mouth. It splatters onto her chest and into her cleavage."
    mc.name "There, add some of your own too. IT feels better."
    the_person "Ah, yes sir..."
    "[the_person.possessive_title] adds some of her own spit to yours, working it down into her cleavage by jiggling her tits with her hands."
    mc.name "Mmm, that's better. Keep going now."
    $ mc.change_locked_clarity(30)
    $ the_person.change_arousal(20) #70
    "[the_person.title] is clumsily jiggling her tits around your cock. Thankfully her flesh is so soft it feels pretty good anyway."
    "You reach down and grab [the_person.title]'s tits yourself. She places her hands over yours and holds them in place."
    the_person "Stars... your thing is so warm..."
    "You squeeze down hard on her breasts and work your hips, fucking her soft cleavage. [the_person.title] moans in response."
    $ the_person.change_arousal(30)
    mc.name "Cock. Its called my cock. It feels good, doesn't it? To get down on your knees and service my cock like this."
    the_person "Yes..."
    mc.name "Say it. I want you to tell me how much you love getting your tits fucked like this."
    "[the_person.title] stutters for a moment."
    mc.name "Its okay. Just say it."
    the_person "I... it feels so right. I love it! Please fuck my tits [the_person.mc_title]!"
    $ mc.change_arousal(20) #90
    "Your pre-cum is leaking pretty heavily now. It adds to the pleasure of [the_person.possessive_title] fucking you with her tits."
    "She stops moving her tits for a second to spit down into her cleavage. She moves her breasts up and down, slathering you up before continuing."
    $ mc.change_locked_clarity(50)
    $ mc.change_arousal(20) #110
    mc.name "Oh god. [the_person.title], I'm almost there. Keep going!"
    the_person "Okay [the_person.mc_title]!"
    "This southern redhead's big titties are amazing, bouncing up and down around your cock. It's getting ready to burst."
    $ mc.change_locked_clarity(50)
    $ ClimaxController.manual_clarity_release(climax_type = "tits", the_person = the_person)

    "Your orgasm builds to a peak and you grunt, blasting your load up between [the_person.title]'s tits and out the top of her cleavage."
    $ the_person.cum_on_tits()
    $ the_person.draw_person(position = "kneeling1")
    "Your cum splatters down over the top of [the_person.title]'s tits. She gasps as the warm liquid covers her and drips back down between them."
    "She looks up at you. She has no idea what to do."
    mc.name "Hang on, let me get you some tissues and wet wipes."
    "You quickly walk back to your desk and pull some out and hand them to her."
    $ the_person.draw_person()
    the_person "There's so much! And so warm..."
    $ the_person.change_arousal(20)
    "You help her get cleaned up, then back into her outfit."
    $ the_person.apply_planned_outfit()
    $ the_person.draw_person()
    mc.name "That was amazing. Exactly what I needed."
    the_person "Ah, yeah that was nice. Do you want to do it again sometime?"
    mc.name "I do. But for now I need to recover a bit before I go back to work."
    $ the_person.change_stats(obedience = 3)
    the_person "Okay. I'm going to get back to work then."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] awkwardly turns and leaves your office. You can't help but smile."
    "She'll get used to servicing your needs in your office with more than just her tits soon enough. For now you are content with the leap of progress you have made with her."
    $ mc.business.add_mandatory_crisis(ellie_start_search)
    $ ellie.story_event_log("obedience")
    $ clear_scene()
    return

label ellie_start_search_label(): #140 obedience. Scene where you talk to ellie and Steph about the contact
    $ the_person = ellie
    $ scene_manager = Scene()
    $ the_researcher = mc.business.head_researcher
    $ mc.change_location(mc.business.r_div)
    "You walk into the Research department. As you step in, you see [the_researcher.title] look up from her work and walk over to you."
    $ scene_manager.add_actor(the_researcher)
    the_researcher "Hey [the_researcher.mc_title]. You'll never believe what just happened to me."
    mc.name "What's that?"
    the_researcher "Remember my nanobot contact? The guy that ghosted us?"
    mc.name "Of course."
    the_researcher "Well, I was posting some selfies to my DikDok, and I got a bunch of comments from him!"
    mc.name "Wow... how do you know it was him?... And you are on DikDok?"
    the_researcher "Yes, and I know because he has a very unique last name, and his username was basically just his first initial and last name..."
    mc.name "Huh. You know who might be interested in that?"
    the_researcher "Who?"
    "You look over to the other side of the lab."
    mc.name "Hey [the_person.title]! Come her for a second!"
    $ scene_manager.add_actor(the_person, display_transform = character_center_flipped)
    the_person "Hey, what's the fuss?"
    mc.name "Remember the guy from your last employer that set you up and got you fired?"
    the_person "Stars, how could I forget that jerk!"
    mc.name "He is hitting on [the_researcher.title] on DikDok."
    $ scene_manager.update_actor(the_person, emotion = "angry")
    the_person "He... He what!?!"
    the_researcher "Yeah. He keeps asking for nudes, but doesn't want to pay for em'. I keep blowing him off."
    the_researcher "His last message, he said he lives in the same area as me and was willing to pay $100 for a blowjob."
    the_person "UGH. Typical. What I wouldn't do to get my hands on that good for nothin'..."
    "As [the_person.possessive_title] goes off about the guy, a plan slowly begins to form in your head..."
    "He sounds like a total creep... but you would score major bonus points with [the_person.title] if you could help her get back at him."
    "You wonder... could you lure the guy in? Then capture him offering to pay for sex on video and blackmail him... or even get him arrested?"
    "You probably shouldn't turn him over to the authorities... but blackmail could work..."
    mc.name "Hey [the_researcher.title]. On DikDok, it isn't uncommon to do shoutouts, right? Especially to new accounts?"
    the_researcher "Yeah I think I've seen a few of those."
    mc.name "[the_person.title]... I have an idea."
    the_person "Yeah?"
    $ scene_manager.update_actor(the_person, emotion = "happy")
    mc.name "We're going to set you up with a DikDok account and have [the_researcher.title] do a shoutout for you."
    mc.name "He is sure to see it. We already know he's willing to pay for sexual favors. We'll use the account to lure him in and get dirt on him."
    the_researcher "Damn, a classic honeypot."
    the_person "I ahm, I don't know. Isn't that thing for like, women who send out pictures of themselves naked?"
    mc.name "That is precisely what it is. And for making money off them."
    the_person "I don't know if I can do something like that..."
    mc.name "Non sense. Of course you can. It isn't like you are just doing it for fun, we could use them to get back at him."
    "[the_person.possessive_title] seems to be wavering a bit, so you decide to push her a bit..."
    mc.name "Here, let me see your phone, I'll help you set up an account."
    the_person "Ah, okay, I guess we can try."
    $ the_person.add_role(dikdok_role)
    $ the_person.event_triggers_dict["dikdok_known"] = True
    "You walk her through getting her account set up."
    "Of course you make note of the name so you can check up on it."
    $ the_person.change_stats(obedience = 3)
    mc.name "Alright, once in a while make a new posting with a pic of you doing something naughty, but first lets get you a promo."
    mc.name "Let's go back to the testing room."
    #TODO make a testing room background and transition to it here.
    "You walk with the girls back to the serum testing room for privacy."
    mc.name "Alright, [the_researcher.title], you make a video. Say something like, hey guys, just found out my super hot coworker has an account too and everyone should check it out."
    if the_person.tits_available():
        mc.name "Then you can zoom in on [the_person.title]'s tits and she'll shake em' around or something. Then plug her username and we'll see if we can get a hit. Sound good?"
    else:
        mc.name "Then you can zoom in on [the_person.title] and she'll take her top off. Then plug her username and we'll see if we can get hit. Sound good?"
    the_researcher "Sounds great to me!"
    the_person "You... you wanna take a video of mah tits?"
    mc.name "That's the idea, yeah."
    the_person "I... I dunno, I'm not sure I want a video like that going around on the internet..."
    mc.name "Don't worry. We're just doing this to help you get even, remember?"
    the_researcher "Don't worry, it is fun too!"
    the_person "Okay... I guess..."
    "You make a mental note to thank [the_researcher.possessive_title] for helping convince [the_person.title] to take some topless pics later..."
    mc.name "Alright, well, this should be straight forward. [the_researcher.title]... whenever you are ready?"
    the_researcher "Okay."
    "[the_researcher.possessive_title] pulls out her phone and takes a few seconds to boot up the app."
    "She takes a few seconds to straighten her hair, then starts the video."
    the_researcher "Hey guys! Guess what!?!"
    "Her mock enthusiasm is amusing, but you keep yourself from laughing and ruining the video."
    the_researcher "I just found out... the new girl at work... has a DikDok account too! And she JUST STARTED!"
    the_researcher "She is smoking hot too... I just wanted to give her a quick shoutout!"
    "[the_researcher.title] takes her phone and moves the camera around to get [the_person.title] in frame."
    the_researcher "Here she is! Show my viewers what they're missing!"
    if the_person.tits_available():
        $ scene_manager.update_actor(the_person, position = "kneeling1")
        "[the_person.title] smiles, then takes her tits in her hands and pushes them together, giving them a squeeze."
    else:
        $ scene_manager.strip_to_tits(the_person)
        "[the_person.title] smiles, then takes her top off, revealing her big tits."
    $ mc.change_locked_clarity(30)
    "[the_researcher.possessive_title] brings the camera back to her."
    the_researcher "Damn, right? Anyway, here's her username..."
    "[the_researcher.title] finishes up the promo video."
    $ scene_manager.update_actor(the_person, position = "stand3")
    mc.name "There, that wasn't so bad, was it?"
    the_person "No... actually it was kinda fun... do you think people will like it?"
    the_researcher "I mean, I'm mostly straight, but I loved it. Your tits are fantastic."
    the_person "Aww, thanks [the_researcher.name]."
    $ the_person.increase_opinion_score("showing her tits", max_value = 1)
    mc.name "Alright, [the_person.title], once or twice a day, take a video or a couple pics and drop them on there."
    mc.name "[the_researcher.title] will give you the guy's username. If you get any DMs from him, start talking to him and see if you can get anything going, okay?"
    the_person "Yessir."
    "The two girls get together and start to talk about the mysterious contact. You decide to leave them to it."
    $ scene_manager.remove_actor(the_person)
    $ scene_manager.remove_actor(the_researcher)
    "You step out of the examination room. You have no idea if this plan will work or not, but you know it will take time to find out."
    "Even if the guy never bites, at least you convinced [the_person.title] to start a DikDok account..."
    $ del the_researcher
    $ ellie.story_event_log("obedience")
    $ the_person.add_unique_on_room_enter_event(ellie_search_update)
    return

label ellie_search_update_label(the_person):    #You locate the contact
    $ mc.change_location(mc.business.r_div)
    "You step into the Research and Development department. When you do, [the_person.title] notices you, gets up, and walks over to you."
    $ the_person.draw_person()
    the_person "Hey! Have a second? I have something I need to talk to you about... you know... in private."
    mc.name "Sure. Let's head for my office."
    $ mc.change_location(ceo_office)
    "You walk into your office with [the_person.possessive_title] and sit down."
    $ the_person.draw_person(position = "sitting")
    the_person "Well, Alan, you know that guy we've been trying to find, messaged me on DikDok and I've been messaging back and forth with him."
    mc.name "That is excellent news."
    the_person "I keep trying to get him to meet up, you know, like you told me to do, but so far he hasn't taken any interest."
    the_person "I sent him some pretty umm... interesting... pics, but I can't convince him I'm being legitimate."
    mc.name "Ahhh, he is wary. Have you offered to exchange sexual favors with him?"
    the_person "Umm, yeah I did that, but he doesn't believe me."
    "You think about it for a moment, but you are able to come up with a solution."
    mc.name "What if we get some pictures to send him of you actually doing some of those sexual favors?"
    the_person "Whaddya mean?"
    mc.name "He doesn't believe that you'll actually do anything with him... what if we take a picture of you sucking on my dick and send it to him."
    mc.name "If he truly doesn't believe you would be willing to, it would convince him otherwise."
    if ellie_has_given_blowjob():
        the_person "I dunno... taking pictures while I suck your dick seems like it might be taking things a little too far..."
    else:
        the_person "I... I don't know... that feels like we are taking this whole thing a little too far..."
    mc.name "I know it feels that way, but don't worry, this is just an act to try and expose him."
    "[the_person.possessive_title] mutters something under her breath. She seems unconvinced."
    "You decide to push the issue before she has the chance to think it through."
    mc.name "Come here. It will take just a few minutes, and if it doesn't work, it'll be no big deal."
    the_person "I... okay..."
    $ the_person.draw_person(position = the_person.idle_pose)
    "After hesitating, [the_person.title] obediently gets up and walks around your desk."
    mc.name "Here, let me have your phone. I'll take the pictures. Go ahead and get on your knees."
    $ the_person.draw_person(position = "blowjob")
    "Slowly but obediently, [the_person.possessive_title] hands you her phone and then gets on her knees in front of your chair."
    if the_person.tits_available():
        "You feel your cock twitch in your pants as you look down at the busty redhead, on her knees at your desk, her tits already on display."
    else:
        mc.name "Get your tits out, we want to make this look good."
        the_person "Yes sir."
        $ the_person.strip_to_tits(position = "blowjob")
    "You pull out your dick, now rock hard, and take a picture of [the_person.title] with her face right next to it."
    $ mc.change_locked_clarity(30)
    if ellie_has_given_blowjob():
        mc.name "Alright, you know what to do. Just pretend like I'm not even taking pictures."
    else:
        mc.name "Alright. I know you don't have a lot of experience with this, but don't worry, it's easy."
        the_person "I... I'll try..."
    "You put your free hand on the back of [the_person.possessive_title]'s head. She opens her mouth and lets you guide her lips down to the tip."
    "[the_person.title]'s lips part, and you feel the tip of your cock slide into her soft, wet mouth."
    $ mc.change_locked_clarity(30)
    if ellie_has_given_blowjob():
        "[the_person.possessive_title] has been working on her oral technique, you can tell as she swirls her tongue around the tip."
    else:
        "You've finally gotten [the_person.possessive_title] to give you a blowjob, and victory feels amazing."
    mc.name "Look up at me while you do that."
    "[the_person.title] looks up at you as her tongue plays with the tip. You snap a couple quick pictures."
    mc.name "Damn that's hot. Now make me feel good, the quicker you work the sooner we can get the pictures we need."
    if ellie_has_given_blowjob():
        "[the_person.title] just nods and then starts to bob her head up and down, stroking you with her lips and tongue."
    else:
        "[the_person.title] pops off your cock."
        the_person "Can't you just like... you know... do it yourself? Then get pics when you finish?"
        mc.name "No. You can tell when people take fake pictures like that. Sucking on dick smears lipstick, makes things messy..."
        "[the_person.possessive_title] reluctantly gives in and starts her blowjob in earnest."
        "You pull her head back down on your cock, and her head starts to bob up and down."
    $ mc.change_locked_clarity(50)
    "You hands on her head guide her inexperienced mouth as she gets to work, sucking you off."
    "You make sure to snap a couple pictures here and there, her face getting progressively messier as things continue."
    mc.name "Let's get a picture of you taking it deep, okay?"
    "[the_person.title] looks up, a hint of fear in her eyes, but she nods."
    mc.name "Alright, just relax, and let me guide you down."
    "Slowly, you pull her head down your cock further and further, until at last her nose is touching your skin."
    "You snap a couple quick pictures, when she suddenly gags hard and backs off."
    $ mc.change_locked_clarity(50)
    the_person "Stars! You are so big..."
    "She takes a moment to recover, then with your encouragement gets back to work."
    "The soft slurping noises of [the_person.possessive_title] as she blows you are really turning you on."
    "Her steamy mouth milking your cock is getting to you. You are going to cum soon."
    mc.name "I'm gonna cum. Let me cum on your face, it'll make the most convincing pictures."
    $ the_person.draw_person(position = "kneeling1")
    "[the_person.title] pops off your cock and looks up at you as you point it at her face and give it the final few strokes."
    $ the_person.cum_on_face()
    $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_person)
    "You do your best to snap pictures as you finish all over [the_person.title]'s face. One spurt hits her in the eye and she flinches."
    the_person "Ah! Careful where you point that thing!"
    $ the_person.event_triggers_dict["given_blowjob"] = True
    "You finish cumming with one last drip that lands on [the_person.possessive_title]'s chin."
    "Satisfied with your work, you quickly snap a few pictures."
    mc.name "Go ahead and get cleaned up, I'll DM him the pictures."
    the_person "Umm... right..."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.title] stands up and turns around, looking for something to wipe her face off with."
    "You open up her DikDok account and find the messages with the contact. You quickly read through the more recent ones, and discover she really has been trying to bait this guy."
    "You quickly upload a few from your blowjob session. The last one is with [the_person.title]'s face plastered with your cum."
    "This could have been you ;)"
    "You send him a message with it. Let's see if he takes the bait or not."
    $ the_person.apply_planned_outfit()
    $ the_person.draw_person()
    "You are starting to come up with a plan for what to do if this guy responds when [the_person.title] comes back."
    the_person "Alright, did I get it all?"
    mc.name "Yeah, I think you did. Alright, here is the plan. I want you to see if you can seduce this guy. Make it clear that you want to meet up and go back to his place, okay?"
    the_person "Umm... okay?"
    mc.name "When you do, me and [mc.business.head_researcher.fname] will be there. We'll get some blackmail material on him and then decide our next move."
    the_person "Okay... but like... I won't have to actually do anything with him... right?"
    mc.name "Of course not. We'll be there to put a stop to anything."
    the_person "Hmm... okay... I guess I can try."
    mc.name "Alright. I'm going to coordinate this with the head researcher. Go ahead and get back to work."
    the_person "Yes sir."
    $ the_person.draw_person(position = "walking_away")
    "As [the_person.possessive_title] turns and leaves the office, you call your head researcher to your office."
    $ clear_scene()
    $ the_person = mc.business.head_researcher
    $ the_person.draw_person()
    the_person "You wanted to see me?"
    mc.name "I do. I need you to procure some equipment for me."
    the_person "Oh?"
    mc.name "I need some remote monitoring equipment. It needs to be extremely discreet, and capable of 2 way communication."
    the_person "Like... an ear piece? Like from a spy movie?"
    mc.name "Yes, exactly. I also want you to procure a spare set of portable hard drives and computer imaging software."
    the_person "Okay... what for?"
    mc.name "I have [ellie.fname] working on seducing our nanobot contact. If she is successful, I want to go through his home for blackmail material while he is... occupied..."
    the_person "Oh wow! That's pretty ballsy. Are you sure she's up for it?"
    mc.name "Yes, I think so. Are you?"
    the_person "Hell yeah, nothing like some breaking and entering to get the blood flowing."
    mc.name "Good. Acquire is as soon as possible. Charge it to the company account, I'm not sure when we will have our opportunity, but hopefully soon."
    the_person "Yes sir."
    "You share a few more details of your plan with [the_person.possessive_title], then she returns to work."
    $ the_person.draw_person(position = "walking_away")
    "You aren't sure what kind material you will find, going into this guy's apartment, but you are sure you will be able to find something."
    $ clear_scene()
    "There is just one more piece to the puzzle you need..."
    if starbuck_is_business_partner():
        "You place a phone call to your business partner at the mall."
        starbuck "Hello?"
        mc.name "Hey, it's me. I need you to get a few... shall we say... roleplaying outfits for me..."
        starbuck "Oh! Sounds fun! What do you need?"
    else:
        "You look up a listing of businesses at the mall, and one catches your eye."
        "You dial up the listing for the Sex Shop."
        starbuck "Hello?"
        mc.name "Hello. I was hoping to place a special order for some... roleplaying outfits..."
        starbuck "Oh! What are you looking for?"
    "..."
    $ ellie.story_event_log("obedience")
    $ mc.business.add_mandatory_crisis(ellie_search_finish)
    return

label ellie_search_finish_label():    #You and Ellie sabotage the contact
    $ police_chief_wardrobe = wardrobe_from_xml("Cop_Wardrobe")
    $ cop_outfit = police_chief_wardrobe.get_outfit_with_name("Cop")
    $ prostitute_ward = wardrobe_from_xml("Prostitute_Wardrobe")
    $ prost_outfit = prostitute_ward.get_outfit_with_name("Body Suit")
    $ the_person = ellie
    $ the_researcher = mc.business.head_researcher
    $ scene_manager = Scene()
    "You feel your phone vibrate in your pocket."
    $ mc.start_text_convo(the_person)
    the_person "Hey! I got a hit with the contact! Let's meet in your office!"
    mc.name "I'll be right there."
    $ mc.end_text_convo()
    "Before you go to your office, you text [the_researcher.possessive_title]."
    $ mc.start_text_convo(the_researcher)
    mc.name "Hey. Tonight is the night, meet me in my office ASAP, and bring the equipment."
    the_researcher "OMW"
    $ mc.end_text_convo()
    $ mc.change_location(ceo_office)
    "You hurry to your office. [the_person.title] is right behind you."
    $ scene_manager.add_actor(the_person, position = "sitting")
    "She sits down at your desk and starts to talk hurriedly, clearly nervous."
    the_person "I got him to agree to meet up tonight! He wants to meet for a quick bite, then back to his place to 'see what happens'."
    "She cringes a bit with the last part of the sentence."
    mc.name "Excellent job."
    $ scene_manager.add_actor(the_researcher, display_transform = character_center_flipped)
    "[the_researcher.possessive_title] walks into your office, carrying some electronics."
    mc.name "[the_researcher.title], thanks for coming. Did you get the equipment?"
    the_researcher "I sure did. Here's the hard drives, they have software installed to immediately begin imaging and copying any systems they get plugged into..."
    the_researcher "And here is the wire. It should fit nicely into her ear, and with her long hair it will be basically imperceptible unless someone goes looking for it."
    the_person "The wire?"
    mc.name "We are going to give you a recoding and 2 way communication device, that way we can monitor your situation and hopefully get some blackmail material that way as well."
    the_person "I see."
    the_researcher "So like... what are we going to do if his neighbor or something catches us?"
    mc.name "Leave that to me. We have on more stop before dinner time."
    mc.name "Let's go."
    $ mc.change_location(mall)
    $ scene_manager.update_actor(the_person, position = the_person.idle_pose)
    "You go with the two girls to the mall, then walk into the sex shop."
    $ mc.change_location(sex_store)
    "You step into the sex store with [the_person.title] and [the_researcher.possessive_title], looking for someone..."
    $ scene_manager.add_actor(starbuck, display_transform = character_left_flipped)
    if starbuck_is_business_partner():
        starbuck "Hello there, can I help... Oh hey there [starbuck.mc_title]."
        mc.name "Hello [starbuck.title]. I'm here to pick up those outfits I called about the other day."
        starbuck "Oh! The two police uniforms and one 'lady of night' costumes?"
        mc.name "That is them."
        starbuck "Ah! I don't know what you have planned for those, but I wish I could join! You umm... have room for one more?"
        mc.name "Not this time."
        starbuck "What a shame. Give me a moment I'll find them."
    else:
        starbuck "Hello there, can I help you?"
        mc.name "Ah yes, I called in a few days to order a few outfits, two police officers and..."
        starbuck "Ah! And the lady of the night, of course. Give me just a moment, they just came in!"
    $ scene_manager.remove_actor(starbuck)
    the_person "Did she say lady of the night? What... What's that supposed to mean?"
    "[the_researcher.possessive_title] just looks at you with a smirk."
    "After a few moments, [starbuck.possessive_title] returns with the outfits."
    $ scene_manager.add_actor(starbuck, display_transform = character_left_flipped)
    starbuck "Here they are. Did you want to try them on before you buy them?"
    mc.name "Yes. Actually I was hoping we could leave wearing them."
    starbuck "Oh my. What an adventurous group. Yes that would be fine! The dressing room is back there."
    $ scene_manager.remove_actor(starbuck)
    "You walk back to the dressing room with [the_person.possessive_title] and [the_researcher.title]. You each strip down."
    $ scene_manager.strip_full_outfit(strip_feet = True)
    $ mc.change_locked_clarity(50)
    "You quickly check out the two girls before they start getting dressed..."
    $ the_person.apply_outfit(prost_outfit)
    $ the_researcher.apply_outfit(cop_outfit)
    $ scene_manager.update_scene()
    "You check out the two girls and their outfits. Your police officer uniform seems to fit perfectly."
    the_researcher "Wow, this looks just like a real uniform!"
    the_person "I umm... this is pretty umm..."
    the_researcher "Wow [the_person.fname]! You look so hot. Alan is gonna fall into this for sure!"
    the_person "Ahh, yah think so?"
    mc.name "Definitely. This is going to work."
    "You step out of the dressing room with the two girls. A couple is shopping nearby, and the guy notices you, then gives you a wink and thumbs up."
    "You walk over to the checkout counter."
    $ scene_manager.add_actor(starbuck, display_transform = character_left_flipped)
    starbuck "Oh! Those turned out so good!"
    mc.name "They really did. How much do we owe you for the outfits?"
    starbuck "They were about $100 each... OH one second, I almost forgot!"
    "[starbuck.possessive_title] quickly reaches down to a shelf behind the counter, then drops some handcuffs on the counter."
    starbuck "The cop suits came with these. They aren't real, so there is a quick escape button on the side!"
    mc.name "Thanks [starbuck.title]."
    $ mc.business.change_funds(-300)
    "You pay for the outfits before setting out from the sex shop."
    starbuck "Have fun everyone!"
    $ scene_manager.remove_actor(starbuck)
    "You step out into the mall with [the_person.title] and [the_researcher.possessive_title]."
    $ mc.change_location(mall)
    the_researcher "Alright, here's the earpiece. Me and [the_researcher.mc_title] will be listening to everything."
    mc.name "When you get back to his place, see if you can leave the front door unlocked so we can get in easier."
    the_researcher "I'm also recording, so try to get him to say something incriminating."
    mc.name "If you can get him to offer money for sex that would be a big one, obviously."
    the_person "Stars, I never thought I'd be a honeypot. This feels like one of those Jim Bond movies..."
    mc.name "[the_researcher.fname] and I will stay nearby and follow you to his place."
    the_researcher "Don't worry... you'll do great!"
    the_person "Alright... here goes..."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "[the_person.title] turns and walks way, off to meet with Alan for dinner."
    $ scene_manager.hide_actor(the_person)
    the_researcher "Here is a receiver, push this button to talk into it, otherwise it will just receive and record."
    mc.name "Alright, let's find somewhere discreet to be, before someone realizes we aren't really cops..."

    # TODO write rest of scene
    "This part is outlined. Have a scene with the head researcher in discreet while listening to Ellie have dinner."
    "Pick back up following Ellie to Alan's."

    $ mc.change_location(the_person.home)
    "You quietly slip into the contact's apartment with [the_researcher.title] while [the_person.possessive_title] is keeping him occupied."
    "The place is an absolute mess. Dishes are piled up on the small kitchen counter, and there are dirty clothes on the floor."
    "There are three doors, and one is closed with light coming out from underneath it. That must be the bedroom."
    "You take a quick peak into the next and discover a small office. Along one wall, is some heavy duty looking electronic equipment."
    "[the_researcher.title] follows you in, then whispers."
    the_researcher "Huh... I'm not sure what this stuff is..."
    "She takes one of the hard drives over and plugs it into a computer while you start to go through some of the notes."
    "You find something that looks like a journal... it appears to contain a short timeline."
    mc.name "Look here..."
    "At the beginning, it shows his initial contact with [the_researcher.possessive_title], and some notes on the program he wrote."
    "Then it has notes on how he noticed her insta getting more lewd?"
    "Next it notes... production equipment procured? What kind of production equipment?"
    "You show it to [the_researcher.title]."
    the_researcher "Huh... it is like he was stalking me... he makes notes about how my social media got increasingly sexual..."
    the_researcher "What kind of production equipment? Is that what this heavy duty stuff is?"
    "As you look through the office, you are reminded on the monitor that [the_person.title] is in the next room with him..."
    the_person "Mmm, remember the deal though, right? $100 and..."
    "Alan" "Yeah yeah... I was wondering about..."
    "For now, it seems he is still trying to talk her out of charging... you aren't sure if he is suspicious, or just cheap."
    the_researcher "Oh my god... I know what this is..."
    mc.name "What?"
    the_researcher "This is a production rig for the nanobots! He stole the equipment to make them himself!..."
    "She is excited, but is trying to keep her voice down."
    mc.name "Are you sure?"
    the_researcher "I'm positive. He was trying to recreate what we are doing? He even has some test notes.... oh my god..."
    mc.name "What is it?"
    the_researcher "The sick fuck... he was testing them on his SISTER."
    mc.name "Oh my god. What a sick fuck."
    the_researcher "I know... thankfully he had basically zero success. He didn't realize we were combining them with the suggestibility serums..."
    mc.name "Do you have copies of his research data?"
    the_researcher "Almost... it is still copying..."
    $ mc.change_location(the_person.bedroom)
    $ scene_manager.hide_actor(the_researcher)
    $ scene_manager.show_actor(the_person, position = "stand3")
    "Alan" "Okay, okay. $100 it is. I have the cash right here."
    the_person "Oh! That's... perfect... let me just count it real quick..."
    "Alan" "It's all there. Now get on your knees whore, I need this."
    $ ellie_ntr = False
    if persistent.show_ntr:
        "Oh no, it sounds like [the_person.title] is about out of time. You should probably step in now..."
        "Or should you? You need a few more minutes to finish copying the files... Should you stall a little longer? Or step in before [the_person.title] gets taken advantage of?"
        menu:
            "Step in right away":
                "You quietly push the button to talk to [the_person.title]."
                mc.name "Don't worry, we'll be there in a few seconds, help is on the way [the_person.title]."
                $ the_person.change_love(3, 80)
                $ the_person.change_happiness(5)
                $ mc.change_location(the_person.home)
                $ scene_manager.hide_actor(the_person)
                $ scene_manager.show_actor(the_researcher)
                "You look at [the_researcher.title]."
                mc.name "We need to get in there. Let these things keep copying... we might have to improvise a little."
                the_researcher "Ok, I'm sure we can still get the information we need..."
                mc.name "Get your handcuffs ready."
                the_researcher "They aren't real?"
                mc.name "Yeah, but HE doesn't know that."

            "Stall for a few more minutes" if persistent.show_ntr:
                $ ellie_ntr = True
                "You quietly push the button to talk to [the_person.title]."
                mc.name "We found some good stuff, but we need a few more minutes to copy files. You're doing great, do what you have to do, [the_person.title]."
                the_person "Oh stars..."
                $ the_person.change_obedience(2)
                $ the_person.change_love(-2)
                $ the_person.change_happiness(-10)
                "Alan" "Yeah, it IS big, ain't it?"
                the_person "Oh uhh, yeah. So big..."
                "Alan" "That's right. Now choke on it whore."
                $ scene_manager.update_actor(the_person, position = "blowjob")
                "Through the receiver, you listen as blowjob noises begin."
                "You can hear [the_person.title] lips smack and the soft sounds of sucking start coming through the received."
                "Alan" "Ohh, that's it. Swallow it all bitch."
                $ mc.change_location(the_person.home)
                $ scene_manager.hide_actor(the_person)
                $ scene_manager.show_actor(the_researcher)
                mc.name "Alright, she's buying us some extra time, let's make sure we get everything we need."
                the_researcher "Poor [the_person.fname]... she's taking one for the team, so to speak..."
                "You continue going through the research notes, while you hear the blowjob noises continue on the other side of the receiver..."
                the_person "Ulg.... ULGGG"
                "[the_person.possessive_title] gags a couple times, follow by some coughing."
                "Alan" "I guess you need more practice, whore. Take a breath. Now get back to work."
                "The sounds of gagging and slobbering continue."
                mc.name "Do you think we can get this production equipment out of here?"
                the_researcher "Umm... I mean we probably could, but he would probably hear it..."
                mc.name "Maybe it's time for us to intervene... We might have to freestyle a bit."
                mc.name "Get your handcuffs ready."
                the_researcher "They aren't real?"
                mc.name "Yeah, but HE doesn't know that."
                "Alan" "Oh fuck, that's it bitch! Get ready I'm going to cum all over that pouty little face of yours!"
                "You hear a loud pop in the receiver you assume is the contact pulling out of [the_person.title]'s mouth..."
                "Alan" "Fuck! OH FUCK YEAH!"
                $ cum_on_face_ntr(the_person)

            "Stall for a few more minutes (disabled)" if not persistent.show_ntr:
                pass
    else:
        "You didn't allow things to go this far so that another man could get sucked off by [ellie.possessive_title]. It's time to end this."
        "You quietly push the button to talk to [the_person.title]."
        mc.name "Don't worry, we'll be there in a few seconds, help is on the way [the_person.title]."
        $ the_person.change_love(3, 80)
        $ the_person.change_happiness(5)
        "You look at [the_researcher.title]."
        mc.name "We need to get in there. Let these things keep copying... we might have to improvise a little."
        the_researcher "Ok, I'm sure we can still get the information we need..."
        mc.name "Get your handcuffs ready."
        the_researcher "But they aren't real?"
        mc.name "Yeah, but HE doesn't know that."
    "You step out of the office and next to the bedroom door."
    "You count down from 3, then kick the door open as loudly as possible."
    $ mc.change_location(the_person.bedroom)
    $ scene_manager.show_actor(the_person, display_transform = character_left_flipped, position = "standing_doggy")
    mc.name "POLICE! Stop right there!!!"
    "[the_person.possessive_title] is bent over the contact, his cock in her hand."
    "Alan" "Wha... what!?!"
    mc.name "Deputy! Cuff him to the chair."
    the_researcher "Yes sir."
    $ scene_manager.update_actor(the_person, position = "sitting")
    "[the_person.title] sits on the floor as [the_researcher.possessive_title] walks over and grabs the contact and drag him to a nearby chair."
    $ scene_manager.update_actor(the_researcher, position = "standing_doggy")
    mc.name "Nice work, officer [the_person.fname], we got him paying for sex loud and clear on the wire."
    "Alan" "The wire? Wha... I didn't... you don't work for the cops..."
    "[the_researcher.title] has one hand cuffed down now... she's working on the other hand. Your distraction only has to work for a few more moments..."
    mc.name "Of course she does. Where else was she going to work after she got fired from her job after YOU SET HER UP?"
    "Alan" "Wha? Why I would never... you have no proof!... Wait..."
    "You hear the second set of handcuffs click into place."
    "Alan" "That's... [the_researcher.fname]? But... Oh shit."
    mc.name "That's right. Thank you [the_researcher.title]."
    $ scene_manager.update_actor(the_researcher, position = "stand3")
    the_researcher "My pleasure."
    "Alan" "That... that makes you..."
    mc.name "Yeah yeah. Thought you could ghost us, did you?"
    "Alan" "I..."
    mc.name "We found all kinds of equipment in your office. Oh, and evidence, too."
    mc.name "Your sister though? Really?"
    "Alan" "It isn't what you think!"
    mc.name "Isn't it? No matter. We'll be taking that with us. Along with the production equipment."
    "Alan" "Hey! You can't steal that!"
    mc.name "Can't we? Are you telling me you acquired it legitimately? What exactly are you going to do about it?"
    "The contact turns red in the face as he realizes just how much shit he is in. Stolen equipment, unethical research, you've got him by the balls."
    $ scene_manager.update_actor(the_person, position = the_person.idle_pose)
    the_person "That's right! And making it look like I was the one who did it!"
    "Alan" "Ellie... it wasn't anything personal..."
    the_person "Nothing personal... stars... No Alan, when you go after a person's integrity, you MAKE it personal."
    the_person "If things were different, I would have you arrested for what you've done."
    the_person "But you are lucky... that I was able to find another job, doing work more exciting and cutting edge than anything I did before."
    "Alan" "You... you aren't going to release any of that data... are you?"
    mc.name "Maybe. Maybe not. We'll see. But secrets carry a price. Be ready for it."
    "The contact just looks down. You look at the two girls and motion for them to follow you out of the room."
    $ mc.change_location(the_person.home)
    "You leave him there, cuffed to a chair, going back to his office."
    if ellie_ntr:
        the_person "Let me just... wash up really quick..."
        $ scene_manager.hide_actor(the_person)
        $ the_person.apply_outfit(prost_outfit)
        $ scene_manager.update_scene()
    $ scene_manager.update_actor(the_researcher, position = "standing_doggy")
    "[the_researcher.possessive_title] checks the computer."
    the_researcher "Looks like the drives are done copying. We should have everything we need."
    "She unplugs the drives and collects them. You look at the production equipment."
    if ellie_ntr:
        $ scene_manager.show_actor(the_person, emotion = "happy")
        "Your [the_person.possessive_title] walks back in, with a smile."
    mc.name "Let's take this with us."
    the_person "If you ever get caught with it, there could be serious legal implications."
    mc.name "Then let's not get caught."
    "[the_person.possessive_title] helps you break down the equipment enough to move it. You put the pieces into your backpacks."
    $ scene_manager.update_actor(the_researcher, position = the_researcher.idle_pose)
    mc.name "Alright, let's get out of here."
    "You walk out of the contact's apartment. You can hear him yelling after you."
    "Alan" "Hey! You aren't... you can't leave me like this!?!"
    # TODO if you have beta male obedience serum for ashley, give the option to use it here.
    $ mc.change_location(downtown)
    "[the_person.title] chuckles as you step outside the apartment."
    mc.name "I'm sure he'll figure out those cuffs have an easy release button sooner or later..."
    $ mc.change_location(mc.business.r_div)
    "You and the two girls take your loot back to the research department. You start to unload your new equipment."
    the_researcher "We'll have to keep this somewhere secure."
    "You look at the nanobot production equipment."
    mc.name "Honestly, it looks like just about any other research equipment. I don't think anyone would know what it is unless they were looking for it specifically."
    mc.name "And if someone comes along looking for it... well I think we will already have other problems."
    the_person "True... I can probably get it set up... but it is going to take me some time I think."
    mc.name "Sounds good. You don't have to make it a high priority, we aren't going to run out of nanobots anytime soon, but it would still be useful to have running."
    mc.name "Good work today girls. We have all the blackmail material we need on the contact, if we ever need anything from him."
    the_person "If we just want to make him sweat a little."
    the_researcher "Or if we ever need a male test subject."
    $ scene_manager.remove_actor(the_researcher)
    "[the_researcher.possessive_title] unpacks, then says goodbye and leaves, but [the_person.title] sticks around..."
    the_person "Hey, before I go... I need to say something."
    mc.name "Sure."
    if ellie_ntr:
        the_person "I know it is important that we got all the stuff that we did but... I really wish you hadn't let things go so far with me and Alan."
        the_person "It was awful... the whole time I just kept telling myself... just pretend it's [the_person.mc_title]..."
        the_person "I don't know if I can ever do that again... please don't make me do that again, okay?"
    else:
        the_person "Thank you for stepping in when you did. I... I really thought I was going to have to suck that man's dick."
        the_person "I'm not sure I could have done it... I was freaking out so bad!"
        the_person "Please tell me you'll never make me do anything like that?"
    menu:
        "Be strict":
            mc.name "[the_person.title]... I can't make that promise. There may be times that I need you to accomplish things that might get messy."
            mc.name "But I want you to understand something. Just because I allow something like that to happen, doesn't make you any less mine."
            mc.name "Do you understand?"
            "[the_person.possessive_title] sighs."
            the_person "Yes sir."
            $ the_person.change_slut(3, 80)
        "Be Reassuring":
            mc.name "[the_person.title]... I appreciate you being flexible like that. But don't worry, I won't put you in that position again."
            the_person "Thank you! I really needed to hear that..."
            $ the_person.change_love(3, 80)
    $ the_person.change_obedience(5)
    "You give her ass a quick swat."
    mc.name "Now let's get going. We have a lot of work to do, but let's get some rest now."
    the_person "Yes [the_person.mc_title]!"
    $ mc.business.add_mandatory_crisis(ellie_submission)
    $ ellie.story_event_log("obedience")
    return

label ellie_submission_label():   #Ellie submits herself to be used by MC
    $ the_person = ellie
    $ mc.change_location(lobby)
    "Closing time. You make your rounds through the business, making sure the lights are off and the rooms are empty."
    $ mc.change_location(mc.business.r_div)
    $ the_person.draw_person(position = "walking_away")
    "You enter the research department. You notice [the_person.possessive_title] standing at her desk, and barely hear her muttering to herself."
    the_person "I said work... there's no reason in on god's name that you shouldn't be working you piece of..."
    "You walk behind her and put your hands on her shoulders."
    $ the_person.draw_person(position = "back_peek")
    the_person "Stars! Oh hi [the_person.mc_title]."
    mc.name "Everything going okay over here?"
    the_person "Yes... but actually no. I'm trying to get this blasted nanobot tool to work, but the data protocols just don't seem to be working right!"
    mc.name "Sounds complicated."
    the_person "Everything about nanotech is complicated, and this certainly isn't my specialty."
    "She sighs."
    $ the_person.draw_person(position = "standing_doggy")
    "[the_person.title] bends over and starts typing on her terminal... her ass pointing back, straight at you."
    "It makes an incredibly tantalizing target..."
    "*SLAP*"
    the_person "Aghhhnnnhhh!"
    $ the_person.change_arousal(3)
    $ the_person.draw_person(position = "back_peek")
    "[the_person.possessive_title] let's out a... did that turn into a moan?"
    $ mc.change_locked_clarity(10)
    the_person "[the_person.mc_title]!... Wha... what was that for...?"
    mc.name "All my employees know what happens when they bend over like that in front of me."
    the_person "Oh... is that so?..."
    "[the_person.title] bites her lip for a second. She looks around the room, realizing that you are alone together."
    $ the_person.draw_person(position = "standing_doggy")
    "Then bends over and returns to typing, her ass pointing back at you. A switch flips in your brain as you realize what is happening."
    "[the_person.possessive_title] is actively seeking your attention and approval now, of her work AND her body."
    "You decide it is time to see how she reacts if you rough things up a bit."
    "You put your hand on her hip and run it across her back, then down her ass, stopping to grope one of her cheeks."
    mc.name "Still working on the production equipment then? It sure does seem to be taking you a long time."
    "*SLAP*"
    the_person "Ahh!"
    $ mc.change_locked_clarity(10)
    $ the_person.change_arousal(5)
    "You give her ass a hard spank, she gasps out a mixture of pleasure and pain."
    the_person "Sir? I..."
    "Her voice has a hint of fear in it."
    mc.name "Shhh... Let's just roleplay a little. I know you're working hard, but let's have a little fun with it."
    the_person "Ah... yes sir..."
    "You softly rub her ass where you just spanked a moment earlier. The you pull back and swing at the other cheek."
    "*SLAP*"
    the_person "Mmmf..."
    $ mc.change_locked_clarity(10)
    $ the_person.change_arousal(5)
    mc.name "Yes, you've been slacking haven't you? Waiting for me to notice? Waiting for me to come over here and bend you over like the bad little girl you are?"
    the_person "Of course not! I don't..."
    "*SLAP*"
    $ mc.change_locked_clarity(10)
    $ the_person.change_arousal(5)
    the_person "Oh stars, yes sir! I've been hoping you would notice me..."
    mc.name "I know. Come here you little slut. I'm going to have to teach you a lesson."
    "You sit down in her chair, then grab her by the hips. You pull her onto your lap while she is still leaning over. You stick out one leg, bending her over your knee while she hangs onto the edge of the desk."
    $ the_person.draw_person(position = "doggy")
    if the_person.vagina_available():
        "You softly rub her bare ass, bent over your knee. There are couple red circles starting to form, one on each ass cheek."
    else:
        mc.name "Of course, if we are going to do this properly, we're going to have to get these out of the way..."
        "[the_person.possessive_title] ass shakes pleasantly as you pull her bottoms down..."
        $ the_person.strip_to_vagina(prefer_half_off = False, position = "doggy")
        "Once her ass is bare, you gently rub the two red circles starting to form, one on each cheek."
    "*SLAP*, *SLAP*"
    "You give each rosey cheek another spank. Her voice trembles with a moan."
    $ mc.change_locked_clarity(20)
    $ the_person.change_arousal(10)
    the_person "Ahhh, I'm sorry sir, I'll have the equipment working soon I..."
    "*SLAP*"
    the_person "AHH!"
    $ mc.change_locked_clarity(20)
    $ the_person.change_arousal(10)
    "You give her ass a harded spank this time."
    mc.name "Shhh, I didn't tell you to speak. I understand exactly what is going on, and right now, it is time to take your punishment without excuses."
    $ the_person.change_obedience(2)
    "You run your hand between her cheeks now, down and between her legs, along her slit."
    "Your attention is starting to get her wet. Having the busty red head bent over your knee is starting to get you really turned on too."
    $ mc.change_arousal(10)
    "You give her rosey cheeks another thorough round of spanking. She gasps or moans with each strike."
    $ mc.change_locked_clarity(50)
    $ the_person.change_arousal(20)
    $ mc.change_arousal(20)
    the_person "Ahhh!"
    "You decide to give her a break from the spanking for a few moments. You run your fingers along her slit again, finding her to be even more aroused."
    "You push a finger inside her and she moans loudly. Her body shakes a little bit with your intrusion."
    the_person "Ohhh that feels so good... oh stars [the_person.mc_title]..."
    $ mc.change_locked_clarity(50)
    $ the_person.change_arousal(20)
    $ mc.change_arousal(10)
    mc.name "You like it, don't you? Having my finger inside your needy cunt?"
    if ellie_has_given_virginity():
        "Note from the author. You have already had sex with [the_person.title]."
        "However, you can reset her virginity status now to experience this part of the story as if it were her first time."
        "Would you like to experience this event as if she is still a virgin?"
        menu:
            "Yes. Take her virginity (again)":
                $ restore_virginity(the_person)
            "No.":
                pass
    if ellie_has_given_virginity():
        mc.name "Don't worry. I'll replace it with my cock soon. Once your punishment is complete anyway."
        "You pull your finger out then give her ass cheeks another series of spanks. She is starting to wince with each one."
        $ mc.change_locked_clarity(50)
        $ the_person.change_arousal(20)
        $ mc.change_arousal(10)
        the_person "Stars... [the_person.mc_title]... please..."
        mc.name "Please what? I want you beg for what you want."
        the_person "Sir! Please... please fuck me now! I want you to fill me up again!"
        $ mc.change_locked_clarity(50)
        "The busty redhead is begging you to fuck her. It has been a long road to get her here, but having her beg you now, to put your cock inside her, makes it all worth it."
        mc.name "Mmm... okay slut. Bend over your desk and get ready for me."
        "You let her off your knee and she quickly bends over her desk, her ass still pointed at you."
        $ the_person.draw_person(position = "standing_doggy")
        "Her sorry little cheeks are red like her hair. You pull of your pants and get behind her, run your dick along her slit a few times."
        "You put one hand on her hip, and with the other you grab the back of her hair. You line yourself up then push yourself deep inside her in one quick thrust."
        the_person "Yes! Oh stars yes fuck me [the_person.mc_title]!"
        "You pull her hair a bit to remind her you are in control, but you begin to do exactly as she asks."
        call fuck_person(the_person, private=True, start_position = SB_doggy_standing, start_object = make_desk(), skip_intro = True, skip_condom = True) from _call_fuck_person_ellie_obedience_60_02
    else:
        the_person "Yes, yes sir. It feels so good."
        "[the_person.title]'s hips move back and forth with your hand as you finger her. The busty redhead is putty in your hands now."
        "You decide it is time to take the next step, to gain carnal knowledge of the submissive minx."
        mc.name "[the_person.fname]..."
        "She pauses when she hears you use her first name."
        the_person "Y... yes?"
        mc.name "It's time."
        "You feel her body quiver for a second when she hears your words."
        the_person "For what...?"
        mc.name "Don't play coy. You know what it is time for."
        "You push a second finger into her incredibly tight little breeding hole."
        the_person "I know... I'm scared, [the_person.mc_title]..."
        mc.name "I know. But it'll be okay. You enjoyed your spanking, didn't you? This will be just as good."
        the_person "Are you sure?"
        mc.name "Yes. Now bend over my desk. I'm going to fuck you now."
        $ the_person.change_arousal(25)
        the_person "Oh stars... yes sir."
        "You let her off your knee, and she slowly bends over her desk for you."
        $ the_person.draw_person(position = "standing_doggy")
        the_person "I'm ready sir... do whatever you want with me... I'm yours to do what you want with..."
        "Her soft words convey her total submission to you. It is time to take her virginity."
        "You stand up and take off your pants, ready for the deed. She seems ready for anything that is about to happen, but stop for a moment."
        "Should you wear a condom? You have no idea if she is on birth control..."
        menu:
            "Put on a condom":
                $ mc.condom = True
                mc.name "I'm going to put on a condom, that way I don't have to worry about pulling out."
                the_person "Okay, if that is what you want."
                "You reach over to your pants, grab your wallet and quickly pull out a condom. You quickly slide it on."
            "Go bareback":
                mc.name "I'm going to fuck you raw. If you want me to pull out, I can try, but I'm not going to promise I'll be able to."
                the_person "That's okay. I kind of want to know, what it feels like... to take your seed..."
                the_person "But if you want to pull out, you can do that too. Do what you want with me."
                "[the_person.possessive_title] blushes with the last of her words."
                $ the_person.increase_opinion_score("bareback sex")
                $ the_person.increase_opinion_score("creampies")
        "You step directly behind her. You run the length of your erection up and down her slit a few times. She is ready for you."
        mc.name "Alright. Here we go."
        "With your hands on both her hips, you slowly push your cock into her virin entrance. It yields slowly for a bit, then stops."
        "With one smooth motion, you pull her hips back with your hands and push forward, your cock pushing through her hymen, deep inside of her."
        $ take_virginity(the_person)
        $ the_person.draw_person(position = "standing_doggy")
        "Another small push, and you bottom out inside of her. You are finally balls deep inside of [the_person.possessive_title]."
        call fuck_person(the_person, private=True, start_position = SB_doggy_standing, start_object = make_desk(), skip_intro = True, skip_condom = True, condition = make_condition_taking_virginity()) from _call_fuck_person_ellie_obedience_60_01
        $ the_person.change_obedience(5)
    "When you finish with her, [the_person.title] slumps over her desk. Her well used ass is still bare and pointing back at you."
    $ the_person.draw_person(position = "standing_doggy")
    $ the_person.unlock_spanking()
    $ the_person.increase_opinion_score("being submissive")
    "You can now spank her whenever you please."
    mc.name "Fuck, you are a such a hot lay. I'm going to finish closing up, you should clean up and head home."
    the_person "Yes sir... I just need a moment."
    $ clear_scene()
    "You leave the research department to finish closing up your business. You swing back by research before you leave to verify she left."
    "[the_person.possessive_title] is getting more and more submissive. You feel like you are so close to breaking her completely to your will."
    "You should try to keep increasing her obedience and see what happens."
    $ ellie.event_triggers_dict["has_submit"] = True
    $ ellie.story_event_log("obedience")
    $ ellie.add_unique_on_room_enter_event(ellie_nanobot_fetish_testing)
    return

label ellie_nanobot_fetish_testing_label(the_person):   #MC has ellie test fetish impact of nanobots
    $ ellie.event_triggers_dict["fetish_avail"] = True
    $ ellie.story_event_log("obedience")
    return

label ellie_nanobot_fetish_label(the_person):   #After first test, MC can give ellie additional fetishes at will.
    pass
    $ ellie.story_event_log("obedience")
    return



init -1 python:
    def ellie_is_working_on_nanobots(): #This should probably always return true now since she is in R&D
        if ellie.location == mc.business.r_div and mc.business.IT_project_in_progress is not None:
            if mc.business.IT_project_in_progress in nanobot_IT_project_list:
                return True
        return False

    def ellie_is_working_on_project():
        if ellie.location == mc.business.r_div and mc.business.IT_project_in_progress is not None:
            return True
        return False

    def ellie_is_a_squirter():
        return ellie.event_triggers_dict.get("squirts", False)

    def ellie_has_been_fingered():
        return ellie.event_triggers_dict.get("been_fingered", False)

    def ellie_has_given_handjob():
        return ellie.event_triggers_dict.get("given_handjob", False)

    def ellie_has_given_blowjob():
        return ellie.event_triggers_dict.get("given_blowjob", False)

    def ellie_has_given_virginity():
        return ellie.event_triggers_dict.get("given_virginity", False)

    def ellie_has_given_anal_virginity():
        return ellie.event_triggers_dict.get("given_anal_virginity", False)

    def ellie_has_tit_fuck():
        return ellie.event_triggers_dict.get("tit_fuck", False)

    def ellie_has_brought_lunch_date():
        return ellie.event_triggers_dict.get("brought_lunch", False)

    def ellie_has_cooked_dinner_date():
        return ellie.event_triggers_dict.get("dinner_date", False)

    def ellie_work_crisis_unlocked():
        return ellie.event_triggers_dict.get("work_turnon", False)

    def ellie_has_anal_fetish():
        if "ellie" in globals():
            return ellie.has_anal_fetish()
        return False

    def ellie_has_cum_fetish():
        if "ellie" in globals():
            return ellie.has_cum_fetish()
        return False

    def ellie_has_breeding_fetish():
        if "ellie" in globals():
            return ellie.has_breeding_fetish()
        return False

    def ellie_has_exhibition_fetish():
        if "ellie" in globals():
            return ellie.has_exhibition_fetish()
        return False
