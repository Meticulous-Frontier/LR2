# TODO: Encourage players to unlock the "Follow Me" command to bring people to the Dungeon for situational bonuses from the objects in the Room.
#       Balance how much of a bonus the objects give. Right now it's a sluttiness_modifier = 10, obedience_modifier = 20 for the lowest tier, "the_bdsmbed" which is +10 obedience from a normal bed.
# NOTE: Strip action is now in generic_people_role
init 10 python:
    def dungeon_room_appoint_slave_requirement():
        if mc.location.people:
            return True
        else:
            return "Requires: Person in Room"

    dungeon_room_appoint_slave_action = Action("Appoint a slave", dungeon_room_appoint_slave_requirement, "dungeon_room_appoint_slave_label", menu_tooltip = "Assigns the person a role as a slave. Use the \"Follow Me\" Action on a person to bring them to the Dungeon.")

    def dungeon_intro_action_requirement():
        if day > 24 and time_of_day > 1 and time_of_day < 4:
            if mc.business.funds > 20000 and not mc.business.is_open_for_business(): #Only trigger when alone in the office
                if mc.is_at_work():
                    return True
        return False

    def dungeon_completed_action_requirement(completion_day):
        if day > completion_day and mc.is_at_work() and mc.business.is_open_for_business():
            return True
        return False

    def add_dungeon_intro_action():
        dungeon_intro_action = Action("Dungeon Intro", dungeon_intro_action_requirement, "dungeon_intro_label")
        mc.business.add_mandatory_crisis(dungeon_intro_action)

    def add_dungeon_completed_action():
        dungeon_completed_action = Action("Dungeon Completed", dungeon_completed_action_requirement, "dungeon_completed_label", requirement_args = day + 7)
        mc.business.add_mandatory_crisis(dungeon_completed_action)

    def slave_unique_sex_positions(person, prohibit_tags = []):
        positions = []
        if "Foreplay" not in prohibit_tags:
            positions.append([spanking, 1])

        return positions

label dungeon_intro_label():
    "By yourself on the weekend at work, you are taking a moment to relax. Suddenly you are struck by a brilliant idea..."
    "You decide to build a dungeon at your house that would allow you to turn obedient girls into slaves who fulfill your deepest desires."
    "You pick up the phone and make a call."
    mc.name "Good afternoon, this is [mc.name] [mc.last_name] from [mc.business.name], I need some construction work done at my house."
    "You go over the details with the constructor and agree on a price of $10,000 for converting your existing cellar into a dungeon, fully soundproofed of course."
    $ mc.business.change_funds(-10000)
    $ add_dungeon_completed_action()
    return

label dungeon_completed_label():
    $ man_name = get_random_male_name()
    "Going about your day, you get a call from your contractor."
    man_name "Hello Sir, this is [man_name] from Turner Construction. I just wanted you to know that we have finished our work."
    mc.name "Thank you [man_name], much appreciated."
    "The dungeon at your house is now ready for use."
    $ mc.business.event_triggers_dict["dungeon_owned"] = True
    $ dungeon.visible = True
    return

label dungeon_room_appoint_slave_label():
    while True:
        call screen enhanced_main_choice_display(build_menu_items([get_sorted_people_list(mc.location.people, "Turn into slave", ["Back"])]))
        $ person_choice = _return

        if person_choice == "Back":
            return # Where to go if you hit "Back"
        elif person_choice.personality is alpha_personality:
            "This girl has an Alpha personality and will never submit into becoming your slave. You could turn her into a bimbo, that would remove her Alpha personality."
        else:
            call dungeon_room_appoint_slave_label_2(person_choice) from dungeon_room_appoint_slave_label_1
            $ del person_choice

label dungeon_room_appoint_slave_label_2(the_person):

    if not the_person.has_role(slave_role): # What happens when you try to appoint them
        if the_person.obedience >= 130 and the_person.get_opinion_score("being submissive") > 0:
            "[the_person.possessive_title] seems to be into the idea of serving you."
            $ the_person.call_dialogue("sex_obedience_accept")
        elif the_person.get_opinion_score("being submissive") <= 0 and the_person.obedience >= 160:
            "[the_person.possessive_title] is willing to serve you as her master."
            $ the_person.call_dialogue("sex_obedience_accept")
        else:
            "[the_person.possessive_title] needs to be more obedient before being willing to commit to being your slave."
            return

        $ the_person.add_role(slave_role)

        $ the_person.event_triggers_dict["unique_sex_positions"] = slave_unique_sex_positions

        "[the_person.title] is now a willing slave of yours."


    else: # What happens when they are already appointed
        "Releasing has a high impact on the girls stats, are you sure?"
        menu:
            "Release her":
                $ slave_release_slave(the_person)
                $ del the_person.event_triggers_dict["unique_sex_positions"]
                "You release [the_person.possessive_title] from their duties as a slave."
            "Never mind":
                pass

    return
