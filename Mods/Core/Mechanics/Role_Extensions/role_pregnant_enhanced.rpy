init 3 python:
    def validate_pregnancy_crisis_events():
        for crisis in (mc.business.mandatory_crises_list + mc.business.mandatory_morning_crises_list):
            if "Pregnancy" in crisis.name:
                argument_info = ""
                for arg in crisis.args:
                    if len(argument_info) > 0:
                        argument_info += ", "
                    if isinstance(arg, Person):
                        argument_info += "Person: " + arg.name + " " + arg.last_name
                    elif isinstance(arg, SerumDesign):
                        argument_info += "Serum: " + arg.name
                    elif isinstance(arg, list):
                        for i in arg:
                            argument_info += str(arg[i]) + " - "
                    else:
                        argument_info += str(arg)

                if len(argument_info) > 0:
                    renpy.say(None, "Available: " + crisis.name + "\n" + argument_info)

    def silent_pregnant_tits_start_person(person):
        person.event_triggers_dict["preg_knows"] = True
        person.tits = Person.get_larger_tit(person.tits) #Her tits start to swell.
        person.personal_region_modifiers["breasts"] = person.personal_region_modifiers["breasts"] + 0.1 #As her tits get larger they also become softer, unlike large fake tits. (Although even huge fake tits get softer)

        if not person.title is None:    # don't announce pregnancy for unknown girls
            target_label = "pregnant_tits_announce" if person.is_mc_father() else "silent_pregnant_tits_announce"

            pregnant_tits_announce_action = Action("Announce Pregnant Tits", pregnant_tits_announcement_requirement, target_label, args = day)
            person.on_talk_event_list.append(Limited_Time_Action(pregnant_tits_announce_action, 15))
        return

    def silent_pregnant_transform_person(person):
        if "pre_preg_body" in person.event_triggers_dict:
            renpy.say("Warning", "Something went wrong with pregnancy transform for " + person.name + ", she is already transformed.")
            return # already transformed

        person.event_triggers_dict["pre_preg_body"] = person.body_type
        person.body_type = "standard_preg_body"
        person.tits = Person.get_larger_tit(person.tits) # Her tits get even larger
        person.personal_region_modifiers["breasts"] = person.personal_region_modifiers["breasts"] + 0.1 #As her tits get larger they also become softer, unlike large fake tits. (Although even huge fake tits get softer)
        person.lactation_sources += 1

        if not person.title is None:    # don't announce pregnancy for unknown girls
            target_label = "pregnant_transform_announce" if person.is_mc_father() else "silent_pregnant_transform_announce"

            preg_transform_announce_action = Action("Pregnancy Transform Announcement", preg_transform_announce_requirement, target_label, args = day)
            person.on_room_enter_event_list.append(Limited_Time_Action(preg_transform_announce_action, 15))

        target_label = "pregnant_finish_announce" if person.is_mc_father() else "silent_pregnant_finish_announce"

        preg_finish_announce_action = Action("Pregnancy Finish Announcement", preg_finish_announcement_requirement, target_label, args = person, requirement_args = person)
        mc.business.add_mandatory_crisis(preg_finish_announce_action)
        return

    def clone_schedule(person):
        schedule = {}
        for day in __builtin__.range(0, 7):
            schedule[day] = {}
            for tod in __builtin__.range(0, 5):
                schedule[day][tod] = person.schedule[day][tod]
        return schedule

    def silent_pregnant_finish_announce_person(person):
        person.available = False

        target_label = "pregnant_finish" if person.is_mc_father() else "silent_pregnant_finish"

        preg_finish_action = Action("Pregnancy Finish", preg_finish_requirement, target_label, args = person, requirement_args = [person, day + renpy.random.randint(4,7)])
        mc.business.add_mandatory_morning_crisis(preg_finish_action)
        return

    def pregnant_finish_announce_person(person):
        person.available = False

        preg_finish_action = Action("Pregnancy Finish", preg_finish_requirement, "pregnant_finish", args = person, requirement_args = [person, day + renpy.random.randint(4,7)])
        mc.business.mandatory_morning_crises_list.append(preg_finish_action)
        return

    def become_pregnant(person, mc_father = True, progress_days = 0): # Called when a girl is knocked up. Establishes all of the necessary bits of info.
        # prevent issues when function is called for already pregnant person / clones are sterile
        if not person or person.is_pregnant() or person.has_role(clone_role):
            return

        # she recently had a child, so block pregnancy for at least 36 days (allow all events to play out)
        if day < person.event_triggers_dict.get("last_birth", -36) + 36:
            return

        # clear any party schedules
        if not person in unique_character_list:
            person.set_override_schedule(None, the_times = [4])
        # historic start date of pregnancy
        start_day = day - progress_days

        person.event_triggers_dict["immaculate_conception"] = person.has_taboo("vaginal_sex")
        person.event_triggers_dict["preg_accident"] = person.on_birth_control # If a girl is on birth control the pregnancy is an accident.
        person.event_triggers_dict["preg_start_date"] = start_day
        person.event_triggers_dict["preg_announce_day"] = start_day + renpy.random.randint(7, 11)
        person.event_triggers_dict["preg_tits_date"] = start_day + 14 + renpy.random.randint(0,5)
        person.event_triggers_dict["preg_transform_day"] = start_day + 30 + renpy.random.randint(0,10)
        person.event_triggers_dict["preg_finish_announce_day"] = start_day + 90 + renpy.random.randint(0,10)
        person.event_triggers_dict["pre_preg_tits"] = person.tits
        person.event_triggers_dict["preg_mc_father"] = mc_father

        if day > person.event_triggers_dict.get("preg_start_date", 0) + 14:
            person.event_triggers_dict["preg_knows"] = True
        else:
            target_label = "pregnant_announce" if person.is_mc_father() else "silent_pregnant_announce"

            preg_announce_action = Action("Pregnancy Announcement", (preg_announce_requirement if not bugfix_installed else pregnant_announce_requirement), target_label)
            person.on_room_enter_event_list.append(Limited_Time_Action(preg_announce_action, (5 * 10) + (5 * 5))) #LTA is turns valid, not days (5 slots per day), yield 5 days after it becomes active

        if day > person.event_triggers_dict.get("preg_tits_date", 0):
            person.event_triggers_dict["preg_knows"] = True
            person.tits = Person.get_larger_tit(person.tits) #Her tits start to swell.
            person.personal_region_modifiers["breasts"] = person.personal_region_modifiers["breasts"] + 0.1
        else:
            target_label = "pregnant_tits_start" if person.is_mc_father() else "silent_pregnant_tits_start"

            preg_tits_action = Action("Pregnancy Tits Grow", (preg_tits_requirement if not bugfix_installed else pregnant_tits_requirement), target_label, args = person, requirement_args = person)
            mc.business.add_mandatory_morning_crisis(preg_tits_action)

        if day > person.event_triggers_dict.get("preg_transform_day", 0):
            person.event_triggers_dict["pre_preg_body"] = person.body_type
            person.body_type = "standard_preg_body"
            person.tits = Person.get_larger_tit(person.tits) # Her tits get even larger
            person.personal_region_modifiers["breasts"] = person.personal_region_modifiers["breasts"] + 0.1 #As her tits get larger they also become softer, unlike large fake tits. (Although even huge fake tits get softer)
            person.lactation_sources += 1

            target_label = "pregnant_finish_announce" if person.is_mc_father() else "silent_pregnant_finish_announce"

            preg_finish_announce_action = Action("Pregnancy Finish Announcement", preg_finish_announcement_requirement, target_label, args = person, requirement_args = person)
            mc.business.add_mandatory_crisis(preg_finish_announce_action)
        else:
            target_label = "pregnant_transform" if person.is_mc_father() else "silent_pregnant_transform"

            preg_transform_action = Action("Pregnancy Transform", (preg_transform_requirement if not bugfix_installed else pregnant_transform_requirement), target_label, args = person, requirement_args = person)
            mc.business.add_mandatory_morning_crisis(preg_transform_action) #This event adds an announcement event the next time you enter the same room as the girl.

        person.add_role(pregnant_role)

        mc.listener_system.fire_event("girl_pregnant", the_person = person)
        return

init 3 python:
    def pregnant_finish_person(person):
        if not "pre_preg_body" in person.event_triggers_dict:
            renpy.say("Warning", "Something went wrong with restoring the pregnancy of " + person.name)
            return False # she is not giving birth

        person.body_type = person.event_triggers_dict.pop("pre_preg_body")
        person.available = True

        person.event_triggers_dict["preg_knows"] = False #Otherwise she immediately knows the next time she's pregnant.
        person.kids += 1 #TODO: add a new role related to a girl being a mother of your kid?
        person.event_triggers_dict["last_birth"] = day  # record last day giving birth

        tit_shrink_one_day = day + renpy.random.randint(7,14)
        tit_shrink_one = Action("Tits Shrink One", tit_shrink_requirement, "tits_shrink", args = [person, True, add_tits_shrink_one_announcement], requirement_args = [person, tit_shrink_one_day])
        mc.business.mandatory_morning_crises_list.append(tit_shrink_one) #Events for her breasts to return to their normal size.

        tit_shrink_two_day = day + renpy.random.randint(21,35)
        tit_shrink_two = Action("Tits Shrink Two", tit_shrink_requirement, "tits_shrink", args = [person, False, add_tits_shrink_two_announcement], requirement_args = [person, tit_shrink_two_day])
        mc.business.mandatory_morning_crises_list.append(tit_shrink_two)

        if person.is_mc_father():
            person.sex_record["Children with MC"] = person.sex_record.get("Children with MC", 0) + 1

        the_person.remove_role(pregnant_role)
        return True

label silent_pregnant_announce(the_person):
    #In silent pregnancy, she just knows she's pregnant, but doesn't necessarily announce it.
    $ the_person.event_triggers_dict["preg_knows"] = True #Set here and in the larger tits, represents the person knowing they're pregnant so they don't ask for condoms ect.
    #"DEBUG [the_person.title] now knows she is pregnant."
    return

label silent_pregnant_tits_start(the_person):
    $ silent_pregnant_tits_start_person(the_person)
    #"DEBUG [the_person.title] grows larger tits."
    return

label silent_pregnant_tits_announce(start_day, the_person):
    "As you begin to talk to [the_person.title], you can't help but notice her tits seem... a little larger than your remember?"
    "The way they bounce is enticing also. There is this glow that surrounds her in general. You wonder what is going on?"
    call talk_person(the_person) from _call_talk_person_silent_11
    return

label silent_pregnant_transform(the_person): #Changes the person to their pregnant body and stores what their pre-pregnancy body and tits were
    $ silent_pregnant_transform_person(the_person)
    return

label silent_pregnant_transform_announce(start_day, the_person):
    if the_person.title is None or not mc.phone.has_number(the_person):
        return  # unknown girls should not inform you about their pregnancy

    $ the_person.draw_person()
    "[the_person.possessive_title] notices you and comes over to talk."
    the_person "Hey [the_person.mc_title]. So, it's probably pretty obvious at this point..."
    "She turns and runs a hand over her belly, accentuating the new and prominent curves that have formed there."
    the_person "... but, I'm pregnant!"
    mc.name "Congratulations! You look fantastic. You really are glowing."
    $ the_person.change_happiness(10)
    if the_person.is_employee():
        the_person "Thank you! So obviously, when the baby comes, I'll need some time off work..."
        mc.name "Just let me know when the time comes, if you can. We'll make do without you while you are giving birth."
    the_person "Thank you!"
    return

label silent_pregnant_finish_announce(the_person): #TODO: have more variants for girlfriend_role, affair_role, etc.
    $ silent_pregnant_finish_announce_person(the_person)
    if the_person.title is None or not mc.phone.has_number(the_person):
        return  # unknown girls should not announce delivery

    # The girl tells you she'll need a few days to have the kid and recover, and she'll be back in a few days.
    "You get a call from [the_person.possessive_title]. You answer it."
    mc.name "Hey [the_person.title], what's up?"
    if the_person.is_employee():
        the_person "Hi [the_person.mc_title]. I wanted to let you to know that I won't be at work for a few days."
    else:
        the_person "Hi [the_person.mc_title], I have some exciting news."
    the_person "I saw my doctor yesterday and he tells me I'm going to pop any day now."
    if day - the_person.event_triggers_dict.get("preg_start_date", day) <= 90: #It's unusually short
        the_person "It's earlier than I expected, but he tells me everything looks like it's perfectly normal."
    mc.name "That's amazing news. Do you need me to do anything?"
    the_person "No, I just wanted to let you know. Thanks for everything!"
    mc.name "Okay, I'll talk to you soon then."
    the_person "I'll let you know as soon as things are finished. Bye!"
    return

label silent_pregnant_finish(the_person):
    $ pregnant_finish_person(the_person)
    if the_person.title is None:
        return  # unknown girls should not about the delivery

    "You get a call from [the_person.possessive_title] early in the morning. You answer it."
    if the_person in [aunt, mom]:
        the_person "Hey [the_person.mc_title], good news! Two days ago I had a beautiful, healthy baby girl!"
        mc.name "That's amazing, where is she now?"
        the_person "I'll be leaving her with my mother, your grand-mother for now."

    elif the_person in [lily, cousin]:
        the_person "Hey [the_person.mc_title], good news! Two days ago I had a beautiful, healthy baby girl!"
        mc.name "That's amazing, where is she now?"
        the_person "I'll be leaving her with our grandma for now, so I can get back to a normal life."

    elif employee_role in the_person.special_role:
        the_person "Hey [the_person.mc_title], good news! Two days ago I had a beautiful, healthy baby girl! I'll be coming back to work today." #Obviously they're all girls for extra fun in 18 years.
        mc.name "That's amazing, but are you sure you don't need more rest?"
        if the_person.relationship != "Single":
            $ so_title = SO_relationship_to_title(the_person.relationship)
            the_person "I'll be fine, I'll be leaving her with my [so_title], so I can come back to work sooner."
        else:
            the_person "I'll be fine. I'm leaving her with my mother for a little while so I can get back to a normal life."

    else:
        the_person "Hey [the_person.mc_title], good news! Two days ago I had a beautiful, healthy baby girl!"
        mc.name "That's amazing, how are you doing?"
        if the_person.relationship != "Single":
            $ so_title = SO_relationship_to_title(the_person.relationship)
            the_person "I'll be fine, I'll be leaving her with my [so_title]."
        else:
            the_person "I'll be fine. I'm leaving her with my mother for a little while so I can get back to a normal life."

    the_person "I just wanted to let you know. I'll talk to you soon."
    "You say goodbye and [the_person.title] hangs up."
    return
