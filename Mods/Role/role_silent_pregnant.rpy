# Contains all of the information related to characters being pregnant.
init 1 python:
    def test_silent_pregnancy(person, progress_days):
        silent_become_pregnant(person, progress_days)
        return

init -1 python:
    silent_pregnant_role = Role("Pregnant", [], hidden = True)
    def silent_pregnant_announce_requirement(person, start_day):
        if day >= start_day:
            return True

    def silent_pregnant_transform_requirement(person):
        if day >= person.event_triggers_dict.get("preg_transform_day", 0):
            return True
        return False

    def silent_pregnant_tits_requirement(person):
        if day >= person.event_triggers_dict.get("preg_tits_date", 0):
            return True

        return False

    def silent_pregnant_tits_announcement_requirement(person):
        return True

    def silent_become_pregnant(person, progress_days = 0): # Called when a girl is knocked up. progress days is how far she is already when this gets called.
        person.event_triggers_dict["preg_accident"] = person.on_birth_control # If a girl is on birth control the pregnancy is an accident.
        person.event_triggers_dict["preg_start_date"] = day - progress_days
        person.event_triggers_dict["preg_tits_date"] = (day - progress_days) + 14 + renpy.random.randint(0,5)
        person.event_triggers_dict["preg_transform_day"] = ((day + 30) - progress_days) + renpy.random.randint(0,10)
        person.event_triggers_dict["preg_finish_announce_day"] = ((day + 90) - progress_days) + renpy.random.randint(0,10)
        person.event_triggers_dict["pre_preg_tits"] = person.tits


        #Add actions based on whether or not we are already passed that date. If so, run applicable transformations.
        if day > person.event_triggers_dict.get("preg_start_date", 0) + 15:
            person.event_triggers_dict["preg_knows"] = True
        else:
            silent_preg_announce_action = Action("Pregnancy Announcement", silent_pregnant_announce_requirement, "silent_pregnant_announce", requirement_args = day + renpy.random.randint(12,18))
            person.on_room_enter_event_list.append(silent_preg_announce_action)

        if day > person.event_triggers_dict.get("preg_tits_date", 0):
            person.event_triggers_dict["preg_knows"] = True
            person.tits = get_larger_tits(person.tits) #Her tits start to swell.
            person.personal_region_modifiers["breasts"] = person.personal_region_modifiers["breasts"] + 0.1
        else:
            silent_preg_tits_action = Action("Pregnancy Tits Grow", silent_pregnant_tits_requirement, "silent_pregnant_tits_start")
            person.on_room_enter_event_list.append(silent_preg_tits_action)

        if day > person.event_triggers_dict.get("preg_transform_day", 0):
            person.event_triggers_dict["pre_preg_body"] = person.body_type
            person.body_type = "standard_preg_body"
            person.tits = get_larger_tits(person.tits) # Her tits get even larger
            person.personal_region_modifiers["breasts"] = person.personal_region_modifiers["breasts"] + 0.1 #As her tits get larger they also become softer, unlike large fake tits. (Although even huge fake tits get softer)
            person.lactation_sources += 1

            silent_preg_finish_announce_action = Action("Pregnancy Finish Announcement", silent_preg_finish_announcement_requirement, "silent_pregnant_finish_announce", args = person, requirement_args = person)
            mc.business.mandatory_crises_list.append(silent_preg_finish_announce_action)
        else:
            silent_preg_transform_action = Action("Pregnancy Transform", silent_pregnant_transform_requirement, "silent_pregnant_transform", args = person, requirement_args = person)
            mc.business.mandatory_morning_crises_list.append(silent_preg_transform_action)

        person.add_role(silent_pregnant_role)

    def silent_preg_transform_announce_requirement(person):
        return True

    def silent_preg_finish_announcement_requirement(person):
        if person == None:
            return True
        if day >= person.event_triggers_dict.get("preg_finish_announce_day", 0):
            return True
        return False

    def silent_preg_finish_requirement(person, trigger_day):
        if day >= trigger_day:
            return True
        return False

    def silent_tit_shrink_requirement(person, trigger_day):
        if day >= trigger_day:
            return True
        return False


label silent_pregnant_announce(the_person):
    #In silent pregnancy, she just knows she's pregnant, but doesn't necessarily announce it.
    $ the_person.event_triggers_dict["preg_knows"] = True #Set here and in the larger tits, represents the person knowing they're pregnant so they don't ask for condoms ect.
    #"DEBUG [the_person.title] now knows she is pregnant."
    return

init 2 python:
    def silent_pregnant_tits_start_person(person):
        person.event_triggers_dict["preg_knows"] = True
        person.tits = get_larger_tits(person.tits) #Her tits start to swell.
        person.personal_region_modifiers["breasts"] = person.personal_region_modifiers["breasts"] + 0.1 #As her tits get larger they also become softer, unlike large fake tits. (Although even huge fake tits get softer)

        silent_pregnant_tits_announce_action = Action("Announce Pregnant Tits", silent_pregnant_tits_announcement_requirement, "silent_pregnant_tits_announce", args = day)
        person.on_talk_event_list.append(silent_pregnant_tits_announce_action)
        return

label silent_pregnant_tits_start(the_person):
    $ silent_pregnant_tits_start_person(the_person)
    #"DEBUG [the_person.title] grows larger tits."
    return

label silent_pregnant_tits_announce(start_day, the_person):
    "As you being to talk to [the_person.title], you can't help but notice her tits seem... a little larger than your remember?"
    "The way the bounce is enticing also. There is this glow that surrounds her in general. You wonder what is going on?"
    call talk_person(the_person) from _call_talk_person_silent_11
    return

init 2 python:
    def silent_pregnant_transform_person(person):
        person.event_triggers_dict["pre_preg_body"] = person.body_type
        person.body_type = "standard_preg_body"
        person.tits = get_larger_tits(person.tits) # Her tits get even larger
        person.personal_region_modifiers["breasts"] = person.personal_region_modifiers["breasts"] + 0.1 #As her tits get larger they also become softer, unlike large fake tits. (Although even huge fake tits get softer)
        person.lactation_sources += 1

        silent_preg_transform_announce_action = Action("Pregnancy Transform Announcement", silent_preg_transform_announce_requirement, "silent_pregnant_transform_announce", args = day)
        person.on_room_enter_event_list.append(silent_preg_transform_announce_action)

        silent_preg_finish_announce_action = Action("Pregnancy Finish Announcement", silent_preg_finish_announcement_requirement, "silent_pregnant_finish_announce", args = person, requirement_args = person)
        mc.business.mandatory_crises_list.append(silent_preg_finish_announce_action)
        return

label silent_pregnant_transform(the_person): #Changes the person to their pregnant body and stores what their pre-pregnancy body and tits were
    $ silent_pregnant_transform_person(the_person)
    return

label silent_pregnant_transform_announce(start_day, the_person):
    $ the_person.draw_person()
    "[the_person.possessive_title] notices you and comes over to talk."
    the_person.char "Hey [the_person.mc_title]. So, it's probably pretty obvious at this point..."
    "She turns and runs a hand over her belly, accentuating the new and prominent curves that have formed there."
    the_person.char "...but, I'm pregnant!"
    mc.name "Congratulations! You look fantastic. You really are glowing."
    $ the_person.change_happiness(10)
    if the_person.has_role(employee_role):
        the_person.char "Thank you! So obviously, when the baby comes, I'll need some time off work..."
        mc.name "Just let me know when the time comes, if you can. We'll make due without you while you are off."
    the_person.char "Thank you!"
    return

init 2 python:
    def silent_pregnant_finish_announce_person(person):
        if person == None:  #This person is no longer in the game
            #"DEBUG silent pregnant girl no longer in game."
            return
        person.event_triggers_dict["preg_old_schedule"] = person.schedule.copy() #Take a shallow copy so we can change their current schedule to nothing
        person.set_schedule([0,1,2,3,4], person.home)

        silent_preg_finish_action = Action("Pregnancy Finish", silent_preg_finish_requirement, "silent_pregnant_finish", args = person, requirement_args = [person, renpy.random.randint(4,7)])
        mc.business.mandatory_morning_crises_list.append(silent_preg_finish_action)
        return

label silent_pregnant_finish_announce(the_person): #TODO: have more variants for girlfriend_role, affair_role, etc.
    if the_person == None or the_person.title == None or the_person.title == "None":  #This person is no longer in the game
        #"DEBUG silent pregnant girl no longer in game."
        return
    # The girl tells you she'll need a few days to have the kid and recover, and she'll be back in a few days.
    "You get a call from [the_person.possessive_title]. You answer it."
    mc.name "Hey [the_person.title], what's up?"

    if the_person.has_role(employee_role):
        the_person.char "Hi [the_person.mc_title]. I wanted to let you to know that I won't be at work for a few days."
    else:
        the_person.char "Hi [the_person.mc_title], I have some exciting news."

    the_person.char "I saw my doctor yesterday and he tells me I'm going to pop any day now."

    if day - the_person.event_triggers_dict.get("preg_start_date", day) <= 90: #It's unusually short
        the_person.char "It's earlier than I expected, but he tells me everything looks like it's perfectly normal."

    mc.name "That's amazing news. Do you need me to do anything?"
    the_person.char "No, I just wanted to let you know. Thanks for everything!"
    mc.name "Okay, I'll talk to you soon then."
    the_person.char "I'll let you know as soon as things are finished. Bye!"
    $ silent_pregnant_finish_announce_person(the_person)
    return

init 2 python:
    def silent_pregnant_finish_person(person):
        person.body_type = person.event_triggers_dict.get("pre_preg_body", "standard_body")
        person.schedule = person.event_triggers_dict.get("preg_old_schedule")

        person.remove_role(pregnant_role) #Should this be triggered some time after instead of being instant?
        person.kids += 1

        tit_shrink_one_day = day + renpy.random.randint(7,14)
        silent_tit_shrink_one = Action("Tits Shrink One", tit_shrink_requirement, "silent_tits_shrink", args = [person, True], requirement_args = [person, tit_shrink_one_day])
        silent_tit_shrink_one_announcement_action = Action("Tits Shrink One Announcement", silent_tit_shrink_requirement, "silent_tits_shrink_announcement_one", args = tit_shrink_one_day, requirement_args = tit_shrink_one_day)

        tit_shrink_two_day = day + renpy.random.randint(21,35)
        silent_tit_shrink_two = Action("Tits Shrink Two", silent_tit_shrink_requirement, "silent_tits_shrink", args = [person, False], requirement_args = [person, tit_shrink_two_day])
        silent_tit_shrink_two_announcement_action = Action("Tits Shrink Two Announcement", silent_tit_shrink_requirement, "silent_tits_shrink_announcement_two", args = tit_shrink_two_day, requirement_args = tit_shrink_two_day)

        mc.business.mandatory_morning_crises_list.append(silent_tit_shrink_one) #Events for her breasts to return to their normal size.
        mc.business.mandatory_morning_crises_list.append(silent_tit_shrink_two)

        person.on_talk_event_list.append(silent_tit_shrink_one_announcement_action) #And here is where she tells you about those changes
        person.on_talk_event_list.append(silent_tit_shrink_two_announcement_action)

        if person.has_role(silent_pregnant_role):
            person.remove(silent_pregnant_role)
        return

label silent_pregnant_finish(the_person):
    $ silent_pregnant_finish_person(the_person)

    "You get a call from [the_person.possessive_title] early in the morning. You answer it."
    the_person.char "Hey [the_person.mc_title], good news! Two days ago I had a beautiful, healthy baby girl! I'll be coming back to work today." #Obviously they're all girls for extra fun in 18 years.
    #TODO: Let you pick a name (or at low obedience she's already picked one)
    mc.name "That's amazing, but are you sure you don't need more rest?"
    the_person.char "I'll be fine. I'm leaving her with my mother for a little while so I can get back to a normal life."
    the_person.char "I just wanted to let you know. I'll talk to you soon."
    "You say goodbye and [the_person.title] hangs up."
    return


label silent_tits_shrink(the_person, reduce_lactation):
    #"DEBUG [the_person.title] tits are slightly smaller."
    python:

        the_person.lactation_sources -= 1
        the_person.tits = get_smaller_tits(the_person.tits)
        the_person.personal_region_modifiers["breasts"] = the_person.personal_region_modifiers["breasts"] - 0.1
    return

label silent_tits_shrink_announcement_one(day_shrunk, the_person):
    #"DEBUG [the_person.title] has slightly smaller tits."
    call talk_person(the_person) from _call_talk_person_silent_12
    return

label silent_tits_shrink_announcement_two(day_shrunk, the_person):
    "As you start to talk to [the_person.title], you notice her tits have gotten smaller."
    "They must be returning to their pre-pregnancy state."
    call talk_person(the_person) from _call_talk_person_silent_13
    return
