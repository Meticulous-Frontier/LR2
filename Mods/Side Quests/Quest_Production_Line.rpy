#Super basic intro quest. Is available early, will help with early profitability if selected.
#Quest requires someone in production. STarts when girl approaches you, says father also works in pharmaceuticals. Sets you up to get coffee with him next day.
#next day if MC meets with father, says he is worried about daughter who is having money problems.
#Says if you give her a pay raise without telling her he told you to do it, he will share company secrets that will increase your chemical production.
#MC agrees. IF you give her a raise within 10 days, he meets with you again and agrees to help you. Meet for coffee again and gain an upgrade to serum production (+1)
#If you don't, he texts you and says he is disappointed. Says he is going to try and convince her to leave.
#Immediate happiness drop and penalties to happiness, such that girl probably quits

# flags
# 1: Quest has been initiated X
# 2: After 5 days, if MC hasn't talked to girl yet, she approaches MC on the next workday (We don't want these quests to drag out too long) TODO
# 11: talked to girl, agreed to meet with girls dad the next day. X
# 21: reminder has gone off on MC's phone (mandatory event) to remind MC to meet with dad. X
# 22: MC doesn't meet with girls dad. Quest is set to unset. X
# 29: Next day girl texts MC to say she is disappointed he didn't make time to meet with dad. Quest END
# 31: MC meets with dad, agrees to give girl a raise. X
# 32: MC fails to give girl a raise after 10 days. X
# 39: dad calls MC, states disappointment. QUEST END X
# 41: MC gives girl a raise.
# 42: Talk to the girl about her relationship with her dad
# 51: Dad meets with MC the next day. Gives plans X
# 61: Girl asks for MC's help moving into her new apartment. X
# 69: MC refuses to help girl move into new apartment.
# 91: MC helps girl move into new apartment. X
# 101: Girl meets with MC, says dad spoke highly of him. Love bonus(Low slutty ending)
# 102: Girl meets with MC, says dad spoke highly of him. Love  and obedience bonus and asks if she can call you daddy. (mid slutty ending)
# 103: Girl meets with MC, says dad spoke highly of him. Says she loves the bonus pay, large obedience boost and asks if she can call MC daddy and spank her. (High slutty ending)
# Any 100 ending adds personality tweak to girl that gives title change option of Daddy at high enough sluttiness, can call her "baby girl"
# girl also gains being submissive opinion (sub / dom type relationship)

init 1 python:
    def get_quest_production_line_person():
        able_person_list = []
        for person in mc.business.production_team:
            if person.age < 25:
                if person not in quest_director.unavailable_persons:
                    if day > person.event_triggers_dict.get("employed_since", 9999) + 7: #Employed for atleast 7 days#
                        able_person_list.append(person)
        return get_random_from_list(able_person_list)

    def setup_quest_production_line():
        person = get_quest_production_line_person()

        # make sure 'selected person' is single and has no kids
        # although the player might have seen other information
        # it is more disturbing when this information does not
        # match the story line
        person.kids = 0
        person.relationship = "Single"
        person.SO_name = None
        person.update_opinion_with_score("incest", 2, add_to_log = False) # this method updates or adds the opinion
        person.update_opinion_with_score("being submissive", 2, add_to_log = False) # this method updates or adds the opinion

        quest_production_line.quest_event_dict["target"] = person
        quest_production_line.quest_event_dict["father_name"] = get_random_male_name()
        quest_production_line.quest_event_dict["initial_meeting_day"] = 9999
        quest_production_line.quest_event_dict["starting_pay"]  = quest_production_line.quest_event_dict["target"].salary
        quest_production_line.quest_event_dict["moving_day"] = 9999
        quest_production_line.set_quest_flag(1)
        return

    def quest_production_line_tracker():  #I'm so sorry for anyone who tries to read this function
        the_person = quest_production_line.quest_event_dict.get("target", None)
        if quest_production_line.get_quest_flag() < 100:
            if the_person == None:          #quest target is fired or otherwise out of the game
                quest_production_line.quest_complete = True
                return
        if quest_production_line.get_quest_flag() <= 1: #Intro
            if quest_production_line_intro not in the_person.on_room_enter_event_list:
                the_person.on_room_enter_event_list.append(quest_production_line_intro)

        elif quest_production_line.get_quest_flag() == 11: #Agreed to meet
            mall.add_action(quest_production_line_coffee)
            if quest_production_line_coffee_reminder not in mc.business.mandatory_crises_list:
                mc.business.mandatory_crises_list.append(quest_production_line_coffee_reminder)

        elif quest_production_line.get_quest_flag() == 21: #reminder went off.
            if time_of_day > 3: #Missed the meeting.
                remove_mandatory_crisis_list_action("quest_production_line_coffee_reminder_label")
                mc.business.mandatory_crises_list.append(quest_production_line_coffee_miss)
                quest_production_line.set_quest_flag(22)
                mall.remove_action(quest_production_line_coffee)

        elif quest_production_line.get_quest_flag() == 29:  #Bad end
            quest_production_line.quest_complete = True

        elif quest_production_line.get_quest_flag() == 31: #agreed to give raise.
            mall.remove_action(quest_production_line_coffee)
            remove_mandatory_crisis_list_action("quest_production_line_coffee_reminder_label")
            if the_person.salary > quest_production_line.quest_event_dict.get("starting_pay", 0): #She has received a raise!
                quest_production_line.set_quest_flag(41)
                mc.business.mandatory_crises_list.append(quest_production_line_after_raise_consult)
            if quest_production_line_raise_miss not in mc.business.mandatory_crises_list:
                mc.business.mandatory_crises_list.append(quest_production_line_raise_miss)

        elif quest_production_line.get_quest_flag() == 39: #Bad End
            quest_production_line.quest_complete = True

        elif quest_production_line.get_quest_flag() == 41:
            remove_mandatory_crisis_list_action("quest_production_line_raise_miss_label")
            remove_mandatory_crisis_list_action("quest_production_line_after_raise_consult_label")
            if quest_production_line_after_raise_consult not in mc.business.mandatory_crises_list:
                mc.business.mandatory_crises_list.append(quest_production_line_after_raise_consult)

        elif quest_production_line.get_quest_flag() == 61:
            remove_mandatory_crisis_list_action("quest_production_line_after_raise_consult_label")
            if quest_production_line_help_move not in mc.business.mandatory_crises_list:
                mc.business.mandatory_crises_list.append(quest_production_line_help_move)

        elif quest_production_line.get_quest_flag() == 69:  #Moderate end. Really you won't help her move?
            quest_production_line.quest_complete = True

        elif quest_production_line.get_quest_flag() >= 100:  #Good ends
            quest_production_line.quest_complete = True
        return

    def quest_production_line_start_requirement():
        return day > 40 and not get_quest_production_line_person() is None

    def quest_production_line_cleanup():
        mall.remove_action(quest_production_line_coffee)
        remove_mandatory_crisis_list_action("quest_production_line_intro_label")
        remove_mandatory_crisis_list_action("quest_production_line_coffee_reminder_label")
        remove_mandatory_crisis_list_action("quest_production_line_coffee_label")
        remove_mandatory_crisis_list_action("quest_production_line_coffee_miss_label")
        remove_mandatory_crisis_list_action("quest_production_line_raise_miss_label")
        remove_mandatory_crisis_list_action("quest_production_line_after_raise_consult_label")
        remove_mandatory_crisis_list_action("quest_production_line_help_move_label")
        # cleanup dictionary (quest is done)
        quest_production_line.quest_event_dict.clear()
        return

    def quest_production_line_intro_requirement(the_person):
        if the_person.location() == the_person.work:
            return True

    def quest_production_line_coffee_reminder_requirement():
        if day == quest_production_line.quest_event_dict.get("initial_meeting_day", 0):
            if time_of_day == 1:
                return True
        return False

    def quest_production_line_coffee_requirement():
        if day == quest_production_line.quest_event_dict.get("initial_meeting_day", 0):
            if time_of_day == 2:
                return True
        return False

    def quest_production_line_coffee_miss_requirement():
        if day == quest_production_line.quest_event_dict.get("initial_meeting_day", 0) + 1:
            if time_of_day == 1:
                return True
        return False

    def quest_production_line_raise_miss_requirement():
        if day >= quest_production_line.quest_event_dict.get("initial_meeting_day", 0) + 10: #10 days to giver her a raise. Maybe change this?
            if time_of_day == 1:
                return True
        return False

    def quest_production_line_after_raise_consult_requirement():
        if time_of_day == 1:
            return True
        return False

    def quest_production_line_help_move_requirement():
        if day >= quest_production_line.quest_event_dict.get("moving_day", 0):
            if time_of_day == 3:
                return True
        return False

    def quest_production_line_daddy_title_requirement(the_person):
        if the_person.sluttiness > 40 and mc.is_at_work() and mc.business.is_open_for_business(): # only trigger at work
            return True
        return False

    def prod_line_target_unique_sex_positions(person, foreplay_positions, oral_positions, vaginal_positions, anal_positions,  prohibit_tags = []):
        willingness = spanking.build_position_willingness_string(person, ignore_taboo = True)
        foreplay_positions.insert(1, [willingness, spanking])
        return [foreplay_positions, oral_positions, vaginal_positions, anal_positions]

    quest_production_line_intro = Action("Begin Production Quest", quest_production_line_intro_requirement, "quest_production_line_intro_label")
    quest_production_line_coffee_reminder = Action("Meeting Remind", quest_production_line_coffee_reminder_requirement, "quest_production_line_coffee_reminder_label")
    quest_production_line_coffee = Action("Business Meeting", quest_production_line_coffee_requirement, "quest_production_line_coffee_label")
    quest_production_line_coffee_miss = Action("Missed Meeting", quest_production_line_coffee_miss_requirement, "quest_production_line_coffee_miss_label")
    quest_production_line_raise_miss = Action("No Raise Given", quest_production_line_raise_miss_requirement, "quest_production_line_raise_miss_label")
    quest_production_line_after_raise_consult = Action("Production Consultation", quest_production_line_after_raise_consult_requirement, "quest_production_line_after_raise_consult_label")
    quest_production_line_help_move = Action("Help Her Move", quest_production_line_help_move_requirement, "quest_production_line_help_move_label")
    quest_production_line_daddy_title =  Action("She Calls You Daddy", quest_production_line_daddy_title_requirement, "quest_production_line_daddy_title_label")

label quest_production_line_init_label():
    $ setup_quest_production_line()
    return

label quest_production_line_intro_label(the_person):
    $ dad_name = quest_production_line.quest_event_dict.get("father_name", "Gregory")
    "You walk into the production department. You take a moment to look around and see how things are going."
    "At her desk, you notice [the_person.title] struggling a bit with some of her serum."
    $ the_person.draw_person()
    mc.name "Hello there, [the_person.title]. Are you doing okay over here?"
    the_person.char "Hello [the_person.mc_title]. Yeah I guess, just struggling a bit with the small quantities of chemicals I am mixing up today."
    the_person.char "You know, I was talking to my daddy last night about the work I'm doing here. He is a chemist at a big petrol company, and I was explaining to him the work I am doing."
    mc.name "Oh yeah?"
    the_person.char "Yeah, he said he was surprised at a couple of our methods. He tried to explain some of it to me but to be honest I didn't really understand it."
    mc.name "Hmm, that sounds like it would be useful to have someone like that as a consultant."
    the_person.char "Yeah, his work keeps him pretty busy. Hey, you know what? Why don't I call him? Maybe he would be willing to meet with you for coffee or something?"
    mc.name "That would be good. Any increase in efficiency is huge in maintaining profitability."
    the_person.char "Ok! One second..."
    $ the_person.draw_person(position = "back_peek")
    "[the_person.possessive_title] turns away from you and calls her dad."
    the_person.char "Hey daddy! Yeah... yeah I know... Hey actually..."
    "She chats with her dad for a minute."
    the_person.char "Oh wow! So tomorrow in the afternoon you could meet with him? Yeah I'll let him know!"
    $ the_person.draw_person( position = "stand4")
    the_person.char "Okay, he said he actually has time tomorrow afternoon! He can meet with you and grab some coffee, maybe talk about some of the workflows and processes around here."
    mc.name "That sounds perfect."
    the_person.char "Yeah... He's really smart! I'm not sure if any of his ideas will be useful or not, but if anyone can help, I'm sure it would be him!"
    the_person.char "He said to share his contact info and to meet him over at the coffee shop. His name is [dad_name]."
    "You get his contact info and put it in your phone, as well as add a reminder in your phone to go meet him."
    mc.name "Thank you."
    the_person.char "No problem!"
    $ del dad_name
    $ quest_production_line.set_quest_flag(11)
    $ quest_production_line.quest_event_dict["initial_meeting_day"] = (day + 1)
    return

label quest_production_line_coffee_reminder_label():
    $ dad_name = quest_production_line.quest_event_dict.get("father_name", "Gregory")
    "An alarm on your phone is going off. You check it."
    "Meet [dad_name] at coffee shop at the mall."
    "If you are going to go meet with the chemist, do it after lunch. He should be at the mall."
    $ del dad_name
    $ quest_production_line.set_quest_flag(21)
    return

label quest_production_line_coffee_label():
    $ dad_name = quest_production_line.quest_event_dict.get("father_name", "Gregory")
    $ the_person = quest_production_line.quest_event_dict.get("target", None)
    "You text [the_person.title]'s father, [dad_name]. He tells you the name of the coffee shop. You quickly find it."
    #TODO location = shop
    #TODO get generic dad sprite to use? Placeholder? Theres no male images in the game...
    mc.name "Hello there, you must be [dad_name]."
    dad_name "Ah, nice to meet you."
    "You chat for a few minutes, exchanging some of the details of your work with each other."
    "[dad_name] is a very smart chemist, he clearly knows his stuff."
    mc.name "So, [the_person.name] said you might have some ideas for how I could increase the efficiency of my production."
    dad_name "She's right, I do. I'm willing to help you, however, I need you to do me a favor first."
    mc.name "Oh? What is that?"
    dad_name "This job that my baby girl is doing... its her first real job, you know? She's had a couple part time jobs, but nothing like this."
    dad_name "She is right on the verge of being able to afford her own place, with no roommates."
    dad_name "I'm not asking for much, even just a small raise in her salary would be enough to do it."
    mc.name "So... you are proposing an exchange? I give her a raise, and you give me an efficiency consultation?"
    dad_name "Exactly. I need you to keep it kinda quiet as well."
    mc.name "Oh?"
    dad_name "My baby girl... we have always been so close since her mother left us when she was young. She means the world to me."
    dad_name "But she's all grown up now. She refuses any financial assistance from me. She is determined to make it on her own."
    dad_name "So when you do it, make sure you make it seem like she accomplished it on her own."
    mc.name "I do occasional performance reviews. I could probably do it then, praising her for all her hard work."
    dad_name "I'll leave the details to you. And don't take too long. My baby girl is smart, if not at your company, I'm sure she'll get the wage she deserves somewhere else."
    mc.name "I understand."
    $ del dad_name
    "You get up and leave the coffee shop. So, if you want his help streamlining your production department, you should give [the_person.title] a raise."
    "Next time you see her, maybe you could just give her a performance review? High praise for her performance followed by raise."
    $ quest_production_line.set_quest_flag(31)
    return

label quest_production_line_coffee_miss_label():
    $ dad_name = quest_production_line.quest_event_dict.get("father_name", "Gregory")
    "You have a message on your phone. It is from [dad_name]."
    dad_name "You stood me up at the coffee shop? Tells me a lot about you, as a man."
    dad_name "I'll be telling my daughter to look for work elsewhere ASAP. Good luck with your business, asshole."
    "Yikes! Maybe you shouldn't have missed that meeting. Not much you can do about it now though."
    #TODO lower girl opinions, causing her to probably quit ASAP.
    $ del dad_name
    $ quest_production_line.set_quest_flag(29)
    return

label quest_production_line_raise_miss_label():
    $ dad_name = quest_production_line.quest_event_dict.get("father_name", "Gregory")
    "You have a message on your phone. It is from [dad_name]."
    dad_name "I asked my daughter last night if she had any good news about her job to share. She got suspicious and dragged out of me that I'd told you to give her a raise."
    dad_name "I told you to move quick. She missed a potential opportunity to rent a nice condo. The deal is off, good luck with your drug business, asshole."
    "Yikes! Maybe you should have moved a little quicker on that meeting [dad_name]'s daughter..."
    #TODO lower girl opinions, causing her to probably quit ASAP.
    $ del dad_name
    $ quest_production_line.set_quest_flag(39)
    return

label quest_production_line_after_raise_consult_label():
    $ dad_name = quest_production_line.quest_event_dict.get("father_name", "Gregory")
    $ the_person = quest_production_line.quest_event_dict.get("target", None)
    "Your phone is ringing. It is [dad_name], [the_person.title]'s father. You answer."
    mc.name "Hello?"
    dad_name "Hello there [mc.name]! This is [dad_name]. Guess what."
    mc.name "What's that?"
    dad_name "I just got off the phone with my baby girl. She is so excited, she is moving into her own apartment!"
    dad_name "I can only assume this is because of a raise she received recently."
    mc.name "That's right, I gave her a pay hike."
    dad_name "Alright. Glad to hear it."
    mc.name "So, would you like to come out to the lab for the consult?"
    dad_name "No need! [the_person.name] told me about your process for separating chemicals. The centrifuges you are currently using are ancient technology."
    dad_name "I pulled some strings at work, we have some that are a bit more state of the art. I'll have them delivered to your lab ASAP."
    dad_name "Using the new centrifuges should increase your serum output."
    mc.name "Ah, well thank you for the help. I'm still new to this, owning a business thing, and every little bit helps."
    dad_name "Of course. Take care."
    "You hang up the phone."
    "Your serum batch size has increased by 1!"
    $ batch_size_increase(increase_amount = 1)
    "A few minutes later, your phone is ringing again. Now it is [the_person.title]"
    mc.name "Hello?"
    the_person.char "Hey! Have a sec?"
    mc.name "Of course."
    the_person.char "I was just wondering... what are you doing tomorrow evening?"
    mc.name "Nothing as of now. Have something in mind?"
    the_person.char "Well... as a matter of fact I do! I umm, could use some help, especially from a strong man such as you."
    mc.name "I'm listening."
    the_person.char "I'm... moving! Into my own apartment! I have a ton of heavy stuff and I really need help! Daddy is too busy with work to help me..."
    menu:
        "Help her":
            mc.name "That's okay, your other daddy can come give you a hand."
            the_person.char "Ohh... my... other daddy? Will you come help me... daddy?"
            mc.name "Anything for you baby girl."
            $ the_person.change_arousal(10)
            the_person.char "Ohhh... wow... okay! Sounds good. I'll be expecting you tomorrow night then!"
            $ quest_production_line.quest_event_dict["moving_day"] = (day + 1)
            "You hang up the phone."
            "So... you're gonna be with [the_person.title] tomorrow, in her apartment."
            "You might want to prep a serum or two... never know if an opportunity might pop up to have some fun!"
            $ quest_production_line.set_quest_flag(61)
            $ quest_production_line.quest_event_dict["moving_day"] = (day + 1)
        "Too busy":
            mc.name "I'm sorry, I won't be able to help then."
            the_person.char "Damn... okay, I'm sure I'll be able to find someone."
            "You hang up the phone."
            "You already gave her a raise. Besides, you really don't even know her that well. Why would you want to spend all evening help her move?"
            $ quest_production_line.set_quest_flag(69)
    $ del dad_name
    return

label quest_production_line_help_move_label():
    $ the_person = quest_production_line.quest_event_dict.get("target", None)
    "You promised to help [the_person.title] move now. She texts you the address so you head out."
    $ mc.change_location(the_person.home) #TODO instead of showing this, have it show the elevator background? So when we are at her new place later it actually looks different.
    $ mc.location.show_background()
    $ the_person.draw_person()
    "When you show up, she greets you at the door."
    the_person.char "Oh my god, thank you so much for coming!"
    mc.name "It's my pleasure baby girl."
    $ the_person.change_arousal(10)
    the_person.char "That's... I'm glad to hear that... d... d..."
    if the_person.sluttiness < 20:
        the_person.char "Sorry, I just, its so weird for someone else to call me that. Could you just stick with [the_person.title]?"
        mc.name "Certainly, if that is what you prefer."
    else:
        mc.name "Its okay, you can say it."
        "When she realizes that you are okay with it, she finally says it."
        the_person.char "Daddy, I'm so glad you are here!"
        $ the_person.draw_person(position = "kissing")
        "She wraps her hands around you and gives you a lingering hug."
        "Eventually, she lets go."
    the_person.char "Okay... let's get to work!"
    $ renpy.scene("Active")
    "You spend about an hour helping [the_person.title] loading her things into a small rental trailer."
    "When you are done, you ride with her over to her new apartment."
    #TODO her apartment which is actually different than the place she was earlier.
    $ the_person.draw_person()
    $ the_person.learn_home()
    "Before we get to work, would you do me a favor? Could you grab a couple bottles of water from the fridge? I'm so thirsty!"
    $ renpy.scene("Active")
    "You grab a couple of water bottles. [the_person.title] is still out in the trailer. Now would be a good time to drop a serum in her drink..."
    menu:
        "Add a dose of serum to [the_person.title]'s drink.":
            call give_serum(the_person) from _call_give_prod_line_girl_serum_01
        "Leave her drink alone.":
            pass
    "You take the water bottle out to [the_person.title]."
    $ the_person.draw_person(emotion = "happy")
    the_person.char "Mmm, thanks!"
    "She chugs the whole thing down."
    "You get back to work. At her direction you are stacking up boxes in appropriate areas of her one bedroom apartment."
    if the_person.sluttiness < 20:
        the_person.char "That one goes in the bedroom."
        mc.name "Sure thing."
    else:
        the_person.char "That one goes in my bedroom daddy."
        mc.name "Sure thing baby girl."
        $ the_person.change_arousal(10)
        "You can definitely feel some sexual tension building with the way she is talking to you."
    "A couple hours later, the trailer is empty. Basic furniture is set up around [the_person.title]'s apartment, and there are large stacks of boxes in each room."
    the_person.char "Oh my god, I can't believe it. We did it!"
    mc.name "Thankfully you don't have too much stuff."
    the_person.char "Yeah... this is it! My first place... all to myself!"
    $ the_person.draw_person(position = "sitting")
    "[the_person.title] sits on the edge of her bed. One of the few places in her apartment to sit, for now."
    if the_person.sluttiness < 20:
        the_person.char "This has been a ton of work, but you have no idea how much I appreciate this."
        mc.name "Of course. Always glad to help out."
        $ the_person.change_stats(happiness = 10, love = 20, obedience = 20)
        the_person.char "I really owe you one. I think I can take over from here though."
        mc.name "You sure? I'd be glad to help you unpack some stuff."
        "She shakes her head."
        the_person.char "Your enthusiasm is appreciated, but unnecessary."
        $ the_person.draw_person()
        "You stand up and get yourself together."
        "She walks you to her door."
        the_person.char "Thank you again, for everything!"
        mc.name "You're welcome [the_person.title]. I'll see you at work?"
        the_person.char "Yes Sir!"
        $ quest_production_line.set_quest_flag(101)
        $ the_person.on_room_enter_event_list.append(quest_production_line_daddy_title)
    else:
        the_person.char "So... I was wondering something."
        mc.name "What might that be?"
        the_person.char "Is... is it okay if I call you... daddy? From now on?"
        mc.name "I don't see why not. I've been called worse!"
        the_person.char "Yeah! You remind me a lot of him, you know? And being away from him now... It's nice having you around."
        mc.name "As long as you don't mind if I reciprocate, Baby Girl."
        $ the_person.change_arousal(10)
        $ the_person.set_mc_title("Daddy")
        $ the_person.set_title("Baby Girl")
        $ the_person.set_possessive_title("Your Baby Girl")
        "You notice she catches her breath when you say that. It is almost like she is getting excited."
        mc.name "You and your father... you umm, have a very special relationship... don't you?"
        if the_person.sluttiness > 40:  #She reveals her incest
            the_person.char "That's... I mean... kind of private!"
            mc.name "It's ok, [the_person.title]. You can tell me."
            "You can see her defenses breaking down."
            the_person.char "Oh god [the_person.mc_title], its like you see right through me..."
            the_person.char "Its not what you think! Mom left us when I was really young. When I was growing, my dad threw himself into his work, and all his spare time he spent raising me."
            the_person.char "He didn't have any time to himself. He didn't have time to date or meet anyone. He spent all his time with me. I love him so much."
            the_person.char "And then it happened. I was older, and I was over at a friend's house. I'd told him I was going to spend the night there, but I decided to come home instead."
            the_person.char "When I got home... he didn't hear me come in the door. He was in the living room on the computer, watching pornography. I know I should have looked away... but I just couldn't!"
            the_person.char "When he realized I was home and watching... he tried to tell me to go to my room, but I just couldn't! It's not his fault mom ditched us! Every man has needs..."
            the_person.char "I just wanted to take care of him... so... I did! And I don't regret it one bit!"
            mc.name "Just the one time?"
            the_person.char "No... it's... we've been intimate... on multiple occasions."
            the_person.char "But now, I'm moved out. He has already started spending more time being social. Even been on a couple of dates!"
            the_person.char "I'm so proud to have him as my dad. But I always knew it wouldn't last forever. We both did."
            the_person.char "So we decided, together, to stop. Doing sexual things together anyway."
            "You take a moment to consider this revelation."
            mc.name "That's okay. I totally understand."
            the_person.char "You do?"
            mc.name "There are multiple ways of telling someone you love them. Some are more intimate than others. If it feels right, and both people consent, what's the harm?"
            the_person.char "Yeah! Exactly! Not many people think the way that we do though."
            $ the_person.change_stats(happiness = 20, love = 40, obedience = 40)
            $ the_person.draw_person()
            "She stands up."
            the_person.char "That feels good... to get off my chest. You know? But still... I had sex with my dad! Multiple times! And liked it!"
            mc.name "So?"
            the_person.char "Well... you're kind of my daddy now. Isn't that naughty?"
            mc.name "I suppose..."
            $ the_person.draw_person(position = "kissing")
            "She wraps her arms around you. She whispers in your ear."
            the_person.char "Do you think you could... spank me? For a bit? Please [the_person.mc_title]?"
            mc.name "Oh [the_person.title]... you HAVE been bad..."
            "Your hand drops to her ass. You give it a squeeze."
            $ the_person.event_triggers_dict["unique_sex_positions"] = prod_line_target_unique_sex_positions
            $ the_person.personality = get_daddy_girl_personality(the_person)
            call fuck_person(the_person, start_position = spanking) from _spank_production_assistant_01
            $ the_person.increase_opinion_score("being submissive")
            the_person.char "Oh god... that was wonderful [the_person.mc_title]."
            $ the_person.draw_person()
            "You stand up and get yourself together."
            "She walks you to her door."
            the_person.char "Thank you again, for everything!"
            mc.name "You're welcome [the_person.title]. I'll see you at work?"
            the_person.char "Yes Sir!"
            "As you turn from her door, you process all the events of the last few days."
            "One of your employees, recently had an amicable breakup... with her dad? And now she calls you Daddy... And she likes to get spanked."
            "While it is unlikely this relationship is going to last, you decide to make sure you have as much fun with it as you can while it lasts."
            $ quest_production_line.set_quest_flag(103)
        else:
            the_person.char "I'm sorry, that's kind of... private!"
            mc.name "That's okay. I understand."
            the_person.char "Thank... Sometime, maybe we can talk about it... but not right now!"
            $ the_person.change_stats(happiness = 10, love = 30, obedience = 40)
            $ the_person.draw_person()
            "You stand up and get yourself together."
            "She walks you to her door."
            the_person.char "Thank you again, for everything!"
            mc.name "You're welcome [the_person.title]. I'll see you at work?"
            the_person.char "Yes Sir!"
            $ quest_production_line.set_quest_flag(102)
            $ the_person.on_room_enter_event_list.append(quest_production_line_daddy_title)
    return

label quest_production_line_daddy_title_label(the_person): #This label is activated if the MC does not gain "daddy" status in the quest but still finished with a good end.
    $ the_person.draw_person()
    the_person.char "Hey there [the_person.mc_title]... It's good to see you."
    the_person.char "Do you have a minute?"
    mc.name "Of course."
    the_person.char "So... I was wondering something."
    mc.name "What might that be?"
    the_person.char "Since I've moved into my own place, it has been great, but, I haven't seen my daddy in weeks now. I miss him a lot."
    the_person.char "Is... is it okay if I call you... daddy? From now on?"
    mc.name "I don't see why not. I've been called worse!"
    the_person.char "Yeah! You remind me a lot of him, you know? And being away from him now... It's nice having you around."
    mc.name "As long as you don't mind if I reciprocate, Baby Girl."
    $ the_person.change_arousal(10)
    $ the_person.set_mc_title("Daddy")
    $ the_person.set_title("Baby Girl")
    $ the_person.set_possessive_title("Your Baby Girl")
    "You notice she catches her breath when you say that. It is almost like she is getting excited."
    $ the_person.draw_person(position = "kissing")
    "She wraps her arms around you. She whispers in your ear."
    the_person.char "Do you think you could... spank me? For a bit? Please [the_person.mc_title]?"
    mc.name "Oh [the_person.title]... you HAVE been bad..."
    "Your hand drops to her ass. You give it a squeeze."
    $ the_person.event_triggers_dict["unique_sex_positions"] = prod_line_target_unique_sex_positions
    $ the_person.personality = get_daddy_girl_personality(the_person)
    call fuck_person(the_person, start_position = spanking) from _spank_production_assistant_02
    $ the_person.increase_opinion_score("being submissive")
    the_person.char "Oh god... that was wonderful [the_person.mc_title]."
    $ the_person.draw_person()
    return

#Daddy's girl personality overrides
init 1301 python:
    def daddy_girl_titles(the_person):
        return "Baby Girl"
    def daddy_girl_possessive_titles(the_person):
        return "Your Baby Girl"
    def daddy_girl_player_titles(the_person):
        return "Daddy"
    def get_daddy_girl_personality(the_person): #Use a function to get this so we can keep the girls prefix so her personality doesn't change TOO much
        daddy_girl = Personality("princess", default_prefix = the_person.personality.personality_type_prefix,
        common_likes = [],
        common_sexy_likes = [],
        common_dislikes = [],
        common_sexy_dislikes = [],
        titles_function = daddy_girl_titles, possessive_titles_function = daddy_girl_possessive_titles, player_titles_function = daddy_girl_player_titles)
        return daddy_girl

label princess_greetings(the_person):
    $ update_ass_condition(the_person)
    if the_person.sluttiness > 40:
        if the_person.event_triggers_dict.get("spank_level", 0) < 2: #Flawless
            the_person.char "Hi [the_person.mc_title]! I've been so good lately!"
            "She lowers her voice a little."
            the_person.char "But maybe a little too good... Are you sure I don't need a spanking?"
        elif the_person.event_triggers_dict.get("spank_level", 0) < 6: #Flawless
            the_person.char "Hi [the_person.mc_title]! I'm trying to be good!'"
            "She lowers her voice a little."
            the_person.char "I'm still a little sore, but if you need to spank me, I understand!"
        else:
            the_person.char "Hi [the_person.mc_title]! I'm being good I promise!"
            the_person.char "I'm still sore, I swear I don't need a spanking!"
        mc.name "Hello [the_person.title]. I'll be the judge of when you need spanking."
    elif the_person.love < 0:
        the_person.char "Ugh, what do you want?"
    elif the_person.happiness < 90:
        the_person.char "Hey..."
    else:
        if the_person.sluttiness > 60:
            if the_person.obedience > 130:
                the_person.char "Hello [the_person.mc_title], it's good to see you."
            else:
                the_person.char "Hey there handsome, feeling good?"
        else:
            if the_person.obedience > 130:
                the_person.char "Hello [the_person.mc_title]."
            else:
                the_person.char "Hey there!"
    return

label princess_clothing_accept(the_person):
    if the_person.obedience > 130:
        the_person.char "You want me to wear this [the_person.mc_title]? Anything for you!"
    else:
        the_person.char "Oh [the_person.mc_title]! Are you sure I can wear this out of the house?"
    return

label princess_clothing_reject(the_person):
    the_person.char "I want to wear this for you [the_person.mc_title], but I'm not sure I can!"
    return

label princess_sex_accept(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Oh [the_person.mc_title]! I'll do ANYTHING for you."
    else:
        the_person.char "Okay [the_person.mc_title], we can give that a try."
    return

label princess_sex_obedience_accept(the_person):
    the_person.char "I'll do it, but only because it's for you [the_person.mc_title]."

    return

label princess_cum_face(the_person):
    the_person.char "Oh [the_person.mc_title], I look cute covered in your cum?"
    if the_person.sluttiness > 60:
        "[the_person.title] licks her lips, cleaning up a few drops of your semen that had run down her face."
    else:
        "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
    return

label princess_cum_vagina(the_person):
    if mc.condom:
        if the_person.sluttiness > 75 or the_person.get_opinion_score("creampies") > 0:
            the_person.char "God [the_person.mc_title], your cum feels so warm! If I'm good will you promise not to use a condom next time?"
        else:
            the_person.char "[the_person.mc_title]... I can feel how warm your cum is through the condom. It feels nice."

    else: #TODO this probably hchanges with pregnancy stuff. change it later.
        the_person.char "Your cum is so nice and warm [the_person.mc_title]!"
        the_person.char "You can fill me up anytime you want."
    return

label princess_suprised_exclaim(the_person):
    $rando = renpy.random.choice(["Daddy!","Shit!","Oh fuck!","Fuck me!","Ah! Oh fuck!", "Ah!", "Fucking tits!", "Holy shit Daddy!", "Fucking shit!"])
    the_person.char "[rando]"
    return
