init 5 python:
    add_label_hijack("normal_start", "activate_starbuck_mod_core")
    add_label_hijack("after_load", "update_starbuck_mod_core")

init -2 python:
    def SB_mod_setting_change_difficulty():
        if store.shop_difficulty_value == 1.0:
            store.shop_difficulty_value = 2.0
        elif store.shop_difficulty_value == 2.0:
            store.shop_difficulty_value = 0.5
        elif store.shop_difficulty_value == 0.5:
            store.shop_difficulty_value = 1.0
        return

    def SB_mod_setting_change_maximum_fetishes():
        if store.max_fetishes_per_person == 1:
            store.max_fetishes_per_person = 2
        elif store.max_fetishes_per_person == 2:
            store.max_fetishes_per_person = 3
        elif store.max_fetishes_per_person == 3:
            store.max_fetishes_per_person = 1
        return

    def SB_mod_setting_difficulty_name():
        if store.shop_difficulty_value == 2.0:
            return "Lucrative (Easy)"
        elif store.shop_difficulty_value == 1.0:
            return "Average (Normal)"
        else:
            return "Poor (Hard)"

    def SB_mod_setting_maximum_fetishes_name():
        return "Max " + str(store.max_fetishes_per_person) + " Fetishes per person"

    def SB_mod_change_action_mod_settings():
        tuple_list = []
        tuple_list.append(["Difficulty: " + SB_mod_setting_difficulty_name() + " (tooltip)Changes the return on investment you get from the sex shop.", "SB_mod_setting_change_difficulty"])
        tuple_list.append([SB_mod_setting_maximum_fetishes_name(), "SB_mod_setting_change_maximum_fetishes"])
        tuple_list.append(["Back","Back"])
        return renpy.display_menu(tuple_list, True, "Choice")


# TODO: Add difficulty configuration
label SB_mod_options_menu():
    python:
        action_mod_choice = SB_mod_change_action_mod_settings()
        if action_mod_choice == "Back":
            renpy.return_statement()
        globals()[action_mod_choice]()
    jump SB_mod_options_menu

label initialize_starbuck_configuration_values():
    $ store.shop_difficulty_value = 2.0
    $ store.max_fetishes_per_person = 3
    return

label activate_starbuck_mod_core(stack):
    call initialize_starbuck_configuration_values from _call_initialize_starbuck_configuration_values_1
    # continue on the hijack stack if needed
    $ execute_hijack_call(stack)
    return

label update_starbuck_mod_core(stack):
    python:
        if not hasattr(store, 'shop_difficulty_value'):
            renpy.call("initialize_starbuck_configuration_values")

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return
