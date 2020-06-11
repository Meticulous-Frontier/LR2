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

### The next three functions define the quest progress tracker, init requirements, and how we clean up after quest is done.
init 1 python:
    def setup_quest_cuckold_employee():
        quest_cuckold_employee.quest_event_dict["target"] = quest_cuckold_employee_person_find_employee()
        quest_cuckold_employee.quest_event_dict["start_day"] = 9999
        quest_cuckold_employee.quest_event_dict["decision_day"] = 9999
        quest_cuckold_employee.quest_event_dict["fertility_day"] = 9999
        quest_cuckold_employee.quest_event_dict["creampie_count"] = 0
        quest_cuckold_employee.set_quest_flag(1)
        quest_cuckold_employee_get_target().add_opinion("creampies", 2, discovered = False)
        quest_cuckold_employee_get_target().add_opinion("bareback sex", 2, discovered = False)
        return

    def quest_cuckold_employee_get_target():
        return quest_cuckold_employee.quest_event_dict.get("target", None)

    def quest_cuckold_employee_tracker():
        if quest_cuckold_employee.get_quest_flag() <= 1:
            mc.business.add_unique_mandatory_crisis(quest_cuckold_employee_intro)
        elif quest_cuckold_employee.get_quest_flag() == 11:
            mc.business.add_unique_mandatory_crisis(quest_cuckold_employee_decision)
        elif quest_cuckold_employee.get_quest_flag() == 21:
            mc.business.add_unique_mandatory_crisis(quest_cuckold_employee_rethink_decision)
            mc.business.add_unique_mandatory_crisis(quest_cuckold_employee_after_window)
        elif quest_cuckold_employee.get_quest_flag() == 22:
            quest_cuckold_employee_get_target().add_unique_on_talk_event(quest_cuckold_employee_breeding_session)
            mc.business.add_unique_mandatory_crisis(quest_cuckold_employee_after_window)
        elif quest_cuckold_employee.get_quest_flag() == 25:
            mc.business.add_unique_mandatory_crisis(quest_cuckold_employee_gloryhole)
        elif quest_cuckold_employee.get_quest_flag() == 28:  #BAD END
            quest_cuckold_employee.quest_complete = True
        elif quest_cuckold_employee.get_quest_flag() == 29:  #BAD END
            quest_cuckold_employee.quest_complete = True
        elif quest_cuckold_employee.get_quest_flag() == 31:  #BAD END
            quest_cuckold_employee_get_target().add_unique_on_talk_event(quest_cuckold_employee_breeding_session)
        elif quest_cuckold_employee.get_quest_flag() == 35:  #neutral end
            quest_cuckold_employee.quest_complete = True
        elif quest_cuckold_employee.get_quest_flag() == 39:  #BAD END
            quest_cuckold_employee.quest_complete = True
        elif quest_cuckold_employee.get_quest_flag() == 49:   #BAD END
            quest_cuckold_employee_get_target().add_unique_on_talk_event(quest_cuckold_employee_reconsider)
            quest_cuckold_employee.quest_complete = True
        elif quest_cuckold_employee.get_quest_flag() == 101:
            quest_cuckold_employee.quest_complete = True
            mc.business.add_unique_mandatory_crisis(quest_cuckold_employee_knocked_up)
        elif quest_cuckold_employee.get_quest_flag() == 102:
            quest_cuckold_employee.quest_complete = True
        return

    def quest_cuckold_employee_start_requirement():
        if quest_cuckold_employee_person_find_employee():
            return True
        return False

    def quest_cuckold_employee_cleanup():
        remove_mandatory_crisis_list_action("quest_cuckold_employee_intro_label")
        remove_mandatory_crisis_list_action("quest_cuckold_employee_decision_label")
        remove_mandatory_crisis_list_action("quest_cuckold_employee_rethink_decision_label")
        remove_mandatory_crisis_list_action("quest_cuckold_employee_after_window_label")
        remove_mandatory_crisis_list_action("quest_cuckold_employee_gloryhole_label")
        quest_cuckold_employee_get_target().remove_on_talk_event(quest_cuckold_employee_breeding_session)
        #Leave knocked up and reconsider events in the stack to run after quest finishes.
        # cleanup dictionary to save space and memory
        quest_cuckold_employee.quest_event_dict.clear()
        return

###Declare any requirement functions
    def quest_cuckold_employee_intro_requirement():
        if mc.business.is_open_for_business():
            if mc.is_at_work():
                return True
        return False

    def quest_cuckold_employee_decision_requirement():
        if mc.business.is_open_for_business():
            if mc.is_at_work():
                if quest_cuckold_employee.quest_event_dict.get("start_day", 0) + 2 < day: #Atleast two days after first convo
                #TODO random element so it isn't necessarily in the morning?
                    return True
        return False

    def quest_cuckold_employee_rethink_decision_requirement():
        if mc.business.is_open_for_business():
            if mc.is_at_work():
                if quest_cuckold_employee.quest_event_dict.get("decision_day", 0) + 2 < day:
                    return True
        return False

    def quest_cuckold_employee_breeding_session_requirement(the_person):
        if mc.is_at_work():
            return True
        return False

    def quest_cuckold_employee_after_window_requirement():
        if quest_cuckold_employee.quest_event_dict.get("fertility_day", 0) + 3 < day:
            if time_of_day == 2:
                return True
        return False

    def quest_cuckold_employee_reconsider_requirement(the_person):
        if quest_cuckold_employee.quest_event_dict.get("fertility_day", 0) + 5 < day:
            return True
        return False

    def quest_cuckold_employee_knocked_up_requirement():
        if mc.business.is_open_for_business():
            if mc.is_at_work():
                if quest_cuckold_employee.quest_event_dict.get("fertility_day", 0) + 7 < day:
                    if time_of_day == 2:
                        return True
        return False

    def quest_cuckold_employee_gloryhole_requirement():
        if mc.business.is_open_for_business():
            if mc.is_at_work():
                if quest_cuckold_employee.quest_event_dict.get("decision_day", 0) + 2 < day:
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
    quest_cuckold_employee_intro = Action("Begin Cuckold Quest", quest_cuckold_employee_intro_requirement, "quest_cuckold_employee_intro_label")
    quest_cuckold_employee_decision = Action("Begin Cuckold Quest", quest_cuckold_employee_decision_requirement, "quest_cuckold_employee_decision_label")
    quest_cuckold_employee_rethink_decision = Action("Begin Cuckold Quest", quest_cuckold_employee_rethink_decision_requirement, "quest_cuckold_employee_rethink_decision_label")
    quest_cuckold_employee_breeding_session = Action("Begin Cuckold Quest", quest_cuckold_employee_breeding_session_requirement, "quest_cuckold_employee_breeding_session_label")
    quest_cuckold_employee_after_window = Action("Begin Cuckold Quest", quest_cuckold_employee_after_window_requirement, "quest_cuckold_employee_after_window_label")
    quest_cuckold_employee_reconsider = Action("Begin Cuckold Quest", quest_cuckold_employee_reconsider_requirement, "quest_cuckold_employee_reconsider_label")
    quest_cuckold_employee_knocked_up = Action("Begin Cuckold Quest", quest_cuckold_employee_knocked_up_requirement, "quest_cuckold_employee_knocked_up_label")
    quest_cuckold_employee_gloryhole = Action("Begin Cuckold Quest", quest_cuckold_employee_gloryhole_requirement, "quest_cuckold_employee_gloryhole_label")

#Quest Labels. This is the story you want to tell!
label quest_cuckold_employee_init_label(): #Use this function to set quest specific variables.
    $ setup_quest_cuckold_employee()
    return

label quest_cuckold_employee_intro_label():
    $ the_person = quest_cuckold_employee_get_target()
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
    $ quest_cuckold_employee.set_quest_flag(11)
    return

label quest_cuckold_employee_decision_label():
    $ the_person = quest_cuckold_employee_get_target()
    $ quest_cuckold_employee.quest_event_dict["decision_day"] = day
    if the_person == None:
        #ABORT ABORT, we fucked up somewhere.
        return
    "You are lost in your work when a feminine voice clearing her throat nearby catches your attention. You look up and see [the_person.title] standing in front of you again."
    mc.name "Hello [the_person.title]. Can I help you?"
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
                $ the_person.ideal_fertile_day = (day % 30) + 2  #Peak fertility is in 2 days.
                $ quest_cuckold_employee.quest_event_dict["fertility_day"] = day + 2
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
                the_person.char "Umm, you? Oh geez. I'm sorry, you're my boss! That wouldn't be right!"
                "She changes her voice to imitate a masculinity."
                the_person.char "Oh honey! The baby is so cute... but he looks just like your boss???"
                "She shakes her head."
                the_person.char "I appreciate the thought, you've definitely given me something to think about, but I'm not sure that is a good idea."
                mc.name "Okay, well if you change your mind, let me know."
                the_person.char "Yeah... right... fucking my boss... bareback... totally not a good idea..."
                $ the_person.draw_person(position = "walking_away")
                "As [the_person.title] turns and walks away, you can almost see the wheels turning in her head."
                "Her initial reaction was not great, but you wonder if she will think about it more. Maybe you should try talking to her again in a few days?"
                $ quest_cuckold_employee.set_quest_flag(21)
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
                    the_person.char "Of course if you don't I comple... What? You would!?!"
                    $ the_person.change_happiness(15)
                    the_person.char "That's amazing! I can't believe it."
                    "She bites her lip for a moment and looks down at the floor."
                    $ the_person.ideal_fertile_day = (day % 30) + 2  #Peak fertility is in 2 days.
                    $ quest_cuckold_employee.quest_event_dict["fertility_day"] = day + 2
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
                    if mc.business.unisex_restroom_unlocks.get("unisex_restroom_gloryhole", 0) == 1: #She can try through the glory hole
                        $ quest_cuckold_employee.set_quest_flag(25)
                    else:
                        $ quest_cuckold_employee.set_quest_flag(29)
                    return
    # only get here if we are gonna breed in the office.
    "[the_person.possessive_title] follows you to your office."
    $ mc.change_location(office)
    $ mc.location.show_background()
    "After you walk in, you close the door and lock it."
    the_person.char "Let's do this. I'm ready. I'm ready to get bred!"
    $ the_person.draw_person(position = "kissing")
    "You wrap your arms around [the_person.title]. She embraces you, and you start to kiss. You hands go down to her ass."
    $ the_person.change_arousal(5)
    the_person.char "Okay, so... the best way to do this that I've read anyway, is good old fashioned missionary."
    mc.name "Get naked and lay down on my desk. I always wanted my own personal breeding stock."
    the_person.char "Oh my god, I can't believe I'm doing this. I have a bull now, oh god!"
    $ the_person.strip_outfit()
    the_person.char "Alright [the_person.mc_title]. This is it. Time to put a baby in me!"
    call fuck_person(the_person, starting_position = breeding_missionary, private= True, start_object = desk, position_locked = True, affair_ask_after = False, asked_for_condom = True) from _breed_cuckold_attempt_1
    if the_person.has_creampie_cum():
        the_person.char "Oh god, I can feel it inside me! We really did it."
        $ the_person.change_stats(happiness = 10, obedience = 10, love = 5)
        the_person.char "There's so much, god I have such a good bull."
        mc.name "Do you think that did it?"
        the_person.char "I hope so!... but you never know."
        "She gives a deep sigh."
        the_person.char "My fertility window. It starts today, but realistically I'm at my most fertile over the next 5 days."
        "She looks up at you."
        the_person.char "If you are okay with it, we should probably try again."
        mc.name "How often is best?"
        the_person.char "I mean, as often as possible during the window. It would give it the best possible chance of success."
        "[the_person.possessive_title] wants you balls deep and cumming inside her as much as possible over the next 5 days. You get goosebumps for a second just thinking about it."
        mc.name "Sounds like for the next five days you are my personal cumdump."
        the_person.char "Yum! I umm... I'm going to lay here for a while longer if thats okay with you."
        mc.name "Certainly. I'll lock the door behind me so you aren't disturbed."
        the_person.char "Thank you [the_person.mc_title]. I can't believe this is really happening!"
        mc.name "Me neither."
        "With that, you leave your office, being careful to lock the door behind you."
        "Your sperm might already be racing to her egg, ready to fertilize it. But it also might not be. To be certain, you should breed her as often as you can over the next few days."
        $ quest_cuckold_employee.quest_event_dict["creampie_count"] = quest_cuckold_employee.quest_event_dict.get("creampie_count", 0) + 1
        $ quest_cuckold_employee.set_quest_flag(22)
    else:
        "[the_person.title] is completely silent."
        the_person.char "You... you didn't even finish inside of me?"
        $ the_person.change_stats(happiness = -20, obedience = -30, love = -30)
        the_person.char "You... you just wanted to fuck me, didn't you!?!"
        mc.name "I'm sorry, I want to help you, but it's been a long day and I'm just wore out..."
        the_person.char "Fuck you! I see right through that charade. You just wanted to fuck a married woman!"
        $ the_person.draw_person(position = "walking_away")
        "[the_person.title] stands up and storms out of your office. Unfortunately, you may have damaged your relationship with her irreperably."
        $ quest_cuckold_employee.set_quest_flag(28)
    return

label quest_cuckold_employee_rethink_decision_label():
    $ the_person = quest_cuckold_employee_get_target()
    $ the_person.ideal_fertile_day = (day % 30) + 2  #Peak fertility is in 2 days.
    $ quest_cuckold_employee.quest_event_dict["fertility_day"] = day + 2
    "You are lost in paperwork when a figure enters your peripheral vision. You look up and see [the_person.title] standing in front of you."
    $ the_person.draw_person()
    mc.name "Hello [the_person.title]. Can I help you?"
    the_person.char "I think so... can we talk in private?"
    mc.name "Certainly, let's go to my office."
    "[the_person.possessive_title] follows you to your office."
    $ mc.change_location(office)
    $ mc.location.show_background()
    mc.name "So, what is on your mind?"
    "She is fidgeting a bit. She is clearly nervous about what she has to say."
    the_person.char "Well... ever since the other day, when you offered to help me with my... you know... fertility issue? I just can't seem to get the idea out of my head!"
    the_person.char "It's been running through my head over and over. Should I? Shouldn't I? My head says its wrong, but my body says MAKE A BABY. I'm going crazy."
    mc.name "Its okay. Do you need a few days off? Get out from the office for a while?"
    the_person.char "No, not at all. I want to be here, every day, as much as possible, around you."
    the_person.char "You offered... you know... to help me. Are you still willing to do that?"
    mc.name "I'll do everything in my power to get your pregnant if that is what you want."
    "She looks a little relieved, but also still nervous."
    the_person.char "My hormones are going nuts. I'm going to ovulate... probably any day now!"
    "You move a little closer to her."
    mc.name "Do you want your bull to breed you?"
    the_person.char "My bull? Oh god... Yes! I want to get bred like some kind of wild animal!"
    mc.name "Get naked and lay down on my desk. I always wanted my own personal breeding stock."
    the_person.char "Oh my god, I can't believe I'm doing this. I have a bull now, oh god!"
    $ the_person.strip_outfit()
    the_person.char "Alright [the_person.mc_title]. This is it. Time to put a baby in me!"
    call fuck_person(the_person, starting_position = breeding_missionary, private= True, start_object = desk, position_locked = True, affair_ask_after = False, asked_for_condom = True) from _breed_cuckold_attempt_3
    if the_person.has_creampie_cum():
        the_person.char "Oh god, I can feel it inside me! We really did it."
        $ the_person.change_stats(happiness = 10, obedience = 10, love = 5, slut_temp = 5)
        the_person.char "There's so much, god I have such a good bull."
        mc.name "Do you think that did it?"
        the_person.char "I hope so!... but you never know."
        "She gives a deep sigh."
        the_person.char "My fertility window. It starts today, but realistically I'm at my most fertile over the next 5 days."
        "She looks up at you."
        the_person.char "If you are okay with it, we should probably try again."
        mc.name "How often is best?"
        the_person.char "I mean, as often as possible during the window. It would give it the best possible chance of success."
        "[the_person.possessive_title] wants you balls deep and cumming inside her as much as possible over the next 5 days. You get goosebumps for a second just thinking about it."
        mc.name "Sounds like for the next five days you are my personal cumdump."
        the_person.char "Yum! I umm... I'm going to lay here for a while longer if thats okay with you."
        mc.name "Certainly. I'll lock the door behind me so you aren't disturbed."
        the_person.char "Thank you [the_person.mc_title]. I can't believe this is really happening!"
        mc.name "Me neither."
        "With that, you leave your office, being careful to lock the door behind you."
        "Your sperm might already be racing to her egg, ready to fertilize it. But it also might not be. To be certain, you should breed her as often as you can over the next few days."
        $ quest_cuckold_employee.quest_event_dict["creampie_count"] = quest_cuckold_employee.quest_event_dict.get("creampie_count", 0) + 1
        $ quest_cuckold_employee.set_quest_flag(22)
    else:
        "[the_person.title] is completely silent."
        the_person.char "You... you didn't even finish inside of me?"
        $ the_person.change_stats(happiness = -20, obedience = -30, love = -30)
        the_person.char "You... you just wanted to fuck me, didn't you!?!"
        mc.name "I'm sorry, I want to help you, but it's been a long day and I'm just wore out..."
        the_person.char "Fuck you! I see right through that charade. You just wanted to fuck a married woman!"
        $ the_person.draw_person(position = "walking_away")
        "[the_person.title] stands up and storms out of your office. Unfortunately, you may have damaged your relationship with her irreperably."
        $ quest_cuckold_employee.set_quest_flag(28)
    return

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
    mc.name "Get naked, cow. I'm just here to breed you."
    the_person.char "Oh god, its so hot when you talk to me like that."
    "You and [the_person.title] get naked."
    $ the_person.strip_outfit()
    mc.name "I'm gonna fuck you on my desk again. Tell your bull how much you want it."
    the_person.char "Oh god please! I want you to fuck me over and over until my belly is popping with your seed!"
    call fuck_person(the_person, starting_position = breeding_missionary, private= True, start_object = desk, position_locked = True, affair_ask_after = False, asked_for_condom = True) from _breed_cuckold_attempt_2
    if the_person.has_creampie_cum():
        the_person.char "Oh god, every risky load feels even better than the last..."
        $ the_person.change_stats(love = 10, happiness = 10, obedience = 10)
        "You gently rub her stomach."
        mc.name "Your hungry cunt feels like its sucking the cum out of me. It's amazing, honestly."
        mc.name "A little part of me is hoping it doesn't take right away and we have to keep trying for a while."
        the_person.char "Mmm, I'd be lying if I said I didn't feel the same way. You always cum so much, you are the perfect bull."
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
        "Your sperm might already be racing to her egg, ready to fertilize it. But it also might not be. To be certain, you should breed her as often as you can over the next few days."
        $ quest_cuckold_employee.quest_event_dict["creampie_count"] = quest_cuckold_employee.quest_event_dict.get("creampie_count", 0) + 1
    else:
        mc.name "Sorry, I'm just too tired, I shouldn't have tried this right now..."
        the_person.char "It's okay... You've been pushing yourself pretty hard."
        the_person.char "Besides, I'm probably already pregnant. This is just making certain of it!"
        "You both get up and leave your office, resuming your day."
    call advance_time from cuckold_advance_time
    return

label quest_cuckold_employee_gloryhole_label():
    $ the_person = quest_cuckold_employee.quest_event_dict.get("target", None)
    $ anon_char = get_anon_person(the_person)
    if mc.business.unisex_restroom_unlocks.get("unisex_restroom_gloryhole", 0) == 1:
        pass
    else:
        #We don't have glory hole unlocked.
        $ quest_cuckold_employee.set_quest_flag(29)
        return
    "You step into the restroom and walk into one of the stalls."
    if mc.business.unisex_restroom_unlocks.get("unisex_policy_unlock", 0) < 6:
        "You see that someone has drawn multiple hearts in red lipstick around it."
    else:
        "You see that someone has drawn an open mouth around it in lipstick."
        "Above the hole, someone has drawn a phallus, then the text 'dick goes here plz' with an arrow drawn to the hole."
        "Below, in different handwriting, someone else has written 'cum inside me please!' with another arrow pointed up to the hole."
    "You finish relieving yourself, and then consider. Should you wait and see if someone comes along? Or maybe try some other time?"
    menu:
        "Wait for a few minutes":
            pass
        "Finish up and maybe try it another time":
            "You decide not to bother at this time."
            "As you step out of the stall, you almost bump into [the_person.title] as she is entering the stall next to yours."
            $ the_person.draw_person()
            the_person.char "Oh! You're done... I mean... Excuse me!"
            $ renpy.scene("Active")
            "She quickly enters the stall and closes the door."
            "Hmm... was she trying to follow you in here? You wonder if your refusal to try and knock her up has anything to do with it..."
            $ quest_cuckold_employee.set_quest_flag(39)
            return
    "As you are waiting, you hear someone enter the restroom and walk into the stall next to yours."
    "This is crazy. It could be anybody in there! You hear on the other side the toilet flush as the person finishes relieving herself. You take a deep breath, then go for it."
    "You give yourself a couple of strokes to make sure you are good and hard, then stick your cock through the glory hole."

    anon_char "Oh my god... its really happening..."

    "Sounds like your bathroom stall neighbor is interested in what she sees!"

    if the_person.has_taboo("touching_penis"):
        $ the_person.break_taboo("touching_penis", add_to_log = False)

    "You feel a soft hand grasp your member and give it a couple of strokes. You hear movement coming from the stall next to you but you aren't sure what's they are doing."

    if the_person.has_taboo(["condomless_sex", "vaginal_sex"]):
        $ the_person.break_taboo("condomless_sex", add_to_log = False)
        $ the_person.break_taboo("vaginal_sex", add_to_log = False)

    "You feel her hand hold you rigidly in place as you begin to slowly feel a hot, wet sleeve enveloping your cock."
    "It feels like she is taking you in her pussy! You let out a moan of appreciation."

    anon_char "Mmmm, its so good when it goes in."
    "You press yourself against the wall to try and push yourself as deep as you can. You are almost balls deep, but the thin wall is in the way."
    "You start to work your hips a bit, testing the limits of how far you can pull back without pulling all the way out of her."
    anon_char "Yes! Mmm that feels good."
    "It's so hot, not knowing for sure who is on the other side of the wall. You have some guesses, based on her voice, but there's no way to know for sure."
    "Actually... her voice sounds an awful lot like... [the_person.title]? Wasn't she asking you to knock her up the other day?"
    "You're giving whoever it is good hard thrusts now. Once in a while you thrust a little too hard and your hips ram into the stall wall."
    "The mystery cunt you are fucking feels like its getting wetter and wetter. The slippery channel feels so good wrapped around you."
    "Moaning and panting coming from the other stall is getting urgent now. She must be enjoying this as much as your are!"
    anon_char "Oh god don't stop, please don't stop! Cum inside me please!!!"
    "This is just too much of a coincidence. Surely this is [the_person.title]! Should you give in and seed her? Or pull out?"
    menu: #The illusion of choice lol
        "Seed Her":
            pass
        "Pull Out\n{color=#ff0000}{size=18}Too horny[cost]{/size}{/color} (disabled)":
            pass

    "Ha! Stopping was never even an option. You can feel her cunt starting to quiver and twitch. It feels TOO good!"
    "You give several more strong thrusts as you pass the point of no return. You moan as you begin to dump your load inside of her."
    anon_char "Yes. Yes! Oh fuck yes!"
    "You cum as deep inside of her as you can manage. Maybe you knocked her up? There's atleast some plausable deniability in it now, if it DOES happen to be [the_person.title]..."
    "You pull out. You grab some toilet paper and wipe your cock off."

    # the person is happy and a sluttier (don't log as to preserve anonymity)
    $ the_person.change_slut_temp(5, add_to_log = False)
    $ the_person.change_happiness(5, add_to_log = False)
    if not the_person.is_pregnant():
        $ become_pregnant(the_person)
    $ quest_cuckold_employee.set_quest_flag(35)

    $ del anon_char
    return


label quest_cuckold_employee_after_window_label():
    $ the_person = quest_cuckold_employee.quest_event_dict.get("target", None)
    if not the_person.is_pregnant():
        if quest_cuckold_employee.quest_event_dict.get("creampie_count", 0) >= 5:  #You creamed her atleast 5 times via the event. #TODO we should probably track this via person.sex_record instead...
            $ become_pregnant(the_person)

    if the_person.is_pregnant():#Success
        "You get a text message from [the_person.title]."
        the_person.char "Hey bull! I was supposed to start my period a couple of days ago, but I haven't. Just thought you might find that interesting ;)"
        "Oh boy, a missed period is a good sign! You wonder if your seed is growing inside of her..."
        the_person.char "I'll be able to test for sure in a couple of days! I wouldn't mind a couple more tries between now and then though... just in case my period is just late."
        "You text her back."
        mc.name "I'll make time to breed you again cow. Look forward to it."
        $ the_person.on_room_enter_event_list.remove(preg_announce_action)  #We are overriding this event and doing our own announcement. No reason to use vanilla one in this situation.
        $ quest_cuckold_employee.set_quest_flag(101)
        return

    else:
        "You get a text message from [the_person.title]."
        the_person.char "Hey... just wanted to let you know I just started my period. I guess it didn't take."
        "Damn, maybe you can try again next cycle!"
        mc.name "We can try again in a few weeks."
        the_person.char "Hmm... yeah, maybe..."
        "Sounds like she might be having second thoughts..."
        $ quest_cuckold_employee.set_quest_flag(49)
    return

label quest_cuckold_employee_reconsider_label(the_person):
    "You walk up to [the_person.title]. When she sees you she frowns."
    $ the_person.draw_person(emotion = "sad")
    the_person.char "Hey [the_person.mc_title]... I've been meaning to talk to you..."
    mc.name "Is everything okay?"
    the_person.char "Yeah... Just... I've been thinking a lot about things between you and me."
    mc.name "And?"
    the_person.char "I was letting my hormones run away with me. Messing around was a lot of fun, but, I changed my mind. I don't want to keep trying to get pregnant."
    mc.name "I understand, and I'll do my best to respect that."
    the_person.char "Ah... okay... Thanks! Is there anything else I can do for you?"
    return

label quest_cuckold_employee_knocked_up_label():
    $ the_person = quest_cuckold_employee.quest_event_dict.get("target", None)
    "You get a text message from [the_person.title]."
    the_person.char "Hey! I need to see you in your office, ASAP!"
    $ mc.change_location(office)
    $ mc.location.show_background()
    $ the_person.draw_person(position = "stand4")
    "As you step into your office, you see [the_person.possessive_title]."
    the_person.char "Well [the_person.mc_title], you did it! Positive pregnancy test!"
    mc.name "Oh my god, that's amazing! Congratulations!"
    the_person.char "I know! I can't wait to tell my husband... Its so weird though, knowing in my head that it isn't even his?"
    menu:
        "Leave your [so_title] for me." if the_person.love + 10 > leave_SO_love_calculation(the_person):   #Hide yo wife
            mc.name "[the_person.title], think it's time you left him so we can be together. It isn't right hiding this from him.."
            "[the_person.title] seems nervous, you can tell she is dealing with some guilt after cheating on her husband."
            the_person.char "I know... you're right. I know you're right! This has gone on long enough. I'll... I'll tell him later today."
            #call transform_affair(the_person) from _call_transform_affair_4  #TODO this isn't the right function, because you aren't currently having an affair? Figure this branch out.
            the_person.char "I cant believe it, I'm really doing this. You're my one and only bull now."

        "You're doing the right thing.":      #Be the good guy
            mc.name "I'm really happy for you. Don't worry, your secret is safe with. For all purposes, the baby IS his."
            the_person.char "Yeah... I know... Its just hard, you know?"
            "She gets a sulty tone to her voice."
            the_person.char "If you want to, you can still cum inside me once in a while... It was kinda hot, playing around with breeding."
            mc.name "I'm happy to be your bull whenever you need it."
    the_person.char "Do you think, I could just start calling you that? My bull?"
    mc.name "As long as you are my happy cow."
    $ the_person.set_mc_title("Bull")
    $ the_person.set_title("Cow")
    $ the_person.set_possessive_title("Your Personal Breeding Stock")
    "She puts her hand on your chest. She traces a few circles around it, then slower lowers her hand to your crotch. She starts to stroke the shaft."
    the_person.char "Mmm, it just feel so... virile..."
    the_person.char "Do you need a little release? I know I'm alrady pregnant but..."
    "You growl at her."
    mc.name "Bend over, [the_person.title]. I need a hole for my seed."
    $ the_person.change_arousal(20)
    the_person.char "Yes my [the_person.mc_title]!"
    $ the_person.draw_person(position = "doggy")
    "Her ass in position, you quickly get her ready."
    $ the_person.strip_outfit( exclude_upper = True)
    call fuck_person(the_person, starting_position = doggy, private = True, affair_ask_after = False, asked_for_condom = True) from _breed_cuckold_victory_lap_01
    if the_person.has_creampie_cum():
        the_person.char "Sweet jesus, no wonder you knocked me up. I'm so full of your cum, its amazing..."
    "After you both recover, you carefully leave your office. Sounds like you have your very own breeding stock available from now on!"
    "It's going to be amazing to watch her belly swell with your seed."
    $ the_person.change_stats(obedience = 20, slut_temp = 20, slut_core = 20)  #She is now your slutty breeding stock.
    #TODO consider giving her a collar?
    $ the_person.personality = get_breeding_stock_personality(the_person)
    return

init 1301 python:
    def breeding_stock_titles(the_person):
        return "Cow"
    def breeding_stock_possessive_titles(the_person):
        return "Your Breeding Stock"
    def breeding_stock_player_titles(the_person):
        return "Bull"
    def get_breeding_stock_personality(the_person): #Use a function to get this so we can keep the girls prefix so her personality doesn't change TOO much
        breeding_stock = Personality("breeding_stock", default_prefix = the_person.personality.personality_type_prefix,
        common_likes = [],
        common_sexy_likes = [],
        common_dislikes = [],
        common_sexy_dislikes = [],
        titles_function = breeding_stock_titles, possessive_titles_function = breeding_stock_possessive_titles, player_titles_function = breeding_stock_player_titles)
        return breeding_stock

label breeding_stock_greetings(the_person):
    $ update_ass_condition(the_person)
    if the_person.has_creampie_cum():

        the_person.char "Hi [the_person.mc_title]!"
        "She lowers her voice to a whisper."
        the_person.char "I can still feel your seed deep inside me, but if you want to go again, I'll happily take another load..."
        if the_person.knows_pregnant():
            "She rubs her belly, absent mindedly."

    else:
        he_person.char "Hi [the_person.mc_title]!"
        "She lowers her voice to a whisper."
        the_person.char "Its been a bit since you filled me up. Want to?"
        if the_person.knows_pregnant():
            "She rubs her belly, absent mindedly."
    return

label breeding_stock_anal_sex_taboo_break(the_person):
    the_person.char "I can't believe we're doing this... Do you think when you get ready to cum you could... you know, slip it in my pussy?"
    mc.name "Maybe, it depends on how good your ass is."
    if not the_person.knows_pregnant():
        the_person.char "Sure but like... how are you gonna get me pregnant if you don't put it in the right hole?"
    else:
        the_person.char "I know I'm already pregnant but, I just love it when you cum in my other hole, okay?"
    mc.name "I'll do my best, but no promises."
    return

label breeding_stock_sex_responses_vaginal(the_person):
    if mc.condom:
        the_person.char "Mmm, your cock feel good inside me, but you know what would be better? If we took off that awful latex condom."
        if the_person.knows_pregnant():
            the_person.char "I mean, I'm already pregnant! What's the harm in going bare?"
        else:
            the_person.char "I want to feel everything, and the warmth that goes deep when you cum inside me..."
        menu:
            "Take the condom off":
                mc.name "You're right, what was I thinking?"
                "You pull out for a second, then pull the condom off and resume fucking her."
                $ mc.condom = False
                "She gets goosebumps when you bottom out inside of her, completely bareback."
                $ the_person.change_arousal(20)
                the_person.char "Oh fuck! That's it!"
            "Leave it on":
                mc.name "Sorry, I think this should stay on for now."
                "She gives you a pouting face."
                the_person.char "You know I'm just going to keep asking right?"

    else:
        the_person.char "Keep fucking me [the_person.mc_title], it feels fantastic!"

    return

label breeding_stock_cum_vagina(the_person):
    if mc.condom:
        the_person.char "Mmm, your cum feels so warm, but why did you waste it in that condom?"

    else:
        if the_person.on_birth_control:
            the_person.char "Oh fuck, it's so warm. I can feel it inside me..."
            "She sighs happily as you cum inside her."
        elif the_person.is_pregnant():
            the_person.char "Mmm, it's so warm... its feels so good, just like the load that knocked me up!"
        else:
            the_person.char "Oh my good its sooo good. Come on little swimmers, knock me up!"
    return
