#This is an adaption of the cuckold wife side quest. Her story is getting changed over to a side character to support the elimination of the side quest system.
#Her story get's triggered by players who have shown a tendency to impregnate employees.

init -1 python: #Requirement functions
    def cuckold_employee_init_requirement():
        if mc.business.mc_offspring_count() + len(mc.business.employees_knocked_up_by_mc()) <= 2: #kids or knocked up atleast 3 employees so far
            return False
        if day < TIER_3_TIME_DELAY * 2:
            return False  # don't start too early
        if mc.business.get_employee_count() < 10:
            return False  # wait until we have a sizeable business
        if mc.business.unisex_restroom_unlocks.get("unisex_restroom_gloryhole", 0) == 0:
            return False  # disabled until glory hole unlocked

        # check if we have a married woman without kids who is slutty enough for breeding
        return not find_avail_cuckold_employee() is None

    def cuckold_employee_intro_requirement():
        if mc.is_at_work() and mc.business.is_open_for_business():
            return True
        return False

    def cuckold_employee_decision_requirement():
        if mc.is_at_work() and mc.business.is_open_for_business():
            if cuckold_employee_get() is None:
                return True #Return true so that the event clears and we clean up at the start of the label.
            elif cuckold_employee_get().days_since_event("breeding_event") >= TIER_1_TIME_DELAY:
                return True
        return False

    def cuckold_employee_rethink_decision_requirement():
        if mc.is_at_work() and mc.business.is_open_for_business():
            if cuckold_employee_get() is None:
                return True #Return true so that the event clears and we clean up at the start of the label.
            elif cuckold_employee_get().days_since_event("breeding_event") >= TIER_1_TIME_DELAY:
                return True
        return False

    def cuckold_employee_breeding_session_requirement(the_person):
        if mc.is_at_work():
            return True
        return False

    def cuckold_employee_reload_breeding_session_requirement():
        return True

    def cuckold_employee_gloryhole_requirement():
        if mc.is_at_work() and mc.business.is_open_for_business():
            if cuckold_employee_get() is None:
                return True #Return true so that the event clears and we clean up at the start of the label.
            elif cuckold_employee_get().days_since_event("breeding_event") >= TIER_1_TIME_DELAY:
                return True
        return False

    def cuckold_employee_after_window_requirement():
        if mc.is_at_work() and mc.business.is_open_for_business():
            if cuckold_employee_get() is None:
                return True #Return true so that the event clears and we clean up at the start of the label.
            elif cuckold_employee_get().days_since_event("breeding_event") >= 7:    #One week of fucking
                return True
        return False

    def cuckold_employee_reconsider_requirement(the_person):
        return False

    def cuckold_employee_knocked_up_requirement():
        if mc.is_at_work() and mc.business.is_open_for_business():
            if cuckold_employee_get() is None:
                return True #Return true so that the event clears and we clean up at the start of the label.
            elif cuckold_employee_get().days_since_event("breeding_event") >= TIER_1_TIME_DELAY:
                return True
        return False

    def cuckold_employee_fertile_return_requirement():
        if mc.is_at_work() and mc.business.is_open_for_business():
            if cuckold_employee_get() is None:
                return True #Return true so that the event clears and we clean up at the start of the label.
            elif cuckold_employee_get().is_highly_fertile():    #She has started a new fertile period
                return True
        return False


init 1 python:      #Actions
    cuckold_employee_init = Action("Initialize cuckold", cuckold_employee_init_requirement, "cuckold_employee_init_label")
    cuckold_employee_intro = Action("Cuckold Intro", cuckold_employee_intro_requirement, "cuckold_employee_intro_label")
    cuckold_employee_decision = Action("Cuckold Reveal", cuckold_employee_decision_requirement, "cuckold_employee_decision_label")
    cuckold_employee_rethink_decision = Action("Cuckold Submits", cuckold_employee_rethink_decision_requirement, "cuckold_employee_rethink_decision_label")
    cuckold_employee_breeding_session = Action("Cuckold Breeding Session", cuckold_employee_breeding_session_requirement, "cuckold_employee_breeding_session_label")
    cuckold_employee_reload_breeding_session = Action("Breeding Session reload", cuckold_employee_reload_breeding_session_requirement, "cuckold_employee_reload_breeding_session_label")
    cuckold_employee_gloryhole = Action("Cuckold at Glory Hole", cuckold_employee_gloryhole_requirement, "cuckold_employee_gloryhole_label")
    cuckold_employee_after_window = Action("Cuckold Aftermath", cuckold_employee_after_window_requirement, "cuckold_employee_after_window_label")
    cuckold_employee_reconsider = Action("Cuckold Reluctance", cuckold_employee_reconsider_requirement, "cuckold_employee_reconsider_label")
    cuckold_employee_knocked_up = Action("Cuckold Success", cuckold_employee_knocked_up_requirement, "cuckold_employee_knocked_up_label")
    cuckold_employee_fertile_return = Action("Cuckold Return", cuckold_employee_fertile_return_requirement, "cuckold_employee_fertile_return_label")

init 2 python:      #Other python functions
    def setup_cuckold_employee():
        person = find_avail_cuckold_employee()
        if person is None:
            #Probably reset this event somehow.
            return
        mc.business.event_triggers_dict["cuckold_employee_ident"] = person.identifier
        mc.business.event_triggers_dict["cuckold_employee_start"] = True
        mc.business.event_triggers_dict["cuckold_employee_finish"] = False
        person.event_triggers_dict["start_day"] = 9999
        person.event_triggers_dict["decision_day"] = 9999
        person.event_triggers_dict["fertility_day"] = 9999
        person.event_triggers_dict["creampie_count"] = 0
        person.add_opinion("creampies", 2, discovered = False, add_to_log = False)
        person.add_opinion("bareback sex", 2, discovered = False, add_to_log = False)
        person.add_opinion("vaginal sex", 2, discovered = False, add_to_log = False)
        person.on_birth_control = False
        person.change_baby_desire(1000)
        mc.business.add_mandatory_crisis(cuckold_employee_intro)
        side_character_set_unavail(person)
        return

    def find_avail_cuckold_employee():
        able_person_list = []
        for person in [x for x in mc.business.get_employee_list() if x.sluttiness >= 50 and x.kids == 0 \
            and x.relationship == "Married" and not x.is_pregnant() \
            and not side_character_is_unavail(x)]:
                able_person_list.append(person)
        return get_random_from_list(able_person_list)

    def cuckold_employee_get():
        person = get_person_by_identifier(mc.business.event_triggers_dict.get("cuckold_employee_ident", None))
        if person is None:
            return None
        if not person.is_employee():
            return None
        return person

    def cuckold_employee_finished():
        return mc.business.event_triggers_dict.get("cuckold_employee_finish",False)

label cuckold_employee_init_label(): #Use this function to set quest specific variables.
    $ setup_cuckold_employee()  #This call needs to figure out which employee and then set up the first event
    return

label cuckold_employee_intro_label():
    $ the_person = cuckold_employee_get()    #Find a way to get the target.
    if the_person is None or not the_person.is_employee():
        #ABORT ABORT, we fucked up somewhere.
        #Loop back to init?
        call cuckold_employee_init_label() from _starbuck_sucks_at_programming_01   #If we can't find the person, run init again to reset the whole thing.
        return

    "You're working diligently when a figure appears in your peripheral vision. You look up and see [the_person.title] standing in front of you."
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
    $ the_person.set_event_day("breeding_event")
    $ mc.business.add_mandatory_crisis(cuckold_employee_decision)
    return

label cuckold_employee_decision_label():
    $ the_person = cuckold_employee_get()
    if the_person is None:
        #ABORT ABORT, we fucked up somewhere.
        # $ cuckold_employee().quest_completed()
        return
    $ the_person.set_event_day("breeding_event")
    $ the_person.draw_person()
    $ the_person.tag_sex_record("Vaginal Creampies")
    "You are lost in your work when a feminine voice clearing her throat nearby catches your attention. You look up and see [the_person.title] standing in front of you again."
    mc.name "Hello [the_person.title]. Can I help you?"
    the_person "Well, kind of yes, kind of no."
    mc.name "I'm sorry?"
    the_person "I just... I need to vent to someone about something, but I don't trust the other girls around here not to gossip about it."
    mc.name "Of course, you can talk to me about anything."
    the_person "Well... my husband and I... we've been trying to have a baby lately, but after months of trying, still nothing."
    the_person "I did something I probably shouldn't have... I took a semen sample when we had sex a few days ago secretly and had it analyzed."
    the_person "He is basically infertile. I'm absolutely crushed! I love him so much, but I also want to have a baby so bad."
    mc.name "I understand. It might take a while for you to grieve about this if you need some time off."
    the_person "No, no, that's not it. I keep thinking, maybe there is some way, you know? Maybe a miracle will happen, or some drug or something will be invented that can help."
    the_person "I can't leave him, but my body is screaming at me. The urge to make a baby is SO strong!"
    mc.name "Have you considered something like a sperm bank?"
    the_person "No... I'd have to tell him that he is infertile. It would crush him! I'm not sure our relationship would survive that."
    "Hmmm... well... there is always another way of getting pregnant... You wonder if she has considered it at all."
    "You could always offer to knock her up. But then again, impregnating another man's wife could lead you to some heavy drama down the road..."
    menu:
        "Offer to help":
            mc.name "You know, [the_person.title]... there may be a solution that would allow you to have a baby AND stay with your husband."
            $ the_person.draw_person(emotion = "happy")
            the_person "Oh? What would that be?"
            mc.name "Well, if you want a baby that bad, you could always have someone else do the deed..."
            the_person "Oh... OH... Oh my..."
            "She stumbles for words for a moment."
            the_person "That's... wow... I don't know, that is an awfully big step."
            the_person "I don't even know anyone. How could I even find a man that would do that?"
            if mc.charisma > 4: #Charisma check
                mc.name "I know how much this means to you. I know I'm your boss, but I'm also your friend, and I want to see you happy."
                mc.name "I would be glad to help you out if you decided that was a step you would like to take."
                the_person "Oh my! That's crazy. I never would have thought to do something like that. I don't know, that sounds pretty nuts..."
                mc.name "The urges your body are giving you are completely natural. They are only going to get stronger over time, until they drive a wedge between you and your husband."
                the_person "Oh god... you're right. I know you are. I don't want to admit it, but deep down inside, I know you are right."
                "She bites her lip for a moment and looks down at the floor."
                $ the_person.ideal_fertile_day = (day % 30) + 2  #Peak fertility is in 2 days.
                $ the_person.event_triggers_dict["fertility_day"] = day + 2
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
                "She changes her voice to imitate a more masculine one."
                the_person "Oh honey! The baby is so cute... but he looks just like your boss???"
                "She shakes her head."
                the_person "I appreciate the thought, you've definitely given me something to think about, but I'm not sure that is a good idea."
                mc.name "Okay, well if you change your mind, let me know."
                the_person "Yeah... right... fucking my boss... bareback... totally not a good idea..."
                $ the_person.draw_person(position = "walking_away")
                "As [the_person.title] turns and walks away, you can almost see the wheels turning in her head."
                "Her initial reaction was not great, but you wonder if she will think about it more. Maybe you should try talking to her again in a few days?"
                $ mc.business.add_mandatory_crisis(cuckold_employee_rethink_decision)
                $ mc.business.add_mandatory_crisis(cuckold_employee_after_window)
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
            "You weigh the decision carefully."
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
                    $ the_person.event_triggers_dict["fertility_day"] = day + 2
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
                        $ mc.business.add_mandatory_crisis(cuckold_employee_gloryhole)
                    return
    # only get here if we are gonna breed in the office.
    "[the_person.possessive_title] follows you to your office."
    $ mc.change_location(ceo_office)
    "After you walk in, you close the door and lock it."
    the_person "Let's do this. I'm ready. I'm ready to get bred!"
    $ the_person.draw_person(position = "kissing")
    "You wrap your arms around [the_person.title]. She embraces you, and you start to kiss. Your hands go down to her ass."
    $ the_person.change_arousal(5)
    the_person "Okay, so... the best way to do this that I've read anyway, is a good old-fashioned missionary."
    mc.name "Get ready and lay down on my desk. I always wanted my own personal breeding stock."
    the_person "Oh my god, I can't believe I'm doing this. I have a bull now, oh god!"
    "[the_person.possessive_title] gets on your desk and lays on her back."
    $ the_person.draw_person(position = "missionary")
    if the_person.vagina_visible():
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
        $ mc.change_location(lobby)
        "Your sperm might already be racing to her egg, ready to fertilize it, but it also might not be. To be certain, you should breed her as often as you can over the next few days."
        $ the_person.event_triggers_dict["creampie_count"] = the_person.event_triggers_dict.get("creampie_count", 0) + 1
        $ the_person.add_unique_on_talk_event(cuckold_employee_breeding_session)
        $ mc.business.add_mandatory_crisis(cuckold_employee_after_window)
        $ the_person.apply_planned_outfit() # make sure she is dressed again after event
    elif the_report.get("guy orgasms", 0) == 0:
        "[the_person.title] is silent for a few moments in frustration."
        the_person "You... you didn't even finish."
        the_person "Don't you like breeding me?"
        if mc.energy < 30:
            mc.name "I'm really sorry, but I'm just too tired at the moment, we can try again tomorrow."
            $ the_person.change_stats(happiness = -10, obedience = -10, love = -10)
            the_person "Alright, for just this once, I will believe you, but you better clean up your act."
            $ the_person.apply_planned_outfit()
            $ the_person.draw_person(position = "walking_away")
            "[the_person.title] stands up, throws on her clothes and storms out of your office."
            $ the_person.add_unique_on_talk_event(cuckold_employee_breeding_session)
            $ mc.business.add_mandatory_crisis(cuckold_employee_after_window)
        else:
            mc.name "I'm sorry, I want to help you, but it's been a long day and I'm just worn out..."
            the_person "Fuck you! I see right through that charade. You just wanted to fuck a married woman!"
            $ the_person.apply_planned_outfit()
            $ the_person.draw_person(position = "walking_away")
            "[the_person.title] stands up, throws on her clothes and storms out of your office. Unfortunately, you may have damaged your relationship with her irreparably."
    else:
        "[the_person.title] is completely silent."
        the_person "You... you didn't even finish inside of me?"
        $ the_person.change_stats(happiness = -20, obedience = -30, love = -30)
        the_person "You... you just wanted to fuck me, didn't you!?!"
        mc.name "I'm sorry, I want to help you, but it's been a long day and I'm just worn out..."
        the_person "Fuck you! I see right through that charade. You just wanted to fuck a married woman!"
        $ the_person.apply_planned_outfit()
        $ the_person.draw_person(position = "walking_away")
        "[the_person.title] stands up, throws on her clothes and storms out of your office. Unfortunately, you may have damaged your relationship with her irreparably."
    return

label cuckold_employee_rethink_decision_label():
    $ the_person = cuckold_employee_get()
    if the_person is None:
        #ABORT ABORT, we fucked up somewhere.
        return
    $ the_person.ideal_fertile_day = (day % 30) + 2  #Peak fertility is in 2 days.
    $ the_person.set_event_day("breeding_event")
    $ the_person.event_triggers_dict["fertility_day"] = day + 2
    "You are lost in paperwork when a figure enters your peripheral vision. You look up and see [the_person.title] standing in front of you."
    $ the_person.draw_person()
    mc.name "Hello [the_person.title]. Can I help you?"
    the_person "I think so... can we talk in private?"
    mc.name "Certainly, let's go to my office."
    "[the_person.possessive_title] follows you to your office."
    $ mc.change_location(ceo_office)
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
    the_person "My bull? Oh god... Yes! I want to get bred like a wild animal!"
    mc.name "Get ready and lay down on my desk. I always wanted my own personal breeding stock."
    the_person "Oh my god, I can't believe I'm doing this. I have a bull now, oh god!"
    "[the_person.possessive_title] gets on your desk and lays on her back."
    $ the_person.draw_person(position = "missionary")
    if the_person.vagina_visible():
        "She spreads her legs, her pussy on display in front of you."
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
        $ mc.change_location(lobby)
        "Your sperm might already be racing to her egg, ready to fertilize it, but it also might not be. To be certain, you should breed her as often as you can over the next few days."
        $ the_person.event_triggers_dict["creampie_count"] = the_person.event_triggers_dict.get("creampie_count", 0) + 1
        $ the_person.add_unique_on_talk_event(cuckold_employee_breeding_session)
        $ mc.business.add_mandatory_crisis(cuckold_employee_after_window)
        $ the_person.apply_planned_outfit() # make sure she is dressed again after event
    elif the_report.get("guy orgasms", 0) == 0:
        "[the_person.title] is completely silent."
        the_person "You... you didn't even finish."
        the_person "Don't you like breeding me?"
        if mc.energy < 30:
            mc.name "I'm really sorry, but I'm just too tired at the moment, we can try again tomorrow."
            $ the_person.change_stats(happiness = -10, obedience = -10, love = -10)
            the_person "Alright, for just this once, I will believe you, but you better clean up your act."
            $ the_person.apply_planned_outfit()
            $ the_person.draw_person(position = "walking_away")
            "[the_person.title] stands up, throws on her clothes and storms out of your office."
            $ the_person.add_unique_on_talk_event(cuckold_employee_breeding_session)
            $ mc.business.add_mandatory_crisis(cuckold_employee_after_window)
        else:
            mc.name "I'm sorry, I want to help you, but it's been a long day and I'm just worn out..."
            the_person "Fuck you! I see right through that charade. You just wanted to fuck a married woman!"
            $ the_person.apply_planned_outfit()
            $ the_person.draw_person(position = "walking_away")
            "[the_person.title] stands up, throws on her clothes and storms out of your office. Unfortunately, you may have damaged your relationship with her irreparably."
    else:
        "[the_person.title] is completely silent."
        the_person "You... you didn't even finish inside of me?"
        $ the_person.change_stats(happiness = -20, obedience = -30, love = -30)
        the_person "You... you just wanted to fuck me, didn't you!?!"
        mc.name "I'm sorry, I want to help you, but it's been a long day and I'm just worn out..."
        the_person "Fuck you! I see right through that charade. You just wanted to fuck a married woman!"
        $ the_person.apply_planned_outfit()
        $ the_person.draw_person(position = "walking_away")
        "[the_person.title] stands up, throws on her clothes and storms out of your office. Unfortunately, you may have damaged your relationship with her irreparably."
    return

label cuckold_employee_breeding_session_label(the_person):
    $ mc.business.add_mandatory_crisis(cuckold_employee_reload_breeding_session)
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
            call talk_person(the_person) from _call_talk_person_cuckold_employee_breeding_session
            return
    mc.name "Yes that is exactly right. I really need help with something in my office, could you please come give me a hand?"
    the_person "Of course! Let's go!"
    "[the_person.possessive_title] follows you to your office."
    $ mc.change_location(ceo_office)
    "After you walk in, you close the door and lock it."
    $ mc.change_arousal(5)
    $ the_person.change_arousal(5)
    the_person "I've been looking forward to this. I know that we're doing this for practical reasons, but that doesn't mean it doesn't feel really good..."
    mc.name "Get ready, cow. I'm just here to breed you."
    the_person "Oh god, it's so hot when you talk to me like that."
    "[the_person.possessive_title] gets on your desk and lays on her back."
    $ the_person.draw_person(position = "missionary")
    if the_person.vagina_visible():
        $ mc.change_arousal(5)
        $ the_person.change_arousal(5)
        "She spreads her legs, her pussy on display in front of you."
    else:
        $ generalised_strip_description(the_person, the_person.outfit.get_vagina_strip_list(), position = "missionary")
    $ mc.change_arousal(10)
    mc.name "I'm gonna fuck you on my desk again. Tell your bull how much you want it."
    $ mc.change_arousal(15)
    $ the_person.change_arousal(20)
    the_person "Oh god please! I want you to fuck me over and over until my belly is popping with your seed!"
    call fuck_person(the_person, start_position = breeding_missionary, start_object = make_desk(), private= True, position_locked = True, skip_intro = True, affair_ask_after = False, skip_condom = True) from _breed_cuckold_attempt_2
    $ the_report = _return
    if the_report.get("guy orgasms", 0) > 0 and the_person.has_creampie_cum():
        the_person "Oh god, every fertile load feels even better than the last..."
        $ the_person.change_stats(happiness = 1, obedience = 1, love = 1, max_love = 80, add_to_log = False)
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
            the_person "In this case, a hard, throbbing, amazing end..."
        the_person "I'm going to lay here for a while again."
        mc.name "Okay. I'll lock the door behind me when I leave."
        the_person "Thank you [the_person.mc_title]. Let's keep our fingers crossed!"
        "With that, you leave your office, being careful to lock the door behind you."
        $ clear_scene()
        $ mc.change_location(lobby)
        # only show message twice (first time and when you reached the requirement count)
        if the_person.event_triggers_dict.get("creampie_count", 0) < 5:
            "Your sperm might already be racing to her egg, ready to fertilize it, but it also might not be. To be certain, you should breed her as often as you can over the next few days."
        elif the_person.event_triggers_dict.get("creampie_count", 0) >= 5:
            "You've cum inside [the_person.possessive_title] now so many times the last few days, if she really is fertile, there almost no way you haven't knocked her up."
        $ the_person.event_triggers_dict["creampie_count"] = the_person.event_triggers_dict.get("creampie_count", 0) + 1
    else:
        mc.name "Sorry, I'm just too tired, I shouldn't have tried this right now..."
        the_person "It's okay... You've been pushing yourself pretty hard."
        the_person "Besides, I'm probably already pregnant. This is just making certain of it!"
        "You both get up and leave your office, resuming your day."
    $ the_person.add_unique_on_talk_event(cuckold_employee_breeding_session)
    $ the_person.apply_planned_outfit() # make sure she is dressed when back at workstation
    call advance_time from cuckold_advance_time
    return

label cuckold_employee_reload_breeding_session_label():
    $ the_person = cuckold_employee_get()
    if the_person is None:
        #ABORT ABORT, we fucked up somewhere.
        return
    $ the_person.add_unique_on_talk_event(cuckold_employee_breeding_session)
    return


label cuckold_employee_gloryhole_label():
    $ the_person = cuckold_employee_get()
    if the_person is None:
        #ABORT ABORT, we fucked up somewhere.
        return
    $ anon_char = get_anon_person(the_person)
    if mc.business.unisex_restroom_unlocks.get("unisex_restroom_gloryhole", 0) == 1:
        pass
    else:
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
            return
    "As you are waiting, you hear someone enter the restroom and walk into the stall next to yours."
    "This is crazy. It could be anybody in there! You hear on the other side the toilet flush as the person finishes relieving herself. You take a deep breath, then go for it."
    "You give yourself a couple of strokes to make sure you are good and hard, then stick your cock through the glory hole."

    anon_char "Oh my god... it's really happening..."

    "Sounds like your bathroom stall neighbor is interested in what she sees!"

    if the_person.has_taboo("touching_penis"):
        $ the_person.break_taboo("touching_penis", add_to_log = False)

    "You feel a soft hand grasp your member and give it a couple of strokes. You hear movement coming from the stall next to you but you aren't sure what they are doing."

    if the_person.has_taboo(["condomless_sex", "vaginal_sex"]):
        $ the_person.break_taboo("condomless_sex", add_to_log = False)
        $ the_person.break_taboo("vaginal_sex", add_to_log = False)

    "You feel her hand hold you rigidly in place as you begin to slowly feel a hot, wet sleeve enveloping your cock."
    "It feels like she is taking you in her pussy! You let out a moan of appreciation."

    anon_char "Mmmm, it's so good when it goes in."
    "You press yourself against the wall to try and push yourself as deep as you can. You are almost balls deep, but the thin wall is in the way."
    "You start to work your hips a bit, testing the limits of how far you can pull back without pulling all the way out of her."
    anon_char "Yes! Mmm, that feels good."
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
        "Pull Out\n{color=#ff0000}{size=18}Too horny{/size}{/color} (disabled)":
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
    $ del anon_char
    return

label cuckold_employee_after_window_label():
    $ the_person = cuckold_employee_get()
    if the_person is None:
        #ABORT ABORT, we fucked up somewhere.
        return
    $ the_person.set_event_day("breeding_event")
    if not the_person.is_pregnant():
        if the_person.comp_sex_record("Vaginal Creampies") >= 5:  #You creamed her at least 5 times via the event. #TODO we should probably track this via person.sex_record instead...
            $ become_pregnant(the_person)

    if the_person.is_pregnant():#Success
        $ mc.start_text_convo(the_person)
        the_person "Hey bull! I was supposed to start my period a couple of days ago, but I haven't. Just thought you might find that interesting ;)"
        "Oh boy, a missed period is a good sign! You wonder if your seed is growing inside of her..."
        the_person "I'll be able to test for sure in a couple of days! I wouldn't mind a couple more tries between now and then though... just in case my period is just late."
        mc.name "I'll make time to breed you again cow. Be prepared to receive my potent seed."
        $ mc.end_text_convo()
        $ mc.business.add_mandatory_crisis(cuckold_employee_knocked_up)
        return

    else:
        $ mc.start_text_convo(the_person)
        the_person "Hey... just wanted to let you know I just started my period. I guess it didn't take."
        mc.name "We can try again in a few weeks."
        the_person "Hmm... yeah, maybe..."
        $ mc.end_text_convo()
        "Sounds like she might be having second thoughts..."
        $ the_person.add_unique_on_talk_event(cuckold_employee_reconsider)
        $ the_person.remove_on_talk_event(cuckold_employee_breeding_session)
    return

label cuckold_employee_reconsider_label(the_person):
    $ the_person.set_event_day("breeding_event")
    "You walk up to [the_person.title]. When she sees you she frowns."
    $ the_person.draw_person(emotion = "sad")
    the_person "Hey [the_person.mc_title]... I've been meaning to talk to you..."
    mc.name "Is everything okay?"
    the_person "Yeah... Just... I've been thinking a lot about things between you and me."
    mc.name "And?"
    the_person "I was letting my hormones run away with me. Messing around was a lot of fun, but, I changed my mind. I don't want to keep trying to get pregnant."
    mc.name "I understand, and I'll do my best to respect that."
    the_person "Ah... okay... Thanks! Is there anything else I can do for you?"
    $ mc.business.add_mandatory_crisis(cuckold_employee_fertile_return)
    return

label cuckold_employee_knocked_up_label():
    $ the_person = cuckold_employee_get()
    if the_person is None:
        #ABORT ABORT, we fucked up somewhere.
        return
    $ the_person.remove_on_talk_event(cuckold_employee_breeding_session)
    $ mc.start_text_convo(the_person)
    $ mc.business.event_triggers_dict["cuckold_employee_finish"] = False
    the_person "Hey! I need to see you in your office, ASAP!"
    mc.name "Ok, I'll be there soon."
    $ mc.end_text_convo()
    $ mc.change_location(ceo_office)
    $ the_person.draw_person(position = "stand4")
    $ the_person.event_triggers_dict["preg_knows"] = True
    "As you step into your office, you see [the_person.possessive_title]."
    the_person "Well [the_person.mc_title], you did it! Positive pregnancy test!"
    mc.name "Oh my god, that's amazing! Congratulations!"
    the_person "I know! I can't wait to tell my husband... It's so weird though, knowing in my head that it isn't even his?"
    menu:
        "Leave your [so_title] for me" if the_person.love + 10 > leave_SO_love_calculation(the_person):   #Hide yo wife
            mc.name "[the_person.title], I think it's time you left him so we can be together. It isn't right hiding this from him.."
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
    $ the_person.strip_to_vagina(position = "doggy", prefer_half_off = True, visible_enough = True)
    call fuck_person(the_person, start_position = doggy, start_object = make_floor(), private = True, affair_ask_after = False, skip_intro = True, skip_condom = True) from _breed_cuckold_victory_lap_01
    $ the_report = _return
    if the_report.get("guy orgasms", 0) > 0 and the_person.has_creampie_cum():
        the_person "Sweet Jesus, no wonder you knocked me up. I'm so full of your cum, it's amazing..."
    "After you both recover, you carefully leave your office. Sounds like you have your very own breeding stock available from now on!"
    "It's going to be amazing to watch her belly swell with your seed."
    $ the_person.change_stats(obedience = 2, slut = 2, max_slut = 70)  #She is now your slutty breeding stock.
    #TODO consider giving her a collar?
    $ the_person.personality = get_breeding_stock_personality(the_person)
    return

label cuckold_employee_fertile_return_label():
    #In this label, we repeat the previous pattern, to give MC a chance to knock her up.
    $ the_person = cuckold_employee_get()
    if the_person is None:
        #ABORT ABORT, we fucked up somewhere.
        # $ cuckold_employee().quest_completed()
        return
    $ the_person.set_event_day("breeding_event")
    $ the_person.tag_sex_record("Vaginal Creampies")
    "You are lost in paperwork when a figure enters your peripheral vision. You look up and see [the_person.title] standing in front of you."
    $ the_person.draw_person()
    mc.name "Hello [the_person.title]. Can I help you?"
    the_person "Errr... yes..."
    the_person "So like... do you remember how last month you tried to knock me up, but it didn't work out, and then I said I didn't want to do that anymore..."
    mc.name "I do, yes."
    the_person "I... like... before I say this... I just want to say, hormones are powerful things."
    mc.name "I'm aware."
    the_person "Ha, yeah, I'm sure you are..."
    "......"
    mc.name "Is this going somewhere?"
    the_person "Oh! Ummm. Yes. Okay, I'm just gonna spit it out."
    the_person "It is coming up on my fertile time again... and I changed my mind... again..."
    mc.name "So... you DO want me to knock you up now?"
    the_person "I mean, it doesn't have to be like... right this second!"
    the_person "I'm going to get to work. Just... come find me if you are still willing to try... okay?"
    mc.name "Alright."
    $ the_person.draw_person(position = "walking_away")
    "Interesting. So [the_person.title] is fertile again, and she wants you to take another shot at knocking her up!"
    "You should talk to her if you want to try."
    $ the_person.add_unique_on_talk_event(cuckold_employee_breeding_session)
    return

init 1400 python:
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

label breeding_stock_sex_accept(the_person, the_position):
    if the_position.skill_tag == "Foreplay":
        the_person "Mmmm, let me get you ready for another breeding session."
    elif the_position.skill_tag == "Oral":
        if "getting head" in the_position.opinion_tags:
            the_person "Oh yes, let's get my pussy ready for your baby machine."
        else:
            the_person "Let me make your cock nice and slick so you can cum deep inside me."
    else:
        the_person "OH yes, my sweet bull, come and fill up your slutty cow."
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
