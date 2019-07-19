init 10 python:
    #add_label_hijack("normal_start", "activate_generic_personality")
    add_label_hijack("after_load", "label_override_actions_hook")

label label_override_actions_hook(stack):

    python:
        advance_time_action_list = [x for x in action_mod_list if x in advance_time_action_list]
    $ execute_hijack_call(stack)
    return
