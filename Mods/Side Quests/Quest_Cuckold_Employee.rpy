#Mid game quest. Is available mid game, will allow you to knock an employee up early..
#Requires a married woman with no children atleast sluttiness... 40? 60?
#Employee approaches MC, asking if company has had any luck with fertility serum for males.
#If fertility serum for males exist, she asks if anything else has been researched.
#After no, she gets sad, goes away. 2 days later she approaches MC and says she is distraught because her husband is infertile, doesn't know what to do.
#BRANCH 1
#MC volunteers to seed her. With a charisma check, she agrees immediately. If MC fails charisma check, she initially refuses.
#If she refused, a couple days later, she reapproaches MC and says she reconsiders.
#TODO figure out if we can tweak her fertile period so she is most fertile during quest.
#Have sex with girl as many times as possible. Good end if you knock her up. (After X creampies, force pregnancy?)
#BRANCH 2
#MC doesn't volunteer to help. She gets the idea and begs MC to fuck her.
#A few days later, if gloryhole has been unlocked, she hides inside and waits for MC during mandatory event.
#If MC sticks his dick in, she fucks him to completion with creampie. IF POSSIBLE force pregnancy Good end if she's pregnant.

#Once complete, can refer to girl as porn star, slight personality tweek.

# flags
# 1: Quest has been initiated
# 11: MC has been approached once.
# 21: MC meets again with woman, has volunteered to seed her but has been told no.
# 22: MC meets again with woman, has volunteered and has been accepted.
# 25: MC meets again with woman, has not volunteered to seed her or said no, but has gloryhole unlocked.
# 28: MC agreed to breed woman, she agrees, but doesn't creampie her. She gets pissed and claims MC just wanted to have sex. (BAD END)
# 29: MC said no to seeding and no gloryhole. (BAD END)
# 31: Set flag to 31 during "breeding season". Pie her as much as possible. Make sure to set vaginal creampie, bareback sex to loved opinions
# 35: Gloryhole scene occured and woman has been pied.
# 39: Gloryhole scene, MC did not pie her. (BAD END)
# 49: After "breeding season", woman is not pregnant. (BAD END)
# 101: Woman is pregnant from MC volunteering (GOOD END)
# 102: Woman is pregnant from glory hole (GOOD END)
# 101: Girl moves to marketing. Gain marketability based on sex video rating. (Good end)
# Any 100 ending adds marketability. Also 40+ can refer to girl as porn star, personality tweak.


label quest_cuckold_employee_init_label(): #Use this function to set quest specific variables.
    $ quest_cuckold_employee.quest_event_dict["target"] = quest_cuckold_employee_person_find_employee()
    $ quest_cuckold_employee.quest_event_dict["start_day"] = 9999
    $ quest_cuckold_employee.quest_event_dict["creampie_count"] = 0
    return

### The next three functions define the quest progress tracker, init requirements, and how we clean up after quest is done.
init 1 python:
    def quest_cuckold_employee_tracker():
        pass
        return

    def quest_cuckold_employee_start_requirement():
        if quest_cuckold_employee_person_find_employee():
            return True
        return False

    def quest_cuckold_employee_cleanup():
        pass
        return

###Declare any requirement functions
    def quest_cuckold_employee_intro_requirement(the_person):
        if mc.business.is_open_for_business():
            if mc.is_at_work():
                return True
        return False

    def quest_cuckold_employee_intro_requirement(the_person):
        if mc.business.is_open_for_business():
            if mc.is_at_work():
                if quest_cuckold_employee.quest_event_dict.get("start_day", 0) + 2 > day: #Atleast two days after first convo
                #TODO random element so it isn't necessarily in the morning?
                    return True
        return False

###Functions unique to the quest
    def quest_cuckold_employee_person_find_employee():
        able_person_list = []
        for person in mc.business.get_employee_list(): #TODO is there a method that grabs ENTIRE employee list?
            if person not in quest_director.unavailable_persons:
                if person.core_sluttiness > 50:
                    if person.relationship == "Married":
                        if person.kids == 0:
                            #TODO isn't already pregnant
                            able_person_list.append(person)
        if len(able_person_list) > 0:
            return get_random_from_list(able_person_list)
        else:
            return False

###Declare quest actions###



#Quest Labels. This is the story you want to tell!
label quest_cuckold_employee_intro_label():
    $ the_person = quest_cuckold_employee.quest_event_dict.get("target", None)
    if the_person == None:
        #ABORT ABORT, we fucked up somewhere.
        return
    "You working diligently when a figure appears in your peripheral vision. You look up and see [the_person.title] standing in front of you."
    $ the_person.draw_person(emotion = "sad")
    mc.name "Hello [the_person.title]. Can I help you?"
    the_person.char "Hopefully! I was just wondering... we've worked on a lot of drugs around here... have we ever made any progress on drugs that can increase... fertility?"
    mc.name "As a matter of fact..."
    the_person.char "Male fertility, to be exact."
    mc.name "Oh! Well... to be honest, no, we haven't."
    $ the_person.change_stats(happiness = -10)
    the_person.char "Ah Damn. Thanks, I should have expected that."
    mc.name "... Everything okay?"
    the_person.char "Yeah! Yeah definitely. Everything is A-OKAY with me and [the_person.SO_name]!"
    mc.name "Oh? I didn't ask about him..."
    the_person.char "Right..."
    "There's a long, awkward silence."
    the_person.char "Welp! I'll be getting back to work now!"
    mc.name "Take care."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] begins to walk away. Well that was an awkward moment..."
    $ quest_cuckold_employee.quest_event_dict["start_day"] = day
    return

label quest_cuckold_employee_decision_label():
    $ the_person = quest_cuckold_employee.quest_event_dict.get("target", None)
    if the_person == None:
        #ABORT ABORT, we fucked up somewhere.
        return
    "You are lost in your work when a feminine voice clearing her throat nearby catches your attention. You look up and see [the_person.title] standing in front of you again."
    mc.name "Hello [the_perosn.title]. Can I help you?"
    the_person.char "Well, kind of yes, kind of no."
    mc.name "I'm sorry?"
    the_person.char "I just... I need to vent to someone about something, but I don't trust the other girls around her not to gossip about it."
    mc.name "Of course, you can talk to me about anything."
    the_person.char "Well... my husband and I... we've been trying to have baby lately, but after months of trying, still nothing."
    the_person.char "I did something I probably shouldn't have... I took a semen sample when we had sex a few days ago secretly and had it analyzed."
    the_person.char "He is basically infertile. I'm absolutely crushed! I love him so much, but I also want to have a baby so bad."
    mc.name "I understand. It might take a while for you to grieve this if you need some time off."
    the_person.char "No, no, that's not it. I keep thinking, maybe there is some way, you know? Maybe a miracle will happen, or some drug or something will be invented that can help."
    the_person.char "I can't leave him, but my body is screaming at me. The urge to make a baby is SO strong!"
    mc.name "Have you considered something like a sperm bank?"
    the_person.char "No... I'd have to tell him. That he is infertile. It would crush him! I'm not sure our relationship would survive that."
    "Hmmm... well... there is always another way of getting pregnant... You wonder if she has considered it at all."
    "You could always offer to knock her up. But then again, impregnating another man's wife could lead  you to some heavy drama down the road..."
    menu:
        "Offer to help":
            mc.name "You know, [the_person.title]... there may be a solution that would allow you to have a baby AND stay with your husband."
            $ the_person.draw_person(emotion = "happy")
            the_person.char "Oh? What would that be?"
            mc.name "Well, if you want a baby that bad, you could always have someone else do the deed..."
            the_person.char "Oh... OH... Oh my..."
            "She stumbles for words for a moment."
            the_person.char "That's... wow... I don't know, that is an awfully big step."
            the_person.char "I don't even know anyone. How could I even find a man that would that?"
            if mc.charisma > 4: #Charisma check
                mc.name "I know how much this means to you. I know I'm your boss, but I'm also your friend, and I want to see you happy."
                mc.name "I would be glad to help you out if you decided that was a step you would like to take."
                the_person.char "Oh my! That's crazy. I never would have thought to do something like that. I don't know, that sounds pretty nuts..."
                mc.name "The urges your body are giving you are completely natural. They are only going to get stronger over time, until they drive a wedge between you and your husband."
                the_person.char "Oh god... you're right. I know you are. I don't want to admit it, but deep down inside, I know you are right."
                "She bites her lip for a moment and looks down at the floor."
                the_person.char "I know this is kind of a crazy coincidence... but... I'm actually really fertile. Like right now."
                mc.name "Oh?"
                the_person.char "I've been tracking my cycles... I'm going to ovulate in the next few days almost for certain."
                the_person.char "Do you think... we could go to your office?"
                "She leaves the question in the air for a moment..."
                the_person.char "Oh my god! what am I thinking! This is crazy, I can't be..."
                mc.name "Hush. Let's go, we can definitely find some privacy in my officer."
                the_person.char "Oh! Oh fuck, I can't believe it. Okay. Let's go."
            else:
                mc.name "It would be really no problem. I'd be glad to help you out with that..."
                the_person.char "Umm, you? Oh geeze. I'm sorry, you're my boss! That wouldn't be right!"
                "She changes her voice to imitate a masculinity."
                the_person.char "Oh honey! The baby is so cute... but he looks just like your boss???"
                "She shakes her head."
                the_person.char "I appreciate the thought, you've definitely given me something to think about, but I'm not sure that is a good idea."
                mc.name "Okay, well if you change your mind, let me know."
                the_person.char "Yeah... right... fucking my boss... bareback... totally not a good idea..."
                $ the_person.draw_person(position = "walking_away")
                "As [the_person.title] turns and walks away, you can almost see the wheels turning in her head."
                "Her initial reaction was not great, but you wonder if she will think about it more. Maybe you should try talking to her again in a few days?"
                return
        "Stay quiet":
            "There is a long moment of silence."
            mc.name "I'm really sorry, I wish I could do something to help."
            the_person.char "It's okay. I mean, I just needed to vent, I wasn't expecting a solution to be... starting at me in the face."
            "She's looking straight into your eyes now. You start to feel a bit uncomfortable."
            the_person.char "You know... you remind me a lot of my husband. Height... hair color..."
            the_person.char "What if there was something you could do to help? Would you do it?"
            mc.name "I guess that would depend on what that action would be."
            "She clears her throat."
            the_person.char "I mean, I could always get pregnant the regular way, just with someone else..."
            "IS this really going where you think it is going?"
            the_person.char "That person would have to be careful, of course, to keep it a secret... a dirty little secret."
            mc.name "That is certainly a possible solution."
            the_person.char "So umm... what would you say if I asked you? To get me pregnant I mean."
            "You weight the decision carefully."
            menu:
                "Help her":
                    mc.name "Let me see if I have this right. You are asking me, if I would be willing to fuck you, bareback, and fill you with my seed?"
                    $ the_person.change_arousal(10)
                    the_person.char "I mean, that's really hot sounding but completely hypothetical of course..."
                    mc.name "Fuck yeah. I would do that in a heartbeat."
                    the_person.char "Of course if you don't I comple... Wha? You would!?!"
                    $ the_person.change_happiness(15)
                    the_person.char "That's amazing! I can't believe it."
                    "She bites her lip for a moment and looks down at the floor."
                    the_person.char "I know this is kind of a crazy coincidence... but... I'm actually really fertile. Like right now."
                    mc.name "Oh?"
                    the_person.char "I've been tracking my cycles... I'm going to ovulate in the next few days almost for certain."
                    the_person.char "Do you think... we could go to your office?"
                    mc.name "Let's go, we can definitely find some privacy in my officer."
                    the_person.char "Oh! Oh fuck, I can't believe it. Okay. Let's go."
                "Can't help":
                    mc.name "I understand what you are going through, but I just don't think I can do that. Not without having your husband on board with it."
                    "She groans."
                    the_person.char "Nooo, he would never agree to it! I need someone to keep it secret..."
                    mc.name "I'm sorry, I feel like that is a line I'm not willing to cross."
                    the_person.char "Thats... ARG! Okay okay okay. I get it!"
                    "She takes a deep breath."
                    the_person.char "I'm sorry. I shouldn't have asked, that was really inappropriate."
                    $ the_person.change_obedience(15)
                    mc.name "It's alright."
                    $ the_person.draw_person(position = "walking_away")
                    "[the_person.possessive_title] turns and walks away. You wonder if you have heard the last of this?"
                    return
    # only get here if we are gonna breed in the office.
    "[the_person.possessive_title] follows you to your office."
    $ mc.change_location(office)
    $ mc.location.show_background()
    "After you walk in, you close the door and lock it."
    the_person.char "Let's do this. I'm ready "
    $ the_person.draw_person(position = "kissing")
    "You wrap your arms around [the_person.title]. She embraces you, and you start to kiss. You hands go down to her ass."
    $ the_person.change_arousal(5)
    the_person.char "Okay, so... the best way to do this that I've read anyway, is good old fashioned missionary."
    mc.name "Get naked and lay down on my desk."
    the_person.char "Oh my god, I can't believe I'm doing this."
    $ the_person.strip_outfit()
    the_person.char "Alright [the_person.mc_title]. This is it. Time to make a baby!"
    call fuck_person(the_person, starting_position = breeding_missionary, private= True, start_object = desk, position_locked = True, affair_ask_after = False, asked_for_condom = True) from _breed_cuckold_attempt_1
    if the_person.has_creampie_cum():
        the_person.char "Oh god, I can feel it inside me! We really did it."
        $ the_person.change_stats(happiness = 10, obedience = 10, love = 5)
        mc.name "Do you think that did it?"
        the_person.char "I hope so!... but you never know."
        "She gives a deep sigh."
        the_person.char "My fertility window. It starts today, but realistically I'm at my most fertile over the next 5 days."
        "She looks up at you."
        the_person.char "If you are okay with it, we should probably try again."
        mc.name "How often is best?"
        the_person.char "I mean, as often as possible during the window. It would give it the best possible chance of success."
        "[the_person.possessive_title] wants you balls deep and cumming inside her as much as possible over the next 5 days. You get goosebumps for a second just thinking about it."
        mc.name "I'll do my best. Whenever I have time, I'll come find you."
        the_person.char "Okay! I umm... I'm going to lay here for a while longer if thats okay with you."
        mc.name "Certainly. I'll lock the door behind me so you aren't disturbed."
        the_person.char "Thank you [the_person.mc_title]. I can't believe this is really happening!"
        mc.name "Me neither."
        "With that, you leave your office, being careful to lock the door behind you."
        "Your sperm might already be racing to her egg, ready to fertalize it. But it also might not be. To be certain, you should breed her as often as you can over the next few days."
    else:
        "[the_person.title] is completely silent."
        the_person.char "You... you didn't even finish inside of me?"
        $ the_person.change_stats(happiness = -20, obedience = -30, love = -30)
        the_person.char "You... you just wanted to fuck me, didn't you!?!"
        mc.name "I'm sorry, I want to help you, but it's been a long day and I'm just wore out..."
        the_person.char "Fuck you! I see right through that charade. You just wanted to fuck a married woman!"
        $ the_person.draw_person(position = "walking_away")
        "[the_person.title] stands up and storms out of your office. Unfortunately, you may have damaged your relationship with her irreperably."

    return

label quest_cuckold_employee_rethink_decision_label():
    $ the_person = quest_cuckold_employee.quest_event_dict.get("target", None)

label quest_cuckold_employee_breeding_session_label(the_person):
    "You walk up to [the_person.title]. When she sees you she smiles."
    $ the_person.draw_person(emotion = "happy")
    the_person.char "Hey [the_person.mc_title]! Do you need something? I can help you out with that thing in your office again... You know what I mean, right?"
    "She is still in her fertile window. Do you want to take her to your office and try and breed her again?"
    menu:
        "Breeding session{image=gui/heart/Time_Advance.png}":
            pass
        "Not now":
            mc.name "Actually, I need to talk to you about something else."
            the_person.char "Oh! What can I do for you?"
            return
    mc.name "Yes that is exactly right. I really need help with something in my office, could you please come give me a hand?"
    the_person.char "Of course! Let's go!"
    "[the_person.possessive_title] follows you to your office."
    $ mc.change_location(office)
    $ mc.location.show_background()
    "After you walk in, you close the door and lock it."
    the_person.char "I've been looking forward to this. I know that we're doing this for practical reasons, but that doesn't mean it doesn't feel really good..."
    "You and [the_person.title] get naked."
    $ the_person.strip_outfit()
    mc.name "I'm gonna fuck you on my desk again."
    the_person.char "Yes sir!"
    call fuck_person(the_person, starting_position = breeding_missionary, private= True, start_object = desk, position_locked = True, affair_ask_after = False, asked_for_condom = True) from _breed_cuckold_attempt_2
    if the_person.has_creampie_cum():
        the_person.char "Oh god, every risky load feels even better than the last..."
        $ the_person.change_stats(love = 10, happiness = 10, obedience = 10)
        "You gently rub her stomach."
        mc.name "Your hungry cunt feels like its sucking the cum out of me. It's amazing, honestly."
        mc.name "A little part of me is hoping it doesn't take right away and we have to keep trying for a while."
        the_person.char "Mmm, I'd be lying if I said I didn't feel the same way."
        if the_person.love > 60:
            the_person.char "Even if I do get pregnant... I'll already have one dirty little secret anyway. Maybe we could still fool around some..."
            "Sounds like she might be open to some kind of an affair in the future..."
        else:
            the_person.char "But, its like they say, all good things must come to and end."
            "She looks down at your crotch for a second."
            the_person.char "In this case, a hard, throbbing, amazing thing..."
        the_person.char "I'm going to lay here for a while again."
        mc.name "Okay. I'll lock the door behind me  when I leave."
        the_person.char "Thank you [the_person.mc_title]. Let's keep our fingers crossed!"
        "With that, you leave your office, being careful to lock the door behind you."
        "Your sperm might already be racing to her egg, ready to fertalize it. But it also might not be. To be certain, you should breed her as often as you can over the next few days."
    else:
        mc.name "Sorry, I'm just too tired, I shouldn't have tried this right now..."
        the_person.char "It's okay... You've been pushing yoursel pretty hard."
        the_person.char "Besides, I'm probably already pregnant. This is just making certain of it!"
        "You both get up and leave your office, resuming your day."
    call advance_time from cuckold_advance_time
    return
