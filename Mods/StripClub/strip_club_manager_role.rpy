## Strip club storyline Mod by Corrado
# You have some strippers but the business could improve: you need a manager.
# When the strip club has a BDSM room, the role will be improved as Mistress.
# The role is incompatible with: low Charisma, slave_role, having collar.

init 3303 python:
    def manager_role_status_acquisition(person):
        if slave_role in person.special_role:
            slave_release_slave(person)
            # restore stat loss from removing slave
            person.change_stats(happiness = 20, love = 20, obedience = 50, add_to_log = False)
            
        person.update_opinion_with_score("taking control", 2, add_to_log = False)
        if not person.personality is alpha_personality:
            person.original_personality = person.personality
            person.personality = alpha_personality
        return

    def has_manager_role_requirement(person):
        if person.has_role(manager_role):
            if not mc.location in [strip_club, bdsm_room]:
                return "Only in [strip_club.formalName]"
            return True
        return False
    
    def allow_promote_to_mistress_requirement(person):
        if person.has_role(manager_role) and mc.business.event_triggers_dict.get("strip_club_has_bdsm_room", False) and not strip_club_get_mistress():
            if not mc.location in [strip_club, bdsm_room]:
                return "Only in [strip_club.formalName]"
            return True
        return False

    def has_mistress_role_requirement(person):
        if person.has_role(mistress_role):
            if not mc.location in [strip_club, bdsm_room]:
                return "Only in [strip_club.formalName]"
            return True
        return False

    def mistress_hunt_for_me_requirement(person):
        if person.has_role(mistress_role):
            if not mc.location in [strip_club, bdsm_room]:
                return "Only in [strip_club.formalName]"
            if person.core_sluttiness < 80:
                return "Requires: 80 Core Sluttiness"
            return True
        return False

    def mistress_hunt_for_me_prey(person):
        valid_people_list = []
        for target in known_people_at_location(mc.location, [person]):
            if willing_to_threesome(person, target):
                valid_people_list.append(person)
        return get_random_from_list(valid_people_list)

    def promote_strip_club_stripper_to_manager(person):
        if person.love <= 0:
            person.love = 5
        person.change_stats(happiness = 15, obedience = 10, love = 5)
        person.remove_role(stripper_role)
        person.remove_role(bdsm_performer_role)
        person.remove_role(waitress_role)
        person.add_role(manager_role)
        # remove from work rosters
        if person in stripclub_strippers:
            stripclub_strippers.remove(person)
        if person in stripclub_bdsm_performers:
            stripclub_bdsm_performers.remove(person)
        if person in stripclub_waitresses:
            stripclub_waitresses.remove(person)

        # change to correct schedule
        if person.is_employee() or person in [lily, mom, aunt]:
            person.event_triggers_dict["strip_club_shifts"] = 1
            person.set_schedule([4], strip_club)
        else:
            person.event_triggers_dict["strip_club_shifts"] = 2
            person.set_schedule([3, 4], strip_club)

        manager_role_status_acquisition(person)

        add_strip_club_manager_hire_more_stripper_reminder_action()
        add_strip_club_manager_bdsm_room_suggestion_action()
        return

    def promote_strip_club_manager_to_mistress(person):
        person.remove_role(manager_role)
        person.add_role(mistress_role)
        # change default work location
        if person.is_employee() or person in [lily, mom, aunt]:
            person.event_triggers_dict["strip_club_shifts"] = 1
            person.set_schedule([4], bdsm_room)
        else:
            person.event_triggers_dict["strip_club_shifts"] = 2
            person.set_schedule([3, 4], bdsm_room)
        return

    manager_role_remove_action = Action("Remove as Manager", has_manager_role_requirement, "manager_role_remove_label", menu_tooltip = "Remove [the_person.title] as strip club manager.")
    promote_to_mistress_action = Action("Promote to Mistress", allow_promote_to_mistress_requirement, "promote_to_mistress_label", menu_tooltip = "Promote [the_person.title] as strip club mistress.")
    mistress_role_remove_action = Action("Remove as Mistress", has_mistress_role_requirement, "mistress_role_remove_label", menu_tooltip = "Remove [the_person.title] as strip club mistress.")
    mistress_hunt_for_me_action = Action("Hunt for me", mistress_hunt_for_me_requirement, "mistress_hunt_for_me_label", menu_tooltip = "Ask her to find you a girl for a threesome.")

    manager_role = Role("Manager", [manager_role_remove_action, promote_to_mistress_action], hidden = False)
    mistress_role = Role("Mistress", [mistress_role_remove_action, mistress_hunt_for_me_action], hidden = False)

label promote_to_manager_label(the_person):
    mc.name "[the_person.title], I need to talk with you."
    the_person.char "Sure [the_person.mc_title], something I can help you with?"
    mc.name "May be, ever since I bought this place I never lost money, but I think the business could be better..."
    mc.name "Manage the girl's shifts, the suppliers, check if everything here is going to take time, and I'm already pretty busy with other things."
    mc.name "So I wanna ask you, do you think you can manage this place? Are you the girl I'm looking for?"
    the_person.char "[mc.name], with the previous owner this place was a real mess, and I've seen the changes and the improvement you made."
    the_person.char "The place now is clean, the girls are happy, and I didn't see those shady figures hanging around this place anymore."
    the_person.char "I get what you're doing here, and I think I see what you are trying to do."
    mc.name "Ok [the_person.title], I will let you run the place, prove to me that I made the right choice."
    "She looks you intensely in your eyes, you can see the excitement for being the chosen one, then she simply responds..."
    the_person.char "I will."
    $ promote_strip_club_stripper_to_manager(the_person)
    return

label manager_role_remove_label(the_person):
    mc.name "[the_person.title], I need to talk with you."
    the_person.char "Sure [the_person.mc_title], something I can help you with?"
    mc.name "I checked your management results and I can't say I'm happy, so I have decided to remove you from your management position."
    $ the_person.draw_person(emotion = "sad")
    the_person.char "I understand [the_person.mc_title], I can assure you I did my best..."
    mc.name "I know, that's why I keep you with me here."
    $ the_person.change_stats(happiness = -10, obedience = 2)
    $ the_person.remove_role(manager_role)

    # this might increase the number of active strippers to 6
    $ strip_club_hire_stripper(the_person, stripper_role)
    return

label promote_to_mistress_label(the_person):
    mc.name "[the_person.title], I need to talk with you."
    the_person.char "Sure [the_person.mc_title], something I can help you with?"
    mc.name "I think someone should manage the BDSM room..."
    the_person.char "Wow, it would be a kinky job that one! Wait, are you planning to get some other man instead of you to do it?"
    $ the_person.draw_person(emotion = "sad")
    the_person.char "Because I don't know if I can accept someone else instead of you giving me orders, even if it is you asking me that..."
    the_person.char "You have been my 'first'... Well, not in the physical way but you know what I mean, and I think you're the only one I can accept..."
    mc.name "Actually I was planning to have a woman doing the job."
    $ the_person.draw_person(emotion = "angry")
    the_person.char "What? No way! I will never agree to have a woman commanding me, if you do that, I will be forced to resign!"
    mc.name "And what if that commanding woman is you?"
    $ the_person.draw_person(emotion = "happy")
    the_person.char "Really? Are you asking me to be, after you, the complete boss here?"
    mc.name "I know it's a dirty job, but someone needs to do it."
    "A malicious smile creeps over her face, while she glances over to the other girls."
    the_person.char "I will do my best... or worst, depending on my mood."
    $ promote_strip_club_manager_to_mistress(the_person)
    return

label mistress_role_remove_label(the_person):
    mc.name "[the_person.title], I need to talk with you."
    the_person.char "Sure [the_person.mc_title], something I can help you with?"
    mc.name "I checked your management results and I can't say I'm happy, so I have decided to remove you from your management position."
    $ the_person.draw_person(emotion = "sad")
    the_person.char "I understand [the_person.mc_title], I can assure you I did my best..."
    mc.name "I know, that's why I keep you with me here."
    $ the_person.remove_role(mistress_role)

    # this might increase the number of active strippers to 6
    $ strip_club_hire_stripper(the_person, stripper_role)
    return

label mistress_hunt_for_me_label(the_person):
    mc.name "Do you think you can find a girl here to have some fun with?"
    the_person.char "Oh, 'that' kind of fun, [the_person.mc_title]? Sure, let me see..."
    $ the_person.draw_person(position = "walking_away")
    "She starts scanning the room, looking for a new victim."
    $ the_person.draw_person(position = "back_peek")
    the_person.char "I think I've found what we're looking for, let me work my magic."
    $ the_person.draw_person(position = "walking_away")
    "She arranges her clothes and starts moving closer to her prey..."
    $ the_person_two = mistress_hunt_for_me_prey(the_person)
    if the_person_two is None:
        $ the_person.draw_person(emotion = "sad")
        the_person.char "Amazing, she's not interested and I cannot find anyone else... Am I loosing my touch?"
        return
    "After a couple of minutes the girls are back."
    $ the_person.draw_person(emotion = "happy", position = "stand4")
    the_person.char "I told her we have something nice planned for her, [the_person.mc_title]..."
    mc.name "Good choice [the_person.title]! So [the_person_two.title], would you like to join us?"
    $ the_person_two.draw_person(emotion = "happy", position = "stand2")
    the_person_two.char "It would be my pleasure [the_person.mc_title]!" # Only known people answer this tnx to the high obedience required
    mc.name "Ok, let's find a more appropriate place, follow me girls!"
    $ mc.change_location(downtown_hotel)
    $ mc.location.show_background()
    $ renpy.scene("active")
    "A couple of minutes later you are in the downtown hotel where you get a room."
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person_two, position = "walking_away")
    $ scene_manager.add_actor(the_person, position = "back_peek")
    "You open the door of the room and motion the girl's to come in, you notice [the_person.title] already grabbing [the_person_two.title]'s ass."
    call start_threesome(the_person, the_person_two, girl_in_charge = the_person, start_object = make_bed(), affair_ask_after = False) from _call_start_threesome_mistress_hunt_for_me_label
    "Once you all had your fun, you go back to the Strip Club."
    $ scene_manager.clear_scene()
    $ mc.change_location(strip_club)
    $ mc.location.show_background()
    return
