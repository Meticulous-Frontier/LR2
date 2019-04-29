## Hijack Original Label
# If you want run your MOD label after an an in game label you just need to call
# the add_label_hijack method, since we store all hijacked labels, you can attach
# your code to any base game code, without changing the original game code.

init 2 python:
    hijack_list = []
    # Keep track of the old callback so it can still be called
    original_label_callback = config.label_callback
    # Hijack the config label callback function
    def hijack_label_callback(label, abnormal):
        # Make sure to call the original label callback too
        if not original_label_callback is None:
            original_label_callback(label, abnormal)

        # loop hijacked labels an jump to mod label
        for hijack in hijack_list:
            if label == hijack[0]:  # base game label called
                renpy.call(hijack[1])
            
    config.label_callback = hijack_label_callback
    
    def add_label_hijack(orginal_label_name, hijack_label_name):
        hijack_list.append([orginal_label_name, hijack_label_name])

    def remove_label_hijack(orginal_label_name):
        if orginal_label_name in hijack_list[0]:
            item_index = hijack_list[0].index(orginal_label_name)
            del hijack_list[item_index]


#label advance_time_extra:
#    "Testing hijack"
#    return

#init 200:
#    $ add_label_hijack("advance_time", "advance_time_extra")