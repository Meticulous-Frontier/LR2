init 2 python:
    def change_crisis_chance_requirement():
        return True

    change_crisis_chance_action = Action("Change Event Occurance", change_crisis_chance_requirement, "show_crisis_chance_ui", menu_tooltip = "Change how often events will occur in the game.")

init 5 python:
    add_label_hijack("normal_start", "activate_change_crisis_chance")  
    add_label_hijack("after_load", "update_change_crisis_chance")

label activate_change_crisis_chance(stack):
    python:
        bedroom.actions.append(change_crisis_chance_action)

        crisis_base_chance = 10
        morning_crisis_base_chance = 5

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_change_crisis_chance(stack):
    python:
        if not change_crisis_chance_action in bedroom.actions:
            bedroom.actions.append(change_crisis_chance_action)
            crisis_base_chance = 10
            morning_crisis_base_chance = 5

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label show_crisis_chance_ui():
    call screen crisis_chance_setting()
    $ crisis_chance = crisis_base_chance
    $ morning_crisis_chance = morning_crisis_base_chance
    return