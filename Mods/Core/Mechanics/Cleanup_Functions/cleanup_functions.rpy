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

    def fix_breakup_action():
        if "ask_break_up_action" in globals():
            ask_break_up_action.effect = "ask_break_up_label"

    if config.version == "v0.22.0":
        if "girlfriend_role" not in globals():

            ask_break_up_action = Action("Break up with her.", ask_break_up_requirement, "ask_break_up_label", menu_tooltip = "Breaking up may break her heart, but it'll be easier on her than catching you with another woman.")

            girlfriend_role = Role("Girlfriend", [ask_break_up_action])

            plan_fuck_date_action = Action("Plan a fuck date at her place.", fuck_date_requirement, "plan_fuck_date_label", menu_tooltip = "Pick a night to go over there and spend nothing but \"quality time\" with each other.")
            ask_leave_SO_action = Action("Ask her to leave her significant other for you.", ask_leave_SO_requirement, "ask_leave_SO_label", menu_tooltip = "This affair has been secret long enough! Ask her to leave her significant other and make your relationship official.")
            affair_role = Role("Paramour", [plan_fuck_date_action, ask_leave_SO_action]) #A woman who is in a relationship but also wants to fuck you because of love (rather than pure sluttiness, where she thinks that's normal)

label run_cleanup(stack):

    $ clean_elevator_action()
    $ serum_action_cleanup()
    $ fix_breakup_action()

    $ execute_hijack_call(stack)

    return
