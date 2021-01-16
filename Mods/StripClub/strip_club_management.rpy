## Stripclub storyline Mod by Corrado
# You have some strippers but the business could improve.

init 3304 python:
    def strip_club_get_manager():
        managers = people_in_role(manager_role)
        if __builtin__.len(managers) > 0:
            return managers[0]
        return None

    def strip_club_get_mistress():
        mistresses = people_in_role(mistress_role)
        if __builtin__.len(mistresses) > 0:
            return mistresses[0]
        return None

    def strip_club_get_job_title(person):
        if person.has_role(stripper_role):
            return "Stripper"
        elif person.has_role(waitress_role):
            return "Waitress"
        elif person.has_role(bdsm_performer_role):
            return "BDSM Performer"
        elif person.has_role(manager_role):
            return "Strip Club Manager"
        elif person.has_role(mistress_role):
            return "Strip Club Mistress"
        return ""

    def strip_club_manager_reminder_requirement():
        if day >= (get_strip_club_foreclosed_last_action_day() + 7): # the event start to trigger after 7 days MC bought the club.
            if get_strip_club_foreclosed_stage() == 5 and not strip_club_get_manager(): # the event only trigger if there's no Manager yet
                if day % 5 == 0 and time_of_day == 2: # the event trigger every 5 days in the afternoon. (toughts)
                    return True
        return False

    def add_strip_club_manager_reminder_action():
        if not strip_club_get_manager():
            strip_club_manager_reminder_action = Action("A simple reminder to appoint someone as strip club manager", strip_club_manager_reminder_requirement, "strip_club_manager_reminder_label")
            mc.business.add_mandatory_crisis(strip_club_manager_reminder_action)

    def strip_club_manager_hire_more_stripper_reminder_requirement():
        if __builtin__.len(stripclub_strippers) < 5: # the event only trigger if there's not the max nr. of strippers (5 + 1 manager)
            if strip_club_get_manager(): # the event only trigger if there's a Manager
                if day % 5 == 0 and time_of_day == 2: # the event trigger every 5 days in the afternoon. (phone call)
                    return True
        return False

    def add_strip_club_manager_hire_more_stripper_reminder_action():
        if __builtin__.len(stripclub_strippers) < 5:
            strip_club_manager_hire_more_stripper_reminder_action = Action("A simple reminder from the strip club manager to hire more stripper", strip_club_manager_hire_more_stripper_reminder_requirement, "strip_club_manager_hire_more_stripper_reminder_label")
            mc.business.add_mandatory_crisis(strip_club_manager_hire_more_stripper_reminder_action)

    def strip_club_manager_waitresses_suggestion_requirement():
        if __builtin__.len(stripclub_waitresses) < 2: # the event only trigger if there's not the max nr. of waitresses (2)
            if strip_club_get_manager(): # the event only trigger if there's a Manager
                if day % 5 == 2 and time_of_day == 2: # the event trigger every 5 days in the afternoon. (phone call)
                    return True
        return False

    def add_strip_club_manager_waitresses_suggestion_action():
        if __builtin__.len(stripclub_waitresses) < 2:
            strip_club_manager_waitresses_suggestion_action = Action("Your strip club manager suggest to hire a couple of waitresses.", strip_club_manager_waitresses_suggestion_requirement, "strip_club_manager_waitresses_suggestion_label")
            mc.business.add_mandatory_crisis(strip_club_manager_waitresses_suggestion_action)

    def strip_club_manager_hire_more_waitresses_reminder_requirement():
        if __builtin__.len(stripclub_waitresses) < 2: # the event only trigger if there's not the max nr. of waitresses (2)
            if strip_club_get_manager(): # the event only trigger if there's a Manager
                if day % 5 == 2 and time_of_day == 2: # the event trigger every 5 days in the afternoon. (phone call)
                    return True
        return False

    def add_strip_club_manager_hire_more_waitresses_reminder_action():
        if __builtin__.len(stripclub_waitresses) < 2: # the event only trigger if there's not the max nr. of waitresses (2)
            strip_club_manager_hire_more_waitresses_reminder_action = Action("A simple reminder from the strip club manager to hire more waitresses", strip_club_manager_hire_more_waitresses_reminder_requirement, "strip_club_manager_hire_more_waitresses_reminder_label")
            mc.business.add_mandatory_crisis(strip_club_manager_hire_more_waitresses_reminder_action)

    def strip_club_manager_bdsm_room_suggestion_requirement():
        if not mc.business.event_triggers_dict.get("strip_club_has_bdsm_room", False):
            if day >= (get_strip_club_foreclosed_last_action_day() + 15): # the event trigger after 15 days you have a manager
                if not mc.business.event_triggers_dict.get("strip_club_bdsm_decision_day", None): # Not suggested yet
                    if __builtin__.len(stripclub_waitresses) > 0 and strip_club_get_manager():
                        if not mc.location is strip_club and time_of_day == 3:
                            return True
        return False

    def add_strip_club_manager_bdsm_room_suggestion_action():
        if not mc.business.event_triggers_dict.get("strip_club_has_bdsm_room", False):
            strip_club_manager_bdsm_room_suggestion_action = Action("Your strip club manager suggest to build a new BDSM room.", strip_club_manager_bdsm_room_suggestion_requirement, "strip_club_manager_bdsm_room_suggestion_label")
            mc.business.add_mandatory_crisis(strip_club_manager_bdsm_room_suggestion_action)

    def strip_club_manager_bdsm_room_reminder_requirement():
        if not mc.business.event_triggers_dict.get("strip_club_has_bdsm_room", False) and mc.business.event_triggers_dict.get("strip_club_bdsm_decision_day") == 0: # the event only trigger if the bdsm_room isn't started yet
            if day % 5 == 2 and time_of_day == 2: # the event trigger every 5 days in the afternoon. (phone call)
                return True
        return False

    def add_strip_club_manager_bdsm_room_reminder_action():
        if not mc.business.event_triggers_dict.get("strip_club_has_bdsm_room", False):
            strip_club_manager_bdsm_room_reminder_action = Action("A simple reminder from the strip club manager to build a BDSM room.", strip_club_manager_bdsm_room_reminder_requirement, "strip_club_manager_bdsm_room_reminder_label")
            mc.business.add_mandatory_crisis(strip_club_manager_bdsm_room_reminder_action)

    def strip_club_manager_bdsm_room_build_requirement():
        if mc.business.funds >= 10000:
            if not mc.business.event_triggers_dict.get("strip_club_has_bdsm_room", False):
                if strip_club_get_manager():
                    if not mc.business.is_open_for_business():
                        return "Only during work hours"
                    return True
        return False

    strip_club_manager_bdsm_room_build_action = Action("Build a BDSM room\n{color=#ff0000}{size=18}Costs: $10,000{/size}{/color}", strip_club_manager_bdsm_room_build_requirement, "strip_club_manager_bdsm_room_build_label")

    def strip_club_manager_bdsm_room_built_requirement():
        if day >= (mc.business.event_triggers_dict.get("strip_club_bdsm_decision_day") + 5):
            if mc.business.is_open_for_business(): # only during work hours
                return True
        return False

    def add_strip_club_manager_bdsm_room_built_event():
        strip_club_manager_bdsm_room_built_event = Action("Your new BDSM room has been built.", strip_club_manager_bdsm_room_built_requirement, "strip_club_manager_bdsm_room_built_label")
        mc.business.add_mandatory_crisis(strip_club_manager_bdsm_room_built_event)

    def strip_club_switch_rooms_requirement():
        if mc.business.event_triggers_dict.get("strip_club_has_bdsm_room", False):
            return True
        return False

    strip_club_switch_rooms_action = Action("Switch rooms", strip_club_switch_rooms_requirement, "strip_club_switch_rooms_label", menu_tooltip = "Switch between Stripclub and BDSM rooms.")


label strip_club_manager_reminder_label():
    "A few days have passed since you bought the strip club, and after running the numbers, you realize the business could be better..."
    "But you can't spend all your time there micro-managing everything, you need to find someone to do it for you."
    "Someone obedient to you, but also strong enough to manage the other girls, the customers and the suppliers... Perhaps one of the strippers?"
    return

label strip_club_manager_hire_more_stripper_reminder_label(): # phone call
    if __builtin__.len(stripclub_strippers) >= 5:
        return
    "Suddenly your smartphone rings, it's your strip club manager."
    $ the_person = strip_club_get_manager()
    the_person.char "Hello [the_person.mc_title], I called just to remember you we can have five girls here, performing on the stage."
    the_person.char "To have them would make setting up the shifts more easy and, of course, it would be more profitable for you."
    mc.name "Thank you [the_person.title]... I know, I'll find someone, I promise!"
    the_person.char "Ok [the_person.mc_title], thank you!"
    return

label strip_club_manager_hire_more_waitresses_reminder_label(): # phone call
    if __builtin__.len(stripclub_waitresses) >= 2:
        return
    "Suddenly your smartphone rings, it's your strip club manager."
    $ the_person = strip_club_get_manager()
    the_person.char "Hello [the_person.mc_title], I called just to remember you we need two waitresses, we can't have our strippers do that."
    mc.name "Thank you [the_person.title]... I know, I'll find someone, I promise!"
    the_person.char "Ok [the_person.mc_title], thank you!"
    return

label strip_club_manager_waitresses_suggestion_label(): # (personal contact)
    "Suddenly your smartphone rings: it's your StripClub manager."
    $ the_person = strip_club_get_manager()
    the_person.char "Hi [the_person.mc_title]! Can you join me here at the Club ? I need to talk with you..."
    mc.name "Sure [the_person.title], I'm coming."
    $ mc.change_location(strip_club)
    $ mc.location.show_background()
    $ the_person.draw_person(emotion = "happy", position = "stand3")
    mc.name "Here I am [the_person.title], how things are going here ?"
    the_person.char "That's exactly what I wanna talk to you about: you spent a lot of money to buy this place, don't you wanna make it more profitable ?"
    mc.name "Of course I do: what do you have in mind ?"
    the_person.char "A lot of customers here get a drink at the bar then sit at the border of the stage to watch the girls stripping, right ?"
    mc.name "Yes, that's how the business here works..."
    the_person.char "Exactly! After they got their drink, the customers don't wanna move anymore from the stage, only a few come back to get another drink..."
    mc.name "I think I got where are you going with this..."
    the_person.char "Yeah! What if we had a couple of waitresses serving the drinks directly at the customer's seat, and maybe some peanuts or some chips..."
    the_person.char "They would be more thirsty, so the drinks sold at the end of the day would be a lot, lot more!"
    mc.name "Thank you [the_person.title], that's really a good idea! I'll look into hiring some waitresses as soon as possible."
    $ the_person.draw_person(emotion = "happy", position = "stand4")
    "[the_person.title] smiles back to you, proud to have proven herself worthy."
    $ add_strip_club_manager_hire_more_waitresses_reminder_action()
    return

label strip_club_manager_bdsm_room_suggestion_label(): # (personal contact)
    "Suddenly your smartphone rings, it's your strip club manager."
    $ the_person = strip_club_get_manager()
    the_person.char "Hi [the_person.mc_title]! Can you join me here at the club? I need to talk with you..."
    mc.name "Sure [the_person.title], I'll be right over."
    $ mc.change_location(strip_club)
    $ mc.location.show_background()
    $ the_person.draw_person(emotion = "happy", position = "stand3")
    mc.name "Ok, here I am [the_person.title], how things are going here?"
    the_person.char "That's exactly what I wanna talk to you about, I have an idea to make the business here more profitable."
    mc.name "You have my attention, what do you have in mind?"
    the_person.char "This place has a lot of unused space around the back... What if we make another room there for a different kind of shows?"
    mc.name "'Different shows'? You know that this is a strip club, right, and not a brothel?"
    the_person.char "No no no [the_person.mc_title], nothing like that! I did some research, and I found that in other cities you can find places that offer BDSM shows."
    the_person.char "But here, in our city, there's nothing like it... yet!"
    mc.name "What do you mean with 'BDSM shows'?"
    the_person.char "Well, you know there are girls who like to submit themselves completely to their partners during sex, right?"
    "Your mind wanders of for a bit, of course you know, you know very well!"
    the_person.char "And you know that almost every girl, more or less, likes to show herself off, right?"
    "You don't even try to hide your smile, you know that too..."
    the_person.char "So, in a BDSM show girls submit themselves completely to their partners in a public place like this, showing off their obedience and devotion to their Master."
    mc.name "But you know [the_person.title], we can't have guys on the stage, fucking around with girls... we would get into some serious trouble!"
    the_person.char "Whoever said anything about men performing on stage?"
    "She mischievously winks at you, now it's clear what kind of picture is floating in her vicious mind..."
    mc.name "I got it and I admit it could be a very good idea, but I need to double-check with my lawyer to see if it is feasible."
    the_person.char "I made a business prospect for you with costs and revenues, I will send it to your phone."
    mc.name "Thank you [the_person.title], I'll look at it!"
    $ the_person.draw_person(emotion = "happy", position = "stand4")
    "After you got the documents, even just with a quick glance you notice that the $10,000 investment could be very, very profitable."
    $ add_strip_club_manager_bdsm_room_reminder_action()
    $ mc.business.event_triggers_dict["strip_club_bdsm_decision_day"] = 0
    $ strip_club.add_action(strip_club_manager_bdsm_room_build_action)
    return

label strip_club_manager_bdsm_room_build_label(): # (action button)
    "You pick up the phone and call your usual contractor."
    mc.name "Hello, this is [mc.name] [mc.last_name] from [strip_club.formalName], I need some construction work done here at my club."
    "You go over the details and agree on a price of $10,000 for converting some unused space into a fully equipped and soundproofed BDSM room."
    $ mc.business.change_funds(-10000)
    $ add_strip_club_manager_bdsm_room_built_event()
    $ strip_club.remove_action(strip_club_manager_bdsm_room_build_action)
    $ mc.business.event_triggers_dict["strip_club_bdsm_decision_day"] = day
    return

label strip_club_manager_bdsm_room_reminder_label(): # phone call
    "Suddenly your phone rings, it's your strip club manager."
    $ the_person = strip_club_get_manager()
    the_person.char "Hello [the_person.mc_title], did you check the business prospect I sent you for having a special room for BDSM shows?"
    the_person.char "I'm sure it would make the business here a lot more profitable, we will be the only club in the city having that kind of entertainment."
    mc.name "Thank you [the_person.title]... I know, I'll get back to you, I promise!"
    the_person.char "Ok [the_person.mc_title], thank you!"
    return

label strip_club_manager_bdsm_room_built_label(): # (time event)
    $ man_name = get_random_male_name()
    "Going about your day, you get a call from your contractor."
    man_name "Hello Sir, this is [man_name] from Turner Construction. I just wanted you to know that we have finished our work."
    mc.name "Thank you [man_name], much appreciated."
    "The BDSM room at the strip club is now ready for use."
    $ strip_club.add_action(strip_club_switch_rooms_action)
    $ bdsm_room.add_action(strip_club_switch_rooms_action)
    $ add_strip_club_cage_her_action_to_mc_actions()
    $ mc.business.event_triggers_dict["strip_club_has_bdsm_room"] = True
    return

label strip_club_switch_rooms_label():
    if mc.location is strip_club:
        $ mc.change_location(bdsm_room)
        $ mc.location.show_background()
    elif mc.location is bdsm_room:
        $ mc.change_location(strip_club)
        $ mc.location.show_background()
    return
