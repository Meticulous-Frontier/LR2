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

        # init ellie role
        ellie_role = Role(role_name ="ellie", actions =[], hidden = True)

        #global ellie_role
        global ellie
        ellie = make_person(name = "Ellie", age = 24, body_type = "thin_body", face_style = "Face_13",  tits="DDD", height = 0.92, hair_colour="dark auburn", hair_style = bobbed_hair, skin="white" , \
            eyes = "light blue", personality = introvert_personality, name_color = "#228b22", dial_color = "228b22" , starting_wardrobe = ellie_wardrobe, \
            stat_array = [1,4,4], skill_array = [1,1,3,5,1], sex_array = [4,2,2,2], start_sluttiness = 0, start_obedience = 5, start_happiness = 103, start_love = -3, \
            relationship = "Single", kids = 0, force_random = True, base_outfit = ellie_base_outfit,
            forced_opinions = [["production work", 2, True], ["work uniforms", 1, False], ["flirting", 1, False], ["working", 1, False], ["the colour green", 2, False], ["pants", 1, False]])

        ellie.generate_home()
        ellie.set_schedule(ellie.home, times = [0,1,2,3,4])
        # ellie.set_schedule(downtown_bar, times = [2,3])
        ellie.home.add_person(ellie)
        ellie.idle_pose = "stand2"

        ellie.event_triggers_dict["intro_complete"] = False    # True after first talk


        mc.business.add_mandatory_crisis(ellie_start_intro_note) #Add the event here so that it pops when the requirements are met.

        # set relationships
        # Ellie is relatively new in town and has no mutual relationship with MC
        ellie.text_modifiers.append(southern_belle)

        ellie.add_role(ellie_role)
        return

init -2 python: #Requirement Functions

    def ellie_start_intro_note_requirement():
        return False
        if fetish_serum_unlock_count() >= 2 and get_fetish_basic_serum().mastery_level > 3.0 and mc.business.head_researcher:
            if time_of_day == 2 and day%7 == 2 and mc.is_at_work():
                return True
        return False

    def ellie_meet_ellie_intro_requirement():
        if time_of_day == 4 and day%7 == 3:
            return True

    def ellie_head_researcher_halfway_intro_requirement():
        if time_of_day == 3 and day%7 == 0:
            return True
    def ellie_unnecessary_payment_requirement():
        return False
    def ellie_end_blackmail_requirement():
        if time_of_day == 4 and day%7 == 3:
            return True
    def ellie_work_welcome_requirement():
        if time_of_day == 0 and day%7 == 4:
            return True
    def ellie_never_been_kissed_requirement():
        return False
    def ellie_kiss_followup_requirement():
        return False
    def ellie_text_message_apology_requirement():
        return False
    def ellie_never_given_handjob_requirement():
        return False
    def ellie_never_tasted_cock_requirement():
        return False
    def ellie_never_been_fucked_requirement():
        return False
    def ellie_loses_her_virginity_requirement():
        return False
    def ellie_never_tried_anal_requirement():
        return False
    def ellie_turned_on_while_working_requirement():
        return False

init -1 python:
    ellie_start_intro_note = Action("Blackmail Note", ellie_start_intro_note_requirement, "ellie_start_intro_note_label")
    ellie_meet_ellie_intro = Action("Meet Your Blackmailer", ellie_meet_ellie_intro_requirement, "ellie_meet_ellie_intro_label")
    ellie_head_researcher_halfway_intro = Action("Blackmailer Identity", ellie_head_researcher_halfway_intro_requirement, "ellie_head_researcher_halfway_intro_label")
    ellie_end_blackmail = Action("End Blackmail", ellie_end_blackmail_requirement, "ellie_end_blackmail_label")
    ellie_work_welcome = Action("Hire Ellie", ellie_work_welcome_requirement, "ellie_work_welcome_label")

label ellie_start_intro_note_label():
    $ the_person = mc.business.head_researcher
    "You get an email notification on your phone. Normally you would brish something like this off as spam, but the subject line has your name in it."
    "You open it up and are surprised what you are reading. It is short and to the point."
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
    mc.name "So, here is what I am thinking. Across from the alley is bar where you can get on the roof fairly easily."
    mc.name "Can you come with me, but hide up on the roof with like... a camera or binoculars or something? Just watch while I deal with this."
    the_person "Yeah. I can do that. I think I know where you are talking about."
    mc.name "I'll pull out some cash the day of and be ready. Although the email doesn't even say how much cash to bring."
    the_person "Yeah... its a little ambigious... But I can do that."
    "You spend some time in your office with [the_person.title], making a quick and dirty plan for how to deal with the blackmail threat."
    mc.name "Alright, its a plan. I won't meet with you tomorrow night, in case we are being watched or tracked, but its a plan atleast."
    the_person "Ok... We'll talk then."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] gets up and leaves your office. This is a precarious situation, and you can't help but worry about it."
    $ clear_scene()
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
    "You have no idea how organized this person or group is, but you doubt that if things turn sour a taser will make much of a difference, but you decide to keep that to yourself."
    "Hopefully she will go unnoticed if the blackmailer decides to have reinforcements of his own."
    "The blackmail note said to bring cash... But not how much. You pulled some strings at the bank and got $1000 in 20s, hopefully that will be enough."
    "Your business is just getting off the ground, so you really don't have the cash to handle a huge demand."
    "Eventually, the time comes, so you head down the alley. As you hit the halfway mark, a shadowy figure emerges from behind a dumpster."
    $ ellie.draw_person()
    ellie "That's far enough right there y'all."
    "The first thing you notice is the heavy southern twang in her accent. Secondly, it is heavily feminine. A southern woman is blackmailing you? It catches you completely off gaurd."
    ellie "You got cash?"
    mc.name "Yeah, although the note failed to mention exactly how much you were expecting."
    ellie "I'm figurin a million dollars in cold hard cash."
    "You pause. She can't be serious? If she knows anything about your business, she has to know you have no way of pulling that kind of liquidity."
    mc.name "I'm sorry, my business is just founded, and I don't have the ability to pull that much, especially on such short notice."
    ellie "Ah lordie help me. Hmm. How about this. You give me some cash now as a show of good faith, and we'll meet again next week and you kin give me the money then."
    ellie "As a fellow criminal, surely y'all can understand that I got bills to pay."
    "You doubt you will be able to find a million dollars between now and next week, but atleast this will give you some time to try and figure things out."
    mc.name "Alright, that's a deal."
    ellie "Aight. For now, let me have a hundred dollars. That'd outta get me thru until next week..."
    "This whole conversation is throwing up serious red flags. Is she really just asking a hundred for now? The whole thing reeks of amateurism."
    "You look up and around, trying to see if you see any motion or hint that she may have someone else watching, but don't see anything. You decide to play along for now."
    "You pull out a hundred dollars, being careful not to show the remaining bills you have with you, and extend your hand with them."
    "She slowly walks forward and take she money from you. The alley is dark, but is that red hair? She quickly pulls away."
    ellie "Same time next week."
    "The mysterious blackmailer turns and quickly leaves the alley. You stand there observing her until she turns the corner, when you turn around and leave the alley."
    $ clear_scene()
    "Once you are a safe distance away from the alley, you pull out your phone and text [the_person.possessive_title])."
    $ mc.start_text_convo(the_person)
    mc.name "Hey, meet me at the bar. We have a lot to talk about."
    the_person "Okay, see you there"
    $ mc.end_text_convo()
    $ mc.change_location(downtown_bar)
    $ mc.location.show_background()
    $ mc.location.lighting_conditions = standard_indoor_lighting
    "You grab a secluded table away from the crowd around the bar with [the_person.title]."
    $ the_person.draw_person(position = "sitting")
    the_person "So, how'd it go?"
    mc.name "Confusing, to be honest. You see anything from where you were at?"
    the_person "Not much, to be honest. I could tell it was a woman, but I didn't see anyone else and couldn't make out much about her."
    mc.name "Well, first thing, she had a heavy southern accent. She could have been faking it, but I doubt it. The whole thing felt... Like she was an amateur to be honest."
    the_person "Why do you say that?"
    mc.name "Well, she really seemed to have no idea how much money to ask for, so she just said she needed a million dollars."
    the_person "Wow, there's no way you could make a ransom like that, atleast as far as I know."
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
    $ clear_scene()
    $ mc.business.add_mandatory_crisis(ellie_head_researcher_halfway_intro)
    return

label ellie_head_researcher_halfway_intro_label():
    $ the_person = mc.business.head_researcher
    "You feel your phone vibrate in your pocket. its [the_person.possessive_title]"
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
    the_person "I gave him description of the blackmailer, and he finally got back to me this morning."
    the_person "The company launched an investigation trying to figure out who leaked the bots, but they got the wrong person."
    the_person "The company came down hard on a relatively new person. A woman they had hired about a year ago. A fresh computer science college graduate from University of Alabama..."
    mc.name "Ahhhhh"
    the_person "He sent me her basic details..."
    "[the_person.possessive_title] hands you a dossier she has put together on this person. The first thing you notice is her red hair."
    the_person "[ellie.name] [ellie.last_name]. Redhead, souther computer expert."
    mc.name "It's perfect. What happened with her employer?"
    the_person "She got fired. The kicker is, she signed a 5 year non-compete contract when she got hired, and so the company threatened her with lawsuit if she tries to get a job in her field."
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
    mc.name "Alright. Next time I meet with her, I'll consider trying to hire her. If nothing else, maybe I can atleast scare her off."
    the_person "Okay. Let me know if there is anything else I can help out with, [the_person.mc_title]!."
    $ clear_scene()
    "[the_person.possessive_title] gets up and leaves you a lone in your office."
    "You meet again with [ellie.name] on Thursday night. You feel like you could definitely hire her."
    "WARNING: If you want to hire [ellie.name], make sure you have an open employee position! You may miss the opportunity to hire her if you don't!"
    #TODO link up next event.
    $ mc.business.add_mandatory_crisis(ellie_end_blackmail)
    return

label ellie_unnecessary_payment_label():    #Use this scene each week if MC can't find out info on Ellie for some reason (head researcher fired, etc)
    "Meet with Ellie at the drop location."
    "You pay her the money she wants."
    "Over 5 weeks, you learn more about her, eventually find out she's just out of work after being fired."
    "She blames you for being fired. She's kinda right."
    "After 5 weeks you offer her a job."
    return

label ellie_end_blackmail_label():
    $ the_person = ellie
    "As night falls, you make your way downtown. Tonight you are meeting with your blackmailer."
    $ mc.change_location(downtown)
    $ mc.location.show_background()
    $ mc.location.lighting_conditions = dark_lighting
    "The time comes so you head for the allie. As you approach, you hear the southern twang of her accent as she steps from the shadows."
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
    the_person "They fired me... but it was y'all! And now I can't find another job anywhere! Anytime I give my work history, I get an instant no thanks from any employer."
    "She seems ready to chat. Do you want to try and hire her?"
    menu:
        "Hire Her":
            pass
        "Scare her off":
            "She is so emotional. You can't imagine her being a good fit for your company now."
            "You scare her off from blackmailing you using dialogue that Starbuck hasn't written yet."
            #TODO
            #Figure out a way to remove her from the game without breaking stuff.
            return
    mc.name "I get it. You just want to work, and something in your field."
    the_person "I... I just moved here a year ago... I just want to do my family proud..."
    mc.name "What if you came and worked for me?"
    "She startles. She clearly had not expected this at all."
    the_person "Me? Y'all... after I blackmailed you and..."
    mc.name "How did you get information on my company anyway? About the nanobots?"
    the_person "Oh gee, your cyber security is non existent. All y'all have full databases of information without even a firewall to protect it..."
    mc.name "I could really use someone with your talents to help me with stuff like that."
    the_person "I could help... but I can't... I signed a non-compete..."
    mc.name "I run a small company. We all know each other. I could make your official position be in HR, but you could run IT projects for me on the side. Your prior employer doesn't need to know."
    mc.name "I'll match your previous salary plus ten percent. And if you decide to move on, I'll give you a proper reference."
    "She seems skeptical, but agrees."
    the_person "Okay... Let's say I decide I want to try it out."
    mc.name "Come on out to the business tomorrow morning. I'll show you around, give you a chance to settle in, and then you can think about it over the weekend."
    the_person "Okay mister. I'll come out tomorrow and y'all can show me the ropes."
    mc.name "That's all I ask. I think you'll fit right in."
    $ the_person.set_possessive_title("Your IT Girl")
    $ the_person.set_title(the_person.name)
    $ the_person.set_mc_title(mc.name)
    "You exchange some information with [the_person.title]. You feel pretty certain she'll decide to stick around."
    $ mc.business.add_mandatory_crisis(ellie_work_welcome)
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
    mc.name "We'll make HR department your official job position, with the other projects on side. How does that sound?"
    the_person "Well... that sounds okay I guess. What kind of security do you currently have in place?"
    mc.name "Ah, well... we have a fairly short policy book..."
    the_person "Lordie. You don't have any kind of safety measures in place?"
    mc.name "Its a small business..."
    the_person "Alright. Tell you what, I'll look things over today and I'll see what I can do. I'll do some research over the weekend and on Monday I'll let you know what I decide."
    mc.name "Deal! Why don't we get your onboarding paperwork complete?"
    the_person "Okay."
    $ mc.business.hire_person(the_person, "HR")
    $ mc.business.it_director = the_person
    $ mc.business.it_director.IT_tags = {}
    #$ mc.business.hr_director.HR_unlocks = {}
    $ mc.business.it_director.add_role(IT_director_role)

    return

label ellie_never_been_kissed_label():  #This is Ellies 20 sluttiness event.
     "Ellie contacts you. Says working on nanobots has been interesting. Asks if she can share a secret."
     "You find out Ellie grew up religious south (you already suspected and knew some of this). Parents super strict."
     "She lived at home during university and never dated, workaholic at her first job and was too scared to date."
     "She admits she's never been kissed."
     "She's lookin sexy. You ask her if she wants to. She doesn't answer, just looks down."
     "makeout"
     "happy"
     "Grope her"
     "Mega Happy"
     "Finger her"
     "She cums and can't believe it. Thinks she peed herself. Runs out of the room embrassed."
     return

label ellie_kiss_followup_label():
    "Ellie approaches you. Says sorry for peeing on your fingers."
    "That was an orgasm bitch."
    "You send her a link of a sex health website. Tell her to take a look at it over the weekend."
    return

label ellie_text_message_apology_label():
    "Sunday morning, you get a text from Ellie."
    "She's been up all night reading about stuff. Apologizes for being so naive, wants to know if she can make it up to you."
    "heck yes"
    "She asks to meet you early before work on Monday again."
    return

label ellie_never_given_handjob_label():
    "Meet with Ellie monday morning in your office."
    "She locks the door. She asks to see your junk."
    "She can't stop staring at it. Asks if she can touch it."
    "heck yes"
    "She touches it. A little. Then a lot. She ready about men and male orgasms, wants to see one."
    "You guide her through giving handjobs. Cum. She's ecstatic."
    "You've now unlocked all her foreplay options."
    return

label ellie_never_tasted_cock_label():  #This is Ellie's 40 sluttiness event.
    "Ellie has an on room entry event."
    "You hear her asking another girl what its like to suck dick."
    "She gets crazy embrassed when she sees you. Cute"
    "You ask her to come with you to your office. Pretend like you're gonna discipline her for lewd talk."
    "Get to your office, close door, lock it."
    "She starts to say sorry, but instead you stop her."
    "Do you really want to know what its like to suck dick."
    "She says yes. Give MC a choice. Whip it out and go for it, or offer to eat her out first. Best possible ending is non selfish route."
    menu:
        "Lick her first":
            "If you eat her out first, her opinion on getting head is min(orgasms, 2)"
            "You let her take the lead and practice sucking cock. Patient answers increase her opinoin on sucking cock, impatient decrease."
            "When you cum, she is putty and will take your cum wherever you say. If positive interactions so far, she likes or loves cum there now (face, swallow, body)"
            "+1 taking control"
        "Suck it now":
            "If you whip out your cock, you an still be patient or impatient with responses. Impatient decreases giving blowjobs opinion and vice versa."
            "When you cum, if interaction positive she lets you cum where you want, now likes cum there. (law of primacy)"
            "If interaction was negative, she tries to swallow your cum but struggles. Now doesn't like swallowing cum, but gains a bit of slut and obedience."
            "+1 being submissive"

    "Ellie now has oral positions unlocked."
    "Ellie may now approach MC once in a while when she is working on nanobot programs because working on sex related code is getting in her head and she needs some relief"
    return

label ellie_never_been_fucked_label():  #This is Ellie's 60 sluttiness event. Also requires X number of oral encounters?
    "You check up on Ellie while she is working on nanobot programming stuff."
    "She says working on this program is getting her really worked up. You can tell she's aroused (flushed cheeks, pointy nipples)."
    "She asks if you could fool around a little again. MC says he is tired of foreplay, says she probably just needs a good fucking."
    "She is embrassed. Says she knows that but she is just scared of having sex for the first time."
    "MC asks if she would be open to sleeping with him if he promises to go slow and be gentle."
    "Ellie is uncertain. Her mama would be so disappointed."
    "MC offers to take her out on a proper date first, have a couple drinks, go back to her place, she can stop any point she wants to."
    "She says okay. Make a plan for dinner on... some day? Figure out best day."
    "She's still needy right now though. Quick detour to the office for sixty nine."
    "She goes back to work."
    return

label ellie_loses_her_virginity_label():
    "You meet up with Ellie. Take her out for a nice dinner."
    "Have the option to mess around a little under the table. If you use your foot to rub against her privates, she gains +1 public sex opinion."
    "Also have a drink. At some point she uses ladies room and you can serum her."
    "Like a normal dinner date gain love based on how fancy wine is, how fancy dinner is, etc."
    "When finished, she asks MC back to her place, but says she is still scared."
    "Discover her place."
    "She's nervous, you makeout with her for a bit to get her warmed up."
    "Finally go back to her bedroom. She wants to strip for you."
    "Positive remarks give positive view on showing tits, showing ass, no clothes at all, and love gain."
    "Degrading remarks give negative opinion, but gain obedience and sluttiness."
    "If she likes getting head, asks for just a bit of oral. Arousal gain here that sets up MC to make her orgasm more later."
    "Lays down on bed. MC can be gentle for positive vaginal sex opinion, or rough for negative and obedience gain."
    "Mc can ask if she wants condom. She says she wants her first time natural, but appreciates it if MC asks and likes bareback sex. Otherwise dislikes bareback sex if MC doesn't ask."
    "After pentration, use creampie_cum but use red color to make it look like virginity taken."
    "Sex scene. If Ellie cums twice or more she begs MC to finish inside her. Gain creampie like."
    "If not, she asks MC to pull out. If MC pulls out she likes cum on her body. If he doesn't, she dislikes creampies."
    "Taking Ellie's virginity has made her putty in your hands now. She gains large love and obedience bonuses."
    "Ellie can't believe she did that, she always thought growing up she was saving herself for marriage, but can't believe what she has been missing out on."
    "With high love stat, MC has option to ask her to be his girlfriend. She accepts."
    "Leave her place and go home."
    "You have unlocked Ellie's vaginal sex options."
    return

label ellie_never_tried_anal_label():   #This is Ellie's 80 sluttiness rating. Must have anal nanobots unlocked.
    pass
    return

label ellie_turned_on_while_working_label():    #Crisis event. Can be triggered after unlocking Ellie's oral sex options, and procs when she is working on nanobot programming.
    "During a break, you make the rounds to the different departments. When you swing by R&D, you decide to check up on Ellie"
    "Ellie is masturbating, trying to type with one hand and playing with herself with the other."
    "She is sorry. Working on this stuff gets her so horny."
    "Initially, you can chastise her (dislikes mastubation), encourage her (likes masturbation), or offer to help her."
    "If you offer to help her, you can do it right there in R&D (likes public sex), or find somewhere private."
    "Her reactions change based on her story and corruption progress. At extreme sluttiness, when she sees you walk up she may jump MC or if submissive, pull down bottoms and bend over her desk and beg."
    "Sex scene."
    return
