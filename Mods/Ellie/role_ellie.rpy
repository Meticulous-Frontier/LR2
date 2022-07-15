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
            mandatory_duties = [hr_work_duty], available_duties = [] + general_duties_list + general_hr_duties)

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

        mc.business.add_mandatory_crisis(ellie_start_intro_note) #Add the event here so that it pops when the requirements are met.

        #We usually set progress screen info here, but we wait until appropriate in the story to do it, since Ellie is initially a ?????

        # set relationships
        # Ellie is relatively new in town and has no mutual relationship with MC
        ellie.text_modifiers.append(southern_belle)
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
        if ellie_is_working_on_nanobots() and ellie.sluttiness >= 20:
            return True
        if ellie.location == mc.business.r_div and ellie.sluttiness > 40 and mc.business.is_open_for_business():
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

    def ellie_never_tasted_cock_requirement(the_person):
        if the_person.sluttiness >= 40 and mc.is_at_work() and mc.business.is_open_for_business():
            if get_random_employees(1, exclude_list = [the_person], slut_required = 50):
                return True
        return False

    def ellie_never_been_fucked_requirement(the_person):
        return False

    def ellie_loses_her_virginity_requirement():
        return False

    def ellie_never_tried_anal_requirement():
        return False

    def ellie_turned_on_while_working_intro_requirement(the_person):
        return False

    def ellie_turned_on_while_working_requirement():
        return False

    def ellie_brings_lunch_requirement():
        if ellie.love >= 40 and mc.is_at_work() and mc.business.is_open_for_business() and time_of_day == 1:
            return True
        return False

    def ellie_dinner_date_intro_requirement():
        return False

    def ellie_dinner_date_requirement():
        return False

init -1 python:
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
    ellie_never_given_handjob = Action("Ellie wants to touch", ellie_never_given_handjob_requirement, "ellie_never_given_handjob_label")
    ellie_never_tasted_cock = Action("Ellie wants to taste", ellie_never_tasted_cock_requirement, "ellie_never_tasted_cock_label")
    ellie_never_been_fucked = Action("Ellie wants to fuck", ellie_never_been_fucked_requirement, "ellie_never_been_fucked_label")
    ellie_loses_her_virginity = Action("Ellie loses her cherry", ellie_loses_her_virginity_requirement, "ellie_loses_her_virginity_label")
    ellie_never_tried_anal = Action("Ellie tries anal", ellie_never_tried_anal_requirement, "ellie_never_tried_anal_label")
    ellie_brings_lunch = Action("Ellie likes cooking", ellie_brings_lunch_requirement, "ellie_brings_lunch_label")
    ellie_dinner_date_intro = Action("Ellie asks for a dinner date", ellie_dinner_date_intro_requirement, "ellie_dinner_date_intro_label")
    ellie_dinner_date = Action("Ellie cooks for you", ellie_dinner_date_requirement, "ellie_dinner_date_label")
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
    $ mc.location.show_background()
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
    $ mc.location.show_background()
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
    if the_person == None:
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
    $ mc.location.show_background()
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
    $ mc.location.show_background()
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
    $ mc.location.show_background()
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
    mc.name "However, I'm not sure that, due to the size of the company, I'll be able to keep you busy full time with those projects, so when you have down time, I'll assign you to the HR department."
    mc.name "We'll make HR department your official job position, with the other projects on the side. How does that sound?"
    the_person "Well... that sounds okay, I guess. What kind of security policies do you currently have in place?"
    mc.name "Ah, well... we use the anti-virus software that came with the computers..." #BB- I changed it to this because it seems like something someone unfamiliar with network security would say
    the_person "Lordie. You don't have any kind of security measures in place?"
    mc.name "That's just something we haven't given much thought..." #BB- Network security would be an oversight for a small business
    the_person "Alright. Tell you what, I'll look things over today and I'll see what I can do. I'll do some research over the weekend and on Monday I'll let you know what I decide."
    mc.name "Deal! Why don't we get your onboarding paperwork complete?"
    the_person "Okay."
    $ the_person.draw_person(position = "sitting")
    "You sit down at your desk, filling out some paperwork and getting her officially hired by the company."
    $ mc.business.add_employee_hr(the_person)
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
        ellie "Alright well, when you decide what you want me to work on, let me know, I'll be in HR."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] gets up and starts to walk away. You have now unlocked IT projects!"
    "Talk to your IT director to change projects when she is at work. If she is working on developing a new project, she will be in the Research Department."
    $ ellie.add_unique_on_room_enter_event(ellie_never_been_kissed)
    $ mc.location.show_background()
    return


label ellie_never_been_kissed_label(the_person):  #This is Ellies 20 sluttiness event.
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
    the_person "I just don't understand why you all got to use them bots for making women do, you know, fornicating."
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
    $ ceo_office.show_background()
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
    $ the_person.change_obedience(20)
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
        call fuck_person(the_person, private=True, start_position = cum_fetish_blowjob, start_object = make_floor(), skip_intro = True) from _call_ellie_arousal_relief_01
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
        call fuck_person(the_person, private=True, start_position = blowjob, start_object = make_floor(), skip_intro = True) from _call_ellie_arousal_relief_04
    if mc.arousal < 20:
        "After you finish, you feel much better."
        mc.name "Thank you [the_person.title], I really needed that."
        the_person "Glad to help!"
        $ the_person.change_stats(happiness = 10, love = 5, obedience = 10)
    $ clear_scene()
    "You dismiss her. After you get yourself cleaned up, you get back to work."
    $ mc.location.show_background()
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
    the_person "Can... can I try? I want to try something I read about."
    mc.name "Well, I might be up for that, but it depends on what exactly you have in mind."
    the_person "I mean, since then, I've seen all kinds of methods... but I think I can just use my hand... right?"
    mc.name "[the_person.title], are you saying you want to give me a handjob?"
    the_person "Eh!? I mean, you make it sound so dirty, I just..."
    "She is kind of cute when she gets disgruntled."
    the_person "I just want us to be even, okay? I hate the thought of leaving your poor thing all pent up..."
    "You keep quiet about the fact that you've had multiple releases since the incident."
    mc.name "Well I think that's great. I would love to have a nice handjob right now."
    $ the_person.change_slut(2)
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
    if not the_person.is_willing(tit_fuck):
        #TODO something here to make sure she it willing to tit fuck.
        pass
    the_person "[the_person.mc_title], this feels so hot, I want to do something else too that I saw."
    mc.name "Oh?"
    the_person "[the_person.mc_title], can I put it between my boobies?"
    mc.name "[the_person.title], when you're doing sexual stuff like this, you can call them titties. And yes, that sounds amazing."
    mc.name "Let me feel your big titties wrapped around my cock!"
    "[the_person.possessive_title] lifts up her knees a little. She looks up at you, obviously still a little unsure, but you nod your encouragement."
    "You help press forward a bit when her soft tit-flesh finally makes contact with your groin. You take her hands in yours and show her how to wrap her tits around you."
    mc.name "There, now just... bounce them a little."
    the_person "Ah, okay."
    "[the_person.title] uses her hands to move her big tits up and down your cock. The soft flesh feels amazing sliding up and down."
    $ mc.change_locked_clarity(30)
    $ the_person.change_arousal(5)
    mc.name "Ah, this feels amazing. I'm not going to last very long like this. You know what is going to happen when I finish... right?"
    the_person "It's gonna spurt out... right?"
    mc.name "Yeah."
    the_person "I... I'm getting all kinds of crazy feelings right now. I kind of want you to do it on my boo... on my titties, [the_person.mc_title]."
    $ mc.change_arousal(10)
    mc.name "Oh fuck, okay, I'll cum all over your big titties, [the_person.title]."
    "Your pre-cum is leaking pretty heavily now. It adds to the pleasure of [the_person.possessive_title] fucking you with her tits."
    mc.name "Spit some."
    the_person "Okay."
    "She stops moving her tits for a second to spit down into her cleavage. She moves her breasts up and down, slathering you up before continuing."
    $ mc.change_locked_clarity(50)
    mc.name "Oh god. [the_person.title], I'm almost there. Keep going!"
    the_person "Okay [the_person.mc_title]!"
    "This southern redhead's big titties are amazing, bouncing up and down around your cock. It's getting ready to burst."
    $ mc.change_locked_clarity(50)
    $ ClimaxController.manual_clarity_release(climax_type = "tits", the_person = the_person)
    $ the_person.event_triggers_dict["given_handjob"] = True

    "Your orgasm builds to a peak and you grunt, blasting your load up between [the_person.title]'s tits and out the top of her cleavage."
    $ the_person.cum_on_tits()
    $ the_person.draw_person(position = "kneeling1")
    "Your cum splatters down over the top of [the_person.title]'s tits. She gasps as the warm liquid covers her and drips back down between them."

    "She looks up at you. She has no idea what to do."
    the_person "Mister I... I mean [the_person.mc_title]..."
    mc.name "Hang on, let me get you some tissues and wet wipes."
    "You quickly walk back to your desk and pull some out and hand them to her."
    $ the_person.draw_person()
    the_person "There's so much! Is it... is it because you had blue balls?"
    "You can't help but laugh this time, caught off guard by her pronunciation again."
    mc.name "No, that's about how much usually comes out."
    "You help her get cleaned up, then back into her outfit."
    $ the_person.apply_planned_outfit()
    $ the_person.draw_person()
    mc.name "That was amazing."
    the_person "Ah, yeah that was nice. Do you want to do it again sometime?"
    mc.name "I do. But for now I need to recover a bit before I go back to work."
    the_person "Okay. I'm going to get back to work then."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] awkwardly turns and leaves your office. You can't help but smile."
    "She'll get used to servicing your needs in your office soon enough. For now you are content with the leap of progress you have made with her."
    $ mc.location.show_background()
    $ the_person.add_unique_on_room_enter_event(ellie_never_tasted_cock)
    $ mc.business.add_mandatory_crisis(ellie_brings_lunch)
    return

label ellie_never_tasted_cock_label(the_person):  #This is Ellie's 40 sluttiness event.
    $ talk_person = get_random_employees(1, exclude_list = [the_person], slut_required = 50)
    $ scene_manager = Scene()
    "As you walk towards the entrance of research and development, you begin to overhear a conversation."
    "You stop and listen in before walking in the door, not because of what is being talked about, but because of WHO is talking."
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
        "Cum on her face":
            "You put your hand on the back of her head and pull her off."
            mc.name "Use your hand, I want you jack me off all over your face."
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
    else:
        mc.name "That's a good idea."
        the_person "But umm... can we do this again sometime? I ummm... I might need more practice."
        mc.name "I think that can be arranged."
        $ the_person.draw_person(position = "walking_away")
        "[the_person.possessive_title] awkwardly turns and walks out of your office."
        $ clear_scene()
    "Your conservative, southern belle has now given you a blowjob! And it sounds like she wants to do it again soon!"
    "[the_person.title] now has oral positions unlocked."
    $ mc.business.add_mandatory_crisis(ellie_brings_lunch)  #TODO delete this line with 48.1 release
    $ the_person.add_unique_on_room_enter_event(ellie_turned_on_while_working_intro)
    $ the_person.apply_planned_outfit()
    $ mc.location.show_background()
    #"Ellie may now approach MC once in a while when she is working on nanobot programs because working on sex related code is getting in her head and she needs some relief"
    return

label ellie_never_been_fucked_label(the_person):  #This is Ellie's 60 sluttiness event. Also requires X number of oral encounters?
    "You check up on [ellie.fname] while she is working on nanobot programming stuff."
    "She says working on this program is getting her really worked up. You can tell she's aroused (flushed cheeks, pointy nipples)."
    "She asks if you could fool around a little again. MC says he is tired of foreplay, says she probably just needs a good fucking."
    "She is embarrassed. Says she knows that but she is just scared of having sex for the first time."
    "MC asks if she would be open to sleeping with him if he promises to go slow and be gentle."
    "[ellie.fname] is uncertain. Her mama would be so disappointed."
    "MC offers to take her out on a proper date first, have a couple drinks, go back to her place, she can stop any point she wants to."
    "She says okay. Make a plan for dinner on... some day? Figure out best day."
    "She's still needy right now though. Quick detour to the office for sixty nine."
    "She goes back to work."

    return

label ellie_loses_her_virginity_label():
    "You meet up with [ellie.fname]. Take her out for a nice dinner."
    "Have the option to mess around a little under the table. If you use your foot to rub against her privates, she gains +1 public sex opinion."
    "Also have a drink. At some point she uses ladies room and you can serum her."
    "Like a normal dinner date gain love based on how fancy wine is, how fancy dinner is, etc."
    "When finished, she asks MC back to her place, but says she is still scared."
    "Discover her place."
    "She's nervous, you make out with her for a bit to get her warmed up."
    "Finally go back to her bedroom. She wants to strip for you."
    "Positive remarks give positive view on showing tits, showing ass, no clothes at all, and love gain."
    "Degrading remarks give negative opinion, but gain obedience and sluttiness."
    "If she likes getting head, asks for just a bit of oral. Arousal gain here that sets up MC to make her orgasm more later."
    "Lays down on bed. MC can be gentle for positive vaginal sex opinion, or rough for negative and obedience gain."
    "Mc can ask if she wants condom. She says she wants her first time natural, but appreciates it if MC asks and likes bareback sex. Otherwise dislikes bareback sex if MC doesn't ask."
    "After penetration, use creampie_cum but use red color to make it look like virginity taken."
    "Sex scene. If [ellie.fname] cums twice or more she begs MC to finish inside her. Gain creampie like."
    "If not, she asks MC to pull out. If MC pulls out she likes cum on her body. If he doesn't, she dislikes creampies."
    "Taking [ellie.fname]'s virginity has made her putty in your hands now. She gains large love and obedience bonuses."
    "[ellie.fname] can't believe she did that, she always thought growing up she was saving herself for marriage, but can't believe what she has been missing out on."
    "With high love stat, MC has option to ask her to be his girlfriend. She accepts."
    "Leave her place and go home."
    "You have unlocked [ellie.fname]'s vaginal sex options."
    $ ellie.event_triggers_dict["given_virginity"] = True
    return

label ellie_never_tried_anal_label():   #This is Ellie's 80 sluttiness rating. Must have anal nanobots unlocked.
    pass
    $ ellie.event_triggers_dict["given_anal_virginity"] = True
    return

label ellie_turned_on_while_working_intro_label(the_person):
    $ ellie.event_triggers_dict["work_turnon"] = False
    return

label ellie_turned_on_while_working_label():    #Crisis event. Can be triggered after unlocking Ellie's oral sex options, and procs when she is working on nanobot programming.
    "During a break, you make the rounds to the different departments. When you swing by R&D, you decide to check up on [ellie.fname]"
    "[ellie.fname] is masturbating, trying to type with one hand and playing with herself with the other."
    "She is sorry. Working on this stuff gets her so horny."
    "Initially, you can chastise her (dislikes masturbation), encourage her (likes masturbation), or offer to help her."
    "If you offer to help her, you can do it right there in R&D (likes public sex), or find somewhere private."
    "Her reactions change based on her story and corruption progress. At extreme sluttiness, when she sees you walk up she may jump MC or if submissive, pull down bottoms and bend over her desk and beg."
    "Sex scene."
    return

# Love Scenes
label ellie_brings_lunch_label():   #40 love scene. Brings MC lunch to have a date in his office.
    if ellie_has_brought_lunch_date():  #I left a scenario in game where this could occur twice. IF this event has already occurred, just exit immediately.
        return
    $ the_person = ellie
    $ ellie.event_triggers_dict["brought_lunch"] = True
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
    else:
        "There is some tension in the air... but you decide for now it would be better not to act on it."
        mc.name "Yes, it was great. Thank you again."
        "You stand up and [the_person.title] does the same."
        $ the_person.draw_person()
        "You leave your office together and go back to the work day."

    $ ellie.apply_planned_outfit()
    $ mc.business.add_mandatory_crisis(ellie_dinner_date_intro)
    $ clear_scene()
    $ mc.location.show_background()
    return

label ellie_cunnilingus_office_label(the_person):
    $ the_person.draw_person (position = "sitting")
    $ the_person.arousal = 0
    $ the_person.add_unique_on_room_enter_event(ellie_never_been_fucked)
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
    $ the_person.change_obedience(10)
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

label ellie_dinner_date_intro_label():
    pass
    return

label ellie_dinner_date_label():
    $ ellie.event_triggers_dict["dinner_date"] = False
    return


init -1 python:
    def ellie_is_working_on_nanobots():
        if ellie.location == mc.business.r_div and mc.business.IT_project_in_progress != None:
            if mc.business.IT_project_in_progress in nanobot_IT_project_list:
                return True
        return False

    def ellie_is_working_on_project():
        if ellie.location == mc.business.r_div and mc.business.IT_project_in_progress != None:
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

    def ellie_has_brought_lunch_date():
        return ellie.event_triggers_dict.get("brought_lunch", False)

    def ellie_has_cooked_dinner_date():
        return ellie.event_triggers_dict.get("dinner_date", False)

    def ellie_work_crisis_unlocked():
        return ellie.event_triggers_dict.get("work_turnon", False)
