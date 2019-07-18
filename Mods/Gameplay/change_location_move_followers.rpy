# Allows followers from list_of_followers to move with the player

init 5 python:
    add_label_hijack("normal_start", "activate_change_location_mod")
    add_label_hijack("after_load", "update_change_location_mod")

label activate_change_location_mod(stack):

    call store_change_location_mod_actions from activate_change_location_mod_1
    $ execute_hijack_call(stack)
    return

label update_change_location_mod(stack):

    call store_change_location_mod_actions from update_change_location_mod_1
    $ execute_hijack_call(stack)
    return

init 2 python: # Change location requirements block.

    def move_followers_action_requirement():
        if "generic_people_role_follow" in globals():
            return len(list_of_followers) > 0 and generic_people_role_follow


label store_change_location_mod_actions():

    python:

        move_followers_action = ActionMod("Moves the followers with the player", move_followers_action_requirement, "move_followers_label", priority = move_player_action.priority + 1, menu_tooltip = "Moves the followers with the player to new location.") # If this action requires the mc.location to be set first then it would depend on move_player_action therefore set it to always run after its dependency.
        if move_followers_action not in change_location_action_list:
            change_location_action_list.append(move_followers_action)

    return

label move_followers_label():

    python:
        # list of followers follow you around. Will go to scheduled room on time advance.¨
        # Added extra checks to make sure it runs through everything and moves all people in list, not only first.
        for room in list_of_places:
            for person in room.people:
                for person in list_of_followers:
                    if person in list_of_followers:
                        if person in room.people:
                            room.move_person(person, new_location)

    return
