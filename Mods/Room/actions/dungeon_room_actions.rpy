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

label dungeon_room_appoint_slave_label():
    while True:
        $ people_list = get_sorted_people_list(mc.location.people, "Turn into slave", ["Back"])

        if "build_menu_items" in globals():
            call screen main_choice_display(build_menu_items([people_list]))
        else:
            call screen main_choice_display([people_list])
            
        $ person_choice = _return
        $ del people_list

        if person_choice == "Back":
            return # Where to go if you hit "Back"
        else:
            call dungeon_room_appoint_slave_label_2(person_choice) from dungeon_room_appoint_slave_label_1
            $ del person_choice

label dungeon_room_appoint_slave_label_2(the_person):

    if slave_role not in the_person.special_role: # What happens when you try to appoint them

        if the_person.obedience >= 130 and the_person.get_opinion_score("being submissive") > 0:
            "[the_person.possessive_title] seems to be into the idea of serving you."

            $ the_person.call_dialogue("sex_obedience_accept")
        elif the_person.get_opinion_score("being submissive") <= 0 and the_person.obedience >= 160:
            "[the_person.possessive_title] is willing to serve you as her master and now likes being submissive."
            $ the_person.sexy_opinions["being submissive"] = [1, True]               
            $ the_person.call_dialogue("sex_obedience_accept")
        else:
            "[the_person.possessive_title] needs to be more obedient before being willing to commit to being your slave."
            return

        $ the_person.special_role.append(slave_role)

        "[the_person.title] is now a willing slave of yours."


    else: # What happens when they are already appointed

        $ the_person.special_role.remove(slave_role)


        "You release [the_person.possessive_title] from their duties as a slave."

    return
