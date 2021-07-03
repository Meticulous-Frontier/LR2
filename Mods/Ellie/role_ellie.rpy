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
        ellie_wardrobe = wardrobe_from_xml("ashley_Wardrobe")
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
        if fetish_serum_unlock_count() >= 2 and get_fetish_basic_serum().mastery_level > 3.0 and mc.business.head_researcher:
            if time_of_day == 2 and day%7 == 2 and mc.is_at_work():
                return True
        return False
    def ellie_meet_ellie_intro_requirement():
        return False
    def ellie_head_researcher_halfway_intro_requirement():
        return False
    def ellie_unnecessary_payment_requirement():
        return False
    def ellie_end_blackmail_requirement():
        return False
    def ellie_work_welcome_requirement():
        return False
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

label ellie_start_intro_note_label():
    $ the_person = mc.business.head_researcher
    "You get an email notification on your phone. Normally you would brish something like this off as spam, but the subject line has your name in it."
    "You open it up and are surprised what you are reading. It is short and to the point."
    "?????" "I know what your company is doing with the nanobots, and I'll go public with it if you don't meet my demands. Meet me tomorrow night in the alley between 3rd and 5th street, and come alone."
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
    the_person "Wow... fuck... okay."
    mc.name "So... "
    return

label ellie_meet_ellie_intro_label():
    "You meet ellie in the alley. You convince your head researcher to go along with you."
    "The head researcher stakes the place out while you meet with ellie. She snaps some pictures to try and get an idea of who you are dealing with."
    "Ellie wants money to keep quiet. She asks for a laughably small sum."
    "ellie is awkward, it is clear she has never blackmailed anyone before."
    "You leave the meeting more confused that you started. She was really young."
    "You get back with head researcher and she promises to look into who the girl is."
    return

label ellie_head_researcher_halfway_intro_label():
    "Head researcher calls you to the lab, says she's found out more about the mystery girl."
    "Found out through her contact that her name is Ellie, used to work at the nanobot facility."
    "Her contact framed Ellie for the missing nanobots, Ellie got fired, and due to a noncompete contract can't find work anywhere."
    "Says she was pretty fresh there, young, hired straight out of college, from somewhere else."
    "You come up with a plan with the head researcher to offer her a job. Officially in a different department."
    "But on the side will complete IT projects for you, including working on the nanobot programs."
    return

label ellie_unnecessary_payment_label():    #Use this scene each week if MC can't find out info on Ellie for some reason (head researcher fired, etc)
    "Meet with Ellie at the drop location."
    "You pay her the money she wants."
    "Over 5 weeks, you learn more about her, eventually find out she's just out of work after being fired."
    "She blames you for being fired. She's kinda right."
    "After 5 weeks you offer her a job."
    return

label ellie_end_blackmail_label():
    "You meet with ellie at the alley. You reveal you know who she is, her background."
    "She gets scared. She knows she shouldn't be doing this but didn't know what else to do. It was desperation."
    "You offer to hire her with terms."
    "She suspicious, but agrees. Agrees to show up early to work on monday and learn more."
    return

label ellie_work_welcome_label():
    "You meet with Ellie early the next monday. You show her around your company. She's still nervous, but thinks it is quaint."
    "You ask her if she has a department preference. TODO figure out a dept skill set for her."
    "You can either let her go to her choice (happy) or pick something different (obedient)."
    "You also give her the rundown on the nanobot program. She very intrigued on the direction the program is going."
    "You ask her if she would be willing to work on it for you. She says if you give her time to work on it she can see what she can do."
    "If you let her work on it, she will be in R&D instead of her dept, and doesn't contribute to overall company production."
    "However, you can use her to bypass Head researchers contact for developing new nanobot programs and she can also improve existing programs."
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
