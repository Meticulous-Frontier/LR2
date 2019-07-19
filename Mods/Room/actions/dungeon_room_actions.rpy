# TODO: Encourage players to unlock the "Follow Me" command to bring people to the Dungeon for situational bonuses from the objects in the Room.
#       Balance how much of a bonus the objects give. Right now it's a sluttiness_modifier = 10, obedience_modifier = 20 for the lowest tier, "the_bdsmbed" which is +10 obedience from a normal bed.
# TODO: Create a "Slave" role that can be unlocked at high obedience. It should make sure that "Generic People Actions" are always available.
# TODO: Make a "Strip" Action that can be used to a) Strip person of clothing and B) Change their planned outfit to the stripped state if the player wants.
# TODO: Create a short story resulting in an expensive Serum trait that enables the "Slave" role, inherently skipping the common requirements for certain Actions.
#       Something as simple as 1st Slave reveal short text, then the same on 2nd and finally the third reveals a short text and that you have somehow come to the conclusion
#       That you know how to chemically induce the "Slave" behavior.
# TODO: Find and implement interesting Actions exclusive to the Room or the Role so that it doesn't become meaningless filler content.
#       Increasing obedience seems to be relatively easy in the base game, so having obedience boosts seem redundant. What about converting some obedience into sluttiness?
#       See whats possible in regards to using Role "Slave" to temporary increase the obedience of other People in the same room if the MainCharacter is present AND has interacted with the "Slave".
# NOTE: Current actions seem pointless and can't see how they could be interesting without extensive story writing work even if fleshed out.
init -1 python:
    dungeon_room_actions = []
    dungeon_room_slave_actions = []

init 10 python:

    def dungeon_room_actions_requirement():
        return True

    def dungeon_room_collar_person_requirement(the_person):
        if the_person.obedience >= 130 and mc.location == office_basement and the_person.dungeon_collar == False:
            return True
        if the_person.dungeon_collar == True:
            return False
        else:
            if mc.location == office_basement: #Only display the if you are in the Dungeon and they don't have a collar
                return "Requires: 130 Obedience"

    def dungeon_room_uncollar_person_requirement(the_person):
        return the_person.dungeon_collar

    def advance_time_collar_person_requirement():
        return dungeon_room_collar_person_action.enabled

    dungeon_room_action = Action("Manage [office_basement.formalName]", dungeon_room_actions_requirement, "dungeon_room_action_label",
        menu_tooltip = "Do things in the [office_basement.formalName]")

    dungeon_room_collar_person_action = ActionMod("Place collar on [the_person.title].", dungeon_room_collar_person_requirement, "dungeon_room_collar_person_label",
        menu_tooltip = "Put a collar of ownership on the target, ensure that their obedience stays high.", category = "Dungeon Actions")
    dungeon_room_uncollar_person_action = ActionMod("Remove collar from [the_person.title].", dungeon_room_uncollar_person_requirement, "dungeon_room_collar_person_label",
        menu_tooltip = "Remove the collar, declearing them a free spirit.", category = "Dungeon Actions", allow_disable = False)
    Person.dungeon_collar = False #NOTE: Is this harmful?
    generic_people_role.actions.append(dungeon_room_collar_person_action)
    generic_people_role.actions.append(dungeon_room_uncollar_person_action)

    advance_time_collar_person_action = ActionMod("Enable collar functionality", advance_time_collar_person_requirement, "advance_time_collar_person_label", allow_disable = False, priority = advance_time_people_to_process_action.priority + 1,
        menu_tooltip = "Allows the dungeon_room_collar_person_action to do what it is intended to do.")
    advance_time_action_list.append(advance_time_collar_person_action)

label dungeon_room_action_label():
    while True:
        python: #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
                dungeon_options = []
                for act in dungeon_room_actions:
                    dungeon_options.append(act)
                dungeon_options.append("Back")
                act_choice = call_formated_action_choice(dungeon_options)

        if act_choice == "Back":
            return
        else:
            $ act_choice.call_action()

    return

label dungeon_room_collar_person_label(the_person):

    if the_person.dungeon_collar:
        $ the_person.dungeon_collar = False
        "You remove the collar from your [the_person.possessive_title]'s neck"
    else:
        $ the_person.dungeon_collar = True
        "You put one of the collars you created around your [the_person.possessive_title]'s neck"

    return

label advance_time_collar_person_label():

    python:
        for (people,place) in people_to_process:
            if hasattr(people, "dungeon_collar"): # Since the attribute is not part of the class, make sure it has been attributed first.
                if people.dungeon_collar and people.obedience < 150:
                    people.obedience = 150
    return
