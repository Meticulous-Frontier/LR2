# NOTE: Functions that cleanup Actions / Rooms / Personalities, Roles etc. that we no longer intend to support or want to have removed from the game.

init 5  python:

    #add_label_hijack("normal_start", "run_cleanup") # NOTE: Should only be relevant on loading existing saves.
    add_label_hijack("after_load", "run_cleanup")

init 2 python:

    def dungeon_room_collar_person_requirement(the_person):
        return False
    def dungeon_room_uncollar_person_requirement(the_person):
        return False

    def serum_mod_settings_requirement():
        return False

    def clean_elevator_action():
        if "room_manager_action" in globals():
            for room in list_of_places:
                if room_manager_action in room.actions:
                    room.actions.remove(room_manager_action)
        return

    def serum_action_cleanup():
        if "serum_mod_options_action" in globals():
            if serum_mod_options_action in bedroom.actions:
                bedroom.actions.remove(serum_mod_options_action)
        return
label run_cleanup(stack):

    $ clean_elevator_action()
    $ serum_action_cleanup()

    $ execute_hijack_call(stack)

    return
