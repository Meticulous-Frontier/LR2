#Mid game quest. Is available mid game, will allow you to knock an employee up early..
#Requires a married woman with no children at least sluttiness... 40? 60?
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
        person = quest_cuckold_employee_person_find_employee()
        quest = quest_cuckold_employee()
        quest.quest_event_dict["target"] = person.identifier
        quest.quest_event_dict["start_day"] = 9999
        quest.quest_event_dict["decision_day"] = 9999
        quest.quest_event_dict["fertility_day"] = 9999
        quest.quest_event_dict["creampie_count"] = 0
        quest.set_quest_flag(1)
        person.add_opinion("creampies", 2, discovered = False, add_to_log = False)
        person.add_opinion("bareback sex", 2, discovered = False, add_to_log = False)
        person.add_opinion("vaginal sex", 2, discovered = False, add_to_log = False)
        person.on_birth_control = False
        mc.business.add_mandatory_crisis(quest_cuckold_employee_intro)
        game_hints.append(Hint("Cuckold Employee", "An employee is having trouble conceiving.", "quest_cuckold_employee().get_quest_flag() <= 11", "quest_cuckold_employee().get_quest_flag() > 11"))
        hint_string = "Let " + person.title + " think about it for a few days."
        game_hints.append(Hint("Cuckold Employee", hint_string, "quest_cuckold_employee().get_quest_flag() == 21", "quest_cuckold_employee().get_quest_flag() != 21"))
        hint_string_2 = "Creampie " + person.title + " as much as possible. At least 5 times for best possible outcome."
        game_hints.append(Hint("Cuckold Employee", hint_string_2, "quest_cuckold_employee().get_quest_flag() == 22", "quest_cuckold_employee().get_quest_flag() != 22"))
        hint_string_3 = person.title + " is probably pregnant. She'll let you know in a few days."
        game_hints.append(Hint("Cuckold Employee", hint_string_3, "quest_cuckold_employee().get_quest_flag() == 91", "quest_cuckold_employee().get_quest_flag() != 91"))
        return

    def quest_cuckold_employee():
        return quest_director.get_quest("Cuckold Employee")

    def quest_cuckold_employee_get_target():
        contact = quest_cuckold_employee().quest_event_dict.get("target", None)
        if isinstance(contact, basestring):
            return get_person_by_identifier(contact)
        return contact

    def quest_cuckold_employee_tracker():
        person = quest_cuckold_employee_get_target()
        if quest_cuckold_employee().get_quest_flag() == 22:
            if person and not quest_cuckold_employee_breeding_session in person.on_talk_event_list:
                # readd the breeding session (we talked to her without breeding)
                person.add_unique_on_talk_event(quest_cuckold_employee_breeding_session)
        if quest_cuckold_employee().get_quest_flag() <= 101:
            if person == None:
                quest_cuckold_employee().quest_completed()
                return
        return

    def quest_cuckold_employee_start_requirement():
        if day < 50: # don't start this until we have a better employee base
            return False
        if persistent.pregnancy_pref > 0:
            if quest_cuckold_employee_person_find_employee():
                return True
        return False

    def quest_cuckold_employee_cleanup():
        mc.business.remove_mandatory_crisis("quest_cuckold_employee_intro_label")
        mc.business.remove_mandatory_crisis("quest_cuckold_employee_decision_label")
        mc.business.remove_mandatory_crisis("quest_cuckold_employee_rethink_decision_label")
        mc.business.remove_mandatory_crisis("quest_cuckold_employee_after_window_label")
        mc.business.remove_mandatory_crisis("quest_cuckold_employee_gloryhole_label")
        if quest_cuckold_employee_get_target():
            quest_cuckold_employee_get_target().remove_on_talk_event(quest_cuckold_employee_breeding_session)
        #Leave knocked up and reconsider events in the stack to run after quest finishes.
        # cleanup dictionary to save space and memory
        quest_cuckold_employee().quest_event_dict.clear()
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
                if quest_cuckold_employee().quest_event_dict.get("start_day", 0) + 2 < day: #at least two days after first convo
                #TODO random element so it isn't necessarily in the morning?
                    return True
        return False

    def quest_cuckold_employee_rethink_decision_requirement():
        if mc.business.is_open_for_business():
            if mc.is_at_work():
                if quest_cuckold_employee().quest_event_dict.get("decision_day", 0) + 2 < day:
                    return True
        return False

    def quest_cuckold_employee_breeding_session_requirement(the_person):
        if mc.is_at_work():
            return True
        return False

    def quest_cuckold_employee_after_window_requirement():
        if quest_cuckold_employee().quest_event_dict.get("fertility_day", 0) + 3 < day:
            if time_of_day == 2:
                return True
        return False

    def quest_cuckold_employee_reconsider_requirement(the_person):
        if quest_cuckold_employee().quest_event_dict.get("fertility_day", 0) + 5 < day:
            return True
        return False

    def quest_cuckold_employee_knocked_up_requirement():
        if mc.business.is_open_for_business():
            if mc.is_at_work():
                if quest_cuckold_employee().quest_event_dict.get("fertility_day", 0) + 7 < day:
                    if time_of_day == 2:
                        return True
        return False

    def quest_cuckold_employee_gloryhole_requirement():
        if mc.business.is_open_for_business():
            if mc.is_at_work():
                if quest_cuckold_employee().quest_event_dict.get("decision_day", 0) + 2 < day:
                    return True
        return False

###Functions unique to the quest
    def quest_cuckold_employee_person_find_employee():
        able_person_list = []
        for person in mc.business.get_employee_list():
            if not quest_director.is_person_blocked(person):
                if person.sluttiness > 50 and not person.is_pregnant():
                    if person.relationship == "Married" and person.kids == 0:
                        able_person_list.append(person)
        return get_random_from_list(able_person_list)

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
        $ quest_cuckold_employee().quest_completed()
        return
    # lock selected person out of other quests
    $ quest_director.add_unavailable_person(the_person)
    "You working diligently when a figure appears in your peripheral vision. You look up and see [the_person.title] standing in front of you."
    $ the_person.draw_person(emotion = "sad")
    mc.name "Hello [the_person.title]. Can I help you?"
    the_person "Hopefully! I was just wondering... we've worked on a lot of drugs around here... have we ever made any progress on drugs that can increase... fertility?"
    mc.name "As a matter of fact..."
    the_person "Male fertility, to be exact."
    mc.name "Oh! Well... to be honest, no, we haven't."
    $ the_person.change_stats(happiness = -10)
    the_person "Ah Damn. Thanks, I should have expected that."
    mc.name "... Everything okay?"
    the_person "Yeah! Yeah definitely. Everything is A-OKAY with me and [the_person.SO_name]!"
    mc.name "Oh? I didn't ask about him..."
    the_person "Right..."
    "There's a long, awkward silence."
    the_person "Welp! I'll be getting back to work now!"
    mc.name "Take care."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] begins to walk away. Well that was an awkward moment..."
    $ quest_cuckold_employee().quest_event_dict["start_day"] = day
    $ quest_cuckold_employee().set_quest_flag(11)
    $ mc.business.add_mandatory_crisis(quest_cuckold_employee_decision)
    return

label quest_cuckold_employee_decision_label():
    $ the_person = quest_cuckold_employee_get_target()
    $ quest_cuckold_employee().quest_event_dict["decision_day"] = day
    if the_person == None:
        #ABORT ABORT, we fucked up somewhere.
        $ quest_cuckold_employee().quest_completed()
        return
    $ the_person.draw_person()
    "You are lost in your work when a feminine voice clearing her throat nearby catches your attention. You look up and see [the_person.title] standing in front of you again."
    mc.name "Hello [the_person.title]. Can I help you?"
    the_person "Well, kind of yes, kind of no."
    mc.name "I'm sorry?"
    the_person "I just... I need to vent to someone about something, but I don't trust the other girls around here not to gossip about it."
    mc.name "Of course, you can talk to me about anything."
    the_person "Well... my husband and I... we've been trying to have a baby lately, but after months of trying, still nothing."
    the_person "I did something I probably shouldn't have... I took a semen sample when we had sex a few days ago secretly and had it analyzed."
    the_person "He is basically infertile. I'm absolutely crushed! I love him so much, but I also want to have a baby so bad."
    mc.name "I understand. It might take a while for you to grieve this if you need some time off."
    the_person "No, no, that's not it. I keep thinking, maybe there is some way, you know? Maybe a miracle will happen, or some drug or something will be invented that can help."
    the_person "I can't leave him, but my body is screaming at me. The urge to make a baby is SO strong!"
    mc.name "Have you considered something like a sperm bank?"
    the_person "No... I'd have to tell him that he is infertile. It would crush him! I'm not sure our relationship would survive that."
    "Hmmm... well... there is always another way of getting pregnant... You wonder if she has considered it at all."
    "You could always offer to knock her up. But then again, impregnating another man's wife could lead  you to some heavy drama down the road..."
    menu:
        "Offer to help":
            mc.name "You know, [the_person.title]... there may be a solution that would allow you to have a baby AND stay with your husband."
            $ the_person.draw_person(emotion = "happy")
            the_person "Oh? What would that be?"
            mc.name "Well, if you want a baby that bad, you could always have someone else do the deed..."
            the_person "Oh... OH... Oh my..."
            "She stumbles for words for a moment."
            the_person "That's... wow... I don't know, that is an awfully big step."
            the_person "I don't even know anyone. How could I even find a man that would that?"
            if mc.charisma > 4: #Charisma check
                mc.name "I know how much this means to you. I know I'm your boss, but I'm also your friend, and I want to see you happy."
                mc.name "I would be glad to help you out if you decided that was a step you would like to take."
                the_person "Oh my! That's crazy. I never would have thought to do something like that. I don't know, that sounds pretty nuts..."
                mc.name "The urges your body are giving you are completely natural. They are only going to get stronger over time, until they drive a wedge between you and your husband."
                the_person "Oh god... you're right. I know you are. I don't want to admit it, but deep down inside, I know you are right."
                "She bites her lip for a moment and looks down at the floor."
                $ the_person.ideal_fertile_day = (day % 30) + 2  #Peak fertility is in 2 days.
                $ quest_cuckold_employee().quest_event_dict["fertility_day"] = day + 2
                the_person "I know this is kind of a crazy coincidence... but... I'm actually really fertile. Like right now."
                mc.name "Oh?"
                the_person "I've been tracking my cycles... I'm going to ovulate in the next few days almost for certain."
                the_person "Do you think... we could go to your office?"
                "She leaves the question in the air for a moment..."
                the_person "Oh my god! what am I thinking! This is crazy, I can't be..."
                mc.name "Hush. Let's go, we can definitely find some privacy in my office."
                the_person "Oh! Oh fuck, I can't believe it. Okay. Let's go."
            else:
                mc.name "It would be really no problem. I'd be glad to help you out with that..."
                the_person "Umm, you? Oh geez. I'm sorry, you're my boss! That wouldn't be right!"
                "She changes her voice to imitate a masculinity."
                the_person "Oh honey! The baby is so cute... but he looks just like your boss???"
                "She shakes her head."
                the_person "I appreciate the thought, you've definitely given me something to think about, but I'm not sure that is a good idea."
                mc.name "Okay, well if you change your mind, let me know."
                the_person "Yeah... right... fucking my boss... bareback... totally not a good idea..."
                $ the_person.draw_person(position = "walking_away")
                "As [the_person.title] turns and walks away, you can almost see the wheels turning in her head."
                "Her initial reaction was not great, but you wonder if she will think about it more. Maybe you should try talking to her again in a few days?"
                $ quest_cuckold_employee().set_quest_flag(21)
                $ mc.business.add_mandatory_crisis(quest_cuckold_employee_rethink_decision)
                $ mc.business.add_mandatory_crisis(quest_cuckold_employee_after_window)
                return
        "Stay quiet":
            "There is a long moment of silence."
            mc.name "I'm really sorry, I wish I could do something to help."
            the_person "It's okay. I mean, I just needed to vent, I wasn't expecting a solution to be... staring me in the face."
            "She's looking straight into your eyes now. You start to feel a bit uncomfortable."
            the_person "You know... you remind me a lot of my husband. Height... hair color..."
            the_person "What if there was something you could do to help? Would you do it?"
            mc.name "I guess that would depend on what that action would be."
            "She clears her throat."
            the_person "I mean, I could always get pregnant the regular way, just with someone else..."
            "IS this really going where you think it is going?"
            the_person "That person would have to be careful, of course, to keep it a secret... a dirty little secret."
            mc.name "That is certainly a possible solution."
            the_person "So umm... what would you say if I asked you? To get me pregnant I mean."
            "You weight the decision carefully."
            menu:
                "Help her":
                    mc.name "Let me see if I have this right. You are asking me, if I would be willing to fuck you, bareback, and fill you with my seed?"
                    $ the_person.change_arousal(10)
                    the_person "I mean, that's really hot sounding but completely hypothetical of course..."
                    mc.name "Fuck yeah. I would do that in a heartbeat."
                    the_person "Of course if you don't I comple... What? You would!?!"
                    $ the_person.change_happiness(5)
                    the_person "That's amazing! I can't believe it."
                    "She bites her lip for a moment and looks down at the floor."
                    $ the_person.ideal_fertile_day = (day % 30) + 2  #Peak fertility is in 2 days.
                    $ quest_cuckold_employee().quest_event_dict["fertility_day"] = day + 2
                    the_person "I know this is kind of a crazy coincidence... but... I'm actually really fertile. Like right now."
                    mc.name "Oh?"
                    the_person "I've been tracking my cycles... I'm going to ovulate in the next few days almost for certain."
                    the_person "Do you think... we could go to your office?"
                    mc.name "Let's go, we can definitely find some privacy in my office."
                    the_person "Oh! Oh fuck, I can't believe it. Okay. Let's go."
                "Can't help":
                    mc.name "I understand what you are going through, but I just don't think I can do that. Not without having your husband on board with it."
                    "She groans."
                    the_person "Nooo, he would never agree to it! I need someone to keep it secret..."
                    mc.name "I'm sorry, I feel like that is a line I'm not willing to cross."
                    the_person "That's... ARG! Okay okay okay. I get it!"
                    "She takes a deep breath."
                    the_person "I'm sorry. I shouldn't have asked, that was really inappropriate."
                    $ the_person.change_obedience(5)
                    mc.name "It's alright."
                    $ the_person.draw_person(position = "walking_away")
                    "[the_person.possessive_title] turns and walks away. You wonder if you have heard the last of this?"
                    if mc.business.unisex_restroom_unlocks.get("unisex_restroom_gloryhole", 0) == 1: #She can try through the glory hole
                        $ mc.business.add_mandatory_crisis(quest_cuckold_employee_gloryhole)
                        $ quest_cuckold_employee().set_quest_flag(25)
                    else:
                        $ quest_cuckold_employee().set_quest_flag(29)
                        $ quest_cuckold_employee().quest_completed()
                    return
    # only get here if we are gonna breed in the office.
    "[the_person.possessive_title] follows you to your office."
    $ mc.change_location(office)
    $ ceo_office.show_background()
    "After you walk in, you close the door and lock it."
    the_person "Let's do this. I'm ready. I'm ready to get bred!"
    $ the_person.draw_person(position = "kissing")
    "You wrap your arms around [the_person.title]. She embraces you, and you start to kiss. You hands go down to her ass."
    $ the_person.change_arousal(5)
    the_person "Okay, so... the best way to do this that I've read anyway, is good old fashioned missionary."
    mc.name "Get ready and lay down on my desk. I always wanted my own personal breeding stock."
    the_person "Oh my god, I can't believe I'm doing this. I have a bull now, oh god!"
    "[the_person.possessive_title] gets on your desk and lays on her back."
    $ the_person.draw_person(position = "missionary")
    if the_person.outfit.vagina_available():
        "She spreads her legs, her pussy on display in front of you."
    else:
        if the_person.outfit.can_half_off_to_vagina():
            $ generalised_strip_description(the_person, the_person.outfit.get_half_off_to_vagina_list(), half_off_instead = True, position = "missionary")
        else:
            $ generalised_strip_description(the_person, the_person.outfit.get_vagina_strip_list(), position = "missionary")
    the_person "Alright [the_person.mc_title]. This is it. Time to put a baby in me!"
    call fuck_person(the_person, start_position = breeding_missionary, start_object = make_desk(), private= True, position_locked = True, skip_intro = True, affair_ask_after = False, skip_condom = True) from _breed_cuckold_attempt_1
    $ the_report = _return
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    if the_report.get("guy orgasms", 0) > 0 and the_person.has_creampie_cum():
        the_person "Oh god, I can feel it inside me! We really did it."
        $ the_person.change_stats(happiness = 2, obedience = 2, love = 1)
        the_person "There's so much, god I have such a good bull."
        mc.name "Do you think that did it?"
        the_person "I hope so!... but you never know."
        "She gives a deep sigh."
        the_person "My fertility window. It starts today, but realistically I'm at my most fertile over the next 5 days."
        "She looks up at you."
        the_person "If you are okay with it, we should probably try again."
        mc.name "How often is best?"
        the_person "I mean, as often as possible during the window. It would give it the best possible chance of success."
        "[the_person.possessive_title] wants you balls deep and cumming inside her as much as possible over the next 5 days. You get goosebumps for a second just thinking about it."
        mc.name "Sounds like for the next five days you are my personal cumdump."
        the_person "Yum! I umm... I'm going to lay here for a while longer if that's okay with you."
        mc.name "Certainly. I'll lock the door behind me so you aren't disturbed."
        the_person "Thank you [the_person.mc_title]. I can't believe this is really happening!"
        mc.name "Me neither."
        "With that, you leave your office, being careful to lock the door behind you."
        $ clear_scene()
        $ mc.location.show_background()
        "Your sperm might already be racing to her egg, ready to fertilize it, but it also might not be. To be certain, you should breed her as often as you can over the next few days."
        $ quest_cuckold_employee().quest_event_dict["creampie_count"] = quest_cuckold_employee().quest_event_dict.get("creampie_count", 0) + 1
        $ quest_cuckold_employee().set_quest_flag(22)
        $ the_person.add_unique_on_talk_event(quest_cuckold_employee_breeding_session)
        $ mc.business.add_mandatory_crisis(quest_cuckold_employee_after_window)
        $ the_person.apply_planned_outfit() # make sure she is dressed again after event
    elif the_report.get("guy orgasms", 0) == 0:
        "[the_person.title] is completely silent."
        the_person "You... you didn't even finish. "
        the_person "Don't you like breeding me?"
        if mc.energy < 30:
            mc.name "I'm really sorry, but I'm just to tired at the moment, we can try again tomorrow."
            $ the_person.change_stats(happiness = -10, obedience = -10, love = -10)
            the_person "Alright, for just this once, I will believe you, but you better clean up your act."
            $ the_person.apply_planned_outfit()
            $ the_person.draw_person(position = "walking_away")
            "[the_person.title] stands up, throws on her clothes and storms out of your office."
            $ quest_cuckold_employee().set_quest_flag(22)
            $ the_person.add_unique_on_talk_event(quest_cuckold_employee_breeding_session)
            $ mc.business.add_mandatory_crisis(quest_cuckold_employee_after_window)
        else:
            mc.name "I'm sorry, I want to help you, but it's been a long day and I'm just wore out..."
            the_person "Fuck you! I see right through that charade. You just wanted to fuck a married woman!"
            $ the_person.apply_planned_outfit()
            $ the_person.draw_person(position = "walking_away")
            "[the_person.title] stands up, throws on her clothes and storms out of your office. Unfortunately, you may have damaged your relationship with her irreparably."
            $ quest_cuckold_employee().set_quest_flag(28)
            $ quest_cuckold_employee().quest_completed()
    else:
        "[the_person.title] is completely silent."
        the_person "You... you didn't even finish inside of me?"
        $ the_person.change_stats(happiness = -20, obedience = -30, love = -30)
        the_person "You... you just wanted to fuck me, didn't you!?!"
        mc.name "I'm sorry, I want to help you, but it's been a long day and I'm just wore out..."
        the_person "Fuck you! I see right through that charade. You just wanted to fuck a married woman!"
        $ the_person.apply_planned_outfit()
        $ the_person.draw_person(position = "walking_away")
        "[the_person.title] stands up, throws on her clothes and storms out of your office. Unfortunately, you may have damaged your relationship with her irreparably."
        $ quest_cuckold_employee().set_quest_flag(28)
        $ quest_cuckold_employee().quest_completed()
    return

label quest_cuckold_employee_rethink_decision_label():
    $ the_person = quest_cuckold_employee_get_target()
    $ the_person.ideal_fertile_day = (day % 30) + 2  #Peak fertility is in 2 days.
    $ quest_cuckold_employee().quest_event_dict["fertility_day"] = day + 2
    "You are lost in paperwork when a figure enters your peripheral vision. You look up and see [the_person.title] standing in front of you."
    $ the_person.draw_person()
    mc.name "Hello [the_person.title]. Can I help you?"
    the_person "I think so... can we talk in private?"
    mc.name "Certainly, let's go to my office."
    "[the_person.possessive_title] follows you to your office."
    $ mc.change_location(office)
    $ ceo_office.show_background()
    mc.name "So, what is on your mind?"
    "She is fidgeting a bit. She is clearly nervous about what she has to say."
    the_person "Well... ever since the other day, when you offered to help me with my... you know... fertility issue? I just can't seem to get the idea out of my head!"
    the_person "It's been running through my head over and over. Should I? Shouldn't I? My head says it's wrong, but my body says MAKE A BABY. I'm going crazy."
    mc.name "It's okay. Do you need a few days off? Get out from the office for a while?"
    the_person "No, not at all. I want to be here, every day, as much as possible, around you."
    the_person "You offered... you know... to help me. Are you still willing to do that?"
    mc.name "I'll do everything in my power to get you pregnant if that is what you want."
    "She looks a little relieved, but also still nervous."
    the_person "My hormones are going nuts. I'm going to ovulate... probably any day now!"
    "You move a little closer to her."
    mc.name "Do you want your bull to breed you?"
    the_person "My bull? Oh god... Yes! I want to get bred like some kind of wild animal!"
    mc.name "Get ready and lay down on my desk. I always wanted my own personal breeding stock."
    the_person "Oh my god, I can't believe I'm doing this. I have a bull now, oh god!"
    "[the_person.possessive_title] gets on your desk and lays on her back."
    $ the_person.draw_person(position = "missionary")
    if the_person.outfit.vagina_available():
        "She spreads her legs, her pussy on display in front of you."
    else:
        if the_person.outfit.can_half_off_to_vagina():
            $ generalised_strip_description(the_person, the_person.outfit.get_half_off_to_vagina_list(), half_off_instead = True, position = "missionary")
        else:
            $ generalised_strip_description(the_person, the_person.outfit.get_vagina_strip_list(), position = "missionary")
    the_person "Alright [the_person.mc_title]. This is it. Time to put a baby in me!"
    call fuck_person(the_person, start_position = breeding_missionary, start_object = make_desk(), private= True, position_locked = True, skip_intro = True, affair_ask_after = False, skip_condom = True) from _breed_cuckold_attempt_3
    $ the_report = _return
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    if the_report.get("guy orgasms", 0) > 0 and the_person.has_creampie_cum():
        the_person "Oh god, I can feel it inside me! We really did it."
        $ the_person.change_stats(happiness = 2, obedience = 2, love = 1)
        the_person "There's so much, god I have such a good bull."
        mc.name "Do you think that did it?"
        the_person "I hope so!... but you never know."
        "She gives a deep sigh."
        the_person "My fertility window. It starts today, but realistically I'm at my most fertile over the next 5 days."
        "She looks up at you."
        the_person "If you are okay with it, we should probably try again."
        mc.name "How often is best?"
        the_person "I mean, as often as possible during the window. It would give it the best possible chance of success."
        "[the_person.possessive_title] wants you balls deep and cumming inside her as much as possible over the next 5 days. You get goosebumps for a second just thinking about it."
        mc.name "Sounds like for the next five days you are my personal cumdump."
        the_person "Yum! I umm... I'm going to lay here for a while longer if that's okay with you."
        mc.name "Certainly. I'll lock the door behind me so you aren't disturbed."
        the_person "Thank you [the_person.mc_title]. I can't believe this is really happening!"
        mc.name "Me neither."
        "With that, you leave your office, being careful to lock the door behind you."
        $ clear_scene()
        $ mc.location.show_background()
        "Your sperm might already be racing to her egg, ready to fertilize it, but it also might not be. To be certain, you should breed her as often as you can over the next few days."
        $ quest_cuckold_employee().quest_event_dict["creampie_count"] = quest_cuckold_employee().quest_event_dict.get("creampie_count", 0) + 1
        $ quest_cuckold_employee().set_quest_flag(22)
        $ the_person.add_unique_on_talk_event(quest_cuckold_employee_breeding_session)
        $ mc.business.add_mandatory_crisis(quest_cuckold_employee_after_window)
        $ the_person.apply_planned_outfit() # make sure she is dressed again after event
    elif the_report.get("guy orgasms", 0) == 0:
        "[the_person.title] is completely silent."
        the_person "You... you didn't even finish. "
        the_person "Don't you like breeding me?"
        if mc.energy < 30:
            mc.name "I'm really sorry, but I'm just to tired at the moment, we can try again tomorrow."
            $ the_person.change_stats(happiness = -10, obedience = -10, love = -10)
            the_person "Alright, for just this once, I will believe you, but you better clean up your act."
            $ the_person.apply_planned_outfit()
            $ the_person.draw_person(position = "walking_away")
            "[the_person.title] stands up, throws on her clothes and storms out of your office."
            $ quest_cuckold_employee().set_quest_flag(22)
            $ the_person.add_unique_on_talk_event(quest_cuckold_employee_breeding_session)
            $ mc.business.add_mandatory_crisis(quest_cuckold_employee_after_window)
        else:
            mc.name "I'm sorry, I want to help you, but it's been a long day and I'm just wore out..."
            the_person "Fuck you! I see right through that charade. You just wanted to fuck a married woman!"
            $ the_person.apply_planned_outfit()
            $ the_person.draw_person(position = "walking_away")
            "[the_person.title] stands up, throws on her clothes and storms out of your office. Unfortunately, you may have damaged your relationship with her irreparably."
            $ quest_cuckold_employee().set_quest_flag(28)
            $ quest_cuckold_employee().quest_completed()
    else:
        "[the_person.title] is completely silent."
        the_person "You... you didn't even finish inside of me?"
        $ the_person.change_stats(happiness = -20, obedience = -30, love = -30)
        the_person "You... you just wanted to fuck me, didn't you!?!"
        mc.name "I'm sorry, I want to help you, but it's been a long day and I'm just wore out..."
        the_person "Fuck you! I see right through that charade. You just wanted to fuck a married woman!"
        $ the_person.apply_planned_outfit()
        $ the_person.draw_person(position = "walking_away")
        "[the_person.title] stands up, throws on her clothes and storms out of your office. Unfortunately, you may have damaged your relationship with her irreperably."
        $ quest_cuckold_employee().set_quest_flag(28)
        $ quest_cuckold_employee().quest_completed()
    return

label quest_cuckold_employee_breeding_session_label(the_person):
    "You walk up to [the_person.title]. When she sees you she smiles."
    $ the_person.draw_person(emotion = "happy")
    the_person "Hey [the_person.mc_title]! Do you need something? I can help you out with that thing in your office again... You know what I mean, right?"
    "She is still in her fertile window. Do you want to take her to your office and try and breed her again?"
    menu:
        "Breeding session {image=gui/heart/Time_Advance.png}":
            pass
        "Not now":
            mc.name "Actually, I need to talk to you about something else."
            the_person "Oh! What can I do for you?"
            # since this is triggered inside the talk event, it is still in the list
            # so adding it here won't work, let the quest tracker reapply the talk event
            return
    mc.name "Yes that is exactly right. I really need help with something in my office, could you please come give me a hand?"
    the_person "Of course! Let's go!"
    "[the_person.possessive_title] follows you to your office."
    $ mc.change_location(office)
    $ ceo_office.show_background()
    "After you walk in, you close the door and lock it."
    the_person "I've been looking forward to this. I know that we're doing this for practical reasons, but that doesn't mean it doesn't feel really good..."
    mc.name "Get ready, cow. I'm just here to breed you."
    the_person "Oh god, it's so hot when you talk to me like that."
    "[the_person.possessive_title] gets on your desk and lays on her back."
    $ the_person.draw_person(position = "missionary")
    if the_person.outfit.vagina_available():
        "She spreads her legs, her pussy on display in front of you."
    else:
        if the_person.outfit.can_half_off_to_vagina():
            $ generalised_strip_description(the_person, the_person.outfit.get_half_off_to_vagina_list(), half_off_instead = True, position = "missionary")
        else:
            $ generalised_strip_description(the_person, the_person.outfit.get_vagina_strip_list(), position = "missionary")
    mc.name "I'm gonna fuck you on my desk again. Tell your bull how much you want it."
    the_person "Oh god please! I want you to fuck me over and over until my belly is popping with your seed!"
    call fuck_person(the_person, start_position = breeding_missionary, start_object = make_desk(), private= True, position_locked = True, skip_intro = True, affair_ask_after = False, skip_condom = True) from _breed_cuckold_attempt_2
    $ the_report = _return
    if the_report.get("guy orgasms", 0) > 0 and the_person.has_creampie_cum():
        the_person "Oh god, every risky load feels even better than the last..."
        $ the_person.change_love(1, max_modified_to = 80)
        $ the_person.change_stats(happiness = 1, obedience = 1, add_to_log = False)
        "You gently rub her stomach."
        mc.name "Your hungry cunt feels like it's sucking the cum out of me. It's amazing, honestly."
        mc.name "A little part of me is hoping it doesn't take right away and we have to keep trying for a while."
        the_person "Mmm, I'd be lying if I said I didn't feel the same way. You always cum so much, you are the perfect bull."
        if the_person.has_role(affair_role) or the_person.has_role(girlfriend_role):
            the_person "I'm so looking forward to you fucking my brains out, you will be my dirty little secret."
            "She looks down at your crotch and smiles."
        elif the_person.love > 60:
            the_person "Even if I do get pregnant... I'll already have one dirty little secret anyway. Maybe we could still fool around some..."
            "Sounds like she might be open to some kind of an affair in the future..."
        else:
            the_person "But, it's like they say, all good things must come to an end."
            "She looks down at your crotch for a second."
            the_person "In this case, a hard, throbbing, amazing thing..."
        the_person "I'm going to lay here for a while again."
        mc.name "Okay. I'll lock the door behind me  when I leave."
        the_person "Thank you [the_person.mc_title]. Let's keep our fingers crossed!"
        "With that, you leave your office, being careful to lock the door behind you."
        $ clear_scene()
        $ mc.location.show_background()
        "Your sperm might already be racing to her egg, ready to fertilize it, but it also might not be. To be certain, you should breed her as often as you can over the next few days."
        $ quest_cuckold_employee().quest_event_dict["creampie_count"] = quest_cuckold_employee().quest_event_dict.get("creampie_count", 0) + 1
    else:
        mc.name "Sorry, I'm just too tired, I shouldn't have tried this right now..."
        the_person "It's okay... You've been pushing yourself pretty hard."
        the_person "Besides, I'm probably already pregnant. This is just making certain of it!"
        "You both get up and leave your office, resuming your day."
    $ the_person.add_unique_on_talk_event(quest_cuckold_employee_breeding_session)
    $ the_person.apply_planned_outfit() # make sure she is dressed when back at workstation
    call advance_time from cuckold_advance_time
    return

label quest_cuckold_employee_gloryhole_label():
    $ the_person = quest_cuckold_employee_get_target()
    $ anon_char = get_anon_person(the_person)
    if mc.business.unisex_restroom_unlocks.get("unisex_restroom_gloryhole", 0) == 1:
        pass
    else:
        #We don't have glory hole unlocked.
        $ quest_cuckold_employee().set_quest_flag(29)
        $ quest_cuckold_employee().quest_completed()
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
            the_person "Oh! You're done... I mean... Excuse me!"
            $ clear_scene()
            "She quickly enters the stall and closes the door."
            "Hmm... was she trying to follow you in here? You wonder if your refusal to try and knock her up has anything to do with it..."
            $ quest_cuckold_employee().set_quest_flag(39)
            $ quest_cuckold_employee().quest_completed()
            return
    "As you are waiting, you hear someone enter the restroom and walk into the stall next to yours."
    "This is crazy. It could be anybody in there! You hear on the other side the toilet flush as the person finishes relieving herself. You take a deep breath, then go for it."
    "You give yourself a couple of strokes to make sure you are good and hard, then stick your cock through the glory hole."

    anon_char "Oh my god... it's really happening..."

    "Sounds like your bathroom stall neighbor is interested in what she sees!"

    if the_person.has_taboo("touching_penis"):
        $ the_person.break_taboo("touching_penis", add_to_log = False)

    "You feel a soft hand grasp your member and give it a couple of strokes. You hear movement coming from the stall next to you but you aren't sure what's they are doing."

    if the_person.has_taboo(["condomless_sex", "vaginal_sex"]):
        $ the_person.break_taboo("condomless_sex", add_to_log = False)
        $ the_person.break_taboo("vaginal_sex", add_to_log = False)

    "You feel her hand hold you rigidly in place as you begin to slowly feel a hot, wet sleeve enveloping your cock."
    "It feels like she is taking you in her pussy! You let out a moan of appreciation."

    anon_char "Mmmm, it's so good when it goes in."
    "You press yourself against the wall to try and push yourself as deep as you can. You are almost balls deep, but the thin wall is in the way."
    "You start to work your hips a bit, testing the limits of how far you can pull back without pulling all the way out of her."
    anon_char "Yes! Mmm that feels good."
    "It's so hot, not knowing for sure who is on the other side of the wall. You have some guesses, based on her voice, but there's no way to know for sure."
    "Actually... her voice sounds an awful lot like... [the_person.title]? Wasn't she asking you to knock her up the other day?"
    "You're giving whoever it is good hard thrusts now. Once in a while you thrust a little too hard and your hips ram into the stall wall."
    "The mystery cunt you are fucking feels like it's getting wetter and wetter. The slippery channel feels so good wrapped around you."
    "Moaning and panting coming from the other stall is getting urgent now. She must be enjoying this as much as you are!"
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
    "You cum as deep inside of her as you can manage. Maybe you knocked her up? There's at least some plausible deniability in it now, if it DOES happen to be [the_person.title]..."
    "You pull out. You grab some toilet paper and wipe your cock off."

    # the person is happy and a sluttier (don't log as to preserve anonymity)
    $ the_person.change_stats(happiness = 3, slut = 1, max_slut = 60, add_to_log = False)
    if not the_person.is_pregnant():
        $ become_pregnant(the_person)
    $ quest_cuckold_employee().set_quest_flag(35)
    $ quest_cuckold_employee().quest_completed()
    $ del anon_char
    return


label quest_cuckold_employee_after_window_label():
    $ the_person = quest_cuckold_employee_get_target()
    if not the_person.is_pregnant():
        if quest_cuckold_employee().quest_event_dict.get("creampie_count", 0) >= 5:  #You creamed her at least 5 times via the event. #TODO we should probably track this via person.sex_record instead...
            $ become_pregnant(the_person)

    if the_person.is_pregnant():#Success
        $ mc.start_text_convo(the_person)
        the_person "Hey bull! I was supposed to start my period a couple of days ago, but I haven't. Just thought you might find that interesting ;)"
        "Oh boy, a missed period is a good sign! You wonder if your seed is growing inside of her..."
        the_person "I'll be able to test for sure in a couple of days! I wouldn't mind a couple more tries between now and then though... just in case my period is just late."
        mc.name "I'll make time to breed you again cow. Be prepared to receive my potent seed."
        $ mc.end_text_convo()
        $ the_person.on_room_enter_event_list = []  #We are overriding this event and doing our own announcement. No reason to use vanilla one in this situation.
        $ quest_cuckold_employee().set_quest_flag(91)
        $ mc.business.add_mandatory_crisis(quest_cuckold_employee_knocked_up)
        return

    else:
        $ mc.start_text_convo(the_person)
        the_person "Hey... just wanted to let you know I just started my period. I guess it didn't take."
        mc.name "We can try again in a few weeks."
        the_person "Hmm... yeah, maybe..."
        $ mc.end_text_convo()
        "Sounds like she might be having second thoughts..."
        $ quest_cuckold_employee().set_quest_flag(49)
        $ the_person.add_unique_on_talk_event(quest_cuckold_employee_reconsider)
    return

label quest_cuckold_employee_reconsider_label(the_person):
    "You walk up to [the_person.title]. When she sees you she frowns."
    $ the_person.draw_person(emotion = "sad")
    the_person "Hey [the_person.mc_title]... I've been meaning to talk to you..."
    mc.name "Is everything okay?"
    the_person "Yeah... Just... I've been thinking a lot about things between you and me."
    mc.name "And?"
    the_person "I was letting my hormones run away with me. Messing around was a lot of fun, but, I changed my mind. I don't want to keep trying to get pregnant."
    mc.name "I understand, and I'll do my best to respect that."
    the_person "Ah... okay... Thanks! Is there anything else I can do for you?"
    $ quest_cuckold_employee().quest_completed()
    return

label quest_cuckold_employee_knocked_up_label():
    $ the_person = quest_cuckold_employee_get_target()
    $ mc.start_text_convo(the_person)
    the_person "Hey! I need to see you in your office, ASAP!"
    mc.name "Ok, I'll be there soon."
    $ mc.end_text_convo()
    $ mc.change_location(office)
    $ ceo_office.show_background()
    $ the_person.draw_person(position = "stand4")
    $ the_person.event_triggers_dict["preg_knows"] = True
    "As you step into your office, you see [the_person.possessive_title]."
    the_person "Well [the_person.mc_title], you did it! Positive pregnancy test!"
    mc.name "Oh my god, that's amazing! Congratulations!"
    the_person "I know! I can't wait to tell my husband... It's so weird though, knowing in my head that it isn't even his?"
    menu:
        "Leave your [so_title] for me" if the_person.love + 10 > leave_SO_love_calculation(the_person):   #Hide yo wife
            mc.name "[the_person.title], think it's time you left him so we can be together. It isn't right hiding this from him.."
            "[the_person.title] seems nervous, you can tell she is dealing with some guilt after cheating on her husband."
            the_person "I know... you're right. I know you're right! This has gone on long enough. I'll... I'll tell him later today."
            # she becomes your girlfriend
            $ the_person.add_role(girlfriend_role)
            the_person "I can't believe it, I'm really doing this. You're my one and only bull now."

        "You're doing the right thing":      #Be the good guy
            mc.name "I'm really happy for you. Don't worry, your secret is safe with me. For all purposes, the baby IS his."
            the_person "Yeah... I know... It's just hard, you know?"
            "She gets a sultry tone to her voice."
            the_person "If you want to, you can still cum inside me once in a while... It was kinda hot, playing around with breeding."
            mc.name "I'm happy to be your bull whenever you need it."
    the_person "Do you think, I could just start calling you that? My bull?"
    mc.name "As long as you are my happy cow."
    $ the_person.set_mc_title("Bull")
    $ the_person.set_title("Cow")
    $ the_person.set_possessive_title("Your Personal Breeding Stock")
    "She puts her hand on your chest. She traces a few circles around it, then slower lowers her hand to your crotch. She starts to stroke the shaft."
    the_person "Mmm, it just feels so... virile..."
    the_person "Do you need a little release? I know I'm already pregnant but..."
    "You growl at her."
    mc.name "Bend over, [the_person.title]. I need a hole for my seed."
    $ the_person.change_arousal(20)
    the_person "Yes my [the_person.mc_title]!"
    $ the_person.draw_person(position = "doggy")
    "Her ass in position, you quickly get her ready."
    $ the_person.strip_outfit(position = "doggy", exclude_upper = True)
    call fuck_person(the_person, start_position = doggy, start_object = make_floor(), private = True, affair_ask_after = False, skip_intro = True, skip_condom = True) from _breed_cuckold_victory_lap_01
    $ the_report = _return
    if the_report.get("guy orgasms", 0) > 0 and the_person.has_creampie_cum():
        the_person "Sweet Jesus, no wonder you knocked me up. I'm so full of your cum, it's amazing..."
    "After you both recover, you carefully leave your office. Sounds like you have your very own breeding stock available from now on!"
    "It's going to be amazing to watch her belly swell with your seed."
    $ the_person.change_stats(obedience = 2, slut = 2, max_slut = 70)  #She is now your slutty breeding stock.
    #TODO consider giving her a collar?
    $ quest_cuckold_employee().set_quest_flag(101)
    $ the_person.personality = get_breeding_stock_personality(the_person)
    $ quest_cuckold_employee().quest_completed()
    return

init 1301 python:
    def breeding_stock_titles(the_person):
        return "Cow"
    def breeding_stock_possessive_titles(the_person):
        return "Your Breeding Stock"
    def breeding_stock_player_titles(the_person):
        return "Bull"
    def get_breeding_stock_personality(the_person): #Use a function to get this so we can keep the girls prefix so her personality doesn't change TOO much
        breeding_stock = Personality("Breeding Stock", default_prefix = the_person.personality.default_prefix,
        common_likes = [],
        common_sexy_likes = [],
        common_dislikes = [],
        common_sexy_dislikes = [],
        titles_function = breeding_stock_titles, possessive_titles_function = breeding_stock_possessive_titles, player_titles_function = breeding_stock_player_titles)
        return breeding_stock

label breeding_stock_greetings(the_person):
    $ update_ass_condition(the_person)
    if the_person.has_creampie_cum():

        the_person "Hi [the_person.mc_title]!"
        "She lowers her voice to a whisper."
        the_person "I can still feel your seed deep inside me, but if you want to go again, I'll happily take another load..."
        if the_person.knows_pregnant():
            "She rubs her belly, absent mindedly."

    else:
        the_person "Hi [the_person.mc_title]!"
        "She lowers her voice to a whisper."
        the_person "Its been a bit since you filled me up. Want to?"
        if the_person.knows_pregnant():
            "She rubs her belly, absent mindedly."
    return

label breeding_stock_anal_sex_taboo_break(the_person):
    the_person "I can't believe we're doing this... Do you think when you get ready to cum you could... you know, slip it in my pussy?"
    mc.name "Maybe, it depends on how good your ass is."
    if not the_person.knows_pregnant():
        the_person "Sure but like... how are you gonna get me pregnant if you don't put it in the right hole?"
    else:
        the_person "I know I'm already pregnant but, I just love it when you cum in my other hole, okay?"
    mc.name "I'll do my best, but no promises."
    return

label breeding_stock_sex_responses_vaginal(the_person):
    if mc.condom:
        the_person "Mmm, your cock feels good inside me, but you know what would be better? If we took off that awful condom."
        if the_person.knows_pregnant():
            the_person "I mean, I'm already pregnant! What's the harm in going bare?"
        else:
            the_person "I want to feel everything, and the warmth that goes deep when you cum inside me..."
        menu:
            "Take the condom off":
                mc.name "You're right, what was I thinking?"
                "You pull out for a second, then pull the condom off and resume fucking her."
                $ mc.condom = False
                "She gets goosebumps when you bottom out inside of her, completely bareback."
                $ the_person.change_arousal(20)
                the_person "Oh fuck! That's it!"
            "Leave it on":
                mc.name "Sorry, I think this should stay on for now."
                "She gives you a pouting face."
                the_person "You know I'm just going to keep asking, right?"

    else:
        the_person "Keep fucking me [the_person.mc_title], it feels fantastic!"

    return

label breeding_stock_cum_vagina(the_person):
    if mc.condom:
        the_person "Mmm, your cum feels so warm, but why did you waste it in that condom?"

    else:
        if the_person.on_birth_control:
            the_person "Oh fuck, it's so warm. I can feel it inside me..."
            "She sighs happily as you cum inside her."
        elif the_person.is_pregnant():
            the_person "Mmm, it's so warm... it feels so good, just like the load that knocked me up!"
        else:
            the_person "Oh my god it's sooo good. Come on little swimmers, knock me up!"
    return
