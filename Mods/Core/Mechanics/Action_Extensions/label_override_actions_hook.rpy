init 10 python:
    #add_label_hijack("normal_start", "activate_generic_personality")
    add_label_hijack("after_load", "label_override_actions_hook")

    def update_advance_time_action_list():
        global advance_time_action_list
        for adv_time_action in advance_time_action_list:
            found = find_in_set(adv_time_action, ActionMod._instances)
            if found:
                try:
                    idx = action_mod_list.index(found)
                    found.enabled = action_mod_list[idx].enabled

                    # replace the one in the action_mod_list with the current action implementation from the instance list
                    action_mod_list[idx] = found
                except ValueError:
                    null

        # update the advance_time_action_list with the instances in the action_mod_list
        advance_time_action_list = [x for x in action_mod_list if x in advance_time_action_list]
        # sort list on execution priority
        advance_time_action_list.sort(key = lambda x: x.priority)
        return

label label_override_actions_hook(stack):
    python:
        # update actions in action mod list with the ones defined (in loaded instances)
        update_advance_time_action_list()
    $ execute_hijack_call(stack)
    return
