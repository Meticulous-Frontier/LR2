# NOTE: This "override" is done by changing the map screen to call this label instead of the previous change_location() function. This is to allow way more flexibility.
init -1 python:
    change_location_action_list = [] # ALl Action(s) appended to this list will be run if their requirements are met when changing location via the map.

init 5 python:
    add_label_hijack("normal_start", "activate_change_location")
    add_label_hijack("after_load", "update_change_location")

label activate_change_location(stack):

    call store_change_location_actions from activate_change_location_1
    $ execute_hijack_call(stack)
    return

label update_change_location(stack):

    call store_change_location_actions from update_change_location_1
    $ execute_hijack_call(stack)
    return

init 2 python: # Define requirements block.

    def change_location_action_requirements():
        return new_location is not mc.location

label store_change_location_actions(): # NOTE: Update this to always have vanilla functionality present. Any modifications e.g the followers_list are considered modifications and not to be put here.

    python:
        move_player_action = ActionMod("Moves the player", change_location_action_requirements, "move_player_label", priority = 0, allow_disable = False, menu_tooltip = "Moves the player to new location") # This is a vanilla action without any dependencies so it can run first.
        if move_player_action not in change_location_action_list:
            change_location_action_list.append(move_player_action)

    return

label move_player_label(): #NOTE: Upon returning to the game_loop it calls the change_location() function regardless so might consider overriding the game_loop too later on.
    $ mc.location = new_location
    return

label change_location_label(place):


    $ new_location = place

    $ change_location_count = 0
    $ change_location_max = len(change_location_action_list)
    $ change_location_action_list_sorted = sorted(change_location_action_list, key = lambda x: x.priority) # Execute actions in order of priority, from lowest to highest.

    while change_location_count < change_location_max:

        $ act = change_location_action_list[change_location_count]
        if act.is_action_enabled(): # Only run actions that have their requirement met.

            $ act.call_action()
            $ renpy.scene("Active")

        $ change_location_count += 1

    return mc.location # game_loop requires this to be provided.
